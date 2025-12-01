# WAITUS

Action

Suspends program execution for a given time in uS.

Syntax

WAITUS uS

Remarks

US | The number of microseconds to wait. (1-65535) This must be a constant. Not a variable! In version 1.12.x.x and higher you can use a variable as well.  
---|---  
  
No accurate timing is possible with this command. For accurate timing you can best use a timer.

In addition, the use of interrupts can slow down this routine.

The minimum delay possible is determined by the used frequency.

The number of cycles that are needed to set and save registers is 17.

When the loop is set to 1, the minimum delay is 21 uS. In this case you can better use a NOP that generates 1 clock cycle delay.

At 4 MHz the minimum delay is 5 uS. So a waitus 3 will also generate 5 uS delay.

Above these values the delay will become accurate.

In version 2.0.7.6 the compiler will create different code depending on the $CRYSTAL value and the specified delay.

When you use a constant, the timing is reasonable accurate. When using a variable, the timing accuracy depends on the oscillator speed.

As a general rule : the higher the clock speed, the better the result. 

When you really need an accurate delay you should use a timer.

Set the timer to a value and poll until the overflow flag is set. The disadvantage is that you can not use the timer for other tasks during this hardware delay.

The philosophy behind BASCOM is that it should not use hardware resources unless there is no other way to accomplish a task.

See also

[DELAY](delay.md) , [WAIT](wait.md) , [WAITMS](waitms.md)

Example

WAITUS 10 ' wait for 10 uS

Print "*"