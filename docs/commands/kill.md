# KILL

Action

Delete a file from the Disk

Syntax

KILL sFileName

Remarks

sFileName | A String variable or string expression, which denotes the file to delete  
---|---  
  
This function deletes a file from the disk. A file in use can't be deleted. WildCards in Filename are not supported. Check the DOS-Error in variable gDOSError.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _DeleteFile |   
---|---|---  
Input | X: Pointer to string with filename |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

```vb
'We can use the KILL statement to delete a file.

'A file mask is not supported

Print "Kill (delete) file demo"

```
Kill "test.txt"