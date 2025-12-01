# CONFIG I2CSLAVE

The I2C-Slave library is intended to create I2C slave chips. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>)

The I2C Slave add on can turn some chips into a I2C slave device. You can start your own chip plant this way.

Most new AVR chips have a so called TWI/I2C interface. As a customer of the I2C slave lib, you can get both libs.

The i2cslave.lib works in interrupt mode and is the best way as it adds less overhead and also less system resources.

With this add-on library you get both libraries:

| i2cslave.lib and i2cslave.lbx : This library is used for AVRâs which have no hardware TWI/I2C interface like for example ATTINY2313 or ATTINY13. In this case TIMER0 and INT0 is used for SDA and SCL (Timer0 Pin = SCL, INT0 Pin = SDA). Only AVR' with TIMER0 and INT0 on the same port can use this library like for example ATTINY2313 or ATTINY13. The i2cslave.lib file contains the ASM source. The i2cslave.lbx file contains the compiled ASM source. See CONFIG I2CSLAVE below.  
---|---  
  
| i2c_TWI-slave.LBX : This library can be used when an AVR have an TWI/I2C hardware interface like for example ATMEGA8, ATMEGA644P or ATMEGA128. In this case the hardware SDA and SCL pin's of the AVR will be used (with ATMEGA8: SCL is PORTC.5 and SDA is PORTC.4). This library will be used when USERACK = OFF. When USERACK =ON then i2c_TWI-slave-acknack.LBX will be used. See also [Config TWISLAVE](config_twislave.md)  
---|---  
  
Action

Configures the I2C slave mode for ATTINY and ATMEGA devices.

Before you begin

Copy the library files into the BASCOM-AVR\LIB directory.

Syntax

CONFIG I2CSLAVE = address , INT = interrupt , TIMER = tmr

