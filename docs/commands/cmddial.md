# CmdDial

Action

Draw a rotary dial control.

Syntax

CmdDial x, y, r ,options, val

Remarks

x | x-coordinate of dial center, in pixels  
---|---  
y | y-coordinate of dial center, in pixels  
r | radius of dial, in pixels  
options | By default the dial is drawn with a 3D effect. Options OPT_FLAT removes the 3D effect.   
val | Specify the position of dial points by setting a value between 0 and 65535 inclusive.  0 means that the dial points straight down, &H4000 left, &H8000 up, and &Hc000 right.  
  
Example

```vb
' Pseudocode

' A dial set to 50%

```
CmdDial 80, 60, 55, 0, &H8000

![clip0006](clip0006.png)

' Without the 3D look

CmdDial 80, 60, 55, OPT_FLAT, &H8000

![clip0007](clip0007.png)

' Dials set to 0%, 33% and 66%

CmdDial 28, 60 , 24, 0, 0

CmdText 28, 100, 26, OPT_CENTER, "0%"

CmdDial 80, 60, 24, 0, &H5555

CmdText 80, 100, 26, OPT_CENTER, "33%"

CmdDial 132, 60, 24, 0, &HAAAA

CmdText 132, 100, 26, OPT_CENTER, "66%"

![clip0008](clip0008.png)