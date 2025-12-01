# LCASE

Action

Converts a string in to all lower case characters.

Syntax

Target = LCASE(source)

Remarks

Target | The string that is assigned with the lower case string of string target.  
---|---  
Source | The source string.  
  
LCASE supports [$BIGSTRINGS](bigstrings.md)

See also

[UCASE](ucase.md)

ASM

The following ASM routines are called from MCS.LIB : _LCASE

The generated ASM code : (can be different depending on the micro used )

;##### Z = Lcase(s)

Ldi R30,$60

Ldi R31,$00 ; load constant in register

Ldi R26,$6D

Rcall _Lcase

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim S As String * 12 , Z As String * 12

```
S = "Hello World"

Z = Lcase(s)

Print Z

Z = Ucase(s)

```vb
Print Z

End

```