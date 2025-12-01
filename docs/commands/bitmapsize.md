# BitmapSize

Action

Specify the Screen Drawing Bitmap Size (for the current Bitmap Handle)

Syntax

BitmapSize Filter, Wrapx , Wrapx ,Width, Height 

Remarks

Filter | Bitmap Filtering Mode, NEAREST or BILINEAR  
---|---  
Wrapx | Bitmap x wrap mode, REPEAT or BORDER  
Wrapx | Bitmap y wrap mode, REPEAT or BORDER  
Width | Drawn bitmap Width, in Pixels  
Height | Drawn bitmap Height, in Pixels  
  
This command controls the drawing of bitmaps: the on-screen size of the bitmap, the behavior for wrapping, and

the filtering function. Please note that if Wrapx or Wrapy is using REPEAT then the corresponding memory layout dimension

([BitmapLayout](bitmaplayout.md) linestride or height) must be power of two, otherwise the result is undefined.

See also

[BitmapHandle](bitmaphandle.md), [BitmapLayout](bitmaplayout.md), [BitmapSource](bitmapsource.md)

Example

```vb
' Pseudocode

' Drawing a 64 x 64 bitmap

```
BitmapSource 0

BitmapLayout RGB565, 128, 64

BitmapSIZE NEAREST, BORDER, BORDER, 64, 64

Begin_G BITMAPS

Veterx2II 48, 28, 0, 0

![clip0090](clip0090.png)

'Reducing the size to 32 x 50

BitmapSource 0

BitmapLayout RGB565, 128, 64

BitmapSize NEAREST, BORDER, BORDER, 32, 50

Begin_G BITMAPS

Vertex2II 48, 28, 0, 0

![clip0091](clip0091.png)

' Using the REPEAT wrap mode to tile the bitmap

BitmapSource 0

BitmapLayout RGB565, 128, 64

BitmapSize NEAREST, REPEAT, REPEAT, 160, 120

Begin_G BITMAPS

Vertex2II 0, 0, 0, 0

![clip0092](clip0092.png)

' 4X zoom - 128 X 128 - using a bitmap transform

BitmapSource 0

BitmapLayout RGB565, 128, 64

BitmapTransformA 128

BitmapTransformE 128

BitmapSize NEAREST, BORDER,BORDER, 128, 128

Begin_G BITMAPS

Vertex2II 16, 0, 0, 0

![clip0093](clip0093.png)