# CONFIG TWISLAVE

Action

Configure the TWI Slave address and bit rate

Syntax

CONFIG TWISLAVE = address , BTR = value , BITRATE = value , SAVE=option [,GENCALL=value] [,USERACK=ack]

(I2C TWI Slave is part of the I2C-Slave library. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

See also: [I2C TWI Slave](i2ctwislave.md), [USING I2C Protocol](using_the_i2c_protocol.md), [Using USI](using_usi_universal_serial_int.md), [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md)

Remarks

Address | The slave address that is assigned to the slave chip. This must be an Even number. Bit 0 of the address is used to activate the general call address. The GENCAL option will set this bit automatic. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
BTR | Bytes to receive. With this constant you specify how many bytes will be expected when the master reads data from the slave. And thus how many bytes will be sent to the master.  
Bit rate | This is the I2C/TWI clock frequency. Most chips support 400 KHz (400000) but all I2C chips support 100000.  
SAVE | SAVE = NOSAVE : this can be used when you do not change a lot of registers in the interrupt. SAVE = SAVE : this is best to be used when you do not use ASM in the TWI interrupt. See the explanation below. When you do not specify SAVE, the default will be SAVE=SAVE.  
GENCALL | General call address activated or not. When you specify 1 or YES, the General call address will be activated which mean that the slave will respond not only to it's own address, but also to the general call address 0.  When you omit the option or specify 0 or NO, the general call address will not be honored.   
USERACK | Default is OFF. When you use ON, an alternative library will be used. This library will create a variable named TWI_ACK.  Each time your code is called this variable is filled with the value 255. If you do not alter the value, the slave will send an ACK as it is supposed to. If you reset the value to 0, the slave will send a NACK. You can use this to send data with variable length to the slave. In this case, BTR only serves as an index. You must make sure to reset TWI_ACK when you have send the last byte to the master.  
  
The variables Twi , Twi_btr and Twi_btw are created by the compiler. These are all bytes

The TWI interrupt is enabled but you need to enabled the global interrupt

The TWI Slave code is running as an interrupt process. Each time there is a TWI interrupt some slave code is executed. Your BASIC code is called from the low level slave code under a number of events. You must include all these labels in your Slave application. You do not need to write code in all these sub routines. All the time your user code is executed, the clock line is stretched. This will reduce the TWI bus speed. So it is important that you do not put delays in your code. 

Label | Event  
---|---  
Twi_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata | The master has sent data. The variable TWI holds the received value. The byte TWI_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte | The master reads from the slave and needs a value. The variable TWI_BTR can be inspected to see which index byte was needed. With the CONFIG BTR, you specify how many bytes the master will read.  
  
In most cases your main application is just an empty DO LOOP. But when you write a slave that performs other tasks on the background these other tasks are interrupted by the TWI traffic.

Take in mind that the interrupt with the lowest address has the highest priority.

So do NOT write blocking code inside an interrupt. While servicing another interrupt, the TWI interrupt can not be serviced.

The TWI Slave code will save all used registers.

But since it will call your BASIC application when the TWI interrupt occurs, your BASIC code could be in the middle of say a PRINT statement.

When you then execute another PRINT statement , you will destroy registers.

So keep the code in the sub routines to a minimum, and use SAVE option to save all registers. This is the default.

While two printing commands will give odd results (print 12345 and 456 in the middle of the first print will give 1234545) at least no register is destroyed.

A typical configuration is shown below.

![i2c_slave](i2c_slave.png)

To test the above hardware, use the samples : twi-master.bas and twi-slave.bas

Optional you can use i2cscan.bas to test the general call address.

When you want to change the address of the slave at run time you need to write to the TWAR register.

The TWAR register contains the slave address. Bit 0 which is used to indicate a read or write transaction should be cleared. When you set it, the slave will also recognize the general call address. The GENCALL option just sets bit 0 of the slave.

See also

[CONFIG TWI](config_twi.md) , [CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md) , [I2C TWI Slave](i2ctwislave.md), [Using the I2C protocol](using_the_i2c_protocol.md)

ASM

NONE

Example1(master)

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This demo shows an example of the TWI

' Not all AVR chips have TWI (hardware I2C)

'-------------------------------------------------------------------------------

'The chip will work in TWI/I2C master mode

'Connected is a PCF8574A 8-bits port extender

$regfile = "M88def.dat" ' the used chip

$crystal = 8000000 ' frequency used

$baud = 19200 ' baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI

Config Scl = Portc.5 ' we need to provide the SCL pin name

Config Sda = Portc.4 ' we need to provide the SDA pin name

'On the Mega88, On the PCF8574A

'scl=PC5 , pin 28 pin 14

'sda=PC4 , pin 27 pin 15

```
I2cinit ' we need to set the pins in the proper state

```vb
Config Twi = 100000 ' wanted clock frequency

'will set TWBR and TWSR

'Twbr = 12 'bit rate register

'Twsr = 0 'pre scaler bits

Dim B As Byte , X As Byte

Print "TWI master"

Do

```
Incr B ' increase value

I2csend &H0 , B ' send the value to general call address

I2csend &H70 , B ' send the value

Print "Error : " ; Err ' show error status

I2creceive &H70 , X ' get a byte

```vb
Print X ; " " ; Err ' show error

Waitms 500 'wait a bit

Loop

End

```
Example2(slave)

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This demo shows an example of the TWI in SLAVE mode

' Not all AVR chips have TWI (hardware I2C)

' IMPORTANT : this example ONLY works when you have the TWI slave library

' which is a commercial add on library, not part of BASCOM

'Use this sample in combination with i2cscan.bas and/or twi-master.bas

'-------------------------------------------------------------------------------

$regfile = "M88def.dat" ' the chip we use

$crystal = 8000000 ' crystal oscillator value

$baud = 19200 ' baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Print "MCS Electronics TWI-slave demo"

Config Twislave = &H70 , Btr = 1 , Bitrate = 100000 , Gencall = 1

'In i2c the address has 7 bits. The LS bit is used to indicate read or write

'When the bit is 0, it means a write and a 1 means a read

'When you address a slave with the master in bascom, the LS bit will be set/reset automatic.

'The TWAR register in the AVR is 8 bit with the slave address also in the most left 7 bits

'This means that when you setup the slave address as &H70, TWAR will be set to &H0111_0000

'And in the master you address the slave with address &H70 too.

'The AVR TWI can also recognize the general call address 0. You need to either set bit 0 for example

'by using &H71 as a slave address, or by using GENCALL=1

'as you might need other interrupts as well, you need to enable them all manual

Enable Interrupts

'this is just an empty loop but you could perform other tasks there

Do

```
nop

```vb
Loop

End

'A master can send or receive bytes.

'A master protocol can also send some bytes, then receive some bytes

'The master and slave must match.

'the following labels are called from the library

```
Twi_stop_rstart_received:

```vb
Print "Master sent stop or repeated start"

Return

```
Twi_addressed_goread:

```vb
Print "We were addressed and master will send data"

Return

```
Twi_addressed_gowrite:

```vb
Print "We were addressed and master will read data"

Return

'this label is called when the master sends data and the slave has received the byte

'the variable TWI holds the received value

```
Twi_gotdata:

```vb
Print "received : " ; Twi

Return

'this label is called when the master receives data and needs a byte

'the variable twi_btr is a byte variable that holds the index of the needed byte

'so when sending multiple bytes from an array, twi_btr can be used for the index

```
Twi_master_needs_byte:

Print "Master needs byte : " ; Twi_btr

Twi = 65 ' twi must be filled with a value

```vb
Return

'when the mast has all bytes received this label will be called

```
Twi_master_need_nomore_byte:

```vb
Print "Master does not need anymore bytes"

Return

```