# Rainbow Libraries

> WS2812 RGB LED control

## RAINBOWBSC

This lib is based on the rainbow 1.2 lib from Galahat. See also : <http://bascom-forum.de/mediawiki/index.php/Rainbow_Lib>

The rainbowbsc.lib is essentially the same lib providing the same functionality. Some code is moved to CONFIG RAINBOW, and the routines are renamed in order to to give conflicts with existing/future statements/functions.

See [CONFIG RAINBOW](config_rainbow.md)

---

## RB_ADDCOLOR

Action

Adds specified color info to the specified LED in memory

Syntax

RB_ADDCOLOR Led , Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
Led | The index of the LED number. First LED is 0.   
  
The operation is performed on the memory. When the R, G or B exceeds 255, the value is limited to 255. You need to use RB_SEND so that the LED reflects the new color information.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_ANDCOLOR

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

---

## RB_CHANGEPIN

Action

Changes the defined output pin at run time

Syntax

RB_CHANGEPIN Port , Pin

Remarks

Port | A numeric variable or constant with the I/O address of the port. Notice that this is an absolute memory address. For ports in the normal IO range, you need to add a value of &H20 to the address. Example : Const nprt=varptr(portb) + &H20 Rb_ChangePIN nprt, 1  
---|---  
Led | A numeric variable or constant with the pin number in the range from 0-7  
  
When you want to use multiple stripes with the same color, it would require CONFIG RAINBOW to set up all these stripes.

But each configured pin will use memory for the RGB information. When you change the pin at run time, you will use the color information of one stripe. 

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Demo.bas  
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
Dim n as Byte, state as Byte, tel as Byte  
```
state=0 : tel=0  
  
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
'waitms 500 'wait a bit  
select case state  
case 0 : r=r+5 : Rb_AddColor 0, color(1) : rb_send: tel=tel+1  
case 1: g=g+5 : Rb_subColor 0, color(1) : rb_send:tel=tel+1  
case 2: b=b+5 : Rb_orColor 0, color(1) : rb_send: tel=tel+1  
case 3: Rb_ClearStripe : tel=4  
case 4: rb_send : tel=5  
case 5: Rb_Fill color(1) : tel=5  
case 6: const nprt=varptr(portb) + &H20 : Rb_ChangePIN nprt, 1  
case else  
```
state=0  
```vb
end select  
if tel>=2 then  
```
state=state+1 : tel=0  
```vb
end if  
Loop  


```

---

## RB_CLEARCOLORS

Action

Clears all color info in memory of the active channel

Syntax

RB_CLEARCOLORS

Remarks

All color info of the active channel is cleared. The LEDS keep their color until an RB_SEND is used.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## RB_COLOR

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

---

## RB_COPY

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

---

## RB_FILL

Action

Fills the memory of the active channel with a color and updates the LED's.

Syntax

RB_FILL Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
  
All LED's of the active channel will be set to the specified color in memory. This statement will also update the LED's so it is not needed to use RB_SEND.

This statement is similar to RB_CLEARCOLORS except that you can provide a color and that it is not required to use RB_SEND

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

.

---

## RB_FILLCOLORS

Action

Fills the entire memory of the active channel with a specified color

Syntax

RB_FILLCOLORS Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
  
The entire memory of the active channel is filled with the specified color. 

