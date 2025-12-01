# I2C Libraries

> I2C/TWI communication protocol

## $FORCESOFTI2C

Action

The $forcesofti2c directive force the ATXMEGA/ATXTINY to use software I2C/TWI Library instead of the hardware I2C registers of ATXMEGA/XTINY.

Syntax

$forcesofti2c 

Remarks

ATXMEGA have usually enough I2C interfaces with fixed SDA and SCL pins but if you want to use other pins as SDA/SCL you can use this directive.

Required Library: $lib "i2c.lbx" 

![notice](notice.jpg)You can not combine the soft mode with the hardware TWI. Thus when using $forcesofti2c, you can not add an additional TWI channel.

```vb
$forcesofti2c ' with this the software I2C/TWI commands are used when inlcuding i2c.lbx  
$lib "i2c.lbx" ' override the normal xmega i2c lib  
  


Then you need to configure the SDA and SCL Pin and initialize the pins:

Config Scl = Port0.1 ' Pin to use as SCL (The hardware pin is Pinb.1)  
Config Sda = Port0.0 ' Pin to use as SDA (The hardware pin is Pinb.0)  
```
I2cinit ' Bring the Pin's in the proper state  


![notice](notice.jpg)It is important that you include the i2c library name after the $forcesofti2c directive. It is also important that you do that early in your code and that you do not use the hardware TWI registers. Thus CONFIG TWI should not be used. 

The variable named Twi_start is not required when using soft TWI/I2C. So you can remove it to see if the right code is used. The Xmega/Xtiny code need this variable and will give error messages when you do not include it. The software implementation does not need it and should not gives error messages when you remove this variable.

See also

[Using the I2C protocol](using_the_i2c_protocol.md)

Example

  
```vb
' Using ATXMEGA with software I2C routines to use also pins which are no hardware SDA/SCL pins  
' Needed Library: $lib "i2c.lbx"  
' The $forcesofti2c directive force the ATXMEGA to use software I2c/TWI Library  
' The hardware for this example is XMEGA-A3BU XPlained board from Atmel  
' Don't forget the pull-ups on SDA/SCL pin !  
' Bascom Version 2.0.7.6 or higher needed  
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
$forcesofti2c ' with this the software I2C/TWI commands are used when inlcuding i2c.lbx  
$lib "i2c.lbx" ' override the normal xmega i2c lib  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Portr.0 = Output  
  
```
Led0 Alias Portr.0 'LED 0 (XMEGA-A3BU XPlained board from Atmel )  
  
Config Portr.1 = Output  
Led1 Alias Portr.1 'LED 1 (XMEGA-A3BU XPlained board from Atmel )  
  
```vb
Dim B As Byte  
'We use here Virtual port 0  
Config Vport0 = B ' map portB to virtual port0  
Config Scl = Port0.1 ' Pin to use as SCL (The hardware pin is Pinb.1)  
Config Sda = Port0.0 ' Pin to use as SDA (The hardware pin is Pinb.0)  
```
I2cinit ' Bring the Pin's in the proper state  
  
```vb
Do  
Waitms 500  
Set Led1  
Reset Led0  
Waitms 500  
Reset Led1  
Set Led0  
```
Incr B  
I2cstart  
I2cwbyte &H24 ' address of I2C Slave  
I2cwbyte B ' databyte to send to slave  
I2cstop  
```vb
Loop  
End 'end program

  


```

---

## CONFIG I2CSLAVE

The I2C Slave Add-on started with a software emulation for TWI slave using an interrupts and timer. It supported a number of early processors.

When TWI was added to some of the processors, an additional TWI slave lib was added to the package.

With Xmega having up to 4 TWI/I2C interfaces, TWI slave support for Xmega has been added to the package in version 2077 build 3

Most tiny processors do not support TWI but USI. USI support is added as well in 2077 build 3.

So the add on comes with a number of I2C slave libraries.

See [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md), [CONFIG TWISLAVE](config_twislave.md) , [CONFIG TWIXSLAVE](config_twixslave.md)

---

## EXTENDED I2C

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

---

## GLCDdSSD1306-I2C

This library is based on work of Ben Zijstra and Heiko/Hkipnik

The library supports the SSD1306 graphical LCD in I2C mode.

Since the display can not read data back, the library supports only the graphical write statements. Commands like LINE, PSET and CIRCLE which need to alter a single pixel are not supported.

XMEGA

For use with XMEGA you need to define 2 constants in your code.

const TWI_ADR = interface

const TWI_CH = num

The interface must point to the TWI control register, this could be : TWIC_CTRL but aldo TWID_CTRL, TWIE_CTRL and TWIF_CTRL

The TWI_CH constant with the value num, must be 1 for TWIC, 2 for TWID, 4 for TWIE and 8 for TWIF

The reference to : $lib "i2c_twi.lbx" must be removed.

Example

```vb
'-------------------------------------------------------------------------------  
' SSD1306-I2C.BAS  
' (c) 1995-2025 MCS Electronics  
' Sample to demo the 128x64 I2C OLED display  
'  
'-------------------------------------------------------------------------------  
$regfile = "m88pdef.dat"  
$hwstack = 32  
$swstack = 32  
$framesize = 32  
$crystal = 8000000  
Config Clockdiv = 1 ' make sure the chip runs at 8 MHz  
  
Config Scl = Portc.5 ' used i2c pins  
Config Sda = Portc.4  
Config Twi = 400000 ' i2c speed  
  
```
I2cinit  
```vb
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
$lib "glcdSSD1306-I2C.lib" ' override the default lib with this special one  
  

#if _build < 20784  
Dim ___lcdrow As Byte , ___lcdcol As Byte ' dim these for older compiler versions  

#endif  
  
Config Graphlcd = Custom , Cols = 128 , Rows = 64 , Lcdname = "SSD1306"  
```
Cls  
Setfont Font8x8tt ' select font  
  
Lcdat 1 , 1 , "BASCOM-AVR"  
Lcdat 2 , 10 , "1995-2020"  
Lcdat 8 , 5 , "MCS Electronics" , 1  
Waitms 3000  
  
Showpic 0 , 0 , Plaatje  
  
