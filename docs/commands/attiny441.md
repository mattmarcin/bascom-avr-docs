# ATTINY441

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

The Tiny441 has 256 bytes of EEPROM memory.

Usually this means that the high byte EEPROM address register is missing since it has no purpose.

The tiny441 however has an EEARH register. And it seems to cause problems.

The data sheet says :

Devices with 256 bytes of EEPROM, or less, do not require a high address registers (EEARH). In such devices the high

address register is therefore left out but, for compatibility issues, the remaining register is still referred to as the low byte

of the EEPROM address register (EEARL).

Devices that to do not fill an entire address byte, i.e. devices with an EEPROM size not equal to 256, implement readonly

bits in the unused locations. Unused bits are located in the most significant end of the address register and they

always read zero.

The bascom write/read EEPROM code checks if the EEPROM size > 256\. If that is the case, the EEARH is addressed.

But in this case this register is not touched. 

When you have problems, set EEARH register to 0 in your code.

While we could always write this register, it is a waste of code. 

When having problems contact support. 

![attiny441_841](attiny441_841.png)