# CmdTranslate

Action

Apply a translation to the current matrix.

Syntax

CmdTranslate tx, ty 

Remarks

tx | x translate factor, in signed 16.16 bit fixed-point form  
---|---  
ty | y translate factor, in signed 16.16 bit fixed-point form  
  
Example

```vb
' Pseudocode

' To translate the bitmap 20 pixels to the right

```
Begin_G BITMAPS

CmdLoadIdentity

CmdTranslate 20 * 65536, 0

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0076](clip0076.png)

' To translate the bitmap 20 pixels to the left

Begin_G BITMAPS

CmdLoadIdentity

CmdTranslate -20 * 65536, 0

CmdSetMatrix

Vertex2II 68, 28, 0, 0

![clip0077](clip0077.png)