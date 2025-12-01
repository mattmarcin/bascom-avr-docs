# What is new in 2078-2079

Beta version 2079

\- Support for WS2812 RGB led : [CONFIG RAINBOW](config_rainbow.md). This is the rainbow lib from Galahat, see : <http://bascom-forum.de/mediawiki/index.php/Rainbow_Lib>

\- [SETATTR](setattr.md) and [CLEARATTR](clearattr.md) added to AVR-DOS, by Josef.

\- shift & rotate left/right did not work for xmega port registers

\- IDE : improved speed for showing deadcode/unused variables

\- IDE : stacktrace speed up. big projects made the stacktrace slow.

\- included FT801 support. See [CONFIG FT800](config_ft800.md). Notice that the INC files have been renamed into FT80x

\- fixed attiny261,461 and 861 interrupt entries. this chip has only 1 pcint.

\- added check when [$loadersize](loadersize.md) and [$boot](_boot.md) are combined.

\- [Dim](dim.md) supports a list ; dim a,b,c,d as byte. It also supports identifiers like %,#,& and !

\- Font Editor plugin is replaced by integrated Font Editor: [Tools, Font Editor](tools_font_editor.md)

\- Sample added for [USI Slave lib](i2c_usi_slave.md)

\- fonts contributed by Adam Siwek included. You can find them in the Samples\LCDgraph\Fonts folder.

\- [report](program_show_result.md) can be opened in IDE as text file.

\- [mySmartUSB light](mysmartusb_light.md) programmer support added.

\- support added for [W5500](config_tcpip.md) tcp/ip chip

\- W5500 [socketconnect](socketconnect.md) has a 4-th parameter : nowait. When you make it 1, there is no wait for connection.

\- [$ROMSTART](_romstart.md) added : $romstart = &H8000 , will let the code start at &H8000. Default is 0.

\- jtag ice mkII programmer new firmware 7.26 from AVR studio resulted in signoff problem. Workaround implemented.

\- editor can show unused code in conditional compilation. [Edit, Show Excluded Code](edit_show_excluded_code.md) menu option.

\- usbasp programmer updated. chosen clock frequency will work.

\- makemodbus() did not support locals/passed parameters properly.

\- [crc16](crc16.md) can now directly read a range from eeprom memory to calculate a checksum for you. To enable it, just add const CRC16_EEPROM=1 to the beginning of your code.

\- simulator fix for xmega low IO registers. registers were simulated with a 32 byte offset as in plain AVR.

\- [config lcd ](config_lcd.md)has 2 new options : BEFORE and AFTER. with a parameter value of 1 a sub will be called _lcdBefore and _lcdAfter

just before the LCD is used. This allows for example to turn off interrupts when executing LCD code.

Only text LCD is supported.

\- [getadc](getadc.md)() when used on normal AVR with offset parameter, and both parameters numeric will give an error when MUX5 bit must be set.

Use getadc() with just the channel parameter.

\- multi dim arrays, added ERAM byte support, and used registers are saved now.

\- saving programming buffer as HEX file created wrong HEX files which would not load in AVR Studio. This would occur for chips with multiple segments like xmega128 

\- Full [Kamprog](kamprog_for_avr.md) support added.

\- multi dim arrays had no check on invalid index value (non dimmed)

\- using a constant float without leading 0 resulted in an error message : var= var + .12344

\- INPUT did not support DWORD. 

\- added user definable command buttons to [terminal emulator](tools_terminal_emulator.md).

