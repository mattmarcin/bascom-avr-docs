# WAIT

Action

Suspends program execution for a given time.

Syntax

WAIT seconds

Remarks

seconds | The number of seconds to wait.  
---|---  
  
No accurate timing is possible with this command.

When you use interrupts, the delay may be extended.

See also

[DELAY](delay.md) , [WAITMS](waitms.md)

Example

```vb
WAIT 3 ' wait for three seconds

Print "*"

```