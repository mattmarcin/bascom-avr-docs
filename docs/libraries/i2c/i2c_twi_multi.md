# I2C_TWI-MULTI

The I2C_TWI-MULTI library is intended to be used with normal AVR processors which have 2 or more TWI interfaces.  
  
An example of such a processor is the ATMEGA328PB

In order to support multiple busses, this library need to be included using the $LIB directive.

Further you need to create a byte variable named _i2cchannel in your code.

This variable will hold the bus or TWI number.

By default it will be 0 and thus the usual TWI hardware will be used : Portc.5 and Portc.4

By setting the variable to 1, the second TWI hardware will be used : Porte.0 and Porte.1

Further you need to use CONFIG TWI1 instead of CONFIG TWI in order to specify the clock rate for the second TWI : Config Twi1 = 100000 

All other code will remain compatible.

Example

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