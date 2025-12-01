# BINVAL

Action

Converts a string representation of a binary number into a number.

Syntax

var = Binval( s)

Remarks

Var | A numeric variable that is assigned with the value of s.  
---|---  
S | Variable of the string type. Should contain only 0 and 1 digits.  
  
See also

[STR](str.md) , [HEXVAL](hexval.md) , [HEX](hex.md) , [BIN](bin.md) , [VAL](val.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim S As String * 8

```
S = "11001100"

```vb
Dim B As Byte

' assign value to B

```
B = Binval(s)

```vb
Print B

End

```