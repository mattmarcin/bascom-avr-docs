# CmdMemCrc

Action

Compute a CRC-32 for memory.

Syntax

CmdMemCrc ptr, num, result

Remarks

ptr | Starting address of the memory block  
---|---  
num | Number of bytes in the source memory block  
result | Output parameter; written with the CRC-32 after command execution. The completion of this function is detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.  
  
Example

```vb
' Pseudocode

' To compute the CRC-32 of the first 1K byte of FT800 memory, first record the value 

' of REG_CMD_WRITE, execute the command, wait for completion, then read the 32-bit value at result.

```
x = Rd16(REG_CMD_WRITE)

CmdMemCrc 0, 1024, 0

Print Rd32(RAM_CMD + x + 12)