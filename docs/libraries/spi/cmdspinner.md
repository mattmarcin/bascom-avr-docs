# CmdSpinner

Action

Start an animated spinner.

Syntax

CmdSpinner x, y, style, range

Remarks

x | The X coordinate of top left of spinner  
---|---  
y | The Y coordinate of top left of spinner  
style | The style of spinner. Valid range is from 0 to 3  
range | The scaling coefficient of spinner. 0 means no scaling  
  
The spinner is an animated overlay that shows the user that some task is continuing. To trigger the spinner, create a display list and then use CMD_SPINNER. The co-processor engine overlays the spinner on the current display list, swaps the display list to make it 

visible, then continuously animates until it receives CMD_STOP. REG_MACRO_0 and REG_MACRO_1 registers are utilized to perform the animation kind of effect. The frequency of points movement is with respect to the display frame rate configured. 

Typically for 480x272 display panels the display rate is ~60fps. 

```vb
For style 0 and 60fps the point repeats the sequence within 2 seconds. 

For style 1 and 60fps the point repeats the sequence within 1.25 seconds. 

For style 2 and 60fps the clock hand repeats the sequence within 2 seconds. 

For style 3 and 60fps the moving dots repeat the sequence within 1 second.

```
Note that only one of [CmdSketch](cmdsketch.md), [CmdScreenSaver](cmdscreensaver.md) or [CmdSpinner](cmdspinner.md) can be active at one time.

Example

```vb
' Pseudocode

' Create a display list, then start the spinner

```
Clear_B 1,1,1

CmdText 80, 30, 27, OPT_CENTER, "Please wait..."

CmdSpinner 80, 60, 0, 0

![clip0056](clip0056.png)

' Spinner style 0, a circle of dots

CmdSpinner 80, 60, 0, 0

![clip0057](clip0057.png)

' Style 1, a line of dots

CmdSpinner 80, 60, 1, 0

![clip0058](clip0058.png)

' Style 2, a rotating clock hand

CmdSpinner 80, 60, 2, 0

![clip0059](clip0059.png)

' Style 3, two orbiting dots

CmdSpinner 80, 60, 3, 0

![clip0060](clip0060.png)

' Half screen, scale 1

CmdSpinner 80, 60, 0, 1

![clip0061](clip0061.png)

' Full screen, scale 2

CmdSpinner 80, 60, 0, 2

![clip0062](clip0062.png)