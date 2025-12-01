# Clear_B

Action

Clear buffers to preset values.

(This is similar to CLS)

Syntax

Clear_B C,S,T 

Remarks

C | Clear Color buffer. Setting this bit to 1 will clear the color buffer of the FT800 to the preset value.  Setting this bit to 0 will maintain the color buffer of the FT800 with an unchanged value.  The preset value is defined in command [ClearColorRGB](clearcolorrgb.md) for the RGB channel and [ClearColorA](clearcolora.md) for the alpha channel.  
---|---  
S | Clear Stencil buffer. Setting this bit to 1 will clear the stencil buffer of the FT800 to the preset value. Setting this bit to 0 will maintain the stencil buffer of the FT800 with an unchanged value. The preset value is defined in command [ClearStencil](clearstencil.md).  
T | Clear Tag buffer. Setting this bit to 1 will clear the tag buffer of the FT800 to the preset value. Setting this bit to 0 will maintain the tag buffer of the FT800 with an unchanged value. The preset value is defined in command [ClearTag](cleartag.md).  
  
The scissor test and the buffer write masks affect the operation of the clear. Scissor limits the cleared rectangle, and the buffer write masks limit the affected buffers.

The state of the alpha function, blend function, and stenciling do not affect the clear.

See also

[ClearColorA](clearcolora.md), [ClearStencil](clearstencil.md), [ClearTag](cleartag.md), [ClearColorRGB](clearcolorrgb.md)

Example

```vb
' Pseudocode

' To Clear the LCD to bright blue:

```
ClearColorRGB 0, 0, 255

Clear_B 1, 0, 0

![clip0099](clip0099.png)

```vb
' Pseudocode

' To clear part of the screen to gray, part to blue using scissor rectangles:

```
ClearColorRGB 100, 100, 100

Clear_B 1, 1, 1

ClearColorRGB 0, 0, 255

ScissorScize 30, 120

Clear_B 1, 1, 1

![clip0100](clip0100.png)