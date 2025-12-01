# CmdProgress

Action

Draw a progress bar.

Syntax

CmdProgress x, y, w, h, options, val, range

Remarks

x | x-coordinate of progress bar top-left, in pixels  
---|---  
y | y-coordinate of progress bar top-left, in pixels  
w | width of progress bar, in pixels  
h | height of progress bar, in pixels  
options | By default the progress bar is drawn with a 3D effect and the value of options  is zero. Options OPT_FLAT removes the 3D effect and its value is 256.  
val | Displayed value of progress bar, between 0 and range inclusive  
range | Maximum value  
  
The details of physical dimensions are:

•| x,y,w,h give outer dimensions of progress bar. Radius of bar (r) is min (w,h)/2  
---|---  
  
•| Radius of inner progress line is r * (7/8)  
---|---  
  
Example

```vb
' Pseudocode

' A progress bar showing 50% completion

```
CmdProgress 20, 50, 120, 12, 0, 50,100

![clip0043](clip0043.png)

' Without the 3D look

CmdProgress 20, 50, 120, 12, OPT_FLAT, 50, 100

![clip0044](clip0044.png)

' A 4 pixel high bar, range 0-65535, with a brown background

CmdBgColor &H402000

CmdProgress 20, 50, 120, 4, 0, 9000, 65535

![clip0045](clip0045.png)