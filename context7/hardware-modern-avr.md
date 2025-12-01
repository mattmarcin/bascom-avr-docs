# Modern AVR Hardware

> XMEGA, xTiny, MegaX, and AVR-Dx series documentation

## Adding XRAM to XMEGA using EBI

This information has been provided by Electronic Design Bitzer.

Some XMEGA processors have an EBI. The following circuit shows how to set up the EBI for 8 bit bus mode where the SRAM can be selected with a jumper.

128 KB SM621008VLLP70T : SRAM LLPow 3,3V 128Kx8 70ns TSOP32(I)

512 KB SM624008VLLP70M : SRAM LLPow 3,3V 512Kx8 70ns SOP32

The BASCOM setup code : 

```vb
' All EBI-Ports must be set to OUTPUT

' All Ports, ACTIVE-LOW , must be set to 1 !!!

' All Ports, ACTIVE-HIGH, must be set to 0 !!!

```
Porth_dirset = &B1111_1111 : Porth = &B1111_0011 'WR, RD, ALE1, ALE2, CS0-3 = output : ALE1 & 2 auf 0 !!!

Portj_dirset = &B1111_1111 : Portj = &B1111_1111

Portk_dirset = &B1111_1111 : Portk = &B1111_1111

Config Xram = 3port , Ale = Ale12 , Sdbus = 8 , Modesel0 = Sram , Adrsize0 = 256b , Waitstate0 = 4 , Baseadr0 = &H10000 , _

Modesel1 = Sram , Adrsize1 = 128k , Waitstate1 = 1 , Baseadr1 = &H20000

See also : [CONFIG XRAM](configxram.md)

![xram-ebi](xram-ebi.zoom58.png)

---

## ATMEGA4809

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md) and [MEGAX](megax.md).

The ATMEGA4809 comes in different casings. It has 48KB of flash and a maximum of 48 pins. 

There is a DIP version with 40 pins with the same die. PORTB has no pins however

![atmegax4809-40](atmegax4809-40.png)

![atmegax4809-48](atmegax4809-48.png)

![atmegax4809-32](atmegax4809-32.png)

![atmegax4809-28](atmegax4809-28.png)

---

## ATTINY1604

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY204, 404, 804 and 1604 are the 2K/4K/8K/16K flash variants 

![attiny204_404_804_1604](attiny204_404_804_1604.png)

---

## ATTINY1606

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY406, 804 and 1606 are the 4K/8K/16K flash variants 

![attiny806_1606](attiny806_1606.png)

---

## ATTINY1607

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY807 and 1607 are 8K/16K flash variants 

![attiny807_1607](attiny807_1607.png)

---

## ATTINY1614

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY1614/1616 and 1617 are 16K flash variants in 14/20/24 pin variants

![attiny1614](attiny1614.png)

---

## ATTINY1616

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY1614/1616 and 1617 are 16K flash variants in 14/20/24 pin variants

![attiny1616](attiny1616.png)

---

## ATTINY1617

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY1614/1616 and 1617 are 16K flash variants in 14/20/24 pin variants

![attiny417_817](attiny417_817.png)

---

## ATTINY202

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY202 and ATXTINY402 are the 2K/4K flash variants 

\- The manufacturer inc files have reference to VPORTB/VPORTC but these do not exist

![attiny202_402](attiny202_402.png)

---

## ATTINY204

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY204, 404, 804 and 1604 are the 2K/4K/8K/16K flash variants 

![attiny204_404_804_1604](attiny204_404_804_1604.png)

---

## ATTINY212

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY212 and 412 are the 2K/4K flash variants 

![attiny212_412](attiny212_412.png)

---

## ATTINY214

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY214/414 and ATXTINY814 are the 2K/4K/8K flash variants 

![attiny214_414_814](attiny214_414_814.png)

---

## ATTINY3216

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY3216 and 3217 are the 32K flash variants in 20 pin and 24 pin casings

![attiny3216-soic20](attiny3216-soic20.png)

---

## ATTINY3217

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY3216 and 3217 are the 32K flash variants in 20 pin and 24 pin casings

![attiny3217-qfn24](attiny3217-qfn24.png)

---

## ATTINY402

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY202 and ATXTINY402 are the 2K/4K flash variants 

\- The manufacturer inc files have reference to VPORTB/VPORTC but these do not exist

![attiny202_402](attiny202_402.png)

---

## ATTINY404

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY204, 404, 804 and 1604 are the 2K/4K/8K/16K flash variants 

![attiny204_404_804_1604](attiny204_404_804_1604.png).

---

## ATTINY406

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY406, 804 and 1606 are the 4K/8K/16K flash variants 

![attiny406](attiny406.png)

---

## ATTINY412

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY212 and 412 are the 2K/4K flash variants 

![attiny212_412](attiny212_412.png)

---

## ATTINY414

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY214/414 and ATXTINY814 are the 2K/4K/8K flash variants 

![attiny214_414_814](attiny214_414_814.png)

---

## ATTINY416

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY416 and 816 are the 4K/8K flash variants 

![atxtiny416_816](atxtiny416_816.png)

---

## ATTINY417

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY417 and 817 are the 4K/8K flash variants in 24 pin casing

![attiny417_817](attiny417_817.png)

---

## ATTINY804

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY204, 404, 804 and 1604 are the 2K/4K/8K/16K flash variants 

![attiny204_404_804_1604](attiny204_404_804_1604.png)

---

## ATTINY806

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY406, 804 and 1606 are the 4K/8K/16K flash variants 

![attiny806_1606](attiny806_1606.png)

---

## ATTINY807

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY807 and 1607 are 8K/16K flash variants 

![attiny807_1607](attiny807_1607.png)

---

## ATTINY814

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY214/414 and ATXTINY814 are the 2K/4K/8K flash variants 

![attiny214_414_814](attiny214_414_814.png)

---

## ATTINY816

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY416 and 816 are the 4K/8K flash variants 

![atxtiny416_816](atxtiny416_816.png)

---

## ATTINY817

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md).

The ATTINY417 and 817 are the 4K/8K flash variants in 24 pin casing

![attiny417_817](attiny417_817.png)

---

## ATXMEGA

The ATXMEGA is a great new chip. It has a lot of hardware on board and a huge amount of hardware registers.

Some changes in the architecture are however breaking compatibility with normal AVR (ATMEGA/ATTINY) processors.

Dont miss the FAQ - ATXMEGA section below !

The ATXMEGA bring a huge amount of interfaces like UART, I2C, SPI, Counter/Timer, 12-Bit Analog Input/Output and also new features like [DMA](config_dmachx.md) (Direct Memory Access), the [Event System](config_event_system.md) or AES hardware encryption/decryption.

Regarding more infos on ATXMEGA ANALOG DIGITAL CONVERTER (ADC) see here:

