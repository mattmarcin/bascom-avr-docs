# BITWAIT

Action

Wait until a bit is set or reset.

Syntax

BITWAIT x , SET/RESET

Remarks

X | Bit variable or internal register like PORTB.x , where x ranges from 0-7.  
---|---  
  
When using bit variables make sure that they are set/reset by software otherwise your program will stay in a loop.

When you use internal registers that can be set/reset by hardware such as PINB.0 this doesn't apply since this state can change as a result from for example a key press.

See also

NONE

ASM

Calls: NONE

Input: NONE

Output: NONE

Code : shown for address 0-31

label1:

Sbic PINB.0,label2 

Rjmp label1

Label2:

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim A As Bit

```
Bitwait A , Set 'wait until bit a is set

```vb
'the code above will loop forever since the bit 'A' is not set in software

'it could be set in an ISR routine

```
Bitwait Pinb.7 , Reset 'wait until bit 7 of Port B is 0.

End