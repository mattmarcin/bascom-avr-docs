# PUT

Action

Writes a byte to the hardware or software UART.

Writes data to a file opened in BINARY mode.

Syntax

PUT #channel, var

PUT #channel, var ,[pos] [,length]

Remarks

PUT in combination with the software/hardware UART is provided for compatibility with BASCOM-8051. It writes one byte

PUT in combination with the AVR-DOS file system is very flexible and versatile. It works on files opened in BINARY mode and you can write all data types.

#channel | A channel number, which identifies an opened file. This can be a hard coded constant or a variable.  
---|---  
Var | The variable or variable array that will be written to the file  
Pos | This is an optional parameter that may be used to specify the position where the data must be written. This must be a long variable.  
Length | This is an optional parameter that may be used to specify how many bytes must be written to the file.  
  
By default you only need to provide the variable name. When the variable is a byte, 1 byte will be written. When the variable is a word or integer, 2 bytes will be written. When the variable is a long or single, 4 bytes will be written. When the variable is a string, the number of bytes that will be written is equal to the dimensioned size of the string. DIM S as string * 10 , would write 10 bytes.

Note that when you specify the length for a string, the maximum length is 255. The maximum length for a non-string array is 65535.

Example

PUT #1, var

PUT #1, var , , 2 ' write 2 bytes at default position

PUT #1, var ,PS, 2 ' write 2 bytes at location storied in variable PS

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md), [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md), [AVR-DOS File system](avr_dos_file_system.md)

ASM

current position | Goto new position first  
---|---  
Byte: |   
_FilePutRange_1 Input: r24: File number X: Pointer to variable T-Flag cleared | _FilePutRange_1 Input: r24: File number X: Pointer to variable r16-19 (A): New position (1-based) T-Flag Set  
Word/Integer: |   
_FilePutRange_2 Input: r24: File number X: Pointer to variable T-Flag cleared | _FilePutRange_2 Input: r24: File number X: Pointer to variable r16-19 (A): New position (1-based) T-Flag Set  
Long/Single: |   
_FilePutRange_4 Input: r24: File number X: Pointer to variable T-Flag cleared | _FilePutRange_4 Input: r24: File number X: Pointer to variable r16-19 (A): New position (1-based) T-Flag Set  
String (<= 255 Bytes) with fixed length |   
_FilePutRange_Bytes Input: r24: File number r20: Count of Bytes X: Pointer to variable T-Flag cleared | _FilePutRange_Bytes Input: r24: File number r20: Count of bytes X: Pointer to variable r16-19 (A): New position (1-based) T-Flag Set  
Array (> 255 Bytes) with fixed length |   
_FilePutRange Input: r24: File number r20/21: Count of Bytes X: Pointer to variable T-Flag cleared | _FilePutRange Input: r24: File number r20/21: Count of bytes X: Pointer to variable r16-19 (A): New position (1-based) T-Flag Set  
  
Output from all kind of usage:

r25: Error Code

C-Flag on Error

Example

```vb
'for the binary file demo we need some variables of different types  
Dim B As Byte, W As Word, L As Long, Sn As Single, Ltemp As Long  
Dim Stxt As String* 10  
```
B = 1 : W = 50000 : L = 12345678 : Sn = 123.45 : Stxt ="test"  
  
'open the file in BINARY mode  
Open "test.biN" For Binary As#2  
Put#2 , B ' write a byte  
Put#2 , W ' write a word  
Put#2 , L ' write a long  
Ltemp =Loc(#2)+ 1 ' get the position of the next byte  
```vb
Print Ltemp ;" LOC"' store the location of the file pointer  
Print Seek(#2);" = LOC+1"  
  
Print Lof(#2);" length of file"  
Print Fileattr(#2);" file mode"' should be 32 for binary  
```
Put#2 , Sn ' write a single  
Put#2 , Stxt ' write a string  
  
Flush#2 ' flush to disk  
Close#2  
  
'now open the file again and write only the single  
Open "test.bin" For Binary As #2  
L = 1 'specify the file position  
B =Seek(#2 , L) ' reset is the same as using SEEK #2,L  
Get#2 , B ' get the byte  
Get#2 , W ' get the word  
Get#2 , L ' get the long  
Get#2 , Sn ' get the single  
Get#2 , Stxt ' get the string  
Close#2