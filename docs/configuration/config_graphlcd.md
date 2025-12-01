# CONFIG GRAPHLCD

Action

Configures the Graphical LCD display.

Syntax

Config GRAPHLCD = type , DATAPORT = port, CONTROLPORT=port , CE = pin , CD = pin , WR = pin, RD=pin, RESET= pin, FS=pin, MODE = mode

Remarks

Type | This must be 240X64, 128X128, 128X64 , 160X48 , 240X128, 192X64 , SED180X32 or 192X64SED. For SED displays use 128X64sed or 120X64SED or SED180X32 For 132x132 color displays, use COLOR For EADOG128x64 use 128X64EADOGM  For SSD1325 96x64 use 96X64SSD1325. See [SSD1325lib](glcdssd1325_96x64.md). For custom libs : CUSTOM.  The following options are optional for custom LCD: \- cols= num of cols in pixels \- rows= num of rows in pixels \- kind= any number to specify the lcd \- lcdname="somename" , an optional name to identify the LCD  
---|---  
Dataport | The name of the port that is used to put the data on the LCD data pins db0-db7. PORTA for example.  
Controlport | This is the name of the port that is used to control the LCD control pins. PORTC for example  
Ce | The pin number that is used to enable the chip on the LCD.  
Cd | The pin number that is used to control the CD pin of the display.  
WR | The pin number that is used to control the /WR pin of the display.  
RD | The pin number that is used to control the /RD pin of the display.  
FS | The pin number that is used to control the FS pin of the display. Not needed for SED based displays.  
RESET | The pin number that is used to control the RESET pin of the display.  
MODE | The number of columns for use as text display. Use 8 for X-pixels / 8 = 30 columns for a 240 pixel screen. When you specify 6, 240 / 6 = 40 columns can be used.  
  
| EADOG128M pins for SPI mode. This display only can write data. As a result, a number of graphical commands are not supported.  
CS1 | Chip select for EADOG128x64  
A0 | A0 line for EADOG128x64. This is the line that controls data/command  
SI | This is the serial input pin for the EADOG128x64.   
SCLK | This is the clock pin for the EADOG128x64.  
  
| ST7565R parallel data mode A 128x64 graphical display which supports all graphic commands  
dataport | The data port connected to the display. For example portJ  
CS1 | the chip enabled line  
A0 | the chip data/command mode pin  
RST | the reset pin of the chip  
WR | The /WR line of the chip  
RD | The /RD line of the chip  
C86 | This pin selects the transfer mode.  
PM | Some displays have this PM pin which sets the parallel mode  
example  | Config Graphlcd = 128 * 64eadogm ,dataport=portj, Cs1 = Porth.0 , A0 = Porth.2 , rst= Porth.1 , wr = Porth.3 , Rd = Porth.4,c86=porth.6  
  
The first graphical LCD chip supported was T6963C. There are also drivers for other LCD's such as SED and KS0108. The most popular LCD's will be supported with a custom driver.

The following connections were used for the T6963C:

PORTA.0 to PORTA.7 to DB0-DB7 of the LCD

PORTC.5 to FS, font select of LCD

PORTC.2 to CE, chip enable of LCD

PORTC.3 to CD, code/data select of LCD

PORTC.0 to WR of LCD, write

PORTC.1 to RD of LCD, read

PORTC.4 to RESET of LCD, reset LCD

The LCD used from www.conrad.de needs a negative voltage for the contrast.

Two 9V batteries were used with a pot meter.

Some displays have a Vout that can be used for the contrast(Vo)

The T6963C displays have both a graphical area and a text area. They can be used together. The routines use the XOR mode to display both text and graphics layered over each other.

The statements that can be used with the graphical LCD are :

[CLS](cls.md), will clear the graphic display and the text display

CLS GRAPH will clear only the graphic part of the display

CLS TEXT will only clear the text part of the display

[LOCATE](locate.md) row,column : Will place the cursor at the specified row and column

The row may vary from 1 to 16 and the column from 1 to 40. This depends on the size and mode of the display.

[CURSOR](cursor.md) ON/OFF BLINK/NOBLINK can be used the same way as for text displays.

[LCD](lcd_2.md) : can be handled the same way as for text displays.

[SHOWPIC](showpic.md) X, Y , Label : Show image where X and Y are the column and row and Label is the label where the picture info is placed.

[PSET](pset.md) X, Y , color : Will set or reset a pixel. X can range from 0-239 and Y from 9-63. When color is 0 the pixel will turned off. When it is 1 the pixel will be set on.

[$BGF](_bgf.md) "file.bgf" : inserts a BGF file at the current location

[LINE](line.md)(x0,y0) â (x1,y1) , color : Will draw a line from the coordinate x0,y0 to x1,y1.

Color must be 0 to clear the line and 255 for a black line.

[BOX](box.md)(x0,y0)-(x1,y1), color : Will draw a box from x0,y0 to x1,y1. Color must be 0 to clear the box and 255 for a black line.

[BOXFILL](boxfill.md)(x0,y0)-(x1,y1), color : Will draw a filled box from x0,y0 to x1,y1. Color must be 0 or 255.

The Graphic routines are located in the glib.lib or glib.lbx files.

You can hard wire the FS and RESET and change the code from the glib.lib file so these pins can be used for other tasks.

COLOR LCD

Color displays were always relatively expensive. The mobile phone market changed that. And Display3000.com , sorted out how to connect these small nice colorful displays.

