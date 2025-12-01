# LCDCMD

Action

Send a byte in command mode to a Text LCD display.

Syntax

LCDCMD byte

Remarks

To send data to an LCD display you need to use the LCD statement. If you have the need to call the internal LCD routine which sends a byte in command mode, you can use the LCDCMD statement. The byte can be a variable or numeric constant.

See also

[LCD](lcd_2.md) , [LCDDATA](lcddata.md)

Example

  
Lcdcmd 10 ' will call _lcd_control  
Lcddata 65 ' will call _write_lcd and send ASCII 65 (A)