# ColorRGB

Action

Set the current color red, green and blue.

Syntax

ColorRGB red, green ,blue 

Remarks

red | Red value for the current color. 0 to 255 , initial value is 255  
---|---  
green | green value for the current color. 0 to 255 , initial value is 255  
blue | blue value for the current color. 0 to 255 , initial value is 255  
  
Sets red, green and blue values of the FT800 color buffer which will be applied to the following draw operation.

See also

[Color_A](color_a.md) , [ColorRGBdw](colorrgbdw.md)

Example

```vb
' Pseudocode

' Drawing three characters with different colors

```
Begin_G BITMAPS

Vertex2II 50, 38, 31, &H47

ColorRGB 255, 100, 50 

Vertex2II 80, 38, 31, &H47

ColorRGB 50, 100, 255 

Vertex2II 110, 38, 31,&H47

![clip0080](clip0080.png)