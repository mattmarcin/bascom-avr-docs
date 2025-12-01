# CPEEK

Action

Returns a byte stored in code memory.

Syntax

var = CPEEK( address )

Remarks

Var | Numeric variable that is assigned with the content of the program memory at address. The cpeek() function returns one BYTE.  
---|---  
Address | Numeric variable or constant with the byte address location.  
  
So what is code memory? Code memory is the same as the flash memory where your program code is stored.

That is not the same memory as the EEPROM memory!

The code memory is exactly the same as the BIN file that the compiler creates.

So why is Cpeek() useful ? You could read the memory and perform a checksum to see if the code is valid.

Or you could check if a boot loader is present in the code.

There is no CPOKE statement because you can not write into program/code memory. Only a boot loader(a piece of code in a special area of the code memory) can write to the normal code memory.

Cpeek(0) will return the first byte of the flash code memory. Cpeek(1) will return the second byte of the flash code memory.

Cpeek() is limited to the first 64 KB of the code memory. For processors that have larger flash code memory like the Mega128 (128KB) you can use [CpeekH](cpeekh.md)().

While the AVR uses word addresses since all instructions are 2 bytes long, the Cpeek() function uses a byte address. You need to take that in consideration with for example a boot loader address. The Atmel data sheet will only mention word addresses. For example boot loader address $1000 in the data sheet is $2000 and $2001 byte address for Cpeek().

See also

[PEEK](peek.md) , [CPEEKH](cpeekh.md) , [POKE](poke.md) , [INP](inp.md) , [OUT](out.md), [SETREG](setreg.md), [GETREG](getreg.md)

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

$regfile = "m48def.dat" ' specify the used micro

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