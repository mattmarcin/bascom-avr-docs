# VER

Action

Returns the AVR-DOS version

Syntax

result = VER()

Remarks

Result | A numeric variable that is assigned with the AVR-DOS version. The version number is a byte and the first release is version 1.  
---|---  
  
When you have a problem, MCS can ask you for the AVR-DOS version number. The VER() function can be used to return the version number then.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

![notice](notice.jpg)The [VERSION](version.md)() function is something different. It is intended to include compile time info into the program.

ASM

Calls | _AVRDOSVer  
---|---  
|   
Input | -  
Output | R16 loaded with value  
  
Example

Print Ver()