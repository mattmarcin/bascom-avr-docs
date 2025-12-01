# HEX

Action

Returns a string representation of a hexadecimal number.

Syntax

var = HEX( x )

Remarks

var | A string variable.  
---|---  
X | A numeric variable of data type Byte, Integer, Word, Long, Single or Double.  
  
See also

[HEXVAL](hexval.md) , [VAL](val.md) , [STR](str.md) , [BIN](bin.md) , [BINVAL](binval.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim B As Byte , J As Integer , W As Word , L As Long

```
B = 1 : J = &HF001

W = &HF001

L = W

```vb
Print B ; Spc(3) ; Hex(b)

Print J ; Spc(3) ; Hex(j)

Print W ; Spc(3) ; Hex(w)

Print L ; Spc(3) ; Hex(l)

End

```