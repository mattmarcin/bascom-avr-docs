# FM24C64_256-XMEGA

FM24C64_256-XMEGA is the XMEGA version of the [FM24C64_256](fm24c64_256.md) library.

This library is a library that uses a RAMTRON I2C serial EEPROM.

Ramtron memory chips are as quick as RAM and can be overwritten almost unlimited times. 

An external EEPROM is a safe alternative to the internal EEPROM.

By using : $lib "FM24C64_256-XMEGA.lib" 

The EEPROM read and write routines from the library will be used instead of the internal EEPROM.

Thus you can still use : Dim BE as ERAM Byte

And you can use READEEPROM and WRITEEEPROM, but instead of using the internal EEPROM, the external I2C EEPROM is used.

Since Xmega has up to 4 different TWI channels, you need to define which channel is used.

You need to do so by defining a constant in your code named cFRAM_CHANNEL and give it a value of 1 for TWIC, 2 for TWID, 4 for TWIE or 8 for TWIF.

![notice](notice.jpg)This library is only included in the full version. It is not included with the DEMO.

In version 2086 you can also read write strings. 

Example

  
'(  
  
The fm24c64_256-XMEGA library is a library that uses a RAMTRON I2C serial EEPROM.  
Ramtron memory chips are as quick as RAM and can be overwritten almost unlimited times.  
  
An external EEPROM is a safe alternative to the internal EEPROM.  
  
By using : $lib "fm24c64_256-xmega.lib"  
The EEPROM read and write routines from the library will be used instead of the internal EEPROM.  
Thus you can still use : Dim BE as ERAM Byte  
And you can use READEEPROM and WRITEEEPROM, but instead of using the internal EEPROM, the external I2C EEPROM is used.  
The lib is for the FM24C515. It uses I2C / TWI.  
  
You must define a constant in your code with a constant that defines the twi interface :  
CONST cfram_channel = 1 'twic  
CONST cfram_channel = 2 'twid  
CONST cfram_channel = 4 'twie  
CONST cfram_channel = 8 'twif  
  
This library is only included in the full version. It is not included with the DEMO.  
This library is especial for XMEGA and serves as a sample. reading/writing strings is NOT supported but can be added by the user  
  
  
```vb
')  
'-----------------------------------------------------------------------------------------  
'name : 24C512-xmega-simple-RW test-TWIE.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : Testing Read/Write operation with external EEPROM on TWIE  
'micro : xmega128A1  
'suited for demo : no  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "xM128a1def.dat"  
$crystal = 32000000 ' 32MHz  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
Config BASE = 0 ' arrays start at 0  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
'for debug we send some data to the UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Config Twie = 100000 ' CONFIG TWI will ENABLE the TWI master interface  
```
const cfram_channel = 4 ' this constant is required by the fm24c64_256-xmega lib  
' set it to 1 for TWIC , 2 for TWID , 4 for TWIE and 8 for TWIF  
Open "twie" For Binary As #4 ' when not using default twic, you must use a channel  
  
const _twi_stop_1 = 1 ' just test i2cstop option, see help  
  
Dim Twi_start As Byte ' always required for xmega i2c  
I2Cinit #4  
  
```vb
$eepromsize = &H400 ' set it to the size of your EEPROM  
$lib "fm24c64_256-xmega.lib" ' include lib  
  
  
dim ee(100) as eram byte ' dim an EEPROM array  
Dim B , adres As byte  
  
print "Writing EEEPROM"  
for adres = 0 to 10  
print adres ; ",";  
```
ee(adres) = adres  
```vb
waitms 20 ' ONLY FOR NORMAL EEPROM , REMOVE FOR RAMTRON  
next  
print  
  
print "read EEEPROM"  
  
for adres = 0 to 10  
```
b = ee(adres)  
```vb
print adres;"-";b  
next  
  
end

```