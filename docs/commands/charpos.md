# CHARPOS

Action

Returns the position of a single character in a string.

Syntax

pos = CHARPOS(string , search [,start [,SAFE]])

Remarks

Pos | Numeric variable that will be assigned with the position of the sub string in the string. Returns 0 when the sub string is not found.  
---|---  
String | The string to search.  
Search | The search string. This can be a numeric variable too. For example a byte. When a string is used, only the first character will be used for the search.  
Offset | An optional start position where the searching must start.  
SAFE | If you specify an offset, Charpos will check if the offset is not located after the string. For example , when the string is "abc" and you specify an offset of 10, it will be located after the string. The SAFE option is default. When you specify SPEED, the compiler will add the offset without checking. This will result in shorter and quicker code.  
  
No constant can be used for string it must be a string variable.

![notice](notice.jpg)The search is sensitive to case.

CHARPOS supports [$BIGSTRINGS](bigstrings.md)

See also

[SPLIT](split.md) , [INSTR](instr.md) , [REPLACECHARS](replacechars.md) , [DELCHAR](delchar.md) , [INSERTCHAR](insertchar.md) , [DELCHARS](delchars.md)

Example

```vb
'-------------------------------------------------------------------------------

' charpos.bas

' (c) 1995-2025 MCS Electronics

$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

'-------------------------------------------------------------------------------

Dim S As String * 20

Dim Bpos As Byte

Dim Z As String * 1

```
Z = "*"

```vb
Do

Input "S:" , S

```
Bpos = Charpos(s , Z)

```vb
Print Bpos

Loop Until S = ""

Do

Input "S:" , S

```
Bpos = Charpos(s , "A") ' notice charpos is sensitive to case

```vb
Print Bpos

Loop

```