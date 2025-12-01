# MAX

Action

Returns the maximum value of a byte or word array.

Syntax

var1 = MAX(var2)

MAX(ar(1), m ,idx)

Remarks

var1 | Variable that will be assigned with the maximum value.  
---|---  
var2 | The first address of the array.  
|   
| The MAX statement can return the index too  
Ar(1) | Starting element to get the maximum value and index of.  
M | Returns the maximum value of the array.  
Idx | Return the index of the array that contains the maximum value. Returns 0 if there is no maximum value.  
  
The MIN() and MAX() functions work on BYTE and WORD arrays only.

See also

[MIN](min.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : minmax.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show the MIN and MAX functions

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

' These functions only works on BYTE and WORD arrays at the moment !!!!!

'Dim some variables

Dim Wb As Byte , B As Byte

Dim W(10) As Word ' or use a BYTE array

'fill the word array with values from 1 to 10

For B = 1 To 10

```
W(b) = B

```vb
Next

Print "Max number " ; Max(w(1))

Print "Min number " ; Min(w(1))

Dim Idx As Word , M1 As Word

```
Min(w(1) , M1 , Idx)

Print "Min number " ; M1 ; " index " ; Idx

Max(w(1) , M1 , Idx)

```vb
Print "Max number " ; M1 ; " index " ; Idx

End

```