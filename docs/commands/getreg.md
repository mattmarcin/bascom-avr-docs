# GETREG

Action

Reads a byte from an internal register.

Syntax

var = GETREG( Reg )

Remarks

Most AVR chips have 32 registers named R0-R31. The GetReg function will return the value of the specified register.

Reg | The register name : R0-R31 or a register definition.  
---|---  
Var | The name of a variable that will be assigned with the content of the register.  
  
PEEK and POKE work with an address. And will return a HW register on the Xmega since Xmega has a different address map.

GetReg and SetReg will read/write registers on all AVR processors.

![notice](notice.jpg)In version 2078, all internal registers (R0-R31) are made available as normal BYTE variables. This means that you can simply assign or read a register from basic : Rx=value.

This is more convenient than using SETREG and GETREG. 

See also

[SETREG](setreg.md), [PEEK](peek.md) , [POKE](poke.md)

Example