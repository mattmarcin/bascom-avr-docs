# CmdButton

Action

Draw a button.

Syntax

CmdButton x, y, w, h ,font, options, text

Remarks

x | x-coordinate of button top-left, in pixels  
---|---  
y | y-coordinate of button top-left, in pixels  
w | width of button, in pixels  
h | height of button, in pixels  
font | Internal Fonts 16-31, User Defined Fonts 0-14  
options | By default the button is drawn with a 3D effect, OPT_FLAT removes the 3D effect.  
text | Text to display, valid printable ASCII code 32 to 127. For Custom/User Defined font, the ASCII code is from 1 to 127.  
  
Example

' Pseudocode

CmdButton 10, 10, 50, 25, 26, 0, "One"  
CmdButton 10, 40, 50, 25, 26, 0, "Two"  
CmdButton 10, 70, 50, 25, 26, 0, "Three"

' A 140x00 pixel button with large text

CmdButton 10, 10, 140, 100, 31, 0,"Press!"

![clip0105](clip0105.png)

' Several smaller buttons

CmdButton 10, 10, 50, 25, 26, 0, "One"

CmdButton 10, 40, 50, 25, 26, 0, "Two"

CmdButton 10, 70, 50, 25, 26, 0, "Three"

![clip0106](clip0106.png)

' Changing button color

CmdFgColor &Hb9b900

CmdButton 10, 10, 50, 25, 26, 0, "Banana"

CmdFgColor &Hb97300

CmdButton 10, 40, 50, 25, 26, 0, "Orange"

CmdFgColor &Hb90007

CmdButton 10, 70, 50, 25, 26, 0, "Cherry"

![clip0107](clip0107.png)