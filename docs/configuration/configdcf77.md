# CONFIG DCF77

Action

Instruct the compiler to use DCF-77 radio signal to get atom clock precision time

Syntax

CONFIG DCF77 = pin , timer = timer [ INVERTED=inv, CHECK=check, UPDATE=upd, UPDATETIME=updtime , TIMER1SEC=tmr1sec, SWITCHPOWER=swpwr, POWERPIN=pin, POWERLEVEL = pwrlvl , SECONDTICKS=sectick ,DEBUG=dbg , GOSUB = Sectic , PULSE=pulse ]

Remarks

PIN | The input pin that is connected to the DCF-77 signal. This can be any micro processor pin that can be used as an input.  
---|---  
TIMER | The timer that is used to generate the compare interrupts, needed to determine the level of the DCF signal. Supported timers are : TIMER1. For Xmega : TCC0,TCC1,TCE0,TCE1,TCD0,TCD1,TCF0,TCF1 Xmega needs the MED priority set with [CONFIG PRIORITY](config_priority.md) because the MED priority is used for the timer interrupt. For Xtiny platform : TCA0, TCA1, TCAx  
INVERTED | This value is 0 by default. When you specify 1, the compiler will assume you use an inverted DCF signal. Most DCF-77 receivers have a normal output and an inverted output.  
CHECK | Check is 1 by default. The possible values are : 0 \- The DCF-77 parity bits are checked. No other checks are performed. Use it when you have exceptional signal strength 1 \- The received minutes are compared with the previous received minutes. And the difference must be 1. 2 \- All received values(minutes, hours, etc. ) are compared with their previous received values. Only the minutes must differ with 1, the other values must be exactly the same. This value uses more internal ram but it gives the best check. Use this when you have bad signal reception.  
UPDATE | Upd determines how often the internal date/time variables are updated with the DCF received values. The default value is 0. There are 3 possible values : 0 \- Continuous update. The date and time variables are updated every time the correct values have been received 1 \- Hourly update. The date and time variables are updated once an hour. 2\- Daily update. The date and time variables are updated once a day. The UPDATE value also determines the maximum value of the UPDATETIME option.  
UPDATETIME | This value depends on the used UPDATE parameter. When UPDATE is 1, the value must be in the range from 0-59. Start every hour at this minute with the new update. When UPDATE is 2, the value must be in the range from 0-23. Start every day at this hour with the new update. The default is 0.  
TIMER1SEC | 16 bit timers with the right crystal value can generate a precise interrupt that fires every second. This can be used to synchronize only once a day or hour with the DCF values. The remaining time, the 1-sec interrupt will update the soft clock. By default this value is 0.  
SWITCHPOWER | This option can be used to turn on/off the DCF-77 module with the control of a port pin. The default is 0. When you specify a value of 1, the DCF receiver will be switched off to save power, as soon as the clock is synchronized.  
POWERPIN | The name of a pin like pinB.2 that will be used to turn on/off the DCF module.  
POWERLEVEL | This option controls the level of the output pin that will result in a power ON for the module. 0 - When a logic 0 is applied to the power pin, the module is ON. 1 - When a logic 1 is applied to the power pin, the module is ON. Use a transistor to power the module. Do not power it from a port PIN directly. When you do power from a pin, make sure you sink the current. Ie : connect VCC to module, and GND of the module to ground. A logic 0 will then turn on the module.  
SECONDTICKS | The number of times that the DCF signal state is read. This is the number of times per second that the interrupt is executed. This value is calculated by the compiler. The highest possible timer pre scale value is used and the lowest possible number of times that the interrupt is executed. This gives least impact on your main application. You can override the value by defining your own value. For example when you want to run some own code in the interrupt and need it to execute more often.  
DEBUG | Optional value to fill 2 variables with debug info. DEBUG is on when a value of 1 is specified. By default, DEBUG is off. This has nothing to do with other DEBUG options of the compiler, it is only for the DCF77 code! When 1 is specified the compiler will create 2 internal variable named : bDCF_Pause and bDCF_Impuls. These values contain the DCF pulse length of the pause and the impulse. In the sample these values are printed.  
GOSUB | The Sectic option will call a label in the main program every second. You have to insert this label yourself. You must also end it with a RETURN. The option is the same as used with [CONFIG CLOCK](config_clock.md)  
PULSE | This is an optional parameter that sets the pulse time in mS. The default is 150. When you have hardware that requires a shorter or longer pulse you can try a slightly higher or lower value. At all times you should use a value between 100 and 200 where 150 would be the optimum value.  
  
The DCF decoding routines use a status byte. This byte can be examined as in the example.

The bits have the following meaning.

