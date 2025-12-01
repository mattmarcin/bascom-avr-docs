# BitmapLayout

Action

Specify the source bitmap memory format and layout for the current handle.

Syntax

BitmapLayout format, linestride, height

Remarks

format | Bitmap Pixel Formats. ARGB1555 FT_L1 FT_L4 FT_L8 RGB332 ARGB2 ARGB4 RGB565 PALETTED TEXT8x8 TEXTVGA BARGRAPGH  
---|---  
linestride | Bitmap linestride, in bytes. Please note the alignment requirement which is described below.  
height | Bitmap height, in lines  
  
The bitmap formats supported are FT_L1, FT_L4, FT_L8, RGB332, ARGB2, ARGB4, ARGB1555, RGB565 and PALETTED. 

```vb
For FT_L1 format the linestride must be a multiple of 8 bits.

For FT_L4 format the linestride must be multiple of 2 nibbles (Aligned to byte).

For more details about alignment, please refer to the FT800 Series Programmer Guide.PDF from FTDI.

```
See also

[BitmapHandle](bitmaphandle.md), [BitmapSize](bitmapsize.md), [BitmapSource](bitmapsource.md)

Example

![clip0088](clip0088.png)![clip0089](clip0089.png)