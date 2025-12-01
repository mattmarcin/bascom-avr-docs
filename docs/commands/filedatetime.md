# FILEDATETIME

Action

Returns the file date and time of a file

Syntax

Var = FILEDATETIME ()

Var = FILEDATETIME (file)

Remarks

Var | A string variable or byte array that is assigned with the file date and time of the specified file  
---|---  
File | The name of the file to get the date time of.  
  
When the target variable is a string, it must be dimensioned with a length of at least 17 bytes.

When the target variable is a byte array, the array size must be at least 6 bytes.

When you use a numeric variable, the internal file date and time format will be used.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileDateTimeS | _FileDateTimeS0  
---|---|---  
Input |  |   
Output |  |   
  
Calls | _FileDateTimeB | _FileDateTimeB0  
---|---|---  
Input |  |   
Output |  |   
  
Example

See fs_subfunc_decl_lib.bas in the samples dir.