```vb
End  
  
  
$include "font8x8TT.font" ' this is a true type font with variable spacing  
  
  
```
Plaatje:  
$bgf "ks108.bgf" ' include the picture data

---

## GLCDEADOGMXL240-7-I2C

This library was sponsored by a customer. 

The library supports the EADOGMXL240-7 in I2C mode.

The library supports all the usual graphical LCD commands.

Example

```vb
'-------------------------------------------------------------------------------  
' eadogxl240-7.bas  
' (c) 1995-2025 MCS Electronics  
' Sample to demo the EADOGXL240-7 LCD in I2C mode  
'  
'-------------------------------------------------------------------------------  
$regfile = "M328pdef.dat" ' the used chip  
$crystal = 8000000 ' frequency used  
$baud = 19200 ' baud rate  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Config Scl = Portc.5 ' we need to provide the SCL pin name  
Config Sda = Portc.4 ' we need to provide the SDA pin name  
  
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
Config Twi = 400000 'speed 400 KHz  
```
I2cinit  
  
```vb
$lib "glcdEADOGMXL240-7-I2C.lib" 'override the default lib with this special one  

#if _build < 2078  
Dim ___lcdrow As Byte , ___lcdcol As Byte  

#endif  
  
Config Graphlcd = Custom , Cols = 240 , Rows = 128 , Lcdname = "EADOGXL240-7"  
  
```
Cls  
  
Setfont Font8x8tt  
  
```vb
'You can use locate but the columns have a range from 1-240  
'When you want to show somthing on the LCD, use the LDAT command  
  
```
Lcdat 1 , 1 , "11111111"  
Lcdat 2 , 1 , "88888888"  
Lcdat 12 , 64 , "MCS Electronics" , 1  
  
Showpic 60 , 0 , Plaatje  
  
Circle(30 , 30) , 20 , 255  
Line(0 , 0) -(239 , 127) , 255 ' diagonal line  
Line(0 , 127) -(239 , 0) , 255 ' diagonal line  
  
```vb
End  
  
$include "font8x8TT.font"  
  
  
```
Plaatje:  
$bgf "ks108.bgf" 'include the picture data

---

## I2C TWI Slave

The I2C-Slave library is intended to create I2C slave chips. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>)

The I2C Slave add on can turn some chips into a I2C slave device. You can start your own chip plant this way.

Most new AVR chips have a so called TWI/I2C interface. As a customer of the I2C slave lib, you can get both libs.

The i2cslave.lib works in interrupt mode and is the best way as it adds less overhead and also less system resources.

With this add-on library you get both libraries:

| i2cslave.lib and i2cslave.lbx : This library is used for AVRâs which have no hardware TWI/I2C interface like for example ATTINY2313 or ATTINY13. In this case TIMER0 and INT0 is used for SDA and SCL (Timer0 Pin = SCL, INT0 Pin = SDA). Only AVR' with TIMER0 and INT0 on the same port can use this library like for example ATTINY2313 or ATTINY13. The i2cslave.lbx is the compiled library version of i2cslave.lib. See also [Config I2CISLAVE](config_i2cslave.md)  
---|---  
  
| i2c_TWI-slave.LBX : This library can be used when an AVR have an TWI/I2C hardware interface like for example ATMEGA8, ATMEGA644P or ATMEGA128. In this case the hardware SDA and SCL pin's of the AVR will be used (with ATMEGA8: SCL is PORTC.5 and SDA is PORTC.4). This library will be used when USERACK = OFF. When USERACK =ON then i2c_TWI-slave-acknack.LBX will be used. See also [Config TWISLAVE](config_twislave.md)  
---|---  
  
See also: [Using the I2C protocol](using_the_i2c_protocol.md)

---

## I2C-TWI



---

## I2C_MULTIBUS

While XMEGA supports multiple TWI busses, the normal AVR only supports on TWI or no I2C bus. The I2C_MULTIBUS library supports up to 16 I2C busses.

See [CONFIG I2CBUS](config_i2cbus.md)

---

## I2C_TWI

I2C Software vs. Hardware Routines

By default BASCOM will use software routines when you use I2C statements. This because when the first AVR chips were introduced, there was no TWI yet. Atmel named it TWI because Philips is the inventor of I2C. But TWI is the same as I2C. This I2C/TWI peripheral performs all the tasks in hardware so less code is required. But it is limited to the designated pins for SCL and SDA.

So BASCOM allows you to use I2C on every AVR chip. Most newer AVR chips have build in hardware support for I2C. With the I2C_TWI lib you can use the TWI which has advantages as it require less code.

To force BASCOM to use the TWI, you need to insert the following statement into your code:

$LIB "I2C_TWI.LBX"

You also need to choose the correct SCL and SDA pins with the CONFIG SCL and CONFIG SDA statements.

The TWI will save code but the disadvantage is that you can only use the fixed SCL and SDA pins.

For XMEGA the default is using the hardware TWI. You can force bascom to use the software solution using [$FORCESOFTI2C](forcesofti2c.md)

![notice](notice.jpg)You should not reference the I2C_TWI in Xmega or Xtiny ! Xmega and Xtiny use a different TWI interface.

See also: [Using the I2C protocol](using_the_i2c_protocol.md), [CONFIG TWI](config_twi.md) , [I2CV2](i2cv2.md)

---

## I2C_TWI-MULTI

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

---

## I2C_USI

The I2C_USI library is an alternative I2C master library. It is intended to be used with processors that have an USI interface.

Using the hardware is better since it will use less processor resources. 

```vb
If a processor has TWI, use the TWI

If a processors has USI, use the USI

If a processor has no hardware I2C, use the default built in software routines. 

```
To use the USI in master mode, use [CONFIG USI](config_usi.md).

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

---

## I2C_USI_SLAVE

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

---

## I2CINIT

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

---

## I2CRECEIVE

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

---

## I2CSEND

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

---

## I2CV2

I2C Software

By default BASCOM will use software routines when you use I2C statements. This because when the first AVR chips were introduced, there was no TWI interface. Atmel named it TWI because Philips is the inventor of I2C. But TWI is the same as I2C.