\- using {} in constants was not working as expected : Const Cmd_suffix_ver1 = Asc( "{013}") was not interpreted as 13 but 123 (the { sign)

\- changed [PDF download](tools_pdf_update.md) from HTTP to FTP. This is quicker and better for the load of the server. PORT 211 is used for FTP. So you need to have port 211 open on your firewall. 

\- atxmega128c3 added. 

\- [FT800](ft800.md), vertex2ii , the X is clipped. Change call in sub vertex2II into Cmd32 _vertex2ii(___wtmpb , R18 , R17 , R16)

\- support for [EADOGXL240-7 I2C](glcdeadogmxl240_7_i2c.md) added, see eadogxl240-7.bas. This is a customer sponsored lib.

\- added support for [SSD1306 I2C](glcddssd1306_i2c.md) OLED, see SSD1306-I2C.BAS. 

\- i2c multi bus lib did not clear ERR bit correctly. 

\- when a multi dim array is only used within sub/functions and submode=new is used, an error was raised since the index table was not written at that stage. 

\- multi dim arrays can only be used to read/assign variables. Using them in functions and statements will not work. 

\- [str](str.md)() can have an optional parameter to specify the amount of digits. This works for double, but now also for singles. 

\- [MOD](mod.md) for singles changed in fp_trig.lib so it uses the same algorithm as excel/VBA.

\- FOR..NEXT with WORD data type and STEP with values other than 1 failed : for w=1 to 10 step 2 

\- when opening a single file in non-project mode, the code explorer does not get updated until you set the cursor on the code.

This also resulted in not updating the pinout viewer. 

\- R0-R31 internal variables are now exposed as byte variables. This is simpler than using getreg/setreg. 

\- added option to skip eeprom cell test. This allows to write all FF to the EEPROM whithout erasing the chip. 

\- terminal emulator font color could not be selected from the font dialog. 

\- various programmers : added chip name to info panel when chip does not match. no match will result in a red font, a match will show in green. 

\- added an error message when $hwstack,$swstack and $framesize are missing from the source. Also put back compatibility to 2077 when these directives are not specified. 

\- hovering the indention line will show the begin of the structure in the tool tip (just try it).

\- [Terminal emulator](tools_terminal_emulator.md) has 8 user definable buttons

\- [SEROUT](serout.md) defaults to CONST SEROUT_EXTPULL=1 to be in Hi-Z mode. In this mode a pull up resistor is required. To use PORT output mode, set the constant to 0 : CONST SEROUT_EXTPULL=0

2.0.7.8.001 public release

\- changing a bit on a passed array inside a sub/function gave a bit index error. 

\- while moving all single FP code to fp_trig.lib, some double (but WRONG) functions were moved to the top. It causes various problems.

\- clear buffer did not reset the RST pin in case CTS/RTS was used. 

\- val()/asc2float contained a bug for converting big values not fitting into the mantissa. The exponent was not increased. 

\- [asc](asc.md)() can have an additional index parameter : byte=Asc(string|string constant[,index]). Use this instead of asc(mid( 

\- user functions/subs can have a custom color 

\- added support for i2c lcd display RX1602A5. Use : config lcd = 16x2 , chipset = st7032. See sample LCD-RX1602A5.bas

\- using overlay pointing to a string array resulted in a wrong overlay address. 

\- additional XTEA2.LIB added. This lib complies with the original standard. 

\- Tab order can be changed with drag and drop. 

\- USI master TWI mode added. 

\- when config submode=new was used, the syntax check could give false errors. 

\- mkII programmer would give a warning about chip mismatch when atmel chip ID was the same. 

\- pulsein.lib was missing from distribution. 

\- documented beta switches [$NOTYPECHECK](notypecheck.md), [$TYPECHECK](typecheck.md) and [$REDUCEIVR](reduceivr.md)

\- when using a serial boot loader compiled with an older version, and when calling it from code (not after a reset) you need to reset the u2x flag in ucsrxA.

Or you can compile both the bootloader and main code with the new version. When you want the old behaviour, you can remark the u2x constant in the dat file. 

\- FLIP programmer will not erase EEPROM anymore. 

\- use ALT key to select blocks of text in the editor. 

\- hint window location fixed for multi monitors systems. 

\- [rgb8to16](rgb8to16.md)() function added to convert RGB8 to RGB16. 

\- xmega, config OSC : when using external osc, the oscillator ready test was not working properly. enable the internal osc as a workaround in 2077. fixed in this release.

\- arduino leonardo can be programmed with myAVR MK2/AVR910. You need to give a manual reset before pressing F4. 

\- attiny87 dat file contained an error : INTADR = 1 ; it was 2 but must be 1 

\- xmega spi length parameter supported globals only. now it supports locals and parameters as well. 

\- syntax check gave errors when config submode=new was used in some cases. 

\- 1wirecount returned with ERR set, even when sensors were found. 

\- [simulator](program_simulate.md) has trace log option to dump all executed lines to a file. 

\- error list content can be copied to clipboard with right mouse popup menu 

\- xmega uarts 5-8 serial buffered output enable the wrong uart. 

\- indention line colors can be customized. 

\- [proper indent ](edit_proper_indent.md)will not indent comment 

\- [getkbd](getkbd.md)() required change for xmega. (xmega does not use port register for pull up) 

\- added dword support to lookup() 

\- [config rnd](config_rnd.md)=16|32 added to support bigger random numbers. 

\- attiny441 stk500 settings changed. attiny441 and attiny841 verified with real chips. some mods made to the dat files. 

\- increased internal constant string storage length to 1024. for cases like : s="some very long constant". previously the max size was 256. 

\- xmegaE5 timers 4/5 support added. 

\- xmegaE timer4/5 OVF bit need a manual reset, writing a 1 to intflags register. it is not cleared automatically. 

\- xm128a1U dat file added 

\- code folding added to editor. Press F11 to fold a sub/function 

\- all project files can be placed in an [archive](file_zip.md) (zip) file. 

\- AVR-DOS, GET and PUT support [$bigstrings](bigstrings.md)

\- [$boot](_boot.md) extended to support >64KB processors. $boot can be used together with $inc to include a boot loader in your code. 

\- FM25C256 example with BMA.bas sample added which demons xmega ramtron lib with shared bus. 

\- baudX=value added for Xmega. This will change the baud rate on an xmega at run time. 

\- special multi bus i2c added for normal AVR processors. See [config i2cbus](config_i2cbus.md). 

\- muli dimensional array support added like : dim ar(10,50,3,5,2). 

\- long/dword data types added to SORT statement. 

\- report extended with bit position in memory and length of dimensioned strings 

\- [Lookup](lookup.md) supports a numeric variable too for the label : novar = LOOKUP( value, label|address). 

\- soft spi supports DATA ORDER LSB and MSB 

\- [str](str.md)() second optional parameter added to help. It specifies number of digits after the DP. Only for doubles. 

\- m324/m164/m644/m1280 config timer0, disconnect option fixed. 

\- settings xml file can be passed as parameter to allow different settings files and versions. 

\- added option to show invisible characters. 

\- added support for DWORD to [SWAP](swap.md)

\- added insertionsort.bas sample 

\- m64C1 and M32C1 dat files added. 

\- History Backup option added : it will create a unique copy of the source file each time you save a file. 

\- code explorer can show INC files under their own branch ([options, environment, IDE](options_environment.md))

\- [Qsin](qsin.md) and [Qcos](qcos.md) integer trig added.