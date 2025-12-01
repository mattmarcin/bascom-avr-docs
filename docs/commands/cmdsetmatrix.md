# CmdSetMatrix

Action

Write the current matrix to the Display List.

Syntax

CmdSetMatrix

Remarks

The co-processor engine assigns the value of the current matrix to the bitmap transform matrix of the graphics engine by generating Display List commands, i.e. BitmapTransformA-F. After this command, the following bitmap rendering operation will be affected by the new transform matrix.