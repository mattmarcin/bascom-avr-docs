# IDLE

Action

Put the processor into the idle mode.

Syntax

IDLE

Remarks

In the idle mode, the system clock is removed from the CPU but not from the interrupt logic, the serial port or the timers/counters.

The idle mode is terminated either when an interrupt is received(from the watchdog, timers, external level triggered or ADC) or upon system reset through the RESET pin.

Most new chips have many options for Power down/Idle. It is advised to consult the data sheet to see if a better mode is available.

![notice](notice.jpg)You should use the new [CONFIG POWERMODE ](config_powermode.md)statement.

See also

[POWERDOWN](powerdown.md) , [POWERSAVE](powersave.md) , [POWER mode](power_mode.md)

Example

IDLE