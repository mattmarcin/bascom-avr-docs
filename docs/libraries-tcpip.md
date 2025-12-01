# TCP/IP Libraries

> TCP/IP networking with W5100/W5500

## Adding SRAM 4-port Non Multiplexed

The following information was contributed by Juergen Bitzer.

![Adding sram 4port non multiplexed](adding sram 4port non multiplexed.zoom79.png)

The EBI allows to use an SRAM in 4-port non multiplexed mode. This means that you need little parts but you loose 4 ports.

Example

```vb
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = &H32  
$swstack = &H32  
$framesize = &H32  
$xramstart = &H100000  
$xramsize = &H080000  
  
'------------------  
' CPU:  
' ATXMEGA128A1U-AU : 2,23/100 Mouser Muss -->A1U-AU<\-- sein !!!  
' ATXMEGA64A1U-AU  
'------------------  
' SRam:  
' 512 KB AS6C4008-55PCN : SRAM 4MB 2.7V-5.5V, 512KX8, PDIP32  
  
' 512 KB AS6C4008-55SIN : SRAM 4MB 2.7V-5.5V, 512KX8, SOP32  
' 512 KB AS6C4008-55SIN : SRAM 4MB 2.7V-5.5V, 512KX8, SOP32  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
  
' #### Four Port SRAM ####  
' MODE SRAM 4Port direkt  
  
' PortH.0 - Pin 55 /WR  
' PortH.1 - Pin 56 /RD  
  
' PortE.4 - Pin 39 /CS0 / A16 -> CS0: SRAM 512 KB  
' PortE.5 - Pin 40 /CS1 / A17 -> CS1: unbenutzt  
' PortE.6 - Pin 41 /CS2 / A18 -> CS2: unbenutzt  
' PortE.7 - Pin 42 /CS3 / A19 -> CS3: unbenutzt  
  
' PortJ.0 - Pin 65 D0 -> SRam  
' PortJ.1 - Pin 66 D1 -> SRam  
' PortJ.2 - Pin 67 D2 -> SRam  
' PortJ.3 - Pin 68 D3 -> SRam  
' PortJ.4 - Pin 69 D4 -> SRam  
' PortJ.5 - Pin 70 D5 -> SRam  
' PortJ.6 - Pin 71 D6 -> SRam  
' PortJ.7 - Pin 72 D7 -> SRam  
  
' PortK.0 - Pin 75 A0 -> SRam  
' PortK.1 - Pin 76 A1 -> SRam  
' PortK.2 - Pin 77 A2 -> SRam  
' PortK.3 - Pin 78 A3 -> SRam  
' PortK.4 - Pin 79 A4 -> SRam  
' PortK.5 - Pin 80 A5 -> SRam  
' PortK.6 - Pin 81 A6 -> SRam  
' PortK.7 - Pin 82 A7 -> SRam  
  
' PortF.0 - Pin 45 A8 -> SRam  
' PortF.1 - Pin 46 A9 -> SRam  
' PortF.2 - Pin 47 A10 -> SRam  
' PortF.3 - Pin 48 A11 -> SRam  
' PortF.4 - Pin 49 A12 -> SRam  
' PortF.5 - Pin 40 A13 -> SRam  
' PortF.6 - Pin 41 A14 -> SRam  
' PortF.7 - Pin 42 A15 -> SRam  
  
' PortH.2 - Pin 57 A16 -> SRam  
' PortH.3 - Pin 58 A17 -> SRam  
' PortH.4 - Pin 59 A18 -> SRam  
' PortH.5 - Pin 60 A19 - unbenutzt  
' PortH.6 - Pin 61 A20 - unbenutzt  
' PortH.7 - Pin 62 A21 - unbenutzt  
  
'-------------------------------------------------------------------------------  
'----------generate a 32 MHz system clock by use of the PLL (2MHz * 23 = 46MHz)  
  
Config Osc = Disabled , Extosc = Enabled  
  
'Set the Multiplication factor and select the clock Reference for the PLL  
'Osc_pllctrl = &B00_0_10100 '2MHz clock Source and Multiplication factor = 23  
' 00 : 2 MHz internal OSC  
' 01 : Reerved  
' 10 : 32 MHz internal OSC  
' 11 : External Clock Source  
' 1 : 0=PLL-Output devided by 1 |1=PLL-Output devided by 2  
' xxxxx: Multiplikation of PLL 1-31  
```
Osc_pllctrl = &B11_0_01000 : Const Mhz = 32 ' 32 MHz  
  
```vb
'enable PLL  
Set Osc_ctrl.4 'PLL enable  
  
'configure the systemclock  
Config Sysclock = Pll 'use PLL  
  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
```
Open "com1:" For Binary As #1  
  
' Termninal initialisieren  
Printbin #1 , &H1B ; &H5B ; &H30 ; &H6D ' All attributes off(normal)  
Printbin #1 , &H1B ; &H5B ; &H32 ; &H4A ' Bildschirm löschen  
Printbin #1 , &H1B ; &H5B ; &H48 ; ' Cursor Home  
Printbin #1 , &H1B ; &H5B ; &H3F ; &H32 ; &H35 ; &H68 ; ' Cursor an  
  
```vb
'-------------------------------------------------------------------------------  
' Einstellungen externer Speicher  
' Alle EBI-Ports müssen auf OUTPUT  
' ALLE Ports, die ATKIV-LOW sind müssen auf 1 gesetzt werden !!!  
' ALLE Ports, die ATKIV-HIGH sind müssen auf 0 gesetzt werden !!!  
  
Print #1 , "Config Ports for external Adress / Data-Bus with no ALE... ";  
  
```
Portj_dirset = &B1111_1111 : Portj = &B0000_0000 ' D0:7  
Portj_pin0ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin1ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin2ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin3ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin4ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin5ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin6ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin7ctrl = &B0_0_000_000 'Totem (PushPull)  
  
Portk_dirset = &B1111_1111 : Portk = &B1111_1111 ' A0:7  
Portk_pin0ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin1ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
```vb
' PortX_pinYctrl = &B0_0_001_000 : X= Port A... Y= Bit Nr. 0-7  
' X :7 : 0= SlewRate normal, 1= SlewRate limited  
' X :6 : 0= IO normal, 1= IO inverted  
' XXX :5:3: 000 = Totem (PushPull)  
' XXX :5:3: 001 = Totem + Buskeeper  
' XXX :5:3: 010 = Totem + Pulldown on Input  
' XXX :5:3: 011 = Totem + PullUp on Input  
' XXX :5:3: 100 = Wired or  
' XXX :5:3: 101 = Wired and  
' XXX :5:3: 110 = Wired Or + PullDown  
' XXX :5:3: 111 = Wired And + PullUp  
' XXX:2:0: 000 = Both edges trigger port Interrupts / Events  
' XXX:2:0: 001 = Rising edge trigger port Interrupts / Events  
' XXX:2:0: 010 = Falling edge trigger port Interrupts / Events  
' XXX:2:0: 011 = Low Level trigger port Interrupts / Events  
' XXX:2:0: 100 = Reserved  
' XXX:2:0: 101 = Reserved  
' XXX:2:0: 110 = Reserved  
' XXX:2:0: 111 = Input Buffer Disabled (Only Port A to F) for use with ADC or AC  
  
  
```
Portf_dirset = &B1111_1111 : Portf = &B1111_1111 ' A8:15  
Portf_pin0ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin1ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
Porth_dirset = &B1111_1111 : Porth = &B1111_1111 ' WR, RD , A16, A17, A18, A19, A20, A21  
Porth_pin0ctrl = &B0_0_000_000 'Totem (PushPull)  
Porth_pin1ctrl = &B0_0_000_000 'Totem (PushPull)  
Porth_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
Porte_dirset = &B1111_1111 : Porte = &B1111_0000 ' CS3, CS2, CS1, CS0  
Porte_pin0ctrl = &B0_0_000_000 'Totem (PushPull) CS3  
Porte_pin1ctrl = &B0_0_000_000 'Totem (PushPull) CS2 SRAM  
Porte_pin2ctrl = &B0_0_000_000 'Totem (PushPull) CS1 SRAM  
Porte_pin3ctrl = &B0_0_000_000 'Totem (PushPull) CS0 TFT  
Porte_pin4ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin5ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin6ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin7ctrl = &B0_0_000_000 'Totem (PushPull)  
  
  
```vb
' EBI-OUT legt die 4 ChipSelect's auf einen anderen Port, damit die Adressleitungen  
' A16 bis A21 auf Port-H frei wird.  
```
Portcfg_ebiout = &B0000_00_11  
```vb
' XXXX : RESERVED  
' -> 00 : EBI Port3 adress output on PORT-F 0..7: SD: 4'h0, A[11:8] - SR or SR-LPC with SD on CS3: A[23:16] - SR NoAle or ALE1: A[15:8]  
' 01 : EBI Port3 adress output on PORT-E 0..7: SD: 4'h0, A[11:8] - SR or SR-LPC with SD on CS3: A[23:16] - SR NoAle or ALE1: A[15:8]  
' 10 : EBI Port3 adress output on PORT-F 4..7: SD: A[11:8] - SR or SR-LPC with SD on CS3: A[19:16] - SR NoAle or ALE1: ---  
' 11 : EBI Port3 adress output on PORT-E 4..7: SD: A[11:8] - SR or SR-LPC with SD on CS3: A[19:16] - SR NoAle or ALE1: ---  
  
' 00 : EBI CS-output on PORT-H 4..7  
' 01 : EBI CS-output on PORT-L 4..7  
' 10 : EBI CS-output on PORT-F 4..7  
' -> 11 : EBI CS-output on PORT-E 4..7  
  
  
```
Ebi_ctrl = &B01_00_11_10 'SRAM ALE12, 3Port  
```vb
' XX : 00: 4 Bit Data Bus  
' XX -> : 01: 8 Bit Data Bus  
' XX : 10: RESERVED  
' XX : 11: RESERVED  
  
' XX -> : 00: LPC-Mode: ALE1  
' XX : 01: LPC-Mode: RESERVED  
' XX : 10: LPC-Mode: ALE12  
' XX : 11: LPC-Mode: RESERVED  
  
' XX : 00: ALE1 - Adressbyte 0 and 1 multiplexed  
' XX : 01: ALE2 - Adressbyte 0 and 2 multiplexed  
' XX : 10: ALE12- Adressbyte 0,1 and 2 multiplexed  
' -> XX : 11: NOALE- No adress multiplexing  
  
' XX: 00: Externer Bus disabled  
' XX: 01: 3 Port Control-Bus # Data-Bus # A0:A7 und A8:A15 über ALE1 gemuxt  
' -> XX: 10: 4 Port  
' XX: 11: 2 Port  
  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'ChipSelect0 für 512 KByte SRam  
  
' xxxxxxxx xxxx----  
' Bit: 23 bis 12 11 bis 0 nicht verwendet  
' | |  
```
Ebi_cs0_baseaddr = &B00010000_00000000 ' Start &H100000 = 1M  
```vb
' 00000000_00100000_00000000 = &H002000 = 8K  
' 00000000_00110000_00000000 = &H003000 = 12K  
' 00000000_01000000_00000000 = &H004000 = 16K  
' 00000000_10000000_00000000 = &H008000 = 32K  
' 00000001_00000000_00000000 = &H010000 = 64K  
' 00000010_00000000_00000000 = &H020000 = 128K  
' 00000100_00000000_00000000 = &H040000 = 256K  
' 00001000_00000000_00000000 = &H080000 = 512K  
' -> 00010000_00000000_00000000 = &H100000 = 1M  
' 00100000_00000000_00000000 = &H800000 = 2M  
' 01000000_00000000_00000000 = &H800000 = 4M  
' 10000000_00000000_00000000 = &H800000 = 8M  
  
```
Ebi_cs0_ctrla = &B0_01011_01 ' Size &H080000 = 512 KB  
```vb
' X : RESERVED  
' XXXXX : AdressBlockSize  
' 00000 : 256 Byte  
' 00001 : 512 Byte  
' 00010 : 1 KByte  
' 00011 : 2 KByte  
' 00100 : 4 KByte  
' 00101 : 8 KByte  
' 00110 : 16 KByte  
' 00111 : 32 KByte  
' 01000 : 64 KByte  
' 01001 : 128 KByte  
' 01010 : 256 KByte  
' -> 01011 : 512 KByte  
' 01100 : 1 MByte  
' 01101 : 2 MByte  
' 00110 : 4 MByte  
' 01111 : 8 MByte  
' 10000 : 16 MByte  
' XX : ChipSelectMode  
' 00 : disabled  
' -> 01 : Enabled for SRAM  
' 10 : Enabled for SRAM LPC (LowPinCount)  
' 11 : Enabled for SD-SRAM  
  
```
Ebi_cs0_ctrlb = &B00000_100 ' je nach Geschwindigkeit des SRam's  
```vb
' XXXXX : RESERVED  
' XXX : Waitstates  
' 000 : 0 Waitstates  
' 001 : 1 Waitstates  
' 010 : 2 Waitstates  
' 011 : 3 Waitstates  
' -> 100 : 4 Waitstates  
' 101 : 5 Waitstates  
' 110 : 6 Waitstates  
' 111 : 7 Waitstates  
  
'-------------------------------------------------------------------------------  
  
' Nun kann das externe SRam genauso wie das interne SRam angesprochen werden.  
' Vorteil: erheblich schneller im Zugriff, wie DRam !!!  
' So kann auch Hardware "memory-mapped" eingebunden werden  
' oder ein ISA-Bus realisiert werden.  
  
' Now you can use the external SRAM just like the internal SRAM.  
' This is much faster like DRAM  
' This way you can also map hardware and access registers as you would do for SRAM  
  
$xramstart = &H100000  
$xramsize = &H080000

```

