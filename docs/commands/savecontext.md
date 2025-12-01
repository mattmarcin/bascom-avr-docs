# SaveContext

Action

Push the current graphics context on the context stack.

Syntax

SaveContext

Remarks

Saves the current graphics context Any extra SaveContext will throw away the earliest saved context.

See also

[RestoreContext](restorecontext.md)

Example

```vb
' Pseudocode

' Saving and restoring context means that the second 'G' is drawn in red, instead of blue

```
Begin_G BITMAPS

ColorRGB 255, 0, 0 

SaveContext

ColorRGB 50, 100, 255

Vertex2II 80, 38, 31, &H47

RestoreContext

Vertex2II 110, 38, 31, &H47

![clip0083](clip0083.png)