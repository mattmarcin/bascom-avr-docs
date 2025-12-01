# ROTATE

Action

Rotate all bits one place to the left or right.

Syntax

ROTATE var , LEFT/RIGHT[ , shifts]

Remarks

Var | Byte, Integer/Word or Long variable.  
---|---  
Shifts | The number of shifts to perform.  
  
The ROTATE statement rotates all the bits in the variable to the left or right. All bits are preserved so no bits will be shifted out of the variable.

This means that after rotating a byte variable with a value of 1, eight times the variable will be unchanged.

When you want to shift out the MS bit or LS bit, use the SHIFT statement.

See also

[SHIFT](shift.md) , [SHIFTIN](shiftin.md) , [SHIFTOUT](shiftout.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rotate.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example for ROTATE and SHIFT statement

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

'dimension some variables

Dim B As Byte , I As Integer , L As Long

'the shift statement shift all the bits in a variable one

'place to the left or right

'An optional paramater can be provided for the number of shifts.

'When shifting out then number 128 in a byte, the result will be 0

'because the MS bit is shifted out

```
B = 1

Shift B , Left

```vb
Print B

'B should be 2 now

```
B = 128

Shift B , Left

```vb
Print B

'B should be 0 now

'The ROTATE statement preserves all the bits

'so for a byte when set to 128, after a ROTATE, LEFT , the value will

'be 1

'Now lets make a nice walking light

'First we use PORTB as an output

Config Portb = Output

'Assign value to portb

```
Portb = 1

```vb
Do

For I = 1 To 8

```
Rotate Portb , Left

```vb
'wait for 1 second

Wait 1

Next

'and rotate the bit back to the right

For I = 1 To 8

```
Rotate Portb , Right

```vb
Wait 1

Next

Loop

End

```