---

## BIPOM MINI-MAX/C

The BiPOM MINI-MAX/AVR-C board from [www.bipom.com](<www.bipom.com>) can be set into PROGRAM and RUN modes.

In programming mode, the board uses the STK500V2 protocol for program downloads.

Selecting the BiPOM MINI-MAX/AVR-C programmer and the COM port is sufficient. Baud rate is fixed at 115200 baud.

The IDE automatically handles switching between PROGRAM and RUN modes.

If you press F4, the board will be put in PROGRAM mode, the firmware will be uploaded, and the board will be set back to RUN mode.

---

## File ZIP

This option will put all project files into a ZIP file.

The file will be given the ZIP extension and is saved into the same folder as the main file.

When your file is named main.bas, the file main.zip will be created.

The following files will be included :

\- all files which are included with $INCLUDE

\- all files which are included with $INC

\- all files which are included with $BGF

If a file is included in the code but can not be found you will get a warning.

![file_zip](file_zip.png)

This option does take conditional compilation into account. 

Meaning that :

```vb
#const a=1

#if a=2

$Include "FT800.inc"

$Include "FT800_Functions.inc"

#endif

```
The files ft800.inc and ft800_functions.inc are not included since the condition does not match.

---

## FLIP

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

---

## FLIP

Action

Flips the bits in a byte.

Syntax

var = FLIP( s )

Remarks

Var | The variable that is assigned with the flipped byte S.  
---|---  
S | The source variable to flip.  
  
The FLIP function can be useful in cases where you have reversed the data lines d0-d7.

It will reverse or mirror the bits

See also

NONE

Example

```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack=32  
$swstack = 16  
$framesize=24  
  
Dim B As Byte , V As Byte  
  
For B = 1 To 20  
```
V = Flip(b)  
```vb
Print B ; " " ; Bin(b) ; " " ; Bin(v)  
Next  
  
End

```
OUTPUT

1 00000001 10000000

2 00000010 01000000

3 00000011 11000000

4 00000100 00100000

5 00000101 10100000

6 00000110 01100000

7 00000111 11100000

8 00001000 00010000

9 00001001 10010000

10 00001010 01010000

11 00001011 11010000

12 00001100 00110000

13 00001101 10110000

14 00001110 01110000

15 00001111 11110000

16 00010000 00001000

17 00010001 10001000

18 00010010 01001000

19 00010011 11001000

20 00010100 00101000

---

## GETDSTIP

Action

Returns the IP address of the peer.

Syntax

Result = GETDSTIP( socket)

Remarks

Result | A LONG variable that will be assigned with the IP address of the peer or destination IP address.  
---|---  
Socket | The socket number (0-3)  
  
When you are in server mode, it might be desirable to detect the IP address of the connecting client.

You can use this for logging, security, etc.

The IP number MSB, is stored in the LS byte of the variable.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [GETDSTPORT](getdstport.md), [URL2IP](url2ip.md)

Partial Example

Dim L as Long

L = GetdstIP(i) ' store current IP number of socket i

---

## GETSOCKET

Action

Creates a socket for TCP/IP communication.

Syntax

Result = GETSOCKET(socket, mode, port, param)

Remarks

Result | A byte that is assigned with the socket number you requested. When the operation fails, it will return 255.  
---|---  
socket | A numeric constant or variable with the socket number. The socket number is in range of 0-3. And 0-7 for the W5200 and W5300.  
Mode | The socket mode. Use sock_stream(1), sock_dgram(2), sock_ipl_raw(3) or macl_raw(4). The modes are defined with constants. The W5100,W5200,W5300 also have the sock_ppoe(5) mode. For TCP/IP communication you need to specify sock_stream or the equivalent value 1. For UDP communication you need to specify sock_dgram or the equivalent value 2.  
Port | This is the local port that will be used for the communication. You may specify any value you like but each socket must have itâs own local port number. When you use 0, the value of LOCAL_PORT will be used. LOCAL_PORT is assigned with CONFIG TCPIP. After the assignment, LOCAL_PORT will be increased by 1. So the simplest way is to setup a local port with CONFIG TCPIP, and then use 0 for port.  
Param | Optional parameter. Use 0 for default. W3100 128 : send/receive broadcast message in UDP 64 : use register value with designated timeout value 32 : when not using no delayed ack 16: when not using silly window syndrome Consult the W3100A documentation for more information. W5100,W5200,W5300 128 : enable multicasting in UDP 32 : enable 'No delayed ACK' operation. Only for TCP/IP. In case of UDP multicast : 1 : use IGMP version 1, otherwise V 2. Consult the wiznet documentation for more information.  
  
After the socket has been initialized you can use SocketConnect to connect to a client, or SocketListen to act as a server.

W5100

When GetSocket does not return a valid socket number you can use a [SOCKETDISCONNECT](socketdisconnect.md) when it is in status &H18. For some reason the socket can remain in status &H18 for over a minutes and a SOCKETDISCONNECT will free the socket quicker.

See also

