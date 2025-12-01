# SHIFT

Action

Shift all bits one place to the left or right.

Syntax

SHIFT var , LEFT/RIGHT[ , shifts] [,SIGNED]

Remarks

Var | Byte, Integer, Word, Long, Dword or Single variable.  
---|---  
Shifts | The number of shifts to perform.  
signed | An option that only works with right shifts. It will preserve the sign bit which otherwise would be cleared by the first shift.  
  
The SHIFT statement rotates all the bits in the variable to the left or right.

When shifting LEFT the most significant bit, will be shifted out of the variable. The LS bit becomes zero. Shifting a variable to the left, multiplies the variable with a value of two.

When shifting to the RIGHT, the least significant bit will be shifted out of the variable. The MS bit becomes zero. Shifting a variable to the right, divides the variable by two. Use the SIGNED parameter to preserve the sign.

A Shift performs faster than a multiplication or division.

See also

[ROTATE](rotate.md) , [SHIFTIN](shiftin.md) , [SHIFTOUT](shiftout.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : shift.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example for SHIFTIN and SHIFTOUT statement

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

Dim L As Long

```
Clock Alias Portb.0

Output Alias Portb.1

Sin Alias Pinb.2 'watch the PIN instead of PORT

```vb
'shiftout pinout,pinclock, var,parameter [,bits , delay]

' value for parameter :

' 0 - MSB first ,clock low

' 1 - MSB first,clock high

' 2 - LSB first,clock low

' 3 - LSB first,clock high

'The bits is a new option to indicate the number of bits to shift out

'For a byte you should specify 1-8 , for an integer 1-16 and for a long 1-32

'The delay is an optional delay is uS and when used, the bits parameter must

'be specified too!

'Now shift out 9 most significant bits of the LONG variable L

```
Shiftout Output , Clock , L , 0 , 9

```vb
'shiftin pinin,pinclock,var,parameter [,bits ,delay]

' 0 - MSB first ,clock low (4)

' 1 - MSB first,clock high (5)

' 2 - LSB first,clock low (6)

' 3 - LSB first,clock high (7)

'To use an external clock, add 4 to the parameter

'The shiftin also has a new optional parameter to specify the number of bits

'The bits is a new option to indicate the number of bits to shift out

'For a byte you should specify 1-8 , for an integer 1-16 and for a long 1-32

'The delay is an optional delay is uS and when used, the bits parameter must

'be specified too!

'Shift in 9 bits into a long

```
Shiftin Sin , Clock , L , 0 , 9

'use shift to shift the bits to the right place in the long

Shift L , Right , 23

End