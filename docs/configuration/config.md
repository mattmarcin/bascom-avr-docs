# CONFIG

The CONFIG statement is used to configure the various hardware devices.

Some CONFIG statements depend on the processor platform. Since some platforms have unique hardware not found on other platforms.

DIRECTIVE | RE-USABLE | NORMAL AVR | XMEGA | XTINY/MEGAX/AVRX | XMEGA ONLY | XTINY/UPDI ONLY  
---|---|---|---|---|---|---  
[CONFIG 1WIRE](config_1wire.md) | NO | X | X | X |  |   
[CONFIG ACAX|ACBX](config_acxx.md) | YES |  | X |  | X |   
[CONFIG ACI](config_aci.md) | YES | X |  |  |  |   
[CONFIG ACx](config_acix.md) 2083 NEW | YES |  |  | X |  | X  
[CONFIG ADC](config_adc.md) | NO | X |  |  |  |   
[CONFIG ADCA|ADCB](config_adca.md) | YES |  | X |  | X |   
[CONFIG ADC0|ADCx](config_adc0_adcx.md) 2083 NEW | YES |  |  | X |  | X  
[CONFIG ATEMU](config_atemu.md) | NO | X |  |  |  |   
[CONFIG BASE](config_base.md) | NO | X | X | X |  |   
[CONFIG BCCARD](config_bccard.md) | NO | X |  |  |  |   
[CONFIG CANBUS](config_canbusmode.md) | YES | X |  |  |  |   
[CONFIG CANMOB](config_canmob.md) | YES | X |  |  |  |   
[CONFIG CLOCK](config_clock.md) 2083 ENHANCED | NO | X | X | X |  |   
[CONFIG CLOCKDIV](config_clockdiv.md) | YES | X |  |  |  |   
[CONFIG COM1](config_com1.md) 2083 ENHANCED | YES | X | X | X |  |   
[CONFIG COM2](config_com2.md) also COM3 - COM8 | YES | X | X | X |  |   
[CONFIG COMx](configcomx.md) | YES | X | X | X |  |   
[CONFIG DACA|DACB](config_dacx.md) | YES |  | X |  | X |   
[CONFIG DACX](config_dacx2.md) 2083 NEW | YES |  |  | X |  | X  
[CONFIG DATE](config_date.md) | NO | X | X | X |  |   
[CONFIG DCF77](configdcf77.md) | NO | X | X |  |  |   
[CONFIG DEBOUNCE](config_debounce.md) | NO | X | X | X |  |   
[CONFIG DMA](config_dma.md) | YES |  | X |  | X |   
[CONFIG DMACHx](config_dmachx.md) | YES |  | X |  | X |   
[CONFIG DMXSLAVE](config_dmxslave.md) | NO | X | X | X |  |   
[CONFIG DP](config_dp.md) | NO | X | X | X |  |   
[CONFIG EDMA](config_edma.md) |  |  | X |  | x |   
[CONFIG EDMAx](config_edmax.md) |  |  | X |  | x |   
[CONFIG EEPROM](config_eeprom.md) | NO |  | X | X | X |   
[CONFIG ERROR](config_error.md) | NO | X | X | X |  |   
[CONFIG EVENT_SYSTEM](config_event_system.md) XMEGA | YES |  | X |  | X |   
[CONFIG EVENT_SYSTEM](config_event_system_xtiny.md) XTINY 2083 NEW | YES |  |  | X |  | X  
[CONFIG EXTENDED_PORT](config_extended_port.md) | NO | X |  |  |  |   
[CONFIG FT800](config_ft800.md) | NO | X | X | X |  |   
[CONFIG FUSES](config_fuses.md) | NO |  |  | X | X | X  
[CONFIG GRAPHLCD](config_graphlcd.md) | NO | X | X | X |  |   
[CONFIG HITAG](config_hitag.md) | NO | X |  |  |  |   
[CONFIG I2CBUS](config_i2cbus.md) | YES | X | X | X |  |   
[CONFIG I2CDELAY](config_i2cdelay.md) | NO | X |  |  |  |   
[CONFIG I2CSLAVE](config_i2cslave.md) | NO | X | X |  |  |   
[CONFIG INPUT](configinput.md) | NO | X | X | X |  |   
[CONFIG INPUTBIN](config_inputbin.md) | NO | X | X | X |  |   
[CONFIG INTx](config_intx.md) | YES | X | X | X |  |   
[CONFIG INTVECTORSELECTION](config_intvectorselection.md) | YES | X | X | X |  |   
[CONFIG KBD](config_kbd.md) | NO | X | X |  |  |   
[CONFIG KEYBOARD](config_kbd.md) | NO | X | X | X |  |   
[CONFIG LCD](config_lcd.md) | NO | X | X | X |  |   
[CONFIG LCDBUS](config_lcdbus.md) | NO | X | X | X |  |   
[CONFIG LCDMODE](config_lcdmode.md) | NO | X | X | X |  |   
[CONFIG LCDPIN](config_lcdpin.md) | NO | X | X | X |  |   
[CONFIG OPAMP](config_opamp.md) 2085 NEW | YES |  |  | X |  | X  
[CONFIG OSC](config_osc.md) XMEGA | YES |  | X | X |  |   
[CONFIG OSC](config_osc_xtiny.md) XTINY 2085 NEW | YES |  |  | X |  |   
[CONFIG PORT](config_port.md) | YES | X | X | X |  |   
[CONFIG PORT_MUX](config_port_mux.md) 2084 NEW | YES |  |  | X |  | X  
[CONFIG POWERMODE](config_powermode.md) | YES | X | X | X |  |   
[CONFIG POWER_REDUCTION](config_power_reduction.md) | NO |  | X |  | X |   
[CONFIG PRIORITY](config_priority.md) XMEGA | YES |  | X |  | X |   
[CONFIG PRIORITY](config_priority_xtiny.md) XTINY 2083 NEW | YES |  |  | X |  | X  
[CONFIG PRINT](configprint.md) | NO | X | X | X |  |   
[CONFIG PRINTBIN](config_printbin.md) | NO | X | X | X |  |   
[CONFIG PS2EMU](config_ps2emu.md) | NO | X |  |  |  |   
[CONFIG RAINBOW](config_rainbow.md) | NO | X | X | X |  |   
[CONFIG RC5](config_rc5.md) | NO | X |  |  |  |   
[CONFIG RC5SEND](config_rc5send.md) | NO |  |  | X |  | X  
[CONFIG RND](config_rnd.md) | NO | X | X | X |  |   
[CONFIG SERIALIN](config_serialin.md) | NO | X | X | X |  |   
[CONFIG SERIALIN1](config_serialin.md) | NO | X | X |  |  |   
[CONFIG SERIALIN2](config_serialin.md) | NO | X | X |  |  |   
[CONFIG SERIALIN3](config_serialin.md) | NO | X | X |  |  |   
[CONFIG SERIALOUT](config_serialout.md) | NO | X | X |  |  |   
[CONFIG SERIALOUT1](config_serialout.md) | NO | X | X |  |  |   
[CONFIG SERIALOUT2](config_serialout.md) | NO | X | X |  |  |   
[CONFIG SERIALOUT3](config_serialout.md) | NO | X | X |  |  |   
[CONFIG SERVOS](config_servos.md) | NO | X | X |  |  |   
[CONFIG SHIFTIN](config_shiftin.md) | NO | X | X | X |  |   
[CONFIG SINGLE](configsingle.md) | YES | X | X | X |  |   
[CONFIG SDA](config_sda.md) | NO | X | X | X |  |   
[CONFIG SCL](config_scl.md) | NO | X | X | X |  |   
[CONFIG SPI](config_spi.md) | NO | X |  |  |  |   
[CONFIG SPIx](config_spix.md) | YES |  | X | X | X |   
[CONFIG STRCHECK](config_strcheck.md) 2086 NEW | NO | X | X | X |  |   
[CONFIG SUBMODE](config_submode.md) | NO | X | X | X |  |   
[CONFIG SYSCLOCK](config_sysclock.md) XMEGA | YES |  | X |  | X |   
[CONFIG SYSCLOCK](config_sysclock_xtiny.md) XTINY 2083 NEW | YES |  |  | X |  | X  
[CONFIG TCXX](config_tcxx.md) | YES |  | X | X | X |   
[CONFIG TCA0](config_tca0.md) | YES |  |  | X |  | X  
[CONFIG TCB0, TCB1](config_tcb0_tcb1.md) 2084 NEW | YES |  |  | X |  | X  
[CONFIG TCD0](config_tcd0.md) 2084 NEW | YES |  |  | X |  | X  
[CONFIG TCPIP](config_tcpip.md) | NO | X | X | X |  |   
[CONFIG TWI](config_twi.md) | YES | X | X | X |  |   
[CONFIG TWISLAVE](config_twislave.md) | NO | X |  |  |  |   
[CONFIG TWIxSLAVE](config_twixslave.md) | NO |  | X |  | x |   
[CONFIG TIMER0](config_timer0.md) | YES | X |  |  |  |   
[CONFIG TIMER1](config_timer1.md) | YES | X |  |  |  |   
[CONFIG TIMER2 and 3](config_timer2.md) | YES | X |  |  |  |   
[CONFIG USB](config_usb.md) | NO | X |  |  |  |   
[CONFIG USI](config_usi.md) | NO | X |  |  |  |   
[CONFIG VARPTRMODE](config_varptrmode.md) | YES | X | X | X |  |   
[CONFIG VPORT](config_vport.md) | YES |  | X |  | X |   
[CONFIG VREF](config_vref.md) XTINY 2083 NEW | YES |  |  | X |  | X  
[CONFIG VREGPWR](config_vregpwr.md) AVRX 2085 NEW | YES |  |  | X |  | X  
[CONFIG WATCHDOG](config_watchdog.md) | YES | X | X | X |  |   
[CONFIG WAITSUART](config_waitsuart.md) | NO | X | X | X |  |   
[CONFIG X10](config_x10.md) | NO | X |  |  |  |   
[CONFIG XPIN](config_xpin.md) | YES | X | X | X |  |   
[CONFIG XRAM](configxram.md) | YES | X | X |  |  |   
[CONFIG ZCDx](config_zcdx.md) 2085 NEW | YES |  |  | X |  | X  
  