[CONFIG TCPIP](config_tcpip.md), [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

I = Getsocket(0 , Sock_stream , 5000 , 0)' get a new socket

---

## GETTCPREGS

Action

Read a register value from the ethernet chip.

Syntax

var = GETTCPREGS(address, bytes)

Remarks

Address | The address of the register. This should not include the base address.  
---|---  
bytes | The number of bytes to read.  
  
Most options are implemented with BASCOM statements or functions. When there is a need to read from the ethernet registers you can use the GETTCPREGS function. It can read multiple bytes. 

![notice](notice.jpg)It is important that you specify the lowest address. This points to the MSB of the data. 

See also

[SETTCPREGS](settcpregs.md)

ASM

NONE

Example

[See SETTCPREGS](settcpregs.md)

---

## Installation on multiple computers

The following applies to the licensed version and the license key.

You may install BASCOM on multiple computers. For example on your laptop and your desk PC. There is no limit to the number of PC's you install the software on.

But you may only use one PC at the same time. Since you can only operate one PC at the same time, this is not a real restriction.

When you install on multiple PC's and others work on these PC's at the same time as you, you need multiple licenses!

The same applies for all the add-on libraries/products you purchase. 

We do not want to bother customers with anti piracy dongle and internet controlled licenses.

---

## IP2STR

Action

Convert an IP number into itâs string representation.

Syntax

Var = IP2STR(num)

Remarks

An IP number is represented with dots like 192.168.0.1.

The IP2STR function converts an IP number into a string.

This function is intended to be used in combination with the BASCOM TCP/IP routines.

Var | The string variable that is assigned with the IP number  
---|---  
Num | A variable that contains the ip number is numeric format.  
  
See also

[CONFIG TCPIP](config_tcpip.md), [URL2IP](url2ip.md)

---

## MAKETCP

Action

Creates a TCP/IP formatted long variable.

Syntax

var = MAKETCP(b1,b2,b3,b4 [opt])

var = MAKETCP(num)

Remarks

var | The target variable of the type LONG that is assigned with the IP number  
---|---  
b1-b4 | Four variables of numeric constants that form the IP number. b1 is the MSB of the IP/long b4 is the LSB of the IP/long example var = MakeTCP(192,168,0, varx). We can also use reverse order with the optional parameter : example var = MakeTCP(var3,0,168, 192, 1 ). A value of 1 will use reverse order while a value of 0 will result in normal order. When you use a constant, provide only one parameter : example var = MakeTCP(192.168.0.2). Notice the dots !  
  
MakeTCP is a helper routine for the TCP/IP library.

See also

[CONFIG TCPIP](config_tcpip.md) , [IP2STR](ip2str.md), [URL2IP](url2ip.md)

Example

NONE

---

## Options Compiler Chip

![BASC0062](basc0062.gif)

The following options are available:

Options Compiler Chip

Item | Description  
---|---  
Chip | Selects the target chip. Each chip has a corresponding x.DAT file with specifications of the chip. Note that some DAT files are not available yet.  
XRAM | Selects the size of the external RAM. KB means Kilo Bytes. For 32 KB you need a 62256 STATIC RAM chip.  
HW Stack | The amount of bytes available for the hardware stack. When you use GOSUB or CALL, you are using 2 bytes of HW stack space. When you nest 2 GOSUBâs you are using 4 bytes (2*2). Most statements need HW stack too. An interrupt needs 32 bytes.  
Soft Stack | Specifies the size of the software stack. Each local variable uses 2 bytes. Each variable that is passed to a sub program uses 2 bytes too. So when you have used 10 locals in a SUB and the SUB passes 3 parameters, you need 13 * 2 = 26 bytes.  
Frame size | Specifies the size of the frame. Each local variable is stored in a space that is named the frame space. When you have 2 local integers and a string with a length of 10, you need a frame size of (2*2) + 11 = 15 bytes. The internal conversion routines used when you use INPUT num, or STR(), or VAL(), etc, also use the frame. They need a maximum of 16 bytes. So for this example 15+16 = 31 would be a good value.  
XRAM wait state | Select to insert a wait state for the external RAM.  
External Access enable | Select this option to allow external access of the micro. The 8515 for example can use port A and C to control a RAM chip. This is almost always selected if XRAM is used  
Default | Press or click this button to use the current Compiler Chip settings as default for all new projects.

---

## Program Reset Chip

This menu options will let the programmer reset the processor.

Shortcut : SHIFT+F4

The MCS UPDI programmer will perform a reset using UPDI protocol. It could be done using a DTR or RTS pin from the serial port but using UPDI has the advantage that you can program the RESET pin to be used as a normal IO pin. That is important on processors that do not have a dedicated RESET pin.

---

## Program Send to Chip

Program send to chip shortcut ![BASC0058_wmf](basc0058_wmf.gif), F4

When you access the programmer from the main menu, you will notice the submenu. From the sub menu you can choose 'Program' or 'Manual Program'.

Program will erase and program the processor without any user intervention. 

Manual Program will only show the programmer window. You can manually choose the options to program the chip when the programmer supports it.

Auto Program also needs the option 'Auto Flash' to be set in the [Programmer options](options_programmer.md).

The following section applies to the Programmer window (program chip directly NOT selected) otherwise this is not shown to the user.

âBufferâ below refers to the buffer memory that holds data to be programmed to, or read from the chip.

Menu item | Description  
---|---  
File Exit | Return to editor  
File, Test | With this option you can set the logic level to the LPT pins. This is only intended for the Sample Electronics programmer.  
Buffer Clear | Clears buffer  
Buffer Load from file | Loads a file into the buffer  
Buffer Save to file | Saves the buffer content to a file  
Chip Identify | Identifies the chip  
Write buffer into chip | Programs the buffer into the chip ROM or EEPROM  
Read chip code into buffer | Reads the code or data from the chips code memory or data memory  
Chip blank check | Checks if the chip is blank or erased  
Chip erase | Erase the content of both the program memory and the data memory  
Chip verify | Verifies if the buffer is the same as the chip program or data memory  
Chip Set lock bits | Writes the selected lock bits LB1 and/or LB2. Only an erase will reset the lock bits  
Chip auto program | Erases the chip and programs the chip. After the programming is completed, verification is performed.  
  
The following window will be shown for most programmers:

![programmer](programmer.png)

Note that a chip must be ERASED before it can be programmed.

By default the Flash ROM TAB is shown and the binary data is displayed.

When you have an EEPROM in your project, the EEPROM TAB will show this data too.

The most important TAB is in many cases the Lock & Fuse Bits TAB.

When you select it , the lock and fuse bits will be read.

![programmer_LBFB](programmer_lbfb.png)

These Lock and Fuse bits are different in almost every chip !

You can select new settings and write them to the chip. But be careful ! When you select a wrong oscillator option , you can not program the chip anymore without applying an external clock signal.

This is also the solution to communicate with the chip again : connect a clock pulse to the oscillator input. You could use an output from a working micro, or a clock generator or simple 555 chip circuit.

When you found the right settings, you can use [$PROG](_prog.md) to write the proper settings to new, un-programmed chips. To get this setting you press the 'Write PRG' button.

After a new chip is programmed with $PROG, you should remark the line for safety and quicker programming.

The 'Write PRG' will write the settings, read from the Microprocessor, it will NOT insert the unsaved settings you have made manual. Thus, you must first use the 'Write XXX' buttons to write the changed fuse bits settings to the chip, then you can use the 'Write PRG'.

Notice that the Write xxx buttons are disabled by default. Only after you have changed a lock or fuse bit value, the corresponding button will be enabled. You must click this button in order to apply the new Lock or Fuse bit settings.

Many new chips have an internal oscillator. The default value is in most cases 8 MHz. But since in most cases the 'Divide by 8' option is also enabled, the oscillator value will be 1 MHz. We suggest to change the 'Divide by 8' fuse bit so you will have a speed of 8 MHz.

In your program you can use [$crystal](crystal_1.md) = 8000000 then.

![notice](notice.jpg)$crystal will only inform the compiler which oscillator speed you have selected. This is needed for a number of statements. $crystal will NOT set the speed of the oscillator itself.

![important](important.jpg) Do not change the fuse bit that will change the RESET to a port pin. Some chips have this option so you can use the reset pin as a normal port pin. While this is a great option it also means you can not program the chip anymore using the ISP.

---

## RB_CLEARSTRIPE

Action

Turns off all LEDs of the active channel

Syntax

RB_CLEARSTRIPE

Remarks

The LEDS are all turned off. The information in memory is NOT changed. RB_SEND does not need to be used. In fact, using RB_SEND would send the data from memory again.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

See [RB_CHANGEPIN](rb_changepin.md)

---

## RB_FILLSTRIPE

Action

Set all LED's of the active channel to the specified color. This statement will not change the memory.

Syntax

RB_FILLSTRIPE Color

Remarks

Color | Color is a byte array or variable that contains color information.   
---|---  
  
All LED's of the active channel will be set to the specified color. This statement will not change the memory, just the LED's.

See also

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COPY](rb_copy.md) , [RB_COLOR](rb_color.md)

Example

---

## SETIPPROTOCOL

Action

Configures socket RAW-mode protocol

Syntax

SETIPPROTOCOL socket, value

Remarks

Socket | The socket number. (0-3)  
---|---  
Value | The IP-protocol value to set.  
  
In order to use W3100Aâs IPL_RAW Mode, the protocol value of the IP Layer to be used (e.g., 01 in case

of ICMP) needs to be set before socket initialization.

As in UDP, data transmission and reception is possible when the corresponding channel is initialized.

The PING example demonstrates the usage.

As a first step, SETIPPROTOCOL is used :

Setipprotocol Idx , 1

And second, the socket is initialized :

Idx = Getsocket(idx , 3 , 5000 , 0)

The W3100A data sheet does not provide much more details about the IPR register.

See also

