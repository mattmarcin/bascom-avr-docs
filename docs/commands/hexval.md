# HEXVAL

Action

Convert string representing a hexadecimal number into a numeric variable.

Syntax

var = HEXVAL( x )

Remarks

Var | The numeric variable that must be assigned.  
---|---  
X | The hexadecimal string that must be converted.  
  
In VB you can use the VAL() function to convert hexadecimal strings.

But since that would require an extra test for the leading &H signs that are required in VB, a separate function was designed.

The data may only contain hex decimal characters : 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,a,b,c,d,e,f. Other data will lead to conversion errors. If you need spaces to be filtered you can use the alternative library named hexval.lbx

Include it to your code with $LIB "hexval.lbx" and the conversion routine from this library will be used instead of the one from mcs.lbx. The alternative library will also set the ERR flag if an illegal character is found.

See also

[HEX](hex.md) , [VAL](val.md) , [STR](str.md) , [BIN](bin.md) , [BINVAL](binval.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim L As Long

Dim S As String * 8

Do

Input "Hex value " , S

```
L = Hexval(s)

```vb
Print L ; Spc(3) ; Hex(l)

Loop

```