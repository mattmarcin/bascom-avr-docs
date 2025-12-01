# CONFIG TCXX

Action

Configures the Xmega TIMER.

Syntax

CONFIG TCxx = wg , PRESCALE=pre, COMPAREA=ca, COMPAREB=cb, COMPAREC=cc, COMPARED=cd, EVENT_SOURCE= event, EVENT_ACTION=act, EVENT_DELAY=ed, RESOLUTION=res

Remarks

Depending on the Xmega processor of your choice, there are one or more timers. The Xmega uses the name of the port as part of the name. The first port that has a timer is portC. The first timer is named TCC0. Most timer ports have 2 timers. The next timer is named TCC1. Xmega timers are 16 bit but can be cascaded to 32 bit timers or be set to 8 bit mode.

The possible timer names are : TCC0, TCC1, TCD0, TCD1, TCE0, TCE1, TCF0 and TCF1. 

WG | This options sets the Timer and/or Wave Generation mode.  Possible values : \- NORMAL, no wave generation \- FREQ , frequency generation \- PWM , pulse width modulation single slope \- PWM_TOP, pwm dual slope \- PWM_BOT, pwm dual slope \- PWM_TOPBOT, pwm dual slope \- A value between 0-7 will load the mode. See table 2. \- TIMER2. This will set the timer into byte mode.  
---|---  
PRESCALE or CLOCKSEL | The prescaler can divide the system clock that is applied to the timer. Possible values : \- 1 , 2, 4, 8, 64, 256, 1024 \- OFF, timer is disabled \- E0, E1, E2, E3, E4, E5, E6, E7 . Event channel 0-7 \- value between 0-15. This will write the value to the CTRLA register.  In the XMEGA, CLOCKSEL (clock selection) describes the parameter better than PRESCALE because of the additional options.  But the coded explorer will use PRESCALE from the DAT files.  In order not to break code the CLOCKSEL name will be dropped in a future version.  
COMPAREx | Where x is A, B, C, or D. This is the COMPARE or CAPTURE register setup. You may use either COMPARE or CAPTURE since the same registers are used. Each COMPARE/CAPTURE pin must be enabled if the input/output pin is used. By default they are disabled. Each TCx0 timer has 4 compare registers/pins. The TCx1 timer has two capture registers/pins. Possible values : ENABLED : this will enable the capture/compare register DISABLED : this will disable the capture/compare register 0 : this will set the logic level of the compare output pin to 0. 1 : this will set the logic level of the compare output pin to 1. In FREQ and PWM modes the compare pins will be set to output mode. In CAPTURE mode, the capture pin will be set to input mode. NOTE : NOT valid in TIMER2 mode.  
COMPAREx TIMER2 mode | In TIMER2 mode, there are 8 compare outputs. They have the names : CAPTUREAL , CAPTUREAH ,CAPTUREBL , CAPTUREBH, CAPTURECL, CAPTURECH,CAPTUREDL and CAPTUREDH. The last character indicates the Low or High byte. Each COMPARE/CAPTURE pin must be enabled if the input/output pin is used. By default they are disabled.  Possible values : ENABLED : this will enable the capture/compare ouput pin DISABLED : this will disable the capture/compare output pin 0 : this will set the logic level of the compare output pin to 0. 1 : this will set the logic level of the compare output pin to 1.  
EVENT_SOURCE | The event channel source. Possible values : \- OFF (default) \- E0-E7 \- A value between 0-15 NOTE : NOT valid in TIMER2 mode.  
EVENT_ACTION | The event action the timer will perform. Possible values : \- OFF \- CAPTURE, input capture \- UPDOWN, external controlled up/down count \- QDEC, quadrature decode \- RESTART , restart waveform period \- FREQ, frequency capture \- PWC, pulse width capture NOTE : NOT valid in TIMER2 mode.  
EVENT_DELAY | Enabled, or disabled(default). When this bit is set, the selected event source is delayed by one peripheral clock cycle. This feature is intended for 32-bit input capture operation. Adding the event delay is necessary for compensating for the carry propagation delay that is inserted when cascading two counters via the Event System. NOTE : NOT valid in TIMER2 mode.  
RESOLUTION | Valid options : NORMAL, BYTE, SPLIT. Timer resolution is 16 by default (NORMAL). A value of BYTE will set the timer to 8 bit resolution. SPLIT is reserved for future use.(cascading 32 bit timers ). When WG mode TIMER2 is chosen, the timer will be set into BYTE mode automatically.   
  
Table 2.

Value | Mode | TOP | UPDATE | EVENT  
---|---|---|---|---  
0 | NORMAL | PER | TOP | TOP  
1 | FREQ | CCA | TOP | TOP  
2 | reserved |   

3 | PWM, single slope | PER | BOTTOM | BOTTOM  
4 | reserved |   

5 | PWM, dual slope | PER | BOTTOM | TOP  
6 | PWM, dual slope | PER | BOTTOM | TOP and BOTTOM  
7 | PWM, dual slope | PER | BOTTOM | BOTTOM  
  
A CONFIG TCxx statement will update the timer control registers immediately. A pre scale value other than OFF will also [START](start.md) the timer at once.

![notice](notice.jpg)CONFIG TCxx statement must be placed in the main code. Or you may include it in the main code using $INCLUDE.

\- you can use CONFIG TCxx multiple times

\- do not use CONFIG TCxx in a SUB/FUNCTION in combination with SUBMODE=NEW. 

See Also

[START](start.md) , [STOP](stop.md)

Example 1:

```vb
'Counter/Timer D1 is used for overflow counter at --> 400ms  
'32MHz/256 = 125000

'32MHz/256 = 125000 --> 125000/2.5 = 50000 '400ms

'Or in other words: 50000 counts at 125Khz (8µSec per tick) = 50000 * 8µSec = 400mSec = 0.4 sec  
Config Tcd1 = Normal , Prescale = 256  
```
Tcd1_per = 50000 

You could use the overflow for example now as an interrupt (every 400ms) or feed it to the Event System (every 400ms).

Example 2:

The following example configuration counts the incoming events from Event Channel 7. You can use the Tcd0_cnt register to analyze the number of events.

Config Tcd0 = Normal , Prescale = E7 , Event_source = 7 , Event_action = Capture 

Example 3:

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-TIMER-S1.bas  
' This sample demonstrates the TIMER sample 1 from AVR1501  
' This sample uses TIMER TCD0 since TCC0 isused for the UART  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
'include the following lib and code, the routines will be replaced since they are a workaround  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
'connect portE bit 0 and 1 to some LED  
Config Porte = Output  
  
'config timer to normal mode  
Config Tcd0 = Normal , Prescale = 64  
```
Tcd0_per = &H30 ' period register  
  
```vb
Do  
If Inkey() <> 0 Then  
```
Tcd0_per = Tcd0_per + 100 ' increase period  
```vb
Print "period:" ; Tcd0_per ' you will see that a larger PERIOD value will cause the TIMER to

' overflow later and this generating a bigger delay  
End If  
```
Bitwait Tcd0_intflags.0 , Set ' wait for overflow  
Tcd0_intflags.0 = 1 ' clear flag by writing 1  
```vb
Toggle Porte ' toggle led  
Loop

```