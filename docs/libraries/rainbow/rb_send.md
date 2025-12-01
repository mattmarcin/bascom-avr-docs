# RB_SEND

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