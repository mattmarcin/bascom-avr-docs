# StencilFunc

Action

Set function and reference value for stencil testing.

Syntax

StencilFunc func, ref, mask

Remarks

func | Specifies the test function, one of NEVER, LESS, LEQUAL, GREATER, GEQUAL, EQUAL, NOTEQUAL, or ALWAYS. The initial value is ALWAYS.   
---|---  
ref | Specifies the reference value for the stencil test, range 0 to 255, the initial value is 0  
mask | Specifies a mask that is ANDed with the reference value and the stored stencil value, range 0 to 255 The initial value is 255  
  
Stencil test rejects or accepts pixels depending on the result of the test function defined in func parameter, which operates 

on the current value in the stencil buffer against the reference value.

See also

[StencilOp](stencilop.md), [StencilMask](stencilmask.md)

Example

```vb
' Pseudocode

' Draw two points, incrementing stencil at each pixel, then draw the pixels with value 2 in red

```
StencilOp INCR, INCR

PointSize 760

Begin_G FTPOINTS

Vertex2II 50, 60, 0, 0

Vertex2II 110, 60, 0, 0

StencilFunc EQUAL, 2, 255

ColorRGB 100, 0, 0

Vertex2II 80, 60, 0, 0

![clip0085](clip0085.png)