Some CONFIG directives are intended to be used once. Others can be used multiple times. For example you can specify that a port must be set to input after you have specified that it is used as an input.

You cannot change the LCD pins during run time. In that case the last specification will be used or an error message will be displayed.

Some configuration commands are only available to the Xmega. An X in the 'Xmega Only' column indicates that the command can only be used for an Xmega processor.

Some configuration commands are exclusive for the Xtiny processors. An X in the 'Xtiny Only' column indicates that the commands can only be used for an [Xtiny](xtiny.md) processor.

With [XTYINY](xtiny.md) we also mean [MEGAX](megax.md) and [AVRX](avrx.md).

PRESERVE and OVERWRITE

In version 2084 a part of the hard coded option logic is moved to the DAT files.

Some CONFIG statements like CONFIG PORT_MUX have a new value : PRESERVE or OVERWRITE. 

Other CONFIG statements might have an option named REGMODE. This REGMODE option has the same possible values : PRESERVE and OVERWRITE.

So what is this OVERWRITE or PRESERVE about?

When you configure the various options for a piece of hardware, the compiler will convert these options to the proper values and write this to the proper registers.

Only registers that are changed will be written too. But normally the whole register will be written too. 

When a register sets just one option for example the clock speed, that is no problem. But when the register also has a few bits that set other hardware it might become a problem.

