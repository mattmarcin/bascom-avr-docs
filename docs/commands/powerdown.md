# POWERDOWN

Action

Put processor into power down mode.

Syntax

POWERDOWN

Remarks

In the power down mode, the external oscillator is stopped. The user can use the WATCHDOG to power up the processor when the watchdog timeout expires. Other possibilities to wake up the processor is to give an external reset or to generate an external level triggered interrupt.

![notice](notice.jpg)You should use the new [CONFIG POWERMODE ](config_powermode.md)statement.

See also

[IDLE](idle.md) , [POWERSAVE](powersave.md) , [POWER mode](power_mode.md)

Example

Powerdown