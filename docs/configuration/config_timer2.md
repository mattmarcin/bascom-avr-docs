# CONFIG TIMER2

Action

Configure TIMER2.

Syntax for the 8535

CONFIG TIMER2 = TIMER | PWM , ASYNC=ON |OFF,

PRESCALE = 1 | 8 | 32 | 64 | 128 | 256 | 1024 ,

COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = ON | OFF ,

COMPARE_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT ,

CLEAR_TIMER = 1|0

[,CONFIGURATION=NAME]

Syntax for the M103

CONFIG TIMER2 = COUNTER| TIMER | PWM ,

EDGE= FALLING |RISING,

PRESCALE = 1 | 8 | 64 | 256 | 1024 ,

COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = ON | OFF ,

COMPARE_PWM = CLEAR UP| CLEAR DOWN | DISCONNECT ,

CLEAR _TIMER = 1|0

[,CONFIGURATION=NAME]

Remarks

The TIMER2 is an 8 bit counter.

It depends on the chip if it can work as a counter or not.

The syntax shown above must be on one line. Not all the options need to be selected.

Some chips support multiple COMPARE outputs. Use COMPARE_A, COMPARE_B, COMPARE_C , etc.

Here is the effect of the various options.

EDGE | You can select whether the TIMER will count on the falling or rising edge. Only for COUNTER mode.  
---|---  
  
PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024 or 1 , 8, 32 , 64 , 256 or 1024 for the M103 Prescale can not be used in COUNTER mode.  
---|---  
  
The TIMER2 also has a compare registers

When the timer value matches a compare register, an action can be performed

COMPARE | The action can be: SET will set the OC2 pin CLEAR will clear the OC2 pin TOGGLE will toggle the OC2 pin DISCONNECT will disconnect the TIMER from output pin OC2  
---|---  
  
And the TIMER can be used in 8 bit PWM mode

You can specify if the counter must count UP or down after a match to the compare registers

COMPARE PWM | PWM compare mode. Can be CLEAR_UP or CLEAR_DOWN  
---|---  
  
CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

Example

```vb
Dim W As Byte

Config Timer2 = Timer , ASYNC = 1 , Prescale = 128

On TIMER2 Myisr

ENABLE INTERRUPTS

ENABLE TIMER2

DO

LOOP

```
MYISR:

```vb
'get here every second with a 32768 Hz xtal

RETURN

'You can read or write to the timer with the COUNTER2 or TIMER2 variable

```
W = Timer2

Timer2 = W