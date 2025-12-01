# CPEEKH

Action

Returns a byte stored in code memory of micro processors with more then 64KB such as M103, M128.

Syntax

var = CPEEKH( address [,page] )

Remarks

Var | Numeric variable that is assigned with the content of the program memory at address. One byte is returned by the function.  
---|---  
address | Numeric variable or constant with the byte address location.  
page | A numeric variable or constant with the page address. Each page is 64 KB. Thus for the first 64 KB you would specify 0. For the second 64 KB you would specify 1.   
  
The similar Cpeek() function only works on the first 64 KB page. It was intended for processors with memory up to 64 KB.

When processors were made by Atmel with larger memory like the Mega128 (128 KB) the cpeekH() function was added.

The CpeekH() function uses the ELPM instruction instead of the LPM instruction that Cpeek() uses.

Since the memory is broken up in page of 64 KB, the cpeekH() function also access the memory in pages.

You can also omit the page number in which case the compiler will calculate the proper page address.

CpeekH(address,0) will work on the first page (first 64 KB)

CpeekH(address,1) will work on the second page (second 64 KB)

![notice](notice.jpg)When omitting the page, the compiler will calculate and load the page register automatically.

While the AVR uses word addresses since all instructions are 2 bytes long, the Cpeek() function uses a byte address. You need to take that in consideration with for example a boot loader address. The Atmel data sheet will only mention word addresses. For example boot loader address $1000 in the data sheet is $2000 and $2001 byte address for Cpeek().

See also

[PEEK](peek.md) , [POKE](poke.md) , [INP](inp.md) , [OUT](out.md) , [CPEEK](cpeek.md)

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