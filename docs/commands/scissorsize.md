# ScissorSize

Action

Specify the size of the scissor clip rectangle.

Syntax

ScissorSize width, height

Remarks

width | The width of the scissor clip rectangle, in pixels. The initial value is 512. The valid value range is from 0 to 512.  
---|---  
height | The height of the scissor clip rectangle, in pixels. The initial value is 512. The valid value range is from 0 to 512  
  
Sets the width and height of the scissor clip rectangle, which limits the drawing area.

See Also

[SCISSORXY](scissorxy.md)

Example

```vb
' Pseudocode

' Setting a 40 x 30 scissor rectangle clips the clear and bitmap drawing

```
ScissorXY 40, 30

ScissorSize 80, 60

ClearColorRGB 0, 0, 255

Clear_B 1, 1, 1

Begin_G BITMAPS

Vertex2II 35, 20, 31, &H47

![clip0084](clip0084.png)