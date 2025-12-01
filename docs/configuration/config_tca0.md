# CONFIG TCA0

Action

This configuration statement configures timer TCA0 found in the XTINY.

Syntax

CONFIG TCA0=mode, PRESCALE=prescale, RUN=run, LUPD=lupd , COMPAREx=compareX, RESOLUTION=resolution, EVENT_ACTION=event_action, OVF_INT=int, CMP0_INT=int, CMP1_INT=int, CMP2_INT=int

Remarks

At the moment of writing, all XTINY processors have one TIMER TCA0. This is a 16 bit timer with the following capabilities :

â¢ 16-Bit Timer/Counter

â¢ Three Compare Channels

â¢ Double Buffered Timer Period Setting

â¢ Double Buffered Compare Channels

â¢ Waveform Generation:

â Frequency generation

â Single-slope PWM (pulse-width modulation)

â Dual-slope PWM

â¢ Count on Event

â¢ Timer Overflow Interrupts/Events

â¢ One Compare Match per Compare Channel

â¢ Two 8-Bit Timer/Counters in Split Mode

We do not want to copy the data sheet info. You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer and/or Wave Generation mode.  Possible values : \- NORMAL, no wave generation (NORMAL) \- FREQ , frequency generation (FRQ) \- PWM , pulse width modulation single slope (SINGLESLOPE) \- PWM_TOP, pwm dual slope (DSTOP) \- PWM_TOPBOT, pwm dual slope (DSBOTH) \- PWM_BOT, pwm dual slope (DSBOTOM) \- A value between 0-7 will load the mode. See table 2.  
---|---  
PRESCALE | The pre scaler can divide the system clock that is applied to the timer. The pre scaler will only divide the system clock. Possible values : \- 1 , 2, 4, 8, 64, 256, 1024 \- OFF, timer is disabled  
RUN | This enables or disables the timer. Possible values : ON : timer will run OFF : timer will stop  
LUPD | Lock update. Possible values : MANUAL : LUPD in TCA.CTRLE not altered by system AUTO : LUPD in TCA.CTRLE set and cleared automatically  
CompareX COMPARExL COMPARExH | In the FRQ or PWM Waveform Generation mode, the PORT output register for the corresponding pin can be overridden. COMPARE0 will enable/disable WO0 COMPARE1 will enable/disable WO1 COMPARE2 will enable/disable WO2 DISABLE means : Port output settings for the pin with WOn output respected. ENABLE means : Port output settings for pin with WOn output overridden in FRQ or PWM Waveform Generation mode In SPLIT mode the counters are split into two 8 bit timers. The name COMPARE0 becomes COMPARE0L and COMPARE0H. Instead of WO0,WO1 and WO2, there are 3 additional outputs : WO3, WO4 and WO5.  
RESOLUTION | This option sets the resolution of the timer.  Possible value : \- NORMAL : 16 bit \- SPLIT : two 8 bit timers  
EVENT_ACTION | This option defines what kind of event action will increment or decrement. Possible values : \- DISABLED : counting on event input is disabled \- ENABLED, COUNT_POS_EDGE : count on positive edge event \- COUNT_ANY_EDGE : count on any edge event \- COUNT_HIGH_LVL : count on prescaled clock while event line is 1 \- COUNT_UPDOWN : count on prescaled clock. The event controls the count direction. Up counting when the event line is 0, down counting when the event line is 1.  
OVF_INT CMP0_INT CMP1_INT CMP2_INT | You can enable/disable interrupts in BASCOM using the ENABLE/DISABLE statement. You can also enable interrupts using the CONFIG statement. Possible values : ENABLED and DISABLED Possible interrupt sources you can set : OVF_INT : timer overflow/underflow interrupt CMP0_INT : compare channel 0 interrupt CMP1_INT : compare channel 1 interrupt CMP2_INT : compare channel 2 interrupt  
  
Table 2.

Value | Mode | TOP | UPDATE | EVENT  
---|---|---|---|---  
0 | NORMAL | PER | TOP | TOP  
1 | FREQ | CMP0 | TOP | TOP  
2 | reserved |   

3 | PWM, single slope | PER | BOTTOM | BOTTOM  
4 | reserved |   

5 | PWM, dual slope | PER | BOTTOM | TOP  
6 | PWM, dual slope | PER | BOTTOM | TOP and BOTTOM  
7 | PWM, dual slope | PER | BOTTOM | BOTTOM  
  
In normal AVR the ICR register is used to define the PWM frequency. In Xtiny the PER register must be used : TCA0_per = 8000 

The duty cycle can be loaded in the TCA0_CMP0 register (or a register of the other channels)

In normal AVR processors the timers had an alias to the counter register named TIMER0, TIMER1 , etc. 

Thus TIMER1 would access TIMER1 registers TCNT1L and TCNT1H. 

In the Xtiny, megaX. AVRX these aliases do not exist. There is however an alias to access word registers like a word. 

You can find these aliases in the DAT file under the [WIO] section.

For TCA0 you will find :

\- TCA0_CNT the timer counter register

\- TCA0_PER the period register

\- TCA0_CMP0 the compare 0 register

\- TCA0_CMP1 the compare 1 register

\- TCA0_CMP2 the compare 2 register

All relevant registers that form a word register like :

TCA0_CNTL=2592 ; 0A20 byte alias LSB see WIO

TCA0_CNTH=2593 ; 0A21 byte alias MSB see WIO

Will have an entry under the WIO section.

This is simply the name without the L/H

And the address is always the low register address.

Because the name is under the WIO section the variable/register will be treated as a 16 bit word. The correct read/write order will be used by the compiler which is different for AVR/XMEGA/XTINY

When you like to use your own definition or alias you could add an alias. Just take care that an update will replace the DAT files. 

For example if you like TIMER1 or TCA0 you can add it to the WIO section like this :

TCA0_CNT=2592 ; 0A20 word ## EXISTING ENTRY

TCA0 = 2592 ; NEW ENTRY

If you like an alias to be used you best write to support. When there is enough demand we add it.

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : TCA0-PWM.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates TCA0  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
'set the system clock and prescaler  
  
Config Sysclock = 16_20mhz , Prescale = 1 , Clockout = Enabled  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Waitms 2000  
  
Print "Test TCA0"  
  
Config Portb.0 = Output 'WO0 output  
  
Config Tca0 = Pwm_bot , Prescale = 1 , Resolution = Normal , Compare0 = Enabled , Run = On  
```
Tca0_per = 8000 'PWM frequency (period)  
Tca0_cmp0 = 2000 '25% duty cycle on pin PB0 (WO0)  
  
Do  
nop  
Loop