# CONFIG RAINBOW

Action

This configuration command sets up the number of rainbow channels and their ports & pins.

Syntax

CONFIG RAINBOW=channels, [,RGB=rgb] , RBx_LEN=leds, RBx_PORT=port, RBx_PIN=pin

Remarks

Channels | The number of channels. This is a numeric value in the range from 1-16. Each channel drives a port pin.  
---|---  
RGB | An optional parameter that has to be defined second when used. The WS2812 leds are GRB leds. (green, red, blue). 24 bits of data are sent. RGBW leds have an additional white led and are mapped RGBW. 32 bits of data are sent.  The possible options are : 3 - The default. Leds like WS2811/WS2812 with GRB order. 4 - RGBW leds like SK6812RGBW. Notice that 1 more byte internal memory is needed for each led. This option will use RAINBOWBSCN.lib   
RBx_LEN | The number of LED's for the channel. The minimum number of leds is 1. Each LED is made of 3 colors : R(ed), G(reen), and B(lue). A byte array named RAINBOW0_ will be created with a size of len * 3. Thus RB0_LEN=8 will create an array of RAINBOW0_(24).  For RGBW LEDS, the array will have a length of len * 4 to store the additional white color.  
RBx_PORT | The name of the PORT which is connected to the DI of the rainbow led(stripe). This is a port like PORTB.  
RBx_PIN | The pin number of the port pin which is connected to the DI of the rainbow led(stripe). This is a number between 0-7.  
  
* The x should be replaced by a numeric value from 0-7.

Rainbow leds come in different forms and shapes. There are single LED, stripes with 8 leds, round circles with 24 leds, etc. All have a built in WS2812 RGB controller. The nice thing is that you can cascade leds by connecting the DO (output) to another DI (input). These stripes only requires 5V, GND and DI. You can connect different stripes to different port pins. 

The original rainbow library is written by Galahat from the German bascom-forum. It is an excellent example on how to write your own libraries. 

The MCS version is for the BASCOM integrated statements and functions. It is named rainbowBSC.lib. The lib uses a few routines from mcs.lib

![notice](notice.jpg)A minimum CPU-speed of 8 MHz is required. Tests with WS1812b- types showed, it also works with frequencies down to 6.5 MHz because of the tolerance bandwidth by the chips.

Each LED requires 3 or 4 bytes of memory to store the color. Internally, the color info is stored in RGB order. And for RGBW LEDS in RGBW color.

In version 2081 the library was updated to support RGBW LEDS. Some functions in the old lib manipulated the wrong colors. We corrected this in the new library. But to ensure compatibility, we also include the old library.

When you use RGB=4 you will use the new library automatically. Without this option, or when using a value of 3 : RGB=3 , you will use the old library.

In order to use the new library with option 3, you need to include the library in your code using the $LIB directive : $lib "RAINBOWBSCN.lib" 

This must be done BEFORE the CONFIG RAINBOW statement.

When using a normal AVR processor the used port must have a low IO address. Most ports have such an address. But processors like the Mega2560 also have some ports with an extended address. PORTH, PORTJ, PORTK and PORTL for example will not work. 

See also

[RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Knightrider.bas  
' based on sample from Galahat  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
Config RAINBOW=1, RB0_LEN=8, RB0_PORT=PORTB,rb0_pin=0  
' ^ connected to pin 0  
' ^------------ connected to portB  
' ^-------------------------- 8 leds on stripe  
' ^------------------------------------- 1 channel  
  
  
'Global Color-variables  
Dim Color(3) as Byte  
```
R alias Color(_base) : G alias Color(_base + 1) : B alias Color(_base + 2)  
  
'CONST  
const numLeds=8  
  
```vb
'----[MAIN]---------------------------------------------------------------------  
Dim n as Byte  
  
```
RB_SelectChannel 0 ' select first channel  
R = 50 : G = 0 : B = 100 ' define a color  
RB_SetColor 0 , color(1) ' update leds  
RB_Send  
  
```vb
Do  
For n = 1 to Numleds-1  
```
rb_Shiftright 0 , Numleds 'shift to the right all leds except the last one  
Waitms 100  
RB_Send  
```vb
Next  
For n = 1 to Numleds-1  
```
rb_Shiftleft 0 , Numleds 'shift to the left all leds except the last one  
Waitms 100  
RB_Send  
```vb
Next  
waitms 500 'wait a bit  
Loop  


```
EXAMPLE RGBW

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_KnightriderDual-RGBW.bas  
' based on sample from Galahat  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
Config RAINBOW = 1 , rgb = 4 , RB0_LEN = 8 , RB0_PORT = PORTB , rb0_pin = 0  
' ^-- using rgbW leds #### MUST BE FIRST PARAMETER when defined ###  
' ^ connected to pin 0  
' ^------------ connected to portB  
' ^-------------------------- 8 leds on stripe  
' ^------------------------------------- 1 channel  
  
  
'Global Color-variables  
Dim Color(4) as Byte  
```
R alias Color(_base) : G alias Color(_base + 1) : B alias Color(_base + 2) : W alias color(_base + 3)  
  
'CONST  
const numLeds = 8  
  
```vb
'----[MAIN]---------------------------------------------------------------------  
Dim n as Byte  
  
```
RB_SelectChannel 0 ' select first channel  
R = 50 : G = 0 : B = 100 : w = 10 ' define a color  
RB_SetColor 0 , color(_base) ' update led on the left  
RB_SetColor numleds - 1 , color(_base) ' update led on the right  
RB_Send  
```vb
waitms 2000  
  
Do  
For n = 1 to Numleds / 2 - 1  
```
rb_Shiftright 0 , Numleds / 2 'shift to the right  
rb_Shiftleft Numleds / 2 , Numleds / 2 'shift to the left all leds except the last one  
Waitms 1000  
RB_Send  
```vb
Next  
For n = 1 to Numleds/2 - 1  
```
rb_Shiftleft 0 , Numleds / 2 'shift to the left all leds except the last one  
rb_Shiftright Numleds / 2 , Numleds / 2 'shift to the right  
Waitms 1000  
RB_Send  
```vb
Next  
waitms 500 'wait a bit  
Loop

```