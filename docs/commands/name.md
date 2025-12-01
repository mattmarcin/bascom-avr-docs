# NAME

Action

This AVR-DOS statement renames a file or directory name.

Syntax

NAME old AS new

Remarks

old | The name of the file or folder that you want to rename. This file must exist in the current folder.  
---|---  
new | The new name of the file. The new file may not already exist. The current folder will be used.  
  
Both old and new must be valid file names and of the string data type. Constants are not allowed.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [WRITE](write.md) , [INPUT](input.md) , [DIR](dir.md), [MKDIR](mkdir.md), [RMDIR](rmdir.md), [CHDIR](chdir.md)

Example

Old = "file1.txt"

New = "fileNew.txt"

NAME old AS new