# $SERIALOUTPUT

Action

Specifies that serial output must be redirected.

Syntax

$SERIALOUTPUT = label

Remarks

Label | The name of the assembler routine that must be called when a character is send to the serial buffer (UDR). The character is placed into R24.  
---|---  
  
With the redirection of the PRINT and other serial output related commands, you can use your own routines.

This way you can use other devices as output devices.

See also

[$SERIALINPUT](serialinput.md) , [$SERIALINPUT2LCD](serialinput2lcd.md) , [$SERIALINPUT1](_serialinput1.md) , [$SERIALOUTPUT1](_serialoutput1.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

$serialoutput = Myoutput

'your program goes here

Do

Print "Hello"

Loop

End

```
myoutput:

```vb
'perform the needed actions here

'the data arrives in R24

'just set the output to PORTB

```
!outportb,r24

!ret