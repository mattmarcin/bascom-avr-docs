# Remote Control Libraries

> RC5/RC6 infrared remote control

## GETRC5

Action

Retrieves the RC5 remote code from a IR transmitter.

Syntax

GETRC5( address, command )

Uses

TIMER0

Remarks

address | The RC5 address  
---|---  
command | The RC5 command.  
  
This statement is based on the AVR 410 application note. Since a timer is needed for accurate delays and background processing TIMER0 is used by this statement.

The interrupt of TIMER0 is also used by this statement.

TIMER0 can be used by your application since the values are preserved by the statement but a delay can occur. The interrupt can not be reused.

You may use any pin that can work as an input pin. Use the CONFIG RC5 statement to specify which pin is connected to the IR receiver.

GETRC5 supports extended RC5 code reception.

The SFH506-36 is used from Siemens. Other types can be used as well. The TSOP1736 has been tested with success.

You can also use the pin compatible TSOP31236

![SFH506](sfh506.jpg)

For a good operation use the following values for the filter.

![SFH506-2](sfh506-2.jpg)

![tsop312xx](tsop312xx.png)

TSOP 312xx

1=GND, 2=VSS, 3=OUT

Most audio and video systems are equipped with an infra-red remote control.

The RC5 code is a 14-bit word bi-phase coded signal.

The two first bits are start bits, always having the value 1.

The next bit is a control bit or toggle bit, which is inverted every time a button is pressed on the remote control transmitter.

Five system bits hold the system address so that only the right system responds to the code.

Usually, TV sets have the system address 0, VCRs the address 5 and so on. The command sequence is six bits long, allowing up to 64 different commands per address.

The bits are transmitted in bi-phase code (also known as Manchester code).

For extended RC5 code, the extended bit is bit 6 of the command.

The toggle bit is stored in bit 7 of the command.

Xmega

The Xmega will use timer TCC0 instead of TIMER0. 

You MUST enable the low priority interrupts since TCC0 is used in this mode. You can do this with this command :

Config Priority = Static , Vector = Application , Lo = Enabled

Xtiny

The Xtiny will use a TCAx or TCBx timer.

Alternative Background decoding normal AVR

