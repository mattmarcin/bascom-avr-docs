# CmdToggle

Action

Draw a toggle switch.

Syntax

CmdToggle x, y, w, font, options, state, char

Remarks

x | x-coordinate of top-left of toggle, in pixels  
---|---  
y | y-coordinate of top-left of toggle, in pixels  
w | width of toggle, in pixels  
font | font to use for text, 0-31  
options | By default the toggle is drawn with a 3D effect and the value of options is zero.  Options OPT_FLAT removes the 3D effect.  
state | state of the toggle: 0 is off, 65535 is on  
char | String label for toggle. To seperate the labels use 'gap' ie: "off" + gap + "on"  
  
The details of physical dimension are

•| Outer bar radius I is font height*(20/16)  
---|---  
  
•| Knob radius is r-1.5  
---|---  
  
Example

```vb
' Pseudocode

' Using a medium font, in the two states

```
CmdToggle 60, 20, 33, 27, 0, 0,"no" \+ gap + "yes"

CmdToggle 60, 60, 33, 27, 0, 65535, "no" \+ gap + "yes"

![clip0069](clip0069.png)

' Without the 3D look

CmdToggle 60, 20, 33, 27, OPT_FLAT, 0, "no" \+ gap + "yes"

CmdToggle 60, 60, 33, 27, OPT_FLAT, 65535, "no" \+ gap + "yes"

![clip0070](clip0070.png)

' With different background and foreground colors

CmdBgColor &H402000

CmdFgColor &H703800

CmdToggle 60, 20, 33, 27, 0, 0, "no" \+ gap + "yes"

CmdToggle 60, 60, 33, 27, 0, 65535, "no" \+ gap + "yes"

![clip0071](clip0071.png)