When your processor has a TWI interface you can best use this TWI interface. 

By default the software master i2c routines use the library named i2c.lib. This library does not maintain a clock/data state so when i2cstart or i2cstop is generated, the clock and data lines need to be set to the proper state before the start/stop condition can be generated. This can result in small glitches. Most slave chips will not notice them but some do.

For this purpose the i2c master library has been rewritten so that clock and data have a known state/level at all times. This allows to create glitch free clock/data.

To use this library use the $LIB directive : $LIB "I2CV2.LIB"

This will make the compiler use this library. One thing to be aware of : a repeated start can only be created by using the [I2CREPSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) statement. 

This is a difference with the default i2c.lib

When you want to use soft I2C on an XTINY or XMEGA you need to use the [$FORCESOFTI2C](forcesofti2c.md) directive.

Example

```vb
$forcesofti2c ' force soft i2c

$lib "i2cv2.lib" ' use this one

```
See also: [Using the I2C protocol](using_the_i2c_protocol.md), [CONFIG TWI](config_twi.md) , [I2CV2](i2cv2.md)

---

## I2START,I2CSTOP, I2CRBYTE, I2CWBYTE, I2CREPSTART

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

---

## LCD_DOGS104a_I2C

This is a user contributed lbx for the EADOGS104 with the SSD1803A.

The SAMPLES\LCDGRAPH folder contains the sample :

```vb
'--------------------------------------------------------------  
' DOGS-104.bas  
' Demonstration for DOGS 104-A display  
' (c) R. Müller-Westermann  
' HB9EFQ@yahoo.com  
'--------------------------------------------------------------  
  
$regfile = "m168def.dat"  
$crystal = 1000000  
'$sim  
  
$hwstack = 32  
$swstack = 32  
$framesize = 64  
  
$lib "Lcd_dogs104a_i2c.lbx"  
  
  
'LCD -----------------------------------------------------------------  
'chipset:DOGS104V3  
'DOGS104 Display can use either &H78 if pin SA0 of module is set to GND  
'or &H7A if SA0 of module is set to VDD for I²C communication.  
'Pullup resistors on SDA and SCL lines of less or equal to 3.9kOhm @3.3V  
'are recommended.  
  
```
Const Dogs104_adr_w = &H78 'I²C write address  
Const Dogs104_adr_r = &H79 'I²C read address  
  
  
```vb
'LCD has 2 view options. If LCD_view is set to 0 characters are being  
'displayed in bottom view (6 o'clock). If set to 1 characters are being  
'displayed in top view (12 0'clock)  
```
Const Lcd_view = 0 'bottom view  
```vb
'Const Lcd_view = 1 'top View  
  
  
'configuration is needed for defining start address of LCD RAM  
Config Lcd = 20x2  
  
  
'LCD comes with 3 different character sets. These can be accessed by setting  
'LCD_ROM  
```
Const Lcd_rom = 1 'ROM A  
```vb
'Const Lcd_rom = 2 'ROM B  
'Const Lcd_rom = 3 'ROM C  
  
  
'there are 2 custom procedures witch provide number of lines switching at  
'runtime. You can either choose 2 line mode with double hight fonts or regular  
'4 line mode. This is the standard mode used by Initlcd.  
$external 2line_mode  
$external 4line_mode  
  
'LCD -----------------------------------------------------------------  
  
Declare Sub 2line_mode  
Declare Sub 4line_mode  
  
'TWI-------------------------------------------------------------------  
Config Scl = Portc.5  
Config Sda = Portc.4  
```
I2cinit  
'TWI-------------------------------------------------------------------  
  
  
Initlcd  
```vb
Waitms 100  
  
'As with any other LCD module, you can define up to 8 additional characters  
'by using the regular Bascom command  
  
'-----------------------------------------------------------------  
```
Deflcdchar 1 , 32 , 32 , 4 , 10 , 17 , 10 , 4 , 32 ' circle  
'-----------------------------------------------------------------  
  
Cls  
  
Waitms 100  
  
Cursor Off  
  
Locate 1 , 1 : Lcd Chr(1)  
  
```vb
Wait 2  
  
'standard initialization of LCD is set to 4 line mode  
  
```
Cls  
  
Locate 1 , 1 : Lcd "line 1"  
Locate 2 , 1 : Lcd "line 2"  
Locate 3 , 1 : Lcd "line 3"  
Locate 4 , 1 : Lcd "line 4"  
  
```vb
Wait 2  
  
'-----------------------------------  
  
```
Cls  
  
'if needed LCD can be switched to 2 line mode  
2line_mode  
  
Locate 1 , 3 : Lcd "line 1"  
Locate 2 , 3 : Lcd "line 2"  
  
```vb
Wait 2  
  
' ... and back to 4 line mode  
  
```
4line_mode  
  
Cls  
  
Locate 1 , 3 : Lcd "line 1 "  
Locate 2 , 3 : Lcd "line 2"  
Locate 3 , 3 : Lcd "line 3"  
Locate 4 , 3 : Lcd "line 4"  
  
```vb
Wait 2  
  
'if desired you can put the LCD module in power down mode. This saves some  
'400µA.  
'Any other command applicable for DOGS104A using SSD1803A controller can be  
'issued by using regular Rcall _Lcd_control command with preloaded  
'R24 register.  
  
```
Display Off  
```vb
Waitms 100  
  
'power down ----------------  
  
```
R24 = &B00111010 '8 bit data RE1, REV0  
Lcdcmd R24  
  
  
  
R24 = &B00000011 'power down  
Lcdcmd R24  
  
R24 = &B00111000 '8 bit data RE0, IS0  
Lcdcmd R24  
  
```vb
'power down ----------------  
  
Wait 2  
  
'... and power up again. LCD RAM remains unchanged.  
  
'power up -----------------  
  
```
R24 = &B00111010 '8 bit data RE1, REV0  
Lcdcmd R24  
  
R24 = &B00000010 'power up  
Lcdcmd R24  
  
R24 = &B00111000 '8 bit data RE0, IS0  
Lcdcmd R24  
  
```vb
'power up -----------------  
  
Waitms 100  
```
Display On  
  
