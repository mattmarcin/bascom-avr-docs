# $LOADER

Action

Instruct the compiler to create a boot loader at the specified address.

Can be used for all AVR that support a boot loader like ATMEGA and ATXMEGA chips.

Syntax

$LOADER = address [,BOOTONLY]

Remarks

address | The address where the boot loader is located. You can find this address in the data sheet.  In version 2081 a constant named _LOADER_PAGE is created that holds the 64 KB page number.   
---|---  
BOOTONLY | Normally when the BIN and HEX files are created, they are an image of the processor flash memory. The BOOTONLY option will write only the code for the BOOT area to the BIN file. This option has no effect on the HEX file. Writing just the boot portion to a binary file allows to include the boot loader code using the $INC directive to a normal program.   
  
A lot of AVR microcontrollers are configured such that it is possible to use a boot

loader able to receive firmware updates and to reprogram the Flash memory on

demand. 

These AVR which support boot loader have a so called boot section. 

Normally a chip will start at address 0 when it resets. 

This is also called the reset vector.

Chips that have a boot section, split the flash memory in two parts. The boot section is a small part of the normal flash and by setting a fuse bit you select that the chip runs code at the boot sector when it resets instead of the normal reset vector.

The Program Flash memory space of ATXMEGA chips is also divided into Application and Boot sections. Both sections

have dedicated Lock Bits for setting restrictions on write or read/write operations.

ATXMEGA Program Flash memory parts:

1.| Application Section for application code  
---|---  
  
2.| Application Table Section for application code or data storage  
---|---  
  
3.| Boot Section for application code or bootloader code  
---|---  
  
![notice](notice.jpg)You need to set the fuse bits so the chip jump to the boot loader address at reset (BOOTRST) ! 

Some chips also have fuse bits to select the size of the boot loader (e.g. 1024 words, 2048 words, 4096 words)

The boot loader start address depends also on the boot size.

You can find following information in the data sheet of the device (example for ATMEGA644):

Boot Size | Boot Loader Flash Section | Boot Reset Address (Start Boot Loader Section)  
---|---|---  
512 words | 0x7E00 - 0x7FFF | $loader = $7E00  
1024 words | 0x7C00 - 0x7FFF | $loader = $7C00  
2048 words | 0x7800 - 0x7FFF | $loader = $7800  
4096 words | 0x7000 - 0x7FFF | $loader = $7000  
  
For ATXMEGA chips like ATXMEGA32A4 the boot section is part of the Flash Program Memory.

You can find following information in the data sheet of the ATXMEGA device under Flash Program Memory

(example for ATxmega16A4 .....ATxmega128A4):

Chip | Boot Loader Flash Section | Boot Reset Address (Start Boot Loader Section)  
---|---|---  
ATxmega16A4 | 0x2000 - 0x7FFF | $loader = &H2000  
ATxmega32A4 | 0x4000 - 0x47FF | $loader = &H4000  
ATxmega64A4 | 0x8000 - 0x87FF | $loader = &H8000  
ATxmega128A4 | 0x10000 - 0x10FFF | $loader = &H10000  
  
![notice](notice.jpg)An external programmer is needed to program the boot loader into the chip. After the fuse bits are set and the boot loader is programmed you do not need the external programmer anymore for this chip (except you want to change the fuse bits).

The MCS boot loader sample is a serial boot loader that uses the serial port (USART).

With ATXMEGA or with ATMEGA with more then one USART you can choose which USART (COM port) should be used with the boot loader.

```vb
For example you can use COM7 with an ATXMEGA:

  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 '   
```
Open "COM7:" For Binary As #7  


