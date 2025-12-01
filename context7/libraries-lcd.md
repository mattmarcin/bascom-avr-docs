# LCD Libraries

> Text and graphical LCD display libraries

## $LCD

Action

Instruct the compiler to generate code for 8-bit LCD displays attached to the data bus.

Syntax

$LCD = [&H]address

Remarks

Address | The address where must be written to, to enable the LCD display and the RS line of the LCD display. The db0-db7 lines of the LCD must be connected to the data lines D0-D7. (or is 4 bit mode, connect only D4-D7) The RS line of the LCD can be configured with the LCDRS statement. On systems with external RAM, it makes more sense to attach the LCD to the data bus. With an address decoder, you can select the LCD display.  
---|---  
  
Do not confuse $LCD with the LCD statement.

The compiler will create a constant named ___LCD_ADR which you could use in an alternative LCD library.

See also

[$LCDRS](lcdrs.md) , [CONFIG LCD](config_lcdbus.md) , [LCD](lcd_2.md)

Example

```vb
'--------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

'--------------------------------------------------------------

' file: LCD.BAS

' demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'--------------------------------------------------------------

'note : tested in bus mode with 4-bit on the STK200

'LCD - STK200

'-------------------

'D4 D4

'D5 D5

'D6 D6

'D7 D7

'WR WR

'E E

'RS RS

'+5V +5V

'GND GND

'V0 V0

'D0-D3 are not connected since 4 bit bus mode is used!

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
$regfile = "8515def.dat"

$lcd = &HC000

$lcdrs = &H8000

Config Lcdbus = 4

Dim A As Byte

Config Lcd = 16x2 'configure lcd screen

'other options are 16 * 2 , 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

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

---

## $LCDPUTCTRL

Action

Specifies that LCD control output must be redirected.

Syntax

$LCDPUTCTRL = label

Remarks

Label | The name of the assembler routine that must be called when a control byte is printed with the LCD statement. The character must be placed in register R24.  
---|---  
  
With the redirection of the LCD statement, you can use your own routines.

See also

[$LCDPUTDATA](lcdputdata.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'dimension used variables

Dim S As String* 10

Dim W As Long

'inform the compiler which routine must be called to get serial 'characters

$lcdputdata= Myoutput

$lcdputctrl= Myoutputctrl

'make a never ending loop

Do

```
Lcd "test"

```vb
Loop

End

'custom character handling routine

'instead of saving and restoring only the used registers

'and write full ASM code, we use Pushall and PopAll to save and 'restore

'all registers so we can use all BASIC statements

'$LCDPUTDATA requires that the character is passed in R24

```
Myoutput:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return

MyoutputCtrl:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return

---

## $LCDPUTDATA

Action

Specifies that LCD data output must be redirected.

Syntax

$LCDPUTDATA = label

Remarks

Label | The name of the assembler routine that must be called when a character is printed with the LCD statement. The character must be placed in R24.  
---|---  
  
With the redirection of the LCD statement, you can use your own routines.

See also