Locate 4 , 1 : Lcd "powered up"  
End

---

## LCD_I2C_PCF8574

The LCD_I2C_PCF8574 library is made by O-Family. This library supports multiple LCD.

The library is based on an old library from Kent Andersson. The old lib used bascom code but for best performance should use ASM.

O-Family made this possible. He also extended the lib so multiple LCD can be used.

The LCD are normal text LCD. Unlike graphical LCD, TEXT LCD have a kind of standard. 

So most text LCD would be usable. The important part is that an I2C port extended chip is used : the PCF8574.

The PCF8574 also has a brother/sister : an identical chip with the A suffix. The only difference is that it has a different base address.

Normally an LCD is operated in 4 bit or 8 bit parallel pin mode. The PCF chip is connected to the LCD data and control lines. And the driver sends the proper I2C commands to control the LCD. This way you can use I2C which is great since it can be used of a greater distance. 

XMEGA

For use with XMEGA you need to define 2 constants in your code.

const TWI_ADR = interface

const TWI_CH = num

The interface must point to the TWI control register, this could be : TWIC_CTRL but aldo TWID_CTRL, TWIE_CTRL and TWIF_CTRL

The TWI_CH constant with the value num, must be 1 for TWIC, 2 for TWID, 4 for TWIE and 8 for TWIF

![text_lcd_o-family](text_lcd_o-family.png)

The circuit above show how to connect things. Converter boards exist that can be soldered right to the LCD.

But you can also wire this yourself.

The A0-A1-A2 select the address of the PCF chip.

More info in the [forum](<fourthline.htm> "https://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=viewtopic&p=80311#80311").

Two samples you can find in the SAMPLES\LCDTEXT folder

SAMPLE

```vb
$programmer = 22 'ARDUINO (using stk500v1 protocol)  
'  
' *************************************  
' * PCF8574 I2C LCD Adapter test *  
' * For multiple LCDs 2021/ 3/24 *  
' *************************************  
'  
$regfile = "m328pdef.dat" 'Set the AVR to use.  
$crystal = 16000000 'Set the AVR clock.  
'  
$hwstack = 64 'Set the capacity of the hardware stack.  
$swstack = 10 'Set the capacity of the software stack.  
$framesize = 24 'Set the capacity of the frame area.  
'  
' * PCF8574 I2C LCD Adapter settings *  
'  
```
Const I2c_select = 1 '0:Software I2C , 1:TWI  

```vb
#if I2c_select = 0  
'------[For software I2C]------  
Config I2cdelay = 10 'SCL clock frequency = approx. 42KHz. (At AVR clock 16MHz) (* Maximum 100KHz)  
Config Scl = Portd.2 'Set the port pin to connect the SCL line of the I2C bus.  
Config Sda = Portd.3 'Set the port pin to connect the SDA line of the I2C bus.  
```
I2cinit 'Initialize the SCL and SDA lines of the I2C bus.  
```vb
'-------------------------------  

#else  
'------[For TWI]------------------  
$lib "i2c_twi.lib" 'Incorporate the hardware I2C/TWI library.  
Config Twi = 100000 'I2C bus clock = 100KHz  
Config Scl = Portc.5 'You must specify the SCL pin name.  
Config Sda = Portc.4 'You must specify the SDA pin name.  
```
I2cinit 'Initialize the SCL and SDA lines of the I2C bus.  
```vb
'-------------------------------  

#endif  
Dim Pcf8574_lcd As Byte : Pcf8574_lcd = &H4E 'PCF8574 slave address. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Dim Backlight As Byte : Backlight = 1 'LCD backlight control. (0: off, 1: on)  
$lib "lcd_i2c_PCF8574.LIB" 'Incorporate the library of I2C LCD PCF8574 Adapter.  
Config Lcd = 20x4 'Set the LCD to 20 characters and 4 lines.  
```
Initlcd 'Initialize the LCD.  
```vb
'  
' * When installing the second and subsequent LCDs *  
'  
```
Pcf8574_lcd = &H4C 'The slave address of the second PCF8574. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Initlcd 'Initialize the second LCD.  
'  
Pcf8574_lcd = &H4A 'The slave address of the third PCF8574. (&H40,&H42,&H44,&H46,&H48,&H4A,&H4C,&H4E)  
Initlcd 'Initialize the third LCD.  
  
```vb
'  
' ****************  
' * Display test *  
' ****************  
'  
```
Pcf8574_lcd = &H4E 'Specify the first LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 2  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 2 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 15 'Display custom characters.  
Lcd Chr(2) ; "1"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
```vb
'  
' * Second LCD *  
'  
```
Pcf8574_lcd = &H4C 'Specify the second LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 2  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 3 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 15 'Display custom characters.  
Lcd Chr(3) ; "2"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
```vb
'  
' * Third LCD *  
'  
```
Pcf8574_lcd = &H4A 'Specify the third LCD.  
'  
Locate 1 , 1 'Display of title.  
Lcd "PCF8574"  
'  
Locate 2 , 4  
Lcd "I2C LCD Adapter"  
'  
Deflcdchar 4 , &H02 , &H04 , &H0C , &H1E , &H0F , &H06 , &H04 , &H08 'Write the custom character [Lightning] to the LCD.  
Locate 1 , 19 'Display custom characters.  
Lcd Chr(4) ; "3"  
'  
Locate 1 , 9 'Display the slave address of PCF8574.  
Lcd "[" ; Hex(pcf8574_lcd) ; "]"  
'  
Locate 3 , 3  
Lcd "-- 3rd Line --"  
'  
Locate 4 , 4  
Lcd "20x4 Display "  
'  
Locate 4 , 20 'Display the cursor.  
Cursor On , Blink  
End

---

## Options Compiler I2C, SPI, 1WIRE

![options_compiler_i2c](options_compiler_i2c.png)

Options Compiler I2C, SPI, 1WIRE

