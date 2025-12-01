# CmdFgColor

Action

Set the Foreground Color.

Syntax

CmdFgColor rgb

Remarks

rgb | New Foreground color, as a 24-bit RGB number. Red is the most significant 8 bits and Blue is the least. So &Hff0000 is bright Red. Foreground color is applicable for things that the user can move such as handles and buttons.  
---|---  
  
See also

[CmdBgColor](new_cf_card_drivers.md)

Example

' Pseudocode

xOffset = 40  
yOffset = 80  
' Draw horizontal Toggle bars  
CmdBgColor &H800000  
CmdFgColor &H410105  
CmdToggle xOffset, yOffset, 30, 27, 0, 65535, "-ve" + gap + "+ve"  
CmdFgColor &H0b0721  
CmdBgColor &H000080

' The top scrollbar uses the default foreground color, the others with a changed color

CmdScrollBar 20, 30, 120, 8, 0, 10, 40, 100

CmdFgColor &H703800

CmdScrollBar 20, 60, 120, 8, 0, 30, 40,100

CmdFgColor &H387000

CmdScrollBar 20, 90, 120, 8, 0, 50, 40, 100

![clip0108](clip0108.png)