# CmdInflate

Action

Decompress data into memory.

Syntax

CmdInflate ptr

Remarks

ptr | Destination address. The data byte should immediate follow in the command buffer  
---|---  
  
If the number of bytes is not a multiple of 4, then 1, 2 or 3 bytes should be appended to ensure 4-byte alignment of the next command. These padding bytes can have any value Command layout.

Example

' See demos - FT800 Gauges.bas (Sub IntroFTDI), DigitTest.bas