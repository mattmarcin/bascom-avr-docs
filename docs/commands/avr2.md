# AVR

This topic describes some general hardware related problems that were found by users.

Unexpected brown out

\- Processors with analog ports (used for A/D) are connected to AVCC and not VCC. This can cause the brown out detection to trigger. For example this is true for the Mega1284 PORTC. Using the ports to switch a small load would trigger the brown out while using a different port, powered from VCC would not give this problem. 

Errata

The Errata you will find in the data sheet of the processor. It contains information about bugs in the hardware. Some times there are work around's, and some times there is no solution. It is a good idea to read the Errata BEFORE you begin to use the processor for a new design.