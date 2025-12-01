# Call_C

Action

Execute a sequence of commands at another location in the Display List (RAM_DL). 

Syntax

Call_C dest 

Remarks

dest | The destination address in RAM_DL which the display command is to be switched. FT800 has the stack to store the return address. To come back to the next command of source address, the RETURN command can help.   
---|---  
  
Call_C and Return_C have a 4 level stack in addition to the current pointer. 

Any additional Call_C/Return_C done will lead to unexpected behavior.

See also

[JUMP](jump.md), [RETURN_C](return_c.md) , [MACRO_R](macro_r.md) , [DISPLAY_E](display_e.md)