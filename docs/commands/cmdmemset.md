# CmdMemSet

Action

Fill memory with a byte value.

Syntax

CmdMemSet ptr, value, num

Remarks

ptr | Starting address of the memory block  
---|---  
value | Value to be written to memory  
num | Number of bytes in the memory block  
  
The completion of this function is detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.

Example

```vb
' Pseudocode

' To write 0xff the first 1K of main memory

```
CmdMemSet 0, 255, 1024