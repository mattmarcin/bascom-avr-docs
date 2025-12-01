# $EEPROMHEX

Action

Instruct the compiler to store the data in the EEP file in Intel HEX format instead of binary format.

Syntax

$EEPROMHEX

Remarks

The AVR has build in EEPROM. With the WRITEEEPROM and READEEPROM statements, you can write and read to the EEPROM.

To store information in the EEPROM, you can add DATA lines to your program that hold the data that must be stored in the EEPROM. $EEPROM must be used to create a EEP file that holds the data.

The EEP file is by default a binary file. When you use the STK500 you need an Intel HEX file. Use $EEPROMHEX to create an Intel Hex EEP file.

![notice](notice.jpg) $EEPROMHEX must be used together with $EEPROM. 

See also

[$EEPROMLEAVE](_eepleave.md)

Example

$eeprom'the following DATA lines data will go to the EEP file

Data 200 , 100,50

$data

This would create an EEP file of 3 bytes. With the values 200,100 and 50.

Add $eepromhex in order to create an Intel Hex file.

This is how the EEP file content looks when using $eepromhex

:0A00000001020304050A141E283251

:00000001FF