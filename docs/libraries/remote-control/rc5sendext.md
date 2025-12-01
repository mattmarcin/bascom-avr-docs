# RC5SENDEXT

Action

Sends extended RC5 remote code.

Syntax

RC5SENDEXT togglebit, address, command

Uses

TIMER1

Remarks

Togglebit | Make the toggle bit 0 or 32 to set the toggle bit  
---|---  
Address | The RC5 address  
Command | The RC5 command.  
  
Normal RC5 code uses 2 leading bits with the value '1'. After that the toggle bit follows.

With extended RC5, the second bit is used to select the bank. When you make it 1 (the default and normal RC5) the RC5 code is compatible. When you make it 0, you select bank 0 and thus use extended RC5 code.

The resistor must be connected to the OC1A pin. In the example a 2313 micro was used. This micro has pin portB.3 connected to OC1A.

Look in a data sheet for the proper pin when used with a different chip.

Most audio and video systems are equipped with an infra-red remote control.

The RC5 code is a 14-bit word bi-phase coded signal.

The two first bits are start bits, always having the value 1.

The next bit is a control bit or toggle bit, which is inverted every time a button is pressed on the remote control transmitter.

Five system bits hold the system address so that only the right system responds to the code.

Usually, TV sets have the system address 0, VCRs the address 5 and so on. The command sequence is six bits long, allowing up to 64 different commands per address.

The bits are transmitted in bi-phase code (also known as Manchester code).

An IR booster circuit is shown below:

![IRBOOST](irboost.gif)

See also

[CONFIG RC5](config_rc5.md) , [GETRC5](getrc5.md) , [RC6SEND](rc6send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sendrc5.bas

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

' RC5SEND is using TIMER1, no interrupts are used

' The resistor must be connected to the OC1(A) pin , in this case PB.3

Dim Togbit As Byte , Command As Byte , Address As Byte

```
Command = 12 ' power on off

Togbit = 0 ' make it 0 or 32 to set the toggle bit

Address = 0

```vb
Do

Waitms 500

' Rc5send Togbit , Address , Command

'or use the extended RC5 send code. You can not use both

'make sure that the MS bit is set to 1, so you need to send

'&B10000000 this is the minimal requirement

'&B11000000 this is the normal RC5 mode

'&B10100000 here the toggle bit is set

```
Rc5sendExt &B11000000 , Address , Command

```vb
Loop

End

```