# LCD_RX1602A5

This LCD driver is based on O-Family AQM0802A Library.

It is suited for I2C displays RX1602A5. It was developed for, and sponsored by Lab microelectronic GmbH

All you need to do is connect the LCD to the I2C pins and configure LCD like : config lcd = 16x2 , chipset = st7032

A sample you find under [CONFIG LCD](config_lcd.md)

Of course you need a functional I2C or TWI bus. Both soft and HW TWI are supported.