# RB_ANDCOLOR

Action

Ands specified color info to the specified LED in memory

Syntax

RB_ANDCOLOR Led , Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
Led | The index of the LED number. First LED is 0.   
  
The operation is performed on the memory. An AND operation can clear part of a color. You need to use RB_SEND so that the LED reflects the new color information.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Demo_Softblink.bas  
'This demo show RB_OrColor and RB_AndColor which can be used  
'for a flashing LED with a fade effect.  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal=8000000  
$hwstack=32  
$swstack=16  
$framesize=32  
Config RAINBOW=1, RB0_LEN=8, RB0_PORT=PORTB,rb0_pin=0  
' ^ connected to pin 0  
' ^------------ connected to portB  
' ^-------------------------- 8 leds on stripe  
' ^------------------------------------- 1 channel  
  
```
Const Numled=8  
```vb
Dim MASK as Dword  
Dim Fade as Byte  
  
'----[MAIN]---------------------------------------------------------------------  
```
RB_SelectChannel 0 ' select first channel  
  
```vb
Do  
For Fade = 0 to 7  
Waitms 20  
```
Shift MASK , left  
Incr MASK  
RB_ORColor 0 , MASK  
RB_Send  
```vb
Next  
For Fade = 0 to 7  
Waitms 20  
```
Shift MASK , right  
RB_ANDColor 0 , MASK  
RB_Send  
```vb
Next  
Loop

```