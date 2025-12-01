# POWER MODE

Action

Put the micro processor in one of the supported power reserving modes. 

Syntax

POWER mode

Remarks

The mode depends on the micro processor.

Some valid options are :

\- IDLE

\- POWERDOWN

\- STANDBY

\- ADCNOISE

\- POWERSAVE

So for standby you would use : POWER STANDBY

It is also possible to use POWERDOWN, IDLE or POWERSAVE. These modes were/are supported by most processors. It is recommended to use the new POWER command because it allows to use more modes.

POWER has nothing to do with the [POWER](power.md)() function.

![notice](notice.jpg)THIS STATEMENT IS NOT RECOMMENDED. Please use [CONFIG POWERMODE ](config_powermode.md)instead.

See also

[IDLE](idle.md), [POWERDOWN](powerdown.md) , [POWERSAVE](powersave.md)

Example

POWER IDLE