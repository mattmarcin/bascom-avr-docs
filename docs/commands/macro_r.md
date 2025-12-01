# Macro_R

Action

Execute a single command from a macro register.

Syntax

Macro_R m

Remarks

m | Macro register to read. Value 0 means the FT800 will fetch the command from REG_MACRO_0 to execute. Value 1 means the FT800 will fetch the command from REG_MACRO_1 to execute. The content of REG_MACRO_0 or REG_MACRO_1 shall be a valid display list command, otherwise the behavior  is undefined.  
---|---  
  
See Also

[CALL_C](call_c.md) , [JUMP](jump.md), [RETURN_C](return_c.md) , [DISPLAY_E](display_e.md)