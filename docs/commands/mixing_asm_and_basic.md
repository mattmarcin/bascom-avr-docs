# Mixing ASM and BASIC

BASCOM allows you to mix BASIC with assembly.

This can be very useful in some situations when you need full control of the generated code.

In order to use ASM you must start the line with the character !

Optional you can create a block of ASM using $ASM end $END ASM

Use CTRL + SPACE to get a list of ASM mnemonics.

```vb
For example :

Dim a As Byte At &H60 ' A is stored at location &H60

```
!Ldi R27 , $00 ' Load R27 with MSB of address

!Ldi R26 , $60 ' Load R26 with LSB of address

!Ld R1, X ' load memory location $60 into R1

!SWAP R1 ' swap nibbles

As you can see the SWAP mnemonic is preceded by a ! sign. Without it, it would be the BASIC SWAP statement.

Another option is to use the assembler block directives:

$ASM

Ldi R27 , $00 ' Load R27 with MSB of address

Ldi R26 , $60 ' Load R26 with LSB of address

Ld R1, X ' load memory location $60 into R1

SWAP R1 ' swap nibbles

$END ASM

A special assembler helper function is provided to load the address into the register X or Z. Y can may not be used because it is used as the soft stack pointer.

Dim A As Byte ' reserve space

LOADADR a, X ' load address of variable named A into register pair X

This has the same effect as :

Ldi R26, $60 ' for example !

Ldi R27, $00 ' for example !

Some registers are used by BASCOM

R4 and R5 are used to point to the stack frame or the temp data storage

R6 is used to store some bit variables:

R6 bit 0 = flag for integer/word conversion

R6 bit 1 = temp bit space used for swapping bits

R6 bit 2 = error bit (ERR variable)

R6 bit 3 = show/noshow flag when using INPUT statement

R8 and R9 are used as a data pointer for the READ statement.

All other registers are used depending on the used statements.

To Load the address of a variable you must enclose them in brackets.

Dim B As Bit

Lds R16, {B} 'will replace {B} with the address of variable B

To refer to the bit number you must precede the variable name by BIT.

Sbrs R16 , BIT.B 'notice the point!

Since this was the first dimensioned bit the bit number is 7. Bits are stored in bytes and the first dimensioned bit goes in the MS (most significant) bit.

To load an address of a label you must use :

LDI ZL, Low(lbl * 1)

LDI ZH, High(lbl * 1)

Where ZL = R30 and may be R24, R26, R28 or R30

And ZH = R31 and may be R25, R27, R29 or R31.

These are so called register pairs that form a pointer.

When you want to use the LPM instruction to retrieve data you must multiply the address with 2 since the AVR object code consist of words.

LDI ZL, Low(lbl * 2)

LDI ZH, High(lbl * 2)

LPM ; get data into R0

Lbl:

Atmel mnemonics must be used to program in assembly.

You can download the pdf from www.atmel.com that shows how the different mnemonics are used.

Some points of attention :

* All instructions that use a constant as a parameter only work on the upper 16 registers (r16-r31)

So LDI R15,12 WILL NOT WORK

* The instruction SBR register, K

will work with K from 0-255. So you can set multiple bits!

The instruction SBI port, K will work with K from 0-7 and will set only ONE bit in a IO-port register.

The same applies to the CBR and CBI instructions.

You can use constants too:

.equ myval = (10+2)/4

ldi r24,myval+2 '5

ldi r24,asc("A")+1 ; load with 66

Or in BASIC with CONST :

CONST Myval = (10+2) / 4

Ldi r24,myval

How to make your own libraries and call them from BASIC?

The files for this sample can be found as libdemo.bas in the SAMPLES dir and as mylib.lib in the LIB dir.

First determine the used parameters and their type.

Also consider if they are passed by reference or by value

For example the sub test has two parameters:

x which is passed by value (copy of the variable)

y which is passed by reference(address of the variable)

In both cases the address of the variable is put on the soft stack which is indexed by the Y pointer.

The first parameter (or a copy) is put on the soft stack first

To refer to the address you must use:

ldd r26 , y + 0

