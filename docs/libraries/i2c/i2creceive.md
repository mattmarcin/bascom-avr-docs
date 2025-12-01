# I2CRECEIVE

Action

Receives data from an I2C serial slave device.

Syntax

I2CRECEIVE slave, var

I2CRECEIVE slave, var , b2W, b2R

Syntax Xmega

I2CRECEIVE slave, var , #const

I2CRECEIVE slave, var , b2W, b2R , #const

Remarks

Slave | A byte, Word/Integer variable or constant with the slave address from the I2C-device. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
Var | A byte or integer/word or numeric variable or array that will receive the information from the I2C-device. This same variable is used for sending the optional data as for receiving the data. This means that when you need to send/receive data, you first fill the variable with the data you will send. And when the statement ends, the variable will contain the data received. You should dimension the variable or array large enough to hold the data sent/received.  
b2W | The number of bytes to write. When you use a value of 0, no data will be sent.   
b2R | The number of bytes to receive. When you use a value of 0. no data will be received. But since this statement is to receive data, that would not make much sense.  

#const | For the Xmega, a channel constant that was specified with OPEN.  
  
You must specify the base address of the slave chip because the read/write bit is set/reset by the software.

When an error occurs, the internal ERR variable will return 1. Otherwise it will be set to 0.

The I2CRECEIVE statement combines the i2cstart,i2cwbyte, i2crbyte and i2cstop statements.

For the xmega you can optional specify the channel. Without it, SPIC will be used.

ASM

The I2C routines are located in the i2c.lib/i2c.lbx files.

See also

[I2CSEND](i2csend.md), [I2CSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CSTOP](i2start_i2cstop__i2crbyte__i2cwbyte.md), [I2CRBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md)

Example

```vb
Config Sda = Portb.5

Config Scl = Portb.7

Dim X As Byte , Slave As Byte

```
X = 0 'reset variable

Slave = &H40 'slave address of a PCF 8574 I/O IC

I2creceive Slave , X 'get the value

```vb
Print X 'print it

Dim Buf(10)as Byte

```
Buf(1) = 1 : Buf(2) = 2

I2creceive Slave , Buf(1) , 2 , 1 'send two bytes buf(1) and buf(2) and receive one byte into buf(1)

```vb
Print Buf(1) 'print the received byte

End

```