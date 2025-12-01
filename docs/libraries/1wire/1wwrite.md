# 1WWRITE

Action

This statement writes a variable to the 1wire bus.

Syntax

1WWRITE var1

1WWRITE var1, bytes

1WWRITE var1 , bytes , port , pin

Remarks

var1 | Sends the value of var1 to the bus. The number of bytes can be specified too but this is optional.  
---|---  
bytes | The number of bytes to write. Must be specified when port and pin are used.  
port | The name of the PORT PINx register like PINB or PIND.  
pin | The pin number in the range from 0-7. May be a numeric constant or variable.  
  
Multiple 1-wire devices on different pins are supported.

To use this you must specify the port and pin that are used for the communication.

The 1wreset, 1wwrite and 1wread statements will work together when used with the old syntax. And the pin can be configured from the compiler options or with the [CONFIG 1WIRE](config_1wire.md) statement.

The syntax for additional 1-wire devices is :

1WRESET port , pin

1WWRITE var/constant, bytes, port , pin

var = 1WREAD(bytes, port, pin) ,for reading multiple bytes

See also

[1WREAD](1wread.md) , [1WRESET](1wreset.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wire.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wreset, 1wwrite and 1wread()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' pull-up of 4K7 required to VCC from Portb.2

' DS2401 serial button connected to Portb.2

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'when only bytes are used, use the following lib for smaller code

$lib "mcsbyte.lib"

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

Dim Ar(8) As Byte , A As Byte , I As Byte

Do

Wait 1

```
1wreset 'reset the device

Print Err 'print error 1 if error

1wwrite &H33 'read ROM command

For I = 1 To 8

Ar(i) = 1wread() 'place into array

```vb
Next

'You could also read 8 bytes a time by unremarking the next line

'and by deleting the for next above

'Ar(1) = 1wread(8) 'read 8 bytes

For I = 1 To 8

Print Hex(ar(i)); 'print output

Next

Print 'linefeed

Loop

'NOTE THAT WHEN YOU COMPILE THIS SAMPLE THE CODE WILL RUN TO THIS POINT

'THIS because of the DO LOOP that is never terminated!!!

'New is the possibility to use more than one 1 wire bus

'The following syntax must be used:

For I = 1 To 8

```
Ar(i) = 0 'clear array to see that it works

Next

1wreset Pinb , 2 'use this port and pin for the second device

1wwrite &H33 , 1 , Pinb , 2 'note that now the number of bytes must be specified!

```vb
'1wwrite Ar(1) , 5,pinb,2

'reading is also different

```
Ar(1) = 1wread(8 , Pinb , 2) 'read 8 bytes from portB on pin 2

```vb
For I = 1 To 8

Print Hex(ar(i));

Next

'you could create a loop with a variable for the bit number !

For I = 0 To 3 'for pin 0-3

```
1wreset Pinb , I

1wwrite &H33 , 1 , Pinb , I

Ar(1) = 1wread(8 , Pinb , I)

```vb
For A = 1 To 8

Print Hex(ar(a));

Next

Print

Next

End

```