# DECR

Action

Decrements a variable by one.

Syntax

DECR var

Remarks

There are often situations where you want a number to be decreased by 1. It is simpler to write :

DECR var

compared to :

var = var - 1

See also

[INCR](incr.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : decr.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demostrate decr

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

Dim A As Byte , I As Integer

```
A = 5 'assign value to a

Decr A 'decrease (by one)

Print A 'print it

I = 1000

Decr I

```vb
Print I

End

```