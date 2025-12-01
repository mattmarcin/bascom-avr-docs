# FORMAT

Action

Formats a numeric string.

Syntax

target = FORMAT(source, "mask")

Remarks

target | The string that is assigned with the formatted string.  
---|---  
source | The source string that holds the number.  
mask | The mask for formatting the string. When spaces are in the mask, leading spaces will be added when the length of the mask is longer than the source string. " " '8 spaces when source is "123" it will be " 123". When a + is in the mask (after the spaces) a leading + will be assigned when the number does not start with the - (minus) sign. "+" with number "123" will be "+123". When zero's are provided in the mask, the string will be filled with leading zero's. " +00000" with 123 will become " +00123" An optional decimal point can be inserted too: "000.00" will format the number 123 to "001.23" Combinations can be made but the order must be : spaces, + , 0 an optional point and zero's. In version 2080 the mask may be a variable as well.  
  
When you do not want to use the overhead of the single or double, you can use the LONG. You can scale the value by a factor for example 100.

```vb
Then use FORMAT to show the value.

For example : 

Dim L as Long, X as Long , Res as Long

```
L = 1

X = 2

Res = L / X

```vb
' Now this would result in 0 because an integer or Long does not support floating point.

' But when you scale L with a factor 100, you get :

```
L = 100

X = 2

Res = L / X '50

Now Res will be 50. To show it the proper way we can use FORMAT. Format works with strings so the variables need to be converted to string first.

```vb
Dim S1 as string * 16 : s1 = Str(Res)

Print Format(s1,"000.00")

```
See also

[FUSING](fusing.md) , [STR](str.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : format.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : FORMAT

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

Dim S As String * 10

Dim I As Integer

```
S = "12345"

S = Format(s , "+")

Print S ' +12345

S = "123"

S = Format(s , "00000") 

Print S ' 00123

S = "12345"

S = Format(s , "000.00")

Print S ' 123.45

S = "12345"

S = Format(s , "+000.00")

```vb
Print S ' +123.45

End

```