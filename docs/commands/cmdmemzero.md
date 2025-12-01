# CmdMemZero

Action

Write zero to a block of memory.

Syntax

CmdMemZero ptr, num

Remarks

ptr | Starting address of the memory block  
---|---  
num | Number of bytes in the memory block  
  
The completion of this function is detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.

Example

```vb
' Pseudocode

' To erase the first 1K of main memory

```
CmdMemZero 0, 1024