# RB_FILL

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