# RB_CHANGEPIN

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