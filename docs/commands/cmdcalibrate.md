# CmdCalibrate

Action

Execute the touch screen calibration routine.

Syntax

CmdCalibrate

Remarks

The calibration procedure collects three touches from the touch screen, then computes and loads an appropriate matrix into REG_TOUCH_TRANSFORM_A-F. To use it, create a display list and then use [CmdCalibrate](cmdcalibrate.md). The co-processor engine overlays the touch

targets on the current Display List, gathers the calibration input and updates REG_TOUCH_TRANSFORM_A-F.

The completion of this function is detected when the value of REG_CMD_READ is equal to REG_CMD_WRITE.