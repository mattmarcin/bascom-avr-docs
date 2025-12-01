# BYVAL

Action

Specifies that a variable will be passed by value.

Syntax

Sub Test(BYVAL var)

Remarks

Var | Variable name  
---|---  
  
The default for passing variables to SUBS and FUNCTIONS, is by reference(BYREF). When you pass a variable by reference, the address is passed to the SUB or FUNCTION. When you pass a variable by Value, a temp variable is created on the frame and the address of the copy is passed.

When you pass by reference, changes to the variable will be made to the calling variable.

When you pass by value, changes to the variable will be made to the copy so the original value will not be changed.

By default passing by reference is used.

Note that calling by reference will generate less code.

See also

[CALL](call.md) , [DECLARE](declare_sub.md) , [SUB](sub.md) , [FUNCTION](declare_function.md)

ASM

NONE

Example

Declare Sub Test(Byval X As Byte, Byref Y As Byte, Z As Byte)