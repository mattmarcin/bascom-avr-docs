# LOOKUPSTR

Action

Returns a string from a table.

Syntax

var = LOOKUPSTR( index, label )

Remarks

Var | The string returned  
---|---  
Index | A value with the index of the table. The index is zero-based. That is, 0 will return the first element of the table. The maximum value is 65535.  
Label | The label where the data starts. A variable with the address is accepted as well.  
  
See also

[LOOKUP](lookup.md) , [LOOKDOWN](lookdown.md) , [DATA](data_2.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim S As String * 8 , Idx As Byte

```
Idx = 0 : S = Lookupstr(idx , Sdata)

```vb
Print S 'will print 'This'

End

```
Sdata:

Data "This" , "is" , "a test"