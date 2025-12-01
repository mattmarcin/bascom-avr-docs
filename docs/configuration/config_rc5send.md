# CONFIG RC5SEND

Action

Defines the RC5SEND timer and WaveOutput pin.

Syntax

CONFIG RC5SEND = timer, WO=wo

Remarks

TIMER | The TIMER must be TCA0 or when available TCA1 or any oher TCA timer.  
---|---  
WO | The Wave Output pin (WO). This is WO0, WO1 or WO2.  
  
RC5SEND uses a TCA timer in frequency generating mode in order to create a 36 KHz carrier wave.

You can chose any available WO pin. You can also use the PORTMUX to use a different port. 

You must set the corresponding pin to OUTPUT mode using : CONFIG pin statement. The pin must also be set to 1. 

While the compiler could do all this it would need to deal with the portmux. The portmux is a great piece of hardware that allows you to chose alternative pin locations. 

When the compiler performs this automatic it would not be visible to the user. So we have chosen that we leave this to the user.

See also

[GETRC5](getrc5.md) , [RC5SEND](rc5send.md)

Example

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
  
Do  
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