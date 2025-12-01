# SPI1INIT, SPI1IN, SPI1OUT, SPI1MOVE

Some of the new MEGA processors like ATMEGA328PB have a second SPI bus. This is not a USART that can work in SPI mode but a full SPI bus.

In order to use the second SPI which is named SPI1, you have to add a '1' to the SPI commands :

[CONFIG SPI1 ](config_spi.md)

[SPI1INIT](spiinit.md)

[SPI1IN](spiin.md)

[SPI1OUT](spiout.md)

[SPI1MOVE](spimove.md)

The statements above link to the description of the SPI statements (SPI0). 

  
```vb
'in this demo we only use the second SPI interface  
Config Spi1 = Hard , Interrupt = Off , Data_order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 128  
  
'second SPI  
```
Spi1init  
B = 5  
Spi1out A(1) , B  
Spi1in A(1) , B  
A(1) = Spi1move(a(2))  
  
  
Some XTINY processors also have a second SPI bus. They also support the BASCOM SPI commands.