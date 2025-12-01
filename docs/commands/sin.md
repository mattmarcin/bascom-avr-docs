# SIN

Action

Returns the sine of a float

Syntax

var = SIN( source )

Remarks

Var | A numeric variable that is assigned with sinus of variable source.  
---|---  
source | The single or double variable to get the sinus of.  
  
All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

See Also

[RAD2DEG](rad2deg.md) , [DEG2RAD](deg2rad.md) , [ATN](atn.md) , [COS](cos.md)

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
S = 0.5 : X = Tan(s) : Print X ' prints 0.546302195

S = 0.5 : X = Sin(s) : Print X ' prints 0.479419108

S = 0.5 : X = Cos(s) : Print X ' prints 0.877588389

End