# SHOWPIC

Action

Shows a BGF file on the graphic display

Syntax

SHOWPIC x, y , label

Remarks

Showpic can display a converted BMP file. The BMP must be converted into a BGF file with the [Tools Graphic Converter](tools_graphic_converter.md).

The X and Y parameters specify where the picture must be displayed. X and Y must be 0 or a multiple of 8. The picture height and width must also be a multiple of 8.

The label tells the compiler where the graphic data is located. It points to a label where you put the graphic data with the $BGF directive.

You can store multiple pictures when you use multiple labels and $BGF directives,

Note that the BGF files are RLE encoded to save code space.

See also

[PSET](pset.md) , [$BGF](_bgf.md) , [CONFIG GRAPHLCD](config_graphlcd.md) , [LINE](line.md) , [CIRCLE](circle.md) , [SHOWPICE](showpice.md)

Example

See [$BGF](_bgf.md) example