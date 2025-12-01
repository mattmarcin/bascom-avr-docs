# CONFIG RC5

Action

Overrides the RC5 pin assignment from the [Option Compiler Settings](options_compiler_i2c__spi__1wire.md).

Syntax

CONFIG RC5 = pin [,TIMER=2] [,WAIT=value] [,MODE=BACKGROUND]

Syntax XTINY

CONFIG RC5 = pin [,TIMER=TCAx|TCBx] [,WAIT=value] [,MODE=BACKGROUND]

Remarks

Pin | The port pin to which the RC5 receiver is connected.  
---|---  
TIMER | Must be 2. The micro must have a timer2 when you want to use this option. This additional parameter will cause that TIMER2 will be used instead of the default TIMER0. XTINY : for the normal mode the timer can be TCAx or TCBx. For example TCA0. XTINY : for the background mode the timer can be only a TCBx timer like TCB0.  
WAIT | The default value is 100. Each unit is ca. 64 us. This gives a time out of 6.4 ms. Since a start bit is 3.5 ms, you can reduce the value to 56. When you make it lower, it will not work. When you want the old behavior you need to specify a value of 2000 which is ca. 131 ms. The WAIT parameter only has effect on the normal mode. It will not work with the BACKGROUND mode. When no valid RC5 start bit is detected, both command and address will be set to 255.   
MODE | The only possible value is BACKGROUND. The MODE parameter is optional. When used, an alternative library will be used to decode the RC5 signals on the background. This means that GETRC5 will not wait for a signal but that a bit will be set to indicate that a valid RC5 signal is received. This is bit : _rc5_bits.4 The variable _rc5_bits is automatically created when you use the MODE=BACKGROUND. This option is not available in the DEMO. The background mode will use a 16 bit timer in capture mode. It also means that you need to connect the IR-transmitter output pin to the ICP capture pin of the timer.  When using the background mode, you must specify a 16 bit timer. When you include a constant in your code like : CONST=_RC5_TOGGLE=1 , you will get the toggle bit in the address byte.5. Without this constant you will not get this bit. The prescaler value is calculated depending on the used crystal. Some desirable prescale values do not exist is some processors. Such as the 16 divider. In such a case you can override the automatic calculated value by specifying : PRESCALER=64. Typical you would try this when you get a compile error about a missing prescaler value. It is important that the PRESCALER precedes the MODE. Example : Config Rc5 = Pind.6 , Timer = 1 , PRESCALER=64, Mode = Background XTINY : For the Xtiny platform a TCBx timer is used. But the advantage of Xtiny is that you can use any processor pin. The Xtiny platform does require an additional configuration : the event system must be configured in a way that the the pin used for RC5 detection is routed to the timer TCB capture event.  We can do that like this :  
```vb
'setup RC5 and specify pin to use, and the timer which should be a timer type TCB !!!  
Config Rc5 = Pind.1 , Mode = Background , Timer = Tcb1  
Config Event_system = Dummy , Ch2 = Pd1 , Evsys_usertcb1capt = Ch2  
```
The PD1 (PIND.1) pin is the event generator since it will receive RC5 pulses. The timer TCB1 in the above sample, is the event user : it will get the generated event. We use the timer capture unit. In this example channel 2 is used to connect the event and the user. Notice that each channel can access a number of events. Other pins might requires a different channel! It is important that PIND.1 of config-rc5 matches the PD1 of config event_system.  And ch2 of PD1 must match the channel of the evsys_userTCBxcapt register.  
  
When you use different pins in different projects, you can use this statement to override the Options Compiler setting for the RC5 pin. This way you will remember which pin you used because it is in your code and you do not have to change the settings from the options. In BASCOM-AVR the settings are also stored in the project.CFG file. We recommend to use the CONFIG commands.

See also

[GETRC5](getrc5.md) , [RC5SEND](rc5send.md)

Example

```vb
'-------------------------------------------------------------------  
' RC5.BAS  
' (c) 1995-2025 MCS Electronics  
' based on Atmel AVR410 application note  
'-------------------------------------------------------------------  
$RegFile = "m88def.dat"  
  
$Baud = 19200  
$Crystal = 16000000  
  
'This example shows how to decode RC5 remote control signals  
'with a SFH506-35 IR receiver.  
  
'Connect to input to PIND.2 for this example  
'The GETRC5 function uses TIMER0 and the TIMER0 interrupt.  
'The TIMER0 settings are restored however so only the interrupt can not  
'be used anymore for other tasks  
  
  
'tell the compiler which pin we want to use for the receiver input  
  
Config Rc5 = PIND.2 , Wait = 2000  
Config Timer1 = Timer , Prescale = 1  
  
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
'Print Timer1 disable this line to see the different with the various WAIT constants  
```
GetRC5(Address , Command)  
  
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
Example MODE=background 

```vb
'----------------------------------------------------------------------------------------------------------  
' (c) 1995-2025  
' RC5-background.bas  
' this sample receives RC5 on the background. it will not block your code like getrc5  
' it requires a 16 bit timer with input capture. you can not use the timer yourself.  
' some processors have multiple 16 bit timers.  
'----------------------------------------------------------------------------------------------------------  
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Rc5 = Pinb.0 , Timer = 1 , Mode = Background  
' ^--- background interrupt mode  
' ^--- this must be a 16 bit timer  
' ^---- this is the timer input capture pin  
  
Enable Interrupts ' you must enable interrupts since input capture and overflow are used  
  
  
Print "RC5 demo"  
  
Do  
If _rc5_bits.4 = 1 Then ' if there is RC5 code received  
```
_rc5_bits.4 = 0 ' you MUST reset this flag in order to receive a new rc5 command  
  
```vb
Print "Address: " ; Rc5_address ' Address  
Print "Command: " ; Rc5_command ' Command  
End If  
Loop

```
Xtiny Background Example

```vb
'--------------------------------------------------------------------------------  
'name : avrx128da28-rc5-background.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 in background mode using timer TCB1  
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
Config Osc = Enabled , Frequency = 24MHZ  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'setup RC5 and specify pin to use, and the timer which should be a timer type TCB !!!  
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
  
print "RC5 test"  
  
Dim B As Byte  
Enable Interrupts 'since interrupts are used we must enable the global interrupt switch  
  
  
do  
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