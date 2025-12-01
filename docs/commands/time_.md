# TIME$

Action

Internal variable that holds the time.

Syntax

TIME$ = "hh:mm:ss"

var = TIME$

Remarks

The TIME$ variable is used in combination with the CONFIG CLOCK and CONFIG DATE directive.

See [CONFIG CLOCK](config_clock.md) statement for further information. In this interrupt routine the _Sec, _Min and _Hour variables are updated. The time format is 24 hours format.

When you assign TIME$ to a string variable these variables are assigned to the TIME$ variable.

When you assign the TIME$ variable with a constant or other variable, the _sec, _Hour and _Min variables will be changed to the new time.

The only difference with VB is that all digits must be provided when assigning the time. This is done for minimal code. You can change this behavior of course.

![important](important.jpg) Do not confuse TIME$ with the TIME function !

ASM

The following asm routines are called from mcs.lib.

When assigning TIME$ : _set_time (calls _str2byte)

When reading TIME$ : _make_dt (calls _byte2str)

See also

[DATE$](date_.md) , [CONFIG CLOCK](config_clock.md) , [CONFIG DATE](config_date.md)

Example

See the sample of [DATE$](date_.md)