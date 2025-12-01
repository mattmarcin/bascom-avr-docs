# BlendFunc

Action

Specify pixel arithmetic. 

Syntax

BlendFunc src, dst 

Remarks

src | Specifies how the source blending factor is computed. One of ZERO, ONE, SRC_ALPHA, DST_ALPHA,ONE_MINUS_SRC_ALPHA or ONE_MINUS_DST_ALPHA.  
---|---  
dst | Specifies how the destination blending factor is computed, One of ZERO, ONE, SRC_ALPHA, DST_ALPHA,ONE_MINUS_SRC_ALPHA or ONE_MINUS_DST_ALPHA.  
  
The blend function controls how new color values are combined with the values already in the color buffer.

Given a pixel value source and a previous value in the color buffer destination, the computed color is:

source Ã src + destination Ã dst

```vb
for each color channel: red, green, blue and alpha.

For more details please refer to the FT800 Series Programmer Guide.PDF from FTDI.

```
See also

[Color_A](color_a.md)

Example

```vb
' Pseudocode

' The default blend function of (SRC_ALPHA, ONE_MINUS_SRC_ALPHA) causes drawing 

' to overlay the destination using the alpha value

```
Begin_G BITMAPS

Vertex2II 50, 30, 31, &H47

Color_A 128 

Vertex2II 60, 40, 31, &H47

![clip0096](clip0096.png)

' A destination factor of zero means that destination pixels are not used

Begin_G BITMAPS

BlendFunc SRC_ALPHA, ZERO

Vertex2II 50, 30, 31, &H47

Color_A 128 

Vertex2II 60, 40, 31, &H47

![clip0097](clip0097.png)

' Using the source alpha to control how much of the destination to keep

Begin_G BITMAPS

BlendFunc ZERO, SRC_ALPHA

Vertex2II 60, 40, 31, &H47

![clip0098](clip0098.png)