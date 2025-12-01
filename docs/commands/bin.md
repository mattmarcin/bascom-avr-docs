# BIN

Action

Convert a numeric variable into the binary string representation.

Syntax

Var = Bin(source)

Remarks

Var | The target string that will be assigned with the binary representation of the variable source.  
---|---  
Source | The numeric variable that will be converted.  
  
The BIN() function can be used to display the state of a port.

When the variable source has the value &B10100011 the string named var will be assigned with "10100011".

It can be easily printed to the serial port.

See also

[HEX](hex.md) , [STR](str.md) , [VAL](val.md) , [HEXVAL](hexval.md) , [BINVAL](binval.md)

ASM

NONE

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim B As Byte

' assign value to B

```
B = 45

```vb
Dim S As String * 10

'convert to string

```
S = Bin(b)

'assign value to portb

Portb = 33

```vb
Print Bin(portb)

'of course it also works for other numerics

End

```