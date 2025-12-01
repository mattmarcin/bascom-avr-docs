# RB_SETTABLECOLOR

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