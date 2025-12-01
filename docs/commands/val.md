# VAL

Action

Converts a string representation of a number into a number.

Syntax

var = VAL( s)

Remarks

Var | A numeric variable that is assigned with the value of s.  
---|---  
S | Variable of the string type.  
  
It depends on the variable type which conversion routine will be used. Single and Double conversion will take more code space.

When you use INPUT, internal the compiler also uses the VAL routines.

In order to safe code space, there are different conversion routines. For example BINVAL and HEXVAL are separate routines.

While they could be added to the compiler, it would mean a certain overhead as they might never be needed.

With strings as input or the INPUT statement, the string is dynamic and so all conversion routines would be needed.

The VAL() conversion routine does not check for illegal characters. If you use them you get a wrong result or 0.

If you want to check for illegal characters you can add a constant named _VALCHECK to your code with a value of 1.

This will include some code that will set the internal ERR variable to 0 or 1. If illegal characters are found, ERR will return 1.

Since VAL is used for the INPUT statement too, this will also work for the INPUT statement.

See also

[STR](str.md) , [HEXVAL](hexval.md) , [HEX](hex.md) , [BIN](bin.md) , [BINVAL](binval.md) , [STR2DIGITS](str2digits.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim A As Byte , S As String * 10

```
S = "123"

A = Val(s) 'convert string

Print A ' 123

S = "12345678"

Dim L As Long

L = Val(s)

```vb
Print L

End

```
Example2

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Const _VALCHECK=1 ' TEST VAL()

Dim A As Byte , S As String * 10

S = "123"

A = Val(s) 'convert string

Print A ; " ERR:" ; Err ' 123

S = "1234a5678"

Dim L As Long

L = Val(s)

```vb
Print L ; " ERR:" ; Err

End

```