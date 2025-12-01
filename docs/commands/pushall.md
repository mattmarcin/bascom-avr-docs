# PUSHALL

Action

Saves all registers that might be used by BASCOM.

Syntax

PUSHALL

Remarks

When you are writing your own ASM routines and mix them with BASIC you are unable to tell which registers are used by BASCOM because it depends on the used statements and interrupt routines that can run on the background.

That is why Pushall saves all used registers. Use POPALL to restore the registers.

The saved registers are : R0-R5, R7,R10,R11 and R16-R31

The SREG register is also saved. The SREG register contains the processor flags and it is important to save these.

If the micro has a RAMPZ register, the RAMPZ register is saved too. RAMPZ is used to address multiple pages in flash and SRAM memory.

In order to save SREG a register is required. R24 was used for that till version 2086. In version 2087 R25 is used. This because R24 is used to pass data and the value would be altered by the operation. Of course an additional push/pop could be used but this take time.

So when it is essential that after PUSHALL statement all registers have the same value, you must save R25 yourself using this code :

!push R25

PUSHAL

!pop R25

See also

[POPALL](popall.md)