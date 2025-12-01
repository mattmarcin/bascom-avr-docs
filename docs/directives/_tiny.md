# $TINY

Action

Instruct the compiler to generate initialize code without setting up the stacks.

Syntax

$TINY

Remarks

The tiny11 for example is a powerful chip. It only does not have SRAM. BASCOM depends on SRAM for the hardware stack and software stack.

When you like to program in ASM you can use BASCOM with the $TINY directive.

Some BASCOM statements will also already work but the biggest part will not work.

A future version will support a subset of the BASCOM statements and function to be used with the chips without SRAM.

Note that the generated code is not yet optimized for the tiny parts. Some used ASM statements for example will not work because the chip does not support it.

See also

NONE

ASM

NONE

Example

```vb
$regfile = "attiny15.dat"  
$tiny  
$crystal = 1000000  
$noramclear  
$hwstack = 0  
$swstack = 0  
$framesize = 0  
  
Dim A As Iram Byte  
Dim B As Iram Byte  
```
A = 100 : B = 5  
A = A + B  
End