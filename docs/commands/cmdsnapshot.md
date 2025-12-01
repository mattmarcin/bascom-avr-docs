# CmdSnapShot

Action

Take a snapshot of the current screen.

Syntax

CmdSnapShot  ptr 

Remarks

ptr | Snapshot destination address, in RAM_G  
---|---  
  
This command causes the co-processor engine to take a snapshot of the current screen, and write the result into RAM_G as a ARGB4 bitmap.The size of the bitmap is the size of the screen, given by the REG_HSIZE and REG_VSIZE registers.

During the snapshot process, the display should be disabled by setting REG_PCLK to 0 to avoid display glitch.

Because co-processor engine needs to write the result into the destination address, the destination address must be never used or referenced by graphics engine.

Note: If you want to actual take Screen Captures - see FT800 Capture.Bas

Example

' See demo - FT800 Demo4.bas (Sub Snapshot)