Item | Description  
---|---  
SCL port | Select the port pin that serves as the SCL-line for the I2C related statements.  
SDA port | Select the port pin that serves as the SDA-line for the I2C related statements.  
1WIRE | Select the port pin that serves as the 1WIRE-line for the 1Wire related statements.  
Clock | Select the port pin that serves as the clock-line for the SPI related statements.  
MOSI | Select the port pin that serves as the MOSI-line for the SPI related statements.  
MISO | Select the port pin that serves as the MISO-line for the SPI related statements.  
SS | Select the port pin that serves as the SS-line for the SPI related statements.  
Use hardware SPI | Select to use built-in hardware for SPI, otherwise software emulation of SPI will be used. The 2313 does not have internal HW SPI so it can only be used with software SPI mode. When you do use hardware SPI, the above settings are not used anymore since the SPI pins are dedicated pins and can not be chosen by the user.  
  
It is advised to use the various [CONFIG](config.md) commands in your source code. It make more clear in the source code which pins are used.

---

## Using the I2C protocol

IÂ²C bus

IÂ²C bus is an abbreviation for Inter Integrated Circuit bus or "I-Squared-C".

Some manufacturer call it TWI (Two-Wire-Interface) which is technically the same as I2C.

There is also SMBus. The I²C bus and the SMBusâ¢ are essentially compatible with each other. Normally devices, both masters and slaves, are freely interchangeable between both buses. Both buses feature addressable slaves (although specific address allocations can vary between the two).

The buses operate at the same speed, up to 100kHz, but the I²C bus has both 400kHz and 2MHz

versions. Complete compatibility between I2C and SMBus is ensured only below 100kHz.

IÂ²C is a serial and synchronous bus protocol. In standard applications hardware and timing are often the same. The way data is treated on the IÂ²C bus is to be defined by the manufacturer of the IÂ²C master and slave chips.

In a simple IÂ²C system there can only be one master, but multiple slaves. The difference between master and slave is that the master generates the clock pulse. The master also defines when communication should occur. For bus timing it is important that the slowest slave should still be able to follow the masterâs clock. 

In other words the bus should be as fast as the slowest slave.

A typical hardware configuration is shown in the figure below:

![i2cbus](i2cbus.jpg)

Note that more slave chips can be connected to the SDA and SCL lines, normally Rp has a value of 1kOHM. 

The clock generated by the master is called Serial Clock (SCL) and the data is called Serial Data (SDA).

![notice](notice.jpg) Always check if the pull-up resistors are connected !

In most applications the micro controller is the IÂ²C Master. Slave chips can be Real Time Clocks and Temperature sensors. For example the DS1307 and the DS1624 from <http://www.maximintegrated.com> . 

Of course you can also create your own I2C slaves by programming an ATTINY or ATMEGA . See [CONFIG I2CSLAVE](config_i2cslave.md)

In that case there is AVR Master to AVR Slave communication.

LOGIC BUS LEVELS AND CONDITIONS

![i2c_level](i2c_level.jpg)

Data can only occur after the master generates a start condition. A start condition is a high-to-low transition of

the SDA line while SCL remains high. After each data transfer a stop condition is generated. A stop condition is a low-to-high transition of the SDA line while SCL remains high.

![i2c_transfer](i2c_transfer.jpg)

As said a data transfer can occur after a start condition of the master. The length of data sent over IÂ²C is always 8 bit this includes a read/write direction bit, so you can effectively send 7 bits every time.

The most significant bit MSB is always passed first on the bus.

If the master writes to the bus the R/W bit = 0 and if the master reads the R/W bit = 1.

After the R/W bit the master should generate one clock period for an acknowledgement ACK.

Each receiving chip that is addressed is obliged to generate an acknowledge after the reception of each byte. A chip that acknowledges must pull down the SDA line during the acknowledge clock pulse in such a way that the SDA line is stable LOW during the HIGH period of the acknowledge related clock pulse.

After an acknowledge there can be a stop condition, if the master wishes to leave the bus idle. Or a repeated start condition. A repeated start is the same as a start condition.

When the master reads from a slave it should acknowledge after each byte received. There are two reasons for the master not to acknowledge. The master sends a not acknowledge if data was not received correctly or if the master wishes the stop receiving.

In other words if the master wishes to stop receiving, it sends a not acknowledge after the last received byte.

The master can stop any communication on the bus at any time by sending a stop condition.

BUS ADRESSING

Letâs say we have a slave chip with the address &B1101000 and that the master wishes to write to that slave, the slave would then be in receiver mode, like this:

![i2c_write](i2c_write.jpg)

You can see here that the master always generates the start condition, then the master sends the address of the slave and a â0â for R/W. After that the master sends a command or word address. The function of that command or word address can be found in the data sheet of the slave addressed.

After that the master can send the data desired and stop the transfer with a stop condition.

![i2c_read](i2c_read.jpg)

Again the start condition and the slave address, only this time the master sends â1â for the R/W bit. The slave can then begin to send after the acknowledge. If the master wishes to stop receiving it should send a not acknowledge.

OVERVIEW of Routines

Config Sda = Portx.x

Configures a port pin for use as serial data SDA.

Config Scl = Portx.x

Configures a port pin for use as serial clock SCL.

I2cinit

Initializes the SCL and SDA pins.

I2cstart

Sends the start condition.

I2cstop

Sends the stop condition.

I2cwbyte

Writes one byte to an IÂ²Cslave.

I2crbyte

Reads one byte from an IÂ²Cslave.

I2csend

Writes a number of bytes to an IÂ²Cslave.

I2creceive

Reads a number of bytes from an IÂ²Cslave.

I2C write and read:

A typical I2C write to send one byte of data looks like this:

I2cstart  
I2cwbyte I2c_address_of_slave  
I2cwbyte Byte_to_send  
I2cstop

(I2cstart generates the start condition on the I2C bus were all devices are listen to. After this we send the Slave address of the device we want to send a byte to. The I2C slave with this address will send out a Ack where all other do nothing. Now you can start to send a byte (or more bytes) to this Slave address. After this an I2cstop release the bus.)

A typical I2C read to read one byte of data looks like this:

I2cstart  
I2cwbyte I2c_address_of_slave  
I2crbyte Databyte_to_read , Nack  
I2cstop

(Nack indicates that the master do not want to read more bytes)

