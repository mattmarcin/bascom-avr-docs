# LOW

Action

Retrieves the least significant byte of a variable.

Sets the least significant byte of a variable

Syntax

var = LOW( s )

LOW( s ) = value

Remarks

Var | The variable that is assigned with the LSB of var S.  
---|---  
S | The source variable to get the LSB from when used as a function The target variable to set the LSB of when used in an assignment.  
value | The value to assign to the LSB when used as a statement  
  
You can also assign a byte to retrieve the LSB of a Word or Long.

For example :

B = L , where B is a byte and L is a Long.

In version 2083 the LOW function can also be used to set the LSB of a variable. This for compatibility with BASCOM-8051.

See also

[HIGH](high.md) , [HIGHW](highw.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim I As Integer , Z As Byte

```
I = &H1001

Z = Low(i) ' is 1

End