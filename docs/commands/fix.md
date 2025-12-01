# FIX

Action

Returns for values greater then zero the next lower value, for values less then zero the next upper value.

Syntax

var = FIX( x )

Remarks

Var | A single or double variable that is assigned with the FIX of variable x.  
---|---  
X | The floating point variable to get the FIX of.  
  
See Also

[INT](int.md) , [ROUND](round.md) , [SGN](sgn.md)

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