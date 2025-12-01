# LEFT

Action

Return the specified number of leftmost characters in a string.

Syntax

var = LEFT(var1 , n)

Remarks

Var | The string that is assigned.  
---|---  
Var1 | The source string.  
n | The number of characters to get from the source string.  
  
LEFT supports [$BIGSTRINGS](bigstrings.md)

See also

[RIGHT](right.md) , [MID](mid.md)

Partial Example

Dim S As String * 15 , Z As String * 15

S ="ABCDEFG"

Z = Left(s , 5)

Print Z 'ABCDE

Z = Right(s , 3) : Print Z

Z = Mid(s , 2 , 3) : Print Z

End