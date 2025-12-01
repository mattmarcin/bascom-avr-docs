# CRYSTAL

Action

Special byte variable that can be used with software UART routine to change the baud rate during runtime.

Syntax

CRYSTAL = var (old option do not use !!)

___CRYSTAL1 = var

BAUD #1, 2400

Remarks

With the software UART you can generate good baud rates. But chips such as the ATtiny22 have an internal 1 MHz clock. The clock frequency can change during runtime by influence of temperature or voltage.

The crystal variable can be changed during runtime to change the baud rate.

The above has been changed in version 1.11

Now you still can change the baud rate with the crystal variable.

But you don't need to dimension it. And the name has been changed:

___CRYSTALx where x is the channel number.

When you opened the channel with #1, the variable will be named ___CRYSTAL1

But a better way is provided now to change the baud rate of the software uart at run time. You can use the BAUD option now:

Baud #1 , 2400 'change baud rate to 2400 for channel 1

When you use the baud # option, you must specify the baud rate before you print or use input on the channel. This will dimension the ___CRYSTALx variable and load it with the right value.

When you don't use the BAUD # option the value will be loaded from code and it will not use 2 bytes of your SRAM.

The ___CRYSTALx variable is hidden in the report file because it is a system variable. But you may assign a value to it after BAUD #x, zzzz has dimensioned it.

The old CRYSTAL variable does not exist anymore.

Some values for 1 MHz internal clock :

66 for 2400 baud

31 for 4800 baud

14 for 9600 baud

See also

[OPEN](open.md) , [CLOSE](open.md)

Example

Dim B as byte

Open "comd.1:9600,8,n,1,inverted" For Output As #1

```vb
Print #1 , B

Print #1 ,"serial output"

```
baud #1, 4800 'use 4800 baud now

Print #1,"serial output"

___CRYSTAL1 = 255

Close#1

End