This statement will not update the LED's. This means that you need to use RB_SEND to update the LED's. Or use RB_FILL which will update the LED's as well.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Levelmeter.bas  
'  
' This example demonstrate the switching between two Rainbow-Stripes while simulating  
' a simple kind of an stereo levelmeter and the use of some RB_statements.  
'  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal=8000000  
$hwstack=40  
$swstack=16  
$framesize=32  
  
  
Config RAINBOW= 2, RB0_LEN=8, RB0_PORT=PORTB,rb0_pin=0 , RB1_LEN=8, RB1_PORT=PORTB,rb1_pin=1  
Dim n as Byte  
Dim Color as DWord  
Dim CH as Byte  
Dim LEFT_Level as Byte , Left_Level_OLD as Byte  
Dim Right_Level as Byte , Right_Level_OLD as Byte  
```
Const Channels = 2  
Const Backcolor = &H000005  
  
'----[MAIN]---------------------------------------------------------------------  
Color = Backcolor  
For ch = 0 to Channels -1  
Rb_SelectChannel Ch  
RB_Fillcolors Color  
Rb_SetTableColor 0,0  
RB_send  
```vb
Next  
Do  
```
incr n: n = n and &H30 'n counts from 0 to 63  
```vb
If n = 0 then Gosub Get_Level 'Read signal  
'Switch channel  
toggle Ch  
```
Rb_SelectChannel Ch  
```vb
Waitms 40  
If ch = 0 then 'Channel 0  
If left_level_old < left_level then  
```
incr Left_level_old  
ElseIf Left_level_old > Left_level then  
Decr Left_level_old  
End if  
RB_Fillcolors Color  
Rb_SetTableColor Left_level_old ,0  
```vb
Else 'Channel 1  
If right_level_old < right_level then  
```
incr right_level_old  
ElseIf right_level_old > right_level then  
Decr right_level_old  
End if  
RB_Fillcolors Color  
Rb_SetTableColor right_level_old ,0  
end if  
RB_Send  
Loop  
  
Get_Level:  
Left_Level = rnd(7)  
Right_Level = rnd(7)  
Return  
  
Rainbow_Colors:  
Data 100,50,0 'orange

---

## RB_GETCOLOR

Action

Returns the RGB color information of a LED of the active channel.

Syntax

Color =  RB_GETCOLOR( LED )

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
LED | The index of the LED number. First LED is 0.   
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## RB_LOOKUPCOLOR

Action

Returns the RGB color information from a data table using an index.

Syntax

Color = RB_LOOKUPCOLOR(  Index [, Label] )

Remarks

Index | A byte variable or constant that holds the index of the table. The table need to be identified by a label. This is either a user defined label, or a label named RAINBOW_COLORS The table has the R, G, B format. Example: Rainbow_Colors: ' R , G , B index Data &HFF , &H00 , &H00 'Red 0 Data &H00 , &HFF , &H00 'Green 1 Data &H00 , &H00 , &HFF 'Blue 2 Data &HFF , &HA5 , &H00 'Orange 3 Data &HFF , &HFF , &H00 'Yellow 4 Data &HFF , &H69 , &HB4 'HotPink 5  
---|---  
Label | The label name of the table. This is an optional value. If the label name is not specified, the name RAINBOW_COLORS will be used.  
  
RB_LOOKUP is a help function. It does not work on the memory or LED's. I just returns a color from a data table using a lookup value.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## RB_ORCOLOR

Action

Ors specified color info to the specified LED in memory

Syntax

RB_ORCOLOR Led , Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
Led | The index of the LED number. First LED is 0.   
  
The operation is performed on the memory. An OR operation can set part of a color. You need to use RB_SEND so that the LED reflects the new color information.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_ANDCOLOR](rb_andcolor.md)

---

## RB_ROTATELEFT

Action

Rotate all LED's of the active channel to the left

Syntax

RB_ROTATELEFT Index , Width

Remarks

Index | A numeric variable or constant that specifies at which position the rotation should start. The first LED has index value 0.  
---|---  
Width | The number of LED's that ROTATE, starting at Index. Width should at least be 1.  
  
This statement will rotate the memory to the left by one position. Width specifies how many LED's , index inclusive, will take part in the rotation.

Imagine 4 chairs with people on it. When they all stand up and go one place to the left, the person most left will have no chair to sit on. He will take the free chair on the right.

There is also a similar operation named SHIFT. When you SHIFT, information is lost : the person that has no chair on his left will leave the room and there will be 1 empty chair.

Since you can specify both the index and the width, rotation is very flexible : you can rotate all leds, or just a part of them.

The table below demonstrates a number of operation on a LED stipe of 4 LED's. 

LED0 | LED1 | LED2 | LED3 | OPERATION/RESULT  
---|---|---|---|---  

| ![led_green](led_green.png) | OPERATION : RB_ROTATELEFT 0,4  
|   
| ![led_green](led_green.png) |   
| RESULT  
  
![led_green](led_green.png) | ![led_green](led_green.png) |   
|   
| OPERATION : RB_ROTATELEFT 0,2  
![led_green](led_green.png) | ![led_green](led_green.png) |   
|   
| RESULT  
![led_green](led_green.png) |   

| OPERATION : RB_ROTATELEFT 0,4  
  
|   
|  | ![led_green](led_green.png) | RESULT  
  
|   
| ![led_green](led_green.png) |   
| OPERATION : RB_ROTATELEFT 1,2  
  
| ![led_green](led_green.png) |   
|   
| RESULT  
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## RB_ROTATERIGHT

Action

Rotate all LED's of the active channel to the right

Syntax

RB_ROTATERIGHT Index , Width

Remarks

Index | A numeric variable or constant that specifies at which position the rotation should start.  
---|---  
Width | The number of LED's that ROTATE, starting at Index. Width should at least be 1.  
  
This statement will rotate the memory to the right by one place. Width specifies how many LED's , index inclusive, will take part in the rotation.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## RB_SELECTCHANNEL

Action

Selects the active channel.

Syntax

RB_SELECTCHANNEL channel

Remarks

channel | A numeric variable or constant that specifies the active channel. The range is from 0-7  
---|---  
  
This statement will set the active channel and initializes the output pin. The channel is a numeric variable in the range from 0-7.

All rainbow commands will work on the active channel. This means that you need to use RB_SelectChannel at least once. 

You should not specify undefined channels. Channels are defined with [CONFIG RAINBOW](config_rainbow.md)

It is NOT required to use RB_SELECTCHANNEL when the channel remains the same. So use it once and only when the channel changes.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_SEND

Action

Transmits the channel data to the defined port pin.

Syntax

RB_SEND

Remarks

The WS2812 will latch the received information. You only need to use RB_SEND when you want to send new color information.

Some statements and functions will call RB_SEND internally. 

The following table shows which statements update the LED at once

STATEMENT | UPDATE LED  
---|---  
[RB_ADDCOLOR](rb_addcolor.md) |  \-   
[RB_ANDCOLOR](rb_andcolor.md) |  \-   
[RB_ORCOLOR](rb_orcolor.md) |  \-   
[RB_SUBCOLOR](rb_subcolor.md) |  -  
[RB_CLEARSTRIPE](rb_clearstripe.md) |  YES  
[RB_CLEARCOLORS](rb_clearcolors.md) |  \-   
[RB_FILL](rb_fill.md) |  YES  
[RB_FILLCOLORS](rb_fillcolors.md) |  -  
[RB_FILLSTRIPE](rb_fillstripe.md) |  YES  
[RB_SELECTCHANNEL](rb_selectchannel.md) |  -  
[RB_SEND](rb_send.md) |  YES  
[RB_SETCOLOR](rb_setcolor.md) |  -  
[RB_SWAPCOLOR](rb_swapcolor.md) |  \-   
[RB_ROTATELEFT](rb_rotateleft.md) |  -  
[RB_ROTATERIGHT](rb_rotateright.md) |  -  
[RB_SHIFTLEFT](rb_shiftleft.md) |  -  
[RB_SHIFTRIGHT](rb_shiftright.md) |  -  
[RB_CHANGEPIN](rb_changepin.md) | -  
[RB_SETTABLECOLOR](rb_settablecolor.md) |  -  
[RB_GETCOLOR](rb_getcolor.md) |  -  
[RB_LOOKUPCOLOR](rb_lookupcolor.md) |  -  
[RB_COPY](rb_copy.md) | -  
[RB_COLOR](rb_copy.md) | -  
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_SETCOLOR

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

---

## RB_SETTABLECOLOR

Action

Set the color of a LED using a lookup table.

Syntax

RB_SETTABLECOLOR LED , Index [, Label]

Remarks

LED | The index of the LED of the active channel which color need to be changed. The first LED number is 0.  
---|---  
Index | A byte variable or constant that holds the index of the table. The table need to be identified by a label. This is either a user defined label, or a label named RAINBOW_COLORS The table has the R, G, B format. Example: Rainbow_Colors: ' R , G , B index Data &HFF , &H00 , &H00 'Red 0 Data &H00 , &HFF , &H00 'Green 1 Data &H00 , &H00 , &HFF 'Blue 2 Data &HFF , &HA5 , &H00 'Orange 3 Data &HFF , &HFF , &H00 'Yellow 4 Data &HFF , &H69 , &HB4 'HotPink 5  
Label | The label name of the table. This is an optional value. If the label name is not specified, the name RAINBOW_COLORS will be used.  
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Trafficlights.bas  
'  
' This example simulates two simple Trafficlights.  
' It shows how switch between two Stripes with just one defined Rainbow.  
' The active output gets changed by the RB_ChangePin statement.  
' Thus the use of memory is small.  
'  
'-------------------------------------------------------------------------------  
'(  
```
Following situation:  
The one way route from the Weststreet to Nothstreet and vice versa is the main route  
and cars on these roads have priority.The corresponding light will show green light normally.  
In our simple world, every five seconds a car wants to drive from the Eaststreet to the Northstreet.  
Thus, the trafficflow from the main street has to stop, to let the cars pass.  
```vb
' Northstreet  
'  
' | |  
' | |  
' | | ooo  
' ------' '------  
' EastStreet  
' ---> \------  
```
WestStreet |  
```vb
' -----------/  
' ooo  
'  
'  
')  
$Regfile = "m88pdef.dat"  
$Crystal=8000000  
$hwstack=40  
$swstack=16  
$framesize=32  
'We use just one Channel for both Trafficlights, cause LED stripes are static  
Config RAINBOW= 1, RB0_LEN=3, RB0_PORT=PORTB,rb0_pin=0  
```
Rb_SelectChannel 0 'we use the defined Channel  
  
