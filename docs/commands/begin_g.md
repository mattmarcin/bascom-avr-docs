# Begin_G

Action

Begin drawing a Graphics Primitive. 

Syntax

Begin_G prim 

Remarks

prim | BITMAPS FTPOINTS LINES LINE_STRIP EDGE_STRIP_R EDGE_STRIP_L EDGE_STRIP_A EDGE_STRIP_B RECTS |  Bitmap Drawing Primitive Point Drawing Primitive Line Drawing Primitive Line Strip Drawing Primitive Edge Strip Right side Drawing Primitive Edge Strip Left side Drawing Primitive Edge Strip Above Drawing Primitive Edge Strip Below Drawing Primitive Rectangle Drawing Primitive  
---|---|---  
  
All primitives supported by the FT800 are defined in the table above. The primitive 

to be drawn is selected by the [Begin_G](begin_g.md) command. Once the primitive is selected, it will be 

valid till the new primitive is selected by the [Begin_G](begin_g.md) command. 

Please Note: The primitive drawing operation will not be performed until [Vertex2ii](vertex2ii.md) or [Vertex2f](vertex2f.md) is executed.

See also

[END_G](end_g.md) , [VERTEX2F](vertex2f.md), [VERTEX2II](vertex2ii.md)

Example

' Pseudocode

Begin_G Lines  
Vertex2F (FT_DispWidth / 4) * 16, (FT_DispHeight - 25) / 2 * 16  
Vertex2F (FT_DispWidth / 4) * 16, (FT_DispHeight + 25) / 2 * 16  
ColorRGB 0, 128, 0  
LineWidth 10 * 16

Begin_G FTPoints  
Vertex2F 50,5,00  
Vertex2F 110,15,0,0

' Drawing points, lines and bitmap

Begin_G FTPOINTS

Vertex2II 50, 5, 0, 0

Vertex2II 110, 15, 0, 0

Begin_G LINES

Vertex2II 50, 45, 0, 0

Vertex2II 110, 55, 0, 0

Begin_G BITMAPS

Vertex2II 50, 65, 31,&H45

Vertex2II 110, 75, 31,&H46

![clip0087](clip0087.png)