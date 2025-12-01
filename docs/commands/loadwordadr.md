# LOADWORDADR

Action

Loads the Z-register and sets RAMPZ if available.

Syntax

LOADWORDADR label

Remarks

label | The name of the label which address will be loaded into R30-R31 which form the Z-register.  
---|---  
  
The code that will be generated :

LDI R30,Low(label * 2)

LDI R31,High(label * 2)

LDI R24,1 or CLR R24

STS RAMPZ, R24

As the AVR uses a word address, to find a byte address we multiply the address with 2. RAMPZ forms together with pointer Z an address register. As the LS bit of Z is used to identify the lower or the upper BYTE of the address, it is extended with the RAMPZ to address more then 15 bits. For example the Mega128 has 128KB of space and needs the RAMPZ register set to the right value in order to address the upper or lower 64KB of space.

See also

[LOADLABEL](loadlabel.md), [LOADADR](loadadr.md) , [LOOKUP](lookup.md)

Example

LOADWORDADR label