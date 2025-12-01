# $ROMSTART

Action

Instruct the compiler to generate a hex/bin file that starts at the specified address.

Syntax

$ROMSTART = address

Remarks

Address | The address where the code must start. By default the first address is 0.  
---|---  
  
![notice](notice.jpg)The $ROMSTART directive is an inheritance from BASCOM-8051. In the AVR it did not have any meaning.

In the 8051 you can use and relocate external memory. This is not possible in the AVR and hence there is no practical usage.

For a bootloader used with AVR and XMega you can use the $LOADER directive.

Only use $ROMSTART with the Xtiny platform and when you have a boot loader !

In version 2083 where XTINY is supported the $ROMSTART has a new purpose. Since the boot loading mechanism in the XTINY differs from the other AVR processors, the $ROMSTART can be used to relocate the address.

The memory map starts with the BOOT area, followed by the application area. This means that a boot loader starts at &H0000 and a normal application will start after that.

So in order to use a bootloader, your normal code need to be compiled with the $ROMSTART directive. When the boot loader uses 1024 bytes, it means that the normal application starts at the WORD address which is halve of the byte address and in this case would be &H200 (1024 dec=400 hex).

The simulator supports $ROMSTART relocated code.

See also

[$LOADER](loader.md) , [Using a BOOTLOADER](using_a_bootloader.md)

ASM

NONE

Example

$ROMSTART = &H200 'xtiny boot loader