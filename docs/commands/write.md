# WRITE

Action

Writes data to a sequential file

Syntax

WRITE #ch , data [,data1]

Remarks

Ch | A channel number, which identifies an opened file. This can be a hard coded constant or a variable.  
---|---  
Data , data1 | A variable whoâs content are written to the file.  
  
When you write a variables value, you do not write the binary representation but the ASCII representation. When you look in a file it contains readable text.

When you use PUT, to write binary info, the files are not readable or contain unreadable characters.

Strings written are surrounded by string delimiters "". Multiple variables written are separated by a comma. Consider this example :

Dim S as String * 10 , W as Word

S="hello" : W = 100

OPEN "test.txt" For OUTPUT as #1

WRITE #1, S , W

CLOSE #1

The file content will look like this : "hello",100

Use INPUT to read the values from value.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _FileWriteQuotationMark | _FileWriteDecInt  
---|---|---  
| _FileWriteDecByte | _FileWriteDecWord  
| _FileWriteDecLong | _FileWriteDecSingle  
Input | Z points to variable |   
Output |  |   
  
Partial Example

Dim S As String * 10 , W As Word , L As Long

S = "write"

Open "write.dmo"for Output As #2

Write #2 , S , W , L ' write is also supported

Close #2

Open "write.dmo"for Input As #2

Input #2 , S , W , L ' write is also supported

Close #2

Print S ; " " ; W ; " " ; L