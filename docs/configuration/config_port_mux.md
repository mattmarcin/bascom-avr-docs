# CONFIG PORT_MUX

Action

This configuration option allows you to configure the PORTMUX. The PORTMUX allows to chose alternative pin locations.

Syntax

CONFIG PORT_MUX = val0 , opt1=val1,opt2=val2, optx=valx

Remarks

val0 | There are 2 possible settings : \- OVERWITE : the entire register is updated.  \- PRESERVE : the register bits are preserved. See a detailed explanation below.   
---|---  
opt1, opt2, optx | These are the various options which will depend on the processor. Possible options are :  \- EVOUT0 : event output enable \- EVOUTx : event output x enable \- LUTx : alternative pin location CCL LUTx \- USARTx : alternative pin location USARTx \- SPI0 : alternative pin location SPI0 \- TWI0 : alternative pin location TWI0 \- TCA0x : alternative pin location wave output  \- TCB0x : alternative pin location wave output  
valx | The option value. It is either ENABLED or DISABLED The default register value is DISABLED.  
  
You can use the CTRL+SPACE key combination to get a list of options and values. This only works when you specified the definition file with $REGFILE. And when there are no errors in your code.

The PORTMUX is a convenient piece of hardware. It allows you to swap pin locations of hardware that share pins. As the pins are limited most pins share hardware functions.

For example for the TINY816 portA.1 : Besides being a normal port pin it is also MOSI, AIN1 and LUT0-IN1.

Now the PB2 and PB3 pins are used for TX/RX and TOSC1 and TOSC2. This means that you can not use the external oscillator AND the UART TX/RX pins. You need to chose.

But since the TX/RX pins have the option to be swapped with an alternative pin location, you can now use both !

So you would swap the USART0 pins from PB3(RX),PB2(TX),PB1(XCK) to PA1,PA2,PA3.

These PA1,PA2 and PA3 location are normally intended for the SPI and if you need that, you can also swap the SPI to PC0,PC1,PC2 and PC3.

Notice that all the device pins are swapped that belong to a device.

The following table from the data sheet make things more clear ;

![port_mux](port_mux.png)

The compiler will set the proper registers based on your configuration.

There are 2 important settings : OVERWRITE and PRESERVE. 

CONFIG PORT_MUX=PRESERVE will preserve the other settings in case they are not all configured.

Imagine a register with 4 bits and your setting only changes one bit. The compiler will read the data, change the bit and write it back.

When you change all 4 bits, the compiler will just write the new value since there is no need to preserve the old value.

When you use CONFIG PORT_MUX=OVERWRITE, the compiler will not preserve the old values, it will just write the new value. Since all registers are default 0 this is not a problem in many cases. But it could be when you dynamic change the settings.

It is important that you specify all settings on one line or use the line continuation character. This will give the best code.

When 1 register is updated, lds/sts is used while when multiple registers are updated, a pointer is used. 

So we would recommend to use OVERWRITE for the initial setup. Normally there is no need to change the configuration at run time. But when you do need to change it, use the PRESERVE mode.

Other CONFIG statements might also support the OVERWRITE/PRESERVE switch. You will find this when the REGMODE option is present among the options.

When the port multiplexer is configured it will not change the port direction settings. You need to do so yourself when that is required. 

For example when you use the default settings for the USART/COM, the TX is set to output mode. 

When you change the UART pins with the multiplexer you need to set the new TX pin to output mode. 

There is also a simpler way to just set the alternative pins for the USART. The CONFIG COMx have an option : TXPIN=xxx

Where xxx is either the default (DEF_PA0) or ALT1_PA4 or NONE. The setting values depend on the used processor.

DEF_ means that this is the default value. So you do not need to specify it. In fact when you use the default value you should not specify it since it will create more code because the port_mux is automatically set and the port mux registers are preserved.

ALT1_ means that this is the first alternative value. So PORTA4 would be used instead of PORTA.0

NONE means that none of the pins are connected. 

Since the TX pin is set to output mode, the preferred way to set the USART alternative pin is using CONFIG COM. 

The PORT_MUX will be updated automatically. In this scenario you should however use the PRESERVE mode since otherwise you might erase the USART alternative TX setting !

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : portmux.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates PORT_MUX  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 16_20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'dimension a variable  
Dim B As Byte  
  
Print "Test USART"  
  
For B = 1 To 10  
Print "Hello" ; Spc(3) ; B  
Waitms 1000  
Next  
  
'now use the port mux to switch the USART pins  
Config Port_mux = Overwrite , Usart0 = Alt1_pa1pa4 , Evout0 = Enabled  
'we need to set the new TX pin to output outselfs. This is pin PA1 for the tiny816  
Config Porta.1 = Output  
Do  
Print "ALT TX" ; Spc(3) ; B  
Waitms 1000  
```
Incr B  
```vb
Loop  
  
End

```