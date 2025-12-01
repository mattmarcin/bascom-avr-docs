# PEEK

Action

Returns the content of a register.

Syntax

var = PEEK( address )

Remarks

Var | Numeric variable that is assigned with the content of the memory location address  
---|---  
Address | Numeric variable or constant with the address location.(0-31)  
  
Peek() will read the content of a register.

Inp() can read any memory location

See also

[POKE](poke.md) , [CPEEK](cpeek.md) , [INP](inp.md) , [OUT](out.md) , [SETREG](setreg.md), [GETREG](getreg.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : peek.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates PEEk, POKE, CPEEK, INP and OUT

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m162def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim I As Integer , B1 As Byte

'dump internal memory

For I = 0 To 31 'only 32 registers in AVR

```
B1 = Peek(i) 'get byte from internal memory

```vb
Print Hex(b1) ; " ";

'Poke I , 1 'write a value into memory

Next

Print 'new line

'be careful when writing into internal memory !!

'now dump a part ofthe code-memory(program)

For I = 0 To 255

```
B1 = Cpeek(i) 'get byte from internal memory

```vb
Print Hex(b1) ; " ";

Next

'note that you can not write into codememory!!

```
Out &H8000 , 1 'write 1 into XRAM at address 8000

B1 = Inp(&H8000) 'return value from XRAM

```vb
Print B1

End

```