# Tools Font Editor

The Font Editor was a Plug in which is now integrated into the Tools menu.

The editor is intended to create Fonts that can be used with Graphical display such as SED1521, KS108, color displays, etc.

When you choose this option the following window will appear:

![font_editor](font_editor.gif)

You can open an existing Font file, or Save a modified file.

The supplied font files are installed in the Samples\lcdgraph folder.

You can copy an image from the clipboard, and you can then move the image up , down, left and right.

When you select a new character, the current character is saved. The suggest button will draw an image of the current selected character.

When you keep the left mouse button pressed, you can set the pixels in the grid. When you keep the right mouse button pressed, you can clear the pixels in the grid.

When you choose the option to create a new Font, you must provide the name of the font, the height of the font in pixels and the width of the font in pixels.

The Max ASCII is the last ASCII character value you want to use. Each character will occupy space. So it is important that you do not choose a value that is too high and will not be used.

When you display normal text, the maximum number is 127 so it does not make sense to specify a value of 255.

A font file is a plain text file. 

Lets have a look at the first few lines of the 8x8 font:

Font8x8:

$asm

.db 1,8,8,0

.db 0,0,0,0,0,0,0,0 ; 

.db 0,0,6,95,6,0,0,0 ; !

The first line contains the name of the font. With the [SETFONT](setfont.md) statement you can select the font. Essential, this sets a data pointer to the location of the font data.

The second line ($ASM) is a directive for the internal assembler that asm code will follow.

All other lines are data lines. 

The third line contains 4 bytes: 1 (height in bytes of the font) , 8 (width in pixels of the font), 8 (block size of the font) and a 0 which was not used before the 'truetype' support, but used for aligning the data in memory. This because AVR object code is a word long.

This last position is 0 by default. Except for 'TrueType' fonts. In BASCOM a TrueType font is a font where every character can have it's own width. The letter 'i' for example takes less space then the letter 'w'. The EADOG128 library demonstrates the TrueType option.

In order to display TT, the code need to determine the space at the left and right of the character. This space is then skipped and a fixed space is used between the characters. You can replace the 0 by the width you want to use. The value 2 seems a good one for small fonts.

All other lines are bytes that represent the character.

Graphical LCD uses 1 byte to set 8 pixels black/white.

The LCD driver will for load the height in bytes i the example this is 1 byte.

Then the driver will load the width in bytes of the character. in the example this is 8. This means that data lines are 8 bytes long. 

And finally the block size in bytes of one character will be loaded. This is simply the first parameter times the second parameter. In the example this is 8 too. The last parameter is loaded to see if TT spacing must be used.

Depending on the ASCII value of the character to show, the driver will located the proper place in the table by multiplying the block size with the ASCII value. This will be added to the start of the table address.

Now the driver will load and write a byte and thus will set 8 pixels.

The pixels are shown from top to bottom like this :

x 

x

x

x

x

x

x

x

Then the next byte will be loaded and send to the lcd.

xy 

xy

xy

xy

xy

xy

xy

xy

and this will repeat for the number of bytes specified. 

Then if the height is more than 1 byte, the next block will be loaded. 

This also means that each font height must be a multiple of 8 pixels.

This restriction is only because writing a full byte is the fastest way to update an LCD.