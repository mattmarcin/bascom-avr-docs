# LCD_I2C_PCF8574

The LCD_I2C_PCF8574 library is made by O-Family. This library supports multiple LCD.

The library is based on an old library from Kent Andersson. The old lib used bascom code but for best performance should use ASM.

O-Family made this possible. He also extended the lib so multiple LCD can be used.

The LCD are normal text LCD. Unlike graphical LCD, TEXT LCD have a kind of standard. 

So most text LCD would be usable. The important part is that an I2C port extended chip is used : the PCF8574.

The PCF8574 also has a brother/sister : an identical chip with the A suffix. The only difference is that it has a different base address.

Normally an LCD is operated in 4 bit or 8 bit parallel pin mode. The PCF chip is connected to the LCD data and control lines. And the driver sends the proper I2C commands to control the LCD. This way you can use I2C which is great since it can be used of a greater distance. 

XMEGA

For use with XMEGA you need to define 2 constants in your code.

const TWI_ADR = interface

const TWI_CH = num

The interface must point to the TWI control register, this could be : TWIC_CTRL but aldo TWID_CTRL, TWIE_CTRL and TWIF_CTRL

The TWI_CH constant with the value num, must be 1 for TWIC, 2 for TWID, 4 for TWIE and 8 for TWIF

![text_lcd_o-family](text_lcd_o-family.png)

The circuit above show how to connect things. Converter boards exist that can be soldered right to the LCD.

But you can also wire this yourself.

The A0-A1-A2 select the address of the PCF chip.

More info in the [forum](<fourthline.htm> "https://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=viewtopic&p=80311#80311").

Two samples you can find in the SAMPLES\LCDTEXT folder

SAMPLE

```vb
$programmer = 22 'ARDUINO (using stk500v1 protocol)  
'  
' *************************************  
' * PCF8574 I2C LCD Adapter test *  
' * For multiple LCDs 2021/ 3/24 *  
' *************************************  
'  
$regfile = "m328pdef.dat" 'Set the AVR to use.  
$crystal = 16000000 'Set the AVR clock.  
'  
$hwstack = 64 'Set the capacity of the hardware stack.  
$swstack = 10 'Set the capacity of the software stack.  
$framesize = 24 'Set the capacity of the frame area.  
'  
' * PCF8574 I2C LCD Adapter settings *  
'  
```
Const I2c_select = 1 '0:Software I2C , 1:TWI  

```vb
#if I2c_select = 0  
'------[For software I2C]------  
Config I2cdelay = 10 'SCL clock frequency = approx. 42KHz. (At AVR clock 16MHz) (* Maximum 100KHz)  
Config Scl = Portd.2 'Set the port pin to connect the SCL line of the I2C bus.  
Config Sda = Portd.3 'Set the port pin to connect the SDA line of the I2C bus.  
```
I2cinit 'Initialize the SCL and SDA lines of the I2C bus.  
```vb
'-------------------------------  

#else  
'------[For TWI]------------------  
$lib "i2c_twi.lib" 'Incorporate the hardware I2C/TWI library.  
Config Twi = 100000 'I2C bus clock = 100KHz  
Config Scl = Portc.5 'You must specify the SCL pin name.  
Config Sda = Portc.4 'You must specify the SDA pin name.  
```
I2cinit 'Initialize the SCL and SDA lines of the I2C bus.  
```vb
'-------------------------------  

#endif  
Dim Pcf8574_lcd As Byte : Pcf8574_lcd = &H4E 'PCF8574 slave address. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Dim Backlight As Byte : Backlight = 1 'LCD backlight control. (0: off, 1: on)  
$lib "lcd_i2c_PCF8574.LIB" 'Incorporate the library of I2C LCD PCF8574 Adapter.  
Config Lcd = 20x4 'Set the LCD to 20 characters and 4 lines.  
```
Initlcd 'Initialize the LCD.  
```vb
'  
' * When installing the second and subsequent LCDs *  
'  
```
Pcf8574_lcd = &H4C 'The slave address of the second PCF8574. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Initlcd 'Initialize the second LCD.  
'  
Pcf8574_lcd = &H4A 'The slave address of the third PCF8574. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Initlcd 'Initialize the third LCD.  
  
```vb
'  
' ****************  
' * Display test *  
' ****************  
'  
```
Pcf8574_lcd = &H4E 'Specify the first LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 2  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 2 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 15 'Display custom characters.  
Lcd Chr(2) ; "1"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
```vb
'  
' * Second LCD *  
'  
```
Pcf8574_lcd = &H4C 'Specify the second LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 2  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 3 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 15 'Display custom characters.  
Lcd Chr(3) ; "2"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
```vb
'  
' * Third LCD *  
'  
```
Pcf8574_lcd = &H4A 'Specify the third LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 4  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 4 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 19 'Display custom characters.  
Lcd Chr(4) ; "3"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
'  
Locate 3 , 3  
Lcd "-- 3rd Line --"  
'  
Locate 4 , 4  
Lcd "20x4 Display "  
'  
Locate 4 , 20 'Display the cursor.  
Cursor On , Blink  
End