'Port+Pin combinations, formed to a word  
Const MainStreet_0 = (((varptr(portb) + &H20) *256) OR PB0)  
Const EastStreet_1 = (((varptr(portb) + &H20) *256) OR PB1)  
```vb
'----[MAIN]---------------------------------------------------------------------  
Dim PortPin as Word  
Dim Street as Byte 'selects the current PortPin cofiguration  
```
Const Mainstreet = 0  
Const Eaststreet = 1  
'Index for LED and colors also  
Const Red = 0  
Const Yellow = 1  
Const Green = 2  
```vb
Gosub inital_state  
Do  
Gosub Wait_for_car  
'Trafficlight turns to Red  
```
Street = Mainstreet  
```vb
Gosub Turn_to_Red  
'Trafficlight turns to green  
```
Street = Eaststreet  
```vb
Gosub Turn_to_green  
Gosub Wait_for_car 'let some cars passing  
Gosub Turn_to_red  
'Mainstreet becomes green  
```
Street = Mainstreet  
```vb
Gosub Turn_to_green  
Loop  
  
```
Wait_for_car:  
```vb
Wait 5  
Return  
  
```
Turn_to_Green:  
Gosub Change_Port_Pin  
RB_SettableColor Yellow,Yellow,Light 'load and set color from table  
RB_Send 'refresh stripe  
Wait 1  
RB_clearcolors 'clear colors in memory  
RB_SettableColor green,green,Light 'load and set color from table  
RB_Send 'refresh stripe  
```vb
Wait 2  
Return  
  
```
Turn_to_red:  
Gosub Change_Port_Pin  
RB_clearcolors 'clear colors in memory  
RB_SettableColor Yellow,Yellow,Light 'load and set color from table  
RB_Send 'refresh stripe  
Wait 3  
RB_clearcolors 'clear colors in memory  
RB_SettableColor red,red,Light 'load and set color from table  
RB_Send 'refresh stripe  
```vb
Wait 2  
Return  
  
```
Inital_State:  
'select Mainstreet, green  
Street = Mainstreet  
Gosub Change_Port_Pin  
RB_clearcolors  
RB_SettableColor green,green,Light  
RB_Send  
'select Eaststreet, red  
Street = Eaststreet  
Gosub Change_Port_Pin  
RB_clearcolors  
RB_SettableColor Red,Red,Light  
RB_Send  
Return  
  
