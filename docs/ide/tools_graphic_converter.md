# Tools Graphic Converter

The Graphic converter is intended to convert BMP files into BASCOM Graphic Files (.BGF) that can be used with Graphic LCD displays.

The following dialog box will be shown:

![graphic_converter](graphic_converter.png)

To load a picture click the Load button.

The picture can be maximum 128 pixels high and 240 pixels width.

When the picture is larger it will be adjusted.

You can use your favorite graphic tool to create the bitmaps and use the Graphic converter to convert them into black and white images.

When you click the Save-button the picture will be converted into black and white.

Any non-white color will be converted into black.

The resulting file will have the BGF extension. (bascom graphics format)

You can also paste a picture from the clipboard by clicking the Paste button.

Press the Ok-button to return to the editor.

The picture can be shown with the [ShowPic](showpic.md) statement or the [ShowpicE](showpice.md) statement.

![notice](notice.jpg) The BGF files are RLE encoded to save space.

![notice](notice.jpg) It is important that the font selection 6*8 or 8*8 match the font size in the CONFIG GRAPHLCD. For example :

Config Graphlcd = 240x128 , Dataport = Porta , Controlport = Portc , Ce = 2 , Cd = 3 , Wr = 0 , Rd = 1 , Reset = 4 , Fs = 5 , Mode = 8

In this case you would use 8*8.

When you use your own drawing routine you can also save the pictures uncompressed by setting the Uncompressed check box. The resulting BGF files can not be shown with the showpic or showpicE statements anymore in that case!

The BGF format is made up as following:

•| first byte is the height of the picture  
---|---  
  
•| second byte is the width of the picture  
---|---  
  
•| for each row, all pixels are scanned from left to right in steps of 6 or 8 depending on the font size. The resulting byte in stored with RLE compression  
---|---  
  
The RLE method used is : byte value, AA(hex), repeats.

So a sequence of 5, AA, 10 means that a byte with the value of 5 must be repeated 16 times (hex notation used)

Option | Description  
---|---  
Height | The height in pixels of the image.  
Width | The width in pixels of the image.  
Font | The T6963 supports 6x8 and 8x8 fonts. This is the font select that must match the CONFIG statement. For other displays, use 8*8.  
Type | The size of the display. When the size is not listed, use one with the same width.  
SED Series | If your display is a SEDxxxx chip, select this option.  
Uncompressed | Images are RLE encoded. Select this option when you do not want to compress the image.