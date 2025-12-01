# What is new in 2086

\- config sections are also grouped for code collapse

\- toggle code improved for word,int,long. Also bug fixed when toggle as used on a port with constant like porta.pd3

\- spi1move and spimove for xtiny using manual SS setting would set DDR instead of PORT register

\- SW UART Inkey, Input, Waitkey revised for $timeout. $timeout maximum value is &HFF_FF_FF. Input will end when one of the incoming characters times out. 

\- attiny861 , START TIMER did actual stop the timer since the wrong value was written. 

\- buffered serial port changed. since a global variable is used for the buffer count, the interrupts are disabled and reenabled during updating this variable. but users that use the BYTEMATCH option in combination with serial input code

like input, inputbin, etc. autmatic enable the interrupts since reading disable/enables global interrupts. this can lead to problems. it is not good practice to read data from the interrupt but since many users seems to use this

we changed the CLI/SEI so that the I-flag is restored and thus global ints are not enabled by reading inside the ISR. 

\- using rnd() with config rnd=32 on a word/integer result in an internal variable error

### CODE BREAKING CHANGE ###

\- [config comx](configcomx.md) TXPIN becomes TX_RX_XC_XD_PIN. This better reflects that all pins belonging to the USART will have an alternative pin value

This only breaks old code when the TXPIN option was used. 

#########################

\- config comx for xtiny platform has a new option : TX=DISABLED|ENABLED and RX=ENABLED|DISABLED by default both TX and RX are enabled. but you can disable the Transmitter or Receiver

\- M324PBdef.dat updated to support second TWI channel. See also the M324PB sample.

\- included fonts for graphical LCD are now word aligned. this in case the user uses multiple END statements.

\- drivers(libs) updated that were unsafe when using port pins on an extended address. 

\- I2C_TWI-MULTI.lib : i2cstop missed setup call to _i2c_chan_setup when CONST _TWI_STOP_TIMEOUT was not defined resulting in a hang up

\- AVR-DOS updated for xtiny and added sample files : FlashCard-demo-XTINY.bas , Config_MMCSD_HC_XTINY.inc , CONFIG_AVR-DOS.inc. See also the AVR-DOS topic description for a sample.

\- bootloader added for megax : BootLoader-MegaX.bas the file m4808-tca0-BOOT.bas can be used to load the demo which uses [$romstart](_romstart.md). See also [Using a BOOTLOADER](using_a_bootloader.md)

\- dim SAFE changed see help

\- val() to a double for a string with leading + would result in NAN.

\- decr/incr did not protect variables dimmed with SAFE 

\- editor multi search highlight and multi selection highlight added. See [Options Environment](options_environment.md)

\- com5 and com5 buffered output for xtiny bug fixed where there was a double label used.

\- RTF export now capitalizes IO registers, just as they appear on screen.

\- simulator now uses a separate register space. old AVR, xmega and xtiny have different memory maps. while older AVR can reach the registers by a pointer, the xmega and xtiny can not do so.

while desgning the simulator there was one memory area. but it turned out that some instructions writing to registers, actually wrote to lower IO space. So this has been rewritten.

This means that a lot of the simulation code has been changed. Please report any simulation bug to support.

\- config dmxslave support added for xtiny platform

\- xtiny buffered serial input for com5 and com6 gave a duplicate label error

\- some programmers like stk200,stk300, kamprog had no icon any longer in the toolbar. and the chosen size was not working either.

\- clearing history in search box did not work properly(right mouse button)

\- config tcpip for w5500 supports xtiny

\- CLS in $ASM block mistaken as BASIC CLS

\- shiftout number_of_bits would not accept a local/param

\- buffered serial output com5 for xmega caused an error

\- [dcf77](configdcf77.md) xtiny support added for timer TCA0

\- user EDC had a great idea about notification of usb-serial ports. you are notified with an alert window when a CDC is added or removed

\- $programmer extended with constants for programmers and additional COM parameter. prog.inc contains the constants for the programmers

\- [writedac](writedac.md) statement added for xtiny platform

\- simulator usart emulation added for xtiny platform

\- baud statement implemented for Xtiny

\- [getrc5](getrc5.md) xtiny support, also background mode added for TCBx. check config-rc5 in the help and the avrx128da28-RC5-Background-send-receive.bas example

\- [rc5send](rc5send.md) xtiny support, check config rc5send

\- config tca0 splitmode fixed. see also the example. this also requires an update of all DAT files.

\- $romstart number of bugs in simulator fixed (elpm, lpm)

\- Baud statement improved. it did not support channels for a HW UART. it will also raise an error when you try to use non existing channels.

\- [FM24C64_256-XMEGA](fm24c64_256_xmega.md).lib support for strings added.

\- UPDI addon support for more processors : mega808,1608 and 3208. also added 64DB32,128DB32,128DA48,128DA32,32DA48,64DA64,128DA28

\- [updi programmer](updi_programmer.md) enhanced, it works up to 1.6 Mbaud now. not all processors support this. See help. Also added unlock chip function.

also added lockbit table to DA/DB series. these platforms use a 4 byte ID to lock.

updi can use DTR/RTS for switching data and/or a 12V pulse. 12V pulse is used to access UPDI when the updi/reset are shared and the pin is programmed for reset function. 

\- tcpip w5500 corrected a bug for xmega with > 64KB processors. mixing tcpwrite and tcpwritestr could result in sram accessing a wrong page.

\- some checks added for string assignment/passing byval. when constants are used that are too big you get an error. you also get an error when you claim more temp memory than specified with $framesize. 

see also the help for error 406. The option need to be turned on using CONFIG STRCHECK=ON

\- string to double conversion with string in scientific notation conversion bug fixed when there was a leading minus. also added support for the bigger xtinies.

\- some scaling problems fixed. 

\- DB/DA series use a different method for the UPDI fuse/eeprom/signature writing. This is corrected.

\- xtiny with 128 SRAM did not simulate correct. Also the MSB of pointers were not set since normal AVR do not need this for 128 SRAM chips. 

since xtiny has a different memory model this lead to memory bugs

\- optimization did not recognize flag registers. code like : portf_flags = portf_flags would not be executed. 

\- kamprog icons were not visible due to a change in icons

\- writing a constant to an eeprom string on a normal AVR would fail

\- closing bascom with programmer window open produced an access error

\- lib manager can add a routine from the clipboard

\- int_trig.lib 64K boundary bug fixed (qsin/qcos)

\- xtiny/megaX dat files had ADC value exchanged for 8bit/10bit resolution selection

\- mcusr register was not properly cleared at start up for old AVR processors. only the WD flag was reset, notice you should not write a 0, since some AVR have other unrelated bit flags in the MCUSR register!

processors like that will have an additional mask in the dat file : WD=MCUCSR.WDRF,$E0

\- assigning a hex number to a double did not work for all numbers

\- waitkey() for the software uart did not support timeout.

\- [View Show Alert Window](viewalertwindow.md)