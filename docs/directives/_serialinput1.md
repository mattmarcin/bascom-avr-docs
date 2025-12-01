# $SERIALINPUT1

Action

Specifies that serial input of the second UART must be redirected.

Syntax

$SERIALINPUT1 = label

Remarks

Label | The name of the assembler routine that must be called when a character is needed from the INPUT routine. The character must be returned in R24.  
---|---  
  
With the redirection of the INPUT command, you can use your own input routines.

This way you can use other devices as input devices.

Note that the INPUT statement is terminated when a RETURN code (13) is received.

By default when you use INPUT or INKEY(), the compiler will expect data from the COM2 port. When you want to use a keyboard or remote control as the input device you can write a custom routine that puts the data into register R24 once it asks for this data.

See also

[$SERIALOUTPUT1](_serialoutput1.md) , [$SERIALINPUT](serialinput.md) , [$SERIALOUTPUT](serialoutput.md)

Example

See the [$SERIALINPUT](serialinput.md) sample