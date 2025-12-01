# FUSING

Action

FUSING returns a formatted string of a single value.

Syntax

target = FUSING(source, "mask")

Remarks

target | The string that is assigned with the formatted string.  
---|---  
source | The source variable of the type SINGLE that will be converted  
mask | The mask for formatting the string. The mask is a string constant that always must start with #. After the decimal point you can provide the number of digits you want the string to have: #.### will give a result like 123.456. Rounding is used when you use the # sign. So 123.4567 will be converted into 123.457 When no rounding must be performed, you can use the & sign instead of the # sign. But only after the DP. #.&&& will result in 123.456 when the single has the value 123.4567  
  
When the single is zero, 0.0 will be returned, no matter how the mask is set up.

See also

[FORMAT](format.md) , [STR](str.md) , [CONFIG SINGLE](configsingle.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : fusing.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : FUSING

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

Dim S As Single , Z As String * 10

'now assign a value to the single

```
S = 123.45678

'when using str() you can convert a numeric value into a string

Z = Str(s)

Print Z 'prints 123.456779477

Z = Fusing(s , "#.##")

```vb
'now use some formatting with 2 digits behind the decimal point with rounding

Print Fusing(s , "#.##") 'prints 123.46

'now use some formatting with 2 digits behind the decimal point without rounding

Print Fusing(s , "#.&&") 'prints 123.45

'The mask must start with #.

'It must have at least one # or & after the point.

'You may not mix & and # after the point.

End

```