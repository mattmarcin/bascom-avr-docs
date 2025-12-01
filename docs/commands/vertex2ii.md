# Vertex2ii

Action

Start the operation of graphics primitive at the specified coordinates in pixel precision. 

Syntax

Vertex2ii x, y, handle, cell

Remarks

x | x-coordinate in pixels, from 0 to 511  
---|---  
y | y-coordinate in pixels, from 0 to 511  
handle | Bitmap handle. The valid range is from 0 to 31. From 16 to 31, the bitmap handle is dedicated to the FT800 built-in font.  
cell | Cell number. Cell number is the index of bitmap with same bitmap layout and format. For example, for handle 31, the cell 65 means the character "A" in the largest built in font.  
  
The Vertex2II command only allows positive screen coordinates.

If the bitmap is partially off screen, for example during a screen scroll, then it is necessary to 

specify negative screen coordinates (with Vertex2F).

The handle and cell parameters will be ignored unless the graphics primitive is specified as bitmap by command [Begin_G](begin_g.md), prior to this command.

See Also

[BEGIN_G](begin_g.md) , [END_G](end_g.md) , [VERTEX2F](vertex2f.md)

Example

Clear_B 1, 1, 1 ' Clear Screen

BitmapSource RAM_G

BitmapLayout BARGRAPH, 256, 1

BitmapSize NEAREST, Border, Border, 256, 256

Begin_G BITMAPS

ColorRGB 255, 0, 0

' Display bargraph At hoffset, voffset location

Vertex2II 0, 0, 0, 0

Vertex2II 256, 0, 0, 1

ColorRGB 0, 0, 0

Vertex2II 0, 4, 0, 0

Vertex2II 256, 4, 0, 1

UpdateScreen