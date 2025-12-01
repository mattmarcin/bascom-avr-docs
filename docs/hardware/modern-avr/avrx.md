# AVRX

This chapter describes the AVRDBxx processors. To make a distinction between all the different AVR cores , MCS names the DB series the AVRX. This will include all the AVRxxDByy processors and AVRxxDAyy processors.

The difference between the DB and DA series seems to be that DA is missing the MVIO option.

The AVRX processors can be seen as new Xmega processors. They are the big brother of the ATMEGAX (MEGA4809). 

The advantage is that they are cheaper and also run on a voltage between 1v8 and 5V.

The AVRX also has the UPDI interface. It is 24 bit wide since the flash code exceeds the 64KB.

One change compared with other processors is that each pin version has its own ID. This means that the AVR128DB28 (28 pins) and the AVR128DB64 (64 pins) have different ID's.

Since there is one data sheet you need to take good care that the hardware exist in the chip you select. For example, the AVR128DB64 has 6 UARTS. But the AVR128DB28 has 3 UARTS.

From the PDF

The AVR128DB28/32/48/64 microcontrollers of the AVRÂ® DB family of microcontrollers are using the AVRÂ® CPU with

hardware multiplier running at clock speeds up to 24 MHz. They come with 128 KB of Flash, 16 KB of SRAM, and

512 bytes of EEPROM. The microcontrollers are available in 28-, 32-, 48- and 64- pin packages. The AVRÂ® DB

family uses the latest technologies from Microchip with a flexible and low-power architecture, including Event System,

accurate analog subsystems, and advanced digital peripherals.

![avr128dbX](avr128dbx.png)

XTINY/MEGAX

Please read the topics about [XTINY](xtiny.md) and [MEGAX](megax.md). Unless noted the information applies to AVRX as well.

MVIO

We at MCS think that the DB series is great. It is cheap, available in PDIP and has many features.

The DB series has MVIO (Multi Voltage I/O). For the DB series this means that pins or PORTC have a different voltage domain.

You can power the processor from 5V and the MVIO you can power at 3V3. This is great for mixed voltage designs.

Of course you can also connect both domains to the same voltage source.

DAC

There is one DAC with 10 bit resolution.

It can be enabled with the CONFIG statement : config DAC0=ENABLED|DISABLED, OUT_ENABLE=ENABLED|DISABLED, RUNMODE=ENABLED|DISABLED

The DAC has an output pin which can be enabled. 

ADC

There is a 12 bit A/D converter. The input pins depend on the processor model.

The A/D converter has differential channels. Notice that not all input pins can be used for differential input.

ZCD

Also new is the Zero Cross Detector. Up to 3 detectors are available depending on the model.

[Config Zcd0](config_zcdx.md) = Enabled|DISABLED , Runmode = Disabled|ENABLED, INVERT=ENABLED|DISABLED, OUT_ENABLE=ENABLED|DISABLED

We recommend to use an opto coupler with the detector when you interface this with other electronics/voltages.

The interrupt for the ZCD is special. In normal AVR there is a register to enable an interrupt, and some other register might be available to handle specific properties. 

In the AVRX this is all done in the interrupt register. There is only one vector. 

The ENABLE/DISABLE statements have been extended with the options :

```vb
ENABLE ZCD0_BOTH

ENABLE ZCD0_FALLING

ENABLE ZCD0_RISING

```
And the same for DISABLE.

When you enable the ZCD the proper setting will be written to the interrupt register.

When you disable the ZCD, no matter which setting you use, it will disable the interrupt. 

So DISABLE ZCD0_RISING and DISABLE ZCD0_BOTH will have the same effect.

2087

In version 2087 we redesigned the interrupt handling. Interrupts that have multiple settings but only one address get a general name. For ZCD0 this becomes ZCD0_INT

The ENABLE/DISABLE is extended with a section in the DAT file named [ENADISABLE]

When you press ENABLE and CTRL+SPACE you get a list of interrupts you can enable/disable. For ZCD this will be ZDC0_NONE, ZCD0_RISING, ZDC0_FALLING and ZDC0_BOTH.

Only one of the modes can be active at the same time. 

Multiple modes also apply to PIN interrupts. Each port can have 1 interrupt for example PORTD_INT. But each port pin can be enabled/disabled individually to generate an interrupt. 

OPAMP

Also new is the OPAMP. There are up to 3 OPAMP's which can also be connected to each other. The [CONFIG OPAMP](config_opamp.md) has many options. 

TIMERS

There are many timers. All with a different purpose. There are timers of type A(16 bit), B(16 bit) and D(12 bit).

VREGPWR

The Sleep controller also has a voltage regulator control register. [CONFIG VREGPWR](config_vregpwr.md) configures the power options.

All the remaining options are similar to the XTINY and MEGAX series. 

The supported AVRX series are : DA, DB, DD and EA.

See also

[MEGAX](megax.md), [XTINY](xtiny.md)