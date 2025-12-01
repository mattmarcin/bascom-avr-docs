# CONFIG I2CDELAY

Action

Compiler directive that overrides the internal I2C delay routine.

(Only for Software I2C Routines)

Syntax

CONFIG I2CDELAY = value

Remarks

value | A numeric value in the range from 1 to 255.  A higher value means a slower I2C clock. You may use a value of 0 too but it will result in a value of 256.  
---|---  
  
For the I2C routines the clock rate is calculated depending on the used crystal. In order to make it work for all I2C devices the slow mode is used. When you have faster I2C devices you can specify a low value.

By default a value of 5 is used. This will give a 200 kHZ clock.

When you specify 10, 10 uS will be used resulting in a 100 KHz clock.

When you use a very low crystal frequency, it is not possible to work with high clock frequencies.

ASM

The I2C routines are located in the i2c.lib/i2c.lbx files.

For chips that have hardware TWI, you can use the MasterTWI lib.

See also

[CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md), [Using the I2C protocol](using_the_i2c_protocol.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : i2c.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demo: I2CSEND and I2CRECEIVE  
'micro : Mega48  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m48def.dat" ' specify the used micro  
$crystal = 4000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
'We use here the Software I2C Routines  
Config Scl = Portb.4  
Config Sda = Portb.5  
```
I2cinit  
  
```vb
Config I2cdelay = 10 '100KHz  
  
Declare Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
Declare Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
  
```
Const Addressw = 174 'slave write address  
Const Addressr = 175 'slave read address  
  
Dim B1 As Byte , Adres As Byte , Value As Byte 'dim byte  
  
Call Write_eeprom(1 , 3) 'write value of three to address 1 of EEPROM  
Call Read_eeprom(1 , Value) : Print Value 'read it back  
Call Read_eeprom(5 , Value) : Print Value 'again for address 5  
  
  
'-------- now write to a PCF8474 I/O expander -------  
I2csend &H40 , 255 'all outputs high  
I2creceive &H40 , B1 'retrieve input  
```vb
Print "Received data " ; B1 'print it  
End  
  
```
Rem Note That The Slaveaddress Is Adjusted Automaticly With I2csend & I2creceive  
Rem This Means You Can Specify The Baseaddress Of The Chip.  
  
```vb
'sample of writing a byte to EEPROM AT2404  
Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
```
I2cstart 'start condition  
I2cwbyte Addressw 'slave address  
I2cwbyte Adres 'asdress of EEPROM  
I2cwbyte Value 'value to write  
I2cstop 'stop condition  
```vb
Waitms 10 'wait for 10 milliseconds  
End Sub  
  
'sample of reading a byte from EEPROM AT2404  
Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
```
I2cstart 'generate start  
I2cwbyte Addressw 'slave adsress  
I2cwbyte Adres 'address of EEPROM  
I2cstart 'repeated start  
I2cwbyte Addressr 'slave address (read)  
I2crbyte Value , Nack 'read byte  
I2cstop 'generate stop  
```vb
End Sub  
  
' when you want to control a chip with a larger memory like the 24c64 it requires an additional byte  
' to be sent (consult the datasheet):  
' Wires from the I2C address that are not connected will default to 0 in most cases!  
  
' I2cstart 'start condition  
' I2cwbyte &B1010_0000 'slave address  
' I2cwbyte H 'high address  
' I2cwbyte L 'low address  
' I2cwbyte Value 'value to write  
' I2cstop 'stop condition  
' Waitms 10

```