A typical I2C read to read one byte of data looks like this:

  
I2cstart  
I2cwbyte I2c_address_of_slave  
I2crbyte Databyte_to_read , Ack  
I2crbyte Databyte_to_read , Nack  
I2cstop  


(Ack indicates that the master want to read more bytes from the slave and with the last byte to read the master indicate this with Nack)

I2C Software vs. Hardware Routines

By default BASCOM will use software routines when you use I2C statements. This because when the first AVR chips were introduced, there was no TWI yet. Atmel named it TWI because Philips is the inventor of I2C. But TWI is the same as I2C.

So BASCOM allows you to use I2C on every AVR chip. Most newer AVR chips have build in hardware support for I2C. With the [I2C_TWI](i2c_twi.md) lib you can use the hardware TWI which has advantages since it require less code.

To force BASCOM to use the hardware TWI, you need to insert the following statement into your code:

$LIB "I2C_TWI.LBX"

You also need to choose the correct SCL and SDA pins with the CONFIG SCL and CONFIG SDA statements.

The TWI will save code but the disadvantage is that you can only use the fixed SCL and SDA pins.

![notice](notice.jpg)You only should include this library for a normal(older) AVR processor. Like Mega88. Do not include for Xmega, Xtiny, MegaX or AVRX.

XMEGA

When using XMEGA, there is a difference : here you are supposed to use the hardware TWI. So that is a default. The reason is that Xmega has up to 4 different TWI-buses. There is no need to include a library. The only requirement is that you dimension a byte : Dim Twi_start As Byte

To force to the software solution, use [$FORCESOFTI2C](forcesofti2c.md)

XTINY/MEGAX/AVRX

These are all new AVR processors. The have a similar architecture as Xmega. For this reason, you are supposed to use the TWI hardware.

There is no need to include a library. The only requirement is that you dimension a byte : Dim Twi_start As Byte

See also: 

[Using USI (Universal Serial Interface)](using_usi_universal_serial_int.md), [Config TWI](config_twi.md), [CONFIG TWISLAVE](config_twislave.md), [I2C_TWI](i2c_twi.md), [$FORCESOFTI2C](forcesofti2c.md)

[I2CSEND](i2csend.md) , [I2CSTART](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CSTOP](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CRBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md) , [I2C_TWI Library for using TWI](i2c_twi.md)

EXAMPLE with Software Routines

This example shows you how to setup and read the temperature from a DS1624 temperature sensor.

Connect the DS1624 like this:

![i2c_proto_sample](i2c_proto_sample.jpg)

```vb
Then program this sample into your micro controller and connect your micro controller to the serial port of your PC.

$regfile = "m88def.dat" 'Define the chip you use  
$crystal = 8000000 'Define speed  
$hwstack = 40  
$swstack = 30  
$framesize = 40  
  
$baud = 19200 'Define UART BAUD rate  
  
  
' Declare RAM for temperature storage  
Dim I2ctemp As Byte 'Storage for the temperature  
  
' We use here the software emulated I2C routines  
' Configure pins we want to use for the I²C bus  
Config Scl = Portd.1 'Is serial clock SCL  
Config Sda = Portd.3 'Is serial data SDA  
```
I2cinit  
  
  
' Declare constants - I2C chip addresses  
Const Ds1624wr = &B10010000 'DS1624 Sensor write  
Const Ds1624rd = &B10010001 'DS1624 Sensor read  
  
' This section initializes the DS1624  
I2cstart 'Sends start condition  
I2cwbyte Ds1624wr 'Sends the address  
  
```vb
'byte with r/w 0  
  
'Access the CONFIG register (&HAC address byte)  
```
I2cwbyte &HAC  
'Set continuous conversion (&H00 command byte)  
I2cwbyte &H00  
I2cstop 'Sends stop condition  
Waitms 25 'We have to wait some time after a stop  
  
I2cstart  
I2cwbyte Ds1624wr  
'Start conversion (&HEE command byte)  
I2cwbyte &HEE  
I2cstop  
```vb
Waitms 25  
'End of initialization  
  
Print 'Print empty line  
  
  
Do  
  
'Get the current temperature  
```
I2cstart  
I2cwbyte Ds1624wr  
I2cwbyte &HAA 'Read temperature (&HAA command byte)  
I2cstart  
I2cwbyte Ds1624rd 'The chip will give register contents  
'Temperature is stored as 12,5 but the ,5 first  
I2crbyte I2ctemp , Ack  
'So you'll have to read twice... first the ,5  
I2crbyte I2ctemp , Nack  
'And then the 12... we don't store the ,5  
I2cstop  
```vb
'That's why we read twice.  
  
'We give NACK if the last byte is read  
  
'Finally we print  
Print "Temperature: " ; Str(i2ctemp) ; " degrees" ; Chr(13);  
  
Waitms 25  
  
Loop  
End

```
You should be able to read the temperature in your terminal emulator.

Note that the used command bytes in this example can be found in DS1624 temperature sensor data sheet.

Example which use I2C Master hardware in AVR

See here: [CONFIG TWI](config_twi.md)

I2C Practice (Tips&Tricks)

The design below shows how to implement an I2C-bus. The circuit is using a Mega88 as a master.

The TWI bus is used. While you can use any pin for software mode I2C, when a micro has TWI hardware build in, it is advised to use the TWI hardware.

R1 and R2 are 4K7 pull up resistors.

There are many I2C slave chips available. The example shows the PCF8574. With the additional TWI slave library you can make your own slave chips.

![i2_hw](i2_hw.zoom76.png)

How to calculate Pull Up Resistor 

The maximum of bus capacitance is 400pF (which is independent of bus speed 100KHz or 400KHz).

Here is a good article which describe how to calculate the Pull Up Resistor:

<http://www.edn.com/design/analog/4371297/Design-calculations-for-robust-I2C-communications>

Using AVR interal pull-up resistor (with Hardware Routines)

It is recommended to use external pull-up resistors !

For testing you could use also the AVR interal pull-up resistors

See example where Portc.4 and Portc.5 is SDA and SCL (the pull-up needs to be set after i2cinit):

i2cinit  
Portc.4 = 1  
Portc.5 = 1  


Active Termination of I2C

The following information was submitted by Detlef Queck:

