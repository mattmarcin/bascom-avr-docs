# LOCATE

Action

Moves the LCD cursor to the specified position.

Syntax

LOCATE y , x

Remarks

X | Constant or variable with the position. (1-64*)  
---|---  
Y | Constant or variable with the line (1 - 4*)  
  
* Depending on the used display

See also

[CONFIG LCD](config_lcd.md) , [LCD](lcd_2.md) , [HOME](home.md) , [CLS](cls.md)

Partial Example

LCD "Hello"

Locate 1,10

LCD "*"