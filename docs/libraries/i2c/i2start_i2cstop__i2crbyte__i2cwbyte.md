# I2START,I2CSTOP, I2CRBYTE, I2CWBYTE, I2CREPSTART

Action

I2CSTART generates an I2C start condition.

I2CREPSTART generates an I2C repeated start condition.

I2CSTOP generates an I2C stop condition.

I2CRBYTE receives one byte from an I2C-device.

I2CWBYTE sends one byte to an I2C-device.

Syntax

I2CSTART

I2CREPSTART

I2CSTOP

I2CRBYTE var, ack/nack

I2CWBYTE val

Syntax Xmega

I2CSTART #const

I2CREPSTART #const

I2CSTOP #const

I2CRBYTE var, ack/nack , #const

I2CWBYTE val , #const

Remarks

Var | A variable that receives the value from the I2C-device.  
---|---  
ack/nack | Specify ACK if there are more bytes to read. Specify NACK if it is the last byte to read.  
Val | A variable or constant to write to the I2C-device.  

#const | For the Xmega, a channel constant that was specified with OPEN.  
  
These statements are provided as an addition to the I2CSEND and I2CRECEIVE statements.

While I2csend and I2CRECEIVE are well suited for most tasks, a slave chip might need a special sequence that is not possible with these I2C routines.

Using I2CSTART, I2CWBYTE, I2CRBYTE and I2CSTOP you can create any I2C sequence you need.

When an error occurs, the internal Err variable will return 1. Otherwise it will be set to 0.

The Xmega has multiple TWI interfaces. You can use a channel to specify the TWI interface. 

When you do not use a channel the TWIC interface will be used.

![notice](notice.jpg) When using a repeated start, you must use I2CREPSTART on the XMega ! This is also true when using the [i2cv2](i2cv2.md).lib.

Normal AVR processors may use either I2CSTART or I2CREPSTART.

![notice](notice.jpg)For Xmega, the I2CSTART does not actually create a bus START signal. This because for Xmega the start is combined with the first data write (the address).

This means that ERR will always return 0 for Xmega I2CSTART. For this reason the bus scanner example checks ERR after the address write.

All I2C statements are master mode statements. They are stored in the i2c.lib. There is also an improved version of this library available named i2cv2.lib

Since the repeated start is not compatible with the one from i2c.lib, you need to specify yourself that you want to use the improved lib. See also [I2CV2](i2cv2.md).

I2CSTOP and Xmega

The I2CSTOP statement on the Xmega can be influenced by defining a constant in your code.

There are two optional constant you can define.

Const _TWI_STOP_1 = 1

or

Const _TWI_STOP_2 = 1

Notice that the value does not matter ! The library only checks if the constant exists. Also notice that there are 2 different constants. 

When not defining any of the above constants, the default will be used as it was in version 2079.

This default will send a stop, then checks if the bus is not in the owner state, and send new stop commands till it becomes in non-owner state.

Some slave chips choke on multiple stop commands. In such a case you can define the constant named _TWI_STOP_2

This will send a stop, and then keep checking till the bus is in non-owner state.

The last mode you get when defining a constant named _TWI_STOP_1

This will only send a stop without checking if the bus is non-owner. This can have advantages. But generating a new I2CSTART could fail since the bus is not in the right mode yet. You should check the ERR variable in such a case after the I2CSTART command.

ASM

The I2C routines are located in the i2c.lib/i2c.lbx files. There is also an alternative i2c_twi.lib for when using TWI, and an alternative soft lib named i2cv2.lib

For the XMega, the routines are located in the xmega.lib file.

See also

[I2CSEND](i2csend.md) , [I2CRECEIVE](i2creceive.md) , [I2CSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CSTOP](i2start_i2cstop__i2crbyte__i2cwbyte.md), [I2CRBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md), [Using the I2C protocol](using_the_i2c_protocol.md), [CONFIG TWI](config_twi.md) , [I2CV2](i2cv2.md)

Example (using Software I2C Routines)

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
$swstack = 20 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Config Scl = Portb.4  
Config Sda = Portb.5  
```
I2cinit  
  
  
```vb
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
Xmega Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-TWI.bas  
' This sample demonstrates the Xmega128A1 TWI  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Dim S As String * 20  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Dim N As String * 16 , B As Byte  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Config Input1 = Cr , Echo = Crlf ' CR is used for input, we echo back CR and LF  
  
```
Open "COM1:" For Binary As #1  
```vb
' ^^^^ change from COM1-COM8  
  
Print #1 , "Xmega revision:" ; Mcu_revid ' make sure it is 7 or higher !!! lower revs have many flaws  
  
```
Const Usechannel = 1  
  
  
```vb
Dim B1 As Byte , B2 As Byte  
Dim W As Word At B1 Overlay  
  
```
Open "twic" For Binary As #4 ' Use TWI on Port C  
```vb
'you can also use TWIC, TWID, TWIE of TWIF   
Config Twi = 100000 ' 100KHz  
  
  

#if Usechannel = 1  
```
I2cinit #4  

#else  
I2cinit  

```vb
#endif  
  
  
Do  
```
I2cstart  
Waitms 20  
I2cwbyte &H70 ' slave address write  
Waitms 20  
I2cwbyte &B10101010 ' write command  
Waitms 20  
I2cwbyte 2  
Waitms 20  
I2cstop  
```vb
Print "Error : " ; Err ' show error status  
  
'waitms 50  
Print "start"  
```
I2cstart  
Print "Error : " ; Err ' show error  
I2cwbyte &H71  
Print "Error : " ; Err ' show error  
I2crbyte B1 , Ack  
Print "Error : " ; Err ' show error  
I2crbyte B2 , Nack  
Print "Error : " ; Err ' show error  
I2cstop  
```vb
Print "received A/D : " ; W ; "-" ; B1 ; "-" ; B2  
Waitms 500 'wait a bit  
Loop  
  
  
  
Dim J As Byte , C As Byte , K As Byte  
Dim Twi_start As Byte ' you MUST dim this variable since it is used by the lib  
  
'determine if we have an i2c slave on the bus  
For J = 0 To 200 Step 2  
Print J  

#if Usechannel = 1  
```
I2cstart #4  

#else  
I2cstart  

#endif  
  
I2cwbyte J  
```vb
If Err = 0 Then ' no errors  
Print "FOUND : " ; Hex(j)  
'write some value to the pcf8574A  

#if Usechannel = 1  
```
I2cwbyte &B1100_0101 , #4  

#else  
I2cwbyte &B1100_0101  

```vb
#endif  
Print Err  
Exit For  
End If  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
Next  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
  

#if Usechannel = 1  
```
I2cstart #4  
I2cwbyte &H71 , #4 ' read address  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack , #4  
Print Bin(j) ; " err:" ; Err  
I2cstop #4  

#else  
I2cstart  
I2cwbyte &H71 ' read address  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack  
Print Bin(j) ; " err:" ; Err  
I2cstop  

```vb
#endif  
  
'try a transaction  

#if Usechannel = 1  
```
I2csend &H70 , 255 , #4 ' all 1  
Waitms 1000  
I2csend &H70 , 0 , #4 ' all 0  

#else  
I2csend &H70 , 255  
Waitms 1000  
I2csend &H70 , 0  

```vb
#endif  
Print Err  
  
  
'read transaction  
Dim Var As Byte  
```
Var = &B11111111  

#if Usechannel = 1  
I2creceive &H70 , Var , 1 , 1 , #4 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 , #4 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#else  
```
I2creceive &H70 , Var , 1 , 1 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#endif  
  
End

```