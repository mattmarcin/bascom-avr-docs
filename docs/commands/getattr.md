# GETATTR

Action

Returns the file Attribute.

Syntax

bFileAttribut = GETATTR([sFile])

Remarks

bFileAttribut | Numeric variable which is assigned with the file attribute.  
---|---  
sFile | The name of the file (no wildcard) to get the attribute from. You may also omit the name in which case the file will be used previous found by the DIR() function.  
  
This functions returns the DOS file attributes. A file can have multiple attributes.

Return value | DOS Attribute  
---|---  
1 | Read Only  
2 | Hidden  
4 | System File  
8 | Volume Label  
16 | Sub Directory  
32 | Archive  
64,128 | reserved  
  
A file could have an attribute of 3 (hidden+ read only).

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md), [WRITE](write.md) , [INPUT](input.md) , [FILEATTR](fileattr.md)

Partial Example

```vb
'open the file in BINARY mode

Print Getattr("somefile.bin")

```