[$LCDPUTCTRL](lcdputctrl.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'dimension used variables

Dim S As String* 10

Dim W As Long

'inform the compiler which routine must be called to get serial 'characters

$lcdputdata= Myoutput

$lcdputctrl= Myoutputctrl

'make a never ending loop

Do

```
Lcd "test"

```vb
Loop

End

'custom character handling routine

'instead of saving and restoring only the used registers

'and write full ASM code, we use Pushall and PopAll to save and 'restore

'all registers so we can use all BASIC statements

'$LCDPUTDATA requires that the character is passed in R24

```
Myoutput:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return

MyoutputCtrl:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return

---

## $LCDRS

Action

Instruct the compiler to generate code for 8-bit LCD displays attached to the data bus.

Syntax

$LCDRS = [&H]address

Remarks

Address | The address where must be written to, to enable the LCD display. The db0-db7 lines of the LCD must be connected to the data lines D0-D7. (or is 4 bit mode, connect only D4-D7) On systems with external RAM, it makes more sense to attach the LCD to the data bus. With an address decoder, you can select the LCD display.  
---|---  
  
The compiler will create a constant named ___LCDRS_ADR which you could use in an alternative LCD library.

See also

[$LCD](lcd_1.md) , [CONFIG LCDBUS](config_lcdbus.md)

Example

```vb
'--------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

'--------------------------------------------------------------

' file: LCD.BAS

' demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'--------------------------------------------------------------

'note : tested in bus mode with 4-bit on the STK200

'LCD - STK200

'-------------------

'D4 D4

'D5 D5

'D6 D6

'D7 D7

'WR WR

'E E

'RS RS

'+5V +5V

'GND GND

'V0 V0

' D0-D3 are not connected since 4 bit bus mode is used!

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
$regfile = "8515def.dat"

$lcd = &HC000

$lcdrs = &H8000

Config Lcdbus = 4

Dim A As Byte

Config Lcd = 16 * 2 'configure lcd screen

'other options are 16 * 2 , 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

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

---

## $SERIALINPUT2LCD

Action

This compiler directive will redirect all serial input to the LCD display instead of echo-ing to the serial port.

Syntax

$SERIALINPUT2LCD

Remarks

You can also write your own custom input or output driver with the [$SERIALINPUT](serialinput.md) and [$SERIALOUTPUT](serialoutput.md) statements, but the $SERIALINPUT2LCD is handy when you use a LCD display. By adding only this directive, you can view all output form routines such as PRINT, PRINTBIN, on the LCD display.

See also

[$SERIALINPUT](serialinput.md) , [$SERIALOUTPUT](serialoutput.md) , [$SERIALINPUT1](_serialinput1.md) , [$SERIALOUTPUT1](_serialoutput1.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Lcdpin = Pin , Db4 = Portb.4 , Db5 = Portb.5 , Db6 = Portb.6 , Db7 = Portb.7 , E = Portc.7 , Rs = Portc.6

$serialinput2lcd

Dim V As Byte

Do

```
Cls

```vb
Input "Number " , V 'this will go to the LCD display

Loop

```

---

## Attaching an LCD Display

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

---

## DEFLCDCHAR

Action

Define a custom LCD character.

Syntax

DEFLCDCHAR char,r1,r2,r3,r4,r5,r6,r7,r8

Remarks

char | Constant representing the character (0-7).  
---|---  
r1-r8 | The row values for the character.  
  
You can use the [LCD designer](tools_lcd_designer.md) to build the characters.

\- It is important that a CLS follows the DEFLCDCHAR statement(s).

So make sure you use the DEFLCDCHAR before your CLS statement.

\- When using INITLCD make sure this is called before DEFLCDCHAR since it will reset the LCD controller.

Special characters can be printed with the [Chr](chr.md)() function.

LCD Text displays have a 64 byte memory that can be used to show your own custom characters. Each character uses 8 bytes as the character is an array from 8x8 pixels. You can create a maximum of 8 characters this way. Or better said : you can show a maximum of 8 custom characters at the same time. You can redefine characters in your program but with the previous mentioned restriction.

A custom character can be used to show characters that are not available in the LCD font table. For example a Ã.

You can also use custom characters to create a bar graph or a music note. 

Note:

You cannot use Chr(0)-Deflcdchar 0 in any with any String Variables/Arrays, Chr(0) will be interpreted as a String terminator 

and not as Custom Character for Deflcdchar 0 (Deflcdchar from 1 to 7 is fine).

See also

[Tools LCD designer](tools_lcd_designer.md) , [LCD](lcd_2.md) , [CLS](cls.md) , [CURSOR](cursor.md) , [DISPLAY](display.md) , [LOCATE](locate.md)

Partial Example

Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character

---

## GLCD

GLCD.LIB (LBX) is a library for Graphic LCDâs based on the T6963C chip.

The library contains code for [LOCATE](locate.md), [CLS](cls.md), [PSET](pset.md), [LINE](line.md), [CIRCLE](circle.md), [SHOWPIC](showpic.md) and [SHOWPICE](showpice.md).

---

## GLCDCMD

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

---

## GLCDDATA

Action

Sends a data byte to the SED graphical LCD display.

Syntax

GLCDDATA byte [,chip]

Remarks

byte | A variable or numeric constant to send to the display.  
---|---  
chip | An optional numeric variable or constant in the range from 1-2 which indicates which graphic chip CE line need to be selected. The routine _selchip1 or _selchip2 is called.   
  
With GLCDDATA you can write data bytes to the display. This is convenient to control the display when there is no specific statement available.

You need to include the glibSED library with :

$LIB "glibsed.lbx"

See also

[CONFIG GRAPHLCD](config_lcd.md) , [LCDAT](lcdat.md), [GLCDCMD](glcdcmd.md)

Example

NONE

---

## glcdR7565R

The glcdR7565R.lib is intended to be used with 128x64 displays using the ST7565R chip.

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1-ST7565R.bas  
' This sample demonstrates the ST7565R chip with an Xmega128A1  
' Display used : 64128N SERIES from DisplayTech  
' this is a parallel display with read/write options  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'include the following lib and code, the routines will be replaced since they are a workaround  
$lib "xmega.lib"  
$external _xmegafix_clear  
$external _xmegafix_rol_r1014  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
$lib "glcdST7565r.lbx" ' specify the used lib  
$lib "glcd.lbx" ' and this one of you use circle/line etc  
  
'the display was connected with these pins  
Config Graphlcd = 128 * 64eadogm ,dataport=portj, Cs1 = Porth.0 , A0 = Porth.2 , rst= Porth.1 , wr = Porth.3 , Rd = Porth.4,c86=porth.6  
  
```
cls  
  
Setfont Font8x8tt ' set font  
  
```vb
dim y as byte  
  
'You can use locate but the columns have a range from 1-128  
'When you want to show somthing on the LCD, use the LDAT command  
'LCDAT Y , COL, value  
```
Lcdat 1 , 1 , "11111111"  
Lcdat 2 , 1 , "ABCDEFGHIJKL1234"  
Lcdat 3 , 1 , "MCS Electronics" , 1 ' inverse  
Lcdat 4 , 1 , "MCS Electronics"  
  
Waitms 3000  
Setfont My12_16 ' use a bigger font  
  
Cls  
Lcdat 1 , 1 , "112345678" 'a bigger font  
Waitms 3000 ' wait  
  
Line(0 , 0) -(127 , 64) , 1 'make line  
Waitms 2000 'wait 2 secs  
Line(0 , 0) -(127 , 64) , 0 'remove line by inverting the color  
  
For Y = 1 To 20  
Circle(30 , 30) , Y , 1 ' growing circle  
```vb
Waitms 100  
Next  
  
End  
  
  
$include "font8x8TT.font"  
$include "my12_16.font"

```

---

## GLCDSED

GLCDSED.LIB (LBX) is a library for Graphic LCDâs based on the SEDXXXX chip.

The library contains modified code for this type of display.

New special statements for this display are :

[LCDAT](lcdat.md)

[SETFONT](setfont.md)

[GLCDCMD](glcdcmd.md)

[GLCDDATA](glcddata.md)

See the SED.BAS sample from the sample directory

---

## glcdSSD1325_96x64

This lib is for SSD1325 based displays. This lib supports screen 96x64.

The lib is based on bascom code from Robert Wolgajew.

SSD1325 is used for OLED displays. Each pixel can have 16 tints. 

The usual graphic statements are supported. 

Images such as bitmaps can be converted into 16 grey tone images.

The ssd1325 conversion tool you can [download](<http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=247&Itemid=54>) from the MCS web server.

The sample below is using porta pins to control BS1 and BS2. Of course you would connect them to VDD directly.

The pins used, and bascom pins names are :

SSD pin | BASCOM pin  
---|---  
WR | WR  
RD | RD  
D0-D7 | PORTx  
D/C | A0  
RES | RST  
CS | CS1  
VCC | VCC  
  
The VCC pin controls a 12V generator. 

Since the display is using a pallet of 16 grey tones, you must specify the foreground and background colors with LCDAT.

```vb
'-------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' oled_ssd1325.bas  
' demonstrates OLED display 96x64 with SSD1325 chip  
' Based on bascom SSD1325 code from Robert Wolgajew  
'-------------------------------------------------------------------------------  
$regfile = "m8535.dat"  
$crystal = 3686000  
$hwstack = 48  
$swstack = 48  
$framesize = 48  
  
  
'normally the BS1 and BS2 pins would be connected to VCC on the PCB  
'but the test PCB used 2 port pins  
Config Porta.0 = Output  
Config Porta.1 = Output  
```
Porta.0 = 1  
Porta.1 = 1  
  
  
```vb
$lib "glcdSSD1325_96x64.lbx" ' include the lib  
  
'vcc is 12V and must be enabled later. This means vcc needs a control pin.  
Config Graphlcd = 96x64ssd1325 , Dataport = Portc , Wr = Portd.6 , Rd = Portd.7 , Cs1 = Portd.3 , A0 = Portd.5 , Rst = Portd.4 , Vcc = Portd.2  
  
  
```
Cls 'as usual clear display  
  
Dim J As Byte , K As Byte , W As Word  
  
Line(0 , 0) -(95 , 63) , 15 ' diagonal line  
Line(0 , 63) -(95 , 0) , 6 ' diagonal line with other color  
  
  
Pset 1 , 0 , 15 'set a pixel  
  
Setfont Color8x8 ' font to use  
Lcdat 20 , 0 , "123" , 15 , 0 'and show some text  
  
Waitms 3000  
  
Showpic 0 , 0 , Plaatje  
  
  
```vb
End  
'include font  
$include "color8x8.font"  
'$include "color16x16.font"  
  
  
```
Plaatje:  
$bgf "ssd1325.bgc"

---

## INITLCD

Action

Initializes the LCD display.

Syntax

INITLCD

Remarks

The LCD display is initialized automatic at start up when LCD statements are used by your code.

This is done by a call to _LCD_INIT.

If you include the INITLCD statement in your code, the automatic call is disabled and the _LCD_INIT is called at the place in your code where you put the INITLCD statement. (initlcd is translated into a call to _init_lcd).

Why is this useful? 

•| In an environments with static electricity, the display can give strange output.  
---|---  
  
You can initialize the display then once in a while. When the display is initialized, the display content is cleared also.

•| The LCD routines depend on the fact that the WR pin of the LCD is connected to ground. But when you connect it to a port pin, you must first set the logic level to 0 and after that you can initialize the display by using INITLCD  
---|---  
  
•| Xmega chips need a stable oscillator. This is done with some CONFIG statements. The INITLCD should be placed after these commands. And since the Xmega by default has a slow internal oscillator, without using INITLCD at the proper location, your application would start slow. See the explanation below.  
---|---  
  
•| So in short you have more control when the LCD is initialized.  
---|---  
  
![notice](notice.jpg)The [CONFIG LCDPIN](config_lcdpin.md) has an option to use the WR pin, and use the busy flag of the display. If you have enough pins, this is the best mode. 

![notice](notice.jpg)The XMEGA has a built in internal oscillator that runs at a relative slow speed. If your code sets the speed to 32 MHz and you also include the $crystal=32000000 directive, you will notice a delay in the start of the code. This is caused by the fact that the delay routines are calculated with the 32 Mhz frequency, but the actual oscillator speed is 1 or 2 MHz.

There are 2 solutions possible. 

\- you can use $crystal=1000000 and then after you have set up the clock speed with CONFIG OSC, you can use another $CRYSTAL directive with the new speed.

\- you use $INITMICRO and put the CONFIG OSC in the _INIT_MICRO code. This will ensure that the micro will run at the specified speed early as possible.

ASM

The generated ASM code :

Rcall _Init_LCD

See also

[LCD](lcd_1.md) , [CONFIG LCDPIN](config_lcdpin.md)

Example

NONE

---

## LCD

Action

Send constant or variable to LCD display.

Syntax

LCD x

Remarks

X | Variable or constant to display.  
---|---  
  
More variables can be displayed separated by the ; -sign

LCD a ; b1 ; "constant"

The LCD statement behaves just like the [PRINT](print.md) statement. So [SPC](spc.md)() can be used too.

The only difference with PRINT is that no CR+LF is added when you send data to the LCD.

See also

[$LCD](lcd_1.md) , [$LCDRS](lcdrs.md) , [CONFIG LCD](config_lcd.md) , [SPC](spc.md) , [CLS](cls.md) , [INITLCD](initlcd.md) , [SHIFTLCD](shiftlcd.md) , [SHIFTCURSOR](shiftcursor.md) , [CURSOR](cursor.md) , [LCDCMD](lcdcmd.md), [LCDDATA](lcddata.md)

Example

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

Config Lcd = 16 * 2 'configure lcd screen

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

REM BETTER USE LCDCMD 

End

---

## LCD Commands



---

## LCD RGB-8 Converter

Action

This tool is intended to convert normal bitmaps into BGC files.

The BGC format is the Bascom Graphic Color Format.

This is a special RLE compressed format to save space.

The SHOWPIC statement can display graphic bitmaps.

The color display uses a special RGB8 format.

The LCD converter has the task to convert a normal windows bitmap into a 256-color RGB8 coded format.

When you run the tool you will see the following window :

![rgb8-converter](rgb8-converter.png)

You can use File , Open, to load an image from disk.

Or you can use Edit, Paste, to paste an image from the clipboard.

Option | Description  
---|---  
File, Open | Open a graphical file from disk.  
File, Save, Image | Save the file as a windows graphical file  
File, Save, Binary | Save the BGC file, the file you need with SHOWPIC  
File, Save , Data Lines | Save the file as data lines into a text file  
File, Convert | Converts the bitmap into a RGB8 bitmap  
Edit, Bitmap height | height of the image. Change it to make the image smaller or larger  
Edit, Bitmap width | width of the image. Change it to make the image wider.  
Edit, Select All | Select entire image  
Edit, Copy | Copy selection to the clipboard  
Edit, Paste | Paste clipboard to the selection. You must have an area selected !  
Edit, Delete | Delete the selected area  
  
The Output TAB, has an option : Save as RLE. This must be checked. By default it is checked.

When you do not want the image to be RLE encoded, you can uncheck this option.

The bottom area is used to store the DATA lines.

The Color TAB shows the effect on the table inside the color display.

When a picture uses a lot of different red colors, you can put the most used into the table.

It is well explained in the manuals from display3000.

By clicking on the color , you can view which colors are used by the picture.

You can match them with the color table.

You can download the LCD Converter tool from :

[http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=168&Itemid=54](<http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=168&Itemid=54>)

---

## LCD-EPSON

This chip is compatible with [PCF8533](pcf8533.md).

---

## LCD4.LIB

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

---

## LCD4_anypin_oled_RS0010

This LCD driver is intended to be used with the OLED LCD RS0010.

This LCD text driver can be used with any pin. It supports the WR pin in which case the LCD will be used in busy mode.

A typical sample is shown below.

```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack=32  
$swstack = 16  
$framesize=24  
  
  
  
$lib "lcd4_anypin_oled_RS0010.lib" 'override default lib with OLED lib  
  
'Config Lcd Sets The Portpins Of The Lcd  
Config Lcdpin = Pin , Db4 = Portb.2 , Db5 = Portb.3 , Db6 = Portb.4 , Db7 = Portb.5 , E = Portb.1 , Rs = Portb.0  
Config Lcd = 16x2 '16*2 type LCD screen  
  
Dim V As Byte  
  
```
Cls  
Lcd "ABC" ; Chr(253)  
Lowerline  
Lcd "test"  
Const Test = " this is a test" ' Just A Test  
  
Lcdfont 0 'select first font  
  
Cls  
Dim X As Byte , Y As Byte  
X = &B1000_0000 + 0  
Lcdcmd &B0001_1111 'gmode  
Lcdcmd X 'X (0-99)  
Lcdcmd &B0100_0000 'Y (0-1)  
  
```vb
'send data  
For V = 1 To 80  
```
Lcddata &B10101010  
```vb
Waitms 100  
Next  
End

```

---

## LCD4BUSY

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

---

## LCD4E2

The built in LCD driver for the PIN mode is written to support a worst case scenario where you use random pins of the microprocessor to drive the LCD pins.

This makes it easy to design your PCB but it needs more code.

When you want to have less code you need fixed pins for the LCD display.

With the statement $LIB "LCD4E2.LBX" you specify that the LCD4.LIB will be used.

The following connections are used in the asm code:

Rs = PortB.0

RW = PortB.1 we donât use the R/W option of the LCD in this version so connect to ground

E = PortB.2

E2 = PortB.3 the second E pin of the LCD

Db4 = PortB.4 the data bits must be in a nibble to save code

Db5 = PortB.5

Db6 = PortB.6

Db7 = PortB.7

You can change the lines from the lcd4e2.lib file to use another port.

Just change the address used :

.EQU LCDDDR=$17 ; change to another address for DDRD ($11)

.EQU LCDPORT=$18 ; change to another address for PORTD ($12)

See the demo lcdcustom4bit2e.bas in the SAMPLES dir.

Note that you still must select the display that you use with the [CONFIG LCD](config_lcd.md) statement.

See also the [lcd4.lib](lcd4_lib.md) for driving a display with 1 E line.

A display with 2 E lines actually is a display with 2 control chips. They must both be controlled. This library allows you to select the active E line from your code.

In your basic code you must first select the E line before you use a LCD statement.

The initialization of the display will handle both chips.

Note that LBX is a compiled LIB file. In order to change the routines you need the commercial edition with the source code(lib files). After a change you should compile the library with the library manager.

---

## LCD_RX1602A5

This LCD driver is based on O-Family AQM0802A Library.

It is suited for I2C displays RX1602A5. It was developed for, and sponsored by Lab microelectronic GmbH

All you need to do is connect the LCD to the I2C pins and configure LCD like : config lcd = 16x2 , chipset = st7032

A sample you find under [CONFIG LCD](config_lcd.md)

Of course you need a functional I2C or TWI bus. Both soft and HW TWI are supported.

---

## LCDAT

Action

Send constant or variable to a SED or other graphical display.

Syntax

LCDAT y , x , var [ , inv]

LCDAT y , x , var [ , FG, BG]

Remarks

X | X location. In the range from 0-63. The SED displays columns are 1 pixel width. Other displays might have a bigger range such as 132 or 255.  
---|---  
Y | Y location. The row in pixels. The maximum value depends on the display. The minimum value also depends on the used display. Most displays have minimum value of 0. KS108 has a minimum value of 1.  
Var | The constant or variable to display  
inv | Optional number. Value 0 will show the data normal. Any other value will invert the data.  
| For COLOR DISPLAYS  
FG | Foreground color  
BG | Background color  
  
You need to include the glibSED library with :

$LIB "glibsed.lbx"

Other libraries must be included with a different directive.

See also

[CONFIG GRAPHLCD](config_lcd.md) , [SETFONT](setfont.md), [GLCDCMD](glcdcmd.md), [GLCDDATA](glcddata.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sed1520.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates the SED1520 based graphical display support

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 7372800 ' used crystal frequency

$baud = 115200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'I used a Staver to test

'some routines to control the display are in the glcdSED.lib file

'IMPORTANT : since the SED1520 uses 2 chips, the columns are split into 2 of 60.

'This means that data after column 60 will not print correct. You need to locate the data on the second halve

'For example when you want to display a line of text that is more then 8 chars long, (8x8=64) , byte 8 will not draw correctly

'Frankly i find the KS0108 displays a much better choice.

$lib "glcdSED1520.lbx"

'First we define that we use a graphic LCD

Config Graphlcd = 120 * 64sed , Dataport = Porta , Controlport = Portd , Ce = 5 , Ce2 = 7 , Cd = 3 , Rd = 4

'The dataport is the portname that is connected to the data lines of the LCD

'The controlport is the portname which pins are used to control the lcd

'CE =CS Chip Enable/ Chip select

'CE2= Chip select / chip enable of chip 2

'CD=A0 Data direction

'RD=Read

'Dim variables (y not used)

Dim X As Byte , Y As Byte

'clear the screen

```
Cls

```vb
Wait 2

'specify the font we want to use

```
Setfont Font8x8

```vb
'You can use locate but the columns have a range from 1-132

'When you want to show somthing on the LCD, use the LDAT command

'LCDAT Y , COL, value

```
Lcdat 1 , 1 , "1231231"

Lcdat 3 , 80 , "11"

```vb
'lcdat accepts an additional param for inversing the text

'lcdat 1,1,"123" , 1 ' will inverse the text

Wait 2

```
Line(0 , 0) -(30 , 30) , 1

Wait 2

Showpic 0 , 0 , Plaatje 'show a comnpressed picture

```vb
End 'end program

'we need to include the font files

$include "font8x8.font"

'$include "font16x16.font"

```
Plaatje:

```vb
'include the picture data

$bgf "smile.bgf"

```

---

## LCDAUTODIM

Action

Dims the 20x4vfd LCD.

Syntax

LCDAUTODIM x

Remarks

X | A variable or constant in the range from 0-54 0 will turn auto dim off. A value between 1-54 dims the brightness after the given number of seconds. The value is stored permanent.  
---|---  
  
This statement works only with the 20x4vfd display from "Electronic Design Bitzer"

Available in the MCS Shop.

See also

NONE

Example

NONE

---

## LCDCMD

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

---

## LCDCONTRAST

Action

Set the contrast of a TEXT LCD.

Syntax

LCDCONTRAST x

Remarks

X | A variable or constant in the range from 0-3.  
---|---  
  
Some LCD text displays support changing the contrast. Noritake displays have this option for example.

See also

[LCD](lcd_2.md), [LCDFONT](lcdfont.md)

Example

NONE

---

## LCDDATA

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

---

## LCDFONT

Action

Selects the font of the TEXT LCD.

Syntax

LCDFONT x

Remarks

X | A variable or constant in the range from 0-3.  
---|---  
  
Most text LCD displays have one or more built in font tables. By default font 0 is selected.

The LCDFONT statement allows you to chose another font.

See also

[LCD](lcd_2.md) , [INITLCD](initlcd.md) , [LCDCMD](lcdcmd.md), [LCDDATA](lcddata.md)

Example

```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack=32  
$swstack = 16  
$framesize=24  
  
  
  
$lib "lcd4_anypin_oled_RS0010.lib" 'override default lib with OLED lib  
  
'Config Lcd Sets The Portpins Of The Lcd  
Config Lcdpin = Pin , Db4 = Portb.2 , Db5 = Portb.3 , Db6 = Portb.4 , Db7 = Portb.5 , E = Portb.1 , Rs = Portb.0  
Config Lcd = 16x2 '16*2 type LCD screen  
  
Dim V As Byte  
  
```
Cls  
Lcd "ABC" ; Chr(253)  
Lowerline  
Lcd "test"  
Const Test = " this is a test" ' Just A Test  
  
Lcdfont 0 'select first font  
  
Cls  
Dim X As Byte , Y As Byte  
X = &B1000_0000 + 0  
Lcdcmd &B0001_1111 'gmode  
Lcdcmd X 'X (0-99)  
Lcdcmd &B0100_0000 'Y (0-1)  
  
```vb
'send data  
For V = 1 To 80  
```
Lcddata &B10101010  
```vb
Waitms 100  
Next  
End

```

---

## Options Compiler LCD

![image632224065](image632224065.jpg)

Options Compiler LCD

Item | Description  
---|---  
LCD type | The LCD display used.  
Bus mode | The LCD can be operated in BUS mode or in PIN mode. In PIN mode, the data lines of the LCD are connected to the processor port pins. In BUS mode the data lines of the LCD are connected to the data lines of the BUS. Select 4 when you have only connect DB4-DB7. When the data mode is 'pin' , you should select 4.  
Data mode | Select the mode in which the LCD is operating. In PIN mode, individual processor pins can be used to drive the LCD. In BUS mode, the external data bus is used to drive the LCD.  
LCD address | In BUS mode you must specify which address will select the enable line of the LCD display. For the STK200, this is C000 = A14 + A15.  
RS address | In BUS mode you must specify which address will select the RS line of the LCD display. For the STK200, this is 8000 = A15  
Enable | For PIN mode, you must select the processor pin that is connected to the enable line of the LCD display.  
RS | For PIN mode, you must select the processor pin that is connected to the RS line of the LCD display.  
DB7-DB4 | For PIN mode, you must select the processor pins that are connected to the upper four data lines of the LCD display.  
Make upper 3 bits high in LCD designer | Some displays require that for setting custom characters, the upper 3 bits must be 1. Should not be used by default.  
  
It is advised to use the CONFIG LCD command. This way the settings are stored in your source code and not in the separate CFG file.

---

## SHIFTLCD

Action

Shift the LCD display left or right by one position.

Syntax

SHIFTLCD LEFT / RIGHT

Remarks

NONE

See also

[SHIFTCURSOR](shiftcursor.md) , [SHIFTCURSOR](shiftcursor.md) , [INITLCD](initlcd.md) , [CURSOR](cursor.md)

Partial Example

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

---

## Tools LCD Designer

With this option you can design special characters for LCD-text displays.

The following window will appear:

![lcd_designer](lcd_designer.png)

The LCD-matrix has 7x5 points. The bottom row is reserved for the cursor but can be used.

You can select a point by clicking the left mouse button. If a cell was selected it will be unselected.

Clicking the Set All button will set all points.

Clicking the Clear All button will clear all points.

When you are finished you can press the Ok button : a statement will be inserted in your active program-editor window at the current cursor position. The statement looks like this :

Deflcdchar ?,1,2,3,4,5,6,7,8

You must replace the ?-sign with a character number ranging from 0-7.

The eight bytes define how the character will appear. So they will be different depending on the character you have drawn.

See Also

[Font Editor](font_editor.md)

---
