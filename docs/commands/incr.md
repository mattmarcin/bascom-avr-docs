# INCR

Action

Increments a variable by one.

Syntax

INCR var

Remarks

Var | Any numeric variable.  
---|---  
  
See also

[DECR](decr.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : incr.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: INCR

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

Dim A As Byte

```
A = 5 'assign value to a

Incr A 'inc (by one)

```vb
Print A 'print it

End

```