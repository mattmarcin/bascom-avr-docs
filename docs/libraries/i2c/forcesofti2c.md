# $FORCESOFTI2C

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