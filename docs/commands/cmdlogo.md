# CmdLogo

Action

Play device logo animation.

Syntax

CmdLogo

Remarks

The logo command causes the co-processor engine to play back a short animation of the FTDI logo. 

During logo playback the MCU should not access any FT800 resources. After 2.5 seconds have elapsed, the co-processor

engine writes zero to REG_CMD_READ and REG_CMD_WRITE, and starts waiting for commands. After this command is complete, 

the MCU shall write the next command to the starting address of RAM_CMD.

Example

' see it working - FT800 Gauges.bas, FT800 Keyboard.bas, FT800 Signals.bas and FT800 Sketch.bas

![clip0038](clip0038.png)