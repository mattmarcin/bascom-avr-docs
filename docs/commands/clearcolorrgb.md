# ClearColorRGB

Action

Specify the clear values for Red, Green and Blue channels.

Syntax

ClearColorRGB Red, Green, Blue

Remarks

Red | Red value used when the color buffer is cleared. The initial value is 0  
---|---  
Green | Green value used when the color buffer is cleared. The initial value is 0  
Blue | Blue value used when the color buffer is cleared. The initial value is 0  
  
Sets the color values used by a following [Clear_B](clear_b.md)

See also

[ClearColorA](clearcolora.md), [Clear_B](clear_b.md) , [ClearColorRGBdw](clearcolorrgbdw.md)

Example

```vb
' Pseudocode

' To clear the screen to bright blue:

```
ClearColorRGB 0, 0, 255

Clear_B 1, 1, 1

![clip0101](clip0101.png)

' To clear part of the screen to gray, part to blue using scissor rectangles:

ClearColorRGB 100, 100, 100

Clear_B 1, 1, 1

ClearColorRGB 0, 0, 255

ScissorScize 30, 120

Clear_B 1, 1, 1

![clip0100](clip0100.png)