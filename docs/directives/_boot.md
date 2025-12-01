# $BOOT

Action

Instruct the compiler to include boot loader support.

Syntax

$BOOT = address

Remarks

address | The boot loader address. This is a WORD address.   
---|---  
  
Some new AVR chips have a special boot section in the upper memory of the flash.

By setting some fuse bits you can select the code size of the boot section.

The code size also determines the address of the boot loader.

With the boot loader you can reprogram the chip when a certain condition occurs.

The sample checks a pin to see if a new program must be loaded.

When the pin is low there is a jump to the boot address.

The boot code must always be located at the end of your program.

It must be written in ASM since the boot loader may not access the application flash rom. This because otherwise you could overwrite your running code!

The example is written for the M163. You can use the Upload file option of the terminal emulator to upload a new hex file. The terminal emulator must have the same baud rate as the chip. Under Options, Monitor, set the right upload speed and set a monitor delay of 20. Writing the flash take time so after every line a delay must be added while uploading a new file.

![notice](notice.jpg) The $BOOT directive is replaced by $LOADER. $LOADER works much simpler. $BOOT is however still supported.

See also

[$LOADER](loader.md) , [$LOADERSIZE](loadersize.md)

Example

See BOOT.BAS from the samples dir. But better look at the $LOADER directive.