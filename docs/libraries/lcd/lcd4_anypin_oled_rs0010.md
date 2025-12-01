# LCD4_anypin_oled_RS0010

This LCD driver is intended to be used with the OLED LCD RS0010.

This LCD text driver can be used with any pin. It supports the WR pin in which case the LCD will be used in busy mode.

A typical sample is shown below.

```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack=32  
$swstack = 16  
$framesize=24  
  
  
  
$lib "lcd4_anypin_oled_RS0010.lib" 'override default lib with OLED lib  
  
'Config Lcd Sets The Portpins Of The Lcd  
Config Lcdpin = Pin , Db4 = Portb.2 , Db5 = Portb.3 , Db6 = Portb.4 , Db7 = Portb.5 , E = Portb.1 , Rs = Portb.0  
Config Lcd = 16x2 '16*2 type LCD screen  
  
Dim V As Byte  
  
```
Cls  
Lcd "ABC" ; Chr(253)  
Lowerline  
Lcd "test"  
Const Test = " this is a test" ' Just A Test  
  
Lcdfont 0 'select first font  
  
Cls  
Dim X As Byte , Y As Byte  
X = &B1000_0000 + 0  
Lcdcmd &B0001_1111 'gmode  
Lcdcmd X 'X (0-99)  
Lcdcmd &B0100_0000 'Y (0-1)  
  
```vb
'send data  
For V = 1 To 80  
```
Lcddata &B10101010  
```vb
Waitms 100  
Next  
End

```