[SETTCPREGS](settcpregs.md), [GETSOCKET](getsocket.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : PING_TWI.bas http://www.faqs.org/rfcs/rfc792.html

'copyright : (c) 1995-2025, MCS Electronics

'purpose : Simple PING program

'micro : Mega88

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m32def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 80 ' default use 32 for the hardware stack

$swstack = 128 ' default use 10 for the SW stack

$framesize = 80 ' default use 40 for the frame space

```
Const Debug = 1

Const Sock_stream = $01 ' Tcp

Const Sock_dgram = $02 ' Udp

Const Sock_ipl_raw = $03 ' Ip Layer Raw Sock

Const Sock_macl_raw = $04 ' Mac Layer Raw Sock

Const Sel_control = 0 ' Confirm Socket Status

Const Sel_send = 1 ' Confirm Tx Free Buffer Size

Const Sel_recv = 2 ' Confirm Rx Data Size

'socket status

Const Sock_closed = $00 ' Status Of Connection Closed

Const Sock_arp = $01 ' Status Of Arp

Const Sock_listen = $02 ' Status Of Waiting For Tcp Connection Setup

Const Sock_synsent = $03 ' Status Of Setting Up Tcp Connection

Const Sock_synsent_ack = $04 ' Status Of Setting Up Tcp Connection

Const Sock_synrecv = $05 ' Status Of Setting Up Tcp Connection

Const Sock_established = $06 ' Status Of Tcp Connection Established

Const Sock_close_wait = $07 ' Status Of Closing Tcp Connection

Const Sock_last_ack = $08 ' Status Of Closing Tcp Connection

Const Sock_fin_wait1 = $09 ' Status Of Closing Tcp Connection

Const Sock_fin_wait2 = $0a ' Status Of Closing Tcp Connection

Const Sock_closing = $0b ' Status Of Closing Tcp Connection

Const Sock_time_wait = $0c ' Status Of Closing Tcp Connection

Const Sock_reset = $0d ' Status Of Closing Tcp Connection

Const Sock_init = $0e ' Status Of Socket Initialization

Const Sock_udp = $0f ' Status Of Udp

Const Sock_raw = $10 ' Status of IP RAW

```vb
'we do the usual

Print "Init TCP" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Twi = &H80 , Clock = 400000

Print "Init done"

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

Dim Idx As Byte , Result As Word , J As Byte , Res As Byte

Dim Ip As Long

Dim Dta(12) As Byte , Rec(12) As Byte

```
Dta(1) = 8 'type is echo

Dta(2) = 0 'code

Dta(3) = 0 ' for checksum initialization

Dta(4) = 0 ' checksum

Dta(5) = 0 ' a signature can be any number

Dta(6) = 1 ' signature

Dta(7) = 0 ' sequence number - any number

Dta(8) = 1

Dta(9) = 65

Dim W As Word At Dta + 2 Overlay 'same as dta(3) and dta(4)

W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)

```vb
#if Debug

For J = 1 To 9

Print Dta(j)

Next

#endif

```
Ip = Maketcp(192.168.0.16) 'try to check this server

Print "Socket " ; Idx ; " " ; Idx

Setipprotocol Idx , 1 'set protocol to 1

'the protocol value must be set BEFORE the socket is openend

Idx = Getsocket(idx , 3 , 5000 , 0)

Do

Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) 'write ping data '

```vb
Print Result

Waitms 100

```
Result = Socketstat(idx , Sel_recv) 'check for data

```vb
Print Result

If Result >= 11 Then

Print "Ok"

```
Res = Tcpread(idx , Rec(1) , Result) 'get data with TCPREAD !!!

```vb
#if Debug

Print "DATA RETURNED :" ; Res '

For J = 1 To Result

Print Rec(j) ; " " ;

Next

Print

#endif

Else 'there might be a problem

Print "Network not available"

End If

Waitms 1000

Loop

```

---

## SETTCP

Action

Configures or reconfigures the TCP/IP chip.

Syntax

SETTCP MAC , IP , SUBMASK , GATEWAY

Remarks

MAC | The MAC address you want to assign to the ethernet chip. The MAC address is a unique number that identifies your chip. You must use a different address for every W3100A chip in your network. Example : 123.00.12.34.56.78 You need to specify 6 bytes that must be separated by dots. The bytes must be specified in decimal notation.  
---|---  
IP | The IP address you want to assign to the ethernet chip. The IP address must be unique for every ethernet chip in your network. When you have a LAN, 192.168.0.10 can be used. 192.168.0.x is used for LANâs since the address is not an assigned internet address.  
SUBMASK | The sub mask you want to assign to the W3100A. The sub mask is in most cases 255.255.255.0  
GATEWAY | This is the gateway address of the ethernet chip. The gateway address you can determine with the IPCONFIG command at the command prompt : C:\>ipconfig Windows 2000 IP Configuration Ethernet adapter Local Area Connection 2: Connection-specific DNS Suffix . : IP Address. . . . . . . . . . . . : 192.168.0.3 Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 192.168.0.1 Use 192.168.0.1 in this case.  
  
The CONFIG TCPIP statement may be used only once.

When you want to set the TCP/IP settings dynamically for instance when the settings are stored in EEPROM, you can not use constants. For this purpose, SETTCP must be used.

SETTCP can take a variable or a constant for each parameter.

When you set the TCP/IP settings dynamically, you do not need to set them with CONFIG TCPIP. In the CONFIG TCPIP you can use the NOINIT parameter so that the MAC and IP are not initialized which saves code.

See also

[GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [CONFIG TCPIP](config_tcpip.md) , [SOCKETDISCONNECT](socketdisconnect.md) , [GETTCPREGS](gettcpregs.md) , [SETTCPREGS](settcpregs.md)

Example

See the DHCP.BAS example from the BASCOM Sample dir.

---

## SETTCPREGS

Action

Writes to an ethernet chip register

Syntax

SETTCPREGS address, var , bytes

Remarks

address | The address of the register. This must be the address of the MSB, or the address with the lowest address. The address should not include the base address.  
---|---  
var | The variable to write.  
bytes | The number of bytes to write.  
  
Most options are implemented with BASCOM statements or functions. When there is a need to write to the ethernet chip register you can use the SETTCPREGS command. It can write multiple bytes. It is important that you specify the lowest address. The SETTCPREGS statement will add the base address of the chip to the address so you should not add it yourself. Use the address from the datasheet.

The addresses are different for the W3100,W5100,W5200 and W5300. 

Some registers you might want to alter are the Retry Count Register(RCR) and Retry Time Register(RTR).

See also

[GETTCPREGS](gettcpregs.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : regs_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : test custom regs reading writing  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 80 ' default use 40 for the frame space  
  
Dim L As Long  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
```vb
'we do the usual  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
Print "Init done"  
  
'set the IP address to 192.168.0.135  
```
Settcp 12.128.12.24.56.78 , 192.168.1.135 , 255.255.255.0 , 192.168.1.1  
  
'now read the IP address direct from the registers  
L = Gettcpregs(&H0f , 4)  
```vb
Print Ip2str(l)  
  
Dim B4 As Byte At L Overlay ' this byte is the same as the LSB of L  
  
'now make the IP address 192.168.1.136 by writing to the LSB  
```
B4 = 136  
Settcpregs &H0F , L , 4 'write  
  
'and check if it worked  
L = Gettcpregs(&H0f , 4)  
```vb
Print Ip2str(l)  
  
'and with PING you can check again that now it works  
  
  
End

```

---

## SOCKETCLOSE

Action

Closes a socket connection.

Syntax

SOCKETCLOSE socket [ , prm]

Remarks

Socket | The socket number you want to close in the range of 0-3 (0-7 for W5200/W5300). When the socket is already closed, no action will be performed.  
---|---  
Prm | An optional parameter to change the behavior of the CloseSocket statement. The following values are possible : | •| 0 - The code will behave as if no parameter has been set.  
---|---  
  
•| 1 - In normal cases, there is a test to see if all data written to the chip has been sent. When you set bit 0 (value of 1) , this test is not performed.  
---|---  
  
•| 2 - In normal cases, there is a test to see if the socket is actually closed after the command has been given to the chip. When it is not closed, you can not re-use the socket. The statement will block program execution however and you could test at a later time if the connection has been closed.  
---|---  
  
You may combine the values. So 3 will combine parameter value 1 and 2.

It is advised to use option value 1 with care.  
  
You must close a socket when you receive the SOCK_CLOSE_WAIT status.

You may also close a socket if that is needed by your protocol.

You will receive a SOCK_CLOSE_WAIT status when the server closes the connection.

When you use CloseSocket you actively close the connection.

Note that it is not needed to wait for a SOCK_CLOSE_WAIT message in order to close a socket connection.

After you have closed the connection, you need to use GetSocket in order to use the socket number again.

In normal conditions, without using the optional parameter, the statement can block your code for a short or longer time, depending on the connection speed.

The CLOSESOCKET statement is equivalent with SOCKETCLOSE. 

SOCKETCLOSE VS SOCKETDISCONNECT

In the W3x00 chips there was no socket disconnect function. A socket close (SOCKETCLOSE) would create a disconnect. 

But in the W5x00 chips, there is an additional function to disconnect a socket. So for these chips you must use SOCKETDISCONNECT to terminate a connection. After that you can still use SOCKETCLOSE to free the resource of the socket.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : clienttest.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : start the easytcp.exe program and listen to port 5000

'micro : Mega161

'suited for demo : no

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "M161def.dat"

$crystal = 4000000

$baud = 19200

$hwstack = 40 ' default use 40 for the hardware stack

$swstack = 40 ' default use 40 for the SW stack

$framesize = 64 ' default use64 for the frame space

```
Const Sock_stream = $01 ' Tcp

Const Sock_dgram = $02 ' Udp

Const Sock_ipl_raw = $03 ' Ip Layer Raw Sock

Const Sock_macl_raw = $04 ' Mac Layer Raw Sock

Const Sel_control = 0 ' Confirm Socket Status

Const Sel_send = 1 ' Confirm Tx Free Buffer Size

Const Sel_recv = 2 ' Confirm Rx Data Size

'socket status

Const Sock_closed = $00 ' Status Of Connection Closed

Const Sock_arp = $01 ' Status Of Arp

Const Sock_listen = $02 ' Status Of Waiting For Tcp Connection Setup

Const Sock_synsent = $03 ' Status Of Setting Up Tcp Connection

Const Sock_synsent_ack = $04 ' Status Of Setting Up Tcp Connection

Const Sock_synrecv = $05 ' Status Of Setting Up Tcp Connection

Const Sock_established = $06 ' Status Of Tcp Connection Established

Const Sock_close_wait = $07 ' Status Of Closing Tcp Connection

Const Sock_last_ack = $08 ' Status Of Closing Tcp Connection

Const Sock_fin_wait1 = $09 ' Status Of Closing Tcp Connection

Const Sock_fin_wait2 = $0a ' Status Of Closing Tcp Connection

Const Sock_closing = $0b ' Status Of Closing Tcp Connection

Const Sock_time_wait = $0c ' Status Of Closing Tcp Connection

Const Sock_reset = $0d ' Status Of Closing Tcp Connection

Const Sock_init = $0e ' Status Of Socket Initialization

Const Sock_udp = $0f ' Status Of Udp

Const Sock_raw = $10 ' Status of IP RAW

```vb
$lib "tcpip.lbx" ' specify the tcpip library

Print "Init , set IP to 192.168.0.8" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 0.0.0.0 , Localport = 1000 , Tx = $55 , Rx = $55

'Use the line below if you have a gate way

'Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Dim Bclient As Byte ' socket number

Dim Idx As Byte

Dim Result As Word ' result

Dim S As String * 80

For Idx = 0 To 3 ' for all sockets

```
Bclient = Getsocket(idx , Sock_stream , 0 , 0) ' get socket for client mode, specify port 0 so loal_port is used

```vb
Print "Local port : " ; Local_port ' print local port that was used

Print "Socket " ; Idx ; " " ; Bclient

```
Result = Socketconnect(idx , 192.168.0.3 , 5000) ' connect to easytcpip.exe server

```vb
Print "Result " ; Result

Next

Do

If Ischarwaiting() <> 0 Then ' is there a key waiting in the uart?

```
Bclient = Waitkey() ' get the key

```vb
If Bclient = 27 Then

Input "Enter string to send " , S ' send WHO , TIME or EXIT

For Idx = 0 To 3

```
Result = Tcpwritestr(idx , S , 255)

```vb
Next

End If

End If

For Idx = 0 To 3

```
Result = Socketstat(idx , 0) ' get status

```vb
Select Case Result

Case Sock_established

```
Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

```vb
If Result > 0 Then

Do

```
Result = Tcpread(idx , S)

```vb
Print "Data from server: " ; Idx ; " " ; S

Loop Until Result = 0

End If

Case Sock_close_wait

Print "close_wait"

```
Closesocket Idx

```vb
Case Sock_closed

'Print "closed"

End Select

Next

Loop

End

```

---

## SOCKETCONNECT

Action

Establishes a connection to a TCP/IP server.

Syntax

Result = SOCKETCONNECT(socket, IP, port [,nowait])

Remarks

Result | A byte that is assigned with 0 when the connection succeeded. It will return 1 when an error occurred.  
---|---  
socket | The socket number in the range of 0-3. Or 0-7 for W5200/W5300.  
IP | The IP number of the server you want to connect to. This may be a number like 192.168.0.2 or a LONG variable that is assigned with an IP number. Note that the LSB of the LONG, must contain the MSB of the IP number.  
Port | The port number of the server you are connecting to.  
NoWait | This is an optional parameter. Make it 1 to suppress waiting for a connection. By default, when you create a connection, the code waits for the connect flag. But waiting will block program execution. When you specify, not to wait, the code returns immediately. But you must use [SOCKETSTAT](socketstat.md) to determine the outcome of the socketconnect.  NOWAIT parameter is implemented for :  -W5100 -W5200 -W5500  
  
You can only connect to a server. Standardized servers have dedicated port numbers. For example, the HTTP protocol(web server) uses port 80.

After you have established a connection the server might send data. This depends entirely on the used protocol. Most servers will send some welcome text, this is called a banner.

You can send or receive data once the connection is established.

The server might close the connection after this or you can close the connection yourself. This also depends on the protocol.

You need to obtain a valid socket first with the GETSOCKET function.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : servertest_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : start the easytcp after the chip is programmed  
' and create 2 connections  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
  
$hwstack = 128 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 128 ' default use 40 for the frame space  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit ' xram access  
```vb
Print "Init , set IP to 192.168.1.70" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
  
  
Dim Bclient As Byte ' socket number  
Dim Idx As Byte  
Dim Result As Word , Result2 As Word ' result  
Dim S As String * 80  
Dim Flags As Byte  
Dim Peer As Long  
Dim L As Long  
  
  
Do  
Waitms 1000  
For Idx = 0 To 3  
```
Result = Socketstat(idx , 0) ' get status  
```vb
Select Case Result  
Case Sock_established  
If Flags.idx = 0 Then ' if we did not send a welcome message yet  
```
Flags.idx = 1  
Result = Tcpwrite(idx , "Hello from W5100A{013}{010}") ' send welcome  
End If  
Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting  
```vb
Print "Received : " ; Result  
If Result > 0 Then  
Do  
Print "Result : " ; Result  
```
Result = Tcpread(idx , S)  
Print "Data from client: " ; Idx ; " " ; Result ; " " ; S  
Peer = Getdstip(idx)  
```vb
Print "Peer IP " ; Ip2str(peer)  
Print "Peer port : " ; Getdstport(idx)  
'you could analyse the string here and send an appropiate command  
'only exit is recognized  
If Lcase(s) = "exit" Then  
```
Closesocket Idx  
Elseif Lcase(s) = "time" Then  
Result2 = Tcpwrite(idx ,"12:00:00{013}{010}") ' you should send date$ or time$  
```vb
End If  
Loop Until Result = 0  
End If  
Case Sock_close_wait  
Print "close_wait"  
```
Closesocket Idx  
```vb
Case Sock_closed  
Print "closed"  
```
Bclient = Getsocket(idx , Sock_stream , 5000 , 64) ' get socket for server mode, specify port 5000  
Print "Socket " ; Idx ; " " ; Bclient  
  
Socketlisten Idx  
Print "Result " ; Result  
Flags.idx = 0 ' reset the hello message flag  
```vb
Case Sock_listen ' this is normal  
Case Else  
Print "Socket status : " ; Result  
End Select  
Next  
Loop  
  
  
End

```

---

## SOCKETDISCONNECT

Action

Disconnects a socket connection.

Syntax

SOCKETDISCONNECT socket

Remarks

Socket | The socket number you want to close in the range of 0-3 (0-7 for W5200/W5300). When the socket is already closed, no action will be performed.  
---|---  
  
The socketdisconnect statement sends a connection termination request. 

You can also use SOCKETCLOSE to close the socket and free it's resources.

After you have closed the connection, you need to use GetSocket in order to use the socket number again.

If you only disconnect the socket, you can use socketconnect witout Getsocket.

The socketdisconnect is only intended for TCP connections. (UDP does not have connections).

![notice](notice.jpg)This statement is only available for the W5100/W5200/W5300. The W3100A does not support it.

SOCKETCLOSE VS SOCKETDISCONNECT

In the W3x00 chips there was no socket disconnect function. A socket close (SOCKETCLOSE) would create a disconnect. 

But in the W5x00 chips, there is an additional function to disconnect a socket. So for these chips you must use SOCKETDISCONNECT to terminate a connection. After that you can still use SOCKETCLOSE to free the resource of the socket.

See also

[CONFIG TCPIP](config_tcpip.md), [SOCKETCLOSE](socketclose.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETLISTEN](socketlisten.md) , [SETTCP](settcp.md), [URL2IP](url2ip.md)

Example

NONE

---

## SOCKETLISTEN

Action

Opens a socket in server(listen) mode.

Syntax

SOCKETLISTEN socket

Remarks

Socket | The socket number you want to use for the server in the range of 0 -3. Or 0-7 for W5200/W5300.  
---|---  
  
The socket will listen to the port you specified with the GetSocket function.

When a client connects, the socket status changes in sock_established. When a connection is established, you can send or receive data.

After the connection is closed by either the client or the server, a new connection need to be created and the SocketListen statement must be used again.

When the status has changed to sock_closed, there still could be some pending data in the receive buffer. So you could check with the SOCKETSTAT function if there is data waiting. And if data is waiting, you can read it with TCPREAD before opening the socket again. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETDISCONNECT](socketdisconnect.md)

