# LOF

Action

Returns the length of the File in Bytes

Syntax

lFileLength = LOF (#bFileNumber)

Remarks

bFileNumber | (Byte) Filenumber, which identifies an opened file  
---|---  
LFileLength | (Long) Variable, which assigned with the Length of the file (1-based)  
  
This function returns the length of an opened file. If an error occurs, 0 is returned. Check DOS-Error in variable gbDOSError.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileLOF |   
---|---|---  
Input | r24: filenumber | X: Pointer to Long-variable, which gets th result  
Output | r25: Errorcode | C-Flag: Set on Error  
  
Example

' open the file in BINARY mode

Open "test.bin" For Binary As #2

Put #2 , B ' write a byte

Put #2 , W ' write a word

Put #2 , L ' write a long

Ltemp = Loc(#2)+ 1 ' get the position of the next byte

```vb
Print Ltemp ;" LOC" ' store the location of the file pointer

Print Lof(#2);" length of file"

Print Fileattr(#2);" file mode" ' should be 32 for binary

```
Put #2 , Sn ' write a single

Put #2 , Stxt ' write a string

Flush #2 ' flush to disk

Close #2