# READMAGCARD

Action

Read data from a magnetic card.

Syntax

READMAGCARD var , count , coding

Remarks

Var | A byte array the receives the data.  
---|---  
Count | A byte variable that returns the number of bytes read.  
coding | A numeric constant that specifies if 5 or 7 bit coding is used. Valid values are 5 and 7.  
  
There can be 3 tracks on a magnetic card.

Track 1 stores the data in 7 bit including the parity bit. This is handy to store alpha numeric data.

On track 2 and 3 the data is stored with 5 bit coding.

The ReadMagCard routine works with ISO7811-2 5 and 7 bit decoding.

The returned numbers for 5 bit coding are:

Returned number | ISO characterT  
---|---  
0 | 0  
1 | 1  
2 | 2  
3 | 3  
4 | 4  
5 | 5  
6 | 6  
7 | 7  
8 | 8  
9 | 9  
10 | hardware control  
11 | start byte  
12 | hardware control  
13 | separator  
14 | hardware control  
15 | stop byte  
  
Example

```vb
'-----------------------------------------------------------------------------------------

'name : magcard.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show you how to read data from a magnetic card

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

'[reserve some space]

Dim Ar(100) As Byte , B As Byte , A As Byte

'the magnetic card reader has 5 wires

'red - connect to +5V

'black - connect to GND

'yellow - Card inserted signal CS

'green - clock

'blue - data

'You can find out for your reader which wires you have to use by connecting +5V

'And moving the card through the reader. CS gets low, the clock gives a clock pulse of equal pulses

'and the data varies

'I have little knowledge about these cards and please dont contact me about magnectic readers

'It is important however that you pull the card from the right direction as I was doing it wrong for

'some time :-)

'On the DT006 remove all the jumpers that are connected to the LEDs

'[We use ALIAS to specify the pins and PIN register]

```
_mport Alias Pinb 'all pins are connected to PINB

_mdata Alias 0 'data line (blue) PORTB.0

_mcs Alias 1 'CS line (yellow) PORTB.1

_mclock Alias 2 'clock line (green) PORTB.2

Config Portb = Input 'we only need bit 0,1 and 2 for input

Portb = 255 'make them high

```vb
Do

Print "Insert magnetic card" 'print a message

```
Readmagcard Ar(1) , B , 5 'read the data

```vb
Print B ; " bytes received"

For A = 1 To B

Print Ar(a); 'print the bytes

Next

Print

Loop

'By specifying 7 instead of 5 you can read 7 bit data

```