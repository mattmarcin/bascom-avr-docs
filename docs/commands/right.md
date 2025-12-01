# RIGHT

Action

Return a specified number of rightmost characters in a string.

Syntax

var = RIGHT(var1 ,n )

Remarks

var | The string that is assigned.  
---|---  
Var1 | The source string.  
st | The number of bytes to copy from the right of the string.  
  
RIGHT supports [$BIGSTRINGS](bigstrings.md)

See also

[LEFT](left.md) , [MID](mid.md)

Example

Dim S As String * 15 , Z As String * 15

S ="ABCDEFG"

Z = Left(s , 5)

Print Z 'ABCDE

Z = Right(s , 3) : Print Z

Z = Mid(s , 2 , 3) : Print Z

End