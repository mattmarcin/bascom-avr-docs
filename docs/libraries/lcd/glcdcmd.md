# GLCDCMD

Action

Sends a command byte to the SED graphical LCD display.

Syntax

GLCDCMD byte [,chip]

Remarks

byte | A variable or numeric constant to send to the display.  
---|---  
chip | An optional numeric variable or constant in the range from 1-2 which indicates which graphic chip CE line need to be selected. The routine _selchip1 or _selchip2 is called.   
  
With GLCDCMD you can write command bytes to the display. This is convenient to control the display when there is no specific statement available.

You need to include the glibSED library with :

$LIB "glibsed.lbx"

See also

[CONFIG GRAPHLCD](config_lcd.md) , [LCDAT](lcdat.md), [GLCDDATA](glcddata.md)

Example

NONE