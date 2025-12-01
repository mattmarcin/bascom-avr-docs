# $WAITSTATE

Action

Compiler directive to activate external SRAM and to insert a WAIT STATE for a slower ALE signal.

![notice](notice.jpg)[CONFIG XRAM ](configxram.md)should be used instead.

Syntax

$WAITSTATE

Remarks

The $WAITSTATE can be used to override the Compiler Chip Options setting.

Wait states are needed for slow external components that can not handle the fast ALE signal from the AVR chip.

See also

[$XA](xa.md) , [CONFIG XRAM](configxram.md)

Example

$WAITSTATE