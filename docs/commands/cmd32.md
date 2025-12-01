# CMD32

Action

This statement will send a dword to the FT800 graphic processor.

Syntax

CMD32 prm

Remarks

CMD32 expects a numeric parameter. It will call the _cmd32 assembled code in FT800.LIB

See also

[CMD8](cmd8.md) , [CMD16](cmd16.md) , [WR8](wr8.md) , [WR16](wr16.md) , [WR32](wr32.md)

Example

```vb
Sub Cmdnumber(bystack X As Integer , Bystack Y As Integer , Bystack Fontx As Integer , Bystack Options As Word , Bystack Num As Long)  
'------------------------------------------------------------------------------------------------------------  
' Draws a Decimal Number  
' No Justification = 0  
' OPT_CENTERX  
' OPT_CENTERY  
' OPT_CENTER  
' OPT_RIGHTX  
' OPT_SIGNED  
  
```
Cmd32 Cmd_number  
cmdftstack 12  
End Sub