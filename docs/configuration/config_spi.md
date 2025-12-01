# CONFIG SPI

Action

Configures the SPI mode and pins.

Syntax for software SPI

CONFIG SPI|SPISOFT = SOFT, DIN = PIN, DOUT = PIN , SS = PIN|NONE, CLOCK = PIN , SPIIN=value , MODE=mode, SPEED=speed, SETUP=setup , EXTENDED=ext

Syntax for hardware SPI

CONFIG SPI|SPIHARD = HARD, INTERRUPT=ON|OFF, DATA_ORDER = LSB|MSB , MASTER = YES|NO , POLARITY = HIGH|LOW , PHASE = 0|1, CLOCKRATE = 4|16|64|128 , NOSS=1|0 , SPIIN=value , EXTENDED=ext

Syntax for hardware SPI1

CONFIG SPI1 = HARD, INTERRUPT=ON|OFF, DATA_ORDER = LSB|MSB , MASTER = YES|NO , POLARITY = HIGH|LOW , PHASE = 0|1, CLOCKRATE = 4|16|64|128 , NOSS=1|0 , SPIIN=value

When you just want to use one SPI slave chip using the HW SPI, use this : Config Spi = Hard , Interrupt = Off , Data_Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 128

When you want more details, read more about the details and options below.

Remarks software SPI

SPI | SOFT for software emulation of SPI, this allows you to choose the pins to use. Only works in master mode. HARD for the internal SPI hardware, that will use fixed pins of the microprocessor.  
---|---  
DIN | Data input or MISO. Pin is the pin number to use such as PINB.0  
DOUT | Data output or MOSI. Pin is the pin number to use such as PORTB.1  
SS | Slave Select. Pin is the pin number to use such as PORTB.2 Use NONE when you do not want the SS signal to be generated. See remarks. Or as an alternative you can use : NOSS=1.  
CLOCK | Clock. Pin is the pin number to use such as PORTB.3  
DATA ORDER | Selects if MSB or LSB is transferred first. For soft SPI you need to use the MODE option as well. Otherwise only MSB order is available.  
MASTER | Selects if the SPI is run in master or slave mode.  
SPIIN | When reading from the SPI slave, it should not matter what kind of data you send. But some chips require a value of 255 while others require a value of 0. By default, when the SPIIN option is not provided, a value of 0 will be sent to the SPI slave. With this SPIIN option you can override this value.   
MODE | A constant in the range from 0-3 which defines the SPI MODE. Without MODE, the default mode 1 will be used. Also, when using MODE, new SPI code will be used.  When using MODE, you can also specify SPEED and SETUP. MODE is for Software SPI only ! | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 | Rising, Sample | Falling, Setup  
1 | Rising, Setup | Falling, Sample  
2 | Falling, Sample | Rising, Setup  
3 | Falling, Setup | Rising, Sample  
  
SPEED | Is a numeric constant for an optional delay. This delay is in us. When you specify 1, it will result in 2 us delay : 1 us before and 1 us after the clock. By default there is no delay. Only slow slave chips might require a delay.  SPEED only applies when MODE is specified.  
SETUP | Setup is the delay in uS before sampling the MISO pin. A numeric constant must be used. SETUP is for Software SPI only and when MODE is used !  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes.  
  
Software SPI allows you to chose the processor pins for the SPI operation. Typically you need a MISO, MOSI, CLOCK and SS pin.

While this is an advantage, the disadvantage is that software SPI uses more processor resources.

In software spi mode the [SPIINIT](spiinit.md) statement will set the SPI pins to the proper logic level. For example to :

sbi PORTB,5 ;set latch bit hi (inactive)SS

sbi DDRB,5 ;make it an output SS

cbi PORTB,4 ;set clk line lo

sbi DDRB,4 ;make it an output

cbi PORTB,6 ;set data-out lo MOSI

sbi DDRB,6 ;make it an output MOSI

cbi DDRB,7 ;MISO input

Ret

This is just an example. The actual code differs from processor to processor. And also depends on the used port pins. 

In most cases, there is just one slave chip to control/address. In such a case you need only one slave select(SS) pin to control this chip. But SPI can also be used to control multiple SPI slaves.

These slaves need to use the same mode. You can not dynamically change the SPI mode at run time. 

BASCOM will automatically set the SS pin to logic level 0 when you use a SPI command. And when the SPI command has executed, it will set the SS pin back to a logic 1. 

When the slave chip has in inverted SS pin (it requires a 1 to be active) you can not use this automatic SS signal generation.

When you want to address multiple slaves with the software SPI you need multiple pins to select the different slave chips. In this case you also can not use the automatic SS signal generation.

The solution is to specify NONE for SS. This will eliminate the automatic SS signal generation. But it also means that you as a user need to handle this. In practice this means :

\- choose a port pin to serve as SS pin

\- set it to output and to the right logic level (1 in most cases to disable the slave)

\- before using a SPI statement, select the slave by making SS logic 0.

\- after the SPI statement, set the SS logic level back to 1.

