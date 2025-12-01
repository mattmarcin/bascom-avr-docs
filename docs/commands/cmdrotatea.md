# CmdRotateA

Action

Apply a rotation in degrees to the current matrix

Syntax

CmdRotateA angle

Remarks

angle | Clockwise rotation angle, in degrees (0-360)  
---|---  
  
See Also

[CMDROTATE](cmdrotate.md)

Example

```vb
' Pseudocode

' To rotate the bitmap clockwise by 10 degrees with respect to the top left of the bitmap

```
Begin_G BITMAPS

CmdLoadIdentity

CmdRotate 10 

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0046](clip0046.png)

' To rotate the bitmap counter clockwise by 33 degrees top left of the bitmap

Begin_G BITMAPS

CmdLoadIdentity

CmdRotate -33 

CmdSetMatrix

Vertex2II 68, 28, 0, 0

' Rotating a 64 x 64 bitmap around its center

Begin_G BITMAPS

CmdLoadIdentity

CmdTranslate 65536 * 32, 65536 * 32

CmdRotate 90 

CmdTranslate 65536 * -32, 65536 * -32

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0047](clip0047.png)