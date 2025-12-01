# ARDUINO

The ARDUINO is a hardware platform based on AVR processors. ARDUINO boards/chips are programmed with a bootloader. This bootloader is the old STK500 protocol, not longer supported by Atmel in Studio. There are various programmers for ARDUINO, AVRDUDE is probably the most versatile. 

BASCOM also supports the ARDUINO/STK500 v1 protocol. the DTR/RTS lines are used to reset the board.

You can program/read flash/EEPROM but you can not read/write fuse/lock bytes. The STK500 bootloader for ARDUINO does not support this.

Under options you only need to select the programmer, and the COM port. Since an FTDI chip is used on most ARDUINO boards, this is a virtual COM port. Only present when the USB cable is connected to your PC.

Select 57600 baud for the baud rate. Older ARDUINO boards work with 19200 baud.

ARDUINO V2

The developers of the ARDUINO finally implemented the STK500V2 protocol. This protocol is supported by Atmel and of course by BASCOM.

Select the ARDUINO STK500V2 programmer in BASCOM programmer options to use this protocol.

A board like the MEGA2560 R3 uses this protocol and probably all newer AVR based ARDUINO boards will support this protocol. The baud rate should be 115200 but could be different for your board.

ARDUINO Leonardo

For some reason each arduino board seems to use a different bootloader method. The leonardo implements a virtual COM port. When opened at 1200 baud, the board resets into another virtual COM device with a different COM port number.

In BASCOM you need to chose the myAVR MK2 / AVR910 programmer since Leonardo uses the AVR910 loader from Atmel.

You need to select the COM port that you get at Boot time. The baud is 115200. 

To program, press the reset button, wait till the USB is enumerated and the Virtual COM port is ready, then press F4 to program the processor.

Using Bascom-AVR with Arduino Optiboot Bootloader (under Windows 7)

For more information on Optiboot visit following website: http://code.google.com/p/optiboot/

1.| Download AVRDUDE from http://www.nongnu.org/avrdude/  
---|---  
  
2.| Latest Windows Version (April 2012): avrdude-5.11-Patch7610-win32.zip  
---|---  
  
Complete link: http://download.savannah.gnu.org/releases/avrdude/avrdude-5.11-Patch7610-win32.zip

3.| Create a folder like c:\AVRDUDE   
---|---  
  
4.| Copy the content of avrdude-5.11-Patch7610-win32.zip in this new folder  
---|---  
  
5.| Open Bascom-AVR  
---|---  
  
6.| Click on Options >>> Programmer  
---|---  
  
7.| Choose External programmer  
---|---  
  
8.| Checkmark Use HEX file  
---|---  
  
9.| Include the path to avrdude.exe  
---|---  
  
10.| User Parameter:   
---|---  
  
-C c:\avrdude\avrdude.conf -p m328p -P com19 -c arduino -b 115200 -U flash:w:{FILE}:i

![optiboot_bascom_1](optiboot_bascom_1.png)

Explanation of Parameter:

-C 

c:\avrdude\avrdude.conf The config file tells avrdude about all the different ways it can talk to the programmer.

-p 

m328p This is just to tell it what microcontroller its programming. For example, if you are programming an Atmega328p, use m328p as the partnumber

-P 

com19 This is the communication port to use to talk to the programmer (COM19) in this case. Change it to your COM port.

-c

arduino

Here is where we specify the programmer type, if you're using an STK500 use stk500, use arduino for Optiboot

-b

115200

Set serial baudrate for programmer. Use 115200 baud for Optiboot.

-U

flash:w:{FILE}:i

You define here:

•| the memory type: flash or eeprom (this could be also hfuse, lfuse or effuse if you want to verfiy this)  
---|---  
  
•| r (read), w (write) or v (verify)  
---|---  
  
•| Use {FILE} to insert the filename {EEPROM} to insert the filename of the generated EEP file.  
---|---  
  
•| i = Intel Hex File   
---|---  
  
After clicking on the F4 (Program Chip) Button in Bascom-AVR you see the CMD window of Windows 7 until AVRDUDE is ready flashing the Arduino.

![Optiboot_bascom_2](optiboot_bascom_2.png)

Complete documentation of AVRDUDE parameters:

http://www.nongnu.org/avrdude/user-manual/avrdude_4.html#Option-Descriptions