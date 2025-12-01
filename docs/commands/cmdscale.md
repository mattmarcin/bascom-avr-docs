# CmdScale

Action

Apply a scale to the current matrix.

Syntax

CmdScale sx, sy 

Remarks

sx | x scale factor, in signed 16. 16 bit fixed-point form  
---|---  
sy | y scale factor, in signed 16. 16 bit fixed-point form  
  
Example

```vb
' Pseudocode

' To zoom a bitmap 2X

```
Begin_G BITMAPS

CmdLoadIdentity

CmdScale 2 * 65536, 2 * 65536

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0048](clip0048.png)

' To zoom a bitmap 2X around its center

Begin_G BITMAPS

CmdLoadIdentity

CmdTranslate 65536 * 32, 65536 * 32

CmdScale 2 * 65536, 2 * 65536

CmdTranslate 65536 * -32, 65536 * -32

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0049](clip0049.png)