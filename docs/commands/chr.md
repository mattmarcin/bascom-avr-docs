# CHR

Action

Convert a numeric variable or a constant to a string with a length of 1 character. The character represents the ASCII value of the numeric value.

Syntax

PRINT CHR(var)

s = CHR(var)

Remarks

Var | Numeric variable or numeric constant.  
---|---  
S | A string variable.  
  
When you want to print a character to the screen or the LCD display,

you must convert it with the CHR() function.

When you use PRINT numvar, the value will be printed.

When you use PRINT Chr(numvar), the ASCII character itself will be printed.

The Chr() function is handy in combination with the LCD custom characters where you can redefine characters 0-7 of the ASCII table.

Since strings are terminated with a null byte which is the same as Chr(0) , you can not embed a Chr(0) into a string.

When using Chr(0) with the LCD to display a customer character, use : LCD "tekst" ; chr(0) ; "more tekst"

See also

[ASC](asc.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : chr.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to use the CHR() and BCD() function and

' HEX() function in combination with a PRINT statement

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

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim K As Byte

```
K = 65

```vb
Print K ; Chr(k) ; K ; Chr(66) ; Bcd(k) ; Hex(k)

End

```