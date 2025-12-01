# GETRC

Action

Retrieves the value of a resistor or a capacitor.

Syntax

var = GETRC( pin , number )

Remarks

Var | The word variable that is assigned with the value.  
---|---  
Pin | The PIN name for the R/C is connection.  
Number | The port pin for the R/C is connection.  
  
The name of the input port (PIND for example) must be passed even when all the other pins are configured for output. The pin number must also be passed. This may be a constant or a variable.

A circuit is shown below:

![getrc](getrc.gif)

The capacitor is charged and the time it takes to discharge it is measured and stored in the variable. Now when you vary either the resistor or the capacitor, different values will be returned. This function is intended to return a relative position of a resistor wiper, not to return the value of the resistor. But with some calculations it can be retrieved.

The GETRC function passes the address of the PIN register to the _GETRC library code.

This will not work for PINF of the ATMEGA128. The PORTF, PINF, DDRF map is not continuous grouped together.

To solve this, you can use the $lib "getRc_m128_PINF.lib"

This lib is only for the M128/M64 PORTF, and when the compatibility fuse is not set to M103.

See also

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : getrc.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates how to get the value of a resistor

'micro : AT90S8535

'suited for demo : yes

'commercial addon needed : no

' The library also shows how to pass a variable for use with individual port

' pins. This is only possible in the AVR architecture and not in the 8051

'-----------------------------------------------------------------------------------------

$regfile = "8535def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'The function works by charging a capacitor and uncharge it little by little

'A word counter counts until the capacitor is uncharged.

'So the result is an indication of the position of a pot meter not the actual

'resistor value

'This example used the 8535 and a 10K ohm variable resistor connected to PIND.4

'The other side of the resistor is connected to a capacitor of 100nF.

'The other side of the capacitor is connected to ground.

'This is different than BASCOM-8051 GETRC! This because the architecture is different.

'The result of getrc() is a word so DIM one

Dim W As Word

Do

'the first parameter is the PIN register.

'the second parameter is the pin number the resistor/capacitor is connected to

'it could also be a variable!

```
W = Getrc(pind , 4)

```vb
Print W

Wait 1

Loop

```