When you create the initial CONFIG statement there is no problem since all required bits will be set. But if you want to change a configuration later and you want to change just a single part of the configuration you could erase an option.

Lets add a simple sample. Assume there is a register named REGCTRLA and it has 8 bits. The 3 lower bits are used to set the pre-scaler. The upper 1 bit is used to enable some output pin.

BIT 7 | BIT 6 | BIT 5 | BIT 4 | BIT 3 | BIT 2 | BIT 1 | BIT 0  
---|---|---|---|---|---|---|---  
O | x | x | x | x | S | S | S  
  
The x mean don't care. It does not mean what we write to it.

Now when you would : CONFIG TEST=DUMMY, PRESCALER=2, OUTPUT=ENABLED

Here you configure all the bits in the register. So it is not needed to preserve any bits, the compiler can simply write the proper value to the register.

When REGMODE is not used it is the same as OVERWRITE and the same as : CONFIG TEST=DUMMY, PRESCALER=2, OUTPUT=ENABLED, REGMODE=OVERWRITE

Here all the bits will be written. But also when you use : CONFIG TEST=DUMMY, PRESCALER=2

This has the implicit OVERWRITE. What happens however is that only the prescaler value is provided. Since there is no preservation for other bits, the compiler will write a zero for the P bit. 

And that is why the PRESERVE option exist : it will load the register value, alter it, and write it back. This will use more code.

When you use the default OVERWRITE mode the compiler will try to re-use register values. This also means that the compiler output might vary depending on the settings !

For example when you set an option that need to write to 3 registers, and all registers values are different, 3 registers are loaded with those values and written to the hardware registers.

But when the options you select result in a similar values, it is not needed to load the same value multiple times, and a different register will be used.

So the resulting binary might become bigger/smaller depending on the options.