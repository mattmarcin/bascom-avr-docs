# Adding XRAM with External Memory Interface

With ATMEGA AVR like ATMEGA128, ATMEGA1280 or older types like 90S8515 you can access external RAM (SRAM) or other peripherals through its External Memory Interface. Search in the Atmel ATMEGA datasheets for "External Memory Interface"

```vb
For ATXMEGA devices see App Note: [AVR1312: Using the XMEGA External Bus Interface](<http://www.atmel.com/Images/doc8058.pdf>) for details.

For example for an ATMEGA1280 the external memory interface consist of PORTA (multiplexed data and address low byte), PORTC (address high byte), and PORTG[2:0] (RD, WR and ALE).

```
ATMEGA1280 pin connections to SRAM device:

Port A = Multiplexed Address low byte (A0....A7) / Data (D0....D7) <\--------> Direct connection to SRAM (D0...D7) and connected to Input D of octal latch (typically â74 x 573â or equivalent) to (A0.....A7) of SRAM chip

Port C = Address high byte (A8....A15) <\--------> direct connection to for example SRM (A8....A15)

Port G Pin 0 = WR (Write strobe to external memory) <\--------> direct connection to for example SRAM WR

Port G Pin 1 = RD (Read strobe to external memory) <\--------> direct connection to for example SRAM RD

Port G Pin 2 = ALE (Address Latch Enable to external memory) <\--------> Connected to G Input of octal latch (typically â74 x 573â like 74 x 573)

Example for 74HTC573 (TTL variant):

<http://www.nxp.com/documents/data_sheet/74HC_HCT573.pdf>

Address latch with octal latch:

The data bus and the low byte of the address bus is multiplexed on Port A. The ALE signal indicates when the address is present. This low byte must be stored by a latch until the memory access cycle is completed.

Schematics for connecting the ATMEGA with octal latch and sram can be found in:

•| Atmel AVR Studio Help File (AVR tools user guide) search for: "external memory interface" and scroll down to APPENDIX. There you also find a list of 3.3 or 5V compatible SRAM's that can be used with ATMEGA's and there is a link to STK503.pdf which is part of the help file.  
---|---  
  
•| The list of compatible SRAM devices can be also found here: <http://www.atmel.com/images/stk503_ug.pdf> (page 16)  
---|---  
  
•| The datasheet of for example ATMEGA1280 also include a picture which show the connections between AVR, Octal Latch external SRAM device.  
---|---  
  
The data memory map for example for ATmega640/1280/1281/2560/2561:

Hex-Address:

&H00 .... &H1F 32 Registers

&H20 .... &H5F 64 I/O Registers

&H60 .... &H1FF 416 external I/O Registers

&H200 .... &H21FF Internal SRAM (8K in this case)

&H2200 .... &HFFFF External SRAM (XRAM)

XRAM will use an area in the remaining address locations in the 64K address space (&HFFFF). This starts at the address following the internal SRAM. 

Internal SRAM use the lowest 4,608/8,704 bytes, so when using 64KB (65,536 bytes) of XRAM, 60,478/56,832 Bytes of XRAM are available.

See datasheet of ATMEGA device for a way to use the complete 64KByte.

XRAM will be enabled by [CONFIG XRAM](configxram.md) (config XRAM is setting SRE bit of the atmega 1280 XMCRA Register)

The Pins of Port A, Port C and Port G from ATMEGA1280 are automatically enabled for XRAM and can not be used for other tasks by default if XRAM is enabled. The external memory address space can be divided in two sectors (upper and lower sector) with different wait-state bits. You can also release some Port C pins for other tasks (in the XMCRB Register) . See atmega 1280 datasheet for details.

See also: [$XRAMSIZE](xramsize.md) and [$XRAMSTART](xramstart.md)

You can clear the XRAM for example with:

For N = Ramstart To Ramend 'replace RamStart and RamEnd with the real values  
Out N , 0 'zero or any value you like  
Next

