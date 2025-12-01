# $AESKEY

Action

This directive accepts a 16 byte AES key and informs the compiler to encrypt the binary image.

Syntax

$AESKEY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

Remarks

$AESKEY accepts 16 parameters. These are the 16 bytes which form a 128 bit key.

When your code is compiled, the resulting binary code will be encrypted with the provided key.

A boot loader could then use AES and decrypt the binary file before writing to flash memory.

![notice](notice.jpg)Only the binary image is encrypted, the HEX file is not encrypted!

You can not simulate an encrypted program. Add this option when your project is ready.

See also

[$XTEAKEY](xteakey.md) , [AESENCRYPT](aesencrypt.md) , [AESDECRYPT](aesdecrypt.md)

Example

See the Samples\boot\xmega_dos_boot_AES.zip , an Xmega boot loader with AES decryption.