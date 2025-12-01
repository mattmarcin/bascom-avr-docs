# #AUTOCODE

Action

Informs the IDE that code can be maintained by the IDE.

Syntax

```vb
#AUTOCODE

CONFIG STATEMENTS

#ENDAUTOCODE

```
Remarks

Auto code informs the IDE that it may alter the code. A new IDE uses a property editor for the configuration. It will only update, add or delete, CONFIG statements that are enclosed in an #AUTOCODE block. 

#AUTOCODE must be closed with a matching #ENDAUTOCODE

You can still use CONFIG statements in other places of your code. But the property editor will only work on the ones inside the block.

The compiler will ignore #AUTOCODE and #ENDAUTOCODE.