Bit | Explanation  
---|---  
0 | The last reading of the DCF pin.  
1 | This bit is reserved.  
2 | This Bit is set, if after a complete time-stamp at second 58 the time-stamp is checked and it is OK. If after a minute mark (2 sec pause) this bit is set, the time from the DCF-Part is copied to the Clock-Part and this bit reset too. Every second mark also resets this bit. So time is only set, if after second 58 a minute mark follows. Normally this bit is only at value 1 from Second 58 to second 60/00.  
3 | This Bit indicates, that the DCF-Part should be stopped, if time is set. (at the option of updating once per hour or day).  
4 | This Bit indicated that the DCF-Part is stopped.  
5 | This bit indicates, that the CLOCK is configured the way, that during DCF-Clock is stopped, there is only one ISR-Call in one second.  
6 | This Bit determines the level of the DCF input-pin at the pulse (100/200 mSec part).  
7 | This bit indicates, that the DCF-Part has set the time of the Clock-part.  
  
See Also

[DCF77TIMEZONE](dcf77timezone.md)

![notice](notice.jpg)You can read the Status-Bit 7 (DCF_Status.7), to check whether the internal clock was synchronized by the DCF-Part. You can also reset this Bit with [RESET](reset.md) DCF_Status.7. The DCF-Part will set this bit again, if a valid time-stamp is received.

You can read all other bits, but donât change them.

The DCF-77 signal is broadcasted by the German Time and Frequency department.

