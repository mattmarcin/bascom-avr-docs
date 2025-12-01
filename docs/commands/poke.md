# POKE

Action

Write a byte to an internal register.

Syntax

POKE address , value

Remarks

Address | Numeric variable with the address of the memory location to set. (0-31)  
---|---  
Value | Value to assign. (0-255)  
  
See also

[PEEK](peek.md) , [CPEEK](cpeek.md) , [INP](inp.md) , [OUT](out.md), [SETREG](setreg.md), [GETREG](getreg.md)

Example

Poke 1 , 1 'write 1 to R1

End