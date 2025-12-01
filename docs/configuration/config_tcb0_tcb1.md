# CONFIG TCB0-TCB1

Action

This configuration statement configures timer TCB0/TCB1 found in the XTINY.

Syntax

CONFIG TCB0|TCB1=mode, RUN=run, PRESCALE=prescale, RUNMODE=runmode , SYNCUPDATE=syncupdate, ASYNC=async, CCMP_INIT=ccmp_init, CCMP_OTP=ccmp_otp, FILTER=filter, EDGE=edge, CAPT_EVENT=ecapt_event, CAPT_INT=capt_int

Remarks

At the moment of writing, all XTINY processors have one TIMER TCB0. Some processors have 2 TCB timers like the tiny3216.

The second TCB timer is named TCB1.

The TCB is is a 16 bit timer with the following capabilities :

â¢ 16-Bit Counter Operation Modes:

â Periodic interrupt

â Time-out check

â Input capture

â¢ On event

â¢ Frequency measurement

â¢ Pulse-width measurement

â¢ Frequency and pulse-width measurement

â Single shot

â 8-bit Pulse-Width Modulation (PWM)

â¢ Noise Canceler on Event Input

â¢ Optional: Operation Synchronous with TCA0

You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer mode. Possible values : \- PERIODIC_INT : Periodic interrupt \- TIME_OUT_CHECK : time out check \- INP_CAP_EVENT : input capture event \- INP_CAP_FREQ : input capture frequency \- INP_CAP_PWM : input capture pulse with measurement \- INP_CAP_FREQ_PWM : input capture frequency width measurement \- SINGLE_SHOT : single shot \- PWM : 8 bit PWM \- A value between 0-7 will load the mode. See table 2.  
---|---  
PRESCALE | The pre scaler can divide the system clock that is applied to the timer. The pre scaler will divide the system clock. Possible values : \- 1 , 2 \- TCA0 : uses CLK_TCA from timer TCA0 \- OFF, timer is disabled  
RUN | This enables or disables the timer. Possible values : ON : timer will run OFF : timer will stop  
RUNMODE | Run in standby mode.  ENABLED : the timer runs in standby sleep mode.  Except when PRESCALE is set to TCA0. DISABLED : timer is stopped in standby sleep mode.  
SYNCUPDATE | Synchronize Update. ENABLED : TCB will restart whenever the TCA0 counter is restarted or overflows. This can be used to synchronize capture with the PWM period DISABLED : no sync   
ASYNC | Asynchronous Enabling. ENABLED : asynchronous updates of the TCB signal in single shot mode  The output will go HIGH when an event arrives DISABLED : The output will go HIGH when the counter starts after synchronization.  
CCMP_INIT | Compare/Capture PIN initial value. This setting is used to set the initial output value of the pin when an pin output is used. This bit has no effect in 8 bit PWM and single shot mode. LOW : initial pin state is low HIGH : initial pin state is high  
CCMP_OTP | Compare/Capture output enable. This option is used to set the output value of the compare/capture output DISABLED : Compare/capture output is zero. ENABLED : Compare/capture output has a valid value  
FILTER | Filter capture noise cancellation filter.  ENABLED : the input capture noise cancellation unit is enabled DISABLED : input capture noise cancellation unit is disabled.  
EDGE | Event Edge. This selects the event edge. The effect of this depends on the selected count mode.  | Mode | Edge | Positive Edge | Negative Edge  
---|---|---|---  
PERIODIC_INT | 0 1 | NA NA | NA NA  
TIME_OUT_CHECK | 0 1 | Start counter Stop counter | Stop counter Start counter  
INP_CAP_EVENT | 0 1 | Input capture freq and pulse with measurement mode NA | NA capture=count  
INP_CAP_FREQ | 0 1 | capture=count,init,int NA | NA capture=count, init, int  
INP_CAP_PWM | 0 1 | init capture=count, int | capture=count,int init  
SINGLE_SHOT | 0 1 | Start counter Start counter | NA Start counter  
PWM | 0 1 | NA NA | NA NA  
INP_CAP_FREQ_PWM | 0 | On 1st positive : init On following negative : capture On second positive : stop, int  
  
| 1 | On 1st negative : init On following positive : capture On second negative : stop, int  
  
CAPT_EVENT | Capture Event input enable. ENABLED : event input capture is enabled. DISABLED : event input capture is disabled  
CAPT_INT | All interrupts can be enabled/disabled using the ENABLE/DISABLE statements. The Capture interrupt enable can be enabled/disabled using the configuration parameter. ENABLED : capture interrupt is enabled DISABLED : capture interrupt is disabled  
  
See also

[CONFIG TCA0](config_tca0.md), [CONFIG_TCD0](config_tcd0.md)

Example