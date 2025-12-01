# TagMask

Action

Control the writing of the tag buffer.

Syntax

TagMask mask

Remarks

mask | Allow updates to the tag buffer. The initial value is one (1) and it means the tag buffer of the FT800 is updated with the value given by the [Tag](tag.md) command.  Therefore, the following graphics objects will be attached to the tag value given by the TAG command. The value zero (0) means the tag buffer of the FT800 is set as the default value, rather than the value given by [Tag](tag.md) command in the display list.  
---|---  
  
Every graphics object drawn on screen is attached with the tag value which is defined in the FT800 tag buffer. 

The FT800 tag buffer can be updated by [Tag](tag.md) command.

The default value of the FT800 tag buffer is determined by [ClearTag](cleartag.md) and [Clear_B](clear_b.md) commands. 

If there is no [ClearTag](cleartag.md) command present in the Display List, the default value in tag buffer shall be 0.

[TagMask](tagmask.md) command decides whether the FT800 tag buffer takes the value from the default value of the FT800 tag buffer or

the [Tag](tag.md) command of the Display List.

See also

[Tag](tag.md), [ClearTag](cleartag.md), [StencilMask](stencilmask.md), [ColorMask](colormask.md)