# I2C TWI Slave

The I2C-Slave library is intended to create I2C slave chips. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>)

The I2C Slave add on can turn some chips into a I2C slave device. You can start your own chip plant this way.

Most new AVR chips have a so called TWI/I2C interface. As a customer of the I2C slave lib, you can get both libs.

The i2cslave.lib works in interrupt mode and is the best way as it adds less overhead and also less system resources.

With this add-on library you get both libraries:

| i2cslave.lib and i2cslave.lbx : This library is used for AVRâs which have no hardware TWI/I2C interface like for example ATTINY2313 or ATTINY13. In this case TIMER0 and INT0 is used for SDA and SCL (Timer0 Pin = SCL, INT0 Pin = SDA). Only AVR' with TIMER0 and INT0 on the same port can use this library like for example ATTINY2313 or ATTINY13. The i2cslave.lbx is the compiled library version of i2cslave.lib. See also [Config I2CISLAVE](config_i2cslave.md)  
---|---  
  
| i2c_TWI-slave.LBX : This library can be used when an AVR have an TWI/I2C hardware interface like for example ATMEGA8, ATMEGA644P or ATMEGA128. In this case the hardware SDA and SCL pin's of the AVR will be used (with ATMEGA8: SCL is PORTC.5 and SDA is PORTC.4). This library will be used when USERACK = OFF. When USERACK =ON then i2c_TWI-slave-acknack.LBX will be used. See also [Config TWISLAVE](config_twislave.md)  
---|---  
  
See also: [Using the I2C protocol](using_the_i2c_protocol.md)