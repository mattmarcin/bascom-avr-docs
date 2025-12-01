# LCDDATA

Action

Send a byte in data mode to a Text LCD display.

Syntax

LCDDATA byte

Remarks

To send data to an LCD display you need to use the LCD statement. If you have the need to call the internal LCD routine which sends a byte in data mode, you can use the LCDDATA statement. The byte can be a variable or numeric constant.

See also

[LCD](lcd_2.md) , [LCDCMD](lcdcmd.md)

Example

  
Lcdcmd 10 ' will call _lcd_control  
Lcddata 65 ' will call _write_lcd and send ASCII 65 (A)