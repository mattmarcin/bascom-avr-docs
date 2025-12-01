# I2CV2

I2C Software

By default BASCOM will use software routines when you use I2C statements. This because when the first AVR chips were introduced, there was no TWI interface. Atmel named it TWI because Philips is the inventor of I2C. But TWI is the same as I2C.

When your processor has a TWI interface you can best use this TWI interface. 

By default the software master i2c routines use the library named i2c.lib. This library does not maintain a clock/data state so when i2cstart or i2cstop is generated, the clock and data lines need to be set to the proper state before the start/stop condition can be generated. This can result in small glitches. Most slave chips will not notice them but some do.

For this purpose the i2c master library has been rewritten so that clock and data have a known state/level at all times. This allows to create glitch free clock/data.

To use this library use the $LIB directive : $LIB "I2CV2.LIB"

This will make the compiler use this library. One thing to be aware of : a repeated start can only be created by using the [I2CREPSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) statement. 

This is a difference with the default i2c.lib

When you want to use soft I2C on an XTINY or XMEGA you need to use the [$FORCESOFTI2C](forcesofti2c.md) directive.

Example

```vb
$forcesofti2c ' force soft i2c

$lib "i2cv2.lib" ' use this one

```
See also: [Using the I2C protocol](using_the_i2c_protocol.md), [CONFIG TWI](config_twi.md) , [I2CV2](i2cv2.md)