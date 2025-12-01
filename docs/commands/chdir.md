# CHDIR

Action

This statement will change the current directory.

Syntax

CHDIR directory

Remarks

CHange DIRectory changes the current folder or directory.

The directory name must be a valid and existing folder or directory. Like in DOS, you can use ".." to go back one directory.

And you can use "\" to go to the root directory.

You can not specify a path.

You may can have multiple open files, and you could copy from one folder to another folder using the file handles. 

The DIR command and the OPEN command works in the current directory. IF you OPEN a file, the position (Sector# and position inside this sector) of the directory entry of the file is stored at the file-handle-part of that file. So you can move to another directory and OPEN there a second file an so on. In Short: Directory nesting is not limited and you can open files in multiple directories.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [WRITE](write.md) , [INPUT](input.md) , [DIR](dir.md), [MKDIR](mkdir.md), [RMDIR](rmdir.md), [NAME](name.md)

Example

MKDIR "abc"

CHDIR "abc"