Many people have problems over and over with I2C(TWI) Termination. Use 4,7k or 10 k pull up? How long can the SCL, SDA line be when used with pull ups etc, etc.

You can simplify this confusing problem. Here is a Schematic for an active Termination of I2C and TWI. We have used this Schematic for over 10 years, and have had no problems with it. The I2C (TWI) lines can be up to 80cm (400KHz) without any problem when the Terminator is at the end of the lines.

![i2c_detlef](i2c_detlef.gif)

How to handle longer cable length between I2C Master and Slaves or Multi-drop Configurations

The I2C-bus capacitance limit of 400 pF restricts practical communication distances. You can extend the use of the I2C in systems

with more devices and / or longer bus lengths with P82B715 or P82B96.

P82B96

•| Isolates capacitance allowing 400 pF on Sx/Sy side and 4000 pF on Tx/Ty side  
---|---  
  
•| 400 kHz operation over at least 20 meters of wire (see AN10148)  
---|---  
  
•| Create Multi-drop configurations  
---|---  
  
•| Supply voltage range of 2 V to 15 V with I2C-bus logic levels on Sx/Sy side independent of supply voltage  
---|---  
  
•| Splits I2C-bus signal into pairs of forward/reverse Tx/Rx, Ty/Ry signals for interface with opto-electrical isolators and similar devices that need unidirectional input and output signal paths.  
---|---  
  
P82B715

•| Increase the total connected capacitance of an I2C-bus system to around 3000 pF and drive signals over long cables to approximately 50m  
---|---  
  
•| Multi-drop distribution of I2C-bus signals using low cost twisted-pair cables  
---|---  
  
I2C Multiplexing, Switch and Voltage Level translation between different I2C busses

Some specialized devices only have one I2C or SMBus address and sometimes several identical devices are needed in the same system. The multiplexers and switches split the I2C bus into several sub-branches and allow the I2C master to select and address one of multiple identical devices, in order to resolve address conflict issues. An example is PCA9544A or PCA9546A (which also llows voltage level translation between 1.8 V, 2.5 V, 3.3 V and 5 V buses).

Your I2C (TWI) connection is not working (Tips&Tricks):

Checklist:

\- Is the configured I2C clock frequency matching the frequency of the connected chip

\- Check if you have pull-up resistors on SDA and SCL (and if the pull-up resistors are working)

\- Do you have the right SDA and SCL pins conected ?

\- connect also GND to have the same potential

\- You can use the Err variable to check which I2C function is not working. When an error occurs, the internal ERR variable will return 1. Otherwise it will be set to 0.

\- How about the voltage levels on both chips (do not connect 3.3V systems to 5V systems without voltage adapter)

\- Is the system you are connecting the I2C to using a 7 Bit address or 8 Bit address (8-bit addresses include the read/write bit) ?

```vb
Then you can try with shift left:

' you can simply do this; &HC4 is an example address  
```
const someI2caddress= &H4C * 2  
' this would shift the address to the left.

\- It is important that you specify the proper crystal frequency. Otherwise it will result in a wrong TWI clock frequency

