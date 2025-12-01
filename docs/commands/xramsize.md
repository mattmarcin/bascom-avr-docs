# $XRAMSIZE

Action

Specifies the size of the external RAM memory.

Syntax

$XRAMSIZE = [&H] size

Remarks

Size | A constant with the size of the external RAM memory chip.  
---|---  
  
The size of the chip can be selected from the [Options Compiler Chip](options_compiler_chip.md) menu.

The $XRAMSIZE overrides this setting. It is important that $XRAMSTART precedes $XRAMSIZE

See also

[$XRAMSTART](xramstart.md) , [CONFIG XRAM](configxram.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : m128.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrate using $XRAM directive

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 1000000 ' used crystal frequency

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$xramstart = &H1000

$xramsize = &H1000

Dim X As X

```