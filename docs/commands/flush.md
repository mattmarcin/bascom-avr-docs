# FLUSH

Action

Write current buffer of File to Card and updates Directory

Syntax

FLUSH #bFileNumber

FLUSH

Remarks

BFileNumber | Filenumber, which identifies an opened file such as #1 or #ff  
---|---  
  
This function writes all information of an open file, which is not saved yet to the Disk. Normally the Card is updated, if a file will be closed or changed to another sector.

When no file number is specified, all open files will be flushed.

Flush does not need additional buffers. You could use FLUSH to be absolutely sure that data is written to the disk. For example in a data log application which is updated infrequently. A power failure could result in a problem when there would be data in the buffer. 

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileFlush | _FilesAllFlush  
---|---|---  
Input | r24: filenumber |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

```vb
$include "startup.inc"

'open the file in BINARY mode

```
Open "test.bin" For Binary As #2

Put #2 , B ' write a byte

Put #2 , W ' write a word

Put #2 , L ' write a long

Ltemp = Loc(#2) + 1 ' get the position of the next byte

```vb
Print Ltemp ;" LOC" ' store the location of the file pointer

Print Lof(#2);" length of file"

Print Fileattr(#2);" file mode" ' should be 32 for binary

```
Put #2 , Sn ' write a single

Put #2 , Stxt ' write a string

Flush #2 ' flush to disk

Close #2