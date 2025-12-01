# INSTR

Action

Returns the position of a sub string in a string.

Syntax

var = INSTR( start , string , substr )

var = INSTR( string , substr )

Remarks

Var | Numeric variable that will be assigned with the position of the sub string in the string. Returns 0 when the sub string is not found. When used with $BIGSTRINGS, the target variable should be a word instead of a byte.  
---|---  
Start | An optional numeric parameter that can be assigned with the first position where must be searched in the string. By default (when not used) the whole string is searched starting from position 1.  
String | The string to search.  
Substr | The search string.  
  
No constant can be used for string it must be a string variable.

Only substr can be either a string or a constant.

INSTR supports [$BIGSTRINGS](bigstrings.md)

See also

[SPLIT](split.md) , [CHARPOS](charpos.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : instr.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : INSTR function demo

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

'dimension variables

Dim Pos As Byte

Dim S As String * 8 , Z As String * 8

'assign string to search

```
S = "abcdeab" ' Z = "ab"

'assign search string

Z = "ab"

'return first position in pos

Pos = Instr(s , Z)

```vb
'must return 1

'now start searching in the string at location 2

```
Pos = Instr(2 , S , Z)

'must return 6

Pos = Instr(s , "xx")

```vb
'xx is not in the string so return 0

End

```