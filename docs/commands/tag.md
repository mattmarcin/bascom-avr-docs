# Tag

Action

Attach the tag value for the following graphics objects drawn on the screen.

Syntax

Tag s

Remarks

s | Tag value. Valid value range is from 1 to 255  
---|---  
  
The initial value of the tag buffer of the FT800 is specified by command [ClearTag](cleartag.md) and taken effect by command [Clear_B](clear_b.md). 

Tag command can specify the value of the tag buffer of the FT800 that applies to the graphics objects when they are drawn

on the screen. This Tag value will be assigned to all the following objects, unless the [TagMask](tagmask.md) command is used to disable it.

Once the following graphics objects are drawn, they are attached with the tag value successfully. 

When the graphics objects attached with the tag value are touched, the register REG_TOUCH_TAG will be updated 

with the tag value of the graphics object being touched.

If there is no Tag commands in one display list, all the graphics objects rendered by the display list will report tag value as 255

in REG_TOUCH_TAG when they were touched.

See also

[ClearTag](cleartag.md), [TagMask](tagmask.md)