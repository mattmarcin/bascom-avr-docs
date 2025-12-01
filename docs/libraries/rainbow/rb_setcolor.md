# RB_SETCOLOR

Action

Set the color of a LED.

Syntax

RB_SETCOLOR LEDnr , color()

Remarks

LEDnr | A word variable or numeric constant which defines the index of the LED. This should be a valid index for the active channel. When the current channel has 8 leds defined with CONFIG RAINBOW, a valid number would be in the range from 0-7. Leds start counting at 0. This is independent of the option base !  
---|---  
color() | A byte array with a minimum length of 3 that holds the RGB information. A LONG or DWORD can be used as well.  
  
The color information is set in memory. To update the color of the LED, use RB_SEND

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_KnightriderDual.bas  
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
RB_SetColor 0 , color(1) ' update led on the left  
RB_SetColor 7 , color(1) ' update led on the right  
RB_Send  
  
```vb
Do  
For n = 1 to Numleds/2 - 1  
```
rb_Shiftright 0 , Numleds/2 'shift to the right  
rb_Shiftleft 4 , Numleds/2 'shift to the left all leds except the last one  
Waitms 100  
RB_Send  
```vb
Next  
For n = 1 to Numleds/2 - 1  
```
rb_Shiftleft 0 , Numleds/2 'shift to the left all leds except the last one  
rb_Shiftright 4 , Numleds/2 'shift to the right  
Waitms 100  
RB_Send  
```vb
Next  
waitms 500 'wait a bit  
Loop

```