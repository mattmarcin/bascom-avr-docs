# SPIOUT

Action

Sends a value of a variable to the SPI-bus.

Syntax

SPIOUT var , bytes

Syntax SPI1

SPI1OUT var , bytes

Remarks

var | The variable whose content must be send to the SPI-bus.  
---|---  
bytes | The number of bytes to send. Maximum value is 255.  
  
When SPI is used in HW(hardware) mode, there might be a small delay/pause after each byte that is sent. This is caused by the SPI hardware and the speed of the bus. After a byte is transmitted, SPSR bit 7 is checked. This bit 7 indicates that the SPI is ready for sending a new byte.

SPIOUT will always work on the first SPI interface (SPI0).

SPI1OUT will work on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIINIT](spiinit.md) , [CONFIG SPI](config_spi.md) , [SPIMOVE](spimove.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

```vb
Dim A(10) As Byte

Config Spi = Soft , Din =Pinb.0 , Dout =Portb.1 , Ss =Portb.2 , Clock =Portb.3

```
Spiinit

Spiout A(1), 4 'write 4 bytes a(1), a(2) , a(3) and a(4)

End