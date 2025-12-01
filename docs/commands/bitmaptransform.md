# BitmapTransform

Action

Specify the A-F coefficient of the Bitmap Transform Matrix.

Syntax

BitmapTransform CoefValue , CoefName

Remarks

CoefValue | Coefficient value of the Bitmap Transform Matrix in signed 8.8 bit fixed-point form. The initial value is 256.  
---|---  
CoefName | Coeeficient name. There are coefficient A-F. You need to specify a capital letter A,B,C,D,E or F.  
  
BitmapTransform A-F coefficients are used to perform bitmap transform functionalities such as scaling, rotation and translation.

Example

```vb
' Pseudocode

' A value of 0.5 (128) causes the bitmap appear double width:

```
BitmapSource 0

BitmapLayout RGB565, 128,64

BitmapTransform 128, A

BitmapSize Nearest, Border, Border

Begin_G Bitmaps

Vertex2II 16,0,0,0

![clip0112](clip0112.png)

```vb
' Pseudocode

' A value of 2.0 (512) gives a half-width bitmap:

```
BitmapSource 0

BitmapLayout RGB565, 128,64

BitmapTransform 512, A

BitmapSize Nearest, Border, Border

Begin_G Bitmaps

Vertex2II 16,0,0,0

![clip0113](clip0113.png)