# SPIIN

Action  
  
Reads a value from the SPI-bus.

Syntax

SPIIN var, bytes

Syntax SPI1

SPI1IN var, bytes 

Remarks

Var | The variable which receives the value read from the SPI-bus.  
---|---  
Bytes | The number of bytes to read. The maximum is 255.  
  
In order to be able to read data from the SPI slave, the master need to send some data first. The master will send the value 0.

SPI is a 16 bit shift register. Thus writing 1 byte will cause 1 byte to be clocked out of the device which the SPIIN will read.

SPIIN always work on the first SPI interface (SPI0)

SPI1IN works on the second SPI interface (SPI1)

See also

[SPIOUT](spiout.md), [SPIINIT](spiinit.md), [CONFIG SPI](config_spi.md) , [SPIMOVE](spimove.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : spi.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo :SPI

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

Dim A(10) As Byte

```
Spiinit

B = 5

Spiout A(1) , B

Spiin A(1) , B

A(1) = Spimove(a(2))

End