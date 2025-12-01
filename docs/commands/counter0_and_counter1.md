# COUNTER0 and COUNTER1

Action

Set or retrieve the internal 16 bit hardware register.

Syntax

COUNTER0 = var var = COUNTER0 | TIMER0 can also be used  
---|---  
COUNTER1 = var var = COUNTER1 | TIMER1 can also be used  
CAPTURE1 = var var = CAPTURE1 | TIMER1 capture register  
COMPARE1A = var var = COMPARE1A | TIMER1 COMPARE A register  
COMARE1B = var var = COMPARE1B | TIMER1 COMPARE B register  
PWM1A = var var = PWM1A | TIMER1 COMPAREA register. (Is used for PWM)  
PWM1B = var var = PRM1B | TIMER1 COMPARE B register. (Is used for PWM)  
  
Remarks

Var | A byte, Integer/Word variable or constant that is assigned to the register or is read from the register.  
---|---  
  
Because the above 16 bit register pairs must be accessed somewhat differently than you may expect, they are implemented as variables.

The exception is TIMER0/COUNTER0, this is a normal 8 bit register and is supplied for compatibility with the syntax.

When the CPU reads the low byte of the register, the data of the low byte is sent to the CPU and the data of the high byte is placed in a temp register. When the CPU reads the data in the high byte, the CPU receives the data in the temp register.

When the CPU writes to the high byte of the register pair, the written data is placed in a temp register. Next when the CPU writes the low byte, this byte of data is combined with the byte data in the temp register and all 16 bits are written to the register pairs. So the MSB must be accessed first.

All of the above is handled automatically by BASCOM when accessing the above registers.

Note that the available registers may vary from chip to chip.

The BASCOM documentation used the 90S8515 to describe the different hardware registers.