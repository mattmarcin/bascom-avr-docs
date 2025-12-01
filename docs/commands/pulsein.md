# PULSEIN

Action

Returns the number of units between two occurrences of an edge of a pulse.

Syntax

PULSEIN var , PINX , PIN , STATE

Remarks

var | A word variable that is assigned with the result.  
---|---  
PINX | A PIN register like PIND  
PIN | The pin number(0-7) to get the pulse time of.  
STATE | May be 0 or 1. 0 means sample 0 to 1 transition. 1 means sample 1 to 0 transition.  
  
ERR variable will be set to 1 in case of a time out. A time out will occur after 65535 unit counts. With 10 uS units this will be after 655.35 mS.

You can add a [bitwait](bitwait.md) statement to be sure that the PULSEIN statement will wait for the start condition. But when using the BITWAIT statement and the start condition will never occur, your program will stay in a loop.

The PULSIN statement will wait for the specified edge.

When state 0 is used, the routine will wait until the level on the specified input pin is 0. Then a counter is started and stopped until the input level gets 1.

No hardware timer is used. A 16 bit counter is used. It will increase in 10 uS units. But this depends on the XTAL. You can change the library routine to adjust the units.

PULSEIN.LIB

The full version includes a lib named pulsein.lib. It overloads the pulsein statement. This special lib allows to set a custom timeout and delay.

You need to add the following to your code :

const cPulseIn_Timeout = 0 'This is the default timeout value. When you increase the value you will get a shorter time out period.

```vb
dim bPulseIn_Delay as byte : bPulseIn_Delay = 10 'For 10 uS units , the default is 1

$lib "pulsein.lib" 'include the lib to overload the function

```
See also

[PULSEOUT](pulseout.md)

ASM

The following ASM routine is called from mcs.lib

_pulse_in (calls _adjust_pin)

```vb
On entry ZL points to the PINx register , R16 holds the state, R24 holds the pin number to sample.

On return XL + XH hold the 16 bit value.

```
Example

Dim w As Word

pulsein w , PIND , 1 , 0 'detect time from 0 to 1

```vb
print w

End

```