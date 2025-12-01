# CmdRegRead

Action

Read a register value.

Syntax

CmdRegRead ptr, result

Remarks

ptr | Address of register to read  
---|---  
result | The register value to be read at ptr address  
  
Example

```vb
' Pseudocode

' To capture the exact time when a command completes:

```
x = Rd16(REG_CMD_WRITE

CmdRegread REG_CLOCK, 0

...