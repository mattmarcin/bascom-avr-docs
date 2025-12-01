# RestoreContext

Action

Restore the current graphics context from the context stack.

Syntax

RestoreContext

Remarks

Restores the current graphics context. Four (4) levels of SAVE and RESTORE are available in the FT800.

Any extra RestoreContext will load the default values into the present context.

See also

[SaveContext](savecontext.md)

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

Vertex2II 110, 38, 31,&H47

![clip0086](clip0086.png)