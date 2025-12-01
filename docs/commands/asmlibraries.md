# ASM Libraries and Add-Ons

ASM Libs are libraries that are used by the compiler.

They contain machine language statements for various statements and functions.

A library can also be used to modify an existing function.

For example when you use a conversion routine num<>string with a byte variable only, the routine from the MCS.LIB has some overhead as it can also convert integers,word and longs.

You can specify the MCSBYTE.LIB or MCSBYTE.LBX library then to override the function from MCS.LIB.

When you write a user sub/function that calls a user lib and passed parameters, you must include some code to restore the frame protection.

In the bcd.lib you can find code like :

#IF _FPROTECT

Out sreg,r3 ; restore I flag

#ENDIF

The bcd.lib and bin2bcd.bas demonstrate how to write a user lib.

The mylib.lib example contains more details about passing variables. 

A lib must be included with the $LIB directive.

When the library contains an overloaded version of a sub/function it is important that you put the $LIB directive early in your code. 

You can also change the behavior of a sub by putting the code in your own lib.

For example consider the _FLIPBYTE code from mcs.lib 

;flip or mirror bits in register R24

;1001_0000 becomes 0000_1001

[_FLIPBYTE]

_FLIPBYTE: 

push r16 ; save regs 

push r17 

ldi r16,8 ; num of bits 

_FLIPBYTE2: 

rol r24 ; rotate left through carry

ror r17 ; get in r17 rotate right 

dec r16 ; next 

brne _FLIPBYTE2

mov r24, r17 

pop r17 

pop r16 

ret 

[END]

you could put this code into a new lib named fliplib.lib

Then include it with $|LIB "fliplib.lib"

The compiler will use the code from your lib when you include it. The lib code is automatically called when using FLIP() .

You may not share libs where you copied the code from the BASCOM libraries. These are protected by copyright. So when it is required to share libs you need to ask permission. 

When you share a forked lib with another user that has a valid license there is no problem. But when you modify some code and put it on the internet, it could be a problem. 

You can access variables by using brackets :

lds r24, {bSomeVar} ; load into r24 the content from the byte variable bSomeVar

When you want to compile your own lib using LibManager, you should put a asterisk infrom of the code like :

* lds r24, {bSomeVar} ; load into r24 the content from the byte variable bSomeVar

This will leave the line as it is. This is required because when you compile the lib there is no reference to the variable. This variable exist only in your main program

The * will leave the line alone and it will be compiled during compilation of the main program.

What to save?

There is no need to save registers. You can trash them all.

When it is required to change RAMPZ you should protect the value. Then like with normal asm programming, there are some registers you should not alter like R4,R5,R6,R8-R9 and the Y pointer R28-R29.