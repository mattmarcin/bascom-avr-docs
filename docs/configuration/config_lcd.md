# CONFIG LCD

Action

Configure the LCD display and override the compiler setting.

Syntax

CONFIG LCD = LCDtype , CHIPSET=KS077 | Dogm163v5 | DOG163V3 | DOG162V5 | DOG162V3 | ST7032 [,CONTRAST=value] [,BEFORE=0|1] [,AFTER=0|1]

BEFORE and AFTER. with a parameter value of 1 a sub will be called _lcdBefore and _lcdAfter

Remarks

LCDtype | The type of LCD display used. This can be : 40x4,16x1, 16x2, 16x4, 16x4, 20x2, 20x4, 16x1a or 20x4A. Default 16x2 is assumed.  
---|---  
Chipset KS077 | Most text based LCD displays use the same chip from Hitachi. But some use the KS077 which is highly compatible but needs an additional function register to be set. This parameter will cause that this register is set when you initialize the display.  
CHIPSET DOGM | The DOGM chip set uses a special function register that need to be set. The 16 x 2 LCD displays need DOG162V3 for 3V operation or DOG162V5 for 5V operation. The 16 x 3 LCD displays need DOG163V3 for 3V operation or Dogm163v5 for 5V operation  
CHIPSET ST7032 | This chip is used on I2C lcd's. It requires library Lcd_RX1602A5. See example 3 below.  
CONTRAST | The optional contrast parameter is only supported by the EADOG displays. By default a value from the manufacture is used. But you might want to override this value with a custom setting. The default values are : \- DOGM162V5 : &H74 \- DOGM162V3 : &H78 \- DOGM163V5 : &H7C \- DOGM163V3 : &H70  
BEFORE | This is an optional parameter. A value of 1 will result in a call to a routine named _LCDBEFORE, each time LCD value|"text" is used.  This allows you as a user to turn off interrupts or perform other tasks.  
AFTER | This is an optional parameter. A value of 1 will result in a call to a routine named _LCDAFTER, each time LCD value|"text" is ended.  This allows you as a user to turn on interrupts or perform other tasks.  
  
When you have a 16x2 display, you don't have to use this statement.

The 16x1a is special. It is used for 2x8 displays that have the address of line 2, starting at location &H8.

The 20xA is also special. It uses the addresses &H00, &H20, &H40 and &H60 for the 4 lines. It will also set a special function register.

The CONFIG LCD can only be used once. You can not dynamic(at run time) change the pins.

When you want to initialize the LCD during run time, you can use the [INITLCD](initlcd.md) statement.

The BEFORE and AFTER parameters can be used to call some user code just before data is shown on the LCD, and when finished.

For example, you could toggle a LED on/off. Or set some background light. Or disable interrupts before showing data, and enable interrupts afterwards.

You must use DECLARE SUB to declare the called labels. Or you may use normal labels and exit with RETURN.

In version 2084 a constant is created named _TEXTLCDKIND which contains a value based on the selected LCD.

The values are :

LCD | Value  
---|---  
16x1 | 161  
16x2 | 162  
16x3 | 163  
16x4 | 164  
20x2 | 202  
24x2 | 242  
40x4 | 404  
20x4A | 1204  
40x2 | 402  
20x4 | 204  
16x1A | 1610  
20x4VFD | 2204  
  
See Also

[CONFIG LCDPIN](config_lcdpin.md) , [CONFIG LCDBUS](config_lcdbus.md) , [INITLCD](initlcd.md)

Example1

```vb
'-----------------------------------------------------------------------------------------

'name : lcd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'micro : Mega8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m8515.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$sim

'REMOVE the above command for the real program !!

'$sim is used for faster simulation

'note : tested in PIN mode with 4-bit

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

Config Lcdpin = Pin , Db4 = Porta.4 , Db5 = Porta.5 , Db6 = Porta.6 , Db7 = Porta.7 , E = Portc.7 , Rs = Portc.6

'These settings are for the STK200 in PIN mode

'Connect only DB4 to DB7 of the LCD to the LCD connector of the STK D4-D7

'Connect the E-line of the LCD to A15 (PORTC.7) and NOT to the E line of the LCD connector

'Connect the RS, V0, GND and =5V of the LCD to the STK LCD connector

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
Dim A As Byte

Config Lcd = 16x2 'configure lcd screen

'other options are 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

'When you dont include this option 16 * 2 is assumed

'16 * 1a is intended for 16 character displays with split addresses over 2 lines

'$LCD = address will turn LCD into 8-bit databus mode

' use this with uP with external RAM and/or ROM

' because it aint need the port pins !

```
Cls 'clear the LCD display