[CONFIG ADCX](config_adca.md)

All ATXMEGA have their registers at the same address. Some chips might not have all registers because the hardware is not inside the chip, but all DAT* files are similar. And all hardware has a fixed offset. This allows to use dynamic code. For example Bascom-AVR can now use a variable for the UART and the code is only needed once because all hardware has a fixed offset.

* DAT files are the register files. The register files are stored in the BASCOM-AVR application directory and they all have the DAT extension. The register file holds information about the chip such as the internal registers and interrupt addresses. The register file info is derived from ATMEL definition files.

The ATXMEGA work with 3.3V so please do not connect something which output 5V to the XMEGA Pin's. Use a Level Shifter for that. 

The maximum rating for a ATXMEGA Pin is 3.6 V. 

When using the internal 32MHz oscillator you need at least 2.7V Vcc. The internal 32MHz oscillator is stable enough for a lot of applications. The maximum CPU Clock Frequency is 12MHz when using the XMEGA with just 1.6V Vcc.

Read Application Note [AVR1012: XMEGA A Schematic Checklist](<http://www.atmel.com/dyn/resources/prod_documents/doc8278.pdf>) for special considerations in your hardware design.

You can find Bascom samples for ATXMEGA in Bascom-AVR folder:

•| General samples â¦â¦..\BASCOM-AVR\SAMPLES\XMEGA  
---|---  
  
•| Bootloader samples in â¦â¦â¦\BASCOM-AVR\SAMPLES\BOOT  
---|---  
  
•| For chips like xm128a1 in â¦â¦.\BASCOM-AVR\SAMPLES\CHIPS  
---|---  
  
Manuals for ATXMEGA: There are 2 manuals available from ATMEL for every ATXMEGA Chip

1.| One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual  
---|---  
  
2.| Another Manual for the single chips like for example for an ATXMEGA128A1 it is the ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the Alternate Pin Functions. So you can find which Pin on Port C is the SDA and SCL Pin when you want to use the I2C/TWI Interface of this Port.  
---|---  
  
Beside the Manuals for the ATXMEGA chips there are a lot of Appliaction Notes available on the ATMEL website which explain for example the ATXMEGA Event System or Direct Memory Access (DMA) and so forth.

What you need to get started with ATXMEGA and BASCOM-AVR

1.| The latest Bascom-AVR FULL Version (The Demo Version of Bascom-AVR do not support ATXMEGA).   
---|---  
  
2.| An evaluation board like the Atmel AVR XMEGA® Xplained evaluation kit or any other ATXMEGA evaluation board with PDI (Program and Debug Interface) header.  
---|---  
  
3.| A Programmer like AVRISP MKII or any other PDI or JTAG programmer which support ATXMEGA.  
---|---  
  
4.| Latest AVR-Studio 4.X or 5.X only for setting fuse bits and to flash Bootloader to ATXMEGA.  
---|---  
  
5.| Programming the ATXMEGA can be done direct from BASCOM-IDE. See also [LIBUSB](libusb.md) for further information.  
---|---  
  
The most important parts of an Bascom-AVR Program for XMEGA are:

1.|  The Register file for the chip, crystal init and Stacks   
---|---  
  
```vb
$regfile = "xm128a1def.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 64

```
2.| Enable and configure the oscillator of your choice:  
---|---  
  
Config Osc = Enabled , 32mhzosc = Enabled ' enable 2 MHz and 32 MHz internal oscillators

3.| Select the oscillator source for the system clock and prescaler (this must match with $crystal = XXXXXX). The following configure the internal 32MHz oscillator as system clock without prescaler so the system clock is 32MHz which match with $crystal = 32000000  
---|---  
  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1 

4.| If you intend to use interrupts you need to configure it before you use the Enable Interrupt command. Bascom-AVR will automatically enable the medium level interrupt when Enable Interrupt is in the code but not the low and high level interrupts.  
---|---  
  
Config Priority = Static , Vector = Application , Lo = Enabled , Med = Enabled , Hi = enabled

5.| Also when you want to use EEPROM you need to configure it before you can use it:  
---|---  
  
Config Eeprom = Mapped 'Setup memory mode for EEPROM in XMEGA

6.| After this you can add Enable Interrupts and your code in the Main Loop.  
---|---  
  
```vb
Do  
'Insert your code  
Loop

```
7.| End  
---|---  
  
End 'end program 

A first simple program with ATXMEGA which toggle an output every second:

```vb
$regfile = "xm64a3def.dat"  
$crystal = 32000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Portb = Output  
  
Do  
toggle Portb.0  
Waitms 1000  
loop  
  
end 'end program

```
FAQ - ATXMEGA

Q: How to set clock source and clock frequency with ATXMEGA ?

A: See [CONFIG OSC](config_osc.md) and [CONFIG SYSCLOCK](config_sysclock.md)

Q: Do I need to set the XMEGA fuses to get started ?

A: No, to get started there is no need to set the fuses because opposed to megaAVR or ATTINY, where fuses are used to set the clock source and frequency you can set the clock source and frequency in the program by Bascom-AVR. 

You also do not need an external clock source. You can use the internal 32MHz or 2MHz RC oscillator as clock source.

Q: Which Interrupt Level (Low, Med, High) is used when I do not specify the priority ?

A: MED is used when the priority is not specified.

Q: Is AVR-DOS supported for XMEGA ?

A: Yes, see [AVR-DOS File System](avr_dos_file_system.md)

Q: What else is supported (Status: Bascom-AVR 2.0.7.6) where users of Bascom-AVR forum asked for ?

A: Following list:

\- 1-WIRE, EEPROM, XRAM, Event System, Config Servos, AVR-DOS SDHC driver, DCF77, RTC32,

\- INP/OUT support Xmega huge memory, xmega LCD simulation, dmxslave, RS-485, pulsein, pulseout, DMA

\- Bascom Simulator, Event System, getrc5, CONFIG POWER_REDUCTION, buffered serial output (com1-com4)

\- virtual portmap config, config tcXX for xmega timers, xmega comparator, $forcesofti2c will force the xmega to use software i2c

\- AES encyption/decryption, xmega TWI, SPI, UART

Q: Where do I find which pin of ATXMEGA is SDA and SCL ?

A: There are 2 manuals available from ATMEL

1\. One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual

2\. Another Manual for the single chips like for example for an ATXMEGA128A1 it is the

ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the

Alternate Pin Functions. So you can find which Pin on Port C is the SDA and SCL Pin when you want to

use the I2C/TWI Interface of this Port.

Q: How to program/flash an ATXMEGA ?

A: There is no ISP programming support. Only JTAG and PDI is supported. Of course the MCS Bootloader can be used but you need to program the chip first with for example an AVRISP MKII programmer. After this programming the 

ATXMEGA can be done direct from BASCOM-IDE

Important is also that the AVRISP MKII programmer need 3.3V supply voltage from the Target.

Q: Is there a special boot loader source code I can use for ATXMEGA ?

A: There are example boot loader in following Bascom-AVR folder (C:\\......\BASCOM-AVR\SAMPLES\BOOT)

like ATXMEGA32A4 or ATXEMGA128A1. For other ATXMEGA Chips the source code can be easily adapted.

Q: What is the Program and Debug Interface (PDI) ?

A: The Program and Debug Interface (PDI) is an Atmel proprietary interface for external programming and on-chip 

debugging of a device. 

âThe XMEGA doesnât have the SPI based In-System Programming (ISP) interface for 

external programming, which has been used for megaAVR. Nor does it have the 

debugWIRE interface. These have been replaced by a two wire âProgramming and 

Debugging Interfaceâ (PDI).â [from Atmel App Note AVR1005]

Q: How to read/write from/to ATXMEGA Register ?

A: If you want or need to write or read ATXMEGA Registers direct you just need to find the name by using the 

ATXMEGA DAT file.

For example if you want to read the ATXMEGA Revision there is the register Mcu_revid in the DAT file.

The DAT files can be found in the BASCOM-AVR folder.

Take care with protected registers. Before you can write to this registers you need to release it. An example for this is the Software Reset.

Q: How to initiate a software Reset of an ATXMEGA ?

A: Before you can write the Software Reset Bit you need to release the write protection for this bit and register.

'enable change of protected Registers for following 4 CPU Instruction Cycles  
CPU_CCP = &HD8  
'Initiate Software Reset by setting Bit0 of RST_CTRL Register  
Rst_ctrl.0 = 1 'When this bit is set a software reset occur

Q: How are External Interrupts (Port Interrupt) used with ATXMEGA ?

A: Each XMEGA port (like PortA or PortF) with pin's from Pin0....Pin7 has 2 interrupts (INT0 and INT1). So there is INT0 and INT1 available for every port.

Port Interrupts must be enabled before they can be used like for example Int1 on PortA = PORTA_INT1

Steps to use PortE.0 as Port Interrupt where INT0 is used:

1\. enable the INT0 Interrupt on Port E

```vb
On Porte_int0 Port_e_int0__isr  
Enable Porte_int0 , Lo 'Enable this Interrupt as Lo Level Interrupt  
Enable Interrupts

```
2\. Config Porte.0 as Input:

Config Pine.0 = Input 'Set PINE.0 as Input 

3\. Configure the reaction:

Config Xpin = Porte.0 , Outpull = Pullup , Sense = Falling 'enable Pull up and reaction on falling edge 

4\. Set the interrupt mask (which pin will be activated to generate an INT0 in this case):

Porte_int0mask = &B0000_0001 'include PIN0 in INT0 Mask 

1 = Pin is activated for interrupt

0 = Pin is deactivated for interrupt

You could also set more pin's as activated (set to 1) but then you need to check in the interrupt service routine which pin was the root cause for generating the interrupt.

5\. The Interrupt Service Routine:

'Port E INT0 Interrupt Service Routine  
Port_e_int0__isr:

  
```vb
'do something....

  
Return

```
Additional info for Port Interrupts:

For asynchronous sensing, only port pin 2 on each port has full asynchronous sense support. This means that for edge

detection, pin 2 will detect and latch any edge and it will always trigger an interrupt request. The other port pins have

limited asynchronous sense support [ATXMEGA A Manual].

See also below for an example for Port Interrupt (External Interrupt) 

Q: For what do I need Fuse Bits (Fuses) with ATXMEGA ?

A: âThe Fuses are used to set important system function and can only be written from an external

programming interface. The application software can read the fuses. The fuses are used to configure

```vb
reset sources such as Brown-out Detector and Watchdog, Start-up configuration, JTAG

enable and JTAG user ID, Bootloaderâ¦..An unprogrammed fuse or lock bit will have the value one, while a 

```
programmed flash or lock bit will have the value zero..â [ATXEMGA A Manual]

Q: How to write to 16-Bit (Word) Register of ATXMEGA ?

A: You do not care about the 16-Bit (Word) Register because the compiler will handle this for you automatic.

```vb
For this you can find the [WIO] (Word IO) Section in the DAT file. You can only write direct to 16-Bit Register over the defined register in the [WIO] section of the DAT file

If there is a need to manual write/read to/from 16-Bit register you always need to write/read the LOW Byte (LSB) 

```
and then the HIGH Byte (MSB). 

Q: Is there also a linear memory architecture as with ATMEGA or ATTINY AVR's ?

A: The power of the AVR is/was the linear memory architecture. In the ATXMEGA this has been changed : the registers are placed into a separate address space. This makes code like this fail:

Clr r31

Ldi r30,10 ; point to register R10

Ld r24,z+ ; load value from R10 and inc pointer

Code like LDS r16, 0 will not load the content of register R0 either with Xmega

If your ASM code contains such code you need to rewrite it.

Q: Is the Bascom-AVR Demo version supporting ATXMEGA ?

A: ATXMEGA is not available in PDIP. This means that the ATXMEGA is not really suited for hobby projects. 

As a result, the DEMO version does not support the ATXMEGA.

Q: For what are Virtual Port Registers good for ?

A: âVirtual port registers allow for port registers in the extended I/O memory space to be mapped virtually

in the I/O memory space. When mapping a port, writing to the virtual port register will be

the same as writing to the real port register. This enables use of I/O memory specific instructions

for bit-manipulation, and the I/O memory specific instructions IN and OUT on port register that

normally resides in the extended I/O memory space. There are four virtual ports, so up to four

ports can be mapped virtually at the same time. The mapped registers are IN, OUT, DIR and

INTFLAGS.â [from ATXMEGA A Manual]

Q: On which port of ATXMEGA can I find the COM1.....COM8 ?

A: See table below:

COM1 --> Usartc0  
COM2 --> Usartc1  
COM3 --> Usartd0  
COM4 --> Usartd1  
COM5 --> Usarte0  
COM6 --> Usarte1  
COM7 --> Usartf0  
COM8 --> Usartf1

Q: Is Serialin and Serialout supported for UART Interfaces above COM4

A: Yes since version 2077 all 8 UARTS support buffered serial input and output.

For ATXMEGA the first 4 UARTS can use for example serialin:

SERIALIN : first UART/UART0 --> COM1  
SERIALIN1 : second UART/UART1 --> COM2  
SERIALIN2 : third UART/UART2 --> COM3  
SERIALIN3 : fourth UART/UART3 --> COM4  
SERIALIN4 : fourth UART/UART4 --> COM5  
SERIALIN5 : fourth UART/UART5 --> COM6  
SERIALIN6 : fourth UART/UART6 --> COM7  
SERIALIN7 : fourth UART/UART7 --> COM8  


For example with an ATXMEGA128A1 you get 8 UARTS:

Every of the 8 USARTâs has for example a Receive Interrupt which you can use to analyze incoming data:

ATXMEGA128A1 Receive Interrupts:  
COM1 --> Usartc0_rxc  
COM2 --> Usartc1_rxc  
COM3 --> Usartd0_rxc  
COM4 --> Usartd1_rxc  
COM5 --> Usarte0_rxc  
COM6 --> Usarte1_rxc  
COM7 --> Usartf0_rxc  
COM8 --> Usartf1_rxc

In the interrupt routine you need to use the inkey(#X) function because inkey(#X) is reading the data register and 

therefore reset the interrupt flag. Without reading the data register or resetting the interrupt flag manual the 

interrupt will fire again and again.

Example the interrupt routine:

Rxc_isr:  
Rs232 = Inkey(#1)  
```vb
'do something with the data  
Return

```
Q: How to get the reason for a reset of ATXMEGA (like power on, watchdog or software rest)

A: There is a special register for that RST_STATUS you can read and analyze.

You can also read R0 register using GetReg(R0) function : myvar=GetReg(r0). You need to do this early in your code.

Q: How to auto calibrate the internal 2MHz and 32MHz Oscillators during runtime ? 

A: The automatic runtime calibration of internal oscillators is activated by enabling the DFLL (Digital Frequency-locked Loops) and autocalibration.

'The internal 32.768 KHz Oscillator is used for calibration

Osc_dfllctrl = &B00000000

```vb
'Enable DFLL and autocalibration   
Set Dfllrc32m_ctrl.0 

```
Additional hint from ATMEL for some chip revisions:

"....Both DFLLs and both oscillators has to be enabled for one to work

In order to use the automatic runtime calibration for the 2 MHz or the 32 MHz internal oscillators,

the DFLL for both oscillators and both oscillators has to be enabled for one to work.

Problem fix/Workarund

Enabled both DFLLs and oscillators when using automatic runtime calibration for one of the

internal oscillators....."

Q: How many Flash and EEPROM Write/Erase Cycles can be done with ATXMEGA ?

A: One write cycle consists of erasing a sector, followed by programming the same sector. You can find the maximum numbers for an ATXMEGA128A1 here: 

XMEGA Flash and EEPROM Write/Erase Cycles:

For ATxmega128A1 devices

Flash:

25°C - 10K Write/Erase cycles

85°C - 10KWrite/Erase cycles

EEPROM:

25°C 80K- Write/Erase cycles

85°C 30K- Write/Erase cycles

Example for XMEGA Port Interrupt (External Interrupt) from user hzz:

```vb
'-----------------------------------------------------------------------------------------------------------------------  
' Configuring external interrupts with XMEGA  
' Tested OK with BASCOM 2.0.7.5 and an XMEGA128A3 board by Chip45  
' 14-aug-2012  
'-----------------------------------------------------------------------------------------------------------------------  
'________________________________________________________________________________  
$regfile = "xm128a3def.dat"  
$hwstack = 256  
$swstack = 128  
$framesize = 128  
'________________________________________________________________________________  
' For 16MHz crystal  
$crystal = 32000000  
Config Osc = Disabled , Extosc = Enabled , Range = 12mhz_16mhz , Startup = Xtal_1kclk , 32khzosc = Enabled  
' Set PLL OSC conditions:  
```
Osc_pllctrl = &B1100_0010 ' reference external oscillator, set the PLL' multiplication factor to 2 (bits 0 - 4)  
Set Osc_ctrl.4 ' Enable PLL Oscillator  
Bitwait Osc_status.4 , Set ' wait until the pll clock reference source is stable  
Clk_ctrl = &B0000_0100 ' switch system clock to pll  
```vb
Config Sysclock = Pll , Prescalea = 1 , Prescalebc = 1_1  
'________________________________________________________________________________  
' Setup:  
```
Led1 Alias Portd.0 : Config Portd.0 = Output : Led1 = 1  
  
```vb
' Each XMEGA port has two interrupt vectors: INT0 and INT1.  
' For example, the XMEGA A3 has 7 ports: A, B, C, D, E, F, each with 8 pins ranging from pin0 to pin7, and port R, with just two pins, normally used by an external XTAL.  
' Therefore up to 12 pins can be used as external interrupts with an XMEGA A3 (or up to 14 if an external XTAL is not used and PORTR.0 and PORTR.1 are free)  
' For each port, any two pins can be defined as an external interrupt source as follows:  
' The following example configures the following ports as external interrupt sources:  
' PORTB.0 using interrupt vector INT0 of PORTB  
' PORTB.3 using interrupt vector INT1 of PORTB  
' (no more port B pins can be defined as external interruopt sources )  
' PORTA.3 using interrupt vector INT0 of PORTA  
  
' 1) Set the Interrupt Service Routines Labels for the interrupt vectors used and  
' enable interrupts setting the intrerrupt level:  
On Portb_int0 B0_b0_isr : Enable Portb_int0 , Hi  
On Portb_int1 B1_b3_isr : Enable Portb_int1 , Lo  
On Porta_int0 A0_a3_isr : Enable Porta_int0 , Lo  
' I choose the label names to indicate the interruopt vector used and the pin that will be assigned  
' next. For instance B1_b3_isr: uses INT vector 1 of port B assigned to pin b3  
  
' 2) Config pins as inputs and define what should cause the interrupt: low level, hi level, or transitions: rising, falling or both  
Config Portb.0 = Input : Config Xpin = Portb.0 , Sense = Rising  
Config Portb.3 = Input : Config Xpin = Portb.3 , Sense = Falling  
Config Porta.3 = Input : Config Xpin = Porta.3 , Sense = Both  
' Three switches are connected these pins, PORTB.0, PORTB.3 and PORTA.3, for testing  
  
' 3) Assign pins to interrupt vectors:  
```
Portb_int0mask = &B0000_0001 ' Assign pin b0 to Portb_int0  
Portb_int1mask = &B0000_1000 ' Assign pin b3 to Portb_int1  
Porta_int0mask = &B0000_1000 ' Assign pin a3 to Porta_int0  
  
```vb
' Notice that more than one pin can be assigned to the same vector. For instance, we could have  
' written:  
' PROTB_INT0MASK = &B0000_1001 ' Assign pin b0 and b3 to Portb_int0  
' In this case, both "b0" and "b3" pins will result in executing the same ISR (If possible, the ISR could  
' distinguish which pin has produced the interrupt and execute a different code. This is a way of  
' having more than two external interrupt sources per port). Another way will be assigning other  
' pins to event channels.  
  
' 4) Write the Interrupt service routines (locate then after the do loop where they will not be  
' executed except when they are called)  
' B0_b0_isr:  
' ' Do whatever at each rising edge of pin b0  
' Return  
'  
' B1_b3_isr:  
' ' Do whatever at each falling edge of pin b3  
' Return  
'  
' A0_a3_isr:  
' ' Do whatever at each rising and falling edges of pin a3  
' Return  
  
'5) Don't forget to enable interrupts and config priorities  
Enable Interrupts  
Config Priority = Static , Vector = Application , Lo = Enabled , Med = Enabled , Hi = Enabled  
'_________________________________________________________________________________  
Do  
' No need to do anything here  
Loop  
'_________________________________________________________________________________  
  
```
B0_b0_isr: ' The switch connected to PORTB.0 will toggle the LED each time it goes HI  
```vb
Toggle Led1  
Return  
  
```
B1_b3_isr: ' The switch connected to PORTB.3 will toggle the LED each time it goes LO  
```vb
Toggle Led1  
Return  
  
```
A0_a3_isr: ' The switch connected to PORTA.3 will toggle the LED each time it goes LO or HI  
```vb
Toggle Led1  
Return

```

---

## ATXMEGA128A1

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega128](atxmega128.png)

Question: The DVDSON FUSE BIT the ATxmega A MANUAL says that for characterization data on VDROP and tSD consult the device data sheet.  
(Device: ATXMEGA128A1 RevH). But I can't find this Information in the datasheet ?  
  
Answer: The voltage spike detector has been removed from the latest revision of the XMEGA A manual.  
This is because we have, unfortunately, not been able to validate the spike detector fully.  
  
Question: The calibration byte in the production signature row show 0xFF and 0x00 for the ADC Calibration byte. Are these really the calibration values ?  
Errata of Rev H don't show something from calibration bytes. (Device: ATXMEGA128A1 RevH)  
  
Answer: Yes this is a known issue with ATXMEGA128A1 RevH. We will be fixing up this  
issue in the later version of the device.  
  
You should write the code for loading the calibration registers in the  
firmware so that when we fix it in the later version you do not have to fix  
the code. Also loading it now will not cause any problem in the ADC  
operation.

---

## ATXMEGA128A3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_A3](atxmega_a3.png)

---

## ATXMEGA128A4U

![atxmega16a4u_32a4u_64a4u_128a4u](atxmega16a4u_32a4u_64a4u_128a4u.png)

---

## ATXMEGA128B1

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega64b1_128b1](atxmega64b1_128b1.png)

---

## ATXMEGA128B3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega128b3](atxmega128b3.png)

---

## ATXMEGA128C3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega32c3_64c3_128c3_192c3_256c3](atxmega32c3_64c3_128c3_192c3_256c3.png)

---

## ATXMEGA128D3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_d3](atxmega_d3.png)

---

## ATXMEGA128D4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega_d4](atxmega_d4.png)

---

## ATXMEGA16A4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega16a_32_64_128](atxmega16a_32_64_128.png)

---

## ATXMEGA16D4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega_d4](atxmega_d4.png)

---

## ATXMEGA16E5

\- The XMEGA E series requires that you reset the interrupt yourself. For example : TCC4_INTflags.0=1 'clear OV flag 

\- The ERASE_APP NVM command (&H20) erases the complete flash, thus the boot space included. Use &H25 instead to erase and write a page.

\- There is a fixed map for the virtual ports : 

VPORT0 - Virtual port A

VPORT1 - Virtual port C

VPORT2 - Virtual port D

VPORT3 - Virtual port R

\- CONFIG XPIN slewrate is for the whole port, not for an individual pin

![atxmega8E5_16E5_32E5](atxmega8e5_16e5_32e5.png)

---

## ATXMEGA192A3

'Show some textThis page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_A3](atxmega_a3.png)

---

## ATXMEGA192D3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_d3](atxmega_d3.png)

---

## ATXMEGA256A3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_A3](atxmega_a3.png)

---

## ATXMEGA256A3B

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_a3b](atxmega_a3b.png)

