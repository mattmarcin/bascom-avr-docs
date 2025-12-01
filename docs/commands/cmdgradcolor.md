# CmdGradColor

Action

Set the 3D button highlight color.

Syntax

CmdGradColor c

Remarks

c | New highlight gradient color, as a 24-bit RGB number. Red is the most significant 8 bits, blue is the least.  So &Hff0000 is bright red.  
---|---  
  
Gradient is supported only for Button and Keys widgets.

Example

```vb
' Pseudocode

' Changing the gradient color: white (the default), red, green and blue

```
CmdFgColor &H101010

CmdButton 2, 2, 76, 56, 31, 0, "W"

CmdGradColor &Hff0000

CmdButton 82, 2, 76, 56, 31, 0, "R"

CmdGradColor &H00ff00

CmdButton 2, 62, 76, 56, 31, 0, "G"

CmdGradColor &H0000ff

CmdButton 82, 62, 76, 56, 31, 0,"B"

![clip0110](clip0110.png)

' The gradient color is also used for keys

CmdFgColor &H101010

CmdKeys 10, 10, 140, 30, 26, 0, "abcde"

CmdGradColor &Hff0000

CmdKeys 10, 50, 140, 30, 26, 0, "fghij"

![clip0111](clip0111.png)