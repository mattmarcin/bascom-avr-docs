# LCD RGB-8 Converter

Action

This tool is intended to convert normal bitmaps into BGC files.

The BGC format is the Bascom Graphic Color Format.

This is a special RLE compressed format to save space.

The SHOWPIC statement can display graphic bitmaps.

The color display uses a special RGB8 format.

The LCD converter has the task to convert a normal windows bitmap into a 256-color RGB8 coded format.

When you run the tool you will see the following window :

![rgb8-converter](rgb8-converter.png)

You can use File , Open, to load an image from disk.

Or you can use Edit, Paste, to paste an image from the clipboard.

Option | Description  
---|---  
File, Open | Open a graphical file from disk.  
File, Save, Image | Save the file as a windows graphical file  
File, Save, Binary | Save the BGC file, the file you need with SHOWPIC  
File, Save , Data Lines | Save the file as data lines into a text file  
File, Convert | Converts the bitmap into a RGB8 bitmap  
Edit, Bitmap height | height of the image. Change it to make the image smaller or larger  
Edit, Bitmap width | width of the image. Change it to make the image wider.  
Edit, Select All | Select entire image  
Edit, Copy | Copy selection to the clipboard  
Edit, Paste | Paste clipboard to the selection. You must have an area selected !  
Edit, Delete | Delete the selected area  
  
The Output TAB, has an option : Save as RLE. This must be checked. By default it is checked.

When you do not want the image to be RLE encoded, you can uncheck this option.

The bottom area is used to store the DATA lines.

The Color TAB shows the effect on the table inside the color display.

When a picture uses a lot of different red colors, you can put the most used into the table.

It is well explained in the manuals from display3000.

By clicking on the color , you can view which colors are used by the picture.

You can match them with the color table.

You can download the LCD Converter tool from :

[http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=168&Itemid=54](<http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=168&Itemid=54>)