\- With following lib you do not use the software emulated TWI (I2C). You use the hardware I2C (for the AVR's that have an hardware I2C)

$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI

\- By default BASCOM will use software routines for I2C.

\- Do you have the right I2C read address ?

Here an example I2C write address which Bascom expects:

&B01000000 = &H40

Read address would be for this example:

&b01000001 = &h41

\- In case of using TWI (I2C) Slave: Are you using the right library for your used chip ?

With the I2C TWI Slave add-on library you get both libraries:

| i2cslave.lib and i2cslave.lbx : This library is used for AVRâs which have no hardware TWI/I2C interface like for example ATTINY2313 or ATTINY13. In this case TIMER0 and INT0 is used for SDA and SCL (Timer0 Pin = SCL, INT0 Pin = SDA). Only AVR' with TIMER0 and INT0 on the same port can use this library like for example ATTINY2313 or ATTINY13. The i2cslave.lib file contains the ASM source. The i2cslave.lbx file contains the compiled ASM source. See CONFIG I2CSLAVE below.  
---|---  
  
| i2c_TWI-slave.LBX : This library can be used when an AVR have an TWI/I2C hardware interface like for example ATMEGA8, ATMEGA644P or ATMEGA128. In this case the hardware SDA and SCL pin's of the AVR will be used (with ATMEGA8: SCL is PORTC.5 and SDA is PORTC.4). This library will be used when USERACK = OFF. When USERACK =ON then i2c_TWI-slave-acknack.LBX will be used. See also [Config TWISLAVE](config_twislave.md)  
---|---  
  
Operation at 400 kHz

Fast- mode devices can only be operated at 400 kHz clock frequency if no standard-mode devices (100KHz) are on the bus.

You can use an I2C Scanner to find I2C devices:

You basically use the Err variable. When an error occurs, the internal ERR variable will return 1. Otherwise it will be set to 0.

So 0 means we have found a I2C Slave with that address.

```vb
'------------------------------------------------------------------  
' (c) 1995-2025 MCS  
' i2cscan.bas  
'purpose : scan all i2c addresses to find slave chips  
'use this sample in combination with twi-slave.bas  
'Micro: Mega88  
'------------------------------------------------------------------  
$regfile = "M88def.dat" ' the used chip  
$crystal = 8000000 ' frequency used  
$baud = 19200 ' baud rate  
$hwstack = 40  
$swstack = 30  
$framesize = 40  
  
Dim B As Byte  
  
'we use the TWI pins of the Mega88  
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
  
  
Config Scl = Portc.5 ' we need to provide the SCL pin name  
Config Sda = Portc.4 ' we need to provide the SDA pin name  
```
I2cinit  
```vb
Config Twi = 100000 ' wanted clock frequency when using $lib "i2c_twi.lbx"  
'will set TWBR and TWSR  
'Twbr = 12 'bit rate register  
'Twsr = 0 'pre scaler bits  
  
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
End

```
I2C Slave Library

See [I2C TWI Slave](i2ctwislave.md)

I2C Slave LIB - how to Send/Receive more than 1 Byte for chips that do not have hardware I2C ?

Using following config:

Config I2cslave = &H34 , Int = Int0 , Timer = Timer0

When you want to receive/send multiple bytes, you need to keep track of them.

You can do this with a byte counter. this counter you would need to reset when the slave is addressed.

To do this the lib need to be altered:

\- open i2cslave.lib with notepad

\- look for label : I2c_adr_ack:

Then add this line :

rcall i2c_master_addressed

-then save and add this label to your code:

I2c_master_addressed:  
Br = 0 'clear the byte counter  
Bw = 0  
return

in your code where the bytes are passed you can increase them.

The BR you increase when a byte is read, the BW you increase when a byte is passed.

for example: 

I2c_master_has_data:  
Incr Bw  
Myarray(bw) = _a1  
Return

Using ATXMEGA I2C with Software Routines (then you can choose the SDA and SCL Pins)

ATXMEGA have usually enough I2C interfaces. But nevertheless there is a possibility to use the I2C software routines and you can use any

Pin you want as SDA and SCL.

Following the ATXMEGA Master and below the ATMEGA328P I2C Slave which was tested with the ATXMEGA Master in I2C Software Mode:

  


Master

  
```vb
' Using ATXMEGA with software I2C routines to use also pins which are no hardware SDA/SCL pins  
' Needed Library: $lib "i2c.lbx"  
' The $forcesofti2c directive force the ATXMEGA to use software I2c/TWI Library  
  
' The hardware for this example is XMEGA-A3BU XPlained board from Atmel  
' Don't forget the pull-ups on SDA/SCL pin !  
' Bascom Version 2.0.7.6 or higher needed  
  
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
$forcesofti2c ' with this the software I2C/TWI commands are used when inlcuding i2c.lbx  
$lib "i2c.lbx" ' override the normal xmega i2c lib  
  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
  
Config Portr.0 = Output  
```
Led0 Alias Portr.0 'LED 0 (XMEGA-A3BU XPlained board from Atmel )  
  
Config Portr.1 = Output  
Led1 Alias Portr.1 'LED 1 (XMEGA-A3BU XPlained board from Atmel )  
  
  
```vb
Dim B As Byte  
  
'We use here Virtual port 0  
Config Vport0 = B ' 'map portB to virtual port0  
  
Config Scl = Port0 .1 ' Pin to use as SCL (The hardware pin is Pinb.1)  
Config Sda = Port0 .0 ' Pin to use as SDA (The hardware pin is Pinb.0)  
```
I2cinit ' Bring the Pin's in the proper state  
  
  
```vb
Do  
  
  
Waitms 500  
Set Led1  
Reset Led0  
Waitms 500  
Reset Led1  
Set Led0  
  
```
Incr B  
  
I2cstart  
I2cwbyte &H24 ' address of I2C Slave  
I2cwbyte B ' databyte to send to slave  
I2cstop  
  
```vb
Loop  
  
End 'end program  


```
Slave (for ATXMEGA using Soft I2C Master)

  
  
```vb
' I2C Slave Example for using with ATXMEGA  
' ATMEGA328P running @ 3.3 Volt !  
  
  
' Terminal output of this example when used with XMEGA_ise_soft_i2c.bas:  
  
'(  
  
```
ATXMEGA using Software TWI/I2C <\------> ATMEGA 328P Bascom-AVR @ 3.3V...  
>>> 180  
>>> 181  
>>> 182  
>>> 183  
>>> 184  
>>> 185  
>>> 186  
>>> 187  
>>> 188  
>>> 189  
>>> 190  
>>> 191  
  
  
```vb
')  
  
$regfile = "m328pdef.dat"  
$crystal = 12e6 '16MHz  
$hwstack = 80  
$swstack = 80  
$framesize = 160  
  
  
'CONFIG TWI SLAVE  
Config Twislave = &H24 , Btr = 1 , Bitrate = 100000 , Gencall = 1  
' With the CONFIG BTR, you specify how many bytes the master will read.  
  
  
Dim Receive As Byte  
Dim S As Byte  
  
Enable Interrupts  
  
  
Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
Wait 3  
  
Print  
Print "ATXMEGA using Software TWI/I2C <\------> ATMEGA 328P Bascom-AVR @ 3.3V..."  
  
Do  
```
nop  
```vb
Loop  
  
End 'end program  
  
'--------------------------------I2C--------------------------------------------  
  
'Master sent stop or repeated start  
```
Twi_stop_rstart_received:  
  
```vb
Return  
  
'We were addressed and master will send data  
```
Twi_addressed_goread:  
  
```vb
Return  
  
  
'We were addressed and master will read data  
```
Twi_addressed_gowrite:  
  
```vb
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWI holds the received value  
'Twi_btw is the BYTE NUMBER  
```
Twi_gotdata:  
Receive = Twi 'lesen  
```vb
Print ">>> " ; Twi 'Print what we have received (ONLY FOR TESTING)  
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twi_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twi_btr can be used for the index  
'twi_btr is the BYTE NUMBER  
```
Twi_master_needs_byte:  
  
```vb
Return  
  
'when the mast has all bytes received this label will be called  
```
Twi_master_need_nomore_byte:  
```vb
Return  
'-------------------------------------------------------------------------------

```

---

## View Show Allert Window

Action

Shows the Alert Windows when available.

An alert window can contain various info. In version 2086 it is limited to show when COM ports are added or removed.

When you use a CDC device (virtual COM port) and you plug the device, depending on settings and hub/usb port a new COM number will be assigned.

In the lower right of the screen an alert window/message will appear. It will not have focus and it will fade away after some time.

Below are 2 examples. One when a new COM port is found. And one when that same COM port is removed.

![alert_show_new_com](alert_show_new_com.png)

![show_alert_com_removed](show_alert_com_removed.png)

The X on the alert window can be used to close the window.

The X on the bottom can be used to Delete the window.

When you close a window, it will exist until BasCom is closed.

For this reason the 'View Show Alert Windows option exists : you can show the old alerts.

A new alert is always added after the last message. So in this example the first message was the NEW com port. 

And when the cable was pulled, the second alert was added. 

When multiple alert windows exist, you can use << and >> to scroll through them.

---
