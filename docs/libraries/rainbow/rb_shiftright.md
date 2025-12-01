# RB_SHIFTRIGHT

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