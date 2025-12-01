# $BAUD

Action

Instruct the compiler to override the baud rate setting from the options menu.

Syntax

$BAUD = var

Remarks

Var | The baud rate that you want to use. This must be a numeric constant.  
---|---  
  
The baud rate is selectable from the [Compiler Settings](options_compiler_communication.md). It is stored in a configuration file. The $BAUD directive overrides the setting from the Compiler Settings.

In the generated report, you can view which baud rate is actually generated. The generated baud rate does depend on the used micro and crystal.

When you simulate a program you will not notice any problems when the baud rate is not set to the value you expected. In real hardware a wrong baud rate can give weird results on the terminal emulator screen. For best results use a crystal that is a multiple of the baud rate.

In the simulator you need to select the UART0-TAB to view the output of the UART0, or to send data to this UART.

See also

[$CRYSTAL](crystal_1.md) , [BAUD](baud_2.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

$hwstack = 32

$swstack = 8

$framesize = 24

Config Com1 = Dummy, Synchrone = 0, Parity = None, Stopbits = 1, Databits = 8, Clockpol = 0

Print "Hello"

'Now change the baud rate in a program

```
Baud = 9600

```vb
Print "Did you change the terminal emulator baud rate too?"

End

```