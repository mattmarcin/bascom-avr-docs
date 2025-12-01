# Vertex2f

Action

Start the operation of graphics primitives at the specified screen coordinate, in 1/16th pixel precision.

Syntax

Vertex2f x, y

Remarks

x | x-coordinate in 1/16 pixel precision (Integer)  
---|---  
y | y-coordinate in 1/16 pixel precision (Integer)  
  
The range of coordinates can be from -16384 to +16383 in terms of 1/16 th pixel units. 

The Vertex2F command allows negative coordinates. It also allows fractional coordinates, because it specifies screen (x,y) in 

units of 1/16 of a pixel.

Please note the negative x coordinate value means the coordinate in the left virtual screen from (0, 0), while the negative y coordinate value means the coordinate in the upper virtual screen from (0, 0). If drawing on the negative coordinate position, the drawing operation will not be visible

See also

[BEGIN_G](begin_g.md) , [END_G](end_g.md) , [VERTEX2II](vertex2ii.md)

Example

ClearColorRGB 5, 45, 10

ColorRGB 255, 168, 64

Clear_B 1 ,1 ,1

Begin_G EDGE_STRIP_R

Vertex2F 16 * 16, 16 * 16

Vertex2F (FT_DispWidth * 2 / 3) * 16, (FT_DispHeight * 2 / 3) * 16

Vertex2F (FT_DispWidth - 80) * 16, (FT_DispHeight - 20) * 16

UpdateScreen