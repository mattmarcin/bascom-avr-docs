# $SIM

Action

Instructs the compiler to generate empty wait loops for the WAIT and WAITMS statements. This to allow faster simulation.

Syntax

$SIM

Remarks

Simulation of a WAIT statement can take a long time especially when memory view windows are opened.

The $SIM compiler directive instructs the compiler to not generate code for WAITMS and WAIT. This will of course allows faster simulation.

When your application is ready you must remark the $SIM directive or otherwise the WAIT and WAITMS statements will not work as expected.

When you forget to remove the $SIM option and you try to program a chip you will receive a warning that $SIM was used.

See also

NONE

ASM

NONE

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

$sim

Do

Wait 1

Print "Hello"

Loop

```