The following information is copied from :[ http://www.ptb.de/en/org/4/44/_index.htm](http://www.ptb.de/en/org/4/44/_index.md)

The main task of the department time and frequency is the realization and dissemination of the base unit time (second) and the dissemination of the legal time in the Federal Republic of Germany.

The second is defined as the duration of 9 192 631 770 periods of the radiation corresponding to the transition between the two hyper fine levels of the ground state of the cesium-133 atom.

For the realization and dissemination of the unit of time, the department develops and operates cesium atomic clocks as primary standards of time and frequency. In the past decades, these, as the worldwide most accurate atomic clocks, have contributed to the international atomic time scale (TAI) and represent the basis for the legal time in Germany. Dissemination of the legal time to the various users in industry, society, and research is performed via satellite, via a low frequency transmitter DCF77 and via an internet- and telephone service.

The department participates in the tests for the future European satellite navigation system âGalileoâ.

Presently the primary clocks realizing the time unit are augmented by Cs clocks with laser cooled atoms (âCs-fountain clocksâ) whose accuracy presently exceeds the clocks with thermal beams by a factor of 10 (frequency uncertainty of 1 . 10-15).

Future atomic clocks will most likely be based on atomic transitions in the optical range of single stored ions. Such standards are presently being developed along with the means to relate their optical frequencies without errors to radio-frequencies or 1 second pulsed.

As one may expect transitions in nuclei of atoms to be better shielded from environmental perturbations than electron-shell transitions which have been used so far as atomic clock references, the department attempts to use an optical transition in the nucleus of 229Th for a future generation of atomic clocks.

The work of the department is complemented by research in nonlinear optics (Solitons) and precision time transfer techniques, funded in the frame of several European projects and by national funding by Deutsche Forschungsgemeinschaft particularly in the frame of Sonderforschungsbereich 407 jointly with Hannover University.

The following information is copied from wikipedia : <http://en.wikipedia.org/wiki/DCF77>

The signal can be received in this area:

![dcf-77-area](dcf-77-area.png)

DCF77 is a long wave time signal and standard-frequency radio station. Its primary and backup transmitter are located in Mainflingen, about 25 km south-east of Frankfurt, Germany. It is operated by T-Systems Media Broadcast, a subsidiary of Deutsche Telekom AG, on behalf of the Physikalisch-Technische Bundesanstalt, Germany's national physics laboratory. DCF77 has been in service as a standard-frequency station since 1959; date and time information was added in 1973.

The 77.5 kHz carrier signal is generated from local atomic clocks that are linked with the German master clocks in Braunschweig. With a relatively-high power of 50 kW, the station can be received in large parts of Europe, as far as 2000 km from Frankfurt. Its signal carries an amplitude-modulated, pulse-width coded 1 bit/s data signal. The same data signal is also phase modulated onto the carrier using a 511-bit long pseudo random sequence (direct-sequence spread spectrum modulation). The transmitted data repeats each minute

Map showing the range of the DCF77 signal.

Map showing the range of the DCF77 signal.

* the current date and time;

* a leap second warning bit;

* a summer time bit;

* a primary/backup transmitter identification bit;

* several parity bits.

Since 2003, 14 previously unused bits of the time code have been used for civil defence emergency signals. This is still an experimental service, aimed to replace one day the German network of civil defense sirens.

The call sign stands for D=Deutschland (Germany), C=long wave signal, F=Frankfurt, 77=frequency: 77.5 kHz. It is transmitted three times per hour in morse code.

Radio clocks have been very popular in Europe since the late 1980s and most of them use the DCF77 signal to set their time automatically.

For further reference see wikipedia, a great on line information resource.

The DCF library parameters state diagram looks as following:

![DCF-Parameter](dcf-parameter.png)

```vb
If the SECTIC option is used, the Sectic Interrupt routine should not need more time, than to the next timer interrupt. If you use a timer for dcf (and softclock) usually with 40 tics per second, the Sectic routine should take only less than 25msec. 

If the Sectic routines needs more than this limit, you will lose accuracy of the softclock time (especially during the time, where the clock is not synchronized by DCF) and also measurement of the length of the DCF-pulses. 

If the SECTIC routine needs more time than the short DCF-pulse (100ms, with some instability in DCF-receiver may be 80ms) you will lose synchronization with the DCF-signal.

```
It is the principle of the DCF-routine, that the timer-interrupt measures the DCF-Pulse length and if you need more time in the interrupt routine as the duration from one timer interrupt to the next, you will get a problem.

Thus keep the SECTIC routine as short as possible and set a flag in the SECTIC routine, which is checked in a loop of the main-program. 

See also

[CONFIG DATE](config_date.md)

ASM

_DCF77 from DCF77.LBX is included by the compiler when you use the CONFIG statement.

Example

```vb
$regfile = "M88def.dat"

$crystal = 8000000

$hwstack = 128

$swstack = 128

$framesize = 128

$baud = 19200

'Config Dcf77 = Pind.2 , Debug = 1 , Inverted = 0 , Check = 2 , Update = 0 , Updatetime = 30 , Switchpower = 0 , Secondticks = 50 , Timer1sec = 1 , Powerlevel = 1 , Timer = 1

Config Dcf77 = Pind.2 , Timer = 1 , Timer1sec = 1 , Debug = 1

Enable Interrupts

Config Date = Dmy , Separator = .

Dim I As Integer

Dim Sec_old As Byte , Dcfsec_old As Byte

```
Sec_old = 99 : Dcfsec_old = 99 ': DCF_Debug_Timer = 0

```vb
' Testroutine fÃ¼r die DCF77 Clock

Print "Test DCF77 Version 1.00"

Do

For I = 1 To 78

Waitms 10

If Sec_old <> _sec Then

Exit For

End If

If Dcfsec_old <> Dcf_sec Then

Exit For

End If

Next

Waitms 220

```
Sec_old = _sec

Dcfsec_old = Dcf_sec

```vb
Print Time$ ; " " ; Date$ ; " " ; Time(dcf_sec) ; " " ; Date(dcf_day) ; " " ; Bin(dcf_status) ; " " ; Bin(dcf_bits) ; " " ; Bdcf_impuls ; " " ; Bdcf_pause

Loop

End

```
Example Xtiny

```vb
'---------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' DCF 77 demo to demonstrate the DCF77 library from Josef Vögel  
'---------------------------------------------------------  
$regfile = "avrx64da64.dat"  
$crystal = 24000000  
  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART connected to PA0 and PA1  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
  
Config Dcf77 = PINB.2 , Timer = Tca0 , Debug = 1 , Check = 1 , Gosub = Sectic  
  
Enable Interrupts  
Config Date = Dmy , Separator =DOT  
  
  
Dim I As Integer  
Dim Sec_old As Byte , Dcfsec_old As Byte  
  
```
Sec_old = 99 : Dcfsec_old = 99  
  
```vb
' Testroutine für die DCF77 Clock  
Print "Test DCF77 Version 1.02"  
  
Print "Configuration"  
  
  
Do  
For I = 1 To 78  
Waitms 10  
If Sec_old <> _sec Then  
Exit For  
End If  
If Dcfsec_old <> Dcf_sec Then  
Exit For  
End If  
Next  
Waitms 220  
```
Sec_old = _sec  
Dcfsec_old = Dcf_sec  
```vb
Print Time$ ; " " ; Date$ ; " " ; Time(dcf_sec) ; " " ; Date(dcf_day) ; " " ; Bin(dcf_status) ; " " ; Bin(dcf_parity) ; " " ; Bin(dcf_bits) ; " " ; Bdcf_impuls ; " " ; Bdcf_pause '; " " ; db1 ; " " ; db2  
If Dcf_sec > 45 Then  
Reset Dcf_status.7  
End If  
Print "Timezone : " ; Dcf77timezone()  
Loop  
  
  
'optional, is called every second by the library  
```
Sectic:  
!nop  
```vb
Return  
  
  
End

```