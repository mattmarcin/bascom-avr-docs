# CONFIG USI

Action

Configures the hardware USI.

Syntax

```vb
CONFIG USI=usimode , Address=adr , ALTPIN=port

CONFIG USI=usimode , Mode=mode , ALTPIN=port

```
Remarks

The USI(universal serial Interface) is found in most atTiny processors. It can be used for various tasks. At the moment only the TWI slave and TWI master modes are supported. The other modes you need to configure/code yourself.

The CONFIG USI = TWISLAVE mode requires a library that is part of the i2c slave add on which is a commercial add on.

The CONFIG USI = TWIMASTER also requires a library which is included in the commercial distribution. 

usiMode | The supported mode is :  \- TWISLAVE. This will set the USI in TWI slave mode. The USI works in interrupt mode on the background. The library i2c_usi_slave.lib contains the USI slave code. -TWIMASTER. This will set the USI in TWI master mode. This mode does not use interrupts. The library i2c_usi.lib contains the USI master code.  
---|---  
Address | This is the I2C/TWI slave address. Notice that bascom uses the 8-bit address notation. The address is only required when using the USI as a slave.  
Mode | The mode is only intended to be used with the USI in master mode. The options are : FAST and NORMAL. Normal will result in a 100 KHz clock signal. And FAST will use a 400 KHz signal if possible.  
Altpin | Some processor have an option to swap the USI pins. For example tiny261 can swap from default portB to portA. When not specified, the default pins will be used. When a different port is defined than the default, a constant will be created that is used inside the library. The USIPP register will be set to swap the pins.  It is not possible to swap pins dynamically.  
  
TWI SLAVE MODE

When USI is used in TWI/I2C mode, it does require that SCL and SDA have pull up resistors. You can not freely choose the SCL and SDA pins : you must use the fixed SCL en SDA pins.

The variables TWI_USI_OVS , TWI_slaveAddress, Twi , Twi_btr and Twi_btw are created by the compiler. These are all bytes.

The USI interrupts are enabled but you need to enabled the global interrupt using ENABLE INTERRUPTS

The USI Slave code is running as an interrupt process. Each time there is an USI interrupt some slave code is executed. Your BASIC code is called from the low level slave code at a number of events.

You must include all these labels in your Slave application. You do not need to write code in all these sub routines.

Label | Event  
---|---  
Twi_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata | The master has sent data. The variable TWI holds the received value. The byte TWI_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte | The master reads from the slave and needs a value. The variable TWI_BTR can be inspected to see which index byte was needed.   
  
TWI MASTER MODE

When USI is used in TWI/I2C mode, it does require that SCL and SDA have pull up resistors. You can not freely choose the SCL and SDA pins : you must use the fixed SCL en SDA pins.

The master mode does NOT require or use any variables. It also does not use any interrupts.

See also

[Using USI](using_usi_universal_serial_int.md) , [CONFIG TWISLAVE](config_twislave.md), [CONFIG TWIXSLAVE ](config_twixslave.md)

Example, USI SLAVE

```vb
'-------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' This demo demonstrates the USI I2C slave  
' Not all AVR chips have an USI !!!!  
'-------------------------------------------------------------------------------  
  
$regfile = "attiny2313.dat"  
  
$crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 24  
  
```
const cPrint = 0 'make 0 for chips that have NO UART, make 1 when the micro has a UART and you want to show data on the terminal  
  

```vb
#if cPrint  
$baud = 19200 'only when the processor has a UART  

#endif  
  
config usi = twislave , address = &H40 'bascom uses 8 bit i2c address (7 bit shifted to the left with one bit)  
  

#if cPrint  
print "USI DEMO"  

#endif  
  
'do not forget to enable global interrupts since USI is used in interrupt mode  
enable interrupts 'it is important you enable interrupts  
  
do  
```
! nop ; nothing to do here  
```vb
loop  
  
  
  
'The following labels are called from the library. You need to insert code in these subroutines  
'Notice that the PRINT commands are remarked.  
'You can unmark them and see what happens, but it will increase code size  
'The idea is that you write your code in the called labels. And this code must execute in as little time  
'as possible. So when you slave must read the A/D converter, you can best do it in the main program  
'then the data is available when the master requires it, and you do not need to do the conversion which cost time.  
  
  
'A master can send or receive bytes.  
'A master protocol can also send some bytes, then receive some bytes  
'The master and slave address must match.  
  
'the following labels are called from the library when master send stop or start  
```
Twi_stop_rstart_received:  
```vb
' Print "Master sent stop or repeated start"  
Return  
  
'master sent our slave address and will not send data  
```
Twi_addressed_goread:  
```vb
' Print "We were addressed and master will send data"  
Return  
  
  
```
Twi_addressed_gowrite:  
```vb
' Print "We were addressed and master will read data"  
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWI holds the received value  
```
Twi_gotdata:  
```vb
' Print "received : " ; Twi ; " byte no : " ; Twi_btw  
Select Case Twi_btw  
Case 1 : 'Portd = Twi ' first byte  
Case 2: 'you can set another port here for example  
End Select  
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twi_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twi_btr can be used for the index  
```
Twi_master_needs_byte:  
```vb
' Print "Master needs byte : " ; Twi_btr  
Select Case Twi_btr  
Case 1 : twi = 68 ' first byte  
Case 2 : twi = 69 ' send second byte  
End Select 'you could also return the state of a port pin or A/D converter  
Return

```
Example, USI Master

```vb
'------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' USI-MASTER.bas  
' USI used as TWI master demo  
'------------------------------------------------------------------------------  
  
$regfile = "attiny2313.dat"  
$crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 24  
$baud = 19200  
  
config usi = twimaster , mode = fast  
  
dim b as byte  
  
```
i2cinit  
  
do  
i2cstart  
i2cwbyte &H40 'send slave WRITE address for PCF8574  
i2cwbyte &B10101010 'send a pattern  
i2crepstart 'repeated start  
  
i2cwbyte &H41 'send slave READ address  
i2crbyte b , ack 'read a byte  
i2crbyte b , nack 'and again  
i2cstop 'end transaction and free bus  
  
```vb
waitms 100 'some delay not required only when you print  
loop

```