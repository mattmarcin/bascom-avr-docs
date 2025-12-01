# FILETIME

Action

Returns the time of a file

Syntax

sTime = FILETIME ()

sTime = FILETIME (file)

Remarks

Stime | A string variable that is assigned with the file time.  
---|---  
File | The name of the file to get the time of.  
  
This function works on any file when you specify the filename. When you do not specify the filename, it works on the current selected file of the DIR() function.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileTimeS ; with file param | _FileTimeS0 ; current file  
---|---|---  
Input | X : points to the string with the mask | Z : points to the target variable  
Output |  |   
  
Example

```vb
Print "File demo"

Print Filelen("josef.img");" length" ' length of file

Print Filetime("josef.img");" time" ' time file was changed

Print Filedate("josef.img");" date" ' file date

```