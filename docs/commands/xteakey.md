# $XTEAKEY

Action

This directive accepts a 16 byte XTEA key and informs the compiler to encrypt the binary image.

Syntax

$XTEAKEY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

Remarks

$XTEAKEY accepts 16 parameters. These are the 16 bytes which together form a 128 bit key.

When your code is compiled, the resulting binary code will be encrypted with the provided key.

A boot loader could then use XTEA and decrypt the binary file before writing to flash memory.

The XTEADECODE statement can be used inside a boot loader to decrypt the encrypted blocks.

The XTEA encoder uses 32 rounds. The same as used in the xtea.lib

![notice](notice.jpg)Only the binary image is encrypted, the HEX file is not encrypted!

You can not simulate an encrypted program. Add this option when your project is ready.

See also

[$AESKEY](_aeskey.md) , [XTEAENCODE](xteaencode.md) , [XTEADECODE](xteadecode.md)

Example

NONE