![notice](notice.jpg)When using another UART as COM1 do not forget to add the Interface number (in this example #7) to all the Serial IO functions like Waitkey(#7) or Print #7 , Chr(bstatus); in the boot loader example  


The boot loader uses the X-modem checksum protocol to receive the data. (XModem protocol (packet size = 128))

Most terminal emulators can send X-modem checksum.

The Boot loader sample can upload both normal flash programs and EEPROM images.

The Boot loader sends a byte with value of 123 to the AVR Boot loader. This boot loader program then enter the boot loader or will jump to the reset vector (0000) to execute the normal flash program.

When it receives 124 instead of 123, it will upload the EEPROM.

When you select a BIN file the flash will be uploaded. When you select an EEP file, the EEPROM will be uploaded.

The following sample is written so it supports all chips with a boot section. 

How you need to use this ATMEGA boot loader example program:

1.|  Uncomment the Chip type and Const Loaderchip you want to use (for example ATMEGA644)  
---|---  
  
```vb
$regfile = "m644def.dat"  
'$regfile = "m644Pdef.dat"  
```
Const Loaderchip = 644

2.| Double check the baud rate and COM port you want to use  
---|---  
  
3.| Compile the boot loader example  
---|---  
  
4.| Program it into the chip with an external programmer like AVR ISP MKII  
---|---  
  
5.| Select [MCS Bootloader](mcsbootloader.md) from programmer (select the right COM Port and baud rate)  
---|---  
  
6.| compile a new program or example for this chip  
---|---  
  
7.| reset the chip  
---|---  
  
Ways to reset the AVR chip:

Hardware reset:

1.|  Hardware Reset switch/button to GND (manual)  
---|---  
  
2.|  MCS Bootloader can set and reset the DTR or RTS line of serial COM port which can be used to reset the AVR (automatic)  
---|---  
  
Software Reset:

1.|  Reset with Watchdog Timer (e.g. setting the Watchdog to 16ms, start it and let it time out)  
---|---  
  
2.|  With GOTO command (e.g. when ATMEGA644 is used the boot loader start at $7c00 ($loader = $7c00).  
---|---  
  
```vb
Then you can use:

GOTO &H7c00

```
to jump to the boot loader start.

3.|  With ATXMEGA there is a special register to reset the ATXMEGA via software. See also topic ATXMEGA   
---|---  
  
4.|  With MCS Bootloader you can send one or several ASCII character to reset the chip like with string "boot_me". In this case the "boot_me" must be detected in your main application on the AVR and then use for example Watchdog or GOTO to reset the chip.   
---|---  
  
The boot loader is written to work at a baud rate of 57600. This baud rate works for most chips that use the internal oscillator. But it is best to check it first with a simple program. When you use a crystal you might even use a higher baud rate. 

You can change this by changing the baud rate in the boot loader example (take care to use also the same baud rate in the boot loader application (e.g. [MCS Bootloader](mcsbootloader.md)) on the PC side)

Now make a new test program and compile it. Press F4 to start the [MCS bootloader](mcsbootloader.md). You now need to reset the chip so that it will start the boot loader section. The boot loader will send a byte with value of 123 and the Bascom boot loader receives this and thus starts the loader process.

There will be a stand alone boot loader available too. And the sample will be extended to support other AVR chips with boot section too.

![notice](notice.jpg) There is a $BOOT directive too. It is advised to use $LOADER as it allows you to write the boot loader in BASIC.

![important](important.jpg)You can not use interrupts in your boot loader program as the interrupts will point to the reset vector which is located in the lower section of the flash. When you start to writing pages, you overwrite this part.

![notice](notice.jpg)Take care when Watchdog is enabled by fuse bits and using a boot loader. You need to reset or deactivate the Watchdog in the boot loader example otherwise the firmware upload could be terminated by watchdog reset !

![notice](notice.jpg)If you want to analyze the MCU Control and Status Register to know which reset source caused the reset you need to save this register already in the boot loader example because this register will be cleared and it will be always 0 when you check it at start of your application.

![notice](notice.jpg)When you use a boot loader it will use space from the available flash memory. The compiler does not know if you use a boot loader or not. When your program exceeds the available space and runs into the boot sector space, it will overwrite the boot loader.

The [$LOADERSIZE](loadersize.md) directive will take the boot loader size into account so you will get an error when the target file gets too big.

Encryption/Decryption with Bootloader:

You can use for example AES or XTEA ( [XTEADECODE](xteadecode.md), [XTEAENCODE](xteaencode.md) ) in combination with boot loader examples.

There is an AES with boot loader and AVR-DOS example in the ...BASCOM-AVR\SAMPLES\boot folder (xmega_dos_boot_AES.zip).

See also

[$BOOT](_boot.md) , [$LOADERSIZE](loadersize.md), [MCS Bootloader](mcsbootloader.md) , [CONFIG INTVECTORSELECTION](config_intvectorselection.md) , [$BOOTVECTOR](bootvector.md)

There is an example for ATMEGA chips and for ATXMEGA Chips:

ATMEGA Example:

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' Bootloader.bas  
' This sample demonstrates how you can write your own bootloader  
' in BASCOM BASIC  
' VERSION 2 of the BOOTLOADER. The waiting for the NAK is stretched  
' further a bug was resolved for the M64/M128 that have a big page size  
'-----------------------------------------------------------------  
'This sample will be extended to support other chips with bootloader  
'The loader is supported from the IDE  
$crystal = 8000000  
'$crystal = 14745600  
$baud = 57600 'this loader uses serial com  
'It is VERY IMPORTANT that the baud rate matches the one of the boot loader  
'do not try to use buffered com as we can not use interrupts  
  
'possible return codes of the PC bootloader.exe  
' -6005 Cancel requested  
' -6006 Fatal time out  
' -6007 Unrecoverable event during protocol  
' -6008 Too many errors during protocol  
' -6009 Block sequence error in Xmodem  
' -6016 Session aborted  
  
'$regfile = "m8def.dat"  
  
'Const Loaderchip = 8  
'$regfile = "m168def.dat"  
'Const Loaderchip = 168  
  
'$regfile = "m16def.dat"  
'Const Loaderchip = 16  
  
'$regfile = "m32def.dat"  
'Const Loaderchip = 32  
  
'$regfile = "m88def.dat"  
'Const Loaderchip = 88  
  
'$regfile = "m162def.dat"  
'Const Loaderchip = 162  
  
'$regfile = "m8515.dat"  
'Const Loaderchip = 8515  
  
'$regfile = "m128def.dat"  
'Const Loaderchip = 128  
  
'$regfile = "m64def.dat"  
'Const Loaderchip = 64  
  
'$regfile = "m2561def.dat"  
'Const Loaderchip = 2561  
  
'$regfile = "m2560def.dat"  
'Const Loaderchip = 2560  
  
'$regfile = "m329def.dat"  
'Const Loaderchip = 329  
  
'$regfile = "m324pdef.dat"  
'Const Loaderchip = 324  
  
$regfile = "m644def.dat"  
'$regfile = "m644Pdef.dat"  
```
Const Loaderchip = 644  
  

```vb
#if Loaderchip = 88 'Mega88  
$loader = $c00 'this address you can find in the datasheet  
'the loader address is the same as the boot vector address  
```
Const Maxwordbit = 5  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 168 'Mega168  
$loader = $1c00 'this address you can find in the datasheet  
'the loader address is the same as the boot vector address  
```
Const Maxwordbit = 6  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 32 ' Mega32  
$loader = $3c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  

#if Loaderchip = 8 ' Mega8  
$loader = $c00 ' 1024 words  
```
Const Maxwordbit = 5 'Z5 is maximum bit  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  

#if Loaderchip = 161 ' Mega161  
$loader = $1e00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit  

```vb
#endif  

#if Loaderchip = 162 ' Mega162  
$loader = $1c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 8515 ' Mega8515  
$loader = $c00 ' 1024 words  
```
Const Maxwordbit = 5 'Z6 is maximum bit  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
Osccal = &HB3 ' the internal osc needed a new value  

```vb
#endif  
  

#if Loaderchip = 64 ' Mega64  
$loader = $7c00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 128 ' Mega128  
$loader = &HFC00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 2561 ' Mega2561  
$loader = &H1FC00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 2560 ' Mega2560  
$loader = &H1FC00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 16 ' Mega16  
$loader = $1c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 329 ' Mega32  
$loader = $3c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 324 ' Mega32  
$loader = $3c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  
  

#if Loaderchip = 644 ' Mega644P  
$loader = $7c00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit   
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  
```
Const Maxword =(2 ^ Maxwordbit) * 2 '128  
Const Maxwordshift = Maxwordbit + 1  
Const Cdebug = 0 ' leave this to 0  
  

```vb
#if Cdebug  
Print Maxword  
Print Maxwordshift  

#endif  
  
'Dim the used variables  
Dim Bstatus As Byte , Bretries As Byte , Bblock As Byte , Bblocklocal As Byte  
Dim Bcsum1 As Byte , Bcsum2 As Byte , Buf(128) As Byte , Csum As Byte  
Dim J As Byte , Spmcrval As Byte ' self program command byte value  
Dim Z As Long 'this is the Z pointer word  
Dim Vl As Byte , Vh As Byte ' these bytes are used for the data values  
Dim Wrd As Word , Page As Word 'these vars contain the page and word address  
Dim Bkind As Byte , Bstarted As Byte  
'Mega 88 : 32 words, 128 pages  
  
  
  
Disable Interrupts 'we do not use ints  
'Waitms 100 'wait 100 msec sec  
'We start with receiving a file. The PC must send this binary file  
  
'some constants used in serial com  
```
Const Nak = &H15  
Const Ack = &H06  
Const Can = &H18  
  
```vb
'we use some leds as indication in this sample , you might want to remove it  
Config Pinb.2 = Output  
```
Portb.2 = 1 'the stk200 has inverted logic for the leds  
Config Pinb.3 = Output  
Portb.3 = 1  
  
```vb
$timeout = 400000 'we use a timeout  
'When you get LOADER errors during the upload, increase the timeout value  
'for example at 16 Mhz, use 200000  
  
```
Bretries = 5 'we try 5 times  
Testfor123:  

```vb
#if Cdebug  
Print "Try " ; Bretries  
Print "Wait"  

#endif  
```
Bstatus = Waitkey() 'wait for the loader to send a byte  

```vb
#if Cdebug  
Print "Got "  

#endif  
  
Print Chr(bstatus);  
  
If Bstatus = 123 Then 'did we received value 123 ?  
```
Bkind = 0 'normal flash loader  
Goto Loader  
Elseif Bstatus = 124 Then ' EEPROM  
Bkind = 1 ' EEPROM loader  
Goto Loader  
Elseif Bstatus <> 0 Then  
Decr Bretries  
```vb
If Bretries <> 0 Then Goto Testfor123 'we test again  
End If  
  
For J = 1 To 10 'this is a simple indication that we start the normal reset vector  
Toggle Portb.2 : Waitms 100  
Next  
  

#if Cdebug  
Print "RESET"  

#endif  
Goto _reset 'goto the normal reset vector at address 0  
  
  
'this is the loader routine. It is a Xmodem-checksum reception routine  
```
Loader:  

```vb
#if Cdebug  
Print "Clear buffer"  

#endif  
Do  
```
Bstatus = Waitkey()  
```vb
Loop Until Bstatus = 0  
  
For J = 1 To 3 his is a simple indication that we start the normal reset vector  
Toggle Portb.2 : Waitms 50  
Next  
  
If Bkind = 0 Then  
```
Spmcrval = 3 : Gosub Do_spm ' erase the first page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
End If  
  
Bretries = 10 'number of retries  
  
Do  
Bstarted = 0 ' we were not started yet  
Csum = 0 'checksum is 0 when we start  
```vb
Print Chr(nak); ' first time send a nack  
Do  
```
Bstatus = Waitkey() 'wait for status byte  
  
```vb
Select Case Bstatus  
Case 1: ' start of heading, PC is ready to send  
```
Incr Bblocklocal 'increase local block count  
Csum = 1 'checksum is 1  
Bblock = Waitkey() : Csum = Csum + Bblock 'get block  
Bcsum1 = Waitkey() : Csum = Csum + Bcsum1 'get checksum first byte  
For J = 1 To 128 'get 128 bytes  
Buf(j) = Waitkey() : Csum = Csum + Buf(j)  
Next  
Bcsum2 = Waitkey() 'get second checksum byte  
```vb
If Bblocklocal = Bblock Then 'are the blocks the same?  
If Bcsum2 = Csum Then 'is the checksum the same?  
Gosub Writepage 'yes go write the page  
Print Chr(ack); 'acknowledge  
Else 'no match so send nak  
Print Chr(nak);  
End If  
Else  
Print Chr(nak); 'blocks do not match  
End If  
Case 4: ' end of transmission , file is transmitted  
If Wrd > 0 And Bkind = 0 Then 'if there was something left in the page  
```
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = 5 : Gosub Do_spm 'write page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
```vb
End If  
' Waitms 100 ' OPTIONAL REMARK THIS IF THE DTR SIGNAL ARRIVES TO EARLY  
Print Chr(ack); ' send ack and ready  
```
Portb.3 = 0 ' simple indication that we are finished and ok  
```vb
Waitms 20  
Goto _reset ' start new program  
Case &H18: ' PC aborts transmission  
Goto _reset ' ready  
Case 123 : Exit Do 'was probably still in the buffer  
Case 124 : Exit Do  
Case Else  
Exit Do ' no valid data  
End Select  
Loop  
If Bretries > 0 Then 'attempte left?  
Waitms 1000  
```
Decr Bretries 'decrease attempts  
```vb
Else  
Goto _reset 'reset chip  
End If  
Loop  
  
'write one or more pages  
```
Writepage:  
```vb
If Bkind = 0 Then  
For J = 1 To 128 Step 2 'we write 2 bytes into a page  
```
Vl = Buf(j) : Vh = Buf(j + 1) 'get Low and High bytes  
! lds r0, {vl} 'store them into r0 and r1 registers  
! lds r1, {vh}

Spmcrval = 1 : Gosub Do_spm 'write value into page at word address  
Wrd = Wrd + 2 ' word address increases with 2 because LS bit of Z is not used  
If Wrd = Maxword Then ' page is full  
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = 5 : Gosub Do_spm 'write page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
  
Page = Page + 1 'next page  
Spmcrval = 3 : Gosub Do_spm ' erase next page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
```vb
End If  
Next  
  
Else 'eeprom  
For J = 1 To 128  
```
Writeeeprom Buf(j) , Wrd  
Wrd = Wrd + 1  
```vb
Next  
End If  
Toggle Portb.2 : Waitms 10 : Toggle Portb.2 'indication that we write  
Return  
  
  
```
Do_spm:  
Bitwait Spmcsr.0 , Reset ' check for previous SPM complete  
Bitwait Eecr.1 , Reset 'wait for eeprom  
  
Z = Page 'make equal to page  
Shift Z , Left , Maxwordshift 'shift to proper place  
Z = Z + Wrd 'add word  
! lds r30,{Z}  
! lds r31,{Z+1}  
  

#if _romsize > 65536  
! lds r24,{Z+2}  
! sts rampz,r24 ' we need to set rampz also for the M128  

#endif  
  
Spmcsr = Spmcrval 'assign register  
! spm 'this is an asm instruction  
! nop  
! nop  
```vb
Return  
  
  
'How you need to use this program:  
'1- compile this program  
'2- program into chip with sample elctronics programmer  
'3- select MCS Bootloader from programmers  
'4- compile a new program for example M88.bas  
'5- press F4 and reset your micro  
' the program will now be uploaded into the chip with Xmodem Checksum  
' you can write your own loader.too  
'A stand alone command line loader is also available  
  
'How to call the bootloader from your program without a reset ???  
'Do  
' Print "test"  
' Waitms 1000  
' If Inkey() = 27 Then  
' Print "boot"  
' Goto &H1C00  
' End If  
'Loop  
  
'The GOTO will do the work, you need to specify the correct bootloader address  
'this is the same as the $LOADER statement.

```
ATXMEGA Example:

![notice](notice.jpg)NOTICE that there are many Xmega processors and the page size differs.

The example is for the xmega32A4 which uses MAXWORDBIT=7 

Other chips require a different value. See the table after the example.

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' BootloaderXmega32A4.bas  
' This sample demonstrates how you can write your own bootloader  
' in BASCOM BASIC for the XMEGA  
'-----------------------------------------------------------------  
'The loader is supported from the IDE  
$crystal = 32000000 ' xmega128 is running on 32 MHz  
$regfile = "xm32a4def.dat"  
$lib "xmega.lib" ' add a reference to this lib  
  
'first enabled the osc of your choice  
Config Osc = Disabled , 32mhzosc = Enabled 'internal 2 MHz and 32 MHz enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1 ' we will use 32 MHz and divide by 1 to end up with 32 MHz  
  
$loader = &H4000 ' bootloader starts after the application  
  
Config Com1 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 ' use USART C0  
'COM0-USARTC0, COM1-USARTC2, COM2-USARTD0. etc.  
Config Portc.3 = Output 'define TX as output  
Config Pinc.2 = Input  
  
```
Const Maxwordbit = 7 ' Z7 is maximum bit '  
Const Maxword =(2 ^ Maxwordbit) * 2 '128  
Const Maxwordshift = Maxwordbit + 1  
Const Cdebug = 0 ' leave this to 0  
  
```vb
'Dim the used variables  
Dim Bstatus As Byte , Bretries As Byte , Bmincount As Byte , Bblock As Byte , Bblocklocal As Byte  
Dim Bcsum1 As Byte , Bcsum2 As Byte , Buf(128) As Byte , Csum As Byte  
Dim J As Byte , Spmcrval As Byte ' self program command byte value  
Dim Z As Long 'this is the Z pointer word  
Dim Vl As Byte , Vh As Byte ' these bytes are used for the data values  
Dim Wrd As Word , Page As Word 'these vars contain the page and word address  
  
Disable Interrupts 'we do not use ints  
  
'We start with receiving a file. The PC must send this binary file  
  
'some constants used in serial com  
```
Const Nak = &H15  
Const Ack = &H06  
Const Can = &H18  
  
```vb
$timeout = 300000 'we use a timeout  
'When you get LOADER errors during the upload, increase the timeout value  
'for example at 16 Mhz, use 200000  
  
```
Bretries = 5 : Bmincount = 3 'we try 10 times and want to get 123 at least 3 times  
Do  
Bstatus = Waitkey() 'wait for the loader to send a byte  
  
```vb
If Bstatus = 123 Then 'did we received value 123 ?  
If Bmincount > 0 Then  
```
Decr Bmincount  
```vb
Else  
Print Chr(bstatus);  
Goto Loader ' yes so run bootloader  
End If  
Else 'we received some other data  
If Bretries > 0 Then 'retries left?  
```
Bmincount = 3  
Decr Bretries  
Else  
Rampz = 0  
```vb
Goto Proces_reset 'goto the normal reset vector at address 0  
End If  
End If  
Loop  
  
'this is the loader routine. It is a Xmodem-checksum reception routine  
```
Loader:  
Do  
Bstatus = Waitkey()  
Loop Until Bstatus = 0  
  
Spmcrval = &H20 : Gosub Do_spm ' erase all app pages  
  
  
Bretries = 10 'number of retries  
  
Do  
Csum = 0 'checksum is 0 when we start  
```vb
Print Chr(nak); ' first time send a nack  
Do  
  
```
Bstatus = Waitkey() 'wait for status byte  
  
```vb
Select Case Bstatus  
Case 1: ' start of heading, PC is ready to send  
```
Incr Bblocklocal 'increase local block count  
Csum = 1 'checksum is 1  
Bblock = Waitkey() : Csum = Csum + Bblock 'get block  
Bcsum1 = Waitkey() : Csum = Csum + Bcsum1 'get checksum first byte  
For J = 1 To 128 'get 128 bytes  
Buf(j) = Waitkey() : Csum = Csum + Buf(j)  
Next  
Bcsum2 = Waitkey() 'get second checksum byte  
  
```vb
If Bblocklocal = Bblock Then 'are the blocks the same?  
  
If Bcsum2 = Csum Then 'is the checksum the same?  
Gosub Writepage 'yes go write the page  
Print Chr(ack); 'acknowledge  
Else 'no match so send nak  
Print Chr(nak);  
End If  
Else  
Print Chr(nak); 'blocks do not match  
End If  
Case 4: ' end of transmission , file is transmitted  
If Wrd > 0 Then 'if there was something left in the page  
```
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = &H24 : Gosub Do_spm 'write page  
```vb
End If  
Print Chr(ack); ' send ack and ready  
Waitms 20  
Goto Proces_reset  
Case &H18: ' PC aborts transmission  
Goto Proces_reset ' ready  
Case 123 : Exit Do 'was probably still in the buffer  
Case 124 : Exit Do  
Case Else  
Exit Do ' no valid data  
End Select  
Loop  
If Bretries > 0 Then 'attempts left?  
Waitms 1000  
```
Decr Bretries 'decrease attempts  
```vb
Else  
Goto Proces_reset 'reset chip  
End If  
Loop  
  
'write one or more pages  
```
Writepage:  
For J = 1 To 128 Step 2 'we write 2 bytes into a page  
Vl = Buf(j) : Vh = Buf(j + 1) 'get Low and High bytes  
! lds r0, {vl} 'store them into r0 and r1 registers  
! lds r1, {vh}  
Spmcrval = &H23 : Gosub Do_spm 'write value into page at word address  
Wrd = Wrd + 2 ' word address increases with 2 because LS bit of Z is not used  
If Wrd = Maxword Then ' page is full  
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = &H24 : Gosub Do_spm 'write page  
Page = Page + 1 'next page  
```vb
End If  
Next  
Return  
  
```
Do_spm:  
Z = Page 'make equal to page  
Shift Z , Left , Maxwordshift 'shift to proper place  
Z = Z + Wrd 'add word  
! lds r30,{Z}  
! lds r31,{Z+1}  
  

#if _romsize > 65536  
! lds r24,{Z+2}  
! sts rampz,r24 ' we need to set rampz also for the M128  

#endif  
  
Nvm_cmd = Spmcrval  
Cpu_ccp = &H9D  
! spm 'this is an asm instruction  
Do_spm_busy:  
! lds r23, NVM_STATUS  
! sbrc r23,7 ;if busy bit is cleared skip next instruc tion  
! rjmp do_spm_busy  
Return  
  
Proces_reset:  
Rampz = 0  
Goto _reset 'start at address 0  
  


PAGE SIZE 

Processor | Pagesize | Maxwordbit  
---|---|---  
ATxmega128A1 | 512 | 8  
ATxmega128A1U | 512 | 8  
ATxmega128A3 | 512 | 8  
ATxmega128A3U | 512 | 8  
ATxmega128A4U | 256 | 7  
ATxmega128B1 | 256 | 7  
ATxmega128B3 | 256 | 7  
ATxmega128C3 | 512 | 8  
ATxmega128D3 | 512 | 8  
ATxmega128D4 | 256 | 7  
ATxmega16A4 | 256 | 7  
ATxmega16A4U | 256 | 7  
ATxmega16C4 | 256 | 7  
ATxmega16D4 | 256 | 7  
ATxmega16E5 | 128 | 6  
ATxmega192A3 | 512 | 8  
ATxmega192A3U | 512 | 8  
ATxmega192C3 | 512 | 8  
ATxmega192D3 | 512 | 8  
ATxmega256A3 | 512 | 8  
ATxmega256A3B | 512 | 8  
ATxmega256A3BU | 512 | 8  
ATxmega256A3U | 512 | 8  
ATxmega256C3 | 512 | 8  
ATxmega256D3 | 512 | 8  
ATxmega32A4 | 256 | 7  
ATxmega32A4U | 256 | 7  
ATxmega32C3 | 256 | 7  
ATxmega32C4 | 256 | 7  
ATxmega32D3 | 256 | 7  
ATxmega32D4 | 256 | 7  
ATxmega32E5 | 128 | 6  
ATxmega384C3 | 512 | 8  
ATxmega384D3 | 512 | 8  
ATxmega64A1 | 256 | 7  
ATxmega64A1U | 256 | 7  
ATxmega64A3 | 256 | 7  
ATxmega64A3U | 256 | 7  
ATxmega64A4U | 256 | 7  
ATxmega64B1 | 256 | 7  
ATxmega64B3 | 256 | 7  
ATxmega64C3 | 256 | 7  
ATxmega64D3 | 256 | 7  
ATxmega64D4 | 256 | 7  
ATxmega8E5 | 128 | 6