# SETREG

Action

Writes a byte value to an internal register.

Syntax

SETREG Reg , value

Remarks

Most AVR chips have 32 registers named R0-R31. Registers R16-R31 can be assigned directly. Register R0-R15 do not accept this.

In some cases you might want to write to the internal registers. While you can include some ASM code directly, you can also use the BASIC SETREG statment.

Reg | The register name : R0-R31 or a register definition.  
---|---  
Value | A constant or byte value to assign to the register.  
  
PEEK and POKE work with an address. And will return a HW register on the Xmega since Xmega has a different address map.

GetReg and SetReg will read/write registers on all AVR processors.

Internally the compiler will use R24 if you write a constant to register R0-R15 :

For example :

Setreg R0 , 1

Compiles into:

Ldi R24,$01

Mov R0, R24

Setreg R31 , 1

Compiles into:

Ldi R31,$01

![notice](notice.jpg)In version 2078, all internal registers (R0-R31) are made available as normal BYTE variables. This means that you can simply assign or read a register from basic : Rx=value.

This is more convenient than using SETREG and GETREG. 

See also

[GETREG](getreg.md) , [PEEK](peek.md) , [POKE](poke.md)

Example

Setreg R16,&HFF