# ROUND

Action

Returns a value rounded to the nearest value.

Syntax

var = ROUND( x )

Remarks

Var | A single or double variable that is assigned with the ROUND of variable x.  
---|---  
X | The single or double to get the ROUND of.  
  
Round(2.3) = 2 , Round(2.8) = 3

Round(-2.3) = -2 , Round(-2.8) = -3

See Also

[INT](int.md) , [FIX](fix.md) , [SGN](sgn.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : round_fix_int.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : ROUND,FIX

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim S As Single , Z As Single

For S = -10 To 10 Step 0.5

Print S ; Spc(3) ; Round(s) ; Spc(3) ; Fix(s) ; Spc(3) ; Int(s)

Next

End

```