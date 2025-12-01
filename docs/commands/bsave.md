# BSAVE

Action

Save a range in SRAM to a File

Syntax

BSave sFileName, wSRAMPointer, wLength

Remarks

sFileName | (String) Name of the File to be written  
---|---  
wSRAMPointer | (Word) Variable, which holds the SRAM Address, from where SRAM should be written to a File  
wLength | (Word) Count of Bytes from SRAM, which should be written to the file  
  
This function writes a range from the SRAM to a file. A free file handle is needed for this function.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _BSave |   
---|---|---  
Input | X: Pointer to string with filename | Z: Pointer to Long-variable, which holds the start position of SRAM  
| r20/r21: Count of bytes to be written |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Example

```vb
' THIS IS A CODE FRAGMENT, it needs AVR-DOS in order to work

'now the good old bsave and bload

Dim Ar(100)as Byte , I Asbyte

For I = 1 To 100

```
Ar(i) = I ' fill the array

```vb
Next

Wait 2

```
W = Varptr(ar(1))

Bsave"josef.img", W , 100

For I = 1 To 100

Ar(i) = 0 ' reset the array

Next

Bload "josef.img" , W ' Josef you are amazing !

```vb
For I = 1 To 10

Print Ar(i) ; " ";

Next

Print

```