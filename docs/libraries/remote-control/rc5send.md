# RC5SEND

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