# LCD4.LIB

The built in LCD driver for the PIN mode is written to support a worst case scenario where you use random pins of the microprocessor to drive the LCD pins.

This makes it easy to design your PCB but it needs more code.

When you want to have less code you need fixed pins for the LCD display.

With the statement $LIB "LCD4.LBX" you specify that the LCD4.LIB will be used.

The following connections are used in the asm code:

Rs = PortB.0

RW = PortB.1 we dont use the R/W option of the LCD in this version so connect to ground

E = PortB.2

E2 = PortB.3 optional for lcd with 2 chips

Db4 = PortB.4 the data bits must be in a nibble to save code

Db5 = PortB.5

Db6 = PortB.6

Db7 = PortB.7

You can change the lines from the lcd4.lib file to use another port.

Just change the address used :

.EQU LCDDDR=$17 ; change to another address for DDRD ($11)

.EQU LCDPORT=$18 ; change to another address for PORTD ($12)

See the demo lcdcustom4bit.bas in the SAMPLES dir.

Note that you still must select the display that you use with the [CONFIG LCD](config_lcd.md) statement.

See also the [lcd42.lib](lcd4e2.md) for driving displays with 2 E lines.

Note that LBX is a compiled LIB file. In order to change the routines you need the commercial edition with the source code(lib files). After a change you should compile the library with the library manager.