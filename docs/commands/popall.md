# POPALL

Action

Restores all registers that might be used by BASCOM.

Syntax

POPALL

Remarks

When you are writing your own ASM routines and mix them with BASIC you are unable to tell which registers are used by BASCOM because it depends on the used statements and interrupt routines that can run on the background.

That is why Pushall saves all used registers and POPALL restores all registers.

The SREG register is also saved/restored. The SREG register contains the processor flags and it is important to save these.

If the micro has a RAMPZ register, the RAMPZ register is saved/restored also. RAMPZ is used to address multiple pages in flash and SRAM memory.

See also

[PUSHALL](pushall.md)