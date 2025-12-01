# $LCDVFO

Action

Instruct the compiler to generate very short Enable pulse for VFO displays.

Syntax

$LCDVFO

Remarks

VFO based displays need a very short Enable pulse. Normal LCD displays need a longer pulse. To support VFO displays this compiler directive has been added.

The display need to be instruction compatible with normal HD44780 based text displays.

Noritake is the biggest manufacturer of VFO displays.

The $LCDVFO directive is intended to be used in combination with the LCD routines.

ASM

NONE

See also

NONE

Example

NONE