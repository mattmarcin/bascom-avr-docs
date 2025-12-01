# M128-1wire-PortF

This user contributed library is only for the atmega128 when 1wire is used on PORTF.

Normally the port registers DDR, PORT and PIN are grouped and this is used to work with pointers.

PORTF is however incompatible since it is grouped different. This library uses fixed addresses.

\- When using this library you can not use 1wire devices on other ports. This because this lib overloads the default library.

\- The EXTENDED=1 option from [CONFIG 1WIRE](config_1wire.md) may not be used in combination with this library.