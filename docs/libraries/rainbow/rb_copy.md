# RB_COPY

Action

Copy whole stripes or any parts of it, to another stripes memory space at any position.

Syntax

RB_COPY Source , SourceStart, Target, TargetStart, Count

Remarks

Source | The index of the source stripe.   
---|---  
SourceStart | The position to start the copy from  
Target | The index of the target stripe. This can be the same stripe or another one.  
TargetStart | The position to start the copy to.   
Count | The number of bytes to copy.   
  
This routine offers a faster track to copy a whole bunch of color data , if necessary.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COLOR](rb_color.md)

Example

```vb
$regfile = "m32adef.dat"  
$crystal = 16000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
'(  
```
RB_Copy Rainbow0_ , 5 ,Rainbow1_ ,0 , 3  
```vb
' ^---- count of leds to copy  
' ^---------- Led, start index of target  
' ^------------------ target stripe or array  
' ^------------------------ LED, start index of source  
' ^-------------------------------- source stripe or array  
')  
  
Config Rainbow = 2 , Rb0_len = 8 , Rb0_port = Porta , Rb0_pin = 0 , _  
```
Rb1_len = 8 , Rb1_port = Porta , Rb1_pin = 1  
  
Dim Color as Dword  
  
Const Red = &H000010  
Const Green = &H001000  
Const Blue = &H100000  
Const Yellow = &H001010  
  
'color the first 4 LED  
Rb_selectchannel 0  
Color = Green  
Rb_setcolor 0 , Color  
  
Color = Red  
RB_SetColor 1 , Color  
  
Color = Blue  
RB_SetColor 2 , Color  
  
Color = Yellow  
RB_SetColor 3 , Color  
RB_Send  
```vb
wait 1  
' copy LED 0 to 3 of stripe 0 to pos 4 to 7  
```
Rb_copy Rainbow0_ , 0 , Rainbow0_ , 4 , 4  
Rb_send  
```vb
Wait 1  
  
' copy whole stripe0 to stripe1  
```
RB_Copy Rainbow0_ , 0 , Rainbow1_ , 0 , 8  
RB_Clearcolors  
RB_SelectChannel(0) : RB_Send  
RB_SelectChannel(1) : RB_Send  
```vb
Wait 1  
'copy LED1 of stripe1 to LED7 of stripe0  
```
RB_Copy Rainbow1_ , 1 , Rainbow0_ , 7 , 1  
RB_SelectChannel(0) : RB_Send  
End