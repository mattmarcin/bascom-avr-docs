# $SERIALINPUT2LCD

Action

This compiler directive will redirect all serial input to the LCD display instead of echo-ing to the serial port.

Syntax

$SERIALINPUT2LCD

Remarks

You can also write your own custom input or output driver with the [$SERIALINPUT](serialinput.md) and [$SERIALOUTPUT](serialoutput.md) statements, but the $SERIALINPUT2LCD is handy when you use a LCD display. By adding only this directive, you can view all output form routines such as PRINT, PRINTBIN, on the LCD display.

See also

[$SERIALINPUT](serialinput.md) , [$SERIALOUTPUT](serialoutput.md) , [$SERIALINPUT1](_serialinput1.md) , [$SERIALOUTPUT1](_serialoutput1.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Lcdpin = Pin , Db4 = Portb.4 , Db5 = Portb.5 , Db6 = Portb.6 , Db7 = Portb.7 , E = Portc.7 , Rs = Portc.6

$serialinput2lcd

Dim V As Byte

Do

```
Cls

```vb
Input "Number " , V 'this will go to the LCD display

Loop

```