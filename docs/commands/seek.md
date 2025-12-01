# SEEK

Action

Function: Returns the position of the next Byte to be read or written

Statement: Sets the position of the next Byte to be read or written

Syntax

Function: NextReadWrite = SEEK (#bFileNumber)

Statement: SEEk #bFileNumber, NewPos

Remarks

bFileNumber | A byte holding the File number, which identifies a previous opened file  
---|---  
NextReadWrite | A Long Variable, which is assigned with the Position of the next Byte to be read or written (1-based). In case of an error, 0 is returned.  
NewPos | A Long variable that holds the new position the file pointer must be set to.  
  
This function returns the position of the next Byte to be read or written. 

Check DOS-Error in variable gbDOSError in case of an error, when the function returns a zero.

SEEK only works on files opened in BINARY mode. The SEEK() function returns 1 for an opened file since this is the start of the file. Once you write data to the file, SEEK() will return the updated location.

The statement also returns an error in the gbDOSerror variable in the event that an error occurs.

You can for example not set the file position behind the file.

In VB the file is filled with 0 bytes when you set the file pointer behind the size of the file. For embedded systems this does not seem a good idea.

Seek and Loc seems to do the same function, but take care : the seek function will return the position of the next read/write, while the Loc function returns the position of the last read/write. You may say that Seek = Loc+1.

![notice](notice.jpg) In QB/VB you can use seek to make the file bigger. When a file is 100 bytes long, setting the file pointer to 200 will increase the file with 0 bytes. By design this is not the case in AVR-DOS.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Function Calls | _FileSeek |   
---|---|---  
Input | r24: filenumber | X: Pointer to Long-variable, which gets the result  
Output | r25: Errorcode | C-Flag: Set on Error  
  
Statement Calls | _FileSeekSet |   
---|---|---  
Input | r24: filenumber | X: Pointer to Long-variable with the position  
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

Open "test.biN"for Binary As #2

Put#2 , B ' write a byte

Put#2 , W ' write a word

Put#2 , L ' write a long

Ltemp = Loc(#2) + 1 ' get the position of the next byte

```vb
Print Ltemp ; " LOC" ' store the location of the file pointer

Print Seek(#2) ; " = LOC+1"

```
Close #2

'now open the file again and write only the single

Open "test.bin" For Binary As #2

Seek#2 , Ltemp ' set the filepointer

Sn = 1.23 ' change the single value so we can check it better

Put #2 , Sn,1 ' specify the file position

Close #2

Example2

```vb
'------------------------------------------------------------------------------  
' simulate-AVR-DOS.bas  
' simulate AVR-DOS using virtual XRAM drive  
'  
'------------------------------------------------------------------------------  
$regfile = "M128def.dat"  
$crystal = 16000000  
' Adjust HW Stack, Soft-Stack and Frame size to 128 minimum each!!!  
$hwstack = 128 : $swstack = 128 : $framesize = 128  
$xramsize = &H10000 'specify 64KB of XRAM for the file system  
$sim 'for simulation only !  
$baud = 19200  
  
Config Clock = Soft  
Enable Interrupts  
Config Date = Mdy , Separator = Dot  
  
Dim Btemp1 As Byte , Battr1 As Byte , Battr2 As Byte  
$include "Config_XRAMDrive.bas" ' Does drive init too  
$include "Config_AVR-DOS.BAS"  
  
Print "Wait for Drive"  
If Gbdriveerror = 0 Then  
Print "Init File System ... ";  
```
Btemp1 = Initfilesystem(1) ' Partition 1  
```vb
' use 0 for drive without Master boot record  
If Btemp1 <> 0 Then  
Print "Error: " ; Btemp1 ; " at Init file system"  
Else  
Print " OK"  
Print "Filesystem: " ; Gbfilesystem  
Print "FAT Start Sector: " ; Glfatfirstsector  
Print "Root Start Sector: " ; Glrootfirstsector  
Print "Data First Sector: " ; Gldatafirstsector  
Print "Max. Cluster Nummber: " ; Glmaxclusternumber  
Print "Sectors per Cluster: " ; Gbsectorspercluster  
Print "Root Entries: " ; Gwrootentries  
Print "Sectors per FAT: " ; Glsectorsperfat  
Print "Number of FATs: " ; Gbnumberoffats  
End If  
Else  
Print "Error during Drive Init: " ; Gbdriveerror  
End If  
  
Dim Lpos As Long  
```
Open "test.bin" For Binary As #11  
Print Seek(#11) ' 1  
Put #11 , Btemp1  
Print Seek(#11) ' 2  
Lpos = Lof(#11) + 1 ' 1+1=2  
Seek #11 , Lpos  
Put #11 , Btemp1  
Print Seek(#11) '3  
Close #11  
  
End