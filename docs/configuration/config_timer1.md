# CONFIG TIMER1

Action

Configure TIMER1.

Syntax

CONFIG TIMER1 = COUNTER | TIMER | PWM ,

EDGE=RISING | FALLING , PRESCALE= 1|8|64|256|1024 ,

NOISE_CANCEL=0 |1, CAPTURE_EDGE = RISING | FALLING ,

CLEAR_TIMER = 1|0,

COMPARE_A = CLEAR | SET | TOGGLE | DISCONNECT ,

COMPARE_B = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = 8 | 9 10 ,

COMPARE_A_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT

COMPARE_B_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT

[,CONFIGURATION=NAME]

Remarks

The TIMER1 is a 16 bit counter. See the hardware description of TIMER1.

It depends on the chip if COMPARE_B is available or not.

Some chips even have a COMARE_C.

The syntax shown above must be on one line. Not all the options need to be selected.

Here is the effect of the various options.

EDGE | You can select whether the TIMER will count on the falling or rising edge. Only for COUNTER mode.  
---|---  
CAPTURE_ EDGE | You can choose to capture the TIMER registers to the INPUT CAPTURE registers With the CAPTURE_EDGE = FALLING/RISING, you can specify to capture on the falling or rising edge of pin ICP  
NOISE_ CANCELING | To allow noise canceling you can provide a value of 1.  
PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024 PRESCALE can't be used in COUNTER mode.  
  
The TIMER1 also has two compare registers A and B

When the timer value matches a compare register, an action can be performed

COMPARE_A | The action can be: SET will set the OC1X pin CLEAR will clear the OC1X pin TOGGLE will toggle the OC1X pin DISCONNECT will disconnect the TIMER from output pin OC1X  
---|---  
  
And the TIMER can be used in PWM mode.

You have the choice between 8, 9 or 10 bit PWM mode

Also you can specify if the counter must count UP or down after a match to the compare registers

Note that there are two compare registers A and B

PWM | Can be 8, 9 or 10.  
---|---  
COMPARE_A_PWM | PWM compare mode. Can be CLEAR_UP or CLEAR_DOWN  
  
Using COMPARE_A, COMPARE_B, COMPARE_A_PWM or COMPARE_B_PWM will set the corresponding pin for output. When this is not desired you can use the alternative NO_OUTPUT version that will not alter the output pin.

For example : COMPARE_A_NO_OUTPUT , COMPARE_A_PWM NO_OUTPUT

CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : timer1.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show using Timer1

'micro : 90S8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8515def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim W As Word

'The TIMER1 is a versatile 16 bit TIMER.

'This example shows how to configure the TIMER

'First like TIMER0 , it can be set to act as a TIMER or COUNTER

'Lets configure it as a TIMER that means that it will count and that

'the input is provided by the internal clock.

'The internal clock can be divided by 1,8,64,256 or 1024

Config Timer1 = Timer , Prescale = 1024

'You can read or write to the timer with the COUNTER1 or TIMER1 variable

```
W = Timer1

Timer1 = W

```vb
'To use it as a COUNTER, you can choose on which edge it is trigereed

Config Timer1 = Counter , Edge = Falling 

'Config Timer1 = Counter , Edge = Rising

'Also you can choose to capture the TIMER registers to the INPUT CAPTURE registers

'With the CAPTURE EDGE = , you can specify to capture on the falling or rising edge of

'pin ICP

Config Timer1 = Counter , Edge = Falling , Capture_Edge = Falling 

'Config Timer1 = Counter , Edge = Falling , Capture Edge = Rising

'To allow noise canceling you can also provide :

Config Timer1 = Counter , Edge = Falling , Capture_Edge = Falling , Noise_Cancel = 1 

'to read the input capture register :

```
W = Capture1

'to write to the capture register :

Capture1 = W

```vb
'The TIMER also has two compare registers A and B

'When the timer value matches a compare register, an action can be performed

Config Timer1 = Counter , Edge = Falling , Compare_A = Set , Compare_B = Toggle , Clear_Timer = 1

'SET , will set the OC1X pin

'CLEAR, will clear the OC1X pin

'TOGGLE, will toggle the OC1X pin

'DISCONNECT, will disconnect the TIMER from output pin OC1X

'CLEAR TIMER will clear the timer on a compare A match

'To read write the compare registers, you can use the COMPARE1A and COMPARE1B variables

```
Compare1a = W

W = Compare1a

```vb
'And the TIMER can be used in PWM mode

'You have the choice between 8,9 or 10 bit PWM mode

'Also you can specify if the counter must count UP or down after a match

'to the compare registers

'Note that there are two compare registers A and B

Config Timer1 = Pwm , Pwm = 8 , Compare_A_Pwm = Clear_Up , Compare_B_Pwm = Clear_Down , Prescale = 1

'to set the PWM registers, just assign a value to the compare A and B registers

```
Compare1a = 100

Compare1b = 200

'Or for better reading :

Pwm1a = 100

Pwm1b = 200

End