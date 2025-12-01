# EOF

Action

Returns the End of File Status.

Syntax

bFileEOFStatus = EOF(#bFileNumber)

Remarks

bFileEOFStatus | (Byte) A Byte Variable, which assigned with the EOF Status  
---|---  
bFileNumber | (Byte) Number of the opened file  
  
This functions returns information about the End of File Status

Return value | Status  
---|---  
0 | NOT EOF  
255 | EOF  
  
In case of an error (invalid file number) 255 (EOF) is returned too.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileEOF |   
---|---|---  
Input | r24: Filenumber |   
Output | r24: EOF Status | r25: Error code  
| C-Flag: Set on Error |   
  
Partial Example

Ff =Freefile()' get file handle

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

Loop Until Eof(#ff)<> 0

'The EOF() function returns a non-zero number when the end of the file is reached

'This way we know that there is no more data we can read

```
Close #ff