# CmdAppend

Action

Appends a block of memory to the current display list memory address where the offset is specified in REG_CMD_DL.

Syntax

CmdAppend Ptr, Num

Remarks

Ptr | Start of source commands in main memory  
---|---  
Num | Number of bytes to copy. This must be a multiple of 4  
  
After appending is done, the co-processor engine will increase the REG_CMD_DL by num to make sure the display list is in order.

Example

' Pseudocode

CmdAppend 0, 40 ' Copy 10 commands from main memory address 0

Display_E  ' finish the display list