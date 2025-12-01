# DEBOUNCE

Action  
  
Debounce a port pin connected to a switch.

Syntax

DEBOUNCE Px.y , state , label [ , SUB]

Remarks

Px.y | A port pin like PINB.0 , to examine.  
---|---  
State | 0 for jumping when PINx.y is low , 1 for jumping when PINx.y is high  
Label | The label to GOTO when the specified state is detected  
SUB | The label to GOSUB when the specified state is detected  
  
When you specify the optional parameter SUB, a GOSUB to label is performed instead of a GOTO.

The DEBOUNCE statement tests the condition of the specified pin and if true there will be a delay for 25 mS and the condition will be checked again. (eliminating bounce of a switch)

When the condition is still true and there was no branch before, it branches to specified the label.

When the condition is not true, or the logic level on the pin is not of the specified level, the code on the next line will be executed.

When DEBOUNCE is executed again, the state of the switch must have gone back in the original position before it can perform another branch. So if you are waiting for a pin to go low, and the pin goes low, the pin must change to high, before a new low level will result in another branch.

Each DEBOUNCE statement, which uses a different port, uses 1 BIT of the internal memory to hold its state. And as the bits are stored in SRAM, it means that even while you use only 1 pin/bit, a byte is used for storage of the bit.

DEBOUNCE will not wait for the input value to met the specified condition. You need to use BITWAIT if you want to wait until a bit will have a certain value.

So DEBOUNCE will not halt your program while a BITWAIT can halt your program if the bit will never have the specified value. You can combine BITWAIT and DEBOUNCE statements by preceding a DEBOUNCE with a BITWAIT statement.

See also

[CONFIG DEBOUNCE](config_debounce.md) , [BITWAIT](bitwait.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : deboun.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates DEBOUNCE

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

Config Debounce = 30 'when the config statement is not used a default of 25mS will be used but we override to use 30 mS

'Debounce Pind.0 , 1 , Pr 'try this for branching when high(1)

```
Debounce Pind.0 , 0 , Pr , Sub

Debounce Pind.0 , 0 , Pr , Sub

```vb
' ^----- label to branch to

' ^---------- Branch when PIND.0 goes low(0)

' ^---------------- Examine PIND.0

'When Pind.0 goes low jump to subroutine Pr

'Pind.0 must go high again before it jumps again

'to the label Pr when Pind.0 is low

```
Debounce Pind.0 , 1 , Pr 'no branch

Debounce Pind.0 , 1 , Pr 'will result in a return without gosub

End

Pr:

```vb
Print "PIND.0 was/is low"

Return

```