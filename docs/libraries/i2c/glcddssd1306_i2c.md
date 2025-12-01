# GLCDdSSD1306-I2C

This library is based on work of Ben Zijstra and Heiko/Hkipnik

The library supports the SSD1306 graphical LCD in I2C mode.

Since the display can not read data back, the library supports only the graphical write statements. Commands like LINE, PSET and CIRCLE which need to alter a single pixel are not supported.

XMEGA

For use with XMEGA you need to define 2 constants in your code.

const TWI_ADR = interface

const TWI_CH = num

The interface must point to the TWI control register, this could be : TWIC_CTRL but aldo TWID_CTRL, TWIE_CTRL and TWIF_CTRL

The TWI_CH constant with the value num, must be 1 for TWIC, 2 for TWID, 4 for TWIE and 8 for TWIF

The reference to : $lib "i2c_twi.lbx" must be removed.

Example

```vb
'-------------------------------------------------------------------------------  
' SSD1306-I2C.BAS  
' (c) 1995-2025 MCS Electronics  
' Sample to demo the 128x64 I2C OLED display  
'  
'-------------------------------------------------------------------------------  
$regfile = "m88pdef.dat"  
$hwstack = 32  
$swstack = 32  
$framesize = 32  
$crystal = 8000000  
Config Clockdiv = 1 ' make sure the chip runs at 8 MHz  
  
Config Scl = Portc.5 ' used i2c pins  
Config Sda = Portc.4  
Config Twi = 400000 ' i2c speed  
  
```
I2cinit  
```vb
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
$lib "glcdSSD1306-I2C.lib" ' override the default lib with this special one  
  

#if _build < 20784  
Dim ___lcdrow As Byte , ___lcdcol As Byte ' dim these for older compiler versions  

#endif  
  
Config Graphlcd = Custom , Cols = 128 , Rows = 64 , Lcdname = "SSD1306"  
```
Cls  
Setfont Font8x8tt ' select font  
  
Lcdat 1 , 1 , "BASCOM-AVR"  
Lcdat 2 , 10 , "1995-2020"  
Lcdat 8 , 5 , "MCS Electronics" , 1  
Waitms 3000  
  
Showpic 0 , 0 , Plaatje  
  
```vb
End  
  
  
$include "font8x8TT.font" ' this is a true type font with variable spacing  
  
  
```
Plaatje:  
$bgf "ks108.bgf" ' include the picture data