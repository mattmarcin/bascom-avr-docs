# ATXMEGA

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