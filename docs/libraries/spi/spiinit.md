# SPIINIT

Action

Initiate the SPI pins.

Syntax

SPIINIT

Syntax SPI1

SPI1INIT

Remarks

After the configuration of the SPI pins, you must initialize the SPI pins to set them for the right data direction. When the pins are not used by other hardware/software, you only need to use SPIINIT once.

When the SPI bus is used in master mode, the MOSI, CLOCK and SS pins will be set to output. 

When the SPI bus is used in slave mode, the MISO is set to output mode.

If you need to change the logic levels of the SPI pins, you need to disable the SPI. You can do this by setting the SPE bit to 0 in SPCR.

When other routines change the state of the SPI pins, use SPIINIT again before using SPIIN and SPIOUT.

SPIINIT is only required for normal AVR. Xmega and Xtiny do not require this statement. 

SPIINIT always work on the first SPI interface (SPI0)

SPI1INIT works on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIOUT](spiout.md), [config spi](config_spi.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

ASM

Calls _init_spi

Example

See [SPIIN](spiin.md)