(This function is part of the I2C-Slave library. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

Remarks

Address | The slave address you want to assign to the I2C slave chip. This is an address that must be even like &H60. So &H61 cannot be used. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases.   
---|---  
Interrupt | The interrupt that must be used. This is INT0 by default.  
Tmr | The timer that must be used. This is TIMER0 by default.  
  
The library was written for TIMER0 and INT0.

While the interrupt can be specified, you need to change the library code when you use a non-default interrupt. For example when you like to use INT1 instead of the default INT0. 

The same applies to the TIMER. You need to change the library when you like to use another timer.

You can not use these interrupts yourself. It also means that the SCL and SDA pins are fixed.

CONFIG I2CSLAVE will enable the global interrupts.

Timer0 and INT0 Pin's of Various AVR's

The I2C slave routines use the TIMER0 and INT0. 

The following table lists the pins for the various chips

Chip | SCL | SDA  
---|---|---  
AT90S1200 | PORTD.4 | PORTD.2  
AT90S2313 | PORTD.4 | PORTD.2  
AT90S2323 | PORTB.2 | PORTB.1  
AT90S2333 | PORTD.4 | PORTD.2  
AT90S2343 | PORTB.2 | PORTB.1  
AT90S4433 | PORTD.4 | PORTD.2  
ATTINY22 | PORTB.2 | PORTB.1  
ATTINY13 | PORTB.2 | PORTB.1  
ATTINY2313 | PORTD.4 | PORTD.2  
ATMEGA1280 | PORTD.7 | PORTD.0  
ATMEGA128CAN | PORTD.7 | PORTD.0  
ATMEGA168 | PORTD.4 | PORTD.2  
ATMEGA2560 | PORTD.7 | PORTD.0  
ATMEGA2561 | PORTD.7 | PORTD.0  
ATMEGA48 | PORTD.4 | PORTD.2  
ATMEGA88 | PORTD.4 | PORTD.2  
ATMEGA8 | PORTD.4 | PORTD.2  

After you have configured the slave address, you can insert your code.

A do-loop would be best:

```vb
Do  
' your code here  
Loop

```
After your main program you need to insert two labels with a return:

When the master needs to read a byte, the following label is always called.

You must put the data you want to send to the master in variable _a1 which is register R16

I2c_master_needs_data:  
```vb
'when your code is short, you need to put in a waitms statement  
'Take in mind that during this routine, a wait state is active and the master will wait  
'After the return, the waitstate is ended  
Config Portb = Input ' make it an input  
  
```
_a1 = Pinb ' Get input from portB and assign it  
Return

When the master writes a byte, the following label is always called.

It is your task to retrieve variable _A1 and do something with it

_A1 is register R16 that could be destroyed/altered by BASIC statements

For that reason it is important that you first save this variable.

I2c_master_has_data:  
```vb
'when your code is short, you need to put in a waitms statement  
'Take in mind that during this routine, a wait state is active and the master will wait  
'After the return, the waitstate is ended  
  
```
Bfake = _a1 ' this is not needed but it shows how you can store _A1 in a byte  
```vb
'after you have stored the received data into bFake, you can alter R16  
Config Portb = Output ' make it an output since it could be an input  
```
Portb = _a1 'assign _A1 (R16)  
Return

See Also

[CONFIG TWI](config_twi.md) , [CONFIG TWISLAVE](config_twislave.md), [I2C TWI Slave](i2ctwislave.md)

Debugging Hint's

If you encounter a problem first check:

•| Do you use the correct Pin's for SDA and SCL ?  
---|---  
  
•| Pull-up Resistor from SDA and SCL to Vcc ?  
---|---  
  
•| Try to reduce clockrate from I2C Master  
---|---  
  
•| Try to use waitms XX between the I2CWBYTE in the I2C Master AVR  
---|---  
  
•| Try to reduce code in the interrupt routine  
---|---  
  
Example

```vb
'-----------------------------------------------------------------------------------------

'name : i2c_pcf8574.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how you could use the I2C slave library to create a PCF8574

'micro : AT90S2313

'suited for demo : NO, ADDON NEEDED

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 3684000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'This program shows how you could use the I2C slave library to create a PCF8574

'The PCF8574 is an IO extender chip that has 8 pins.

'The pins can be set to a logic level by writing the address followed by a value

'In order to read from the pins you need to make them '1' first

'This program uses a AT90S2313, PORTB is used as the PCF8574 PORT

'The slave library needs INT0 and TIMER0 in order to work.

'SCL is PORTD.4 (T0)

'SDA is PORTD.2 (INT0)

'Use 10K pull up resistors for both SCL and SDA

'The Slave library will only work for chips that have T0 and INT0 connected to the same PORT.

'These chips are : 2313,2323, 2333,2343,4433,tiny22, tiny12,tiny15, M8

'The other chips have build in hardware I2C(slave) support.

'specify the slave address. This is &H40 for the PCF8574

'You always need to specify the address used for write. In this case &H40 ,

'The config i2cslave command will enable the global interrupt enable flag !

Config I2cslave = &B01000000 ' same as &H40

'Config I2cslave = &H40 , Int = Int0 , Timer = Timer0

'A byte named _i2c_slave_address_received is generated by the compiler.

'This byte will hold the received address.

'A byte named _i2c_slave_address is generated by the compiler.

'This byte must be assigned with the slave address of your choice

'the following constants will be created that are used by the slave library:

' _i2c_pinmask = &H14

' _i2c_slave_port = Portd

' _i2c_slave_pin = Pind

' _i2c_slave_ddr = Ddrd

' _i2c_slave_scl = 4

' _i2c_slave_sda = 2

'These values are adjusted automatic depending on the selected chip.

'You do not need to worry about it, only provided as additional info

'by default the PCF8574 port is set to input

Config Portb = Input

```
Portb = 255 'all pins high by default

```vb
'DIM a byte that is not needed but shows how you can store/write the I2C DATA

Dim Bfake As Byte

'empty loop

Do

' you could put your other program code here

'In any case, do not use END since it will disable interrupts

Loop

'here you can write your other program code

'But do not forget, do not use END. Use STOP when needed

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

' The following labels are called from the slave library

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'When the master wants to read a byte, the following label is allways called

'You must put the data you want to send to the master in variable _a1 which is register R16

```
I2c_master_needs_data:

```vb
'when your code is short, you need to put in a waitms statement

'Take in mind that during this routine, a wait state is active and the master will wait

'After the return, the waitstate is ended

Config Portb = Input ' make it an input

```
_a1 = Pinb ' Get input from portB and assign it

```vb
Return

'When the master writes a byte, the following label is always called

'It is your task to retrieve variable _A1 and do something with it

'_A1 is register R16 that could be destroyed/altered by BASIC statements

'For that reason it is important that you first save this variable

```
I2c_master_has_data:

```vb
'when your code is short, you need to put in a waitms statement

'Take in mind that during this routine, a wait state is active and the master will wait

'After the return, the waitstate is ended

```
Bfake = _a1 ' this is not needed but it shows how you can store _A1 in a byte

```vb
'after you have stored the received data into bFake, you can alter R16

Config Portb = Output ' make it an output since it could be an input

```
Portb = _a1 'assign _A1 (R16)

```vb
Return

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'You could simply extend this sample so it will use 3 pins of PORT D for the address selection

'For example portD.1 , portd.2 and portD.3 could be used for the address selection

'Then after the CONFIG I2CSLAVE = &H40 statement, you can put code like:

'Dim switches as Byte ' dim byte

'switches = PIND ' get dip switch value

'switches = switches and &H1110 ' we only need the lower nibble without the LS bit

'_i2c_slave_address = &H40 + switches ' set the proper address

```