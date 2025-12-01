# PointSize

Action

Specify the radius of points.

Syntax

PointSize size

Remarks

size | Point radius in 1/16 pixel. range 16 to 8191, the initial value is 16   
---|---  
  
Sets the size of drawn points. The width is the distance from the center of the point to the outermost drawn pixel, in

units of 1/16 pixels. The valid range is from 16 to 8191 with respect to 1/16th pixel unit.

Example

```vb
' Pseudocode

' The second point is drawn with a width of 160, for a 10 pixel radius

```
Begin_G FTPOINTS

Vertex2II 40, 30, 0, 0

PointSize 160

Vertex2II 120, 90, 0, 0

![clip0082](clip0082.png)