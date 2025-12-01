# Options Compiler I2C, SPI, 1WIRE

![options_compiler_i2c](options_compiler_i2c.png)

Options Compiler I2C, SPI, 1WIRE

Item | Description  
---|---  
SCL port | Select the port pin that serves as the SCL-line for the I2C related statements.  
SDA port | Select the port pin that serves as the SDA-line for the I2C related statements.  
1WIRE | Select the port pin that serves as the 1WIRE-line for the 1Wire related statements.  
Clock | Select the port pin that serves as the clock-line for the SPI related statements.  
MOSI | Select the port pin that serves as the MOSI-line for the SPI related statements.  
MISO | Select the port pin that serves as the MISO-line for the SPI related statements.  
SS | Select the port pin that serves as the SS-line for the SPI related statements.  
Use hardware SPI | Select to use built-in hardware for SPI, otherwise software emulation of SPI will be used. The 2313 does not have internal HW SPI so it can only be used with software SPI mode. When you do use hardware SPI, the above settings are not used anymore since the SPI pins are dedicated pins and can not be chosen by the user.  
  
It is advised to use the various [CONFIG](config.md) commands in your source code. It make more clear in the source code which pins are used.