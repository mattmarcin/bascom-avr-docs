# INT

Action

Returns the integer part of a single or double.

Syntax

var = INT( source )

Remarks

Var | A numeric floating point variable that is assigned with the integer of variable source.  
---|---  
Source | The source floating point variable to get the integer part of.  
  
The fraction is the right side after the decimal point of a single.

The integer is the left side before the decimal point.

1234.567 1234 is the integer part, .567 is the fraction

![notice](notice.jpg)The assigned variable must be a single or double. When you want to convert a floating point data type to an integer data type, just assign the variable to a variable of that type : someLong = someDouble

See Also

[FRAC](frac.md) , [FIX](fix.md) , [ROUND](round.md)

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