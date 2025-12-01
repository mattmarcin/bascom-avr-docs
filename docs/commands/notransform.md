# $NOTRANSFORM

Action  
  
This option controls transformation of unsupported ASM mnemonics.

Syntax

$NOTRANSFORM ON|OFF

Remarks

By default, assembler mnemonics that are not supported for a chip or register are transformed into different assembler mnemonics.

The IN and OUT instructions for example only work on hardware registers with an address lower then 64. Most PORT registers are located in this lower address space, but there are many chips that have more ports which are located in extended memory. For such chips, using a IN or OUT on an extended address would result in a failure. 

Thus the compiler changes IN into an LDS and an OUT into an STS. When a register is required, R23 will be used except for SBIS/SBIC, these instructions use R0 when required.

When you develop some ASM code, you might want to get an error when you are using an instruction the wrong way. For this purpose you can turn off the transformation.

$NOTRANSFORM ON will turn off the transformation. And with $NOTRANSFORM OFF you can turn it back on.

You should only use this option in your own code. When you use it on your whole program, it will not compile since the bascom libraries which use CBI, SBI, SBIS, IN, OUT, etc. will use the transformation. 

See also

NONE

Example

NONE