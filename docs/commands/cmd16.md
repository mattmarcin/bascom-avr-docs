# CMD16

Action

This statement will send a word to the FT800 graphic processor.

Syntax

CMD16 prm

Remarks

CMD16 expects a numeric parameter. It will call the _cmd16 assembled code in FT800.LIB

See also

[CMD8](cmd8.md) , [CMD32](cmd32.md) , [WR8](wr8.md) , [WR16](wr16.md) , [WR32](wr32.md)

Example  
```vb
Sub Cmdprogress(bystack X As Integer , Bystack Y As Integer , Bystack W As Integer , Bystack H As Integer , Bystack Options As Word , Bystack Value As Word , Bystack Range As Word)  
  
' Draws a Progress Bar  
  
' Options Are  
' OPT_3D = 0  
' OPT_FLAT  
  
```
Cmd32 Cmd_progress  
cmdftstack 14  
Cmd16 &H0000  
  
```vb
' was a total of 18 bytes, to align with 4byte boundary it had to be offset of 20  
End Sub

```