# STRING

Action

Returns a string consisting of m repetitions of the character with ASCII Code n.

Syntax

var = STRING(m ,n)

Remarks

Var | The string that is assigned.  
---|---  
N | The ASCII-code that is assigned to the string.  
M | The number of characters to assign. This must be a number > 0  
  
Since a string is terminated by a 0 byte, you can't use 0 for n. That is you could but the result would be an empty string.

Using 0 for x will not alter the resulting string.

STRING supports [$BIGSTRINGS](bigstrings.md)

See also

[SPACE](space.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim S As String * 15

```
S = String(5 , 65)

```vb
Print S 'AAAAA

End

```