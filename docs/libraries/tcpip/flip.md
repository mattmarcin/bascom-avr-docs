# FLIP

FLIP is a free USB bootloader from Atmel. With FLIP you can program an AVR without additional (ISP) programmer hardware.

Because it is a USB bootloader it only work with AVR with built in USB functionality.

FLIP is supported by the BASCOM-IDE so you can use it direct by pressing the Program Chip (F4) button and download a HEX file.

FLIP can be downloaded from the Atmel site.

Search for "FLIP bootloader" on the Atmel Website for the latest version: <https://www.microchip.com/developmenttools/ProductDetails/flip>

[ ](<http://www.atmel.com>)

1.| Download FLIP from Atmel Website  
---|---  
  
2.| Install FLIP  
---|---  
  
3.| In BASCOM-IDE Select FLIP from Options >>> Programmer , in order to program quickly without the FLIP executable  
---|---  
  
4.| Now you can press Program Chip (F4) to program the HEX file into the chip  
---|---  
  
As with other programmers, you press F4 to program the HEX file into the chip. A small window will become visible.

A number of dialogs are possible:

![flip_error_wrongdevice](flip_error_wrongdevice.png)

In this case, you try to program a chip which is not supported by FLIP. The Mega88 is not an USB chip so the error makes sense.

If you are using an USB AVR you could get following dialog box:

This dialog informs you about a missing DFU device and/or the device is not in boot loader mode:

![flip_reset](flip_reset.png)

In this case, the boot loader is not found. You can run the boot loader by following the sequence from the dialog box.

In order to make this work, the HWB (Hardware Bootloader Button) and RST (Reset Button) input both need a small switch to ground.

When HWB is pressed(low) during a reset, the boot loader will be executed. 

Abbreviations:

â¢ ISP: In-system programming

â¢ RST: Rest

â¢ USB: Universal serial bus

â¢ DFU: Device firmware upgrade

â¢ FLIP: Flexible in-system programmer

FAQ - Using FLIP with XMEGA-A3BU Xplained Board from Atmel (under Windows 7 32-Bit)

1.| Read Atmel App Note: [AVR1916](<http://www.atmel.com/dyn/resources/prod_documents/doc8429.pdf>): USB DFU Boot Loader for XMEGA   
---|---  
  
2.| Download FLIP  
---|---  
  
3.| Install FLIP 3.4.5 or higher for Windows (Java Runtime Environment included)  
---|---  
  
4.| Connect the USB Cable during pressing Switch0 SW0 (Hardware Bootloader button) on the XMEGA-A3BU Xplained board  
---|---  
  
5.| The USB Driver can be found in the FLIP Software directory (e.g.: C:\Program Files\Atmel\Flip 3.4.5\usb)  
---|---  
  
6.| You can also search for DFU ATXMEGA256A3BU in the Windows 7 device manager and reinstall the driver by pointing it to this directory (e.g.: C:\Program Files\Atmel\Flip 3.4.5\usb)  
---|---  
  
7.| Then you will find this here in the device manager Atmel USB Devices >>>> ATxmega256A3BU  
---|---  
  
8.| In BASCOM-IDE Select FLIP from Options >>> Programmer , in order to program quickly without the FLIP executable  
---|---  
  
9.|  Now you can press Program Chip (F4) to program the HEX file into the chip  
---|---  
  
If you see following dialog: 

![flip_reset](flip_reset.png)

Just connect the USB Cable during pressing Switch0 SW0 on the XMEGA-A3BU Xplained board

Hit OK button then the XMEGA will be programmed.

First example for XMEGA-A3BU board:

  
  
```vb
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
Config Osc = Enabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
  
Config Porte.4 = Output  
```
Backlight Alias Porte.4 'LCD Backlight  
  
Config Portr.0 = Output  
Led0 Alias Portr.0 'LED 0  
  
  
Config Portr.1 = Output  
Led1 Alias Portr.1 'LED 1  
  
  
```vb
Do  
  
Waitms 500  
Reset Led0  
Set Led1  
  
  
  
Waitms 500  
Set Led0  
Reset Led1  
  
  
Loop  
  
End 'end program

```
FAQ - FLIP with BASCOM-IDE 

On former versions like FLIP 3.3.1 there was on VISTA a problem with loading some of the FLIP DLL's. 

In case you get an error, copy the FLIP DLL's to the BASCOM application directory.

You need to copy the following files :

•| atjniisp.dll  
---|---  
  
•| AtLibUsbDfu.dll  
---|---  
  
•| msvcp60.dll  
---|---  
  
•| msvcrt.dll  
---|---  
  
You can also create a command file for that task like: flipDLLcopy.cmd to copy these files.

The content of the command file :

copy "c:\program files\atmel\flip 3.3.1\bin\atjniisp.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\AtLibUsbDfu.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\msvcp60.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\msvcrt.dll" .

pause

The last line pauses so you can view the result. Notice the . (dot) that will copy the file to the current directory, which is the reason that you need to run this file from the BASCOM application directory.

You also need to adapt the version of FLIP in the command file.

In order to use BASCOM's FLIP support, you must have running FLIP successfully first !

Here is a good tip from a user :

IMO he Flip 3.3.1 Installer is a little bit stupid.

The dll´s are located in the Path ...\Atmel\Flip 3.3.1\bin .

The Installer has set a correct Path-Variable in Windows for this path.

But, the libusb0.dll isn´t in that location. It is in ...\Atmel\Flip 3.3.1\USB !

So I moved the libusb0.dll into the \bin dir and Flip runs without the errors. (GRRRR)

In the ...\Atmel\Flip 3.3.1\USB dir I have also detected the missing .inf File.

After installing this, Windows detects the AT90USB162 and Flip can connect the device.