Change_PORT_PIN:  
PortPin = Lookup(Street,PortPin_Tbl) 'get PortPin comination  
RB_ChangePin High(PortPin),PortPin 'use PortPin  
Return  
  
PortPin_Tbl:  
Data MainStreet_0%  
Data EastStreet_1%  
  
Light:  
Data 150,0,0 'Red  
Data 100,50,0 'Yello  
Data 0,150,0 'Green

---

## RB_SHIFTLEFT

Action

Shift all LED's of the active channel to the left

Syntax

RB_SHIFTLEFT Index , Width

Remarks

Index | A numeric variable or constant that specifies at which position the shift should start.  
---|---  
Width | The number of LED's that SHIFT, starting at Index. Width should at least be 1.  
  
This statement will shift the memory to the left by one position. Width specifies how many LED's , index inclusive, will take part in the shift operation.

When you shift information to the LEFT, the RIGHT-most LED will loose it's color information since it had no LED with data at the right.

Imagine 4 chairs with people on it. When they all stand up and go one place to the left, the person most left will have no chair to sit on. The chair on the right will be empty.

The table below demonstrates a number of operation on a LED stipe of 4 LED's. 

LED0 | LED1 | LED2 | LED3 | OPERATION/RESULT  
---|---|---|---|---  

| ![led_green](led_green.png) | OPERATION : RB_SHIFTLEFT 0,4  
|   
| ![led_green](led_green.png) |   
| RESULT  
![led_green](led_green.png) |   

