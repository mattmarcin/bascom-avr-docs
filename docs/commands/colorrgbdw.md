# ColorRGBdw

Action

Set the current color red, green and blue.

Syntax

ColorRGBdw rgb 

Remarks

rgb | Value in the range of 0 to &H00FFFFFF, Red is the most significant 8 bits and Blue is the least. So &Hff0000 is  bright Red.  
---|---  
  
Sets red, green and blue values of the FT800 color buffer which will be applied to the following draw operation.

Note: this is the same as [ColorRGB](colorrgb.md) except you can now parse the whole rgb values in a dword

See also

[Color_A](color_a.md) , [ColorRGB](colorrgb.md)