Example

See [SOCKETCONNECT](socketconnect.md) example

---

## SOCKETSTAT

Action

Returns information about a socket.

Syntax

Result = SOCKETSTAT( socket , mode)

Remarks

Result | A word variable that is assigned with the result.  
---|---  
Socket | The socket number you want to get information of in the range from 0-3. Or 0-7 for W5200/W5300)  
Mode | A parameter which specifies what kind of information you want to retrieve. SEL_CONTROL or 0 : returns the status register value SEL_SEND or 1 : returns the number of bytes that might be placed into the transmission buffer. Or in other words : the free transmission buffer space. SEL_RECV or 2 : returns the number of bytes that are stored in the reception buffer. Or in other words : the number of bytes received.  
  
The SocketStat function contains actual 3 functions. One to get the status of the connection, one to determine how many bytes you might write to the socket, and one to determine how many bytes you can read from the buffer.

When you specify mode 0, one of the following byte values will be returned:

W3100A

Value | State | Description  
---|---|---  
0 | SOCK_CLOSED | Connection closed  
1 | SOCK_ARP | Standing by for reply after transmitting ARP request  
2 | SOCK_LISTEN | Standing by for connection setup to the client when acting in passive mode  
3 | SOCK_SYNSENT | Standing by for SYN,ACK after transmitting SYN for connecting setup when acting in active mode  
4 | SOCK_SYNSENT_ACK | Connection setup is complete after SYN,ACK is received and ACK is transmitted in active mode  
5 | SOCK_SYNRECV | SYN,ACK is being transmitted after receiving SYN from the client in listen state, passive mode  
6 | SOCK_ESTABLISHED | Connection setup is complete in active, passive mode  
7 | SOCK_CLOSE_WAIT | Connection being terminated  
8 | SOCK_LAST_ACK | Connection being terminated  
9 | SOCK_FIN_WAIT1 | Connection being terminated  
10 | SOCK_FIN_WAIT2 | Connection being terminated  
11 | SOCK_CLOSING | Connection being terminated  
12 | SOCK_TIME_WAIT | Connection being terminated  
13 | SOCK_RESET | Connection being terminated after receiving reset packet from peer.  
14 | SOCK_INIT | Socket initializing  
15 | SOCK_UDP | Applicable channel is initialized in UDP mode.  
16 | SOCK_RAW | Applicable channel is initialized in IP layer RAW mode  
17 | SOCK_UDP_ARP | Standing by for reply after transmitting ARP request packet to the destination for UDP transmission  
18 | SOCK_UDP_DATA | Data transmission in progress in UDP RAW mode  
19 | SOCK_RAW_INIT | W3100A initialized in MAC layer RAW mode  
  
W5100,W5200,W5300

Value | State | Description  
---|---|---  
0 | SOCK_CLOSED | Connection closed  
&H11 | SOCK_ARP | Standing by for reply after transmitting ARP request  
&H14 | SOCK_LISTEN | Standing by for connection setup to the client when acting in passive mode  
&H15 | SOCK_SYNSENT | Standing by for SYN,ACK after transmitting SYN for connecting setup when acting in active mode  
&H16 | SOCK_SYNRECV | SYN,ACK is being transmitted after receiving SYN from the client in listen state, passive mode  
&H17 | SOCK_ESTABLISHED | Connection setup is complete in active, passive mode  
&H1C | SOCK_CLOSE_WAIT | Connection being terminated  
&H1D | SOCK_LAST_ACK | Connection being terminated  
&H18 | SOCK_FIN_WAIT | Connection being terminated  
&H1A | SOCK_CLOSING | Connection being terminated  
&H1B | SOCK_TIME_WAIT | Connection being terminated  
&H13 | SOCK_INIT | Socket initializing  
&H22 | SOCK_UDP | Applicable channel is initialized in UDP mode.  
&H32 | SOCK_RAW | Applicable channel is initialized in IP layer RAW mode  
&H42 | SOCK_MACRAW | Applicable channel is initialized in MAC layer RAW mode  
&H5F | SOCK_PPOE | Applicable channel is initialized in PPOE mode  
  
The SocketStat function is also used internal by the library.

For the W5300, if you use ALIGN=2, you need to take in mind that you must read the data buffer if it contains data. Do not call SocketStat again since it will read another 2 bytes to determine the received data size.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

Tempw = Socketstat(i , 0)' get status

```vb
Select Case Tempw

Case Sock_established

Case Else

End Select

```

---

## TCP/IP

TCP/IP

---

## TCPCHECKSUM

Action

Return a TCP/IP checksum, also called Internet Checksum, or IP Checksum.

Syntax

res= TCPCHECKSUM(buffer , bytes [,w1] [,w2])

Remarks

Res | A word variable that is assigned with the TCP/IP checksum of the buffer  
---|---  
Buffer | A variable or array to get the checksum of.  
Bytes | The number of bytes that must be examined.  
w1,w2 | Optional words that will be included in the checksum.  
  
Checksum's are used a lot in communication protocols. A checksum is a way to verify that received data is the same as it was sent. In the many Internet Protocols (TCP, UDP, IP, ICMP â¦) a special Internet checksum is used. Normally the data to calculate the checksum on is stored in an array of bytes, but in some cases like TCP, and UDP, a pseudo header is added. The optional words (w1, w2) can be used for these cases. Most often w1 and w2 will be used for the Protocol number, and the UDP or TCP packet length.

This checksum is calculated by grouping the bytes in the array into 2-byte words. If the number of Bytes is an odd number, then an extra byte of zero is used to make the last 2-byte word. All of the words are added together, keeping the total in a 4-byte Long variable. If the optional words w1, w2, are included, they are also added to the total. Next, the 4-byte Long total is split into two, 2-byte words, and these words are added together to make a new 2-byte Word total. Finally the total is inverted. This is the value returned as Res.

This function using w1, w2, are very useful when working directly with Ethernet chips like the RTL8019AS or with protocols not directly supported by the WIZnet chips.

See the samples directory for more examples of use (IP_Checksum.bas). 

You can use it for the PING sample below.

See also

