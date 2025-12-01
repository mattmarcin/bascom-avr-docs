# Attaching an LCD Display

A LCD display can be connected with two methods.

•| By wiring the LCD-pins to the processor port pins. This is the pin mode. The advantage is that you can choose the pins and that they don't have to be on the same port. This can make your PCB design simple. The disadvantage is that more code is needed.  
---|---  
  
•| By attaching the LCD-data pins to the data bus. This is convenient when you have an external RAM chip and will add only a little extra code.  
---|---  
  
The LCD-display can be connected in PIN mode as follows:

LCD DISPLAY | PORT | PIN  
---|---|---  
DB7 | PORTB.7 | 14  
DB6 | PORTB.6 | 13  
DB5 | PORTB.5 | 12  
DB4 | PORTB.4 | 11  
E | PORTB.3 | 6  
RS | PORTB.2 | 4  
RW | Ground | 5  
Vss | Ground | 1  
Vdd | +5 Volt | 2  
Vo | 0-5 Volt | 3  
  
This leaves PORTB.1 and PORTB.0 and PORTD for other purposes.

You can change these pin settings from the [Options LCD](options_compiler_lcd.md) menu.

BASCOM supports many statements to control the LCD-display.

```vb
For those who want to have more control of the example below shows how to use the internal BASCOM routines.

$ASM

```
Ldi _temp1, 5 'load register R24 with value

Rcall _Lcd_control 'it is a control value to control the display

Ldi _temp1,65 'load register with new value (letter A)

Rcall _Write_lcd 'write it to the LCD-display

$END ASM

Note that _lcd_control and _write_lcd are assembler subroutines which can be called from BASCOM.

See the manufacturer's details from your LCD display for the correct pin assignment.