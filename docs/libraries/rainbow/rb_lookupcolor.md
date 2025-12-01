# RB_LOOKUPCOLOR

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