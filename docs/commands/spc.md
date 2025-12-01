# SPC

Action

Prints the number of specified spaces.

Syntax

PRINT SPC(x)

LCD SPC(x)

Remarks

X | The number of spaces to print.  
---|---  
  
Using 0 for x will result in a string of 255 bytes because there is no check for a zero length assign.

SPC can be used with [LCD](lcd_1.md) too.

The difference with the SPACE function is that SPACE returns a number of spaces while SPC() can only be used with printing. Using SPACE() with printing is also possible but it will use a temporary buffer while SPC does not use a temporary buffer.

See also

[SPACE](space.md)

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

Print "{" ; Spc(5) ; "}" '{ }

```
Lcd "{" ; Spc(5) ; "}" '{ }