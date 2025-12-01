# ATTINY20

The ATTINY20 is a 14 pins AVR chip. It has NO EEPROM. It also does not have a UART.

The TWI slave interface is not compatible with TWI found in other AVR chips.

The chip has a PDI programming interface and does not support ISP or JTAG.

The watchdog is also different compared to other AVR chips. It is using a CCP register which is similar as the Xmega.

The processor also only has 16 registers (R16-R31) and is missing registers R0-R15.

This does not make the chip a good choice for using with BASCOM since BASCOM uses the lower registers as well.

![attiny20](attiny20.png)