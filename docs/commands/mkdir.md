# MKDIR

Action

This statement creates a folder or directory in the current directory.

Syntax

MKDIR directory

Remarks

MaKeDIRectory creates a folder or directory in the current directory.

The directory may not have a device name like COM1, LPT1, etc.

The directory may also not have a name like ".." or "\" since these names are reserved.

You can not create a directory using a path.

MKDIR "test" ' ok

MKDIR "test\abc" ' NOT OK

MKDIR ".." ' NOT OK

MKDIR "\" ' NOT OK

MKDIR "test" : CHDIR "test" : MKDIR "abc" ' this would create test\abc

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [WRITE](write.md) , [INPUT](input.md) , [DIR](dir.md), [RMDIR](rmdir.md) , [CHDIR](chdir.md) , [NAME](name.md)

Example

MKDIR "test"