# BitmapSource

Action

Specify the source address of bitmap data in FT800 graphics memory RAM_G

Syntax

BitmapSource Addr

Remarks

Addr | Bitmap address in graphics FT800 SRAM, aligned with respect to the bitmap format. For example, if the bitmap format is RGB565/ARGB4/ARGB1555, the bitmap source shall be aligned to 2 bytes.  
---|---  
  
The bitmap source address is normally the address in main memory where the bitmap graphic data is loaded.

See also

[BitmapSize](bitmapsize.md), [BitmapLayout](bitmaplayout.md)

Example

' Drawing a 64 x 64 bitmap, loaded at address 0

BitmapSource 0

BitmapLayout RGB565, 128, 64

BitmapSize NEAREST, BORDER, BORDER, 64, 64

Begin_G BITMAPS

Veterx2II 48, 28, 0, 0

![clip0094](clip0094.png)

Using the same graphics data, but with source and size changed to show only a 32 x 32 detail

BitmapSource 128 * 16 + 32

BitmapLayout RGB565, 128, 64

BitmapSize NEAREST, BORDER, BORDER, 32, 32

Begin_G BITMAPS

Vertex2II 48, 28, 0, 0

![clip0095](clip0095.png)