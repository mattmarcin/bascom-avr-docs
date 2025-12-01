# X10DETECT

Action

Returns a byte that indicates if a X10 Power line interface is found.

Syntax

Result = X10DETECT( )

Remarks

Result | A variable that will be assigned with 0 if there is no Power Line Interface found. 1 will be returned if the interface is found, and the detected mains frequency is 50 Hz. 2 will be returned if the interface is found and the detected mains frequency is 60 Hz.  
---|---  
  
When no TW-523 or other suitable interface is found, the other X10 routines will not work.

See also

[CONFIG X10](config_x10.md) , [X10SEND](x10send.md)

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