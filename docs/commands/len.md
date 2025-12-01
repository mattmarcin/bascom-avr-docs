# LEN

Action

Returns the length of a string.

Syntax

var = LEN( string )

Remarks

var | A numeric variable that is assigned with the length of string.  
---|---  
string | The string to calculate the length of.  
  
Strings can be maximum 254 bytes long.

When using $BIGSTRINGS, the string can be as long as 65534 bytes. This depends on the available memory.

LEN supports [$BIGSTRINGS](bigstrings.md)

See Also

[VAL](val.md)

Partial Example

Dim S As String * 15 , Z As String * 15

S ="ABCDEFG"

Print Len(s)