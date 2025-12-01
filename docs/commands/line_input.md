# LINEINPUT

Action

Read a Line from an opened File.

Syntax

LINEINPUT #bFileNumber, sLineText

LINE_INPUT #bFileNumber, sLineText

Remarks

BfileNumber | (Byte) File number, which identifies an opened file  
---|---  
SlineText | (String) A string, which is assigned with the next line from the file.  
  
Only valid for files opened in mode INPUT. Line INPUT works only with strings. It is great for working on text files.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileLineInput |   
---|---|---  
Input | r24: filenumber | X: Pointer to String to be written from file  
| r25: Stringlength |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Example

'Ok we want to check if the file contains the written lines

Ff = Freefile()' get file handle

Open "test.txt" For Input As #ff ' we can use a constant for the file too

```vb
Print Lof(#ff); " length of file"

Print Fileattr(#ff); " file mode" ' should be 1 for input

Do

```
LineInput #ff , S ' read a line

```vb
' line input is used to read a line of text from a file

Print S ' print on terminal emulator

Loop Until Eof(ff)<> 0

'The EOF() function returns a non-zero number when the end of the file is reached

'This way we know that there is no more data we can read

```
Close #ff