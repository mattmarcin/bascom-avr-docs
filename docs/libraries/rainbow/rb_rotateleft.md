# RB_ROTATELEFT

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