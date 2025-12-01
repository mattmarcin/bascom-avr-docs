# I2C_TWI

I2C Software vs. Hardware Routines

By default BASCOM will use software routines when you use I2C statements. This because when the first AVR chips were introduced, there was no TWI yet. Atmel named it TWI because Philips is the inventor of I2C. But TWI is the same as I2C. This I2C/TWI peripheral performs all the tasks in hardware so less code is required. But it is limited to the designated pins for SCL and SDA.

So BASCOM allows you to use I2C on every AVR chip. Most newer AVR chips have build in hardware support for I2C. With the I2C_TWI lib you can use the TWI which has advantages as it require less code.

To force BASCOM to use the TWI, you need to insert the following statement into your code:

$LIB "I2C_TWI.LBX"

You also need to choose the correct SCL and SDA pins with the CONFIG SCL and CONFIG SDA statements.

The TWI will save code but the disadvantage is that you can only use the fixed SCL and SDA pins.

For XMEGA the default is using the hardware TWI. You can force bascom to use the software solution using [$FORCESOFTI2C](forcesofti2c.md)

![notice](notice.jpg)You should not reference the I2C_TWI in Xmega or Xtiny ! Xmega and Xtiny use a different TWI interface.

See also: [Using the I2C protocol](using_the_i2c_protocol.md), [CONFIG TWI](config_twi.md) , [I2CV2](i2cv2.md)