Lcd "Hello world." 'display this at the top line

Wait 1

Lowerline 'select the lower line

Wait 1

Lcd "Shift this." 'display this at the lower line

```vb
Wait 1

For A = 1 To 10

```
Shiftlcd Right 'shift the text to the right

```vb
Wait 1 'wait a moment

Next

For A = 1 To 10

```
Shiftlcd Left 'shift the text to the left

```vb
Wait 1 'wait a moment

Next

```
Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Wait 1 'wait a moment

Shiftcursor Right 'shift the cursor

Lcd "@" 'display this

Wait 1 'wait a moment

Home Upper 'select line 1 and return home

Lcd "Replaced." 'replace the text

Wait 1 'wait a moment

Cursor Off Noblink 'hide cursor

Wait 1 'wait a moment

Cursor On Blink 'show cursor

Wait 1 'wait a moment

Display Off 'turn display off

Wait 1 'wait a moment

Display On 'turn display on

'-----------------NEW support for 4-line LCD------

Thirdline

Lcd "Line 3"

Fourthline

Lcd "Line 4"

Home Third 'goto home on line three

Home Fourth

Home F 'first letteer also works

Locate 4 , 1 : Lcd "Line 4"

```vb
Wait 1

'Now lets build a special character

'the first number is the characternumber (0-7)

'The other numbers are the rowvalues

'Use the LCD tool to insert this line

```
Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character

'----------------- Now use an internal routine ------------

_temp1 = 1 'value into ACC

!rCall _write_lcd 'put it on LCD

End

Example2

```vb
'--------------------------------------------------------------

' EADOG-M163.bas

' Demonstration for EADOG 163 display

' (c) 1995-2025, MCS Electronics

'--------------------------------------------------------------

'

$regfile = "M8515.dat"

$crystal = 4000000

'I used the following settings

'Config Lcdpin = Pin , Db4 = Portb.2 , Db5 = Portb.3 , Db6 = Portb.4 , Db7 = Portb.5 , E = Portb.1 , Rs = Portb.0

'CONNECT vin TO 5 VOLT

Config Lcd = 16x3 , Chipset = Dogm163v5 '16*3 type LCD display

'other options for chipset are DOG163V3 for 3Volt operation

'Config Lcd = 16 * 3 , Chipset = Dogm163v3 , Contrast = &H72 '16*3 type LCD display

'The CONTRAST can be specified when the default value is not what you need

'The EADOG-M162 is also supported :

'Chipset params for the DOGM162 : DOG162V5, DOG162V3

```
Cls 'Dit maakt het scherm leeg

Locate 1 , 1 : Lcd "Hello World"

Locate 2 , 1 : Lcd "line 2"

Locate 3 , 1 : Lcd "line 3"

End

Example3

```vb
'------------------------------------------------------------------------------  
'name : LCD-RX1602A5.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates I2C LCD library  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'The used library was sponsored by Lab microelectronic GmbH  
'------------------------------------------------------------------------------  
  
$regfile = "m88def.dat"  
$crystal = 8000000  
$hwstack = 32  
$swstack = 32  
$framesize = 64  
  
```
const vmode = 3 ' 3V mode  
  
```vb
$lib "Lcd_RX1602A5.lbx"  
$lib "i2c_twi.lbx" ' use hardware twi or remark for software I2C  
  
Config Twi = 100000 ' 100kHz  
config lcd = 16x2 , chipset = st7032  
  
config SCL=PORTC.5  
config SDA=PORTC.4  
  
  
```
I2cinit  
  
lcd_reset alias portc.2 ' pin used for LCD RESET  
lcd_light alias portd.7 ' pin used for back light  
  
```vb
Config lcd_reset = Output ' Display Reset  
Config lcd_light = Output ' Display Licht  
  
  
```
lcd_light = 1 ' activate background LED  
Lcd_reset = 0 ' RESET mode  
waitms 100  
Lcd_reset = 1 ' normal mode  
  
initlcd ' init LCD  
lcdcontrast 30 'a value between 30 and 40 works best at 3V  
  
Do  
Cls  
Locate 1 , 1 : Lcd "test"  
```vb
Waitms 100 '  
Loop  
  
  
End

```
Example 4

```vb
declare sub _lcdbefore()  
declare sub _lcdafter()  
config PORTB.0=OUTPUT  
config LCD=16x2, before=1,after=1  
```
CLS  
LCD "test"  
```vb
End  
  
sub _lcdbefore()  
set portb.0  
end sub  
  
sub _lcdafter()  
reset portb.0  
end sub  
  
  


```