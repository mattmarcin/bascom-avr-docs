# GETRC5

Action

Retrieves the RC5 remote code from a IR transmitter.

Syntax

GETRC5( address, command )

Uses

TIMER0

Remarks

address | The RC5 address  
---|---  
command | The RC5 command.  
  
This statement is based on the AVR 410 application note. Since a timer is needed for accurate delays and background processing TIMER0 is used by this statement.

The interrupt of TIMER0 is also used by this statement.

TIMER0 can be used by your application since the values are preserved by the statement but a delay can occur. The interrupt can not be reused.

You may use any pin that can work as an input pin. Use the CONFIG RC5 statement to specify which pin is connected to the IR receiver.

GETRC5 supports extended RC5 code reception.

The SFH506-36 is used from Siemens. Other types can be used as well. The TSOP1736 has been tested with success.

You can also use the pin compatible TSOP31236

![SFH506](sfh506.jpg)

For a good operation use the following values for the filter.

![SFH506-2](sfh506-2.jpg)

![tsop312xx](tsop312xx.png)

TSOP 312xx

1=GND, 2=VSS, 3=OUT

Most audio and video systems are equipped with an infra-red remote control.

The RC5 code is a 14-bit word bi-phase coded signal.

The two first bits are start bits, always having the value 1.

The next bit is a control bit or toggle bit, which is inverted every time a button is pressed on the remote control transmitter.

Five system bits hold the system address so that only the right system responds to the code.

Usually, TV sets have the system address 0, VCRs the address 5 and so on. The command sequence is six bits long, allowing up to 64 different commands per address.

The bits are transmitted in bi-phase code (also known as Manchester code).

For extended RC5 code, the extended bit is bit 6 of the command.

The toggle bit is stored in bit 7 of the command.

Xmega

The Xmega will use timer TCC0 instead of TIMER0. 

You MUST enable the low priority interrupts since TCC0 is used in this mode. You can do this with this command :

Config Priority = Static , Vector = Application , Lo = Enabled

Xtiny

The Xtiny will use a TCAx or TCBx timer.

Alternative Background decoding normal AVR

A special alternative library named RC5.LIB can be used to decode the RC5 signals on the background. The developing of this library was sponsored by [Lumicoin](<http://www.lumicoin.de/>).

See [CONFIG RC5](config_rc5.md) for more information.

Alternative Background decoding Xtiny

A special alternative library named RC5_BG_XTINY.lib can be used to decode the RC5 signals on the background. The library is automatically included when you select the BACKGROUND mode.

See [CONFIG RC5](config_rc5.md) for more information and an example.

See also

[CONFIG RC5](config_rc5.md) , [RC5SEND](rc5send.md), [RC6SEND](rc6send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rc5.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : based on Atmel AVR410 application note

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'use byte library for smaller code

$lib "mcsbyte.lbx"

'This example shows how to decode RC5 remote control signals

'with a SFH506-35 IR receiver.

'Connect to input to PIND.2 for this example

'The GETRC5 function uses TIMER0 and the TIMER0 interrupt.

'The TIMER0 settings are restored however so only the interrupt can not

'be used anymore for other tasks

'tell the compiler which pin we want to use for the receiver input

Config Rc5 = Pind.2

'the interrupt routine is inserted automatic but we need to make it occur

'so enable the interrupts

Enable Interrupts

'reserve space for variables

Dim Address As Byte , Command As Byte

Print "Waiting for RC5..."

Do

'now check if a key on the remote is pressed

'Note that at startup all pins are set for INPUT

'so we dont set the direction here

'If the pins is used for other input just unremark the next line

'Config Pind.2 = Input

```
Getrc5(address , Command)

```vb
'we check for the TV address and that is 0

If Address = 0 Then

'clear the toggle bit

'the toggle bit toggles on each new received command

'toggle bit is bit 7. Extended RC5 bit is in bit 6

```
Command = Command And &B01111111

```vb
Print Address ; " " ; Command

End If

Loop

End

```
Example XTINY

```vb
'--------------------------------------------------------------------------------  
'name : avr128da28-getrc5.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 using time TCA0 and TCB0  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX128da28.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'we use the uart for some terminal output  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Rc5 = Pind.1 , Mode = Normal , Timer = Tca0  
' ^^^ use either a timer TCA0, TCA1 or a TCBx timer  
' ^^^^ define the pin that is connected to the output of the IR received  
' also have a look at the background mode that runs completely in the background!  
  
'since the timer is used in interrupt mode you must enabl global interrupts  
Enable Interrupts  
  
'reserve space for variables  
Dim Address As Byte , Command As Byte  
  
Print "Waiting for RC5..."  
  
do  
'now check if a key on the remote is pressed  
'Note that at startup all pins are set for INPUT  
'so we dont set the direction here  
'If the pins is used for other input just unremark the next line  
'Config Pind.2 = Input  
```
Getrc5(address , Command)  
```vb
'we check for the TV address and that is 0  
If Address = 0 Then  
'clear the toggle bit  
'the toggle bit toggles on each new received command  
'toggle bit is bit 7. Extended RC5 bit is in bit 6  
```
Command = Command And &B01111111  
```vb
Print Address ; " " ; Command  
End If  
'waitms 500  
loop

```