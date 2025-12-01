# ATN

Action

Returns the Arctangent of a floating point variable in radians.

Syntax

var = ATN( float )

Remarks

Var | A float variable that is assigned with the arctangent of variable float.  
---|---  
float | The float variable to get the arctangent of.   
  
All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

Floating point variables can be of the single or double data type.

See Also

[RAD2DEG](rad2deg.md) , [DEG2RAD](deg2rad.md) , [COS](cos.md) , [SIN](sin.md) , [TAN](tan.md) , [ATN2](atn2.md)

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
S = Atn(1) * 4

```vb
Print S ' prints 3.141593 PI

End

```