# RGB8TO16

Action

This function converts an RGB8 byte value into an RGB16 word value.

Syntax

var = RGB8TO16(bOld)

Remarks

var | The word value that is assigned with the RGB16 value of bOld.  
---|---  
bOld | The byte that contains the RGB8 value.  
  
There are many different graphical LCD displays and most new displays can display in color. There are 8 bit and 16 bit displays. And beside the data bus width displays have different color resolution.

While high resolution is nice, it also means you need more data to display a pixel. The RGB8TO16() function converts an 8 bit RGB value into a 16 bit RGB value. This way you can use the bascom created BGC files. 

See also

NONE

Example

NONE