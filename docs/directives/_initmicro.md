# $INITMICRO

Action

Calls a user routine at startup to perform important initialization functions such as setting ports.

Syntax

$INITMICRO

Remarks

This directive will call a label named _INIT_MICRO just after the most important initialization is performed. You can put the _INIT_MICRO routine into your program, or you can put it in a library. Advantage of a library is that it is the same for all programs, and advantage of storing the code into your program is that you can change it for every program.  
---  
  
It is important that you end the routine with a RETURN as the label is called and expects a return.

The $initmicro can be used to set a port direction or value as it performs before the memory is cleared which can take some mS.

The best solution for a defined logic level at startup remains the usage of pull up/pull down resistors.

See Also

NONE

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 10  
$swstack = 10  
$framesize = 26

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

$initmicro

Print Version() 'show date and time of compilation

Print Portb

Do

```
nop

```vb
Loop

End

'do not write a complete application in this routine.

'only perform needed init functions

```
_init_micro:

Config Portb = Output

Portb = 3

Return