---

## ATXMEGA256A3BU

![atxmega256a3bu](atxmega256a3bu.png)

---

## ATXMEGA256D3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_d3](atxmega_d3.png)

---

## ATXMEGA32A4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega16a_32_64_128](atxmega16a_32_64_128.png)

---

## ATXMEGA32A4U

![atxmega16a4u_32a4u_64a4u_128a4u](atxmega16a4u_32a4u_64a4u_128a4u.png)

---

## ATXMEGA32D4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega_d4](atxmega_d4.png)

---

## ATXMEGA32E5

\- The XMEGA E series requires that you reset the interrupt yourself. For example : TCC4_INTflags.0=1 'clear OV flag 

\- The ERASE_APP NVM command (&H20) erases the complete flash, thus the boot space included. Use &H25 instead to erase and write a page.

\- There is a fixed map for the virtual ports : 

VPORT0 - Virtual port A

VPORT1 - Virtual port C

VPORT2 - Virtual port D

VPORT3 - Virtual port R

\- CONFIG XPIN slewrate is for the whole port, not for an individual pin

![atxmega8E5_16E5_32E5](atxmega8e5_16e5_32e5.png)

---

## ATXMEGA384C3

![ATXMEGA384C3](atxmega384c3.png)

---

## ATXMEGA64A1

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega128](atxmega128.png)

