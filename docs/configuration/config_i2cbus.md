# CONFIG I2CBUS

Action

This configuration statement defines the SCL and SDA pins of an I2C multibus.

Syntax

CONFIG I2CBUS= bus , SCL=scl , SDA=sda

Remarks

bus | A numeric value in the range from 0 to 15.  
---|---  
scl | The SCL pin used for the specified bus.  
sda | The SDA pin used for the specified bus.  
  
While XMEGA supports multiple TWI busses, the normal AVR only supports on TWI or no I2C bus. The CONFIG I2CBUS is a software solution to use multiple I2C busses.

An internal variable is created named I2CBUS. This is a BYTE variable. 

You need to assign this variable a value before you use the usual I2C statements. When you want to use a different bus, you just assign the variable a new bus index value.

Have a look at the sample. It creates 4 busses. Since I2CINIT is required, a loop is used to call the I2CINIT statement for all busses.

And another loop is used to send data to all 4 busses.

![notice](notice.jpg)Both SCL and SDA pins must be on the same PORT. Also, the PIN, DDR and PORT register addresses of the processor must be in ascending order and need to exist.

For example the M1284P portA group :

PORTA = $02

DDRA = $01

PINA = $00

This is ok to use. But some processors have no DDR register because a port can only be used in output or input mode. Such a port can not be used.

An example of a bad port is PORTF in the M128. As you can see there is a gap in the address between PINF and DDRF and this will make it fail.

PORTF = $62

DDRF = $61

PINF = $00 

ASM

The I2C routines are located in the i2c_multibus.lib.

See also

[CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md), [Using the I2C protocol](using_the_i2c_protocol.md) , [I2CINIT](i2cinit.md)

Example

```vb
'------------------------------------------------------------------------------  
'name : I2C-multibus.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates I2C multibus library  
'micro : Mega88  
'suited for demo : no, lib not included in demo  
'commercial addon needed : no  
'------------------------------------------------------------------------------  
$regfile="m88def.dat"  
$crystal=8000000  
$hwstack=32  
$swstack=24  
$framesize=24  
  
config i2cbus=0,scl=portc.0,sda= portc.1 'each bus requires a configuration of the SCL and SDA pins  
config i2cbus=1,scl=portc.2,sda= portc.3 'this sample creates 4 busses  
config i2cbus=2,scl=portd.2,sda= portd.3  
config i2cbus=3,scl=portd.4,sda= portd.5  
  
Dim j as Byte  
  
For j=0 to 3 'the first bus is 0 !!!  
```
i2cbus=j 'select the BUS  
i2cinit 'init the pins and state  
```vb
Next  
  
do  
for j=0 to 3  
```
i2cbus=j 'select the bus  
I2CSend &H40, &B01010101 'send some data  
```vb
next  
waitms 100  
loop  
  
end

```