Example user controlled SS pin.

Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = NONE , Clock = Portb.3  
MySS alias portb.2  
```vb
Config MySS=OUTPUT : MySS=1 ' deactivate  
Dim var As Byte  
```
SPIINIT ' Init SPI state and pins.  
MySS=0 ' select SS  
SPIOUT var , 1 ' send 1 byte  
MySS=1 ' deselect SS

Remarks Hardware SPI

SPI | SOFT for software emulation of SPI, this allows you to choose the pins to use. Only works in master mode. HARD for the internal SPI hardware, that will use fixed pins of the microprocessor.  
---|---  
DATA_ORDER | Selects if MSB or LSB is transferred first.  
MASTER | Selects if the SPI is run in master or slave mode.  
POLARITY | Select HIGH to make the CLOCK line high while the SPI is idle. LOW will make clock LOW while idle.  
PHASE | Refer to a data sheet to learn about the different settings in combination with polarity.  
CLOCKRATE | The clock rate selects the division of the of the oscillator frequency that serves as the SPI clock. So with 4 you will have a clock rate of 4.000000 / 4 = 1 MHz , when a 4 MHZ XTAL is used.  
NOSS | 1 or 0. Use 1 when you do not want the SS signal to be automatically generated in master mode.   
INTERRUPT | Specify ON or OFF. ON will enable the SPI interrupts to occur. While OFF disables SPI interrupts. ENABLE SPI and DISABLE SPI will accomplish the same.  
SPIIN | When reading from the SPI slave, it should not matter what kind of data you send. But some chips require a value of 255 while others require a value of 0. By default, when the SPIIN option is not provided, a value of 0 will be sent to the SPI slave. With this SPIIN option you can override this value.   
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes.  
  
Hardware SPI is the best option when it is available. Hardware SPI can be used in master and slave mode. All BASCOM SPI statements are master mode routines.

The only disadvantage is that you must use the dedicated hardware pins, the SS pin included!

When you use CONFIG SPI = HARD without any other parameter, the SPI will only be enabled. It will work in slave mode then with CPOL =0 and CPH=0.

In hardware spi mode the [SPIINIT](spiinit.md) statement will set the SPI pins to :

SCK = Ouput

MISO = Input

MOSI = Output 

In Master mode, the SS pin will be set to output too.

As explained for Software SPI, it is not always desirable to use the SS pin to control the SPI slave chip. Because you want to use a different pin, use multiple slave, or the slaves has an inverted SS signal.

Since the hardware SPI always has an SS pin, there is an override for this with a different name than for soft spi : NOSS=0|1

So where SS=NONE is used for SOFT SPI to disable automatic SPI signal generation, the HARDWARE SPI use the option NOSS=1 to do the same. NOSS means NO SS signal generation.

When NOSS is not used or NOSS=0, the default will be used where the dedicated SS pin will create the slave select signals.

One big difference with software SPI, is that in order to use the SPI in master mode, the SS pin must be set to output mode. Even if you do not use the dedicated SS pin to control a SPI slave chip !

When the SS pin is in input mode, a logic 0 at the input will turn the master mode into slave mode. A pull up resistor could do the same but our advise : use the SS pin as an output pin.

The SS pin is set to output mode when the MASTER mode is selected. So even if NOSS=1, the SS pin is set to output mode when MASTER=YES.

![notice](notice.jpg)When using NOSS=1 : In order to use the Hardware SPI in master mode, you need to set the SS pin to output. In input mode, this pin can be used to set the SPI bus into slave mode. You only need to set the pin to output when you use the NOSS=1 option. With NOSS=0, the compiler will set the SS pin to output and makes SS pin logic 1.

When NOSS=1 is used, the SS pin is only made an output pin in MASTER mode. No logic level is set when NOSS=1.

This table show how SS pin is set with the various options for HW mode.

MODE | NOSS | SS PIN  
---|---|---  
MASTER | 0 | output, logic 1  
  
| 1 | output, logic level unchanged  
SLAVE | 0 | input  
  
| 1 | input  
  
All SPI routines are SPI-master routines. In the samples directory you will also find a SPI hardware master and SPI hardware slave sample.

The SPI protocol is explained in the chapter : [Using the SPI protocol](using_the_spi_protocol.md)

![notice](notice.jpg)When using a processor for both the master and slave : Take in mind that the SPI master processor clock frequency must be 1/4 of the SPI slave processor frequency. 

Chips with 2 full SPI ports

Some new processors like the ATMEGA328PB have 2 SPI ports. In order to use this second SPI port you have to add a '1' to the statement. 

CONFIG SPI1

SPI1IN

SPI1OUT

SPI1INIT

SPI1MOVE

See also

[SPIIN](spiin.md) , [SPIOUT](spiout.md) , [SPIINIT](spiinit.md) , [SPI](using_the_spi_protocol.md) , [SPIMOVE](spimove.md)

Example for Software SPI

```vb
Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = Portb.2 , Clock = Portb.3  
Dim var As Byte  
```
SPIINIT 'Init SPI state and pins.  
SPIOUT var , 1 'send 1 byte

Example for Hardware SPI, 1 slave

Config Spi = Hard, Interrupt = Off, Data_Order = Msb, Master = Yes, Polarity = High, Phase = 1, Clockrate = 4, Noss = 0

Spiinit