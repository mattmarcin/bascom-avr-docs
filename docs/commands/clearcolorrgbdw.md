# ClearColorRGBdw

Action

Specify the clear values for Red, Green and Blue channels.

Syntax

ClearColorRGBdw RGB 

Remarks

RGB | Value in the range of 0 to &H00FFFFFF, Red is the most significant 8 bits and Blue is the least. So &Hff0000 is  bright Red.  
---|---  
  
Sets the color values used by a following [Clear_B](clear_b.md)

The following colors are defined by constants.

Color | Value  
---|---  
Black | &H000000  
White | &HFFFFFF  
Red | &HFF0000  
Lime | &H00FF00  
Blue | &H0000FF  
Yellow | &HFFFF00  
Cyan | &H00FFFF  
Magenta | &HFF00FF  
Silver | &HC0C0C0  
Grey | &H808080  
Maroon | &H800000  
Olive | &H808000  
Green | &H008000  
Purple | &H800080  
Teal | &H008080  
Navy | &H000080  
Brown | &H703800  
Orange | &H00A5FF  
  
See also

[ClearColorA](clearcolora.md), [Clear_B](clear_b.md) , [ClearColorRGB](clearcolorrgb.md)

Example

```vb
' Pseudocode

' To clear the screen to bright blue:

```
ClearColorRGBdw &H0000FF

Clear_B 1, 1, 1