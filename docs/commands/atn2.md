# ATN2

Action

ATN2 is a four-quadrant arc-tangent.

While the ATN-function returns from -p/2 (-90Â°) to p/2 (90Â°), the ATN2 function returns the whole range of a circle from -p (-180Â°) to +p (180Â°). The result depends on the ratio of Y/X and the signs of X and Y.

Syntax

var = ATN2( y, x )

Remarks

Var | A floating point variable that is assigned with the ATN2 of variable y and x.  
---|---  
X | The float variable with the distance in x-direction.  
Y | The float variable with the distance in y-direction  
  
![atn2](atn2.gif)

Quadrant | Sign Y | Sign X | ATN2  
---|---|---|---  
I | + | + | 0 to p/2  
II | + | - | p/2 to p  
III | - | - | -p/2 to -p  
IV | - | + | 0 to âp/2  
  
If you go with the ratio Y/X into ATN you will get same result for X greater zero (right side in coordinate system) as with ATN2. ATN2 uses X and Y and can give information of the angle of the point over 360Â° in the coordinates system.

All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

See Also

[RAD2DEG](rad2deg.md) , [DEG2RAD](deg2rad.md) , [COS](cos.md) , [SIN](sin.md) , [TAN](tan.md) , [ATN](atn.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim S As Single , X As Single

```
X = 0.5 : S = 1.1

S = Atn2(s , X)

```vb
Print S ' prints 1.144164676

End

```