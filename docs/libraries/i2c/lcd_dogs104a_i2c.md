# LCD_DOGS104a_I2C

This is a user contributed lbx for the EADOGS104 with the SSD1803A.

The SAMPLES\LCDGRAPH folder contains the sample :

```vb
'--------------------------------------------------------------  
' DOGS-104.bas  
' Demonstration for DOGS 104-A display  
' (c) R. Müller-Westermann  
' HB9EFQ@yahoo.com  
'--------------------------------------------------------------  
  
$regfile = "m168def.dat"  
$crystal = 1000000  
'$sim  
  
$hwstack = 32  
$swstack = 32  
$framesize = 64  
  
$lib "Lcd_dogs104a_i2c.lbx"  
  
  
'LCD -----------------------------------------------------------------  
'chipset:DOGS104V3  
'DOGS104 Display can use either &H78 if pin SA0 of module is set to GND  
'or &H7A if SA0 of module is set to VDD for I²C communication.  
'Pullup resistors on SDA and SCL lines of less or equal to 3.9kOhm @3.3V  
'are recommended.  
  
```
Const Dogs104_adr_w = &H78 'I²C write address  
Const Dogs104_adr_r = &H79 'I²C read address  
  
  
```vb
'LCD has 2 view options. If LCD_view is set to 0 characters are being  
'displayed in bottom view (6 o'clock). If set to 1 characters are being  
'displayed in top view (12 0'clock)  
```
Const Lcd_view = 0 'bottom view  
```vb
'Const Lcd_view = 1 'top View  
  
  
'configuration is needed for defining start address of LCD RAM  
Config Lcd = 20x2  
  
  
'LCD comes with 3 different character sets. These can be accessed by setting  
'LCD_ROM  
```
Const Lcd_rom = 1 'ROM A  
```vb
'Const Lcd_rom = 2 'ROM B  
'Const Lcd_rom = 3 'ROM C  
  
  
'there are 2 custom procedures witch provide number of lines switching at  
'runtime. You can either choose 2 line mode with double hight fonts or regular  
'4 line mode. This is the standard mode used by Initlcd.  
$external 2line_mode  
$external 4line_mode  
  
'LCD -----------------------------------------------------------------  
  
Declare Sub 2line_mode  
Declare Sub 4line_mode  
  
'TWI-------------------------------------------------------------------  
Config Scl = Portc.5  
Config Sda = Portc.4  
```
I2cinit  
'TWI-------------------------------------------------------------------  
  
  
Initlcd  
```vb
Waitms 100  
  
'As with any other LCD module, you can define up to 8 additional characters  
'by using the regular Bascom command  
  
'-----------------------------------------------------------------  
```
Deflcdchar 1 , 32 , 32 , 4 , 10 , 17 , 10 , 4 , 32 ' circle  
'-----------------------------------------------------------------  
  
Cls  
  
Waitms 100  
  
Cursor Off  
  
Locate 1 , 1 : Lcd Chr(1)  
  
```vb
Wait 2  
  
'standard initialization of LCD is set to 4 line mode  
  
```
Cls  
  
Locate 1 , 1 : Lcd "line 1"  
Locate 2 , 1 : Lcd "line 2"  
Locate 3 , 1 : Lcd "line 3"  
Locate 4 , 1 : Lcd "line 4"  
  
```vb
Wait 2  
  
'-----------------------------------  
  
```
Cls  
  
'if needed LCD can be switched to 2 line mode  
2line_mode  
  
Locate 1 , 3 : Lcd "line 1"  
Locate 2 , 3 : Lcd "line 2"  
  
```vb
Wait 2  
  
' ... and back to 4 line mode  
  
```
4line_mode  
  
Cls  
  
Locate 1 , 3 : Lcd "line 1 "  
Locate 2 , 3 : Lcd "line 2"  
Locate 3 , 3 : Lcd "line 3"  
Locate 4 , 3 : Lcd "line 4"  
  
```vb
Wait 2  
  
'if desired you can put the LCD module in power down mode. This saves some  
'400µA.  
'Any other command applicable for DOGS104A using SSD1803A controller can be  
'issued by using regular Rcall _Lcd_control command with preloaded  
'R24 register.  
  
```
Display Off  
```vb
Waitms 100  
  
'power down ----------------  
  
```
R24 = &B00111010 '8 bit data RE1, REV0  
Lcdcmd R24  
  
  
  
R24 = &B00000011 'power down  
Lcdcmd R24  
  
R24 = &B00111000 '8 bit data RE0, IS0  
Lcdcmd R24  
  
```vb
'power down ----------------  
  
Wait 2  
  
'... and power up again. LCD RAM remains unchanged.  
  
'power up -----------------  
  
```
R24 = &B00111010 '8 bit data RE1, REV0  
Lcdcmd R24  
  
R24 = &B00000010 'power up  
Lcdcmd R24  
  
R24 = &B00111000 '8 bit data RE0, IS0  
Lcdcmd R24  
  
```vb
'power up -----------------  
  
Waitms 100  
```
Display On  
  
Locate 4 , 1 : Lcd "powered up"  
End