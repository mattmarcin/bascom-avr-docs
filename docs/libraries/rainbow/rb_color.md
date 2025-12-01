# RB_COLOR

Action

Color multiple LED's according to the bit pattern of a mask.

Syntax

RB_COLOR LED_start , Mask, Color1 [,Color2]

Remarks

LED_start | The index of the LED number. First LED is 0.   
---|---  
Mask | Bitmask of 8 LEDâs. A set bit(1) will color a LED with COLOR1, according to its bit position + LED_start. A zero-bit turns a LED off, or optionally colors an LED with COLOR2.   
Color1 | A byte array with a minimum length of 3 that holds the RGB information. A LONG or DWORD can be used as well.   
Color2 | This is an optional parameter. A byte array with a minimum length of 3 that holds the RGB information. A LONG or DWORD can be used as well.   
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) [RB_COPY](rb_copy.md)

Example

```vb
'======================================  
'RB_COLOR test  
'======================================  
$Regfile = "m32adef.dat"  
$Crystal = 16000000  
$hwstack = 40  
$swstack = 32  
$framesize = 32  
Config Rainbow = 2 , Rb0_len = 8 , Rb0_port = Porta , Rb0_pin = 0 , Rb1_len = 8 , Rb1_port = Porta , Rb1_pin = 1  
Dim Color1 as Dword  
Dim Color2 as Dword  
```
Const Red = &H000010  
Const Blue = &H100000  
  
Color1 = Red  
Color2 = Blue  
Rb_selectchannel 0  
Do  
Rb_color 0 , &H88 , Color1  
Rb_send  
Wait 1  
Rb_color 0 , &H88 , Color2 , Color1  
Rb_send  
```vb
Wait 1  
Loop  
End

```