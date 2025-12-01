# SETATTR

Action

Sets the file Attribute.

Syntax

SETATTR [sFile ,] bFileAttribute

Remarks

sFile | The name of the file (no wildcard) which attribute need to be set. You may also omit the name in which case the file will be used previous found by the DIR() function.  
---|---  
bFileAttribute | Numeric variable holding the attribute bits to set.  
  
This statement sets the DOS file attributes. A file can have multiple attributes.

You should not use attributes 8(Volume) and 16(Sub Directory) on a normal file. 

Return value | DOS Attribute  
---|---  
1 | Read Only  
2 | Hidden  
4 | System File  
8 | Volume Label  
16 | Sub Directory  
32 | Archive  
64,128 | reserved  
  
A file can have multiple bits set like 3 (hidden + read only). So you can combine multiple bits to set multiple bits at once.

When you specify the filename, make sure it does not have a wildcard. SETATTR does not support wildcards.

When you omit the filename, the last found file from [DIR](dir.md)() will be used for the operation.

In VB, SETATTR expect a new value for the attribute which replaces the old attribute byte.

In AVR-DOS you specify the bits to set. So old attributes are kept. 

In AVR-DOS you can also reset the individual bits using the CLEARATTR statement.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md), [WRITE](write.md) , [INPUT](input.md) , [FILEATTR](fileattr.md) , [CLEARATTR](clearattr.md) , [GETATTR](getattr.md)

Example

```vb
'------------------------------------------------------------------------------  
' simulate-AVR-DOS.bas  
' simulate AVR-DOS using virtual XRAM drive  
'  
'------------------------------------------------------------------------------  
$regfile = "M128def.dat"  
$crystal = 16000000  
' Adjust HW Stack, Soft-Stack and Frame size to 128 minimum each!!!  
$hwstack=128 : $swstack=128 : $framesize=128  
$xramsize = &H10000 'specify 64KB of XRAM for the file system  
$sim 'for simulation only !  
$baud = 19200  
  
Config Clock = Soft  
Enable Interrupts  
Config Date = Mdy , Separator = dot  
  
Dim Btemp1 As Byte ,battr1 as Byte, battr2 as Byte  
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
  
Dim strDummy as String * 12  
Dim Datei As String * 12 , Attribut As Byte  
```
Datei = "Test1.txt"  
  
Open Datei For Output As #11  
Print #11 , "Testzeile1"  
Close #11  
  
open "Test2.txt" For output as #11  
Print #11, "Testzeile2"  
close #11  
  
open "Test3.txt" for output as #11  
Print #11, "Testzeile3"  
close #11  
  
  
' Set readonly Bit in Test1.txt  
Attribut = &B00000001  
Setattr Datei , Attribut  
  
' Reset Archib-Bit in test1.txt  
Attribut = &B00100000  
clearattr Datei , Attribut  
  
```vb
' Check for Filename with wildcard, which is not supported  
' Set readonly Bit in Test1.txt  
```
Datei = "Test*.txt"  
Attribut = &B00000001  
Setattr Datei , Attribut  
Print gbDOSError  
  
Datei = DIR("Test*.txt")  
Attribut = &B00000001  
while Datei > ""  
SetAttr Attribut  
Datei = DIR()  
wend  
  
Datei = DIR("Test*.txt")  
Attribut = &B00100000  
While Datei > ""  
battr1=Getattr()  
clearattr Attribut  
battr2=Getattr()  
print datei ;" "; battr1;" " ; battr2  
Datei = DIR()  
```vb
wend  
  
End

```