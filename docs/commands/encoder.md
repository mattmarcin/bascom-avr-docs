# ENCODER

Action

Reads pulses from a rotary encoder.

Syntax

Var = ENCODER( pin1, pin2, LeftLabel, RightLabel , wait)

Remarks

Var | The target variable that is assigned with the result. This should be a byte. This byte is used to maintain the state.  
---|---  
Pin1 and pin2 | These are the names of the PIN registers to which the output of the encoder is connected. Both pins must be on the same PIN register. So Pinb.0 and Pinb.7 is valid while PinB.0 and PinA.0 is not.  
LeftLabel | The name of the label that will be called/executed when a transition to the left is encountered.  
RightLabel | The name of the label that will be called/executed when a transition to the right is encountered.  
wait | A value of 0 will only check for a rotation/pulse. While a value of 1 will wait until a user actual turns the encoder. A value of 1 will thus halt your program.  
  
There are some conditions you need to fulfill :

•| The label that is called by the encoder must be terminated by a RETURN statement.  
---|---  
  
•| The pin must work in the input mode. By default all pins work in input mode.  
---|---  
  
•| The pull up resistors must be activated by writing a logic 1 to the port registers as the example shows.  
---|---  
  
Rotary encoders come in many flavors. Some encoders also have a build in switch.

A sample of an encoder

![rotary_encoder](rotary_encoder.gif)

![rotary2](rotary2.gif)

Since the microprocessor has internal pull up resistors, you do not need external pull up resistors for most encoders.

An encoder has 2 output pins which change state when you turn the knob. For one 'click' you can get one or more pulses. This depends on the model of the encoder. Both output pins are sampled and compared with their previous value.

![encoder_state](encoder_state.png)

The table above show the states when rotating left and right. For example, when you turn left, the encoder will change state from 00 to 10 to 11 to 01 to 00 etc.

The software loads the pin values and compares the value with the previous value.

Only if you turn the knob there will be a different value. 

Next the old state nibbles are swapped so that for example state 0000_0011 becomes 0011_0000 and the new state is added to this value. For a left rotation you get the values 2,35,49 and 16. In all other cases, the rotation was right.

When you call the encoder routine often enough, you will not miss any pulses. Most new processors support the pin change interrupt. This means that an interrupt occurs when the logic level of a pin changes. you can use this interrupt to call the encoder function. This way you can be sure you will not miss a pulse.

The example will just show the direction but the idea is that you can increase or decrease a variable in these routines. For example for volume. 

Example

```vb
'-----------------------------------------------------------------------------------------

'name : encoder.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of encoder function

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'An encoder has 2 outputs and a ground

'We connect the outputs to pinb.0 and pinb.1

'You may choose different pins as long as they are at the same PORT

'The pins must be configured to work as input pins

'This function works for all PIN registers

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Print "Encoder test"

Dim B As Byte

'we have dimmed a byte because we need to maintain the state of the encoder

```
Portb = &B11 ' activate pull up registers

Do

B = Encoder(pinb.0 , Pinb.1 , Links , Rechts , 1)

```vb
' ^--- 1 means wait for change which blocks programflow

' ^--------^---------- labels which are called

' ^-------^---------------------------- port PINs

Print B

Waitms 10

Loop

End

'so while you can choose PINB0 and PINB7,they must be both member of PINB

'this works on all PIN registers

```
Links:

```vb
Print "left rotation"

Return

```
Rechts:

```vb
Print "right rotation"

Return

End

```