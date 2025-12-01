# CONFIG SPIx XTINY

Action

Configures the SPI mode of the Xtiny.

Syntax

CONFIG SPIx = HARD, MASTER = YES|NO , MODE=0-3, CLOCKDIV=div, DATA_ORDER = LSB|MSB , EXTENDED=0|1 , SPIPIN=pins

Remarks

SPIx | There is 1 SPI interfaces on the Xtiny. You need to specify SPI0. The DB series has 2 SPI interfaces. You can use the second interface with SPI1. The only supported option is HARD for hardware mode.  
---|---  
MASTER | Selects if the SPI is running in master or slave mode. Possible values : YES(1), NO(0).  
MODE | The mode of the SPI interface. There are 4 modes in the range from 0-3. The mode decides weather the first edge in a clock cycles is rising or falling, and if data setup and sample is on leading or trailing edge. | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 | Rising, Sample | Falling, Setup  
1 | Rising, Setup | Falling, Sample  
2 | Falling, Sample | Rising, Setup  
3 | Falling, Setup | Rising, Sample  
  
CLOCKDIV | The SPI is clocked by the system clock which is divided by a the SPI divider. If you select a division factor of 4, and the system clock is 4 MHz, then the SPI clock will be 1 MHz. The possible values are : CLK2, CLK4, CLK8, CLK16, CLK32, CLK64 and CLK128. Some modes use the internal CLK2X bit. In SLAVE mode, the maximum clock rate is CLK4.  
DATA_ORDER | Selects if MSB or LSB is transferred first. The SPI can send the Least Significant bit (LSB) or the Most Significant Bit(MSB) first.   
SS | Slave select option. The possible values are : \- NONE, the SS will not be set or used \- AUTO, the dedicated pin is used, the pin depends on the used processor.  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes. When defined for one SPI interface like SPI0, it will also work for all other SPI interfaces like SPI1, SPI2 and SPI3.  
SPIPIN | This option allows to select the alternative pin locations. The default option is always the first listed. When you use the default option there is no need to specify it with SPIPIN. The MOSI, CLOCK and SS pin will be set to output mode. The SS pin will only be set to output mode when you use the SS=AUTO option. Otherwise you need to set the pin you use yourself to output mode. When you select the NONE option which means that the SPI is not connected to any of the port pins, no pins will be initialized to output. The mx4809 for example has these options : DEF_PA4567,ALT1_PC0123,ALT2_PE0123,NONE The first listed is DEF_PA4567 which means that this is the default location when you do not use the PORTMUX. PA means port A. And the pins are listed in MOSI,MISO,CLOCK,SS order. Thus PORTA.4 is connected to MOSI, PA.5 to MISO, etc. When you select ALT1_PC0123 it means that you select the alternative pin location 1. This will use PORTC0-3.  And the NONE option means that none of the SPI pins are connected.  The compiler will set the proper port direction and levels. It will also configure the PORTMUX in case the SPIPIN option is used. So when you use the default location, do not use SPIPIN in order to get less code.  
  
The SPI settings for the Xtiny differs only for the hardware name : SPI0 instead of SPI.

SPIINIT is not required for Xtiny. The pins are initialized as part of the CONFIG statement.

SPIINIT is ignored for Xtiny.

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

See Also

[SPIOUT](spiout.md), [SPIIN](spiin.md), [SPIMOVE](spimove.md) , SPI1OUT, SPI1IN, SPI1MOVE 

Example

```vb
'--------------------------------------------------------------------------------  
'name : spi.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates SPI  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'configure the SPI to master mode  
Config Spi0 = Hard , Clockdiv = Clk32 , Data_order = Msb , Mode = 0 , Master = Yes , Ss = Auto  
  
  
'dimension a variable  
Dim B As Word  
```
B = &B1010_1010  
  
Print "Test SPI"  
Spiinit 'initialize SPI is not required for Xtiny  
  
  
Do  
Spiout B , 1 'send some data  
```vb
Waitms 1000  
Loop  
  
End

```