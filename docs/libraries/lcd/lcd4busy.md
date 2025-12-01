# LCD4BUSY

BASCOM supports LCD displays in a way that you can choose all pins random. This is great for making a simple PCB but has the disadvantage of more code usage. BASCOM also does not use the WR-pin so that you can use this pin for other purposes.

The LCD4BUSY.LIB can be used when timing is critical.

The default LCD library uses delays to wait until the LCD is ready. The lcd4busy.lib is using an additional pin (WR) to read the status flag of the LCD.

The db4-db7 pins of the LCD must be connected to the higher nibble of the port.

The other pins can be defined.

```vb
'-----------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' lcd4busy.bas shows how to use LCD with busy check

'-----------------------------------------------------------------------

'code tested on a 8515

$regfile="8515def.dat"

'stk200 has 4 MHz

$crystal= 4000000

'define the custom library

'uses 184 hex bytes total

$lib"lcd4busy.lib"

'define the used constants

'I used portA for testing

```
Const _lcdport =Porta

Const _lcdddr =Ddra

Const _lcdin =Pina

Const _lcd_e = 1

Const _lcd_rw = 2

Const _lcd_rs = 3

'this is like always, define the kind of LCD

ConfigLcd= 16 * 2

'and here some simple lcd code

Cls

Lcd"test"

Lowerline

Lcd"this"

End