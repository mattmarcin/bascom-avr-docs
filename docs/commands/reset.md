# RESET

Action

Reset a bit to zero.

Syntax

```vb
RESET bit

RESET var.x

RESET var

RESET micro

RESET watchdog

```
Remarks

Bit | Bit or Boolean variable.  
---|---  
Var | A byte, integer, word, long or dword variable.  
X | Bit of variable to clear. Valid values are : 0-7 (byte, registers), 0-15 (Integer/Word) and (0-31) for a Long/Dword  
watchdog | This will reset the Watchdog timer.   
micro | This will reset the processor. Depending on the AVR platform different methods will be used:  
\- XTINY/MEGAX/AVR : Reset controller is used \- XMEGA : Reset controller is used \- AVR : a jump to address 0 is used. This will not reset hardware registers and is not a real reset.  
  
You can also use the constants from the definition file to set or reset a bit.

RESET PORTB.PB7 'will reset pin 7 of portB. This because PB7 is a defined constant in the definition file.

When the bit is not specified, bit 0 will be cleared. 

See also

[SET](set.md) , [TOGGLE](toggle.md)

Example

[SEE SET](set.md)