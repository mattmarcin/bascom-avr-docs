# RB_SHIFTLEFT

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