Here a note about the spike detector :

>The calibration byte in the production signature row show 0xFF and 0x00  
>for the ADC Calibration byte. Are these really the calibration values ?  
>And I'm not able to set the HIGH Byte of the calibration register.  
>Errata of Rev H don't show something from calibration bytes.

Reply from Atmel :

The voltage spike detector has been removed from the latest revision of the XMEGA A manual.  
This is because we have, unfortunately, not been able to validate the spike detector fully.  
The module is disabled in currently available parts to avoid unforeseen problems for any customers.

---

## ATXMEGA64A3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_A3](atxmega_a3.png)

---

## ATXMEGA64D3

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega_d3](atxmega_d3.png)

---

## ATXMEGA64D4

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about Xmega.

![atxmega_d4](atxmega_d4.png)

---

## ATXMEGA8E5

\- The XMEGA E series requires that you reset the interrupt yourself. For example : TCC4_INTflags.0=1 'clear OV flag 

\- The ERASE_APP NVM command (&H20) erases the complete flash, thus the boot space included. Use &H25 instead to erase and write a page.

\- There is a fixed map for the virtual ports : 

VPORT0 - Virtual port A

VPORT1 - Virtual port C

VPORT2 - Virtual port D

VPORT3 - Virtual port R

\- CONFIG XPIN slewrate is for the whole port, not for an individual pin

