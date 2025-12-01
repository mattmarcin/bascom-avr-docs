# BREAK

Action

This statement will break the simulator/debugger.

Syntax

BREAK

Remarks

A number of new processors support the BREAK instruction. The break instruction will break execution of the simulator. This is support by the BASCOM simulator but also by Atmels Studio.

Processors that do not support the BREAK instruction interpret the BREAK instruction as a NOP (no operation). So it is safe to use on all processors.

The BREAK instruction uses 1 cycle just like the ASM NOP instruction.

See also

[NOP](nop.md)

Example

NONE