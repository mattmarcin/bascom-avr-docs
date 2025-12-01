# CmdClock

Action

Draw a Analog Clock.

Syntax

CmdClock x, y, r, options, h, m, s, ms

Remarks

x | x-coordinate of clock center, in pixels  
---|---  
y | y-coordinate of clock center, in pixels  
r | Radius of the gauge, in pixels  
options | By default the clock dial is drawn with a 3D effect and the name of this option is OPT_3D.  Option OPT_FLAT removes the 3D effect.  With option OPT_NOBACK, the background is not drawn. With option OPT_NOTICKS, the twelve hour ticks are not drawn.  With option OPT_NOSECS, the seconds hand is not drawn.  With option OPT_NOHANDS, no hands are drawn.  With option OPT_NOHM, no hour and minutes hands are drawn.   
h | hours  
m | minutes  
s | seconds  
ms | milliseconds  
  
The details of physical dimension are:

•| The 12 tick marks are placed on a circle of radius r*(200/256).  
---|---  
  
•| Each tick is a point of radius r*(10/256)  
---|---  
  
•| The seconds hand has length r*(200/256) and width r*(3/256)  
---|---  
  
•| The minutes hand has length r*(150/256) and width r*(9/256)  
---|---  
  
•| The hours hand has length r*(100/256) and width r*(12/256)  
---|---  
  
Refer to sections 5.7 Widgets physical dimensions and 5.7 Widget color settings in the FT800 Series Programmer Guide.PDF from FTDI

for more information.

Example

' A clock with radius 50 pixels, showing a time of 8.15

CmdClock 80, 60, 50, 0, 8, 15, 0, 0

![clip0024](clip0024.png)

' Setting the background color 

CmdBgColor &H401010

CmdClock 80, 60, 50, 0, 8, 15, 0, 0

![clip0025](clip0025.png)

' Without the 3D look

CmdClock 80, 60, 50, OPT_FLAT, 8, 15, 0, 0

```vb
' The time fields can have large values. Here the hours are (7 x 3600s) and minutes 

' are (38 x 60s), and seconds is 59. Creating a clock face showing the time as 7.38.59

```
CmdClock 80, 60, 50, 0, 0, 0, (7 * 3600) + (38 * 60) + 59, 0

![clip0026](clip0026.png)

' No seconds hand

CmdClock 80, 60, 50, OPT_NOBACK, 8, 15, 0, 0

![clip0027](clip0027.png)

' No background

CmdClock 80, 60, 50, OPT_NOBACK, 8, 15, 0, 0

![clip0028](clip0028.png)

' No Ticks

CmdClock 80, 60, 50, OPT_NOTICKS, 8, 15, 0, 0

![clip0029](clip0029.png)

' No Hands

CmdClock 80, 60, 50, OPT_NOHANDS, 8, 15, 0, 0

![clip0030](clip0030.png)