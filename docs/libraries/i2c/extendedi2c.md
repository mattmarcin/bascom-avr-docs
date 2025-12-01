# EXTENDED I2C

Action

Instruct the compiler to use parts of the extended i2c library

Syntax

$LIB = "i2c_extended.lib"

Remarks

The I2C library was written when the AVR architecture did not have extended registers. The designers of the AVR chips did not preserve enough space for registers. So when they made bigger chips with more ports they ran out of registers.

They solved it to use space from the RAM memory and move the RAM memory from &H60 to &H100.

In the free space from &60 to &H100 the new extended register were located.

While this is a practical solution, some ASM instructions could not be used anymore. This made it a problem to use the I2C statements on PORTF and PORTG of the Mega128.

The extended i2c library is intended to use I2C on portF and portG on the M64 and M128.

It uses a bit more space then the normal I2C lib.

Best would be that you use the TWI interface and the i2c_twi library as this uses less code. The disadvantage is that you need fixed pins as TWI used a fix pin for SCL and SDA.

See also

[I2C](i2start_i2cstop__i2crbyte__i2cwbyte.md)

ASM

NONE

Example

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This demo shows an example of I2C on the M128 portF

' PORTF is an extened port and requires a special I2C driver

'-------------------------------------------------------------------------------

$regfile = "m128def.dat" ' the used chip

$crystal = 8000000

$baud = 19200 ' baud rate

$lib "i2c_extended.lib"

Config Scl = Portf.0 ' we need to provide the SCL pin name

Config Sda = Portf.1 ' we need to provide the SDA pin name

Dim B1 As Byte , B2 As Byte

Dim W As Word At B1 Overlay

```
I2cinit ' we need to set the pins in the proper state

```vb
Dim B As Byte , X As Byte

Print "Mega128 master demo"

Print "Scan start"

For B = 1 To 254 Step 2

```
I2cstart

I2cwbyte B

```vb
If Err = 0 Then

Print "Slave at : " ; B

End If

```
I2cstop

```vb
Next

Print "End Scan"

Do

```
I2cstart

I2cwbyte &H70 ' slave address write

I2cwbyte &B10101010 ' write command

I2cwbyte 2

I2cstop

Print Err

I2cstart

I2cwbyte &H71

I2crbyte B1 , Ack

I2crbyte B2 , Nack

I2cstop

```vb
Print "Error : " ; Err ' show error

Waitms 500 'wait a bit

Loop

End

```