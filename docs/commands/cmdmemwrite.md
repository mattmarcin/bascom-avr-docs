# CmdMemWrite

Action

Write bytes into memory.

Syntax

CmdMemWrite ptr, num, 

Remarks

ptr | The memory address to be written  
---|---  
result | Number of bytes to be written  
  
The data byte should immediately follow in the command buffer. If the number of bytes is not a multiple of 4, then

1, 2 or 3 bytes should be appended to ensure 4-byte alignment of the next command, these padding bytes can have any value.

The completion of this function can be detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.

Caution: if using this command, it may corrupt the memory of the FT800 if used improperly.

Example

```vb
' Pseudocode

' To change the backlight brightness to 64 (half intensity) for a particular screen shot

```
...

CmdSwap ' finish the display list

CmdDlStart ' wait until after the swap

CmdMemWrite REG_PWM_DUTY, 4 ' write to the PWM_DUTY register