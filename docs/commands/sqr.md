# SQR

Action

Returns the Square root of a variable.

Syntax

var = SQR( source )

Remarks

var | A numeric single or double variable that is assigned with the SQR of variable source.  
---|---  
source | The single or double variable to get the SQR of.  
  
When SQR is used with a single, the FP_TRIG library will be used.

When SQR is used with bytes, integers, words and longs, the SQR routine from MCS.LBX will be used.

See Also

[POWER](power.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Single

Dim B As Double

```
A = 9.0

B = 12345678.123

A =Sqr(A)

Print A ' prints 3.0

B = Sqr(b)

```vb
Print B

End

```