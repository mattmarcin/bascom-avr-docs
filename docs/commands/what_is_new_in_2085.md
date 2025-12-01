# What is new in 2085

version 2085.003(beta 3)

\- getadc() checks data type for xmega/xtiny. data type should be integer/word

\- $SIM -> _SIM was not properly colored when using 'show excluded code' option

\- simulator gave overflow error when kept running for a long time. 

\- simulator dual port registers support added. this means that using virtual ports will update correctly the normal registers

\- [join](join.md)() function added as counter part of [Split](split.md)() function

\- [lookdown](lookdown.md)() support added for dword/long

version 2085.002(beta2)

\- movw code replaced by mov when the processor does not have the movw instruction. only applies to old processors

\- xtiny platform config SPIx has an additional option SPIPIN to specify which port pins must be used for the SPI bus

\- since some xtiny(megaX,AVRX) have multiple SPI, config SPI1 is added to configure the second SPI bus. This works for SPI1IN, SPI1OUT, SPI1MOVE.

\- mid function and mid statement rewritten. the start position is not simply added but checked so it can not be placed beyond the end of the string

use the byte variant to terminate the string like : mid(somestring,index)=0.

\- Both [MID](mid.md) statement and function support $bigstrings

\- instr() function updated to be more safe. since you can specify an offset, this offset is checked so it will not read beyond the string.

\- [space](space.md)() and [string](string.md)() functions moved to mcs.lib and also added support for $bigstrings

\- [delchar](delchar.md)/[insertchar](insertchar.md) support [$bigstrings](bigstrings.md)

\- [bascomp](bascomp.md) utility updated

version 2085.001 (beta1)

This is an updated to support the DB series.

\- make sure to read about PRESERVE and OVERWRITE in the [CONFIG](config.md) options.

\- lcd_i2c_PCF8574.LIB updated version included. 

\- mega16M1,32M1 and 64M1 corrected for LIN/USART

\- rainbow libs rolled back. the automatic platform code had the disadvantage of requiring a call instead of rcall

\- font editor fixed. The width of the font was not properly saved when it wasn't a multiple of 8.

\- various fonts changed in IDE. There is also a new option to override the windows system settings. 

\- m48pb dat file modified. DDRE entry was invalid

\- a number of icons are changed. Also new bigger icons included which can be selected in the options. This is intended for high resolution DPI. The icons are still in the ICO format however which mean that they do not scale perfect as SVG would do. This is in the works as well.

\- DB/[AVRX](avrx.md) support. The xtiny add on is required. You need to update the add on lib.