![atxmega8E5_16E5_32E5](atxmega8e5_16e5_32e5.png)

---

## AVR128DB28

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md) , [MEGAX](megax.md) and [AVRX](avrx.md)

The AVRDB128DB28 comes in 28 DIP/SOIC/SSOP. It has 128KB of flash and 28 pins. 

![avrx128db28](avrx128db28.png)

---

## AVR128DB64

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

Read the generic info about [Xtiny](xtiny.md) , [MEGAX](megax.md) and [AVRX](avrx.md)

The AVRDB128DB64 comes in 64 TQFP and VQFN. It has 128KB of flash and 64 pins. 

![AVR64DB64](avr64db64.png)

---

## AVRX

This chapter describes the AVRDBxx processors. To make a distinction between all the different AVR cores , MCS names the DB series the AVRX. This will include all the AVRxxDByy processors and AVRxxDAyy processors.

The difference between the DB and DA series seems to be that DA is missing the MVIO option.

The AVRX processors can be seen as new Xmega processors. They are the big brother of the ATMEGAX (MEGA4809). 

The advantage is that they are cheaper and also run on a voltage between 1v8 and 5V.

The AVRX also has the UPDI interface. It is 24 bit wide since the flash code exceeds the 64KB.

One change compared with other processors is that each pin version has its own ID. This means that the AVR128DB28 (28 pins) and the AVR128DB64 (64 pins) have different ID's.

