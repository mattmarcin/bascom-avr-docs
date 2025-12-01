# $EEPLEAVE

Action

Instructs the compiler not to recreate or erase the EEP file.

Syntax

$EEPLEAVE

Remarks

When you want to store data in the EEPROM, and you use an external tool to create the EEP file, you can use the $EEPLEAVE directive.

Normally the EEP file will be created or erased, but this directive will not touch any existing EEP file.

Otherwise you would erase an existing EEP file, created with another tool.

See also

[$EEPROMHEX](_eepromhex.md)

Example

NONE