[CRC8](crc8.md) , [CRC16](crc16.md), [CRC32](crc32.md) , [CHECKSUM](checksum.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : PING_TWI.bas http://www.faqs.org/rfcs/rfc792.html

'copyright : (c) 1995-2025, MCS Electronics

'purpose : Simple PING program

'micro : Mega88

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m32def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 80 ' default use 32 for the hardware stack

$swstack = 128 ' default use 10 for the SW stack

$framesize = 80 ' default use 40 for the frame space

```
Const Debug = 1

```vb
'we do the usual

Print "Init TCP" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0, Mac = 12.128.12.34.56.78, Ip = 192.168.0.8, Submask = 255.255.255.0, Gateway = 192.168.0.1, Localport = 1000, Tx = $55, Rx = $55, Twi = &H80, Clock = 400000

Print "Init done"

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

Dim Idx As Byte , Result As Word , J As Byte , Res As Byte

Dim Ip As Long

Dim Dta(12) As Byte , Rec(12) As Byte

```
Dta(1) = 8 ' type is echo

Dta(2) = 0 ' code

Dta(3) = 0 ' for checksum initialization

Dta(4) = 0 ' checksum

Dta(5) = 0 ' a signature can be any number

Dta(6) = 1 ' signature

Dta(7) = 0 ' sequence number - any number

Dta(8) = 1

Dta(9) = 65

Dim W As Word At Dta + 2 Overlay ' same as dta(3) and dta(4)

W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)

```vb
#if Debug

For J = 1 To 9

Print Dta(j)

Next

#endif

```
Ip = Maketcp(192.168.0.16) ' try to check this server

Print "Socket " ; Idx ; " " ; Idx

Setipprotocol Idx , 1 ' set protocol to 1

'the protocol value must be set BEFORE the socket is openend

Idx = Getsocket(idx , 3 , 5000 , 0)

Do

Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) ' write ping data 

```vb
Print Result

Waitms 100

```
Result = Socketstat(idx , Sel_recv) ' check for data

```vb
Print Result

If Result >= 11 Then

Print "Ok"

```
Res = Tcpread(idx , Rec(1) , Result) ' get data with TCPREAD !!!

```vb
#if Debug

Print "DATA RETURNED :" ; Res 

For J = 1 To Result

Print Rec(j) ; " " ;

Next

Print

#endif

Else ' there might be a problem

Print "Network not available"

End If

Waitms 1000

Loop

```

---

## TCPIP

The TCPIP library allows you to use the W3100A internet chip from [www.iinchip.com](<http://www.iinchip.com>)

There are also libraries for W5100, W5200 and W5300.

MCS has developed a special development board that can get you started quickly with TCP/IP communication. Look at [http://www.mcselec.com](<http://mcselec.com/index.php?option=com_content&task=view&id=18&Itemid=41>) for more info.

All tcpip lbx files areshipped with BASCOM-AVR

The following functions are provided:

[CONFIG TCPIP](config_tcpip.md) | Configures the W3100 chip.  
---|---  
[GETSOCKET](getsocket.md) | Creates a socket for TCP/IP communication.  
[SOCKETCONNECT](socketconnect.md) | Establishes a connection to a TCP/IP server.  
[SOCKETSTAT](socketstat.md) | Returns information of a socket.  
[TCPWRITE](tcpwrite.md) | Write data to a socket.  
[TCPWRITESTR](tcpwritestr.md) | Sends a string to an open socket connection.  
[TCPREAD](tcpread.md) | Reads data from an open socket connection.  
[CLOSESOCKET](socketclose.md) | Closes a socket connection.  
[SOCKETLISTEN](socketlisten.md) | Opens a socket in server(listen) mode.  
[GETDSTIP](getdstip.md) | Returns the IP address of the peer.  
[GETDSTPORT](getdstport.md) | Returns the port number of the peer.  
[BASE64DEC](base64dec.md) | Converts Base-64 data into the original data.  
[BASE64ENC](base64enc.md) | Convert a string into a BASE64 encoded string.  
[MAKETCP](maketcp.md) | Encodes a constant or 4 byte constant/variables into an IP number  
[UDPWRITE](udpwrite.md) | Write UDP data to a socket.  
[UDPWRITESTR](udpwritestr.md) | Sends a string via UDP.  
[UDPREAD](udpread.md) | Reads data via UDP protocol.  
  
The MCS webshop offers the WIZ810MJ ethernet module, and a special converter board so it has few connections.

[WIZ810MJ module](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=266&category_id=22&option=com_phpshop&Itemid=1>)

[TCPADB5100 adapter board. ](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=267&category_id=22&option=com_phpshop&Itemid=1>)

---

## TCPREAD

Action

Reads data from an open socket connection.

Syntax

Result = TCPREAD( socket , var, bytes)

Remarks

Result | A byte variable that will be assigned with 0, when no errors occurred. When an error occurs, the value will be set to 1. When there are not enough bytes in the reception buffer, the routine will wait until there is enough data or the socket is closed.  
---|---  
socket | The socket number you want to read data from (0-3). Or 0-7 for W5200/W5300.  
Var | The name of the variable that will be assigned with the data from the socket.  
Bytes | The number of bytes to read. Only valid for non-string variables.  
  
When you use TCPread with a string variable, the routine will wait for CR + LF and it will return the data without the CR + LF.

```vb
For strings, the function will not overwrite the string.

For example, your string is 10 bytes long and the line you receive is 80 bytes long, you will receive only the first 10 bytes after CR + LF is encountered.

```
Also, for string variables, you do not need to specify the number of bytes to read since the routine will wait for CR + LF.

For other data types you need to specify the number of bytes.

There will be no check on the length so specifying to receive 2 bytes for a byte will overwrite the memory location after the memory location of the byte.

You should only attempt to read data if you have determined with the SocketStat function, that there is actual data in the receive buffer.

$BIGSTRINGS are not supported by TCPREAD. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

If Result > 0 Then

Result = Tcpread(idx , S)

End If

---

## TCPREADHEADER

Action

This statement reads the TCP packet header from the specified socket.

Syntax

TCPREADHEADER socket

Remarks

This option is only available for the W5300 which includes a packet header with the packet size when align is set to 0.

TCP packets start with a 2 byte size header. 

After you have read the TCP header, you can use TCPDATASIZE to read the number of bytes available in the packet. 

TCPDATASIZE is a word variable you need to dimension yourself. 

Socket is a constant or variable in the range from 0-7.

See also

[UDPREAD](udpread.md), [CONFIG TCPIP](config_tcpip.md) , [UDPREADHEADER](udpreadheader.md), [URL2IP](url2ip.md), [URL2IP](url2ip.md)

Example

---

## TCPWRITE

Action  
  
Write data to a socket.

Syntax

Result = TCPWRITE( socket , var , bytes)

Result = TCPWRITE( socket , EPROM, address , bytes)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
Socket | The socket number you want to send data to in the range from 0-3. Or 0-7 for the W5200/W5300.  
Var | A constant string like "test" or a variable. When you send a constant string, the number of bytes to send does not need to be specified.  
Bytes | A word variable or numeric constant that specifies how many bytes must be send.  
Address | The address of the data stored in the chips internal EEPROM. You need to specify EPROM too in that case.  
EPROM | An indication for the compiler so it knows that you will send data from EPROM.  
  
The TCPwrite function can be used to write data to a socket that is stored in EEPROM or in memory.

When you want to send data from an array, you need to specify the element : var(idx) for example.

The amount of data you can send depends on the socket TX size. With CONFIG TCPIP you can define the TX buffer size.

For example, for the W5100, the maximum TX socket size is 2 KB. In this case the maximum data size you can send is 2048 bytes.

Bigger data should be send in multiple chucks. 

You should also consider the maximum packet size. If the packet size is 1460, sending more data will send multiple fragmented packets.

If you have enough RAM available, the best option is to use a buffer with the same size as the packet size. But if your memory it limited, you can let the chip handle this. 

The following sample function demonstrates how you can send multiple chunks. The sample uses a buffer named eth_buffer() with a size of 2048 bytes.

  
Function Write_databuf(byval Txsize As Word) As Word  
Local Strt As Word  
Strt = 1  
```vb
Do  
If Txsize > 2048 Then  
```
Write_databuf = Tcpwrite(idx_http , Eth_buffer(strt) , 2048)  
Txsize = Txsize - 2048 : Strt = Strt + 2048  
Else  
Write_databuf = Tcpwrite(idx_http , Eth_buffer(strt) , Txsize)  
```vb
Exit Do  
End If  
Loop  
```
Http_speed = Http_speed + txSize  
End function  
  


See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md) , [SETTCPREGS](settcpregs.md), [URL2IP](url2ip.md)

Example

Result = Tcpwrite(idx , "Hello from W3100A{013}{010}")

---

## TCPWRITESTR

Action

Sends a string to an open socket connection.

Syntax

Result = TCPWRITESTR( socket , var , param)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
Socket | The socket number you want to send data to (0-3). 0-7 for W5200/W5300.  
Var | The name of a string variable.  
Param | A parameter that might be 0 to send only the string or 255, to send the string with an additional CR + LF This option was added because many protocols expect CR + LF at the end of the string.  
  
The TCPwriteStr function is a special variant of the TCPwrite function.

It will use TCPWrite to send the data.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Example

```vb
'-------------------------------------------------------------------------------

' SMTP.BAS

' (c) 1995-2025 MCS Electronics

' sample that show how to send an email with SMTP protocol

'-------------------------------------------------------------------------------

$regfile = "m161def.dat" ' used processor

$crystal = 4000000 ' used crystal

$baud = 19200 ' baud rate

```
Const Debug = -1 ' for sending feeback to the terminal

```vb
#if Debug

Print "Start of SMTP demo"

#endif

Enable Interrupts ' enable interrupts

'specify MAC, IP, submask and gateway

'local port value will be used when you do not specify a port value while creating a connection

'TX and RX are setup to use 4 connections each with a 2KB buffer

Config Tcpip = Int0 , Mac = 00.44.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

'dim the used variables

Dim S As String * 50 , I As Byte , J As Byte , Tempw As Word

#if Debug

Print "setup of W3100A complete"

#endif

'First we need a socket

```
I = Getsocket(0 , Sock_stream , 5000 , 0)

```vb
' ^ socket numer ^ port

#if Debug

Print "Socket : " ; I

'the socket must return the asked socket number. It returns 255 if there was an error

#endif

If I = 0 Then ' all ok

'connect to smtp server

```
J = Socketconnect(i , 194.09.0. , 25) ' smtp server and SMTP port 25

```vb
' ^socket

' ^ ip address of the smtp server

' ^ port 25 for smtp

' DO NOT FORGET to ENTER a valid IP number of your ISP smtp server

#if Debug

Print "Connection : " ; J

Print S_status(1)

#endif

If J = 0 Then ' all ok

#if Debug

Print "Connected"

#endif

Do

```
Tempw = Socketstat(i , 0) ' get status

```vb
Select Case Tempw

Case Sock_established ' connection established

```
Tempw = Tcpread(i , S) ' read line

```vb
#if Debug

Print S ' show info from smtp server

#endif

If Left(s , 3) = "220" Then ' ok

```
Tempw = Tcpwrite(i , "HELO username{013}{010}" ) ' send username

```vb
' ^^^ fill in username there

#if Debug

Print Tempw ; " bytes written" ' number of bytes actual send

#endif

```
Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S ' show response

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "MAIL FROM:<tcpip@test.com>{013}{010}") ' send from address

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "RCPT TO:<tcpip@test.com>{013}{010}") ' send TO address

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "DATA{013}{010}") ' speicfy that we are going to send data

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "354" Then ' ok

```
Tempw = Tcpwrite(i , "From: tcpip@test.com{013}{010}")

Tempw = Tcpwrite(i , "To: tcpip@test.com{013}{010}")

Tempw = Tcpwrite(i , "Subject: BASCOM SMTP test{013}{010}")

Tempw = Tcpwrite(i , "X-Mailer: BASCOM SMTP{013}{010}")

Tempw = Tcpwrite(i , "{013}{010}")

Tempw = Tcpwrite(i , "This is a test email from BASCOM SMTP{013}{010}")

Tempw = Tcpwrite(i , "Add more lines as needed{013}{010}")

Tempw = Tcpwrite(i , ".{013}{010}") ' end with a single dot

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "QUIT{013}{010}") ' quit connection

Tempw = Tcpread(i , S)

```vb
#if Debug

Print S

#endif

End If

End If

End If

End If

End If

End If

Case Sock_close_wait

Print "CLOSE_WAIT"

```
Closesocket I ' close the connection

```vb
Case Sock_closed

Print "Socket CLOSED" ' socket is closed

End

End Select

Loop

End If

End If

End 'end program

```

---

## Tips and tricks

Tips & Tricks:

1\. You can specify a binary number with the &B and you can use underscore "_" like:

Dim Var As Byte  
  
Var = &B00_110000  
Var = &B0000_1111  
Var = &B00_11_00_11

2\. How to use longer formulas:

```vb
Dim A As Byte  
Dim B As Byte  
Dim C As Byte  
  
' Now you want to use following formula: a = B / 4 + C  
' In Bascom you write  
  
```
A = B / 4  
A = A + C

3\. You can use more than one Bascom statement in one line with colons ":"

```vb
Dim A As Byte  
Dim B As Byte  
Dim C As Byte  
  
' Now you want to use following formula: a = B / 4 + C  
' In Bascom you write  
  
```
A = B / 4 : A = A + C

4\. You can use overlay to have easy access to the low byte and high byte of a WORD

(the same approach also work for e.g. LONG)

```vb
Dim My_word As Word  
Dim Low_byte As Byte At My_word Overlay  
Dim High_byte As Byte At My_word + 1 Overlay  
  
```
Low_byte = &B0000_1111  
High_byte = &B1111_0000  
  
```vb
' This is how it will be stored in SRAM  
' <\-------my_word-------->  
' +-----------+----------+  
' | Low_byte |High_byte |  
' +-----------+----------+

```
5\. To split a word into High byte and Low byte you can also use [HIGH](high.md) and [LOW](low.md)

6\. Here is a way to print the content of a variable or AVR register:

Use Print Bin(X)