You can buy brand new Color displays from Display3000. MCS Electronics offers the same displays.

There are two different chip sets used. One chipset is from EPSON and the other from Philips. For this reason there are two different libraries. When you select the wrong one it will not work, but you will not damage anything.

LCD-EPSON.LBX need to be used with the EPSON chipset.

LCD-PCF8833.LBX need to be used with the Philihps chipset.

Config Graphlcd = Color , Controlport = Portc , Cs = 1 , Rs = 0 , Scl = 3 , Sda = 2

Controlport | The port that is used to control the pins. PORTA, PORTB, etc.  
---|---  
CS | The chip select pin of the display screen. Specify the pin number. 1 will mean PORTC.1  
RS | The RESET pin of the display  
SCL | The clock pin of the display  
SDA | The data pin of the display  
  
As the color display does not have a built in font, you need to generate the fonts yourself.

You can use the [Fonteditor](font_editor.md) for this task.

A number of statements accept a color parameter. See the samples below in bold.

LINE | Line(0 , 0) -(130 , 130) , Blue  
---|---  
LCDAT | Lcdat 100 , 0 , "12345678" , Blue , Yellow  
CIRCLE | Circle(30 , 30) , 10 , Blue  
PSET | 32 , 110 , Black  
BOX | Box(10 , 30) -(60 , 100) , Red  
  
See also

[SHOWPIC](showpic.md) , [PSET](pset.md) , [$BGF](_bgf.md) , [LINE](line.md) , [LCD](lcd_1.md) , [BOX](box.md) , [BOXFILL](boxfill.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : t6963_240_128.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : T6963C graphic display support demo 240 * 128

'micro : Mega8535

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m8535.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'-----------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' T6963C graphic display support demo 240 * 128

'-----------------------------------------------------------------

'The connections of the LCD used in this demo

'LCD pin connected to

' 1 GND GND

'2 GND GND

'3 +5V +5V

'4 -9V -9V potmeter

'5 /WR PORTC.0

'6 /RD PORTC.1

'7 /CE PORTC.2

'8 C/D PORTC.3

'9 NC not conneted

'10 RESET PORTC.4

'11-18 D0-D7 PA

'19 FS PORTC.5

'20 NC not connected

'First we define that we use a graphic LCD

' Only 240*64 supported yet

Config Graphlcd = 240 * 128 , Dataport = Porta , Controlport = Portc , Ce = 2 , Cd = 3 , Wr = 0 , Rd = 1 , Reset = 4 , Fs = 5 , Mode = 8

'The dataport is the portname that is connected to the data lines of the LCD

'The controlport is the portname which pins are used to control the lcd

'CE, CD etc. are the pin number of the CONTROLPORT.

' For example CE =2 because it is connected to PORTC.2

'mode 8 gives 240 / 8 = 30 columns , mode=6 gives 240 / 6 = 40 columns

'Dim variables (y not used)

Dim X As Byte , Y As Byte

'Clear the screen will both clear text and graph display

```
Cls

```vb
'Other options are :

' CLS TEXT to clear only the text display

' CLS GRAPH to clear only the graphical part

```
Cursor Off

```vb
Wait 1

'locate works like the normal LCD locate statement

' LOCATE LINE,COLUMN LINE can be 1-8 and column 0-30

```
Locate 1 , 1

'Show some text

Lcd "MCS Electronics"

'And some othe text on line 2

Locate 2 , 1 : Lcd "T6963c support"

Locate 3 , 1 : Lcd "1234567890123456789012345678901234567890"

Locate 16 , 1 : Lcd "write this to the lower line"

Wait 2

Cls Text

```vb
'use the new LINE statement to create a box

'LINE(X0,Y0) - (X1,Y1), on/off

```
Line(0 , 0) -(239 , 127) , 255 ' diagonal line

Line(0 , 127) -(239 , 0) , 255 ' diagonal line

Line(0 , 0) -(240 , 0) , 255 ' horizontal upper line

Line(0 , 127) -(239 , 127) , 255 'horizontal lower line

Line(0 , 0) -(0 , 127) , 255 ' vertical left line

Line(239 , 0) -(239 , 127) , 255 ' vertical right line

```vb
Wait 2

' draw a line using PSET X,Y, ON/OFF

' PSET on.off param is 0 to clear a pixel and any other value to turn it on

For X = 0 To 140

```
Pset X , 20 , 255 ' set the pixel

```vb
Next

For X = 0 To 140

```
Pset X , 127 , 255 ' set the pixel

```vb
Next

Wait 2

'circle time

'circle(X,Y), radius, color

'X,y is the middle of the circle,color must be 255 to show a pixel and 0 to clear a pixel

For X = 1 To 10

```
Circle(20 , 20) , X , 255 ' show circle

Wait 1

Circle(20 , 20) , X , 0 'remove circle

```vb
Wait 1

Next

Wait 2

For X = 1 To 10

```
Circle(20 , 20) , X , 255 ' show circle

```vb
Waitms 200

Next

Wait 2

'Now it is time to show a picture

'SHOWPIC X,Y,label

'The label points to a label that holds the image data

```
Test:

Showpic 0 , 0 , Plaatje

Showpic 0 , 64 , Plaatje ' show 2 since we have a big display

Wait 2

Cls Text ' clear the text

```vb
End

'This label holds the mage data

```
Plaatje:

```vb
'$BGF will put the bitmap into the program at this location

$bgf "mcs.bgf"

'You could insert other picture data here

```