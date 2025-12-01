# Program Reset Chip

This menu options will let the programmer reset the processor.

Shortcut : SHIFT+F4

The MCS UPDI programmer will perform a reset using UPDI protocol. It could be done using a DTR or RTS pin from the serial port but using UPDI has the advantage that you can program the RESET pin to be used as a normal IO pin. That is important on processors that do not have a dedicated RESET pin.