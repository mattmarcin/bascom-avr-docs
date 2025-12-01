# RTRIM

Action

Returns a copy of a string with trailing blanks removed

Syntax

var = RTRIM( org )

Remarks

var | String that is assigned with the result.  
---|---  
org | The string to remove the trailing spaces from  
  
RTRIM supports [$BIGSTRINGS](bigstrings.md)

See also

[TRIM](trim.md) , [LTRIM](ltrim.md)

ASM

NONE

Example

Dim S As String * 6

S =" AB "

```vb
Print Ltrim(s)

Print Rtrim(s)

Print Trim(s)

End

```