Since there is one data sheet you need to take good care that the hardware exist in the chip you select. For example, the AVR128DB64 has 6 UARTS. But the AVR128DB28 has 3 UARTS.

From the PDF

The AVR128DB28/32/48/64 microcontrollers of the AVRÂ® DB family of microcontrollers are using the AVRÂ® CPU with

hardware multiplier running at clock speeds up to 24 MHz. They come with 128 KB of Flash, 16 KB of SRAM, and

512 bytes of EEPROM. The microcontrollers are available in 28-, 32-, 48- and 64- pin packages. The AVRÂ® DB

family uses the latest technologies from Microchip with a flexible and low-power architecture, including Event System,

accurate analog subsystems, and advanced digital peripherals.

![avr128dbX](avr128dbx.png)

XTINY/MEGAX

Please read the topics about [XTINY](xtiny.md) and [MEGAX](megax.md). Unless noted the information applies to AVRX as well.

MVIO

We at MCS think that the DB series is great. It is cheap, available in PDIP and has many features.

The DB series has MVIO (Multi Voltage I/O). For the DB series this means that pins or PORTC have a different voltage domain.

You can power the processor from 5V and the MVIO you can power at 3V3. This is great for mixed voltage designs.

Of course you can also connect both domains to the same voltage source.

DAC

There is one DAC with 10 bit resolution.

It can be enabled with the CONFIG statement : config DAC0=ENABLED|DISABLED, OUT_ENABLE=ENABLED|DISABLED, RUNMODE=ENABLED|DISABLED

The DAC has an output pin which can be enabled. 

ADC

There is a 12 bit A/D converter. The input pins depend on the processor model.

The A/D converter has differential channels. Notice that not all input pins can be used for differential input.

ZCD

Also new is the Zero Cross Detector. Up to 3 detectors are available depending on the model.

[Config Zcd0](config_zcdx.md) = Enabled|DISABLED , Runmode = Disabled|ENABLED, INVERT=ENABLED|DISABLED, OUT_ENABLE=ENABLED|DISABLED

We recommend to use an opto coupler with the detector when you interface this with other electronics/voltages.

The interrupt for the ZCD is special. In normal AVR there is a register to enable an interrupt, and some other register might be available to handle specific properties. 

In the AVRX this is all done in the interrupt register. There is only one vector. 

The ENABLE/DISABLE statements have been extended with the options :

```vb
ENABLE ZCD0_BOTH

ENABLE ZCD0_FALLING

ENABLE ZCD0_RISING

```
And the same for DISABLE.

When you enable the ZCD the proper setting will be written to the interrupt register.

When you disable the ZCD, no matter which setting you use, it will disable the interrupt. 

So DISABLE ZCD0_RISING and DISABLE ZCD0_BOTH will have the same effect.

2087

In version 2087 we redesigned the interrupt handling. Interrupts that have multiple settings but only one address get a general name. For ZCD0 this becomes ZCD0_INT

The ENABLE/DISABLE is extended with a section in the DAT file named [ENADISABLE]

When you press ENABLE and CTRL+SPACE you get a list of interrupts you can enable/disable. For ZCD this will be ZDC0_NONE, ZCD0_RISING, ZDC0_FALLING and ZDC0_BOTH.

Only one of the modes can be active at the same time. 

Multiple modes also apply to PIN interrupts. Each port can have 1 interrupt for example PORTD_INT. But each port pin can be enabled/disabled individually to generate an interrupt. 

OPAMP

Also new is the OPAMP. There are up to 3 OPAMP's which can also be connected to each other. The [CONFIG OPAMP](config_opamp.md) has many options. 

TIMERS

There are many timers. All with a different purpose. There are timers of type A(16 bit), B(16 bit) and D(12 bit).

VREGPWR

The Sleep controller also has a voltage regulator control register. [CONFIG VREGPWR](config_vregpwr.md) configures the power options.

All the remaining options are similar to the XTINY and MEGAX series. 

The supported AVRX series are : DA, DB, DD and EA.

See also

[MEGAX](megax.md), [XTINY](xtiny.md)

---

## FM24C64_256-XMEGA

FM24C64_256-XMEGA is the XMEGA version of the [FM24C64_256](fm24c64_256.md) library.

This library is a library that uses a RAMTRON I2C serial EEPROM.

Ramtron memory chips are as quick as RAM and can be overwritten almost unlimited times. 

An external EEPROM is a safe alternative to the internal EEPROM.

By using : $lib "FM24C64_256-XMEGA.lib" 

The EEPROM read and write routines from the library will be used instead of the internal EEPROM.

Thus you can still use : Dim BE as ERAM Byte

And you can use READEEPROM and WRITEEEPROM, but instead of using the internal EEPROM, the external I2C EEPROM is used.

Since Xmega has up to 4 different TWI channels, you need to define which channel is used.

You need to do so by defining a constant in your code named cFRAM_CHANNEL and give it a value of 1 for TWIC, 2 for TWID, 4 for TWIE or 8 for TWIF.

![notice](notice.jpg)This library is only included in the full version. It is not included with the DEMO.

In version 2086 you can also read write strings. 

Example

  
'(  
  
The fm24c64_256-XMEGA library is a library that uses a RAMTRON I2C serial EEPROM.  
Ramtron memory chips are as quick as RAM and can be overwritten almost unlimited times.  
  
An external EEPROM is a safe alternative to the internal EEPROM.  
  
By using : $lib "fm24c64_256-xmega.lib"  
The EEPROM read and write routines from the library will be used instead of the internal EEPROM.  
Thus you can still use : Dim BE as ERAM Byte  
And you can use READEEPROM and WRITEEEPROM, but instead of using the internal EEPROM, the external I2C EEPROM is used.  
The lib is for the FM24C515. It uses I2C / TWI.  
  
