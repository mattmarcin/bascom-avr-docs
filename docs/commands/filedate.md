# FILEDATE

Action

Returns the date of a file

Syntax

sDate = FILEDATE ()

sDate = FILEDATE (file)

Remarks

Sdate | A string variable that is assigned with the date.  
---|---  
File | The name of the file to get the date of.  
  
This function works on any file when you specify the filename. When you do not specify the filename, it works on the current selected file of the DIR() function.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md), [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileDateS ; with filename | _FileDateS0 ; for current file from DIR()  
---|---|---  
Input | X : points to the string with the mask | Z : points to the target variable  
Output |  |   
  
Partial Example

```vb
Print "File demo"

Print Filelen("josef.img");" length" ' length of file

Print Filetime("josef.img");" time" ' time file was changed

Print Filedate("josef.img");" date" ' file date

```