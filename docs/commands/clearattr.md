# CLEARATTR

Action

Clears the file Attribute.

Syntax

CLEARATTR [sFile] , bFileAttribute

Remarks

sFile | The name of the file (no wildcard) which attribute need to be cleared. You may also omit the name in which case the file will be used previous found by the DIR() function.  
---|---  
bFileAttribute | Numeric variable holding the attribute bits to clear.  
  
This functions clears the DOS file attributes. A file can have multiple attributes.

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
  
A file can have multiple bits set like 3 (hidden + read only). So you can clear multiple bits by combining the bits.

When you specify the filename, make sure it does not have a wildcard. CLEARTTR does not support wildcards.

When you omit the filename, the last found file from [DIR](dir.md)() will be used for the operation.

In VB, CLEARATTR expects a new value for the attribute which replaces the old attribute byte.

In AVR-DOS you specify the bits to clear. So old attribute bits which are not altered are kept. 

In AVR-DOS you can also set the individual bits using the SETRATTR statement.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md), [WRITE](write.md) , [INPUT](input.md) , [FILEATTR](fileattr.md) , [SETATTR](setattr.md) , [GETATTR](getattr.md)

Example

See [SETATTR](setattr.md)