# $EEPROMSIZE

Action

Instruct the compiler to override the EEPROM size of the micro processor.

Syntax

$EEPROMSIZE = size

size | The size in bytes of the EEPROM.   
---|---  
  
Remarks

The AVR has build in EEPROM. With the WRITEEEPROM and READEEPROM statements, you can write and read to the EEPROM. You can also use the ERAM pseudo variables to read/write EEPROM.

When you use an external EEPROM and an alternative EEPROM library such as FM24C16 or FM25C256 you can override the internal EEPROM. All EEPROM routines will use the external EEPROM then. This way you are able to use a bigger EEPROM than internal available. Or you can use a quicker EEPROM such as a RAMTRON FRAM EEPROM. These EEPROM's are as quick as SRAM and also can be written to almost unlimited times. 

![notice](notice.jpg) When using an external EEPROM and $EEPROMSIZE , take care that the supported programmers can not write to this EEPROM. They assume the internal EEPROM.

See also

[FM24C16](fm24c16.md), [FM25C256](fm25c256.md)

Example

$eepromsize = &H8000