# CONFIG MODBUS

Action

This directive sets the MAKEMODBUS data mode.

Syntax

CONFIG MODBUS = DEFAULT | VAR

Remarks

When not configured, or when DEFAULT is chosen, the number of bytes passed in MakeModBus, is determined by the data type of the variable.

When configured to VAR, the content of the variable is used to pass the number of data bytes. The maximum value is 255.

See also

[MAKEMODBUS](makemodbus.md)

Example

Print #1 , Makemodbus(2 , 1 , 8 , X); ' slave 2, function 1, address 8 , send X byes where X is loaded with the number of bytes