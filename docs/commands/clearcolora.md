# ClearColorA

Action

Specify the clear value for the alpha channel.

Syntax

ClearColorA Alpha 

Remarks

Alpha | Alpha value used when the color buffer is cleared. The initial value is 0  
---|---  
  
Sets the alpha value applied to drawn elements - points, lines, and bitmaps. How the alpha value affects image pixels depends on [BlendFunc](blendfunc.md), the default behavior is a transparent blend.

See also

[ColorRGB](colorrgb.md), [BlendFunc](blendfunc.md)

Example

```vb
' Pseudocode

' Drawing three characters with transparency 255, 128, and 64

```
Begin_G BITMAPS

Vertex2II 50, 30, 31, &H47

Color_A 128

Vertex2II 58, 38, 31, &H47

Color_A 64 

Vertex2II 66, 46, 31, &H47

![clip0102](clip0102.png)