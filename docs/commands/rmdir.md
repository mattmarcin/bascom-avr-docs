# RMDIR

Action

This statement removes the specified directory.

Syntax

RMDIR directory

Remarks

RMDIR (ReMove DIRectory) removes the specified directory or folder.

The folder must exist. You may not use a path.

While KILL is used to remove files, RMDIR is used to remove directories. 

You should remove all files before you remove the directory.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [WRITE](write.md) , [INPUT](input.md) , [DIR](dir.md), [MKDIR](mkdir.md), [CHDIR](chdir.md) , [NAME](name.md)

Example

RMDIR "abc"