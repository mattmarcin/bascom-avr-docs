# $LOADERSIZE

Action

Instruct the compiler that a boot loader is used so it will not overwrite the boot space.

Syntax

$LOADERSIZE = size

Remarks

size | The amount of space in bytes that is used by the boot loader.  
---|---  
  
When you use a boot loader it will use space from the available flash memory. The compiler does not know if you use a boot loader or not. It also does not know how you have set the fuse bits, so it is impossible to know how big the bootloader size is. When your program exceeds the available space and runs into the boot sector space, it will overwrite the boot loader.

The $loadersize directive will take the boot loader size into account so you will get an error when the target file gets too big.

When you select the MCS boot loader as programmer the IDE also will take into account the specified boot loader size.

The directive can be used when you have a different programmer selected. For example an external programmer that does not know about the boot size.

![notice](notice.jpg)Do not use this directive in the bootloader program itself. You will get an error 344 in that case. $LOADERSIZE is only intended to be used in normal applications. 

See also

[$LOADER](loader.md) , [$BOOT](_boot.md)

ASM

NONE

Example

NONE