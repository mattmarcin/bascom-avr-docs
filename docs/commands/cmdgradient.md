# CmdGradient

Action

Draw a smooth color gradient.

Syntax

CmdGradient x0, y0, rgb0, x1, y1, rgb1

Remarks

x0 | x-coordinate of point 0, in pixels  
---|---  
y0 | y-coordinate of point 0, in pixels  
rgb0 | Color of point 0, as a 24-bit RGB number. r is the most significant 8 bits, b is the least. So &hff0000 is bright red.  
x1 | x-coordinate of point 1, in pixels  
y1 | y-coordinate of point 1, in pixels  
rgb1 | Color of point 1.  
  
All the colour step values are calculated based on smooth curve interpolated from the rgb0 to rgb1 parameter. 

The smooth curve equation is independently calculated for all three colors and the equation used is R0 + t * (R1 - R0), where t is interpolated between 0 and 1. 

Gradient must be used with Scissor function to get the intended gradient display

Example

' Pseudocode

ClearScreen  
ColorRGB 255, 255, 255  
ScissorSize wScissor, hScissor  
' Horizontal gradient effect  
ScissorXY xOffset, yOffset ' Clip the Display  
CmdGradient xOffset, yOffset, &H808080, xOffset + wScissor, yOffset, &HFFFF00

Example

```vb
' Pseudocode

' A horizontal gradient from blue to red

```
CmdGradColor 0, 0, &H0000ff, 160, 0, &Hff0000

![clip0020](clip0020.png)

' A vertical gradient

CmdGradColor 0, 0, &H808080, 0, 120, &H80ff40

![clip0021](clip0021.png)

' The same colors in a diagonal gradient

CmdGradColor 0, 0, &H808080, 160, 120, &H80ff40

![clip0023](clip0023.png)

'Using a scissor rectangle to draw a gradient stripe as a background for a title

ScissorXY 20, 40

ScissorSize 120, 32

CmdGradient 20, 0, &H606060, 140, 0, &H404080

CmdText 23, 40, 29, 0, "Heading 1"

![clip0022](clip0022.png)