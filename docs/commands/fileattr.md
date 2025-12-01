# FILEATTR

Action

Returns the file open mode.

Syntax

bFileAttribut = FILEATTR(bFileNumber)

Remarks

bFileAttribut | (Byte) File open mode, See table  
---|---  
bFileNumber | (Byte) Number of the opened file  
  
This functions returns information about the File open mode

Return value | Open mode  
---|---  
1 | INPUT  
2 | OUTPUT  
8 | APPEND  
32 | BINARY  
  
See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md), [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md), [WRITE](write.md) , [INPUT](input.md) , [GETATTR](getattr.md)

ASM

Calls | _FileAttr |   
---|---|---  
Input | r24: Filenumber |   
Output | 24: File open mode | r25: Errorcode  
| C-Flag: Set on Error |   
  
Partial Example

'open the file in BINARY mode

Open "test.biN" For Binary As #2

Print Fileattr(#2); " file mode" ' should be 32 for binary

Put #2 , Sn ' write a single

Put #2 , Stxt ' write a string

Close #2