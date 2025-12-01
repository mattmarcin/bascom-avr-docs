# I2CSEND

Action

Send address and data to an I2C-device.

Syntax

I2CSEND slave, var

I2CSEND slave, var , bytes

Syntax Xmega

I2CSEND slave, var , #const

I2CSEND slave, var , bytes , #const

Remarks

Slave | The slave address off the I2C-device. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
Var | A byte, integer/word or numbers that holds the value, which will be, send to the I2C-device.  
Bytes | The number of bytes to send.  

#const | For the Xmega, a channel constant that was specified with OPEN.  
  
When an error occurs, the internal ERR variable will return 1. Otherwise it will be set to 0.

The I2CSEND statement combines the i2cstart,i2cwbyte and i2cstop statements.

For the xmega you can optional specify the channel. Without it, SPIC will be used.

The I2CSEND is a compound statement that will send : 

\- I2CSTART

\- I2C slave address for writing

\- I2C data

\- I2CSTOP

ASM

The I2C routines are located in the i2c.lib/i2c.lbx files.

See also

[I2CRECEIVE](i2creceive.md) , [I2CSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md), [I2CSTOP](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CRBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md)

Example

```vb
Config Sda = Portb.5

Config Scl = Portb.7

Dim X As Byte , A As Byte , Bytes As Byte

```
X = 5 'assign variable to 5

Dim Ax(10)as Byte

Const Slave = &H40 'slave address of a PCF 8574 I/O IC

I2csend Slave , X 'send the value or

For A = 1 To 10

Ax(a) = A 'Fill dataspace

Next

Bytes = 10

I2csend Slave , Ax(1) , Bytes

End