Example:

```vb
$regfile = "m88def.dat" ' we use the M88  
$crystal = 8000000  
$baud = 19200  
$hwstack = 32  
$swstack = 8  
$framesize = 24  
  
  
Dim A As Byte  
  
```
A = &B00000001  
A = A * 2  
```vb
Print Bin(a)   
  
End ' end program

```
7\. If you do not want that Bascom-AVR is sending Carriage + Return after a print command use semi-colon ";" after the print funtion:

Example:

```vb
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
Print "Hello World" ;  
  
End

```
8\. For the user who want to use external editors:

The bascomp.exe has been updated. It can be downloaded from the download section.

It now supports a simpler way to be called.

The utility has been updated and now will retrieve all info from the source file, but only when your main program contains these directive :

$regfile, $hwstack, $swstack, $framesize

Example :

bascomp.exe "c:\my folder\source\sample.bas" auto

The 'auto' is a switch so the utility will retrieve the settings from your code.

9\. You can use $initmicro if you want to run special tasks at startup:

See [$INITMICRO](_initmicro.md)

10\. You can use $include to make larger projects better readable: See [$INCLUDE](include.md)

11\. Your LCD is not working and you need a list of steps what do check:

a. Check fuse bit settings

b. Are the AVR pins are OK ?

To test the AVR pins you can do following:

Write a program that toggles all the lcd pins and then measure the logic level.

```vb
Then check with a DVM or led-series resistor if all pins change level. if they do, there is a problem with the lcd

If the pin do not toggle:

```
\- pin defect

\- track or solder problem. 

Here the test program:

```vb
$regfile = "m328pdef.dat" ' Specify The Used Micro  
$crystal = 16000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for thehardware stack  
$swstack = 10 ' default use 10 for theSW stack  
$framesize = 40 ' default use 40 for theframe space  
  
Config Clockdiv = 1 ' divide xtal clock by 1, default fuse bit is set ' to 8 by elektor  
  
Config Portc.3 = Output ' RW  
Config Portd.4 = Output ' Db4  
Config Portd.5 = Output ' Db5  
Config Portd.6 = Output ' Db6  
Config Portd.6 = Output ' Db7  
Config Portc.1 = Output ' E  
Config Portc.2 = Output ' RS  
  
do  
toggle portc  
toggle portd  
waitms 1000  
Loop  
  
End ' end program

```
12\. With the Lib Manager you can compile a Library (*.lib) into an *.lbx file.

See here: [Tools LIB Manager](tools_lib_manager.md)

13\. There is a timeout function for hardware and software UART

See [$TIMEOUT](_timeout.md)

14\. How to use the Powerdown function:

See also: [CONFIG POWERMODE](config_powermode.md)

If you can not measure the same power down current as written in the data sheet you also need to use a

Low Quiescent Current LDO Regulator to meet that specs (if you measure the current including the Current LDO Regulator).

Examples for 3.3Volt Low Quiescent Current LDO Regulator :

•| MCP1702 --> typical 2µA  
---|---  
  
•| MCP1700 --> typical 1.6µA  
---|---  
  
•| AS1375 low power LDO --> 1µA (typ.) of quiescent current  
---|---  
  
•| TPS78233 3,3V --> 0.4µA  
---|---  
  
  
```vb
' Using the new config powermode = PowerDown function with ATTINY13  
  
' Used Bascom-AVR Version 2.0.7.3  
  
' Fuse Bits:  
' Disable DWEN (Debug Wire) Fuse Bit  
' Disable Brown-Out Detection in Fuse Bits  
' Disable Watchdog in Fuse Bits  
  
' You can also just use Config Powermode = Powerdown  
  
' But this example here also considers what the data sheet write under "MINIMIZING POWER CONSUMPTION"  
' You need to follow this when you want to achieve the current consumption which you find in the

' data sheet under Powerdown Mode.  
  
' 1. Disable/Switch off ADC  
' 2. Disable/Switch off Analog Comparator  
' 3. Disable Brown-out Detection when not needed  
' 4. Disable internal voltage reference  
' 5. Disable Watchdog Timer when not needed  
' 6. Disable the digital input buffer  
' 7. Enable Pull-up or pull-down an all unused pins  
  
$regfile = "attiny13.dat"  
$crystal = 9600000 ' 9.6MHz  
$hwstack = 10  
$swstack = 0  
$framesize = 24  
  
On Int0 Int0_isr ' INT0 will be the wake-up source for Powerdown Mode  
Config Int0 = Low Level  
Enable Int0  
  
' Prepare Powerdown:  
' To minimize power consumption, enable pull-up or -down on all unused pins, and  
' disable the digital input buffer on pins that are connected to analog sources  
Config Portb.0 = Input  
Set Portb.0  
Config Portb.1 = Input ' INT0 --> external 47K pull-up  
'Set Portb.1  
Config Portb.2 = Input  
Set Portb.2  
Config Portb.3 = Input  
Set Portb.3  
Config Portb.4 = Input  
Set Portb.4  
Config Portb.5 = Input ' External Pull-Up (Reset)  
  
```
Didr0 = Bits(ain1d , Ain0d) ' Disable digital input buffer on the AIN1/0 pin  
  
```vb
Set Acsr.acd ' Switch off the power to the Analog Comparator  
' alternative:  
' Stop Ac  
  
Reset Acsr.acbg ' Disable Analog Comparator Bandgap Select  
  
Reset Adcsra.aden ' Switch off ADC  
' alternative:  
' Stop Adc  
  
'###############################################################################  
Do  
Wait 3 ' now we have 3 second to measure the Supply Current

' in Active Mode  
Enable Interrupts  
' Now call Powerdown function  
Config Powermode = Powerdown

' Here you have time to measure PowerDown current consumption until a Low Level 

' on Portb.1 which is the PowerDown wake-up  
Loop  
'###############################################################################  
End  
  
```
Int0_isr:  
```vb
' wake_up  
Return

```

---

## UDPREAD

Action

Reads data via UDP protocol.

Syntax

Result = UDPREAD( socket , var, bytes)

Remarks

Result | A byte variable that will be assigned with 0, when no errors occurred. When an error occurs, the value will be set to 1. When there are not enough bytes in the reception buffer, the routine will wait until there is enough data or the socket is closed.  
---|---  
socket | The socket number you want to read data from (0-3). Or 0-7 for W5200/W5300  
Var | The name of the variable that will be assigned with the data from the socket.  
Bytes | The number of bytes to read.  
  
Reading strings is not supported for UDP.

When you need to read a string you can use the OVERLAY option of DIM.

There will be no check on the length so specifying to receive 2 bytes for a byte will overwrite the memory location after the memory location of the byte.

W3100

The socketstat function will return a length of the number of bytes + 8 for UDP. This because UDP also includes an 8 byte header. It contains the length of the data, the IP number of the peer and the port number.

The UDPread function will fill the following variables with this header data:

Peersize, PeerAddress, PeerPort

These variables are dimensioned automatically when you use CONFIG TCPIP.

W5100,W5200,W5300

The peersize, peerport and peeraddress have a different order in the W5x00. To avoid mistakes, the compiler will create these variables automatic in the proper order. The NOUDP=1 option can disable this feature if you do not use UDP.

When reading UDP, you need to use the [UDPREADHEADER](udpreadheader.md) statement to read the UDP header. After reading the header, the peersize, peerport and peeraddress variables are set.

You then should use the peersize variable to determine the number of bytes to retrieve. You must read all these bytes. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITE](udpwrite.md), [UDPWRITESTR](udpwritestr.md) , [UDPREADHEADER](udpreadheader.md) , [IP2STR](ip2str.md), [URL2IP](url2ip.md)

Example W3100

```vb
'-----------------------------------------------------------------------------------------

'name : udptest.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : start the easytcp.exe program after the chip is programmed and

' press UDP button

'micro : Mega161

'suited for demo : no

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "m161def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Print "Init , set IP to 192.168.0.8" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 0.0.0.0 , Localport = 1000 , Tx = $55 , Rx = $55

'Use the line below if you have a gate way

'Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Dim Idx As Byte ' socket number

Dim Result As Word ' result

Dim S(80) As Byte

Dim Sstr As String * 20

Dim Temp As Byte , Temp2 As Byte ' temp bytes

'--------------------------------------------------------------------------------------------

'When you use UDP, you need to dimension the following variables in exactly the same order !

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

'--------------------------------------------------------------------------------------------

Declare Function Ipnum(ip As Long) As String ' a handy function

'like with TCP, we need to get a socket first

'note that for UDP we specify sock_dgram

```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000

```vb
Print "Socket " ; Idx ; " " ; Idx

'UDP is a connection less protocol which means that you can not listen, connect or can get the status

'You can just use send and receive the same way as for TCP/IP.

'But since there is no connection protocol, you need to specify the destination IP address and port

'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT

Do

```
Temp = Inkey() ' wait for terminal input

If Temp = 27 Then ' ESC pressed

Sstr = "Hello"

Result = Udpwritestr(192.168.0.3 , 5000 , Idx , Sstr , 255)

End If

Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

```vb
If Result > 0 Then

Print "Bytes waiting : " ; Result

```
Temp2 = Result - 8 'the first 8 bytes are always the UDP header which consist of the length, IP number and port address

Temp = Udpread(idx , S(1) , Result) ' read the result

```vb
For Temp = 1 To Temp2

Print S(temp) ; " " ; ' print result

Next

Print

Print Peersize ; " " ; Peeraddress ; " " ; Peerport ' these are assigned when you use UDPREAD

Print Ipnum(peeraddress) ' print IP in usual format

```
Result = Udpwrite(192.168.0.3 , Peerport , Idx , S(1) , Temp2) ' write the received data back

```vb
End If

Loop

'the sample above waits for data and send the data back for that reason temp2 is subtracted with 8, the header size

'this function can be used to display an IP number in normal format

Function Ipnum(ip As Long) As String

```
Local T As Byte , J As Byte

Ipnum = ""

For J = 1 To 4

T = Ip And 255

Ipnum = Ipnum + Str(t)

If J < 4 Then Ipnum = Ipnum + "."

Shift Ip , Right , 8

```vb
Next

End Function

End

```

---

## UDPREADHEADER

Action

This statement reads the UDP header from the specified socket.

Syntax

UDPREADHEADER socket

Remarks

UDP packets start with a 8 byte header. This header contains the peer address, port and packet size. The UDPREADHEADER reads the header and places the information into the variables PEERADDRESS, PEERPORT and PEERSIZE.

After you have read the UDP header, you can use PEERSIZE to read the number of bytes available in the packet. 

Socket is a constant or variable in the range from 0-3. And 0-7 for the W5200/W5300.

UDPREADHEADER is only available for the W5x00.

See also

