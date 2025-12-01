# AVR Internal Hardware

The AVR chips all have internal hardware that can be used.

For this description of the hardware the 90S8515 was used. Newer chips like the Mega8515 may differ and have more or less internal hardware.

You will need to read the manufacturers data sheet for the processor you are using to learn about the special internal hardware available.

Timer / Counters

The AT90S8515 provides two general purpose Timer/Counters - one 8-bit T/C and one 16-bit T/C. The Timer/Counters have individual pre-scaling selection from the same 10-bit pre-scaling timer. Both Timer/Counters can either be used as a timer with an internal clock time base or as a counter with an external pin connection which triggers the counting.

![basc0073](basc0073.jpg)

More about [TIMERO](avr_internal_hardware_timer0.md)

More about [TIMER1](avr_internal_hardware_timer1.md)

[The WATCHDOG Timer](avr_internal_hardware_watchdog_timer.md)

Almost all AVR chips have the ports B and D. The 40 or more pin devices also have ports A and C that also can be used for addressing an external RAM chip ([XRAM](adding_xram.md)). Since all ports are similar except that PORT B and PORT D have alternative functions, only these ports are described.

[PORT B](avr_internal_hardware_port_b.md)

[PORT D](avr_internal_hardware_port_d.md)