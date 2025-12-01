# BOXFILL

Action

Create a filled box on a graphical display.

Syntax

BOXFILL (x1,y1) - (x2,y2) , color

Remarks

x1 | The left corner position of the box  
---|---  
y1 | The top position of the box  
x2 | The right corner position of the box  
y2 | The bottom position of the box  
color | The color to use to fill the box  
  
The BOXFILL command will draw a number of lines which will appear as a filled box.

See also

[LINE](line.md), [CIRCLE](circle.md) , [BOX](box.md)

ASM

NONE

Example

'create a bargraph effect

Boxfill(0 , 0) -(60 , 10) , 1

Boxfill(2 , 2) -(40 , 8) , 0