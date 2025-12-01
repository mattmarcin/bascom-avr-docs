# DIR

Action

Returns the filename that matches the specified file mask.

Syntax

sFile = DIR(mask)

sFile = DIR()

Remarks

SFile | A string variable that is assigned with the filename.  
---|---  
Mask | A file mask with a valid DOS file mask like *.TXT Use *.* to select all files.  
  
The first function call needs a file mask. All other calls do not need the file mask. In fact when you want to get the next filename from the directory, you must not provide a mask after the first call.

Dir() returns an empty string when there are no more files or when no file name is found that matches the mask.

![notice](notice.jpg)You should not use directory/file manipulation functions between DIR(mask) and DIR(). This because the first use of DIR() with a mask will search the FAT and will set up a pointer to this table. The next use of DIR() will continue to search the next match. But when you change the directory, or create a file or directory the pointer will be lost.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILELEN](filelen.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [WRITE](write.md) , [INPUT](input.md) , [MKDIR](mkdir.md), [RMDIR](rmdir.md) , [CHDIR](chdir.md)

ASM

Calls | _Dir ; with file mask | _Dir0 ; without file mask  
---|---|---  
Input | X : points to the string with the mask | Z : points to the target variable  
Output |  |   
  
Partial Example

```vb
'Lets have a look at the file we created

Print "Dir function demo"

```
S = Dir("*.*")

```vb
'The first call to the DIR() function must contain a file mask

' The * means everything.

'

While Len(s)> 0 ' if there was a file found

Print S ;" ";Filedate();" ";Filetime();" ";Filelen()

' print file , the date the fime was created/changed , the time and the size of the file

```
S = Dir()' get next

Wend