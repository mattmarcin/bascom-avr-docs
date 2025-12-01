# CMDFTSTACK

Action

This FT800 command will send data from the soft stack to the FT800 processor.

Syntax

CMDFTSTACK bts [,opt]

Remarks

bts | The number of bytes to pop from the stack.  
---|---  
opt | An optional parameter to change stack clean up. When no parameter or 0 is specified, the soft stack will be cleaned up. But when a string is passed you can not clean up the stack since the pointers would point to the wrong address. In such a case specify a numeric value like 2 so the compiler will not clean up the stack. You must clean up the stack before the code returns. You can do this with the ADIW asm command. Please make sure you adjust with the same amount of bytes as you passed.  
  
See also

[FT800](ft800.md) , [CMD32](cmd32.md)

Example

```vb
'------------------------------------------------------------------------------------------------------------  
Sub Cmdbutton(bystack X As Integer , Bystack Y As Integer , Bystack W As Integer , Bystack H As Integer , Bystack Fontx As Integer , Bystack Options As Word , Byval S As String)  
'------------------------------------------------------------------------------------------------------------  
' Draws Keyboard like buttons  
  
' Options Are  
' OPT_3D = 0  
' OPT_FLAT  
  
If Asc(S) = 0 Or Asc(S) > 127 then

```
!adiw yl,12 ; manual clean up stack

```vb
Exit Sub

End if   
  
```
Cmd32 Cmd_button  
cmdftstack 12,2 'pop and transmit 12 bytes, option 2 means, no stack clean up  
Cmdstr S 'because we access this string we could not clean up   
! adiw yl,12 ; manual clean up stack  
End Sub