ldd r27 , y + 1

This loads the address into pointer X

The second parameter will also be put on the soft stack so :

The reference for the x variable will be changed :

To refer to the address of x you must use:

ldd r26 , y + 2

ldd r27 , y + 3

To refer to the last parameter y you must use

ldd r26 , y + 0

ldd r27 , y + 1

Write the sub routine as you are used too but include the name within brackets []

[test]

test:

ldd r26,y+2 ; load address of x

ldd r27,y+3

ld r24,x ; get value into r24

inc r24 ; value + 1

st x,r24 ; put back

ldd r26,y+0 ; address of y

ldd r27,y+1

st x,r24 ; store

ret ; ready

[end]

To write a function goes the same way.

A function returns a result so a function has one additional parameter.

It is generated automatic and it has the name of the function.

This way you can assign the result to the function name

```vb
For example:

Declare Function Test(byval x as byte , y as byte) as byte

```
A virtual variable will be created with the name of the function in this case test.

It will be pushed on the soft stack with the Y-pointer.

To reference to the result or name of the function (test) the address will be:

y + 0 and y + 1

The first variable x will bring that to y + 2 and y + 3

And the third variable will cause that 3 parameters are saved on the soft stack

To reference to test you must use :

ldd r26 , y + 4

ldd r27 , y + 5

To reference variable x

ldd r26 , y + 2

ldd r27 , y + 3

And to reference variable y

ldd r26 , y + 0

ldd r27 , y + 1

When you use exit sub or exit function you also need to provide an additional label. It starts with sub_ and must be completed with the function / sub routine name. In our example:

sub_test:

LOCALS

When you use local variables thing become more complicated.

Each local variable address will be put on the soft stack too

When you use 1 local variable its address will become

ldd r26, y+0

ldd r27 , y + 1

All other parameters must be increased with 2 so the reference to y variable changes from

ldd r26 , y + 0 to ldd r26 , y + 2

ldd r27 , y + 1 to ldd r27 , y + 3

And of course also for the other variables.

When you have more local variables just add 2 for each.

Finally you save the file as a .lib file

Use the library manager to compile it into the lbx format.

The declare sub / function must be in the program where you use the sub / function.

The following is a copy of the libdemo.bas file :

```vb
' define the used library

$lib "mylib.lib"

'also define the used routines

$external Test

'this is needed so the parameters will be placed correct on the stack

Declare Sub Test(byval X As Byte , Y As Byte)

'reserve some space

Dim Z As Byte

'call our own sub routine

```
Call Test(1 , Z)

```vb
'z will be 2 in the used example

End

```
When you use ports in your library you must use .equ to specify the address:

.equ EEDR=$1d

In R24, EEDR

This way the library manager knows the address of the port during compile time.

As an alternative precede the mnemonic with a * so the code will not be compiled into the lib. The address of the register will be resolved at run time in that case.

This chapter is not intended to teach you ASM programming. But when you find a topic is missing to interface BASCOM with ASM send me an email.

Translation

In version 1.11.7.5 of the compiler some mnemonics are translated when there is a need for.

For example, SBIC will work only on normal PORT registers. This because the address may not be greater then 5 bits as 3 bits are used for the pin number(0-7).

SBIC worked well in the old AVR chips(AT90Sxxxx) but in the Mega128 where PORTG is on a high address, it will not work.

You always needs a normal register when you want to manipulate the bits of an external register.

For example :

LDS r23, PORTG ; get value of PORTG register

SBR r23,128 ; set bit 7

STS PORTG, R23

The mnemonics that are translated by the compiler are : IN, OUT, SBIC, SBIS, SBI and CBI.

The compiler will use register R23 for this. So make sure it is not used.

Special instructions

ADR Label ; will create a word with the address of the label name

ADR2 Label ; will create a word with the address of the label name, multiplied by 2 to get the byte address 

; since word addresses are used. This is convenient when loading the Z-pointer to use (E)LPM.

.align ; This directive will align the code to a 256 byte page so that the address LSB becomes 0. 

; When storing data at an address where the LSB is zero, you can test for an overflow of the MSB only.