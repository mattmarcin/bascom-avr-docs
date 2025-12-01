# FRAC

Action

Returns the fraction of a single.

Syntax

var = FRAC( single )

Remarks

var | A numeric single variable that is assigned with the fraction of variable single.  
---|---  
single | The single variable to get the fraction of.  
  
The fraction is the right side after the decimal point of a single.

See Also

[INT](int.md)

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates FRAC function

'-------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim X As Single

```
X = 1.123456

```vb
Print X

Print Frac(x)

End

```