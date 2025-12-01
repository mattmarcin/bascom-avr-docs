# CONFIG PORT

Action

Sets the port or a port pin to the right data direction.

Syntax

```vb
CONFIG PORTx = state

CONFIG PINx = state

CONFIG PORTx.y = state

CONFIG PINx.y = state

```
Remarks

state | A numeric constant that can be INPUT or OUTPUT. INPUT will set the data direction register to input for port X. OUTPUT will set the data direction to output for port X. You can also use a number for state. &B00001111, will set the upper nibble to input and the lower nibble to output. You can either set a single port pin or a whole port to input or output. When you set a single pin , you can use INPUT, OUTPUT, 0 or 1. When you set a complete port, you can use INPUT, OUTPUT or a numeric constant that fits into a byte.  
---|---  
x | A valid port letter such as A,B,C etc.  Example : CONFIG PORTB = INPUT Example : CONFIG PINB=OUTPUT  
y | A valid pin number in the range of 0-7. Example : CONFIG PINB.0=OUTPUT Example : CONFIG PORTB.1=INPUT  
  
The best way to set the data direction for more than 1 pin, is to use the CONFIG PORT, statement and not multiple lines with CONFIG PIN statements.

You may not use variables for the port letters and pin numbers. If you need to dynamically set a pin direction, you can use this form : SET PORTB.somepin , where somepin may be a constant or a variable. 

If the the port itself is also dynamic, then you could use OUT with the proper address.

PORT and PIN can equally be used. PIN can be used to indicate that you set a single pin. And PORT can be used to indicate that you set the complete PORT. But they both do the same. 

There could be a reason to use PIN or PORT : when using an ALIAS like in this example:

Switch ALIAS PINB.0

LED ALIAS PORTB.1

```vb
CONFIG SWITCH=INPUT

CONFIG LED=OUTPUT

If SWITCH=0 THEN ' this works only on the PIN register

```
![notice](notice.jpg)When you want to read the status of an input pin you must use the PIN register.

When you want to set the output level of an output pin you must use the PORT register.

So you never write to a PIN register. Exceptions are for processors that have special ports that can toggle when you write to the PIN register. 

The compiler will handle that automatic when you use the TOGGLE statement.

The example below show how to read a pin configured to act as an input pin and how to change a pin configured as output pin.

See Also

[AVR Internal hardware ports](avr_internal_hardware_port_b.md) , [SET](set.md), [RESET](reset.md), [TOGGLE](toggle.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : port.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: PortB and PortD

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Byte , Count As Byte

'configure PORT D for input mode

Config Portd = Input

'reading the PORT, will read the latch, that is the value

'you have written to the PORT.

'This is not the same as reading the logical values on the pins!

'When you want to know the logical state of the attached hardware,

'you MUST use the PIN register.

```
A = Pind

'a port or SFR can be treated as a byte

A = A And Portd

Print A 'print it

Bitwait Pind.7 , Reset 'wait until bit is low

```vb
'We will use port B for output

Config Portb = Output

'assign value

```
Portb = 10 'set port B to 10

Portb = Portb And 2

Set Portb.0 'set bit 0 of port B to 1

Incr Portb

'Now a light show on the STK200

Count = 0

Do

Incr Count

Portb = 1

For A = 1 To 8

Rotate Portb , Left 'rotate bits left

```vb
Wait 1

Next

'the following 2 lines do the same as the previous loop

'but there is no delay

' Portb = 1

' Rotate Portb , Left , 8

Loop Until Count = 10

Print "Ready"

'Again, note that the AVR port pins have a data direction register

'when you want to use a pin as an input it must be set low first

'you can do this by writing zeros to the DDRx:

'DDRB =&B11110000 'this will set portb1.0,portb.1,portb.2 and portb.3 to use as inputs.

'So : when you want to use a pin as an input set it low first in the DDRx!

' and read with PINx

' and when you want to use the pin as output, write a 1 first

' and write the value to PORTx

End

```