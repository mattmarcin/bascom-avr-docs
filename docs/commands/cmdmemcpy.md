# CmdMemCpy

Action

Copy a block of memory.

Syntax

CmdMemCpy dst, src, num

Remarks

dst | address of the destination memory block  
---|---  
src | address of the source memory block  
num | number of bytes to copy  
  
The completion of this function is detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.

Example

```vb
' Pseudocode

' To copy 1K byte of memory from 0 to &H8000

```
CmdMemCpy &H8000, 0, 1024