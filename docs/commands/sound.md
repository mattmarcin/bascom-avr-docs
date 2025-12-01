# SOUND

Action

Sends pulses to a port pin.

Syntax

SOUND pin, duration, pulses

Remarks

Pin | Any I/O pin such as PORTB.0 etc.  
---|---  
Duration | The number of pulses to send. Byte, integer/word or constant.  
Pulses | The time the pin is pulled low and high. This is the value for a loop counter.  
  
When you connect a speaker or a buzzer to a port pin (see hardware) , you can use the SOUND statement to generate some tones.

The port pin is switched high and low for pulses times.

This loop is executed duration times.

The SOUND statement is not intended to generate accurate frequencies. Use a TIMER to do that.

![sound](sound.png)

See also

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : sound.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : SOUND

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

Dim Pulses As Word , Periods As Word

```
Pulses = 65535 : Periods = 10000 'set variables

Speaker Alias Portb.1 'define port pin

Sound Speaker , Pulses , Periods 'make some noice

```vb
'note that pulses and periods must have a high value for high XTALS

'sound is only intended to make some noise!

'pulses range from 1-65535

'periods range from 1-65535

End

```