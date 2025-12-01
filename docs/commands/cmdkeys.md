# CmdKeys

Action

draw a row of keys.

Syntax

CmdKeys x, y, w ,h, font, options, char

Remarks

x | x-coordinate of keys top-left, in pixels  
---|---  
y | y-coordinate of keys top-left, in pixels  
w | The width of the keys  
h | The height of the keys  
font | Bitmap handle to specify the font used in key label. The valid range is from 0 to 31  
options | By default the keys are drawn with a 3D effect and the value of option is zero.  OPT_FLAT removes the 3D effect. If OPT_CENTER is given the keys are drawn at minimum size centered within the w x h rectangle. Otherwise the keys are expanded so that they completely fill the available space.  If an ASCII code is specified, that key is drawn 'pressed' - i.e. in background color with any 3D effect removed.  
char | Key labels, one character per key. The TAG value is set to the ASCII value of each key, so that key presses can be detected using the REG_TOUCH_TAG register.  
  
The gap between keys is 3 pixels.

For OPT_CENTERX case, the keys are (font width + 1.5) pixels wide ,otherwise keys are sized to fill available width.

Example

```vb
' Pseudocode

' A row of keys

```
CmdKeys 10, 10, 140, 30, 26, 0, "12345"

![clip0031](clip0031.png)

' Without the 3D look

CmdKeys 10, 10, 140, 30, 26, OPT_FLAT, "12345"

![clip0032](clip0032.png)

' Default vs. Centered

CmdKeys 10, 10, 140, 30, 26, 0, "12345"

CmdKeys 10, 60, 140, 30, 26, OPT_CENTER, "12345"

![clip0033](clip0033.png)

' Setting the options to show '2' key pressed ('2' is ASCII code &H32)

CmdKeys 10, 10, 140, 30, 26, &H32, "12345"

![clip0034](clip0034.png)

' A calculator-style keyboard using font 29

CmdKeys 22, 1, 116, 28, 29, 0, "789"

CmdKeys 22, 31, 116, 28, 29, 0, "456"

CmdKeys 22, 61, 116, 28, 29, 0, "123"

CmdKeys 22, 91, 116, 28, 29, 0, "0."

![clip0035](clip0035.png)

' A compact keyboard drawn in font 20

CmdKeys 2, 2, 156, 21, 20, OPT_CENTER, "qwertyuiop"

CmdKeys 2, 26, 156, 21, 20,OPT_CENTER, "asdfghijkl"

CmdKeys 2, 50, 156, 21, 20,OPT_CENTER, "zxcvbnm"

CmdButton 2,74, 156, 21, 20, 0, ""

![clip0036](clip0036.png)

' Showing the f (ASCII &H66) key pressed

CmdKeys 2, 2, 156, 21, 20, &H66 OR OPT_CENTER, "qwertyuiop"

CmdKeys 2, 26, 156, 21, 20, &H66 OR OPT_CENTER, "asdfghijkl"

CmdKeys 2, 50, 156, 21, 20, &H66 OR OPT_CENTER, "zxcvbnm"

CmdButton 2, 74, 156, 21, 20, 0, ""

![clip0037](clip0037.png)