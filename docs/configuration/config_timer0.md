# CONFIG TIMER0

Action

Configure TIMER0.

Syntax

```vb
CONFIG TIMER0 = COUNTER , EDGE=RISING/FALLING , CLEAR_TIMER = 1|0 [,CONFIGURATION=NAME]

CONFIG TIMER0 = TIMER , PRESCALE= 1|8|64|256|1024 [,CONFIGURATION=NAME]

CONFIG TIMER2 = TIMER | PWM , ASYNC=ON |OFF,PRESCALE = 1 | 8 | 32 | 64 | 128 | 256 | 1024 ,COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,PWM = ON | OFF ,COMPARE_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT ,CLEAR_TIMER = 1|0 [,CONFIGURATION=NAME]

```
Remarks

TIMER0 is an 8 bit counter. See the hardware description of TIMER0.

When configured as a COUNTER:

EDGE | You can select whether the TIMER will count on the falling or rising edge.  
---|---  
  
When configured as a TIMER:

PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024  
---|---  
  
Note that some new AVR chips have different pre scale values. You can use these.

CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

![notice](notice.jpg) Notice that the Help was written with the AT90S2313 and AT90S8515 timers in mind.

When you use the CONFIG TIMER0 statement, the mode is stored by the compiler and the TCCRO register is set.

When you use the STOP TIMER0 statement, the TIMER is stopped.

When you use the START TIMER0 statement, the TIMER TCCR0 register is loaded with the last value that was configured with the CONFIG TIMER0 statement.

So before using the [START](start.md) and [STOP](stop.md) TIMER0 statements, use the CONFIG statement first.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : timer0.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to use TIMER0 related statements

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'First you must configure the timer to operate as a counter or as a timer

'Lets configure it as a COUNTER now

'You must also specify if it will count on a rising or falling edge

Config Timer0 = Counter , Edge = Rising

'Config Timer0 = Counter , Edge = falling

'unremark the line aboven to use timer0 to count on falling edge

'To get/set the value from the timer access the timer/counter register

'lets reset it to 0

```
Tcnt0 = 0

```vb
Do

Print Tcnt0

Loop Until Tcnt0 >= 10

'when 10 pulses are count the loop is exited

'or use the special variable TIMER0

```
Timer0 = 0

```vb
'Now configire it as a TIMER

'The TIMER can have the systemclock as an input or the systemclock divided

'by 8,64,256 or 1024

'The prescale parameter excepts 1,8,64,256 or 1024

Config Timer0 = Timer , Prescale = 1

'The TIMER is started now automaticly

'You can STOP the timer with the following statement :

```
Stop Timer0

```vb
'Now the timer is stopped

'To START it again in the last configured mode, use :

```
Start Timer0

```vb
'Again you can access the value with the tcnt0 register

Print Tcnt0

'or

Print Timer0

'when the timer overflows, a flag named TOV0 in register TIFR is set

'You can use this to execute an ISR

'To reset the flag manual in non ISR mode you must write a 1 to the bit position

'in TIFR:

Set Tifr.1

'The following code shows how to use the TIMER0 in interrupt mode

'The code is block remarked with '( en ')

'(

'Configute the timer to use the clock divided by 1024

Config Timer0 = Timer , Prescale = 1024

'Define the ISR handler

On Ovf0 Tim0_isr

'you may also use TIMER0 for OVF0, it is the same

Enable Timer0 ' enable the timer interrupt

Enable Interrupts 'allow interrupts to occur

Do

'your program goes here

Loop

'the following code is executed when the timer rolls over

```
Tim0_isr:

```vb
Print "*";

Return

')

End

```