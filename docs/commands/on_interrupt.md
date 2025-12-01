# ON INTERRUPT

Action

Execute subroutine when the specified interrupt occurs.

Syntax

ON interrupt label [NOSAVE|SAVE|SAVEALL]

Remarks

Interrupt | INT0, INT1, INT2, INT3, INT4,INT5, TIMER0 ,TIMER1, TIMER2, ADC , EEPROM , CAPTURE1, COMPARE1A, COMPARE1B,COMPARE1. Or you can use the AVR name convention: OC2 , OVF2, ICP1, OC1A, OC1B, OVF1, OVF0, SPI, URXC, UDRE, UTXC, ADCC, ERDY and ACI. The available interrupts depend on the processor.   
---|---  
Label | The label to jump to if the interrupt occurs.  When using a label, you need to use a RETURN to resume the main program. The label may also be a sub routine. When using a sub routine, the sub routine needs to end with END SUB like any normal sub routine. This sub routine may not have parameters.  So either a label must be uses like : ISR_INT0: Or you define a sub routine : Declare Sub MyISR_Int0() ON INT0 MyISR_Int0 SAVEALL  
NOSAVE | When you specify NOSAVE, no registers are saved and restored in the interrupt routine. So when you use this option make sure to save and restore all used registers. When you omit NOSAVE all used registers will be saved. These are SREG , R31 to R16 and R11 to R0 with exception of R6,R8 and R9 . R12 â R15 are not saved. When you use floating point math in the ISR(not recommended) you must save and restore R12-R15 yourself in the ISR. My_Isr: Push R12 ' save registers Push R13 Push R14 Push R15 Single = single + 1 ' we use FP Pop R15 ' restore registers Pop R14 Pop R13 Pop R12 RETURN ![notice](notice.jpg)When the AVR has extended IO-space (for example ATMega48, 88 or 168, see datasheet at the end: Registersummary), the compiler uses R23 for a number of operations. So Push and Pop R23 as well when using the NOSAVE-option when using these AVR's with extended IO-space.  
SAVE | This is the default and is the same as when no parameter is provided. The most common used registers, SREG, and RAMPZ are saved and restored. Saved : SREG , R31 to R16 and R11 to R0 with exception of R6,R8 and R9. If RAMPZ exists, it will be saved as well.  
SAVEALL | This will save all registers that SAVE will save, but it will also save R12-R15. You should use this option when using floating point math in the ISR.  
  
When using a label you must return from the interrupt routine with the [RETURN](return.md) statement.

The first RETURN statement that is encountered that is outside a condition will generate a RETI instruction. You may have only one such RETURN statement in your interrupt routine because the compiler restores the registers and generates a RETI instruction when it encounters a RETURN statement in the ISR. All other RETURN statements are converted to a RET instruction.

While the label is supported because the old GW-BASIC supported it, it is best to use a Sub routine which you can end with End Sub.

The possible interrupt names can be looked up in the selected microprocessor register file. 2313def.dat for example shows that for the compare interrupt the name is COMPARE1. (look at the bottom of the file)

Using the editor, type ON (SPACE) and press CTRL+SPACE key to get a pop up list with possible interrupt sources.

What are interrupts good for?

An interrupt will halt your program and will jump to a specific part of your program. You can make a DO .. LOOP and poll the status of a pin for example to execute some code when the input on a pin changes.

But with an interrupt you can perform other tasks and when then pin input changes a special part of your program will be executed. When you use INPUT "Name ", v for example to get a user name via the RS-232 interface it will wait until a RETURN is received(a byte with value 13, not the RETURN statement !).

When you have an interrupt routine and the interrupt occurs it will branch to the interrupt code and will execute the interrupt code. When it is finished it will return to the Input statement, waiting until a RETURN is entered(a byte with the return value 13).

Maybe a better example is writing a clock program. You could update a variable in your program that updates a second counter. But a better way is to use a TIMER interrupt and update a seconds variable in the TIMER interrupt handler.

There are multiple interrupt sources and it depends on the used chip/processor which are available.

To allow the use of interrupts you must set the global interrupt switch with an ENABLE INTERRUPTS statement. This only allows that interrupts can be used. You must also set the individual interrupt switches on!

ENABLE TIMER0 for example allows the TIMER0 interrupt to occur.

With the DISABLE statement you turn off the switches.

When the processor must handle an interrupt it will branch to an address at the start of flash memory. These addresses can be found in the DAT files.

The compiler normally generates a RETI instruction at these addresses so that in the event that an interrupt occurs, it will return immediately.

When you use the ON ... LABEL statement, the compiler will generate code that jumps to the specified label. The SREG and other registers are saved at the LABEL location and when the RETURN is found the compiler restores the registers and generates the RETI so that the program will continue where it was at the time the interrupt occurred.

When an interrupt is serviced no other interrupts can occur because the processor(not the compiler) will disable all interrupts by clearing the master interrupt enable bit. When the interrupt is serviced the interrupt is also cleared so that it can occur again when the conditions are met that sets the interrupt.

It is not possible to give interrupts a priority. The interrupt with the lowest address has the highest interrupt!

Finally some tips :

* when you use a timer interrupt that occurs each 10 uS for example, be sure that the interrupt code can execute in 10 uS. Otherwise you would loose time.

* it is best to set just a simple flag in the interrupt routine and to determine it's status in the main program. This allows you to use the NOSAVE option that saves stack space and program space. You only have to Save and Restore R24 and SREG in that case.

* Since you can not PUSH a hardware register, you need to load it first:

PUSH R24 ; since we are going to use R24 we better save it

IN r24, SREG ; get content of SREG into R24

PUSH R24 ; we can save a register

;here goes your asm code

POP R24 ;get content of SREG

OUT SREG, R24 ; save into SREG

POP R24 ; get r24 back

* When you call user functions or sub routines which passes variables from your interrupt, you need to enable frame protection. Use [$frameprotect](frameprotect.md)=1 to activate this protection.

![notice](notice.jpg)Unlike the ON VALUE statement, the ON INTERRUPT does not accept GOTO or GOSUB. The GOSUB/GOSUB tells the compiler that ON VALUE is used rather than ON INTERRUPT. Since interrupt sources are constants with an address, the compiler is happy to accept ON INT0 GOSUB which will do something entirely different than you expect.

See Also

[On VALUE](on_value.md) , [ENABLE](enable.md), [DISABLE](disable.md)

Partial Example using label

```vb
Enable Interrupts

Enable Int0 'enable the interrupt

On Int0 Label2 Nosave 'jump to label2 on INT0

Do'endless loop

```
nop

```vb
Loop

End

```
Label2:

```vb
Dim A As Byte

If A > 1 Then

Return 'generates a RET because it is inside a condition

End If

Return 'generates a RETI because it is the first RETURN

Return 'generates a RET because it is the second RETURN

```
Partial Example using Sub

```vb
Declare Sub Label2()

Dim A As Byte

Enable Interrupts

Enable Int0 'enable the interrupt

On Int0 Label2 Nosave 'jump to label2 on INT0

Do'endless loop

```
nop

```vb
Loop

End

Sub Label2()

If A > 1 Then

exit sub

Else

gosub test 

End If

exit sub

```
Test:

```vb
print "test"

Return

End Sub 'generates a RETI

```
As you can see, using a Sub is more flexible because you can include local routines using a label/return.