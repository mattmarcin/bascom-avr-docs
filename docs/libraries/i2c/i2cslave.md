# CONFIG I2CSLAVE

The I2C Slave Add-on started with a software emulation for TWI slave using an interrupts and timer. It supported a number of early processors.

When TWI was added to some of the processors, an additional TWI slave lib was added to the package.

With Xmega having up to 4 TWI/I2C interfaces, TWI slave support for Xmega has been added to the package in version 2077 build 3

Most tiny processors do not support TWI but USI. USI support is added as well in 2077 build 3.

So the add on comes with a number of I2C slave libraries.

See [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md), [CONFIG TWISLAVE](config_twislave.md) , [CONFIG TWIXSLAVE](config_twixslave.md)