# RB_SELECTCHANNEL

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