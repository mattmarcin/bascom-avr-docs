# BITS

Action

Set all specified bits to 1.

Syntax

Var = Bits( b1 [,bn])

Remarks

Var | The BYTE/PORT variable that is assigned with the constant.  
---|---  
B1 , bn | A list of bit numbers that must be set to 1.  
  
While it is simple to assign a value to a byte, and there is special Boolean notation &B for assigning bits, the Bits() function makes it simple to assign a few bits.

B = &B1000001 : how many zeroâs are there?

This would make it more readable : B = Bits(0, 6)

You can read from the code that bit 0 and bit 6 are set to 1.

It does not save code space as the effect is the same.

It can only be used on bytes and port registers.

Valid bits are in range from 0 to 7.

See Also

[NBITS](nbits.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : bits-nbits.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo for Bits() AND Nbits()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'use in simulator : possible

'--------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

'while you can use &B notation for setting bits, like B = &B1000_0111

'there is also an alternative by specifying the bits to set

```
B = Bits(0 , 1 , 2 , 7) 'set only bit 0,1,2 and 7

```vb
Print B

'and while bits() will set all bits specified to 1, there is also Nbits()

'the N is for NOT. Nbits(1,2) means, set all bits except 1 and 2

```
B = Nbits(7) 'do not set bit 7

```vb
Print B

End

```