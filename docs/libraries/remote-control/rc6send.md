# RC6SEND

Action

Sends RC6 remote code.

Syntax

RC6SEND togglebit, address, command

Uses

TIMER1

Remarks

Togglebit | Make the toggle bit 0 or 1 to set the toggle bit  
---|---  
Address | The RC6 address  
Command | The RC6 command.  
  
The resistor must be connected to the OC1A pin. In the example a 2313 micro was used. This micro has pin portB.3 connected to OC1A.

Look in a data sheet for the proper pin when used with a different chip.

Most audio and video systems are equipped with an infrared remote control.

The RC6 code is a 16-bit word bi-phase coded signal.

The header is 20 bits long including the toggle bits.

Eight system bits hold the system address so that only the right system responds to the code.

Usually, TV sets have the system address 0, VCRs the address 5 and so on. The command sequence is eight bits long, allowing up to 256 different commands per address.

The bits are transmitted in bi-phase code (also known as Manchester code).

An IR booster circuit is shown below:

![IRBOOST](irboost.gif)

Device | Address  
---|---  
TV | 0  
VCR | 5  
SAT | 8  
DVD | 4  
  
This is not a complete list.

Command | Value | Command | Value  
---|---|---|---  
Key 0 | 0 | Balance right | 26  
Key 1 | 1 | Balance left | 27  
Key 2-9 | 2-9 | Channel search+ | 30  
Previous program | 10 | Channel search - | 31  
Standby | 12 | Next | 32  
Mute/un-mute | 13 | Previous | 33  
Personal preference | 14 | External 1 | 56  
Display | 15 | External 2 | 57  
Volume up | 16 | TXT submode | 60  
Volume down | 17 | Standby | 61  
Brightness up | 18 | Menu on | 84  
Brightness down | 19 | Menu off | 85  
Saturation up | 20 | Help | 129  
Saturation down | 21 | Zoom - | 246  
Bass up | 22 | Zoom + | 247  
Bass down | 23 |  |   
Treble up | 24 |  |   
Treble down | 25 |  |   
  
This list is by far not complete.

Since there is little info about RC6 on the net available, use code at your own risk!

See also

[CONFIG RC5](config_rc5.md) , [GETRC5](getrc5.md) , [RC5SEND](rc5send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sendrc6.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : code based on application note from Ger Langezaal

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

' +5V <\---[A Led K]---[220 Ohm]---> Pb.3 for 2313.

' RC6SEND is using TIMER1, no interrupts are used

' The resistor must be connected to the OC1(A) pin , in this case PB.3

Dim Togbit As Byte , Command As Byte , Address As Byte

'this controls the TV but you could use rc6send to make your DVD region free as well :-)

'Just search the net for the codes you need to send. Do not ask me for info please.

```
Command = 32 ' channel next

Togbit = 0 ' make it 0 or 32 to set the toggle bit

Address = 0

```vb
Do

Waitms 500

```
Rc6send Togbit , Address , Command

```vb
Loop

End

```