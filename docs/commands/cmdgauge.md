# CmdGauge

Action

Draw a Gauge.

Syntax

CmdGauge x, y, r, options, major, minor, val, range

Remarks

x | X-coordinate of gauge center, in pixels  
---|---  
y | Y-coordinate of gauge center, in pixels  
r | Radius of the gauge, in pixels  
options | By default the gauge dial is drawn with a 3D effect and the value of options is  zero. OPT_FLAT removes the 3D effect. With option OPT_NOBACK, the  background is not drawn. With option OPT_NOTICKS, the tick marks are not  drawn. With option OPT_NOPOINTER, the pointer is not drawn.   
major | Number of major subdivisions on the dial, 1-10 minor  
minor | Number of minor subdivisions on the dial, 1-10  
val | Gauge indicated value, between 0 and range, inclusive range  
range | Maximum value  
  
The details of physical dimension are:

•| The tick marks are placed on a 270 degree arc, clockwise starting at southwest position  
---|---  
  
•| Minor ticks are lines of width r*(2/256), major r*(6/256)  
---|---  
  
•| Ticks are drawn at a distance of r*(190/256) to r*(200/256)  
---|---  
  
•| The pointer is drawn with lines of width r*(4/256), to a point r*(190/256) from the center  
---|---  
  
•| The other ends of the lines are each positioned 90 degrees perpendicular to the pointer direction, at a distance r*(3/256) from the center  
---|---  
  
Refer to sections 5.7 Widgets physical dimensions and 5.7 Widget color settings in the FT800 Series Programmer Guide.PDF from FTDI

for more information.

Example

```vb
' Pseudocode

' A gauge with radius 50 pixels, five divisions of four ticks each, indicating 30%

```
CmdGauge 80, 60, 50, 0, 5, 4, 30, 100

![clip0010](clip0010.png)

' Without the 3D look

CmdGauge 80, 60, 50, OPT_FLAT, 5, 4, 30, 100

![clip0011](clip0011.png)

' Ten major divisions with two minor divisions each

CmdGauge 80, 60, 50, 0, 10, 2, 30, 100

![clip0013](clip0013.png)

' Setting the minor divisions to 1 makes them disappear

CmdGauge 80, 60, 50, 0, 10, 1, 30, 100

![clip0014](clip0014.png)

' Setting the major divisions to 1 gives minor divisions only

CmdGauge 80, 60, 50, 0, 1, 10, 30, 100

![clip0015](clip0015.png)

' A smaller gauge with a brown background

CmdBgColor &H402000

CmdGauge 80, 60, 25, 0, 5, 4, 30, 100

![clip0016](clip0016.png)

' Scale 0-1000, indicating 1000

CmdGauge 80, 60, 50, 0, 5, 2, 1000, 1000

![clip0017](clip0017.png)

' Scaled 0-65535, indicating 49152

CmdGauge 80, 60, 50, 0, 4, 4, 49152, 65535

![clip0018](clip0018.png)

' No background

CmdGauge 80, 60, 50, OPT_NOBACK, 4, 4, 49152, 65535

![clip0019](clip0019.png)