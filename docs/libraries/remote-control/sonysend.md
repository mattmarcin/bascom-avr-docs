# SONYSEND

Action

Sends Sony remote IR code.

Syntax

SONYSEND address [, bits]

Uses

TIMER1

Remarks

Address | The address of the Sony device.  
---|---  
bits | This is an optional parameter. When used, it must be 12, 15 or 20. Also, when you use this option, the address variable must be of the type LONG.  
  
SONY CD Infrared Remote Control codes (RM-DX55)

Function | Hex | Bin  
---|---|---  
Power | A91 | 1010 1001 0001  
Play | 4D1 | 0100 1101 0001  
Stop | 1D1 | 0001 1101 0001  
Pause | 9D1 | 1001 1101 0001  
Continue | B91 | 1011 1001 0001  
Shuffle | AD1 | 1010 1101 0001  
Program | F91 | 1111 1001 0001  
Disc | 531 | 0101 0011 0001  
1 | 011 | 0000 0001 0001  
2 | 811 | 1000 0001 0001  
3 | 411 | 0100 0001 0001  
4 | C11 | 1100 0001 0001  
5 | 211 | 0010 0001 0001  
6 | A11 | 1010 0001 0001  
7 | 611 | 0110 0001 0001  
8 | E11 | 1110 0001 0001  
9 | 111 | 0001 0001 0001  
0 | 051 | 0000 0101 0001  
>10 | E51 | 1110 0101 0001  
enter | D11 | 1101 0001 0001  
clear | F11 | 1111 0001 0001  
repeat | 351 | 0011 0101 0001  
disc - | BD1 | 1011 1101 0001  
disc + | H7D1 | 0111 1101 0001  
|<< | 0D1 | 0000 1101 0001  
>>| | 8D1 | 1000 1101 0001  
<< | CD1 | 1100 1101 0001  
>> | 2D1 | 0010 1101 0001  

SONY Cassette | RM-J901) |   
Deck A |  |   
stop | 1C1 | 0001 1100 0001  
play > | 4C1 | 0100 1100 0001  
play < | EC1 | 1110 1100 0001  
>> | 2C1 | 0010 1100 0001  
<< | CC1 | 1100 1100 0001  
record | 6C1 | 0110 1100 0001  
pause | 9C1 | 1001 1100 0001  
Dec B |  |   
stop | 18E | 0001 1000 1110  
play > | 58E | 0101 1000 1110  
play < | 04E | 0000 0100 1110  
>> | 38E | 0011 1000 1110  
<< | D8E | 1101 1000 1110  
record | 78E | 0111 1000 1110  
pause | 98E | 1001 1000 1110  
  
\---[ SONY TV Infrared Remote Control codes (RM-694) ]--------------------------

program + = &H090 : 0000 1001 0000

program - = &H890 : 1000 1001 0000

volume + = &H490 : 0100 1001 0000

volume - = &HC90 : 1100 1001 0000

power = &HA90 : 1010 1001 0000

sound on/off = &H290 : 0010 1001 0000

1 = &H010 : 0000 0001 0000

2 = &H810 : 1000 0001 0000

3 = &H410 : 0100 0001 0000

4 = &HC10 : 1100 0001 0000

5 = &H210 : 0010 0001 0000

6 = &HA10 : 1010 0001 0000

7 = &H610 : 0110 0001 0000

8 = &HE10 : 1110 0001 0000

9 = &H110 : 0001 0001 0000

0 = &H910 : 1001 0001 0000

-/-- = &HB90 : 1011 1001 0000

For more SONY Remote Control info:

<http://www.fet.uni-hannover.de/purnhage/>

The resistor must be connected to the OC1A pin. In the example a 2313 micro was used. This micro has pin portB.3 connected to OC1A.

Look in a data sheet for the proper pin when used with a different chip.

An IR booster circuit is shown below:

![IRBOOST](irboost.gif)

When sending hex, prefix with &H. When sending binary data, prefix with &B.

Sonysend &HA90

Sonysend &B010011010001

See also

[CONFIG RC5](config_rc5.md) , [GETRC5](getrc5.md) , [RC5SEND](rc5send.md) , [RC6SEND](rc6send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sonysend.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : code based on application note from Ger Langezaal

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

' +5V <\---[A Led K]---[220 Ohm]---> Pb.3 for 2313.

' RC5SEND is using TIMER1, no interrupts are used

' The resistor must be connected to the OC1(A) pin , in this case PB.3

Do

Waitms 500

```
Sonysend &HA90

```vb
Loop

End

```