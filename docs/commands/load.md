# LOAD

Action

Load specified TIMER with a reload value.

Syntax

LOAD TIMER , value

Remarks

TIMER | TIMER0 , TIMER1 or TIMER2(or valid timer name)  
---|---  
Value | The variable or value to load.  
  
The TIMER0 does not have a reload mode. But when you want the timer to generate an interrupt after 10 ticks for example, you can use the LOAD statement.

It will do the calculation : (256-value)

So LOAD TIMER0, 10 will load the TIMER0 with a value of 246 so that it will overflow after 10 ticks.

TIMER1 is a 16 bit counter so it will be loaded with the value of 65536-value.

See Also

NONE

Example

NONE