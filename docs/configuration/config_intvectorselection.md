# CONFIG INTVECTORSELECTION

Action

Sets or resets the IVSEL bit to chose the vector table address.

Syntax

```vb
CONFIG INTVECTORSELECTION = enabled|disabled

CONFIG INTVECTORSELECTION = boot|normal

```
Remarks

Some processors with a boot loader have a special register and switch that enables the user to chose the interrupt vector table address.

By default the address is &H0000. When running a boot loader application which requires interrupts, you can use $BOOTVECTOR to create an interrupt vector table (IVR). 

The processor must be forced to load the vector addresses from the boot vector address instead of the default 0000. This is where you use CONFIG INTVECTORSELECTION = enabled.

Instead of 'enabled' you can also use 'boot'. And instead of 'disabled' you may also use 'normal'.

Enabled and disabled describe the status of the IVSEL bit while boot and normal are more clear about the address.

Do not forget to reset the IVSEL bit using CONFIG INTVECTORSELECTION = disabled in your normal application. We advise to use a watchdog time out to reset the processor after the boot loader has finished. This will reset all registers to their defaults and this will disable the IVSEL bit too. 

See Also

[$LOADER](loader.md) , [$BOOTVECTOR](bootvector.md)

Example

See [$LOADER](loader.md)