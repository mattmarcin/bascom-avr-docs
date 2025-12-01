# CLOCKDIVISION

Action

Will set the system clock division available in some MEGA chips.

Syntax

CLOCKDIVISON = var

Remarks

Var | Variable or numeric constant that sets the clock division. Valid values are from 2-129. A value of 0 will disable the division.   
---|---  
  
On the MEGA 103 and 603 the system clock frequency can be divided so you can save power for instance. A value of 0 will disable the clock divider. The divider can divide from 2 to 127. So the other valid values are from 2 - 127.

Some routines that rely on the system clock will not work proper anymore when you use the divider. WAITMS for example will take twice the time when you use a value of 2.

Most new processors support a limited number of division factors which can be selected using [CONFIG CLOCKDIV](config_clockdiv.md).

See also

[POWERSAVE](powersave.md) , [CONFIG CLOCKDIV](config_clockdiv.md)

Example

```vb
$regfile = "m103def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Clockdivision = 2