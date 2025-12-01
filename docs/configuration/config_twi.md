# CONFIG TWI, TWIx

Action

Configure the TWI (two wire serial interface) when using hardware I2C/TWI.

Syntax

```vb
CONFIG TWI = clockspeed

CONFIG TWI1 = clockspeed

```
Syntax XMEGA

CONFIG TWIC | TWID | TWIE | TWIF = clockspeed

(Config TWI and TWI1 is for ATMEGA and Config TWIX is for ATXMEGA chips)

Syntax XTINY

CONFIG TWI|TWI0|TWI1 = clockspeed

The XTINY uses TWI0. TWI and TWI0 are similar and can be exchanged. For devices with an additional TWI interface you can use TWI1.

Remarks

clockspeed | The desired clock frequency for SCL  
---|---  
  
CONFIG TWI will set TWSR pre scaler bits 0 and 1, and TWBR depending on the used [$CRYSTAL](crystal_1.md) frequency and the desired SCL clock speed.

Typical you need a speed of 400 KHz. Some devices will work on 100 KHz as well.

When TWI is used in SLAVE mode, you need to have a faster clock speed as the master.

![notice](notice.jpg)There is no dynamic channel support for I2C

![notice](notice.jpg) To use the hardware I2C routines and not the Software I2C routines you need to use the $lib "i2c_twi.lbx"! (NOT FOR XMEGA/XTINY)

XMEGA

The XMEGA can contain up to 4 TWI units. When not specifying TWIC, TWID, TWIE or TWIF, the TWIC will be used as the default. 

Because the XMEGA can contains multiple TWI busses, a channel identifier MUST be used when addressing TWID,TWIE or TWIF.

This means that your normal I2C code is fully compatible but only with TWIC. Thus omitting the channel identifiers, will automatically use TWIC.

You MUST dimension a variable named TWI_START as a byte. It is used by the xmega TWI library code. Without it, you will get an error.

There are 2 manuals available from ATMEL for every ATXMEGA Chip

1.| One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual  
---|---  
  
2.| Another Manual for the single chips like for example for an ATXMEGA128A1 it is the ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the Alternate Pin Functions. So you can find which Pin on Port C is the SDA and SCL Pin when you want to use the I2C/TWI Interface of this Port.  
---|---  
  
![notice](notice.jpg) It is important that you specify the proper crystal frequency. Otherwise it will result in a wrong TWI clock frequency.

XTINY

The XTINY can contain up to 2 TWI units. 

Because the XTINY can contains multiple TWI busses, a channel identifier MUST be used when addressing TWI1 or up. 

This means that your normal I2C code is fully compatible but only with TWI/TWI0. Thus omitting the channel identifiers, will automatically use TWI0.

You MUST dimension a variable named TWI_START as a byte. It is used by the xtiny TWI library code. Without it, you will get an error.

Some processors support multiple TWI interfaces like the MEGA328PB. Use CONFIG TWI1 to configure the second TWI named TWI1. The first TWI which is named TWI0 is referred to as TWI.

See also

[$CRYSTAL](crystal_1.md) , [OPEN](open.md), [Using the I2C protocol](using_the_i2c_protocol.md), [I2CINIT](i2cinit.md)

Example using Hardware I2C Pin's over Library: i2c_twi.lbx

```vb
'-----------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' This demo shows an example of the TWI  
' Not all AVR chips have TWI (hardware I2C)  
'------------------------------------------------------------------------  
  
'The chip will work in TWI/I2C master mode  
'Connected is a PCF8574A 8-bits port extender  
  
  
$regfile="M8def.dat"' the used chip  
$crystal= 4000000 ' frequency used  
$baud = 19200 ' baud rate  
$hwstack = 40  
$swstack = 30  
$framesize = 40  
  
  
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
Config Scl = Portc.5 ' we need to provide the SCL pin name  
Config Sda = Portc.4 ' we need to provide the SDA pin name  
```
I2cinit ' we need to set the pins in the proper state  
  
```vb
'On the Mega8, On the PCF8574A  
'scl=PC5 , pin 28 pin 14  
'sda=PC4 , pin 27 pin 15  
  
Config Twi = 100000 ' wanted clock frequency when using $lib "i2c_twi.lbx"   
'will set TWBR and TWSR  
'Twbr = 12 'bit rate register  
'Twsr = 0 'pre scaler bits  
  
Dim B As Byte , X As Byte  
Print "TWI master"  
  
Do  
```
Incr B ' increase value  
I2csend &B01110000 , B ' send the value  
Print "Error : " ; Err ' show error status  
I2creceive &B01110000 , X ' get a byte  
```vb
Print X ; " " ; Err ' show error  
Waitms 500 ' wait a bit  
Loop  
End

```
XMEGA SAMPLE

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
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
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
Open "twic" For Binary As #4 ' or use TWID,TWIE oR TWIF  
```vb
Config Twic = 100000 'CONFIG TWI will ENABLE the TWI master interface  
'you can also use TWIC, TWID, TWIE of TWIF  
'!!!!!!!!!!! WITHOUT a channel identifier, TWIC will be used !!!!!!!!!!!!!!  
  

#if Usechannel = 1  
```
I2cinit #4  

#else  
I2cinit  

```vb
#endif  
  
  
Do  
```
I2cstart 'since not # is used, TWIC will be used  
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
I2cwbyte &H71 , #4 'read address  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack , #4  
Print Bin(j) ; " err:" ; Err  
I2cstop #4  

#else  
I2cstart  
I2cwbyte &H71 'read address  
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
I2csend &H70 , 0 , #4 'all 0  

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
XTINY SAMPLE

```vb
'------------------------------------------------------------------  
' (c) 1995-2025 MCS  
' xtiny-TWI-scanner.bas  
'purpose : scan all i2c addresses to find slave chips  
'Micro: tiny816  
'------------------------------------------------------------------  
$regfile = "atxtiny816.dat" ' the used chip  
$crystal = 20000000 ' frequency used  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Config Sysclock = 20mhz , Prescale = 1  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Waitms 3000 'small delay  
Print "XTINY:" ; Hex(rstctrl_rstfr) 'print reset cause  
  
Config Twi0 = 100000 'CONFIG TWI will ENABLE the TWI master interface  
```
I2cinit  
  
```vb
Dim Twi_start As Byte , B As Byte  
Do  
Print "Scan start"  
For B = 0 To 254 Step 2 'for all odd addresses  
```
I2cstart 'send start  
I2cwbyte B 'send address  
```vb
If Err = 0 Then 'we got an ack  
Print "Slave at : " ; B ; " hex : " ; Hex(b) ; " bin : " ; Bin(b)  
End If  
```
I2cstop 'free bus  
```vb
Next  
Print "End Scan"  
Waitms 2000 'some delay and then repeat  
Loop

```