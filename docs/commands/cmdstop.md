# CmdStop

Action

Stop any of spinner, screensaver or sketch.

Syntax

CmdStop

Remarks

```vb
For [CmdSpinner](cmdspinner.md) and [CmdScreenSaver](cmdscreensaver.md), REG_MACRO_0 and REG_MACRO_1 will be stopped updating. 

For [CmdSketch](cmdsketch.md) the bitmap data in RAM_G will be stopped updating.

```
Example

```vb
' See FT800 Demo1.bas - Sub Widget_Spinner

' FT800 Demo4.bas - SUB Sketch, Sub Screensaver 

```