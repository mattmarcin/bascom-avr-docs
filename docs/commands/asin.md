# ASIN

Action

Returns the arcsine of a float in radians.

Syntax

var = ASIN( x )

Remarks

Var | A float variable such as single or double that is assigned with the ASIN of variable x.  
---|---  
X | The float to get the ASIN of. Input is valid from â1 to +1 and returns -p/2 to +p/2. If Input is < -1 than -p/2 and input is > 1 than p/2 will returned.  
  
If Input is cause of rounding effect in single-operations a little bit over 1 or -1, the value for 1.0 (-1.0) will be returned. This is the reason to give the value of the limit-point back, if Input is beyond limit. Generally the user have to take care, that Input to this function lies within â1 to +1.

All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

See Also

[RAD2DEG](rad2deg.md) , [DEG2RAD](deg2rad.md) , [COS](cos.md) , [SIN](sin.md) , [TAN](tan.md) , [ATN](atn.md) , [ACOS](acos.md) , [ATN2](atn2.md)

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
X = 0.5 : S = Asin(x)

```vb
Print S '0.523595867

End

```