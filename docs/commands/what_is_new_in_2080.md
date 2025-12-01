# What is new in 2080

\- [tiny461](attiny461.md) and [tiny861](attiny861.md) only did set pcie0 when you enable the PCINT because there is just one interrupt in the chip. In 2080, both PCIE0 and PCIE1 are enabled/disabled.

\- added m48PB, m88PB, 168PB and m328PB dat files.

\- new Rainbow functions : [RB_Color](rb_color.md) and [RB_Copy](rb_copy.md) added by Galahat

\- simulator did not show maximum values of DWORD correct.

\- [RB_GETCOLOR](rb_getcolor.md) and [RB_LOOKUPCOLOR](rb_lookupcolor.md) functions did return false result when index was a variable.

\- some font problems solved.

\- simulator could crash for xmega processors.

\- when using non-mono font like Arial, text selection does not work properly. Use a font like CONSOLAS.

\- Added option 'Use Monofont' for backwards compatibility

\- Some new atmel PDF files could not be loaded with the PDF viewer. Viewer is rewritten and requires a new DLL named BASPDF.DLL

\- [getadc](getadc.md)() on m640.m1280/m2560 or any other processor with 6 mux bits did not set mux5 bit for getadc(32) and higher.

\- generic byte [compare](compare.md)() function added, based on code and idea from MWS. (Magic White Smoke)

\- varexist() did not support ALIAS. 

\- XMega64A1-SRAM 4-Port-Sample.bas sample added for setup EBI 4 port on XMega. See also [Adding XRAM to XMEGA using EBI](adding_sram_4_port_non_multipl.md)

\- when bascom-avr.xml options file exists in the bascom application folder, that option file will be used.

\- [format](format.md) is extended to use a variable for the mask.

\- [config xpin](config_xpin.md) did not support alias for the pin.

\- [bufspace](bufspace.md)() did not support UART 5-8

\- [INSERTCHAR](insertchar.md) and [DELCHAR](delchar.md) use Z pointer which must be cleared for XMEGA. fixed in mcs.lib

\- programmer did not fetch correct chip from editor when code was not saved. this would give a chip mismatch.

\- assigning a negative value to a dword did not throw an error.

\- [code explorer](view_code_explorer.md) can show estimated stack usage. 

\- higher standard baud rates added to terminal emulator

\- added support for EDMA in xmega8/16/32 E5. See [config EDMA](config_edma.md)

\- [version](version.md)() function did not append to string but would overwrite existing string data. 

\- [right](right.md)() adds an additional null byte when a numeric constant is used for the number of characters to copy.

\- new [dim](dim.md) option to specify multiple items : dim a,b,c,d as byte failed when using multiple indexed items.

\- all dat files updated with CONFIG information.

\- printing values from multi index variables failed : print index(index1,index2)

\- m1284pdef.dat updated with missing TIFR3 register.

\- more fonts in various sizes from Adam Siwek.

\- [power()](power.md) function for doubles did not work correct when assigned to a function

\- some new atmel PDF files can not be loaded with the PDF viewer. Viewer is rewritten.

\- SSD1306 i2c oled driver updated for Xmega.

\- m649A and m649P dat files added.

\- [LCDFONT](lcdfont.md) prm, added. prm selects the font table (0-3) of a text LCD.

\- [CONFIG POWER_REDUCTION](config_power_reduction.md) set register to 0 in some conditions. Also added LCD and other new Xmega power reduction options.

\- CONFIG OSC extended with calibration register settings and DFLL.

\- val() for doubles has a bug for XMega >64KB chips

\- added [flip](flip2.md)(byte) function to mirror bits in a byte

\- xmega128B3 dat file added

\- [readsig](readsig.md) also works for normal AVR processors.

\- inputbin and printbin load 1 element too many with arrays using base 0.

\- [config inputbin](config_inputbin.md) added to allow reading packets of up to 64 KB

\- added support for LCD text OLED RS0010 lcd4_anypin_oled_RS0010.lib 

\- [FT81x](ft800.md) support added

\- [M324PB](atmega324pb.md) dat file added.

\- [I2CINIT](i2cinit.md) enhanced for multiple TWI

\- [I2C_TWI-MULTI.lib](i2c_twi_multi.md) added to support multiple TWI busses.

\- second SPI on m328PB added : [INIT1SPI](spi1init_spi1in_spi1out_spi1mo.md), SPI1OUT, SPI1MOVE, SPI1IN

\- user donated library [I2C DOGS104](lcd_dogs104a_i2c.md) driver, SSD1803A included.

\- [URL2IP](url2ip.md)(url) function added to W5100 to do DNS lookup using google DNS server

\- when defining a const [Updateeprom](writeeeprom.md) , the eeprom will be updated. which means that the value will only be written when it differs

\- [BASE64ENC](base64enc.md) and [BASE64DEC](base64dec.md) can work on byte arrays too.

2017, 2080 release

\- [SGN](settcpregs.md) extended to byte, integer, word, dword and long

\- [LOADLABEL](loadlabel.md) assigns a 24 bit address when used with a DWORD

\- CTRL+SPACE for code help.