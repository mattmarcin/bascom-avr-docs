# LineWidth

Action

Specify the width of lines to be drawn with primitive LINES in 1/16th pixel precision.

Syntax

LineWdth width

Remarks

width | Line width in 1/16 pixel. The initial value is 16, range is 16 to 4095  
---|---  
  
Sets the width of drawn lines. The width is the distance from the center of the line to the outermost drawn pixel, in units

of 1/16 pixel. The valid range is from 16 to 4095 in terms of 1/16th pixel units.

Please note the LineWidth command will affect the LINES, LINE_STRIP, RECTS, EDGE_STRIP_A/B/R/L primitives.

Example

```vb
' Pseudocode

' The second line is drawn with a width of 80, for a 5 pixel radius

```
Begin_G LINES

Vertex2F 16 * 10, 16 * 30 

Vertex2F 16 * 150, 16 * 40

LineWidth 80

Vertex2F 16 * 10, 16 * 80

Vertex2F 16 * 150, 16 * 90

![clip0081](clip0081.png)