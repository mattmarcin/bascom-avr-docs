# TRIM

Action

Returns a copy of a string with leading and trailing blanks removed

Syntax

var = TRIM( org )

Remarks

Var | String that receives the result.  
---|---  
Org | The string to remove the spaces from  
  
TRIM is the same as an LTRIM() and RTRIM() call. It will remove the spaces on the left and right side of the string.

TRIM supports [$BIGSTRINGS](bigstrings.md)

See also

[RTRIM](rtrim.md) , [LTRIM](ltrim.md)

Partial Example

Dim S As String * 6

S =" AB "

```vb
Print Ltrim(s)

Print Rtrim(s)

Print Trim(s)

End

```