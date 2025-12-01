# SPACE

Action

Returns a string that consists of spaces.

Syntax

var = SPACE(x)

Remarks

X | The number of spaces. This must be a value > 0  
---|---  
Var | The string that is assigned.  
  
In version 2085 the passed value is tested for 0. Since zero is not allowed, the resulting string will be unaltered when using 0.

SPACE supports [$BIGSTRINGS](bigstrings.md)

See also

[STRING](string.md) , [SPC](spc.md)

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates DEG2RAD function

'-------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim S As String * 15 , Z As String * 15

```
S = Space(5)

```vb
Print " {" ; S ; " }" '{ }

Dim A As Byte

```
A = 3

S = Space(a)

End