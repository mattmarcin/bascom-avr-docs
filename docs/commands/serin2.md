# SERIN

This is an alternative library that adds timeout support to the [SERIN](serin.md) statement. Development was sponsored by a customer.

To use this library instead of the default SERIN code, you need to add it to the configuration using the [$LIB](lib.md) directive

```vb
$lib "serin.lib"

Then you need to dimension a DWORD or LONG variable named SERIN_TIMEOUT which is used for the timeout.

```
You assign a time out value to this variable. A higher value will cause a longer time out.

The time out is not in uSec or mSec but relative to the processor speed.

Thus using a clock of 1 Mhz will have a longer time out than a processor clock of 16 MHz.

How it works : The value of SERIN_TIMEOUT is copied to 4 registers. When the software is waiting for a certain bit level, instead of looping, it will decrease the registers and when they reach 0, the code ends. This will prevent that the processor locks up when you have bad signals.

This lib is only available in the full version.