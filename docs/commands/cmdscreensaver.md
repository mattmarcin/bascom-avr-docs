# CmdScreenSaver

Action

Start an animated screensaver.

Syntax

CmdScreenSaver

Remarks

After the screensaver command, the co-processor engine continuously updates REG_MACRO_0 with VERTEX2F with varying (x,y) coordinates. With an appropriate display list, this causes a bitmap to move around the screen without any MCU work.

Command CMD_STOP stops the update process.

Note that only one of [CmdSketch](cmdsketch.md), [CmdScreenSaver](cmdscreensaver.md) or [CmdSpinner](cmdspinner.md) can be active at one time.

REG_MACRO_0 is updated with respect to frequency of frames displayed (depending on the display registers configuration). 

Typically for 480x272 display the frame rate is around 60 frame per second.

Example

' see it working in FT800 Demo4.bas (Sub Screensaver)