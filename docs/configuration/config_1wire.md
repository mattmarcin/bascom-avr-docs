# CONFIG 1WIRE

Action

Configure the pin to use for 1WIRE statements and override the compiler setting.

Syntax

CONFIG 1WIRE = pin [, extended=0|1]

Remarks

Pin | The port pin to use such as PORTB.0  
---|---  
extended | An optional constant value of 0 or 1. This is an optional parameter  
  
The CONFIG 1WIRE statement overrides the compiler setting. It is the preferred that you use it. This way the setting is stored in your source code. 

You can configure only one pin for the 1WIRE statements because the idea is that you can attach multiple 1WIRE devices to the 1WIRE bus.

You can however use multiple pins and thus multiple busses. All 1wire commands and functions need the port and pin in that case. A CONFIG 1WIRE statement is not need in that case either.

The 1wire commands and function will automatically set the DDR and PORT register bits to the proper state. You do not need to bring the pins into the right state yourself.

It is important that you use a pull up resistor of 4K7 ohm on the 1wire pin(for 5V VCC). The pull up resistor of the AVR is not sufficient.

Also notice that some 1wire chips also need +5V. 1 wire is just marketing since you need GND anyway. The least is 2 wires and typical you need 3 wires.

Extended

The extended option is only required when you use multiple busses/pins and if these pins mix normal and extended addresses.

Let's clear that up. When the 1wire code was written in 1995 all the port addresses were normal I/O addresses. These are addresses that fit in the I/O space (address < &H60). To save code, register R31 was cleared in the library and the port register was passed in R30.

When Atmel introduced the extended I/O registers with address >&HFF, it was possible to set R31 to a fixed value when the user port was an extended I/O address.

But when you want to mix the addresses, there is no other way then to pass the word address of the I/O register to the library code.

And that is exactly what EXTENDED=1 will do. It will use more code. This support was written for a customer that already made his PCB's. We do advise to use the same port when you use multiple pins. 

ATMEGA128 PORTF

The ATMEGA128 PORTF is split up. Normally, the DDR, PIN and PORT registers are in the same order.

For example : PORTB = &H18 , DDRB = &H17 and PINB = &H16

But PORTF in the MEGA128 is different : PINF = &H00 , PORTF = &H62 , DDRF = &H61

You need a special library named [M128-1wire-PortF.lib](m128_1wire_portf.md) for this processor and port. This library is fixed to portF

See also

[1WRESET](1wreset.md) , [1WREAD](1wread.md) , [1WWRITE](1wwrite.md) , [1WIRECOUNT ](1wirecount.md), [1WRESET](1wreset.md) , [1WSEARCHFIRST](1wsearchfirst.md) , [1WSEARCHNEXT](1wsearchnext.md)

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

$crystal = 8000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

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
Xmega Example

```vb
'--------------------------------------------------------------------------------  
'name : XM128-1wire.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates 1wreset, 1wwrite and 1wread()  
'micro : Xm128A1  
'suited for demo : no  
'commercial addon needed : no  
' pull-up of 4K7 required to VCC from Portb.0  
' DS2401 serial button connected to Portb.0  
'--------------------------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
  
$lib "xmega.lib" : $external _xmegafix_clear : $external _xmegafix_rol_r1014  
  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 32 'default use 10 for the SW stack  
$framesize = 32 'default use 40 for the frame space  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
'configure UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
  
'configure 1wire pin  
Config 1wire = Portb.0 'use this pin  
  
Dim Ar(8) As Byte , A As Byte , I As Byte  
  
Print "start"  
  
```
A = 1wirecount()  
```vb
Print A ; " devices found"  
  
'get first  
```
Ar(1) = 1wsearchfirst()  
  
```vb
For I = 1 To 8 'print the number  
Print Hex(ar(i));  
Next  
Print  
  
Do  
'Now search for other devices  
```
Ar(1) = 1wsearchnext() ' get next device  
```vb
For I = 1 To 8  
Print Hex(ar(i));  
Next  
Print  
Loop Until Err = 1  
  
Waitms 2000  
  
  
Do  
```
1wreset 'reset the device  
Print Err 'print error 1 if error  
  
1wwrite &H33 'read ROM command  
```vb
' Ar(1) = 1wread(8) you can use this instead of the code below  
  
For I = 1 To 8  
```
Ar(i) = 1wread() 'place into array  
```vb
Next  
  
For I = 1 To 8  
Print Hex(ar(i)); 'print output  
Next  
Print 'linefeed  
Waitms 1000  
Loop  
  
  
End

```