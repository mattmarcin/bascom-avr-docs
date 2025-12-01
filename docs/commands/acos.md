# ACOS

Action

Returns the arccosine of a float in radians.

Syntax

var = ACOS( x )

Remarks

Var | A floating point variable such as single or double, that is assigned with the ACOS of variable x.  
---|---  
X | The float to get the ACOS of. Input is valid from â1 to +1 and returns p to 0. If Input is < -1 than p and input is > 1 than 0 will returned.  
  
If Input is cause of rounding effect in float-operations a little bit over 1 or -1, the value for 1.0 (-1.0) will be returned. This is the reason to give the value of the limit-point back, if Input is beyond limit. Generally the user have to take care, that Input to this function lies within â1 to +1.

All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

See Also

[RAD2DEG](rad2deg.md) , [DEG2RAD](deg2rad.md) , [COS](cos.md) , [SIN](sin.md) , [TAN](tan.md) , [ATN](atn.md) , [ASIN](asin.md) , [ATN2](atn2.md)

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
x= 0.5 : S = Acos(x)

```vb
Print S

End

```