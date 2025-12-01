# CmdBgColor

Action

Set the Background Color.

Syntax

CmdBgColor rgb

Remarks

rgb | New Background color, as a 24-bit RGB number. Red is the most significant 8 bits and Blue is the least. So &Hff0000 is bright Red. Background color is applicable for things that the user can move. example: behind gauges and sliders etc..  
---|---  
  
See also

[CmdFgColor](new_cf_card_drivers.md)

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

CmdFgColor &H402000

CmdScrollBar 20, 60, 120, 8, 0, 30, 40,100

CmdFgColor &H202020

CmdScrollBar 20, 90, 120, 8, 0, 50, 40, 100

![clip0109](clip0109.png)