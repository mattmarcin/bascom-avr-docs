# GETKBD

Action

Scans a 4x4 matrix keyboard and return the value of the key pressed.

Syntax

var = GETKBD()

Remarks

Var | The numeric variable that is assigned with the value read from the keyboard  
---|---  
  
The GETKBD() function can be attached to a port of the uP.

You can define the port with the CONFIG KBD statement.

A schematic for PORTB is shown below

![matrixkbd](matrixkbd.gif)

Note that the port pins can be used for other tasks as well. But you might need to set the port direction of those pins after you have used getkbd(). For example the LCD pins are set to output at the start of your program. A call to getkbd() would set the pins to input.

By setting DDR.x register you can set the pins to the proper state again.

As an alternative you can use CONFIG PIN or CONFIG PORT.

When no key is pressed 16 will be returned.

When using the 2 additional rows, 24 will be returned when no key is pressed.

On the STK200 this might not work since other hardware is connected too that interferes.

You can use the [Lookup()](lookup.md) function to convert the byte into another value. This because the GetKBD() function does not return the same value as the key pressed. It will depend on which keyboard you use.

Sometimes it can happen that it looks like a key is pressed while you do not press a key. This is caused by the scanning of the pins which happens at a very high frequency.

It will depend on the used keyboard. You can add series resistors with a value of 470-1K

The routine will wait for 100 mS by default after the code is retrieved. With CONFIG KBD you can set this delay.

See also

[CONFIG KBD](config_kbd.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : getkbd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : GETKBD

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

'specify which port must be used

'all 8 pins of the port are used

Config Kbd = Portb

'dimension a variable that receives the value of the pressed key

Dim B As Byte

'loop for ever

Do

```
B = Getkbd()

```vb
'look in the help file on how to connect the matrix keyboard

'when you simulate the getkbd() it is important that you press/click the keyboard button

' before running the getkbd() line !!!

Print B

'when no key is pressed 16 will be returned

'use the Lookup() function to translate the value to another one

' this because the returned value does not match the number on the keyboad

Loop

End

```