A special alternative library named RC5.LIB can be used to decode the RC5 signals on the background. The developing of this library was sponsored by [Lumicoin](<http://www.lumicoin.de/>).

See [CONFIG RC5](config_rc5.md) for more information.

Alternative Background decoding Xtiny

A special alternative library named RC5_BG_XTINY.lib can be used to decode the RC5 signals on the background. The library is automatically included when you select the BACKGROUND mode.

See [CONFIG RC5](config_rc5.md) for more information and an example.

See also

[CONFIG RC5](config_rc5.md) , [RC5SEND](rc5send.md), [RC6SEND](rc6send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rc5.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : based on Atmel AVR410 application note

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'use byte library for smaller code

$lib "mcsbyte.lbx"

'This example shows how to decode RC5 remote control signals

'with a SFH506-35 IR receiver.

'Connect to input to PIND.2 for this example

'The GETRC5 function uses TIMER0 and the TIMER0 interrupt.

'The TIMER0 settings are restored however so only the interrupt can not

'be used anymore for other tasks

'tell the compiler which pin we want to use for the receiver input

Config Rc5 = Pind.2

'the interrupt routine is inserted automatic but we need to make it occur

'so enable the interrupts

Enable Interrupts

'reserve space for variables

Dim Address As Byte , Command As Byte

Print "Waiting for RC5..."

Do

'now check if a key on the remote is pressed

'Note that at startup all pins are set for INPUT

'so we dont set the direction here

'If the pins is used for other input just unremark the next line

'Config Pind.2 = Input

```
Getrc5(address , Command)

```vb
'we check for the TV address and that is 0

If Address = 0 Then

'clear the toggle bit

'the toggle bit toggles on each new received command

'toggle bit is bit 7. Extended RC5 bit is in bit 6

```
Command = Command And &B01111111

```vb
Print Address ; " " ; Command

End If

Loop

End

```
Example XTINY

```vb
'--------------------------------------------------------------------------------  
'name : avr128da28-getrc5.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 using time TCA0 and TCB0  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX128da28.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'we use the uart for some terminal output  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Rc5 = Pind.1 , Mode = Normal , Timer = Tca0  
' ^^^ use either a timer TCA0, TCA1 or a TCBx timer  
' ^^^^ define the pin that is connected to the output of the IR received  
' also have a look at the background mode that runs completely in the background!  
  
'since the timer is used in interrupt mode you must enabl global interrupts  
Enable Interrupts  
  
'reserve space for variables  
Dim Address As Byte , Command As Byte  
  
Print "Waiting for RC5..."  
  
do  
'now check if a key on the remote is pressed  
'Note that at startup all pins are set for INPUT  
'so we dont set the direction here  
'If the pins is used for other input just unremark the next line  
'Config Pind.2 = Input  
```
Getrc5(address , Command)  
```vb
'we check for the TV address and that is 0  
If Address = 0 Then  
'clear the toggle bit  
'the toggle bit toggles on each new received command  
'toggle bit is bit 7. Extended RC5 bit is in bit 6  
```
Command = Command And &B01111111  
```vb
Print Address ; " " ; Command  
End If  
'waitms 500  
loop

```

---

## RC5SEND

Action

Sends RC5 remote code.

Syntax

RC5SEND togglebit, address, command

Uses

TIMER1 or TCAx on Xtiny

Remarks

Togglebit | Make the toggle bit 0 or 32 to set the toggle bit  
---|---  
Address | The RC5 address  
Command | The RC5 command.  
  
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

XTINY

For XTINY platform timer TCA0 or TCA1 can be used. You can chose the WO0, WO1 or WO2 pin.

You must use the CONFIG RC5SEND directive to set up RC5SEND.

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

```
Rc5send Togbit , Address , Command

```vb
'or use the extended RC5 send code. You can not use both

'make sure that the MS bit is set to 1, so you need to send

'&B10000000 this is the minimal requirement

'&B11000000 this is the normal RC5 mode

'&B10100000 here the toggle bit is set

' Rc5sendext &B11000000 , Address , Command

Loop

End

```
Example XTINY

```vb
'--------------------------------------------------------------------------------  
'name : avrx128da28-rc5-background-send-receive.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 in background mode using timer TCB1  
' and RC5 transmission using TCA0  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 64  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'setup RC5 receive and specify pin to use, and the timer which should be a timer type TCB !!!  
Config Rc5 = Pind.1 , Mode = Background , Timer = Tcb1  
Config Event_system = Dummy , Ch2 = Pd1 , Evsys_usertcb1capt = Ch2  
'it is very important that you also configure the event system  
'you need to chose a channel that has access to the PIN used for the RC5 input in this case PIND.1  
'this pin will create an event when it changes. And you need to connect the TCB CAPTURE user to this channel  
'In this example we use TCB1 thus EVSYS_USER will be evsys_userTCB1CAPT, and since PD1 (pin D.1) is connected to  
'channel 2, we also need to select channel 2.  
'Now there is a path from PIN2.1 to TCB0, capture event  
'The compiler could have created this link too but then it is not clear to the user that this event channel is used  
'for this reason you need to configure it manual  
  
'for the RC5 transmission we need a TCA0 WOx pin. This pin is used in output mode.  
'we will use WO2 which is connected to PA2. you could use config port_mux to chose an altenative pin  
'the IR diode anode is connected to the power(vcc) and the cathode is connected to a 220 ohm resistor  
' the other end of the resistor is connected to the WO2 pin, porta.2 in this case  
Config Pina.2 = Output : Porta.2 = 1 'set the port direction and also set the pin high  
  
'we need this new command to select the timer (tca0 or when available tca1) and the WO pin  
'the timer is operated in frequency generation mode, 36 KHz for RC5  
Config Rc5send = Tca0 , Wo = Wo2  
  
Dim Bcmd As Byte  
Enable Interrupts 'since interrupts are used we must enable the global interrupt switch  
  
Print "RC5 test,REV:" ; Hex(syscfg_revid)  
  
do  
```
Incr Bcmd  
Rc5send 0 , 0 , Bcmd 'send RC5 code  
```vb
Waitms 500 'wait 500 msec  
  
'this is the background mode part that receives from the IR led or a remote control  
If _rc5_bits.4 = 1 Then 'this variable is automatically created  
```
_rc5_bits.4 = 0  
```vb
Print "Address: " ; Rc5_address 'auto created variable  
Print "Command: " ; Rc5_command 'auto created variable  
End If  
loop  
  
End  
  
  


```

---

## RC5SENDEXT

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

---

## RC6SEND

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

---

## SONYSEND

Action

Sends Sony remote IR code.

Syntax

SONYSEND address [, bits]

Uses

TIMER1

Remarks

Address | The address of the Sony device.  
---|---  
bits | This is an optional parameter. When used, it must be 12, 15 or 20. Also, when you use this option, the address variable must be of the type LONG.  
  
SONY CD Infrared Remote Control codes (RM-DX55)

Function | Hex | Bin  
---|---|---  
Power | A91 | 1010 1001 0001  
Play | 4D1 | 0100 1101 0001  
Stop | 1D1 | 0001 1101 0001  
Pause | 9D1 | 1001 1101 0001  
Continue | B91 | 1011 1001 0001  
Shuffle | AD1 | 1010 1101 0001  
Program | F91 | 1111 1001 0001  
Disc | 531 | 0101 0011 0001  
1 | 011 | 0000 0001 0001  
2 | 811 | 1000 0001 0001  
3 | 411 | 0100 0001 0001  
4 | C11 | 1100 0001 0001  
5 | 211 | 0010 0001 0001  
6 | A11 | 1010 0001 0001  
7 | 611 | 0110 0001 0001  
8 | E11 | 1110 0001 0001  
9 | 111 | 0001 0001 0001  
0 | 051 | 0000 0101 0001  
>10 | E51 | 1110 0101 0001  
enter | D11 | 1101 0001 0001  
clear | F11 | 1111 0001 0001  
repeat | 351 | 0011 0101 0001  
disc - | BD1 | 1011 1101 0001  
disc + | H7D1 | 0111 1101 0001  
|<< | 0D1 | 0000 1101 0001  
>>| | 8D1 | 1000 1101 0001  
<< | CD1 | 1100 1101 0001  
>> | 2D1 | 0010 1101 0001  

SONY Cassette | RM-J901) |   
Deck A |  |   
stop | 1C1 | 0001 1100 0001  
play > | 4C1 | 0100 1100 0001  
play < | EC1 | 1110 1100 0001  
>> | 2C1 | 0010 1100 0001  
<< | CC1 | 1100 1100 0001  
record | 6C1 | 0110 1100 0001  
pause | 9C1 | 1001 1100 0001  
Dec B |  |   
stop | 18E | 0001 1000 1110  
play > | 58E | 0101 1000 1110  
play < | 04E | 0000 0100 1110  
>> | 38E | 0011 1000 1110  
<< | D8E | 1101 1000 1110  
record | 78E | 0111 1000 1110  
pause | 98E | 1001 1000 1110  
  
\---[ SONY TV Infrared Remote Control codes (RM-694) ]--------------------------

program + = &H090 : 0000 1001 0000

program - = &H890 : 1000 1001 0000

volume + = &H490 : 0100 1001 0000

volume - = &HC90 : 1100 1001 0000

power = &HA90 : 1010 1001 0000

sound on/off = &H290 : 0010 1001 0000

1 = &H010 : 0000 0001 0000

2 = &H810 : 1000 0001 0000

3 = &H410 : 0100 0001 0000

4 = &HC10 : 1100 0001 0000

5 = &H210 : 0010 0001 0000

6 = &HA10 : 1010 0001 0000

7 = &H610 : 0110 0001 0000

8 = &HE10 : 1110 0001 0000

9 = &H110 : 0001 0001 0000

0 = &H910 : 1001 0001 0000

-/-- = &HB90 : 1011 1001 0000

For more SONY Remote Control info:

<http://www.fet.uni-hannover.de/purnhage/>

The resistor must be connected to the OC1A pin. In the example a 2313 micro was used. This micro has pin portB.3 connected to OC1A.

Look in a data sheet for the proper pin when used with a different chip.

An IR booster circuit is shown below:

![IRBOOST](irboost.gif)

When sending hex, prefix with &H. When sending binary data, prefix with &B.

Sonysend &HA90

Sonysend &B010011010001

See also

[CONFIG RC5](config_rc5.md) , [GETRC5](getrc5.md) , [RC5SEND](rc5send.md) , [RC6SEND](rc6send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sonysend.bas

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

Do

Waitms 500

```
Sonysend &HA90

```vb
Loop

End

```

---
