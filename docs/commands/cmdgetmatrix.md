# CmdGetMatrix

Action

Retrieves the current matrix coefficients.

Syntax

CmdGetMatrix a, b ,c, d, e, f

Remarks

a | Output parameter; written with matrix coefficient a. See [BitmapTransform](bitmaptransform.md) for formatting.  
---|---  
b | Output parameter; written with matrix coefficient b. See [BitmapTransform](bitmaptransform.md) for formatting.  
c | Output parameter; written with matrix coefficient c. See [BitmapTransform](bitmaptransform.md) for formatting.  
d | Output parameter; written with matrix coefficient d. See [BitmapTransform](bitmaptransform.md) for formatting.  
e | Output parameter; written with matrix coefficient e. See [BitmapTransform](bitmaptransform.md) for formatting.  
f | Output parameter; written with matrix coefficient f. See [BitmapTransform](bitmaptransform.md) for formatting.  
  
To retrieve the current matrix within the context of co-processor engine. Please note the matrix within the context of co-processor engine will not apply to the bitmap transformation until it is passed to graphics engine through [CmdGetMatrix](cmdgetmatrix.md).

Example