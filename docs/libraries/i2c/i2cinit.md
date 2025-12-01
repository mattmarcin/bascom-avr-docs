# I2CINIT

Action

Initializes the SCL and SDA pins.

Syntax

I2CINIT

I2CINIT twi

I2CINIT #const

Remarks

By default the SCL and SDA pins are in the right state when you reset the chip. Both the PORT and the DDR bits are set to 0 in that case.

When you need to change the DDR and/or PORT bits you can use I2CINIT to bring the pins in the proper state again.

```vb
For the XMEGA which has multiple TWI interfaces you can use a channel to specify the TWI interface otherwise the default TWIC will be used.

For normal AVR processors with multiple TWI interfaces you can specify the interface : TWI or TWI1.

```
When no parameter is provided, the first default TWI will be selected.

ASM

The I2C routines are located in i2c.lib. _i2c_init is called.

See also

[I2CSEND](i2csend.md) , [I2CSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CSTOP](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CRBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2C_TWI Library for using TWI](i2c_twi.md)

Example

```vb
Config Sda = Portb.5

Config Scl = Portb.7

```
I2cinit

Dim X As Byte , Slave As Byte

X = 0 'reset variable

Slave = &H40 'slave address of a PCF 8574 I/O IC

I2creceive Slave , X 'get the value

Print X 'print it

Example XMEGA

Open "twic" For Binary As #4 ' or use TWID,TWIE oR TWIF

Config TwiC = 100000 'CONFIG TWI will ENABLE the TWI master interface

I2cinit #4

Example Mega328PB

```vb
'--------------------------------------------------------------------------------  
'name : m328pb.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates M328pb  
'micro : Mega328pb  
'suited for demo : yes  
'commercial addon needed : no  
'--------------------------------------------------------------------------------  
$regfile = "m328pbdef.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
' USART TX RX  
' 0 D.1 D.0  
' 1 B.3 B.4  
  
' ISP programming  
' MOSI-PB3 MISO-PB4 SCK-PB5  
  
' TWI SDA SCL  
' 0 C.4 C.5  
' 1 E.0 E.1  
  
'Configuration  
  
Config Clockdiv = 1 'make sure we get 8 Mhz from internal osc  
  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
'we have 2 TWI interfaces  
Config Scl = Portc.5 ' we need to provide the SCL pin name  
Config Sda = Portc.4 ' we need to provide the SDA pin name  
  
Config Sda1 = Porte.0 'use this for the second TWI  
Config Scl1 = Porte.1  
  
Config Twi = 100000 'speed 100 KHz  
Config Twi1 = 100000 'speed 100 KHz  
  
'some constants for the signature row  
```
Const Device_signature_byte1 = 0  
Const Device_signature_byte2 = 2  
Const Device_signature_byte3 = 4  
  
Const Rc_oscillator_calibration = 1  
  
Const Serial_number_byte0 = &H0E  
Const Serial_number_byte1 = &H0F  
Const Serial_number_byte2 = &H10  
Const Serial_number_byte3 = &H11  
Const Serial_number_byte4 = &H12  
Const Serial_number_byte5 = &H13  
Const Serial_number_byte6 = &H14  
Const Serial_number_byte7 = &H15  
Const Serial_number_byte8 = &H16  
Const Serial_number_byte9 = &H17  
  
```vb
$lib "I2C_TWI-MULTI.lib" 'important for using 2 TWI interfaces  
  
Dim _i2cchannel As Byte ' you MUST dim this variable yourself when using the above lib  
Dim B As Byte 'just a used byte  
  
```
I2cinit 'default TWI init  
I2cinit Twi1 'optional specify TWI1 to init that interface  
  
Open "com2:" For Binary As #2 'create a channel to reference the UART  
  
```vb
'print the chip ID  
Print "ID : " ; Hex(readsig(device_signature_byte1)) ; Hex(readsig(device_signature_byte2)) ; Hex(readsig(device_signature_byte3))  
  
'all I2C statements will work the same. All you need to do is to set the _i2cchannel variable to 0 or 1  
```
_i2cchannel = 1 'try the second bus  
  
```vb
Print "Scan start"  
For B = 0 To 254 Step 2 'for all odd addresses  
```
I2cstart  
I2cwbyte B 'send address  
```vb
If Err = 0 Then 'we got an ack  
Print "Slave at : " ; B ; " hex : " ; Hex(b) ; " bin : " ; Bin(b)  
End If  
```
I2cstop 'free bus  
```vb
Next  
  
  
Do  
Print "COM1"  
Print #2 , "COM2"  
Waitms 1000  
Loop

```