You must define a constant in your code with a constant that defines the twi interface :  
CONST cfram_channel = 1 'twic  
CONST cfram_channel = 2 'twid  
CONST cfram_channel = 4 'twie  
CONST cfram_channel = 8 'twif  
  
This library is only included in the full version. It is not included with the DEMO.  
This library is especial for XMEGA and serves as a sample. reading/writing strings is NOT supported but can be added by the user  
  
  
```vb
')  
'-----------------------------------------------------------------------------------------  
'name : 24C512-xmega-simple-RW test-TWIE.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : Testing Read/Write operation with external EEPROM on TWIE  
'micro : xmega128A1  
'suited for demo : no  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "xM128a1def.dat"  
$crystal = 32000000 ' 32MHz  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
Config BASE = 0 ' arrays start at 0  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
'for debug we send some data to the UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Config Twie = 100000 ' CONFIG TWI will ENABLE the TWI master interface  
```
const cfram_channel = 4 ' this constant is required by the fm24c64_256-xmega lib  
' set it to 1 for TWIC , 2 for TWID , 4 for TWIE and 8 for TWIF  
Open "twie" For Binary As #4 ' when not using default twic, you must use a channel  
  
const _twi_stop_1 = 1 ' just test i2cstop option, see help  
  
Dim Twi_start As Byte ' always required for xmega i2c  
I2Cinit #4  
  
```vb
$eepromsize = &H400 ' set it to the size of your EEPROM  
$lib "fm24c64_256-xmega.lib" ' include lib  
  
  
dim ee(100) as eram byte ' dim an EEPROM array  
Dim B , adres As byte  
  
print "Writing EEEPROM"  
for adres = 0 to 10  
print adres ; ",";  
```
ee(adres) = adres  
```vb
waitms 20 ' ONLY FOR NORMAL EEPROM , REMOVE FOR RAMTRON  
next  
print  
  
print "read EEEPROM"  
  
for adres = 0 to 10  
```
b = ee(adres)  
```vb
print adres;"-";b  
next  
  
end

```

---

## MEGAX

At MCS we refer to the new range of MEGA processors as the MEGAX. This because they look like Xmega processors but smaller.

Since the name XMEGA was taken by the actual XMEGA, and we use XTINY for the attinyX processors, we use MEGAX.

So why this distinction? And not use the atmel/microchip name? The answer is simple. 

By using different names for the DAT file we want to make it clear that some hardware is different. 

In fact these are all AVR chips but the core differs. As a user you do not need to care much. You can use the processors as usual.

The only important change is the programmer interface which is UPDI. Which is supported by BASCOM.

XMEGA and XTINY users will find many similar options. We based XTINY support on XMEGA. And MEGAX support on XTINY.

If you are unfamiliar with XTINY/MEGAX you best read the information about [XTINY](xtiny.md).

In fact we list all the differences under the XTINY topic. When not mentioned otherwise, the same applies for MEGAX.

The MEGAX is a bigger XTINY with more memory and hardware.

Some also come in DIP form.

We will only list the differences here with the XTINY.

![notice](notice.jpg)When you find info about the XTINY in the help, this info is also for the MEGAX unless there is a note about a difference. So when you read XTINY you can consider it equal to MEGAX.

Like the XTINY the MEGAX requires an add on. This is the same add on as the XTINY. So the XTINY Add On supports the MEGAX processors as well. 

Use the update function to update the add on. 

All tests have been performed using the MEGA4809-40 pins DIP. 

\- The biggest difference with XMEGA is that the MEGAX voltage range goes up to 5V. 

\- Biggest difference with XTINY is that there is more hardware like multiple USART's.

See also

[AVRX](avrx.md) , [XTINY](xtiny.md)

---

## XTINY

The names XTINY, MEGAX, AVRX and UPDI are used in this manual. We do mean the same thing ; the microchip processor with UPDI interface. Since the XTINY was the first platform implemented, you find that XTINY is used a lot.

But it will apply to MEGAX and AVRX as well which were implemented later unless specified otherwise.

At MCS we refer to the new range of TINY processors as the XTINY. This because they look like Xmega processors but smaller.

The XTINY processor is a great new processor. It uses the AVR instruction set. But it has a lot of the hardware found in the Xmega.

But do not make a mistake : these processors are different in many ways. They are the next generation of AVR processors. 

They use little power. 

When XMega was supported we had to make some decisions about this support. The goal is to keep the code BASCOM compatible. And for Xtiny we were faced with the same dilemmas. 

So again there will be new CONFIG statements and because the hardware is different, there will be other changes as well. 

You should read the data sheet of the processor like ATTINY816. We used the attiny 816/817 for testing. 

The processors are not available anymore in DIP. But you can use SOIC with a converter board. Like Xmega, this makes the processor less usable for hobbyists. At least for those that do not make their own PCB's.

Like the Xmega the internal registers can not be addressed by a pointer. So we had to change code using register pointers.

The DAT files contain a constant that identifies the platform. This constant is named _XTINY. For normal AVR and Xmega is is absent.

Platform Value

XTINY 1

MEGAX 2

AVRX DA, DB, DD 3

AVRX EA 4

Since the NVM controller differs among platforms, this constant is used in the xtiny.lib for writing the EEPROM.

UPDI

A big difference is that you once again need a new programmer since the programming interface is using UPDI.

The good news however is that you can use a simple serial port and a resistor to do the programming.

BASCOM-AVR supports the [UPDI](updi_programmer.md) protocol with a dedicated programmer. 

You will notice when you read the fuses that there are a lot of fuses and other settings. 

OSC

Like the Xmega, the Xtiny has extensive internal and external oscillator support. This means that you need to chose the system clock using the CONFIG SYSCLOCK statement.

This is essentially the only difference in code you need to make compared to the normal AVR.

The options and values differ from the Xmega. 

UART

In order to use the UART, you need to use CONFIG COMx. There is no default configuration when you use $baud. We would recommend to use CONFIG COM anyway. It can set all relevant settings. 

Also notice that the UART has separate registers for reading and writing. That is something new, not seen earlier. For this purpose we mapped registers UDRW and UDRR to the USART0_RXDATA / TXDATA registers.

ERAM

The EEPROM is more complex since it only works with pages. But the good news is that the EEPROM can be read like normal variables. 

PORTS

The ports have more options compared to normal AVR but less compared to Xmega. While Xmega can do a setting for an entire port, this feature is missing in Xtiny. The virtual port option is also different. In Xtiny there is just a register in the lower IO space mapped to the three most important port registers : DDR, PORT and PIN. These are named VPORTA_DIR, _OUT and _IN. 

In the first XTINY support we added DDR0, PORT0, PIN0 to make them compatible with Xmega. We also added VDDRA, VPORTA, and VPINA. All these registers are located in lower IO memory. In 2084 we removed these aliases. 

