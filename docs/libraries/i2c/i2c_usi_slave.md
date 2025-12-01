# I2C_USI_SLAVE

The I2C_USI_SLAVE library is a library that ships with the I2C slave add on package.

The purpose of the lib is to offer I2C/TWI slave support for processors that have an USI interface.

USI master support is bundled with the commercial version of Bascom. This library is named i2_USI.

The USI has two interrupts. One to detect the START condition and one to detect a counter overflow.

Unfortunately Atmel did not define an interrupt for STOP condition. This means that it is not possible to detect a STOP condition with an interrupt. 

You can read the STOP condition bit from the USISR register but no interrupt will fire as for the START condition.

So in practice, the Twi_stop_received label will be called just before the I2CSTART is called or when data is clocked by the master.

The following example demonstrates how to receive multiple bytes. It emulates an I2c, EEPROM memory chip.

Example

```vb
'-------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' This demo demonstrates the USI I2C slave and emulates an EEPROM chip  
' This is part of the I2C Slave library which is a commercial addon library  
' Not all AVR chips have an USI !!!!  
'-------------------------------------------------------------------------------  
' This is a simple sample. the master sends the address of the slave, the WORD address  
' of the memory location, and a byte to store or read  
'------------------------------------------------------------------------------  
' The matching master code to write  
' i2cstart : i2cwbyte &H40 : i2cwbyte low(address) : i2cwbyte high(address) : i2cwbyte value : i2cstop  
' The mathing master code to read  
' i2cstart : i2cwbyte &H40 : i2cwbyte low(address) : i2cwbyte high(address) : i2crepstart : i2cwbyte &H41 : i2cRbyte value, nack : i2cstop  
'See also the eeprom_master.bas  
  
$regfile = "attiny2313.dat"  
'$regfile = "attiny85.dat"  
$crystal = 8000000  
$hwstack = 44  
$swstack = 16  
$framesize = 28  
config CLOCKDIV=1  
'I2C pins on tiny2313 connected like :  
'PB5 SDA  
'PB7 SCL  
  
'I2C pins on tiny85 connected like :  
'PB0 SDA  
'PB2 SCL  
  
config BASE=0 'arrays start at address 0  
  
```
Const Cprint = 0 'make 0 for chips that have NO UART, make 1 when the micro has a UART and you want to show data on the terminal  
  

```vb
#if cPrint  
Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
print "USI DEMO"  

#endif  
  
  
config usi = twislave , address = &H40 'bascom uses 8 bit i2c address (7 bit shifted to the left with one bit)  
  
dim epr(128) as Eram byte 'for easy access to the memory  
dim wAdres as Word, bValue as Byte  
dim bAdresL as Byte at Wadres overlay 'overlay with wAdres LSB  
dim bAdresH as Byte at Wadres+1 overlay 'overlay with wAdres MSB  
  
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
Twi_start_received:  

```vb
#if cprint  
Print "Master sent start or repeated start"  

#endif  
Return  
  
```
Twi_stop_received:  

```vb
#if cprint  
Print "Master sent stop"  

#endif  
Return  
  
'master sent our slave address and will now send data  
```
Twi_addressed_goread:  

```vb
#if cprint  
Print "We were addressed and master will send data"  

#endif  
Return  
  
  
```
Twi_addressed_gowrite:  

```vb
#if cprint  
Print "We were addressed and master will read data"  

#endif  
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWI holds the received value  
```
Twi_gotdata:  

```vb
#if cprint  
Print "received : " ; Twi ; " byte no : " ; Twi_btw ; "-"; usidr  

#endif  
Select Case Twi_btw  
Case 1 : bAdresL=TWI 'first byte is LSB  
Case 2 : bAdresH=TWI 'second byte is MSB  
case 3 :  

#if cprint  
print "address:" ; wAdres  

#endif  
```
epr(wAdres)=twi 'write to eeprom in case we receive a third byte which should only happen when we write to the slave  
```vb
End Select  
  
'if you want to auto inc wAdres, use this code instead:  
' Select Case Twi_btw  
' Case 1 : bAdresL=TWI 'first byte is LSB  
' Case 2 : bAdresH=TWI 'second byte is MSB  
' case else : epr(wAdres)=twi 'write to eeprom in case we receive a third byte which should only happen when we write to the slave  
' incr wAdres  
' End Select  
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twi_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twi_btr can be used for the index  
```
Twi_master_needs_byte:  

```vb
#if cprint  
Print "Master needs byte : " ; Twi_btr  
print "address:" ; wAdres  

#endif  
```
twi=epr(wAdres) 'return the data from EEPROM  
```vb
'when you want to support auto adres increase add this :  
'incr wAdres  
Return

```
The following master sample can be used with the slave sample.

Master sample

```vb
'------------------------------------------------------------------------------  
' eeprom_master.bas  
' demo for USI eeprom slave  
'  
'  
'------------------------------------------------------------------------------  
$Regfile= "m88pdef.dat"  
$crystal=8000000  
$HWstack=40  
$SWstack=50  
$FrameSize=40  
$baud=19200  
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
  
config CLOCKDIV=1 ' no need to change fuse byte, we set the divider to 1  
Config Sda = Portc.4 ' I2C Bus konfigurieren  
Config Scl = Portc.5  
  
Dim Address As Word  
Dim Value As Byte  
'!!!!!!!!!!!!!!!!!!!!  
'osccal=46 'REMARK THIS LINE, THIS WAS REQUIRED for the test chip  
'!!!!!!!!!!!!!!!!!!!!  
  
Print "Start"  
```
I2cinit ' init i2c  
For Address = 0 To 10 ' just test a bit  
value=address+10  
print "write "; address ; ":";value  
  
I2cstart : I2cwbyte &H40 'slave address  
I2cwbyte Low(address) 'LSB first  
I2cwbyte High(address) 'MSB  
I2cwbyte Value 'write value  
I2cstop  
```vb
Waitms 500  
next  
  
print "Read"  
For Address = 0 To 10  
' The mathing master code to read  
```
I2cstart : I2cwbyte &H40 'send slave WRITE address  
I2cwbyte Low(address) : I2cwbyte High(address) : 'send eeprom address  
I2crepstart 'repeated start  
I2cwbyte &H41 'write slave READ address  
I2crbyte Value , Nack 'read eeprom value  
I2cstop  
```vb
print address;":";value  
Next Address ' increment address byte  
  
end  
  
'EXPECTED OUTPUT  
'(  
```
Start  
write 0:10  
write 1:11  
write 2:12  
write 3:13  
write 4:14  
write 5:15  
write 6:16  
write 7:17  
write 8:18  
write 9:19  
write 10:20  
Read  
0:10  
1:11  
2:12  
3:13  
4:14  
5:15  
6:16  
7:17  
8:18  
9:19  
10:20  
')