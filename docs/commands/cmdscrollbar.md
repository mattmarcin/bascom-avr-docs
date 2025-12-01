# CmdScrollBar

Action

Draw a scroll bar.

Syntax

CmdScrollBar x, y, w, h, options, val, range, size, range

Remarks

x | x-coordinate of scroll bar top-left, in pixels  
---|---  
y | y-coordinate of scroll bar top-left, in pixels  
w | Width of scroll bar, in pixels. If width is greater than height, the scroll bar is drawn horizontally  
h | Height of scroll bar, in pixels. If height is greater than width, the scroll bar is drawn vertically  
options | By default the scroll bar is drawn with a 3D effect and the value of options is zero.  Options OPT_FLAT removes the 3D effect and its value is 256  
val | Displayed value of scroll bar, between 0 and range inclusive range  
range | Maximum value  
  
Example

```vb
' Pseudocode

' A scroll bar indicating 10-50%

```
CmdScrollBar 20, 50, 120, 8, 0, 10, 40, 100

![clip0050](clip0050.png)

' Without the 3D look

CmdScrollBar 20, 50, 120, 8, OPT_FLAT, 10, 40, 100

![clip0051](clip0051.png)

' A brown-themed vertical scroll bar

CmdBgColor &H402000

CmdFgColor &H703800

CmdScrollBar 140, 10, 8, 100, 0, 10, 40, 100

![clip0052](clip0052.png)