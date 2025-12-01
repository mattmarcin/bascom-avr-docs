# FILELEN

Action

Returns the size of a file

Syntax

lSize = FILELEN ()

lSize = FILELEN (file)

Remarks

lSize | A Long Variable, which is assigned with the file size in bytes of the file.  
---|---  
File | A string or string constant to get the file length of.  
  
This function works on any file when you specify the filename. When you do not specify the filename, it works on the current selected file of the DIR() function.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileLen |   
---|---|---  
Input |  |   
Output |  |   
  
Partial Example

```vb
Print "File demo"

Print Filelen("josef.img");" length" ' length of file

Print Filetime("josef.img");" time" ' time file was changed

Print Filedate("josef.img");" date" ' file date

```