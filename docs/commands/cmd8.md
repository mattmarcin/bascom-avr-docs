# CMD8

Action

This statement will send a byte to the FT800 graphic processor.

Syntax

CMD8 prm

Remarks

CMD8 expects a numeric parameter. It will call the _cmd8 assembler code in FT800.LIB

See also

[CMD16](cmd16.md) , [CMD32](cmd32.md) , [WR8](wr8.md) , [WR16](wr16.md) , [WR32](wr32.md)

Example

Sub Cmdinflatex(byval Ptr As Dword , Byref Varaddress As Word , Byval Count As Dword)  
  
Local Length As Dword  
  
Cmd32 Cmd_inflate  
Cmd32 Ptr  
  
For Length = 1 To Count  
Tb = Cpeek(varaddress)  
Cmd8 Tb  
Incr Varaddress  
Next  
  
Alignfifo Count  
  
End Sub