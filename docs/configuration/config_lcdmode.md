# CONFIG LCDMODE

Action

Configures the LCD operation mode and overrides the compiler setting.

Syntax

CONFIG LCDMODE = type

Remarks

Type | PORT Will drive the LCD in 4-bit port mode and is the default. In PORT mode you can choose different PIN's from different PORT's to connect to the upper 4 data lines of the LCD display. The RS and E can also be connected to a user selectable pin. This is very flexible since you can use pins that are not used by your design and makes the board layout simple. On the other hand, more software is necessary to drive the pins. BUS will drive the LCD in bus mode and in this mode is meant when you have external RAM and so have an address and data bus on your system. The RS and E line of the LCD display can be connected to an address decoder. Simply writing to an external memory location select the LCD and the data is sent to the LCD display. This means the data-lines of the LCD display are fixed to the data-bus lines. Use [$LCD](lcd_1.md) = address and [$LCDRS](lcdrs.md) = address, to specify the addresses that will enable the E and RS lines.  
---|---  
  
See also

[CONFIG LCD](config_lcd.md) , [$LCD](lcd_1.md) , [$LCDRS](lcdrs.md)

Example

```vb
Config LCDMODE = PORT 'the report will show the settings

Config LCDBUS = 4 '4 bit mode

```
LCD "hello"