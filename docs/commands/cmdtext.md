# CmdText

Action

Draw Text.

Syntax

CmdText x, y, font, options, string

Remarks

x | x-coordinate of text base, in pixels  
---|---  
y | y-coordinate of text base, in pixels  
font | Internal Fonts 16-31, User Defined Fonts 0-14  
options | By default (x,y) is the top-left pixel of the text (options = 0).  OPT_CENTERX centers the text horizontally OPT_CENTERY centers it vertically OPT_CENTER centers the text in both directions OPT_RIGHTX right-justifies the text, so that the x is the rightmost pixel.  
string | text to display  
  
Example

ClearScreen  
ColorRGB &H80, &H80, &H00  
CmdText FT_DispWidth/2, FT_DispHeight/2, 31, OPT_CENTER, "Bascom is here"  
  
UpdateScreen

' Plain text at (0,0) in the largest font

CmdText 0, 0, 31, 0, "Text!"

![clip0063](clip0063.png)

' Using a smaller font

CmdText 0, 0, 26, 0, "Text!"

![clip0064](clip0064.png)

' Centered horizontally

CmdText 80, 60, 31, OPT_CENTERX, "Text!"

![clip0065](clip0065.png)

' Right-justified

CmdText 80, 60, 31, OPT_RIGHTX, "Text!"

![clip0066](clip0066.png)

' Centered vertically

CmdText 80, 60, 31, OPT_CENTERY, "Text!"

![clip0067](clip0067.png)

' Centered both horizontally and vertically

CmdText 80, 60, 31, OPT_CENTER, "Text!"

![clip0068](clip0068.png)