With XRAM, you should dim all your global variables with XRAM. Example: Dim Var As Xram Byte

This will leave the internal memory for the stacks and local created variables.

You can also use $default Xram when you do not want to add the XRAM to each DIM. 

Example 1:

A real Example for using SRAM and another Bus-mode device is WIZ200WEB from Wiznet.

Here an ATMEGA128L, an external 32K SRAM and a W5300 Ethernet Chip is used. See also [CONFIG TCPIP](config_tcpip.md)

The data memory map for ATMEGA128:

Hex-Address:

&H00 .... &H1F 32 Registers

&H20 .... &H5F 64 I/O Registers

&H60 .... &HFF 160 external I/O Registers

&H100 .... &H10FF Internal SRAM (4K in this case)

&H1100 Start of External SRAM (XRAM)

So the config is following (&H8000 = 32kByte):

```vb
$xramstart = &H1100  
$xramsize = &H8000  
Config Xram = Enabled

```
The W5300 Chip from Wiznet is setup to use Base Address &H8000.

So the data memory map for ATMEGA128 is:

Hex-Address:

&H00 .... &H1F 32 Registers

&H20 .... &H5F 64 I/O Registers

&H60 .... &HFF 160 external I/O Registers

&H100 .... &H10FF Internal SRAM (4K in this case)

&H1100 Start of External SRAM (XRAM)

&H8000 Base Address of W5300 Chip from WIZNET

&H8400 .... &HFFFF Not in use

See also [CONFIG TCPIP](config_tcpip.md) for further details on W5300 Chip from Wiznet.

Example 2:

We use now an WIZ830mj module (which uses a W5300 Chip from Wiznet) on a board with an 64/128KByte SRAM in combination with ATMEGA1280:

Hex-Address:

&H00 .... &H1F 32 Registers

&H20 .... &H5F 64 I/O Registers

&H60 .... &H1FF 416 external I/O Registers

&H200 .... &H21FF Internal SRAM (8K in this case)

&H2200 .... &HFBFF External SRAM (XRAM) upper and lower

&HFC00 Base Address of W5300 Chip over memory address selector

XRAM configuration here is:

```vb
$xramstart = &H2200  
$xramsize = &HFBFF  
Config Xram = Enabled

```
Writing to the first XRAM address is done by:

Out &H2200 , &H01

Reading from first XRAM is done by:

Var = Inp(&H2200)

The datasheet of W5300 say: "In the case of using an 8bit data bus width, ADDR[9:0] is used " so we have Address 0.......Address 9 but the SRAM need Address 0.....15.

Here an example of additional circuit between ATMEGA and W5300 and SRAM to solve the difference of address (A0...A15) for SRAM and (A0...A9) for W5300:

![adding_xram_2](adding_xram_2.png)  


The Base Address for W5300 (WIZ830mj) in this case is &HFC00

Address Bit | A15 | A14 | A13 | A12 | A11 | A10 | A9 | A8 | A7 | A6 | A5 | A4 | A3 | A2 | A1 | A0  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Binary: | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  
Hex: | FC00 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
  
For older 90S8515 chips for example the maximum size of XRAM can be 64 Kbytes.

Example: The STK200 has a 62256 ram chip (32K x 8 bit).

Here is some info from the BASCOM user list :

If you do go with the external ram , be careful of the clock speed.

Using a 4 MHz crystal , will require a SRAM with 70 nS access time or less. Also the data latch (74HC573) will have to be from a faster

family such as a 74FHC573 if you go beyond 4 MHz.

You can also program an extra wait state, to use slower memory.

Here you will find a pdf file showing the STK200 schematics:

See Stk200_schematic.pdf for more information.

If you use a 32 KB SRAM, then connect the /CS signal to A15 which give to the range of &H0000 to &H7FFF, if you use a 64 KB SRAM, then

tie /CS to GND, so the RAM is selected all the time.

![xram](xram.jpg)