[UDPREAD](udpread.md), [CONFIG TCPIP](config_tcpip.md) , [TCPREADHEADER](tcpreadheader.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : udptest_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : start the easytcp.exe program after the chip is programmed and  
' press UDP button  
'micro : Mega88  
'suited for demo : no  
'commercial addon needed : yes  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 64 ' default use 32 for the hardware stack  
$swstack = 64 ' default use 10 for the SW stack  
$framesize = 50 ' default use 40 for the frame space  
  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
```vb
Print "Init , set IP to 192.168.1.70" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 5000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
  
  
  
Dim Idx As Byte ' socket number  
Dim Result As Word ' result  
Dim S(255) As Byte  
Dim Sstr As String * 255  
Dim Temp As Byte , Temp2 As Byte ' temp bytes  
  
```
Const Showresult = 1  
  
```vb
Print "UDP demo"  
  
Dim Ip As Long  
```
Ip = Maketcp(192.168.1.3) 'assign IP num  
  
```vb
'like with TCP, we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx ; " " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
Do  
```
Temp = Inkey() ' wait for terminal input  
If Temp = 27 Then ' ESC pressed  
Sstr = "Hello"  
Result = Udpwritestr(ip, 5000, Idx, Sstr, 255)  
Elseif Temp = 32 Then ' space  
```vb
Do  
Waitms 200  
Dim Tel As Long : Incr Tel  
```
Sstr = "0000000000111111111122222222223333333333 " + Str(tel)  
Result = Udpwritestr(ip , 5000 , Idx , Sstr , 255)  
```vb
Loop  
End If  
```
Result = Socketstat(idx, Sel_recv) ' get number of bytes waiting  
```vb
If Result > 0 Then  
Print "Bytes waiting : " ; Result  
  
```
Udpreadheader Idx ' read the udp header  
  

```vb
#if Showresult  
Print  
Print Peersize; " "; Peeraddress; " "; Peerport ' these are assigned when you use UDPREAD  
Print Ip2str(peeraddress) ' print IP in usual format  

#endif  
  
  
If Peersize > 0 Then ' the actual number of bytes  
Print "read" ; Peersize  
```
Temp = Udpread(idx, S(1), Peersize) ' read the result  
  

```vb
#if Showresult  
For Temp = 1 To Peersize  
Print S(temp); " " ; ' print result  
Next  
Print "done"  

#endif  
```
Result = Udpwrite(ip, Peerport, Idx, S(1), Peersize) ' write the received data back  
```vb
End If  
End If  
Loop  
'the sample above waits for data and send the data back for that reason temp2 is subtracted with 8, the header size  
  
  
End

```

---

## UDPWRITE

Action

Write UDP data to a socket.

Syntax

Result = UDPwrite( IP, port, socket , var , bytes)

Result = UDPwrite( IP, port, socket , EPROM, address , bytes)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
IP | The IP number you want to send data to. Use the format 192.168.0.5 or use a LONG variable that contains the IP number.  
Port | The port number you want to send data too.  
Socket | The socket number you want to send data to(0-3).  
Var | A constant string like "test" or a variable. When you send a constant string, the number of bytes to send does not need to be specified.  
Bytes | A word variable or numeric constant that specifies how many bytes must be send.  
Address | The address of the data stored in the chips internal EEPROM. You need to specify EPROM too in that case.  
EPROM | An indication for the compiler so it knows that you will send data from EPROM.  
  
The UDPwrite function can be used to write data to a socket that is stored in EEPROM or in memory.

When you want to send data from an array, you need to specify the element : var(idx) for example.

Note that UDPwrite is almost the same as TCPwrite. Since UDP is a connection-less protocol, you need to specify the IP address and the port number.

![notice](notice.jpg) UDP only requires an opened socket. The is no connect or close needed.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITESTR](udpwritestr.md) , [UDPREAD](udpread.md) , [UDPREADHEADER](udpreadheader.md), [URL2IP](url2ip.md)

Example

See [UDPwriteStr](udpwritestr.md)

---

## UDPWRITESTR

Action

Sends a string via UDP.

Syntax

Result = UDPwriteStr( IP, port, socket , var , param)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
IP | The IP number you want to send data to. Use the format 192.168.0.5 or use a LONG variable that contains the IP number.  
Port | The port number you want to send data too.  
Socket | The socket number you want to send data to (0-3).  
Var | The name of a string variable.  
Param | A parameter that might be 0 to send only the string or 255, to send the string with an additional CR + LF This option was added because many protocols expect CR + LF after the string.  
  
The UDPwriteStr function is a special variant of the UDPwrite function.

It will use UDPWrite to send the data.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITE](udpwrite.md), [UDPREAD](udpread.md), [URL2IP](url2ip.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : udptest.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : start the easytcp.exe program after the chip is programmed and

' press UDP button

'micro : Mega161

'suited for demo : no

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "m161def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

```
Const Sock_stream = $01 ' Tcp

Const Sock_dgram = $02 ' Udp

Const Sock_ipl_raw = $03 ' Ip Layer Raw Sock

Const Sock_macl_raw = $04 ' Mac Layer Raw Sock

Const Sel_control = 0 ' Confirm Socket Status

Const Sel_send = 1 ' Confirm Tx Free Buffer Size

Const Sel_recv = 2 ' Confirm Rx Data Size

'socket status

Const Sock_closed = $00 ' Status Of Connection Closed

Const Sock_arp = $01 ' Status Of Arp

Const Sock_listen = $02 ' Status Of Waiting For Tcp Connection Setup

Const Sock_synsent = $03 ' Status Of Setting Up Tcp Connection

Const Sock_synsent_ack = $04 ' Status Of Setting Up Tcp Connection

Const Sock_synrecv = $05 ' Status Of Setting Up Tcp Connection

Const Sock_established = $06 ' Status Of Tcp Connection Established

Const Sock_close_wait = $07 ' Status Of Closing Tcp Connection

Const Sock_last_ack = $08 ' Status Of Closing Tcp Connection

Const Sock_fin_wait1 = $09 ' Status Of Closing Tcp Connection

Const Sock_fin_wait2 = $0a ' Status Of Closing Tcp Connection

Const Sock_closing = $0b ' Status Of Closing Tcp Connection

Const Sock_time_wait = $0c ' Status Of Closing Tcp Connection

Const Sock_reset = $0d ' Status Of Closing Tcp Connection

Const Sock_init = $0e ' Status Of Socket Initialization

Const Sock_udp = $0f ' Status Of Udp

Const Sock_raw = $10 ' Status of IP RAW

```vb
$lib "tcpip.lbx" ' specify the tcpip library

Print "Init , set IP to 192.168.0.8" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 0.0.0.0 , Localport = 1000 , Tx = $55 , Rx = $55

'Use the line below if you have a gate way

'Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Dim Idx As Byte ' socket number

Dim Result As Word ' result

Dim S(80) As Byte

Dim Sstr As String * 20

Dim Temp As Byte , Temp2 As Byte ' temp bytes

'--------------------------------------------------------------------------------------------

'When you use UDP, you need to dimension the following variables in exactly the same order !

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

'--------------------------------------------------------------------------------------------

Declare Function Ipnum(ip As Long) As String ' a handy function

'like with TCP, we need to get a socket first

'note that for UDP we specify sock_dgram

```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000

```vb
Print "Socket " ; Idx ; " " ; Idx

'UDP is a connection less protocol which means that you can not listen, connect or can get the status

'You can just use send and receive the same way as for TCP/IP.

'But since there is no connection protocol, you need to specify the destination IP address and port

'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT

Do

```
Temp = Inkey() ' wait for terminal input

If Temp = 27 Then ' ESC pressed

Sstr = "Hello"

Result = Udpwritestr(192.168.0.3 , 5000 , Idx , Sstr , 255)

End If

Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

```vb
If Result > 0 Then

Print "Bytes waiting : " ; Result

```
Temp2 = Result - 8 'the first 8 bytes are always the UDP header which consist of the length, IP number and port address

Temp = Udpread(idx , S(1) , Result) ' read the result

```vb
For Temp = 1 To Temp2

Print S(temp) ; " " ; ' print result

Next

Print

Print Peersize ; " " ; Peeraddress ; " " ; Peerport ' these are assigned when you use UDPREAD

Print Ipnum(peeraddress) ' print IP in usual format

```
Result = Udpwrite(192.168.0.3 , Peerport , Idx , S(1) , Temp2) ' write the received data back

```vb
End If

Loop

'the sample above waits for data and send the data back for that reason temp2 is subtracted with 8, the header size

'this function can be used to display an IP number in normal format

Function Ipnum(ip As Long) As String

```
Local T As Byte , J As Byte

Ipnum = ""

For J = 1 To 4

T = Ip And 255

Ipnum = Ipnum + Str(t)

If J < 4 Then Ipnum = Ipnum + "."

Shift Ip , Right , 8

```vb
Next

End Function

End

```

---

## URL2IP

Action

This function returns the IP address of an URL.

Syntax

ip=URL2IP(URL)

Remarks

This function performs a DNS query to the google DNS server with address 8.8.8.8.

It returns either a 0 IP address or the IP address of the URL.

The URL must be a string or string constant.

At the moment, this function is only supported by the W5100 and W5200.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [BASE64ENC](base64enc.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : PING_SPI.bas http://www.faqs.org/rfcs/rfc792.html  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : Simple PING program  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 64 for the hardware stack  
$swstack = 64 ' default use 64 for the SW stack  
$framesize = 180 ' default use 80 for the frame space  
  
  
```
Const Cdebug = 1  
  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
  
'Configuration Of The SPI bus  
Config Spi = Hard , Interrupt = Off , Data_order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
  
```vb
'we do the usual  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1 , Cs = Portb.2  
Print "Init done"  
  
Dim Idx As Byte , Result As Word , J As Byte , Res As Byte  
Dim Ip As Long  
Dim Dta(12) As Byte , Rec(12) As Byte  
  
  
```
Dta(1) = 8 'type is echo  
Dta(2) = 0 'code  
  
Dta(3) = 0 ' for checksum initialization  
Dta(4) = 0 ' checksum  
Dta(5) = 0 ' a signature can be any number  
Dta(6) = 1 ' signature  
Dta(7) = 0 ' sequence number - any number  
Dta(8) = 1  
Dta(9) = 65  
  
```vb
Dim W As Word At Dta(1) + 2 Overlay 'same as dta(3) and dta(4)  
Dim B As Byte  
```
W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)  
  

```vb
#if Cdebug  
For J = 1 To 9  
Print Dta(j)  
Next  

#endif  
  
```
Ip = Url2ip( "mcselec.com")  
```vb
Print Ip2str(ip)  
If Ip = 0 Then End  
  
  
Print "Socket " ; Idx ; " " ; Idx  
```
Setipprotocol Idx , 1 'set protocol to 1  
'the protocol value must be set BEFORE the socket is openend  
  
Idx = Getsocket(idx , 3 , 5000 , 0)  
  
```vb
Do  
' Result = Gettcpregs(&H403 , 2) : Print Hex(result)  
  
' Print Hex(s_status(1))  
```
Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) 'write ping data '  
```vb
Print "W:" ; Result  
Waitms 300 ' depending on the hops, speed, etc  
```
Result = Socketstat(idx , Sel_recv) 'check for data  
```vb
Print "REC:" ; Result  
If Result >= 11 Then  
Print "Ok"  
```
Res = Tcpread(idx , Rec(1) , Result) 'get data with TCPREAD !!!  

```vb
#if Cdebug  
Print "DATA RETURNED :" ; Res '  
For J = 1 To Result  
Print Rec(j) ; " " ;  
Next  
Print  

#endif  
Else 'there might be a problem  
Print "Network not available"  
End If  
Waitms 10000  
Loop

```

---
