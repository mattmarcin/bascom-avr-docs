# GRAY2BIN

Action

Returns the numeric value of a Gray code.

Syntax

var1 = GRAY2BIN(var2)

Remarks

var1 | Variable that will be assigned with the binary value of the Grey code.  
---|---  
var2 | A variable in Grey format that will be converted.  
  
Gray code is used for rotary encoders. Gray2bin() works for byte, integer, word and long variables.

See also

[BIN2GRAY](bin2gray.md)

ASM

Depending on the data type of the target variable the following routine will be called from mcs.lbx:

_Bin2grey for bytes , _Bin2Grey2 for integer/word and _Bin2grey4 for longs.

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