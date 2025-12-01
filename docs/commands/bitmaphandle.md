# BitmapHandle

Action

Specify the Bitmap Handle

Syntax

BitmapHandle handle 

Remarks

handle |  Bitmap Handle. The initial value is 0. Valid range values 0 to 31.  
---|---  
  
Handles 16 to 31 are defined by the FT800 for built-in font.

Handle 15 is defined in the co-processor engine commands [CmdGradient](cmdgradient.md), [CmdButton](cmdbutton.md), and [CmdKeys](cmdkeys.md). 

Users can define new bitmaps using handles from 0 to 14.

If there is no co-processor engine command [CmdGradient](cmdgradient.md), [CmdButton](cmdbutton.md) and [CmdKeys](cmdkeys.md) in the current display list, users

can even define a bitmap using handle 15. 

Graphics Context

The value of handle is part of the graphics context, as described in section 4.1 in FT800 Series Programmer Guide.PDF from FTDI.

See also

[BitmapLayout](bitmaplayout.md), [BitmapSize](bitmapsize.md)