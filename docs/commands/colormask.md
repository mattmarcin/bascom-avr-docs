# ColorMask

Action

Enable or disable writing of color components.

Syntax

ColorMask r, g ,b ,a 

Remarks

r | Enable or disable the red channel update of the FT800 color buffer. The initial value is 1 and means enable  
---|---  
g | Enable or disable the green channel update of the FT800 color buffer. The initial value is 1 and means enable  
b | Enable or disable the blue channel update of the FT800 color buffer. The initial value is 1 and means enable  
a | Enable or disable the alpha channel update of the FT800 color buffer. The initial value is 1 and means enable  
  
The color mask controls whether the color values of a pixel are updated. Sometimes it is used to selectively update only the 

red, green, blue or alpha channels of the image. More often, it is used to completely disable color updates while updating the 

tag and stencil buffers.

See also

[TagMask](tagmask.md)

Example

```vb
' Pseudocode

'Draw a '8' digit in the middle of the screen. Then paint an invisible 40-pixel circular 

'touch area into the tag buffer

```
Begin_G BITMAPS

Vertex2II 68, 40, 31, &H38

PointSize 40 * 16

ColorMask 0, 0, 0, 0

Begin_G FTPOINTS

Tag &H38

Vertex2II 80, 60, 0, 0

![clip0079](clip0079.png)