# CmdNumber

Action

Draw a decimal number.

Syntax

CmdNumber x, y, font, options, n

Remarks

x | x-coordinate of text base, in pixels  
---|---  
y | y-coordinate of text base, in pixels  
font | font to use for text, 0-31. See ROM and RAM Fonts  
options | By default (x,y) is the top-left pixel of the text. OPT_CENTERX centers the text horizontally OPT_CENTERY centers it vertically.  OPT_CENTER centers the text in both directions.  OPT_RIGHTX right-justifies the text, so that the x is the rightmost pixel. By default the number is displayed with no leading zeroes, but if a width 1-9 is specified in the options, then the number is padded if necessary with leading zeroes so that it has the given width.  If OPT_SIGNED is given, the number is treated as signed, and prefixed by a minus sign if negative.  
n | The number to display, either unsigned or signed 32-bit. NOTE : while -2147483648 is valid for a long, the FT800 will show -18446744071562067968 (128 bit signed number) which seems a bug in the FT800.  
  
Example

```vb
' Pseudocode

' A number

```
CmdNumber 20, 60, 31, 0, 42

![clip0039](clip0039.png)

' Centered

CmdNumber 80, 60, 31, OPT_CENTER, 42

![clip0040](clip0040.png)

' Signed output of positive and negative numbers

CmdNumber 20, 20, 31, OPT_SIGNED, 42

CmdNumber 20, 60, 31, OPT_SIGNED, -42

![clip0041](clip0041.png)

' Forcing width to 3 digits, right-justified

CmdNumber 150, 20, 31, OPT_RIGHTX OR 3, 42

CmdNumber 150, 60, 31, OPT_SIGNED OR OPT_RIGHTX OR 3, -1

![clip0042](clip0042.png)