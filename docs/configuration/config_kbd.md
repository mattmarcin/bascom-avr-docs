# CONFIG KBD

Action

Configure the GETKBD() function and tell which port to use.

Syntax

CONFIG KBD = PORTx , DEBOUNCE = value [, DELAY = value] [,COLS=cols]

Remarks

PORTx | The name of the PORT to use such as PORTB or PORTD.  
---|---  
DEBOUNCE | By default the debounce value is 20. A higher value might be needed. The maximum is 255.  
Delay | An optional parameter that will cause Getkbd() to wait the specified amount of time after the key is detected. This parameter might be added when you call GetKbd() repeatedly in a loop. Because of noise and static electricity, wrong values can be returned. A delay of say 100 mS, can eliminate this problem.  
COLS | This value is 4 by default. Some chips do not have port pin 7 and for these cases you can use COLS=3, or COLS=2.  This does assume that columns are connected to the high port nibble.  
  
The GETKBD() function can be used to read the pressed key from a matrix keypad attached to a port of the uP.

You can define the port with the CONFIG KBD statement.

In addition to the default behavior you can configure the keyboard to have 6 rows instead of 4 rows.

CONFIG KBD = PORTx , DEBOUNCE = value , rows=6, row5=pinD.6, row6=pind.7

This would specify that row5 is connected to pind.6 and row7 to pind.7

Note that you can only use rows=6. Other values will not work.

See also

[GETKBD](getkbd.md)

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