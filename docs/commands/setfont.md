# SETFONT

Action

Sets the current font which can be used on some graphical displays.

Syntax

SETFONT font

Remarks

font | The name of the font that need to be used with LCDAT statements.  
---|---  
  
Since SED-based displays do not have their own font generator, you need to define your own fonts. You can create and modify your own fonts with the FontEditor Plugin.

SETFONT will set an internal used data pointer to the location in memory where you font is stored. The name you specify is the same name you use to define the font.

You need to include the used fonts with the $include directive:

$INCLUDE "font8x8.font"

The order of the font files is not important. The location in your source is however important.

The $INCLUDE statement will include binary data and this may not be accessed by the flow of your program.

When your program flow enters into font code, unpredictable results will occur.

So it is best to place the $INCLUDE files at the end of your program behind the END statement.

You need to include the glibSED library with :

```vb
$LIB "glibsed.lbx"

While original written for the SED1521, fonts are supported on a number of displays now including color displays.

```
See also

[CONFIG GRAPHLCD](config_lcd.md) , [LCDAT](lcdat.md), [GLCDCMD](glcdcmd.md), [GLCDDATA](glcddata.md)

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