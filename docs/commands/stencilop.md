# StencilOp

Action

Set stencil test actions.

Syntax

StencilOp sfail, spass

Remarks

sfail | Specifies the action to take when the stencil test fails, one of KEEP, ZERO, REPLACE, INCR, DECR and INVERT. The initial value is KEEP  
---|---  
spass | Specifies the action to take when the stencil test passes, one of the same constants as sfail.  The initial value is KEEP  
  
The stencil operation specifies how the stencil buffer is updated. The operation selected depends on whether the stencil test 

passes or not.

See also

[StencilFunc](stencilfunc.md), [StencilMask](stencilmask.md)

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