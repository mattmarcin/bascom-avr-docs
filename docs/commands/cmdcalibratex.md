# CmdCalibratex

Action

Execute the touch screen calibration routine.

This is all in one routine with displaying prompts on the screen and updating of the REG_TOUCH_TRANSFORM_A-F registers.

Syntax

CmdCalibratex

Remarks

The calibration procedure collects three touches from the touch screen, then computes and loads an appropriate matrix into REG_TOUCH_TRANSFORM_A-F. To use it, create a display list and then use [CmdCalibrate](cmdcalibratex.md). The co-processor engine overlays the touch

targets on the current Display List, gathers the calibration input and updates REG_TOUCH_TRANSFORM_A-F.

Note: You can Automatically let Bascom do the Screen calibration for you.

Or if you want to force an Screen calibration at anytime:

1.| Press on the LCD panel  
---|---  
  
2.| Reset your project  
---|---  
  
3.| When you release from the LCD the Screen calibration message will appear.  
---|---  
  
To enable this mode, set LcdCal = 1 from the FT800.inc file.

Const LcdCal = 1 ' Prompts for LCD Calibration (if not previously done)

See also

[CmdCalibrate](cmdcalibrate.md)