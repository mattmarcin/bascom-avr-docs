# CmdTrack

Action

Track touches for a graphics object.

Syntax

CmdTrack x, y, w, h, tag

Remarks

x | For linear tracker functionality, x-coordinate of track area top-left, in pixels. For rotary tracker functionality, x-coordinate of track area center, in pixels.  
---|---  
y | For linear tracker functionality, y-coordinate of track area top-left, in pixels. For rotary tracker functionality, y-coordinate of track area center, in pixels.  
w | Width of track area, in pixels.  
h | Height of track area, in pixels. A w and h of (1,1) means that the tracker is rotary, and reports an, angle value in REG_TRACKER. A w and h of (0,0) disables the track functionality of co-processor engine.  
tag | tag of the graphics object to be tracked, 1-255  
  
This command will enable co-processor engine to track the touch on the particular graphics object with one valid tag value assigned. Then, co-processor engine will update the REG_TRACKER periodically with the frame rate of LCD display panel. 

Co-processor engine tracks the graphics object in rotary tracker mode and linear tracker mode: 

•| Rotary tracker mode â Track the angle between the touching point and the center of graphics object specified by tag value.  
---|---  
  
The value is in units of 1/65536 of a circle. 0 means that the angle is straight down, &H4000 left, &H8000 up, and &HC000 right

from the center.

•| Linear tracker mode â If parameter w is greater than h, track the relative distance of touching point to the width of graphics  
---|---  
  
object specified by tag value. If parameter w is not greater than h, Track the relative distance of touching point to the height of graphics object specified by tag value. The value is in units of 1/65536 of the width or height of graphics object.

The distance of touching point refers to the distance from the top left pixel of graphics object to the coordinate of touching point. 

Example

Note: see demo files for more examples

```vb
' Pseudocode

' Horizontal track of rectangle dimension 40x12 pixels and the present touch is at 50%

```
ClearColorRGB 5, 45, 110

ColorRGB 255, 168, 64

Clear_B 1 ,1 ,1

Begin_G RECTS

Vertex2F 60 * 16, 50 * 16

Vertex2F 100 * 16, 62 * 16

ColorRGB 255, 0, 0

Vertex2F 60 * 16,50 * 16

Vertex2F 80 * 16,62 * 16

ColorMask 0 ,0 ,0 ,0

Tag 1

Vertex2F 60 * 16,50 * 16

Vertex2F 100 * 16,62 * 16

CmdTrack 60 * 16, 50 * 16, 40, 12, 1

![clip0072](clip0072.png)

' Circular track centered at (80,60) display location

ClearColorRGB 5, 45, 110

ColorRGB 255, 168, 64

Clear_B 1 ,1 ,1

Begin_G RECTS

Vertex2F 70 * 16,40 * 16

Vertex2F 82 * 16,80 * 16

ColorRGB 255, 0, 0

Vertex2F 70 * 16,40 * 16

Vertex2F 82 * 16,60 * 16

ColorMask 0 ,0 ,0 ,0

Tag 1

Vertex2F 70 * 16,40 * 16

Vertex2F 82 * 16,80 * 16

CmdTrack 70 * 16, 40 * 16, 12, 40, 1

![clip0073](clip0073.png)

' To draw a dial with tag 33 centered at (80, 60), adjustable by touch

angle = &H8000

CmdTrack 80, 60, 1, 1, 33

Do

Tag 33

CmdDial 80, 60, 55, 0, angle

.....

tracker = Rd32(REG_TRACKER)

If tracker AND 255 = 33 Then

angle = tracker * 1000

.....

```vb
End If

Loop

```
![clip0074](clip0074.png)

' To make an adjustable slider with tag 34

val = &H8000

CmdTrack 20, 50, 120, 8, 34

Do

...

Tag 34

CmdSlider 20, 50, 120, 8, val, 65535

...

tracker = Rd32(REG_TRACKER)

If tracker AND 255 = 33 Then

val = tracker * 1000

End If

...

Loop

![clip0075](clip0075.png)