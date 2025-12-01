# EXP

Action

Returns e( the base of the natural logarithm) to the power of a single or double variable.

Syntax

Target = EXP(source)

Remarks

Target | The single or double that is assigned with the Exp() of the target.  
---|---  
Source | The source to get the Exp of.  
  
See also

[LOG](log.md) , [LOG10](log10.md)

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega88

'suited for demo : no, but without the DOUBLE, it works for DEMO too in M48

'commercial addon needed : no

'purpose : demonstrates EXP function

'-------------------------------------------------------------------------------

$regfile = "m88def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim X As Single

```
X = Exp(1.1)

```vb
Print X

'prints 3.004166124

```
X = 1.1

X = Exp(x)

```vb
Print X

'prints 3.004164931

Dim D As Double

```
D = Exp(1.1)

```vb
Print D

'prints 3.00416602394643

```
D = 1.1

D = Exp(d)

```vb
Print D

'prints 3.00416602394638

End

```