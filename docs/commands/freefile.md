# FREEFILE

Action

Returns a free Filenumber.

Syntax

bFileNumber = FREEFILE()

Remarks

bFileNumber | A byte variable , which can be used for opening next file  
---|---  
  
This function gives you a free file number, which can be used for file â opening statements. In contrast to VB this file numbers start with 128 and goes up to 255. Use range 1 to 127 for user defined file numbers to avoid file number conflicts with the system numbers from FreeFile()

This function is implemented for compatility with VB.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _GetFreeFileNumber |   
---|---|---  
Input | none |   
Output | r24: Filenumber | r25: Errorcode  
| C-Flag: Set on Error |   
  
Partial Example

Ff =Freefile() ' get file handle

Open"test.txt" For Input As #ff ' we can use a constant for the file too

```vb
Print Lof(#ff);" length of file"

Print Fileattr(#ff);" file mode" ' should be 1 for input

Do

```
LineInput #ff , S ' read a line

```vb
' line input is used to read a line of text from a file

Print S ' print on terminal emulator

Loop UntilEof(ff)<> 0

'The EOF() function returns a non-zero number when the end of the file is reached

'This way we know that there is no more data we can read

```
Close #ff