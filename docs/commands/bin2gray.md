# BIN2GRAY

Action

Returns the Gray-code of a variable.

Syntax

var1 = Bin2gray(var2)

Remarks

var1 | Variable that will be assigned with the Gray code.  
---|---  
var2 | A variable that will be converted.  
  
Gray code is used for rotary encoders. Bin2gray() works with byte , integer, word and long variables.

The data type of the variable that will be assigned determines if a byte, word or long conversion will be done.

See also

[GRAY2BIN](gray2bin.md) , [ENCODER](encoder.md)

ASM

Depending on the data type of the target variable the following routine will be called from mcs.lbx:

_grey2Bin for bytes , _grey2bin2 for integer/word and _grey2bin4 for longs.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : graycode.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show the Bin2Gray and Gray2Bin functions

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

'Bin2Gray() converts a byte,integer,word or long into grey code.

'Gray2Bin() converts a gray code into a binary value

Dim B As Byte ' could be word,integer or long too

Print "BIN" ; Spc(8) ; "GREY"

For B = 0 To 15

Print B ; Spc(10) ; Bin2gray(b)

Next

Print "GREY" ; Spc(8) ; "BIN"

For B = 0 To 15

Print B ; Spc(10) ; Gray2bin(b)

Next

End

```