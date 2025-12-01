# $SERIALOUTPUT1

Action

Specifies that serial output of the second UART must be redirected.

Syntax

$SERIALOUTPUT1 = label

Remarks

Label | The name of the assembler routine that must be called when a character is send to the serial buffer (UDR1). The character is placed into R24.  
---|---  
  
With the redirection of the PRINT and other serial output related commands, you can use your own routines.

This way you can use other devices as output devices.

See also

[$SERIALINPUT1](_serialinput1.md) , [$SERIALINPUT](serialinput.md) , [$SERIALINPUT2LCD](serialinput2lcd.md) , [$SERIALOUTPUT](serialoutput.md)

Example

See the [$SERIALOUTPUT](serialoutput.md) example