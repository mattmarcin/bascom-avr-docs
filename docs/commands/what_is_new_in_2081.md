# What is new in 2081

\- [CONTINUE](continue.md) statement added

\- [REDO](redo.md) statement added

\- [NOP](nop.md) is now also a BASCOM BASIC statement

\- The editor supports jump to implementation : hold CTRL key and hover the mouse over an identifier. When it becomes underlined and blue you can click it with the left mouse key.

Use CTRL+BACKSPACE to jump back

\- when defining a constant named [Updateeprom](dim.md) , the eeprom will be updated. which means that the value will only be written when it differs. The value of the constant does not matter.

\- config timer1 for tiny 25/45/85 set the wrong register bits.

\- the watchdog is disabled as part of the init procedure. it is now disabled BEFORE the optional call to [init_micro](_initmicro.md) and not after as in 2079.

\- passing string constants with embedded {034} resulted in an extra (unwanted) space.

\- accessing passed string array in sub without length info, but with constant index failed.

\- [crcmb](crcmb.md) funtion added to help. (checksum for modbus)

\- for xmega [i2cstop](i2start_i2cstop__i2crbyte__i2cwbyte.md) you can define a constant named _TWI_STOP_1 or _TWI_STOP_2 to change the behavior.

\- [makemodbus](makemodbus.md)() function 1, 2 and 4 added to modbus.lib

\- support for xmega added to [getrc](getrc.md)

\- PDF download now also checks/download the BASCOM-AVR manual

\- PRINTBIN did not accept a constant for the optional channel : printbin #someconst. Fixed. 

\- [update](help_update.md) from within the application simplified. see help.

\- printbin raised error while printing multiple variables

\- simulator did not show proper hex value for single variables.

\- fusing which uses ftoa uses a table which could be loaded on a page boundary. this could lead to rampz problems. fixed.

\- [crc8UNI](crc8uni.md) added for normal crc8 CCITT

\- [config clock ](config_clock.md)additional option : highESR=1 to enable high ESR mode in xmega with 32 bit RTC

\- [FM24C64_256](fm24c64_256_xmega.md)-XMEGA.lib added for xmega. read the lib notes.

\- tcpip-w5500.lbx has been updated to support usage from boot space. See [$loader](loader.md)

\- stk500 board. osc can be set from menu

\- using [spimove](spimove.md)() inside a sub with a parameter for the count, would load the wrong data.

\- [i2cwbyte](i2start_i2cstop__i2crbyte__i2cwbyte.md) would raise an error if a multi dim array was used.

\- get/put/seek in AVR-DOS used in combination with $bigstrings would fail for numeric data

\- xmega [i2cstop](i2start_i2cstop__i2crbyte__i2cwbyte.md) has two new optional mode. See help.

\- [CONFIG SPI](config_spi.md) has a new option : EXTENDED=1 to have extended data size reading/writing.

\- support for [rgbW](config_rainbow.md) leds added (ws2812 with extra white led)

\- [CONFIG USI](config_usi.md) has a new option to support optional pins.