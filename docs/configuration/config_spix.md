# CONFIG SPIx XMEGA

Action

Configures the SPI mode of the Xmega.

Syntax

CONFIG SPIx = HARD, MASTER = YES|NO , MODE=0-3, CLOCKDIV=div, DATA_ORDER = LSB|MSB , EXTENDED=0|1

Remarks

SPIx | There are 4 SPI interfaces on the Xmega. You need to specify SPIC, SPID, SPIE or SPIF for SPIx. The value must be HARD.  
---|---  
MASTER | Selects if the SPI is running in master or slave mode. Possible values : YES(1), NO(0).  
MODE | The mode of the SPI interface. There are 4 modes in the range from 0-3. The mode decides weather the first edge in a clock cycles is rising or falling, and if data setup and sample is on leading or trailing edge. | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 CPOL=0, CPHA=0 | Rising, Sample | Falling, Setup  
1 CPOL=0, CPHA=1 | Rising, Setup | Falling, Sample  
2 CPOL=1, CPHA=0 | Falling, Sample | Rising, Setup  
3 CPOL=1, CPHA=1 | Falling, Setup | Rising, Sample  
  
CLOCKDIV | The SPI is clocked by the system clock which is divided by a the SPI divider. If you select a division factor of 4, and the system clock is 4 MHz, then the SPI clock will be 1 MHz. The possible values are : CLK2, CLK4, CLK8, CLK16, CLK32, CLK64 and CLK128. Some modes use the internal CLK2X bit. In SLAVE mode, the maximum clock rate is CLK4.  
DATA ORDER | Selects if MSB or LSB is transferred first. The SPI can send the Least Significant bit (LSB) or the Most Significant Bit(MSB) first.   
SS | Slave select option. The possible values are : \- NONE, the SS will not be set or used \- AUTO, the dedicated pin is used, this is portC.4 for SPIC, portD.4 for SPID, portE.4 for SPIE and portF.4 for SPIF.  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes. When defined for one SPI interface like SPIC, it will also work for all other SPI interfaces like SPID, SPIE and SPIF.  
  
The SPI settings for the Xmega differ from the SPI settings for normal AVR chips.

In order to be able to use the four different SPI interfaces the Xmega uses a channel which you need to OPEN.

After you have opened the device, you can send/receive data using PRINT and INPUT.

There are 2 manuals available from ATMEL for every ATXMEGA Chip

1.| One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual  
---|---  
  
2.| Another Manual for the single chips like for example for an ATXMEGA128A1 it is the ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the Alternate Pin Functions. So you can find which Pin MISO, MOSI etc.  
---|---  
  
The SS pin, MOSI and CLOCK pins are set to output mode automatic in master mode.

The SS pin is also made high. The SS pin is only configured when you have selected SS=AUTO.

![notice](notice.jpg)If you need to use a different pin for SS or when you need to switch the logic level yourself for SS, and thus you use the SS=NONE option, you must setup the SS pin, even if you do not use it yourself. You must prevent that the SS pin will be made low in input mode since that will set the SPI into SLAVE mode, even while it was in MASTER mode. 

When SS is in auto mode, the SS pin will be made low before each SPI transfer and be made high when the SPI transfer is finished. SS can be used when multiple slaves are used, or to synchronize data packets.

![notice](notice.jpg)The pins are configured before the SPI control register is set. If you do not use the AUTO mode, you must set the pin direction and state yourself before using the CONFIG SPI. The following table shows which pins you have to set when NOT using the AUTO mode.

Pin | Master Mode | Slave Mode  
---|---|---  
MOSI | User set | Input  
MISO | Input | User set  
SCK | User set | Input  
SS | User set | Input  
  
It is very important that you set the pin direction and level BEFORE you use the CONFIG SPI statement. This because the CONFIG SPI will enable the SPI interface and once enabled you can not change data direction/level.

If you want to change pin levels , you must disable the SPI interface first by clearing bit 6 :

Spid_ctrl.6 = 0 ' disable

```vb
Config Portd.4 = Output ' set direction

Set Portd.0.4 ' set level

```
Spid_ctrl.6 = 1 ' enable 

See also

[INPUT](input.md), [PRINT](print.md), [OPEN](open.md)

[SPIIN](spiin.md) , [SPIOUT](spiout.md) , [SPIINIT](spiinit.md) , [SPI](using_the_spi_protocol.md) , [SPIMOVE](spimove.md)

Example

Dim Bspivar As Byte , Ar(4) As Byte , W As Word

Bspivar = 1

```vb
Config Spic = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk2 , Data_order = Msb

Config Spid = Hard , Master = Yes , Mode = 1 , Clockdiv = Clk8 , Data_order = Lsb

Config Spie = Hard , Master = Yes , Mode = 2 , Clockdiv = Clk4 , Data_order = Msb

Config Spif = Hard , Master = Yes , Mode = 3 , Clockdiv = Clk32 , Data_order = Msb

```
Open "SPIC" For Binary As #10

Open "SPID" For Binary As #11

Open "SPIE" For Binary As #12

Open "SPIF" For Binary As #13

Open "SPI" For Binary As #bspivar ' use a dynamic channel

```vb
'SPI channel only suppor PRINT and INPUT

Print #10 , "to spi" ; W

Input #10 , Ar(1) , W

Print #bspivar , W

Input #bspivar , W

```