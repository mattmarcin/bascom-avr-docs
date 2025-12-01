# WAITMS

Action

Suspends program execution for a given time in mS.

Syntax

WAITMS mS

Remarks

Ms | The number of milliseconds to wait. (1-65535)  
---|---  
  
No accurate timing is possible with this command.

In addition, the use of interrupts can slow this routine.

See also

[DELAY](delay.md) , [WAIT](wait.md) , [WAITUS](waitus.md)

ASM

WaitMS will call the routine _WAITMS. R24 and R25 are loaded with the number of milliseconds to wait.

Uses and saves R30 and R31.

Depending on the used XTAL the asm code can look like :

_WaitMS:

_WaitMS1F:

Push R30 ; save Z

Push R31

_WaitMS_1:

Ldi R30,$E8 ; delay for 1 mS

Ldi R31,$03

_WaitMS_2:

Sbiw R30,1 ; -1

Brne _WaitMS_2 ; until 1 mS is ticked away

Sbiw R24,1

Brne _WaitMS_1 ; for number of mS

Pop R31

Pop R30

Ret

Example

```vb
WAITMS 10 ' wait for 10 mS

Print "*"

```