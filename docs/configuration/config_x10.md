# CONFIG X10

Action

Configures the pins used for X10.

Syntax

CONFIG X10 = pinZC , TX = portpin

Remarks

PinZC | The pin that is connected to the zero cross output of the TW-523. This is a pin that will be used as INPUT.  
---|---  
Portpin | The pin that is connected to the TX pin of the TW-523. TX is used to send X10 data to the TW-523. This pin will be used in output mode.  
  
The TW-523 RJ-11 connector has the following pinout:

Pin | Description | Connect to micro  
---|---|---  
1 | Zero Cross | Input pin. Add 5.1K pull up.  
2 | GND | GND  
3 | RX | Not used.  
4 | TX | Output pin. Add 1K pull up.  
  
See also

[X10DETECT](x10detect.md) , [X10SEND](x10send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : x10.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example needs a TW-523 X10 interface

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'define the house code

```
Const House = "M" ' use code A-P

```vb
Waitms 500 ' optional delay not really needed

'dim the used variables

Dim X As Byte

'configure the zero cross pin and TX pin

Config X10 = Pind.4 , Tx = Portb.0

' ^--zero cross

' ^--- transmission pin

'detect the TW-523

```
X = X10detect()

```vb
Print X ' 0 means error, 1 means 50 Hz, 2 means 60 Hz

Do

Input "Send (1-32) " , X

'enter a key code from 1-31

'1-16 to address a unit

'17 all units off

'18 all lights on

'19 ON

'20 OFF

'21 DIM

'22 BRIGHT

'23 All lights off

'24 extended code

'25 hail request

'26 hail acknowledge

'27 preset dim

'28 preset dim

'29 extended data analog

'30 status on

'31 status off

'32 status request

```
X10send House , X ' send the code

```vb
Loop

Dim Ar(4) As Byte

```
X10send House , X , Ar(1) , 4 ' send 4 additional bytes

End