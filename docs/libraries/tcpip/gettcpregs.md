# GETTCPREGS

Action

Read a register value from the ethernet chip.

Syntax

var = GETTCPREGS(address, bytes)

Remarks

Address | The address of the register. This should not include the base address.  
---|---  
bytes | The number of bytes to read.  
  
Most options are implemented with BASCOM statements or functions. When there is a need to read from the ethernet registers you can use the GETTCPREGS function. It can read multiple bytes. 

![notice](notice.jpg)It is important that you specify the lowest address. This points to the MSB of the data. 

See also

[SETTCPREGS](settcpregs.md)

ASM

NONE

Example

[See SETTCPREGS](settcpregs.md)