| OPERATION : RB_SHIFTLEFT 0,2  

| RESULT  
  
|   
| ![led_green](led_green.png) | ![led_green](led_green.png) | OPERATION : RB_SHIFTLEFT 0,4  
  
| ![led_green](led_green.png) | ![led_green](led_green.png) |   
| RESULT  
![led_green](led_green.png) | ![led_green](led_green.png) | ![led_green](led_green.png) | ![led_green](led_green.png) | OPERATION : RB_SHIFTLEFT 1,2  
![led_green](led_green.png) | ![led_green](led_green.png) |   
| ![led_green](led_green.png) |   
  
  
See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_SHIFTRIGHT

Action

Shift all LED's of the active channel to the right

Syntax

RB_SHIFTRIGHT Index , Width

Remarks

Index | A numeric variable or constant that specifies at which position the shift should start.  
---|---  
Width | The number of LED's that SHIFT, starting at Index. Width should at least be 1.  
  
This statement will shift the memory to the right by one position. Width specifies how many LED's , index inclusive, will take part in the shift operation

When you shift information to the RIGHT, the LEFT-most LED will loose it's color information.

Imagine 4 chairs with people on it. When they all stand up and go one place to the right, the person most right will have no chair to sit on. The chair on the left will become empty.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_SUBCOLOR

Action

Subtracts specified color info to the specified LED in memory

Syntax

RB_SUBCOLOR Led , Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
Led | The index of the LED number. First LED is 0.   
  
The operation is performed on the memory. When the R, G or B go below 0, the value is limited to 0. You need to use RB_SEND so that the LED reflects the new color information.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_SWAPCOLOR

Action

Exchange color between to LED's of the active channel. This statement will only change the memory.

Syntax

RB_SWAPCOLOR Led1 , Led2

Remarks

Led1 , Led2 | The index of the LED of the active channel.  
---|---  
  
This statement will swap the color info of the specified LED's.

So after the execution of the statement, LED1 becomes the color of LED2 and LED2 becomes the color of LED1.

This statement operates on the memory, it will not update the LED's.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---
