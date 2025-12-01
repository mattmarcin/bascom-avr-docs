# SHOWPICE

Action

Shows a BGF file stored in EEPROM on the graphic display

Syntax

SHOWPICE x, y , label

Remarks

Showpice can display a converted BMP file that is stored in the EEPROM of the micro processor. The BMP must be converted into a BGF file with the [Tools Graphic Converter](tools_graphic_converter.md).

The X and Y parameters specify where the picture must be displayed. X and Y must be 0 or a multiple of 8. The picture height and width must also be a multiple of 8.

The label tells the compiler where the graphic data is located. It points to a label where you put the graphic data with the $BGF directive.

You can store multiple pictures when you use multiple labels and $BGF directives,

Note that the BGF files are RLE encoded to save code space.

See also

[PSET](pset.md) , [$BGF](_bgf.md) , [CONFIG GRAPHLCD](config_graphlcd.md) , [LINE](line.md) , [SHOWPIC](showpic.md) , [CIRCLE](circle.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : showpice.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates showing a picture from EEPROM

'micro : AT90S8535

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8535def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'First we define that we use a graphic LCD

' Only 240*64 supported yet

Config Graphlcd = 240 * 128 , Dataport = Porta , Controlport = Portc , Ce = 2 , Cd = 3 , Wr = 0 , Rd = 1 , Reset = 4 , Fs = 5 , Mode = 8

'The dataport is th e portname that is connected to the data lines of the LCD

'The controlport is the portname which pins are used to control the lcd

'CE, CD etc. are the pin number of the CONTROLPORT.

' For example CE =2 because it is connected to PORTC.2

'mode 8 gives 240 / 8 = 30 columns , mode=6 gives 240 / 6 = 40 columns

'we will load the picture data into EEPROM so we specify $EEPROM

'the data must be specified before the showpicE statement.

$eeprom

```
Plaatje:

```vb
'the $BGF directive will load the data into the EEPROM or FLASH depending on the $EEPROM or $DATA directive

$bgf "mcs.bgf"

'switch back to normal DATA (flash) mode

$data

'Clear the screen will both clear text and graph display

```
Cls

```vb
'showpicE is used to show a picture from EEPROM

'showpic must be used when the data is located in Flash

```
Showpice 0 , 0 , Plaatje

End