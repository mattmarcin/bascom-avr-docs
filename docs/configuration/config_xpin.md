# CONFIG XPIN

Action

Configures additional features of a processor port or pin.

Syntax

CONFIG XPIN=PORT|PIN, OUTPULL=pull

Syntax Xmega

CONFIG XPIN=PORT|PIN, INVERTIO=invio, SLEWRATE=slew, PULLUP=pull, SENSE=sense

Syntax Xtiny

CONFIG XPIN=PORT|PIN, INVERTIO=invio, PULLUP=pull, SENSE=sense

Remarks

Normal AVR port pins can be configured as an input or output. When configured as an input (CONFIG PIN=INPUT) they can also be set to tri-state (write a 0 to the PORT register) or to activate the pull up resistor(write a 1 to the PORT register).

Some new AVR processors use a special PUD register to control the pull up. The CONFIG XPIN automatically uses the proper registers to control the pull up state.

![notice](notice.jpg)The XPIN option was added for the Xmega which uses the term Outpull instead of Pullup. The compiler will accept both names but the Code Explorer and Intellisense expect PULLUP.

Normal AVR

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
PULLUP | Sets the output or pull mode. The following options are available: \- OFF :no pull up \- PULLUP : input pull up  
  
Normal AVR processors (tiny,mega) have only one option : PULLUP. 

The compiler will either write a 1 or 0 to the PORT register or the PUEx register.

You can control a single pin using a port pin name like PORTB.0 or the whole register like PORTB.

Normal AVR code that use : PORTX.Y=1 to activate the pull up, should be written as : CONFIG XPIN=PORTX.Y,PULLUP=PULLUP

XMEGA

You still need to use PORTx = state or PINx.y = state to configure the data direction of that port or pin in addition to CONFIG XPIN.

The xmega has many more options. The Xmega manual explains all the options.

The CONFIG XPIN statement will set the proper registers.

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
INVERTIO | This option will invert the data for both input and output modes. Possible values : ENABLED (will invert data), DISABLED(normal mode)   
SLEWRATE | Will enable or disable the slewrate. Enabling the slew rate will increase the rise/fall time by 50%-150%. Possible values : ENABLED, DISABLED ![notice](notice.jpg)For the Xmega E-series, the slewrate is set for the whole port. While the other Xmega series allow setting of sleware for an individual pin.  
PULLUP | Sets the output or pull mode. The following options are available: \- TOTEM : output totem pole \- BUSKEEPER : output totem pole, input bus keeper \- PULLDOWN : output totem pole, input pull down \- PULLUP : output totem pole, input pull up \- WIREDOR : output wired OR \- WIREDAND: output wired AND -WIREDORPULL : output wired OR, input pull down -WIREDANDPULL : output wired AND, input pull up  
SENSE | In input mode, the trigger sense can be configured. Possible values : \- BOTH : sense both edges \- RISING : sense rising edge -FALLING : sense falling edge -LOW_LEVEL :sense low level -INP_DISABLED : digital input buffer disabled (only PORTA-PORTF)  
  
Xtiny

You still need to use PORTx = state or PINx.y = state to configure the data direction of that port or pin in addition to CONFIG XPIN.

The xtiny has many more options.

The CONFIG XPIN statement will set the proper registers.

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
INVERTIO | This option will invert the data for both input and output modes. Possible values : ENABLED (will invert data), DISABLED(normal mode)   
PULLUP | Sets the output or pull mode. The following options are available: \- DISABLED or OFF : pull up disabled \- PULLUP : output totem pole, input pull up  
SENSE | In input mode, the trigger sense can be configured. Possible values : \- INT_DISABLED : interrupt disabled but input buffer enabled \- BOTH : sense both edges \- RISING : sense rising edge -FALLING : sense falling edge -LOW_LEVEL :sense low level -INP_DISABLED : digital input buffer disabled   
  
See also

[CONFIG PIN](config_port.md), [CONFIG INT](config_intx.md)

Example:

```vb
Config Porte.5 = Input  
Config Xpin = Porte.5 , Pullup = Pullup , Sense = Falling 'enable Pull up and reaction on falling edge

```
Example

```vb
$regfile = "xm256a3budef.dat"  
$Crystal = 32000000 '32MHz  
  
Config Xpin = Portc.0 , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
Config Xpin = Portc.1 , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
  
'setup the whole port at once  
Config Xpin = Portd , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
  


```