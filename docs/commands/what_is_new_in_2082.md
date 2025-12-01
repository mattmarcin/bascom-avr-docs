# What is new in 2082

\- rearranging memory order for usb support caused a bug in config clock : the date time bytes are not mapped after each other. Fixed.

\- START/STOP statements worked on the wrong register for the TINY1634

\- i2c_twi_multi lib had a problem in the readbyte function.

\- [SPIMOVE](spimove.md) added for Xmega

\- split screen did not allow copy & paste

\- USI slave support added for tiny1634

\- All DAT files are now stored in a sub folder named DAT. This means you need to copy your DAT file to this folder if you made custom DAT files.

\- some registers of tcc1 were missing in xmega D3 series

\- read only files could not be opened anymore. fixed.

\- On win10 you could get a HID error message. 

\- w5500 tcp lbx : removed RST status bit check since the bit never becomes 0 and hangs the code

\- [url2ip](url2ip.md) bug fix. one byte of the IP address could get trashed

\- url2ip added to w5500

\- new samples for w5500 wiznet chip

\- accessing a zero based array inside a sub coulld result in an index error.

\- simulator did not support writing to xmega portx_CLR _SET and TGL registers

\- using search in files function could result in 'out of bound' error.

\- [manchesterEnc](manchesterenc.md) and [manchesterDec](manchesterdec.md) functions added for manchester coding/decoding

\- assigning a byte with a string constant with spaces, resulted in 0, not 32. 

\- [VARPTR](varptr.md)() function returned &H1000 too much for Xmega ERAM data type.

\- using getadc() with 2 numeric parameters or constants like : getadc(4,&H20) would not set the right bits.

\- i2csend and i2creceive updated for xmega. after the start/slave address, the status is now checked and does not send data in case of a bus problem. this to prevent a hangup in the twi logic.

\- printing supports selection of text and page range now. you need to use print preview for this.

\- OUT instruction did not clear RAMPZ for Xmega with ROM > 64KB and normal SRAM.

\- [PS2MOUSEXY](ps2mousexy.md) accepts an additional optional parameter for mouse wheel support. Notice that you MUST download an update of the ps2 lib add on

\- config spi on non xmega did not support the extended mode for HW SPI

\- [config tcpip](config_tcpip.md) now supports SPI1 for the SPI bus

\- windows 10 DEP and ASLR support added. 

\- printbin: when using automatic rs485 and printing a long/dword constant on a chip with extended port register, R23 was trashed. Example : printbin &HABCDEF00

\- FLIP() function resulted in an error about $REGS

\- terminal emulator component is replaced in order to support windows DEP/ASLR. This means that some features from the terminal emulator have changed.

\- [printbin](printbin.md) can print a variable amount of bytes now. while ; is used to separate multiple variables, the comma can be used to specify the amount of bytes

like : printbin ar(1) , numbytes ; othervar 

this makes the syntax compatible with the old syntax. We recommend to use the new syntax

\- terminal emulator custom messages extended to 16

\- [UPDI programmer](updi_programmer.md) added for new AVR processors with UPDI interface. 

\- A table is added to [$LOADER](loader.md) with the size of maxwordbit. This constant depends on the number of flash pages.

FILE LOCATION

With DOS things were simple : all files could go in a folder and sub folder. To make a backup all you had to do was using XCOPY.

With Windows things are not so simple : files are located all over the PC. Some folders are write protected and to make a backup is not so simple.

A lot of customers are looking for the SAMPLE files. These are put in the documents folder and can be accessed using the File, Open Sample option. 

In 2082 the preferred folder for installation is C:\MCS\BASCAVR2082

But of course you are free to install in any other folder of your choice.

The samples are installed in a sub folder of the application folder too.

In the Environment Options of the IDE you can specify which folder you want to use for the sample files. 

About UPDI

The new UPDI processors have a total different architecture compared to normal AVR. In fact the differences are similar to XMEGA. For this reason we refer to these processors as XTINY since they are tiny Xmega processors.

Because of the work and support for XMEGA fresh in mind, the actual UPDI compiler/DAT support will be available very soon in a next update as an add on. 

The TINY816/817 will be the first processor to be supported.