IMPORTANT CHANGE in 2084

It turned out that using the same scheme as for the Xmega was not optimal. So for 2084 we changed some ALIAS. 

We suggest you read the following information.

In the normal AVR there are PIN, PORT and DDR registers. They always have a low IO address so the instructions like CBI/SBI can be used.

This means that only 1 asm instruction is required to set/reset a bit of a port related register.

For example for the 2313def.dat we have PORTD:

PORTD =$12

DDRD =$11

PIND =$10

Since low IO space is limited and AVR processors with more ports were made, these ports got an extended IO address. Which means that the address is higher.

It also means that instructions like CBI/SBI will not work since they only work on low memory addresses.

For example from the m128RFA1.DAT

PORTL= $10b 

DDRL= $10a 

PINL= $109 

To change a bit in such a register, the value must be loaded, altered and written back.

With Xmega the port related addresses got a high address. But also a virtual port was added. These are dynamic virtual ports. Which means that you can chose at run time to which port a virtual register is mapped to. These virtual port addresses are placed in the low IO address space. So CBI/SBI could be used.

For example for the xm128A4Udef.dat these are some virtual registers

VPORT0_DIR = 16

VPORT0_OUT = 17

VPORT0_IN = 18

These registers can be made to map to PORTA, PORTB, etc. And you can change this at run time. So there is no fixed relation between the virtual and the actual port. Writing to a virtual port will write to the actual register. Thus when VPORT0 is mapped to PORTA, both writing to PORTA and VPORT0 will do the same thing.

Since there is no fixed relation, an ALIAS to PORTA points to PORTA_OUT. This because there is no PORT/DDRA/PINA register. So as a user you can use the port as you always did.

```vb
For the XTINY there is again a virtual register but it has a fixed relation. 

For example for the attiny816 :

```
VPORTA_DIR=0 ; 0000

VPORTA_OUT=1 ; 0001

VPORTA_IN=2 ; 0002

The relation is fixed. Each port has a virtual register. 

So instead of pointing to PORTA_OUT for PORTA, we now point to the VPORTA_OUT register. 

This will give better code. 

But it also required compiler changes. The problem with the virtual address is that the order is different. It would have been great if the traditional order was used. 

Because the ports are similar to xmega ports we point to PORTx_DIR.

Lets have a look at VPORTA in the DAT file :

VPORTA_DIR=0 ; 0000

DDRA=0 ; 0000 alias

VPORTA_OUT=1 ; 0001

PORTA=1 ; 0001 alias

VPORTA_IN=2 ; 0002

PINA=2 ; 0002 alias

The alias we use are DDRA, PORTA and PINA.

Since all ports are aliased all port related code should work without problems.

Pull Up

The pin behavior can be further configured using [CONFIG XPIN](config_xpin.md). 

This is important since the pull up need to be configured. The pull up can no longer be activated by writing a 1 to the PORT register !

INTERRUPTS

The interrupt system is extended with an option to specify one high priority interrupt.

So this is a nice extension.

You should also notice that a lot of interrupts need to be cleared manually. For example using a PIN interrupt requires to reset the INTFLAG register by writing a 1. 

While normal AVR pin interrupts let you guess which pin caused the interrupt, the Xtiny has registers that tell which pin caused the interrupt.

WATCHDOG

The watchdog works different since it has no on/off control. A timeout value of 0 will turn off the WD timer.

Any other time will start the WD timer.

START WATCHDOG will use the last value found from CONFIG WATCHDOG. When not found or available an error will be thrown by the compiler

STOP WATCHDOG will write a value of 0 to turn of the WD.

DAT files

When you look in the DAT file you will notice that almost all registers have new names. Also compared to Xmega. Of course BASCOM will use the right register when you use BASCOM code. 

When using ASM you need to check the datasheet and the DAT file.

When you are familiar with Xmega the transition should be smooth.

ADC and DAC

The Xtiny chips are very complete. They also have AD converter and a DA converter on board. 

TWI/I2C

The TWI is almost identical to the TWI in Xmega. This also means that when using TWI you need to create a byte variable named TWI_START in your user code.

The reason for this is that the TWI hardware sends a START and the slave address at once. 

Traditionally this was separated by an I2CSTART and I2CWBYTE. 

The TWI_START variable holds the state of I2CSTART. And when you write the address, it will use the proper instruction to send start and slave address. 

When you want to use soft I2C, you need to use the $FORCESOFTI2C directive. 

Do NOT include the "i2c_twi.lbx" library since this library is only for old AVR processors.

1WIRE

Since the ports have a different mapping, the 1wire code needed to be rewritten as well. The code is placed in the xtiny.lib

LIB

All Xtiny specific code you can find in Xtiny.lib

It contains overloaded versions of the code found in mcs.lib

Xtiny specific code in mcs.lib or other libs can be found by looking for the _XTINY constant.

This constant is set when you use a processor from the Xtiny range.

For normal Xtiny the value is set to 1. For megaX (like M4809) it is set to 2. 

BOOT

The XTINY has a different memory model. The BOOT area is located at the start of memory. After this memory the normal memory is located. With a FUSE you can set how many pages of the BOOT area you would like to use for boot code. A value of 1 will reserve a space of 256 bytes(this depends on the page size). When your loader binary code is 1024 bytes you would set it to : 1024/256 = 4

After the normal application code there is also the optional application data. This area can also be set with a fuse.

When using a boot loader you need to take care of the fact that your normal application code must start after the boot code. This can be done by using $ROMSTART in your code.

TCAx

Timer TCA has 1 or more wave outputs. As a user you need to set the pin to the output mode. 

XTINY/MEGAX/AVRX

The newest processors can configure each pin of a port. This is done using the CONFIG XPIN statement.

The sense parameter controls how the pin is used :

INT_DISABLED : no interrupt will occur but input buffer is enabled

BOTH : on a rising or falling edge an interrupt will occur

RISING : a rising edge will trigger an interrupt

FALLING : a falling edge will trigger an interrupt

INP_DISABLED : input and digital input buffer are disabled

LOW_LEVEL : interrupt will occur on a low level

So instead of using ENABLE you need to use CONFIG XPIN and select the proper trigger mode.

Instead of DISABLE you need to use CONFIG XPIN and select INT_DISABLED for the sense mode.

Add on

The addition of Xmega to BASCOM was a lot of work. This because only the instruction set was the same. We worked long on UPDI processor support and still this is a work in progress. So expects some updates specific for Xtiny/UPDI.

The Xtiny addition is not free of charge. It requires a commercial add on. It is available from the MCS shop.

The Xtiny add on will support all Xtiny processors. And by that we mean processors from the mega range like mega4808, DA/DB/DD range like avr128da28 etc.

See also

[MEGAX](megax.md), [AVRX](avrx.md)

---
