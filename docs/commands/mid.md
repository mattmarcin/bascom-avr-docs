# MID

Action

The MID function returns part of a string (a sub string).

The MID statement replaces part of a string variable with another string.

Syntax

var = MID(var1 ,st [, l] )

MID(var ,st [, l] ) = var1

Remarks

var | The string that is assigned.  
---|---  
Var1 | The source string.  
st | The starting position.  
l | The number of characters to get/set.  
  
Both MID statement and MID function support [$BIGSTRINGS](bigstrings.md).

In version 2085 the code has been rewritten to be more efficient and safe. The safety comes with a small penalty.

When you provide an offset the old code would simply add this offset to the string address. This will work out fine except when the string is smaller than specified.

See also

[LEFT](left.md) , [RIGHT](right.md)

Example

Dim S As String * 15 , Z As String * 15

S ="ABCDEFG"

Z = Left(s , 5)

Print Z 'ABCDE

Z = Right(s , 3) : Print Z

Z = Mid(s , 2 , 3) : Print Z

End