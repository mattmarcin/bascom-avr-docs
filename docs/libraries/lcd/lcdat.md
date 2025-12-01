# LCDAT

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