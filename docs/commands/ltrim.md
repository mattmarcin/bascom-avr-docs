# LTRIM

Action

Returns a copy of a string with leading blanks removed

Syntax

var = LTRIM( org )

Remarks

Var | String that receives the result.  
---|---  
Org | The string to remove the leading spaces from  
  
LTRIM supports [$BIGSTRINGS](bigstrings.md)

See also

[RTRIM](rtrim.md) , [TRIM](trim.md)

ASM

NONE

Partial Example

Dim S As String * 6

S =" AB "

```vb
Print Ltrim(s)

Print Rtrim(s)

Print Trim(s)

End

```