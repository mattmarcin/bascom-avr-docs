# PS2MOUSEXY

Action

Sends mouse movement and button information to the PC.

Syntax

PS2MOUSEXY X , Y, button

Remarks

X | The X-movement relative to the current position. The range is â255 to 255.  
---|---  
Y | The Y-movement relative to the current position. The range is â255 to 255.  
Button | A variable or constant that represents the button state. 0 â no buttons pressed 1- left button pressed 2- right button pressed 4- middle button pressed You can combine these values by adding them. For example, 6 would emulate that the right and middle buttons are pressed. To send a mouse click, you need to send two ps2mouseXY statements. The first must indicate that the button is pressed, and the second must release the button. Ps2mouseXY 0,0,1 ' left mouse pressed PsmouseXY 0,0,0 ' left mouse released  
  
The SENDSCAN statement could also be used.

See also

[SENDSCAN](sendscan.md), [CONFIG PS2EMU](config_ps2emu.md)