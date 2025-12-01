# CmdSlider

Action

Draw a slider.

Syntax

CmdSlider x, y, w, h, options, val, range, size, range

Remarks

x | x-coordinate of scroll bar top-left, in pixels  
---|---  
y | y-coordinate of scroll bar top-left, in pixels  
w | Width of slider, in pixels. If width is greater than height, the scroll bar is drawn horizontally  
h | Height of slider, in pixels. If height is greater than width, the scroll bar is drawn vertically  
options | By default the slider is drawn with a 3D effect. OPT_FLAT removes the 3D effect  
val | Displayed value of slider, between 0 and range inclusive  
range | Maximum value  
  
Example

```vb
' Pseudocode

' A slider set to 50%

```
CmdSlider 20, 50, 120, 8, 0, 50, 100

![clip0053](clip0053.png)

' Without the 3D look

CmdSlider 20, 50, 120, 8, OPT_FLAT, 50, 100

![clip0054](clip0054.png)

' A brown-themed vertical slider with range 0-65535

CmdBgColor &H402000

CmdFgColor &H703800

CmdSlider 76, 10, 8, 100, 0, 20000, 65535

![clip0055](clip0055.png)