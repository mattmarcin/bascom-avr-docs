# $CRYSTAL

Action

Instruct the compiler to override the crystal frequency options setting.

Syntax

$CRYSTAL = var

Remarks

var | A numeric constant with the Frequency of the crystal.  
---|---  
  
The frequency is selectable from the [Compiler Settings](options_compiler_communication.md). It is stored in a configuration file. The $CRYSTAL directive overrides this setting.

It is best to use the $CRYSTAL directive as the used crystal frequency is visible in your program that way.

![notice](notice.jpg) The $CRYSTAL directive only informs the compiler about the used frequency. It does not set any fuse bit. The frequency must be know by the compiler for a number of reasons. First when you use serial communications, and you specify [$BAUD](baud_1.md), the compiler can calculate the proper settings for the UBR register. And second there are a number of routines like [WAITMS](waitms.md), that use the execution time of a loop to generate a delay. When you specify $CRYSTAL = 1000000 (1 MHz) but in reality, connect a 4 MHz XTAL, you will see that everything will work 4 times as quick.

![notice](notice.jpg)Most new AVR chips have an internal oscillator that is enabled by default. Check the data sheet for the default value.

Most new AVR chips have an option to divide the oscillator frequency by a number of values. If these options are used you need to take this into account.

For example, you connect a 16 MHz crystal and select the external oscillator fuse byte, this would result in a 16 MHz clock for most old processors.

Most new processors have an internal divider which can be enabled. This is an 8-divider in most cases. So in such a case, the resulting frequency would be 2 MHz. $crystal should have a value of 2 MHz in that case.

Instead of changing the divider fusebyte you can also use the CONFIG CLOCKDIV statement to select the division factor.

In case you have a crystal with 16 MHz and you code has code like : CONFIG CLOCKDIV=4 , you would use $CRYSTAL=4000000

Thus $crystal is the clock value used to clock the processor.

Here follows some more info :

What might not be clear : $crystal value does not reflect the value of the xtal you put in your circuit. But it reflects the value of the system clock. 

Early older processors just had a provision for using an external oscillator. For example you could connect a 24 MHz xtal. There was no divider or option to divide this frequency. So the oscillator frequency was directly connected to the processor. This meant : xtal=processor clock

For this reason there was the $crystal directive. There were simply no internal oscillators. 

But later series got options with an internal oscillator. And also options to set a fuse to divide the clock by 8 or some times 16. 

Later series also had a divisor/pre scaler between the xtal oscillator and the system clock input.

So you start with an oscillator frequency of 16 Mhz. The divider is by default 1 so it will result in a 16 Mhz clock. For this reason you use $crystal=16000000

Now when you want to run on 8 Mhz, you still have 16 Mhz osc. so you divide by 2. This means your system clock will be 8 Mhz. And for this reason you set $crystal to a value of 8000000

In short, $crystal value must reflect the system clock.

The reason is that many options need to know the system clock. For example for waitms, waitus, etc. But also when setting a baud rate.

When designed when all AVR chips were known the $crystal directive probably was named $systemclock or something like that.

See also

[$BAUD](baud_1.md) , [BAUD](baud_2.md) , [CONFIG CLOCKDIV](config_clockdiv.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Print "Hello world"

End

```