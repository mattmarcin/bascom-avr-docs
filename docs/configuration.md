# Configuration Directives

> CONFIG directives for hardware initialization

## CONFIG

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

---

## CONFIG 1WIRE

Action

Configure the pin to use for 1WIRE statements and override the compiler setting.

Syntax

CONFIG 1WIRE = pin [, extended=0|1]

Remarks

Pin | The port pin to use such as PORTB.0  
---|---  
extended | An optional constant value of 0 or 1. This is an optional parameter  
  
The CONFIG 1WIRE statement overrides the compiler setting. It is the preferred that you use it. This way the setting is stored in your source code. 

You can configure only one pin for the 1WIRE statements because the idea is that you can attach multiple 1WIRE devices to the 1WIRE bus.

You can however use multiple pins and thus multiple busses. All 1wire commands and functions need the port and pin in that case. A CONFIG 1WIRE statement is not need in that case either.

The 1wire commands and function will automatically set the DDR and PORT register bits to the proper state. You do not need to bring the pins into the right state yourself.

It is important that you use a pull up resistor of 4K7 ohm on the 1wire pin(for 5V VCC). The pull up resistor of the AVR is not sufficient.

Also notice that some 1wire chips also need +5V. 1 wire is just marketing since you need GND anyway. The least is 2 wires and typical you need 3 wires.

Extended

The extended option is only required when you use multiple busses/pins and if these pins mix normal and extended addresses.

Let's clear that up. When the 1wire code was written in 1995 all the port addresses were normal I/O addresses. These are addresses that fit in the I/O space (address < &H60). To save code, register R31 was cleared in the library and the port register was passed in R30.

When Atmel introduced the extended I/O registers with address >&HFF, it was possible to set R31 to a fixed value when the user port was an extended I/O address.

But when you want to mix the addresses, there is no other way then to pass the word address of the I/O register to the library code.

And that is exactly what EXTENDED=1 will do. It will use more code. This support was written for a customer that already made his PCB's. We do advise to use the same port when you use multiple pins. 

ATMEGA128 PORTF

The ATMEGA128 PORTF is split up. Normally, the DDR, PIN and PORT registers are in the same order.

For example : PORTB = &H18 , DDRB = &H17 and PINB = &H16

But PORTF in the MEGA128 is different : PINF = &H00 , PORTF = &H62 , DDRF = &H61

You need a special library named [M128-1wire-PortF.lib](m128_1wire_portf.md) for this processor and port. This library is fixed to portF

See also

[1WRESET](1wreset.md) , [1WREAD](1wread.md) , [1WWRITE](1wwrite.md) , [1WIRECOUNT ](1wirecount.md), [1WRESET](1wreset.md) , [1WSEARCHFIRST](1wsearchfirst.md) , [1WSEARCHNEXT](1wsearchnext.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wire.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wreset, 1wwrite and 1wread()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' pull-up of 4K7 required to VCC from Portb.2

' DS2401 serial button connected to Portb.2

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 8000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'when only bytes are used, use the following lib for smaller code

$lib "mcsbyte.lib"

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

Dim Ar(8) As Byte , A As Byte , I As Byte

Do

Wait 1

```
1wreset 'reset the device

Print Err 'print error 1 if error

1wwrite &H33 'read ROM command

For I = 1 To 8

Ar(i) = 1wread() 'place into array

```vb
Next

'You could also read 8 bytes a time by unremarking the next line

'and by deleting the for next above

'Ar(1) = 1wread(8) 'read 8 bytes

For I = 1 To 8

Print Hex(ar(i)); 'print output

Next

Print 'linefeed

Loop

'NOTE THAT WHEN YOU COMPILE THIS SAMPLE THE CODE WILL RUN TO THIS POINT

'THIS because of the DO LOOP that is never terminated!!!

'New is the possibility to use more than one 1 wire bus

'The following syntax must be used:

For I = 1 To 8

```
Ar(i) = 0 'clear array to see that it works

Next

1wreset Pinb , 2 'use this port and pin for the second device

1wwrite &H33 , 1 , Pinb , 2 'note that now the number of bytes must be specified!

```vb
'1wwrite Ar(1) , 5,pinb,2

'reading is also different

```
Ar(1) = 1wread(8 , Pinb , 2) 'read 8 bytes from portB on pin 2

```vb
For I = 1 To 8

Print Hex(ar(i));

Next

'you could create a loop with a variable for the bit number !

For I = 0 To 3 'for pin 0-3

```
1wreset Pinb , I

1wwrite &H33 , 1 , Pinb , I

Ar(1) = 1wread(8 , Pinb , I)

```vb
For A = 1 To 8

Print Hex(ar(a));

Next

Print

Next

End

```
Xmega Example

```vb
'--------------------------------------------------------------------------------  
'name : XM128-1wire.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates 1wreset, 1wwrite and 1wread()  
'micro : Xm128A1  
'suited for demo : no  
'commercial addon needed : no  
' pull-up of 4K7 required to VCC from Portb.0  
' DS2401 serial button connected to Portb.0  
'--------------------------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
  
$lib "xmega.lib" : $external _xmegafix_clear : $external _xmegafix_rol_r1014  
  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 32 'default use 10 for the SW stack  
$framesize = 32 'default use 40 for the frame space  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
'configure UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
  
'configure 1wire pin  
Config 1wire = Portb.0 'use this pin  
  
Dim Ar(8) As Byte , A As Byte , I As Byte  
  
Print "start"  
  
```
A = 1wirecount()  
```vb
Print A ; " devices found"  
  
'get first  
```
Ar(1) = 1wsearchfirst()  
  
```vb
For I = 1 To 8 'print the number  
Print Hex(ar(i));  
Next  
Print  
  
Do  
'Now search for other devices  
```
Ar(1) = 1wsearchnext() ' get next device  
```vb
For I = 1 To 8  
Print Hex(ar(i));  
Next  
Print  
Loop Until Err = 1  
  
Waitms 2000  
  
  
Do  
```
1wreset 'reset the device  
Print Err 'print error 1 if error  
  
1wwrite &H33 'read ROM command  
```vb
' Ar(1) = 1wread(8) you can use this instead of the code below  
  
For I = 1 To 8  
```
Ar(i) = 1wread() 'place into array  
```vb
Next  
  
For I = 1 To 8  
Print Hex(ar(i)); 'print output  
Next  
Print 'linefeed  
Waitms 1000  
Loop  
  
  
End

```

---

## CONFIG ACAX|ACBX

Action

Configures the Analog Comparator of the Xmega.

Syntax

CONFIG ACXX = state, TRIGGER=trigger, HISPEED=speed, HYSMODE=hys , MUXPLUS=mp , MUXMIN=mm , OUTPUT=otp , SCALE=scale , WINDOW=w , WINTMODE = wint

Remarks

ACXX | The name of the Analog comparator : ACA0,ACA1, ACB0 or ACB1 Some XMEGA chips might not have (all) comparators.   
---|---  
State | ON or OFF. Select ON to turn the comparator on. By default it is off.  
HiSpeed | When ENABLED, the comparator hi speed mode is activated. Default mode is DISABLED.  
Trigger | Specifies which comparator event triggers the analog comparator interrupts. This options are : RISING, FALLING or BOTH / TOGGLE.  
Hysmode | To prevent quick toggling, a hysteresis is built in. You can chose the mode : \- OFF  \- SMALL  \- LARGE  
MuxPlus | This option controls which pin is connected to the positive input of the comparator. Possible values : 0-7, DAC. When you chose 7, DAC will also be used. So 7 and DAC are equivalent.  
MuxMin | This option controls which pin is connected to the negative input of the comparator. Possible values : 0-7, DAC, BANDGAP, SCALER. 0 - connects pin 0 1 - connects pin 1 2 - connects pin 3 ! 3 - connects pin 5 4 - connects pin 7 5 - connects the DAC output (same as DAC option) 6 - connects the BANDGAP voltage (same as BANDGAP option) 7 - connects the SCALER output (same as SCALE option)  
Output | Enabled or Disabled (default). When the output is enabled, the output of the comparator is routed to pin 7 of the port.  For ACA1 the output is routed to the AC1OUT pin if the Xmega supports this.  
Scale | The input voltage of the negative mux pin can be scaled. The scale value must be in range from 0-63. The scale output voltage is calculated as : (vcc * (scale+1)) / 64 Thus a value of 63 would give VCC. And 32 would give vcc/2  
Windows | Enabled or Disabled (default). When enabled, the two comparators of the port (ACA0 + ACA1) or (ACB0 + ACB1) form a window discriminator so you can control if a voltage is in the range of the lower and upper comparator.  
WintMode | The status register contains the window state. (bit 6 and 7). You can also fire an interrupt at one of the states: ABOVE : interrupt on signal above window INSIDE : interrupt on signal inside window BELOW : interrupt on signal below window OUTSIDE : interrupt on signal outside window  
  
A window is used in battery voltage meters. you could set the lower voltage to 12 V. And the upper voltage to 14 V.

```vb
If the voltage is inside this window : >=12V and <=14V then the battery is OK.

If the voltage is below the battery need to be charged.

If the voltage is above the window the battery if fully charged. The mentioned values are just an example.

```
See also

NONE

Example

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-AC.bas  
' This sample demonstrates the Analog Comparator  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
'include the following lib and code, the routines will be replaced since they are a workaround  
$lib "xmega.lib"  
$external _xmegafix_clear  
$external _xmegafix_rol_r1014  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
'setup comparator pin 0 and pin 1 are the input of portA. Pin 7 is an output in this sample  
Config Aca0 = On , Hysmode = Small , Muxplus = 0 , Muxmin = 1 , Output = Enabled  
  
  
  
Do  
Print Bin(aca_status)  
Print Aca_status.4 ' output ac0  
Waitms 1000  
Loop  
  


```

---

## CONFIG ACI

Action

Configures the Analog Comparator.

Syntax

CONFIG ACI = ON|OFF, COMPARE = ON|OFF, TRIGGER=TOGGLE|RISING|FALLING

Remarks

ACI | Can be switched on or off  
---|---  
COMPARE | Can be on or off. When switched ON, the TIMER1 in capture mode will trigger on ACI too.  
TRIGGER | Specifies which comparator events trigger the analog comparator interrupts.  
  
See also

NONE

Example

NONE

---

## CONFIG ACX

Action

Configures the Analog Comparator of the Xtiny.

Syntax

CONFIG ACX = state, RUNMODE=runmode, OUTPUT=otp ,TRIGGER=trigger, LOW_POWER=lowpow, HYSMODE=hys , MUX_INVERT=muxinv , MUXMIN=muxmin , MUXPOS=muxpos

Remarks

ACIX | The name of the Analog comparator : AC0,AC1, AC2. Some XTINY processors have multiple comparators.   
---|---  
State | ON or OFF. Select ON to turn the comparator on. By default it is OFF.  
Runmode | Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
Trigger | Specifies which comparator event triggers the analog comparator interrupts. This options are : RISING, FALLING or BOTH.  
Hysmode | To prevent quick toggling, a hysteresis is built in. You can chose the mode : \- OFF  \- 10 (10 mV) \- 25 (25 mV) \- 50 (50 mV)  
lowpow | ENABLED or DISABLED. When you enable this mode the current through the comparator is reduced. It reduces power consumption but increase the reaction time of the comparator.   
Muxinv | ENABLED or DISABLED (default) When enabled the output of the AC is inverted. This effectively inverts the input to all the peripherals connected to the signal, and also affects the internal status signals.  
Output | ENABLED or DISABLED (default). When the output is enabled, the output of the comparator is routed to the output pin of the port.   
muxmin | Negative input MUX selection. Possible values : \- AINN0 : negative pin 0 \- AINN1 : Negative pin 1 \- VREF : voltage reference \- DAC : DAC output  
muxpos | Positive input MUX selection. Possible values : \- AINP0 : positive PIN 0 (default) \- AINP1 : positive pin 1  
  
See also

NONE

Example

---

## CONFIG ADC

Action

Configures the A/D converter.

Syntax

CONFIG ADC = single, PRESCALER = AUTO, REFERENCE = opt

Remarks

ADC | Running mode. May be SINGLE or FREE. This is the converter mode and has nothing to do with single ended or differential input mode.  
---|---  
PRESCALER | A numeric constant for the clock divider. Use AUTO to let the compiler generate the best value depending on the XTAL  
REFERENCE | The options depend on the used micro. Some chips like the M163 have additional reference options. In the definition files you will find : ADC_REFMODEL = x This specifies which reference options are available. The possible values are listed in the table below.  
  
Chip | Modes | ADC_REFMODEL  
---|---|---  
2233,4433,4434,8535,m103,m603, m128103 | OFF AVCC | 0  
m165, m169, m325,m3250, m645, m6450, m329,m3290, m649, m6490,m48,m88,m168 | OFF AVCC INTERNAL or INTERNAL_1.1 | 1  
tiny15,tiny26 | AVCC OFF INTERNAL INTERNALEXTCAP | 2  
tiny13 | AVCC INTERNAL | 3  
tiny24,tiny44,tiny84 | AVCC EXTERNAL or OFF INTERNAL or INTERNAL_1.1 | 4  
m164,m324,m644,m640,m1280, m1281,m2561,m2560 | AREF or OFF AVCC INTERNAL1.1 INTERNAL_2.56 | 5  
tiny261,tiny461,tiny861, tiny25,tiny45,tiny85 | AVCC EXTERNAL or OFF INTERNAL_1.1 INTERNAL_2.56_NOCAP INTERNAL_2.56_EXTCAP | 7  
CAN128, PWM2_3,USB1287, m128, m16, m163, m32, m323, m64 | AREF or OFF AVCC INTERNAL or INTERNAL_2.56 | 8  

| You may also use VALUE=value |   
  
  
When you use VALUE=value, you may specify any value. The disadvantage is that when you port your code from one chip to another it will not work.

While the AREF, AVCC, etc. are all converted to the right settings, the value can not be converted. 

The AD converter is started automatic when you use the CONFIG ADC command.

You can use [STOP](stop.md) ADC and [START](start.md) ADC to disable and enable the power of the AD converter.

The [GETADC](getadc.md)() function is intended to be used with the SINGLE running mode. This means that each time you call GETADC(), a conversion is started. If you use the free running mode, you need to retrieve the value from the AD converter yourself. For example by reading the internal ADC word variable.

See also

[GETADC](getadc.md) , [CONFIG ADCx](config_adca.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : adc.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of GETADC() function for 8535 or M163 micro

'micro : Mega163

'suited for demo : yes

'commercial addon needed : no

'use in simulator : possible

' Getadc() will also work for other AVR chips that have an ADC converter

'--------------------------------------------------------------------------------

$regfile = "m163def.dat" ' we use the M163

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'configure single mode and auto prescaler setting

'The single mode must be used with the GETADC() function

'The prescaler divides the internal clock by 2,4,8,16,32,64 or 128

'Because the ADC needs a clock from 50-200 KHz

'The AUTO feature, will select the highest clockrate possible

Config Adc = Single , Prescaler = Auto

'Now give power to the chip

```
Start Adc ' NOT required since it will start automatic

```vb
'With STOP ADC, you can remove the power from the chip

'Stop Adc

Dim W As Word , Channel As Byte

```
Channel = 0

```vb
'now read A/D value from channel 0

Do

```
W = Getadc(channel)

Print "Channel " ; Channel ; " value " ; W

Incr Channel

```vb
If Channel > 7 Then Channel = 0

Loop

End

'The new M163 has options for the reference voltage

'For this chip you can use the additional param :

'Config Adc = Single , Prescaler = Auto, Reference = Internal

'The reference param may be :

'OFF : AREF, internal reference turned off

'AVCC : AVCC, with external capacitor at AREF pin

'INTERNAL : Internal 2.56 voltage reference with external capacitor ar AREF pin

'Using the additional param on chip that do not have the internal reference will have no effect.

```

---

## CONFIG ADC0-ADCX

Action

Configures the A/D converter of the Xtiny

Syntax

CONFIG ADC0 | ADCx = mode, RUNMODE=runmode, RESOLUTION=res, ADC=adc, SAMPLE_ACCU=samp_acc, SAMPLE_CAP=samp_cap, SAMPLE_DELAY=samp_dly, SAMPLE_LEN=samp_len,

REFERENCE=ref,PRESCALER=pre, INIT_DELAY=init_dly,ASDV=asdv,WINDOW_COMP=win_cmp, MUX=mux

Remarks

mode | AD converter mode. \- SINGLE (default mode for a single conversion) \- FREE. In FREE mode a new conversion cycle is started immediately after a previous conversion has completed.   
---|---  
runmode | Possible values: ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
res | The resolution of the conversion. Valid values are : \- 8BIT \- 10BIT. This is the default  
adc | ENABLED or DISABLED. By default the AD converter is DISABLED.  
samp_acc | This value selects how many consecutive ADC sampling results are accumulated automatically. Possible values : \- 0 : (accumulation disabled, default value) \- 2, 4,8,16,32,64 : number of accumulated samples.  
samp_cap | Sample capacitance selection.  Possible values : \- BELOW_1V : Recommended for reference voltage values below 1V. \- ABOVE_1V : Reduced size of sampling capacitance. Recommended for higher reference voltages.  
samp_dly | Sampling Delay Selection : Numeric constant between 0 and 15. These bits define the delay between consecutive ADC samples. The programmable Sampling Delay allows modifying the sampling frequency during hardware accumulation, to suppress periodic noise sources that may otherwise disturb the sampling. The SAMPDLY field can be also modified automatically from sampling cycle to another, by setting the ASDV bit. The delay is expressed as CLK_ADC cycles and is given directly by the bitfield setting. The sampling cap is kept open during the delay.  
samp_len | Sample Length. Numeric constant between 0 and 31. These bits extend the ADC sampling length in number of CLK_ADC cycles. By default the sampling time is two CLK_ADC cycles. Increasing the sampling length allows sampling sources with higher impedance. The total conversion time increased with the selected sampling length.  
ref | Voltage Reference selection. Possible values : \- INTERNAL : internal reference. See CONFIG VREF \- VDD : VDD  
prescale | Prescaler selection. This is the division from the peripheral clock to the ADC clock. Possible values : 2,4,8,16,32,64,128,256  
init_dly | Initialization delay. These bits defines the initialization/startup delay before the first sample when enabling the ADC or changing to internal reference voltage. Setting this delay will ensure that the reference, muxes, etc are ready before starting the first conversion. The initialization delay will also take place when waking up from deep sleep to do a measurement. The delay is expressed as a number of CLK_ADC cycles. Possible values : \- 0 : Delay 0 CLK_CYCLES (no delay) \- 16 : Delay 16 CLK_CYCLES \- 32 : Delay 32 CLK_CYCLES \- 64 : Delay 64 CLK_CYCLES \- 128 : Delay 128 CLK_CYCLES \- 256 : Delay 256 CLK_CYCLES  
asdv | Automatic Sampling Delay Variation. ENABLED or DISABLED. Selecting ENABLED, enables automatic sampling delay variation between ADC conversions. The purpose of varying sampling instant is to randomize the sampling instant and thus avoid standing frequency components in frequency spectrum. The value of the SAMPDLY bits is automatically incremented by one after each sample. When the Automatic Sampling Delay Variation is enabled and the SAMPDLY value reaches &HF, it wraps around to 0.  
win_cmp | Window Comparator Mode. This field enables and defines when the interrupt flag is set in Window Comparator mode. RESULT is the 16-bit accumulator result. WINLT and WINHT are 16-bit lower threshold value and 16-bit higher threshold value, respectively. Possible values : \- NONE : No windows comparison (default) \- BELOW : result < WINLT \- ABOVE : result > WINHT \- INSIDE : WINLT < result < WINHT \- OUTSIDE : result < WINLT or result > WINHT  
mux | Mux position. This bit field selects which single-ended analog input is connected to the ADC. If these bits are changed during a conversion, the change will not take effect until this conversion is complete. Possible values : \- GND : 0V, GND \- TEMPSENSE : Temperature sensor \- INTREF : Internal reference (from VREF) \- DAC0 : DAC0 output 0-11 : ADC input pin 0-11  
  
The MUX value is an optional initial value.This value writes to the ADC0_MUXPOS register. The GETADC() function will also write to this register.

See Also

[CONFIG VREF](config_vref.md) , [GETADC](getadc.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name : adc.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates ADC and DAC. Notice that DAC is not available on all processors  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'configre the internal reference to be 1v1 for both the ADC and the DAC  
Config Vref = Dummy , Adc0 = 1v1 , Dac0 = 1v1  
  
'configure the ADC0 to read the DAC  
Config Adc0 = Single , Resolution = 10bit , Adc = Enabled , Reference = Internal , Prescaler = 32 , Sample_len = 1 , Sample_cap = Above_1v , Init_delay = 32 , Mux = Dac0  
  
'configure the DAC. We do not output the signal on a port pin otherwise out_enable would be required too  
Config Dac0 = Enabled  
  
'dimension a variable  
Dim W As Word  
  
Print "Test ADC"  
  
'set the DAC to halve the output which would be halve of 1.1V which is 0.55V  
```
Dac0_data = 127  
  
```vb
Do  
'when getadc() does not have parameters, it will use the current mux setting  
'other options are : getadc(channel) and getadc(adc0 | adc1 , channel)  
```
W = Getadc() : Print "W:" ; W  
```vb
'output should be 512  
Waitms 1000  
Loop  
  
End

```

---

## CONFIG ADCA|ADCB

Action

Configures the A/D converter of the Xmega.

See also [ATXMEGA](atxmega.md) for base info on ATXMEGA.

Syntax

CONFIG ADCA | ADCB = mode, CONVMODE=sign, RESOLUTION=res, DMA=dma, REFERENCE=ref,EVENT_MODE=evt, EVENT_CHANNEL=evtchan, PRESCALER=pre, BANDGAP=gap, TEMPREF=tref, SWEEP=sweep, CH0_GAIN=gain, CH0_INP= inp, MUX0=mux, CH1_GAIN=gain, CH1_INP= inp, MUX1=mux , CH2_GAIN=gain, CH2_INP= inp, MUX2=mux, CH3_GAIN=gain, CH3_INP= inp, MUX3=mux

Remarks

mode | Running mode. May be SINGLE or FREE.  
---|---  
sign | The conversion mode. This can be SIGNED or UNSIGNED. When choosing SIGNED you should assign the result to an integer. When choosing UNSIGNED you should assign the result to a word. The default is UNSIGNED. When the ADC uses differential input, SIGNED mode must be used, when using single ended input both signed or UNSIGNED mode can be used. Note: | •| Conversion mode is configured for the whole ADC, not individually for each channel, which means that the ADC must be put in the signed mode even if only one of the channels uses differential inputs.  
---|---  
  
•| Negative values are not negative inputs on the IO pins, but higher voltage level on the negative input in respect to the positive input. Even though the resulting value can be negative. For example +1.4 V on negative Input and +0.3 V on positive input is OK.  
---|---  
  
•| Do not apply Voltages below GND or above VCC !!  
---|---  
  
res | The resolution of the conversion. Valid values are : \- 8BIT \- 12BIT. This is the default \- LEFT12BIT. This will result in a left aligned 21 bit value.  
dma | If you want to use the DMA channel, you can select which DMA channels must be used: \- OFF (no DMA) \- CH01 (channel 0 + 1) \- CH012 (channel 0 + 1 + 2) \- CH0123 (channel 0 + 1 + 2 + 3)  
ref | Selects the reference to use. Valid options : \- INT1V. For internal 1V reference \- INTVCC. For internal voltage divided by 1.6 \- AREFA. External reference from AREF pin on PORT A. \- AREFB. External reference from AREF pin on PORT B.  
gap | Enables the bangap reference. Use ENABLED or DISABLED. Setting this bit enables the bandgap to prepare for ADC measurement. Note that if any other functions are using the bandgap already, this bit does not need to be set. This could be when the internal 1V reference is used in ADC or DAC, or if the Brown-out Detector is enabled.  
tref | Enables the temperature reference. Use ENABLED or DISABLED. Setting this bit enables the temperature reference to prepare for ADC measurement  
sweep | Selects which channels are included in a sweep when a channel sweep is triggered by the event system or in the free running mode. Valid options : \- CH0 : channel 0 included \- CH01 : channel 0 and 1 included \- CH012 : channel 0-2 included \- CH0123 : all channels are included   
evtchan | Event channel selection. This selects which channel should trigger which ADC channel. Valid options: \- CH0123. Event channel 0, 1, 2, 3 as selected inputs \- CH1234. Event channel 1, 2, 3, 4 as selected inputs \- CH2345. Event channel 2,3, 4, 5 as selected inputs \- CH3456. Event channel 3, 4, 5, 6 as selected inputs \- CH4567. Event channel 4, 5, 6, 7 as selected inputs \- CH456. Event channel 4, 5, 6 as selected inputs \- CH67. Event channel 6 and 7 as selected inputs \- CH7. Event channel 7 as selected input  
evt | Event channel mode selection. This selects how many of the selected event channel are in use. Valid options: \- NONE. Event system is not used \- CH0. Event channel with the lowest number, defined by evtchan triggers conversion on channel 0 \- CH01. Event channel with the two lowest numbers, defined by evtchan trigger conversion on channel 0 and 1 respectively \- CH012. Event channel with the three lowest numbers, defined by evtchan trigger conversion on channel 0, 1 and 2 respectively \- CH0123. Event channel defined by evtchan trigger conversion on channel 0, 1, 2 and 3 respectively \- SWEEP. One sweep of all active ADC channels defined by SWEEP on incoming event channel with the lowest number, defined by evtchan \- SYNCSWEEP. One sweep of all active ADC channels defined by SWEEP on incoming event channel with the lowest number, defined by evtchan. In addition, the conversion will be synchronized on event to ensure a very accurate timing for the conversion.  
pre | Prescaler value. The prescaler divides the system clock and applies it to the A/D converter.  Valid prescaler values : \- 4, 8, 16, 32, 64, 128, 256 and 512  
gain | Each of the 4 channels can have a different gain. Valid values are : 1,2,4,8,16,32 and 64  
inp | Each of the 4 channels can have a different mode. The 4 modes are : \- INTERNAL. For example for temperature measurement \- SINGLE_ENDED. For measuring positive voltages \- DIFF. For differential input without gain which allows to measure negative voltages. \- DIFFWGAIN. Same as DIFF but with gain.  
mux | Selects the MUX to use with the channel. This must be a numeric constant. The value depends on the mode. See details below under How to select the MUX to use with the channel. At run time you can change the ADCx_CHy_MUXCTRL register. Where x is A or B, and y is the channel 0-3.  
  
XMEGA chips are grouped into different families. For example the features of an A-family device differ from a B-family or D-family device.

An example for a A-family device is ATXMEGA128A1.

The following table show the differences of the different XMEGA families:

  
| AVR XMEGA A | AVR XMEGA B | AVR XMEGA D  
---|---|---|---  
ADCA | Yes | Yes | Yes  
ADCB | Yes | Yes | \- -  
Channel 0 | Yes | Yes | Yes  
Channel 1 | Yes | \- - | \- -  
Channel 2 | Yes | \- - | \- -  
Channel 3 | Yes | \- - | \- -  
Architecture | Pipelined | Cyclic | Cyclic  
Max ADC frequency | 2MHz | 1.4Mhz | 1.4MHz  
Single propagation ADC cycles number (12 bits) | 7 | 7 | 7  
Single propagation ADC cycles number (8 bits) | 5 | 5 | 5  
Max sample per second (12 bits) | 2Msps | 200Ksps | 200Ksps  
ADC result to DMA | Yes | Yes | \- -   
SWEEP mode (channel sweep) | Yes | \- -  | \- -  
Number of Internal inputs | 4 | 3 | 3  
Internal inputs | Temp, Vcc/10, Bandgap, DAC | Temp, Vcc/10, Bandgap | Temp, Vcc/10, Bandgap  
x 0.5 Gain | \- -  | Yes | \- -   
Voltage reference = INTVCC/2 | \- -  | Yes | \- -   
  
The XMEGA A-family ADC conversion block has a 12-stage pipelined architecture capable of sampling several signals almost parallel. There are four input selection multiplexers with individual configurations. The separate configuration settings for the four multiplexers can be

viewed as virtual channels, with one set of result registers each, all sharing the same ADC conversion block. 

ADC overview of XMEGA AU (Xmega with USB):

![config_adcx_overview](config_adcx_overview.png)

So with the pipelined structure, four basic elements (Virtual Channels) can be used at the same time.

Each signal propagates through the 12-stage pipelined ADC Block (12-stage for 12-Bit), where one bit is converted at each stage.

The propagation time for one single 12-Bit signal conversion through the pipeline is 7 ADC clock cycles for 12-bit conversions. If Gain

is used the propagation time increases by one cycle.

When free running mode is configured an ADC channel will continuously sample and do new conversions.

12-Bit = [MSB , Bit 10 , Bit 9 , Bit 8, Bit 7 , Bit 6, Bit 5, Bit 4, Bit 3, Bit 2, Bit 1, LSB]

If 4 Virtual ADC Channels are used the pipelined architecture will work as following:

ADC Clock Cycle 1: Start Ch0 without gain

ADC Clock Cycle 2: Channel 0 MSB (Bit11)

ADC Clock Cycle 3: Channel 0 Bit9, Channel 1 MSB

ADC Clock Cycle 4: Channel 0 Bit7, Channel 1 Bit9, Channel 2 MSB

ADC Clock Cycle 5: Channel 0 Bit5, Channel 1 Bit7, Channel 2 Bit9, Channel 3 MSB

ADC Clock Cycle 6: Channel 0 Bit3, Channel 2 Bit5, Channel 2 Bit7, Channel 3 Bit9

ADC Clock Cycle 7: Channel 0 Bit1, Channel 2 Bit3, Channel 2 Bit5, Channel 3 Bit7

ADC Clock Cycle 8: Channel 0 LSB

ADC Clock Cycle 9: Channel 0 conversion complete ......

ADC Clock Cycle 10 Channel 1 conversion complete ....

....

.....

The even elements (0, 2, 4 â¦) of 12-stage pipelined ADC Block will be enabled during the high level of the ADC

clock, and the odd elements (1, 3 , 5 â¦) of 12-stage pipelined ADC Block will be enabled during the low level of the

ADC clock.

After four ADC clock cycles all 4 ADC channels have done the first sample bit (the MSB).

![config_adcx_propagation_4ch](config_adcx_propagation_4ch.png)

```vb
For further details see Atmel Application Notes and data sheets.

If real simultaneous conversions are needed on different channels then you need to use 2 ADC's. For example Channel 0 of ADCA and Channel 0 of ADCB an A-family device can be measured absolute simultaneously.

```
Selectable voltage input types:

â¢ Differential measurement without gain

The ADC must be in signed mode when differential input is used

Pin 0...Pin 7 can be selected as positive input

Pin 0...Pin 3 can be sleected as negative input

```vb
'  
' +--------------+  
' | |  
' Pina.0 -----+ differnential|  
' | without gain |  
' | |  
' Pina.1 -----+ ADC |  
' | |  
' +--------------+  
'

```
•| Differential measurement with gain  
---|---  
  
The gain is selectable to 1/2x, 1x, 2x, 4x, 8x, 16x, 32x and 64x gain

The ADC must be in signed mode when differential input is used

Pin 0...Pin 7 can be selected as positive input

Pin 4...Pin 7 can be sleected as negative input

```vb
'  
' +--------------+  
' | |  
' Pina.0 -----+ differnential|  
' | with gain |  
' | |  
' Pina.4 -----+ ADC |  
' | |  
' +--------------+  
'

```
â¢ Single ended input (signed mode)

The ADC is differential, so for single ended measurements the negative input is connected to a fixed internal value.

The negative input is connected to internal ground (GND) in signed mode.

```vb
'  
' +--------------+  
' | |  
' Vinp -----+ single ended |  
' | signed mode |  
' | |  
' GND -----+ ADC |  
' | |  
' +--------------+  
'

```
•| Single ended input (unsigned mode)  
---|---  
  
In unsigned mode the negative input is connected to half of the voltage reference (Vref) voltage minus a fixed device specific negative offset

The approximate value corresponding to ground is around 200. This value corresponds to the digital result of ÎV (0.05 * 4096).

This value also depend on the selected voltage reference so you should measure the real value by first selecting the voltage reference.

(ÎV = Vref * 0.05)

How to measure the offset ? 

Connect the ADC input pin (Vinp) to GND and measure the offset.

This is also called offset calibration. This value can be stored for example in EEPROM and is therefore available for all other measurements.

See also example below.

This offset calibration value is then subtracted to each ADC output

The offset enables the ADC to measure for example zero crossing in unsigned mode.

```vb
'  
' +--------------+  
' | |  
' Vinp -----+ single ended |  
' | unsigned mode|  
' | |  
' (Vref/2)-dV -----+ ADC |  
' | |  
' +--------------+  
'

```
â¢ Internal input 

The ADC is differential, so for single ended measurements the negative input is connected to a fixed internal value

How to select the MUX to use with the channel

Mux0 = &B0_0000_000

Bit 0...2 of MUX0 = MUX selection on negative ADC input (For internal or single-ended measurements, these bits are not in use.)

Bit 3...6 of MUX0 = MUX selection on Positive ADC input

Input mode = INTERNAL:

MUX POSITIVE INPUT | Group Configuration | Description  
---|---|---  
0000 | TEMP | Temperature Reference  
0001 | Bandgap | Bandgap voltage  
0010 | SCALEDVCC | 1/10 scaled Vcc  
0011 | DAC | DAC output  
  
For example:

W = Getadc(adcb , 0 , &B0_0011_000) 'Measure DAC

Another example:

Ch0_gain = 1 , Ch0_inp = INTERNAL , Mux0 = &B0_0011_000 'configure MUX0 to measure internal DAC

Input mode =  SINGLE_ENDED, DIFF or DIFFWGAIN:

MUX POSITIVE INPUT | Group Configuration | Description  
---|---|---  
0000 | Pin0 | ADC0  
0001 | Pin1 |   
0010 | Pin2 |   
0011 | Pin3 |   
0100 | Pin4 |   
0101 | Pin5 |   
0110 | Pin6 |   
0111 | Pin7 |   
1000 | Pin8 |   
1001 | Pin9 |   
1010 | Pin10 |   
1011 | Pin11 |   
1100 | Pin12 |   
1101 | Pin13 |   
1110 | Pin14 |   
1111 | Pin15 | ADC15  
  
Input mode =  DIFF:

MUX NEGATIVE INPUT | Group Configuration | Description  
---|---|---  
000 | Pin0 | ADC0  
001 | Pin1 |   
010 | Pin2 |   
011 | Pin3 | ADC3  
100 | reserved | reserved  
101 | GND |   
110 | reserved | reserved  
111 | INTGND | inernal GND  
  
Input mode = DIFFWGAIN:

MUX NEGATIVE INPUT | Group Configuration | Description  
---|---|---  
000 | Pin4 | ADC0  
001 | Pin5 |   
010 | Pin6 |   
011 | Pin7 | ADC3  
100 | INTGND | internal GND  
101 | reserved | reserved  
110 | reserved | reserved  
111 | GND | GND  
  
Example:

Ch1_gain = 1 , Ch1_inp = Diffwgain , Mux1 = &B0_0001_001

Positive Input = PIN1

Negative Input = PIN5

Calculation of ADC Value:

G = Gain

TOP with 12-bit resolution:

•|  TOP value of a signed result is 2047 and the results will be in the range -2048 to +2047 (0xF800 - 0x07FF). This is 11-bit plus sign bit (+ or -).  
---|---  
  
•|  TOP value of of an unsigned result is 4095 and the results will be in the range 0 to +4095 (0x0 - 0x0FFF). This is 12-bit.  
---|---  
  
For single ended and internal measurements GAIN is always 1 and Vinp is internal Ground.

In signed mode, negative and positive results are generated:

Vinp and Vinn = the positive and negative inputs to the ADC

ADC Resolution = ((Vinp - Vinn)/Vref) * G * (TOP + 1)

Example for signed differential input (with gain): 

TOP = 2047

Vinp = +0.3V

Vinn = +1.4V

Vref = Vcc/1.6 = 3.3V/1.6 = 2.0625

G = 1

ADC Resolution = ((Vinp - Vinn)/Vref) * G * (TOP + 1)

ADC Resolution = ((0.3 - 1.4)/2.0625) * 1 * (2047 + 1)

ADC Resolution = - 1092

Example for unsigned single ended:

TOP = 4095

Vinp = +1.0V

Vref = 3.323Volt/1.6 = 2.076875

ÎV = Vref * 0.05 = 2.0625 * 0.05 = 103.1mV

G = 1

ADC Resolution = ((Vinp - (-ÎV))/Vref) * G * (TOP + 1)

ADC Resolution = ((1.0 + 0.103125)/2.076875) * 1 * (4095 + 1)

ADC Resolution = 2175

The offset needs to be subtracted to get the right value.

See also example below where the real ADC Resolution was output over terminal with the ATXMEGA256A3BU (Measure Offset in Single Ended Unsigned Mode).

ADC Compare function

Another feature of XMEGA ADC is a 12-bit compare function. The ADC compare register can hold a 12-bit value that represents a threshold voltage. Each ADC Channel can be configured to automatically compare its result with this compare value to give an interrupt or event only when the result is above or below the threshold. All four ADC Channels share the same compare register but you can decide which ADC channel is working in compare mode.

For ADC A you need to set register ADCA_CMP and configure the interrupt.

The used interrupt for this feature is the ADC conversion complete interrupt of the according channel which will (when configured in compare mode) only fire when the compare condition is met.

To configure the interrupt for example for ADC A Channel 0 the register ADCA_CH0_INTCTRL need to be set to:

•| Compare Result Below Threshold  
---|---  
  
•| Compare Result Above Threshold  
---|---  
  
instead of a conversion complete interrupt.

ADC Calibration:

The production signature row offers several bytes for ADC calibration. The ADC is calibrated during production testing, and the calibration value must be loaded from the signature row into the ADC registers (CAL registers).

Register ADCA_CALL = Low Byte of calibration value

Register ADCA_CALH = High Byte of calibration value

The calibration corrects the capacitor mismatch of the switched capacitor technology.

This ADC calibration value copy should be done in a setup routine before using the ADC.

See also [READSIG](readsig.md) (reads a byte from the signature area in the XMEGA)

ADC Clock Frequency

The ADC clock need to be set within the recommended speed limits for the ADC module to guarantee correct operation.

For example for a ATXMEGA A4U device the minimum is 100Khz and the maximum is 2MHz (for internal signals like internal temp the max. value is 125KHz). The ADC clock is derived from a prescaled version of the XMEGA peripheral clock which is set with the Prescaler value paramter.

Don't confuse ADC Clock frequency with ADC conversion speed. So even if you set the ADC Clock frequency to 2MHz you can sample at a rate of for example 20KHz !

Because the maximum ADC Clock Frequency is 1/4 of the peripheral clock of an ATXMEGA you can not sample at a rate higher than one fourth of the system clock speed.

![notice](notice.jpg)Take care on the source impedance of the analog signal source. If the source impedance is too high, the internal sampling

capacitor will not be charged to the correct level and the result will not be accurate.

In Atmel application Note AVR1300 you find details regarding sample rate vs. source impedance of analog signal source.

Additional Best Practise

Some additional best practise to use ADC with XMEGA:

•| Switch off unused peripheral parts with [CONFIG POWER_REDUCTION](config_power_reduction.md) to eliminate noise.  
---|---  
  
•| Put the XMEGA in the âIdleâ sleep mode directly after starting the ADC conversion to reduce noise from the CPU  
---|---  
  
•| Use the lowest gain possible to avoid amplifying external noise  
---|---  
  
•| Apply offset and gain calibration to the measurement  
---|---  
  
External Voltage Reference (REFA and REFB)

The internal reference voltages like INT1V is derived from the bandgap voltage. Parameter like gain error of bandgap voltage can be found in the device data sheet.

An external voltage reference can be more accurate compared to the internal voltage reference but is depending on the external circuit. The max. voltage for external ref on REFA pin (with ADC A this is PINA.0) is Vrefmax = Vcc - 0.6V so with Vcc=3.3V this is 2.7V. And external Vref must be at least 1V.

![notice](notice.jpg)The external reference pin AREFA or AREFB is shared with the DAC module !

See also Atmel Application Note AVR1012: XMEGA A Schematic Checklist

```vb
For example a reference diode (like LM336-2.5V) can be used or a shunt voltage reference like LM4040 as external reference.

For Maximum Performance use Event System and DMA Controller combined with ADC

```
See [config DMA](config_dma.md), [config DMAchx](config_dmachx.md), [config Event_System](config_event_system.md)

See also

[GETADC](getadc.md) , [CONFIG ADC](config_adc.md), [ATXMEGA](atxmega.md)

Example for Single Conversion:

```vb
'--------------------------------------------------------------------------------

'setup the ADC-A converter

Config Adca = Single , Convmode = Unsigned , Resolution = 12bit , Dma = Off , Reference = Int1v , Event_mode = None , Prescaler = 32 , Ch0_gain = 1 , Ch0_inp = Single_ended , Mux0 = 0 'you can setup other channels as well

```
W = Getadc(adca , 0) 

Example for Free Running Mode:

```vb
'Configure ADC of Port A in FREE running mode  
Config Adca = Free , Convmode = Signed , Resolution = 12bit , Dma = Off , _  
```
Reference = Intvcc , Event_mode = None , Prescaler = 256 , Sweep = Ch01 , _  
Ch0_gain = 1 , Ch0_inp = Diffwgain , Mux0 = &B00000000 , _  
Ch1_gain = 1 , Ch1_inp = Diffwgain , Mux1 = &B00001001  
  
```vb
' With MuxX you can set the 4 MUX-Register  
' ADCA_CH0_MUXCTRL (for Channel 0)  
' ADCA_CH1_MUXCTRL (for Channel 1)  
' ADCA_CH2_MUXCTRL (for Channel 2)  
' ADCA_CH3_MUXCTRL (for Channel 3)  
  
' Mux0 = &B00000000 means in Signed Mode:  
' MUXPOS Bits = 000 --> Pin 0 is positive Input for Channel 0  
' MUXNEG Bits = 00 --> Pin 4 is negative Input for Channel 0 (Pin 4 because of Differential with gain)  
  
' Mux1 = &B00001001 means in Signed Mode:  
' MUXPOS Bits = 001 --> Pin 1 is positive Input for Channel 1  
' MUXNEG Bits = 01 --> Pin 5 is negative Input for Channel 1 (Pin 5 because of Differential with gain)

```
Measure Offset in Single Ended Unsigned Mode:

With this example we want to measure the offset in single ended unsigned mode and also the output of the internal 1.0 Voltage reference to DAC B PINB.2. Also the signature row with calibration byte is in the example.

1.| With the used ATXMEGA256A3BU the voltage on DAC B was measured with an DMM and the value was: 1.014V  
---|---  
  
2.| After changing the gain calibration register of DAC B Ch0 to DACB_GAINCAL = 160 then the DAC B Ch0 analog output value was the expected 1.000V  
---|---  
  
3.| The offset in single ended unsigned mode is 208  
---|---  
  
4.| Now we connect the DAC B output (Pinb.2) to ADC B input (Pinb.0): the ADC resolution is 2180  
---|---  
  
5.| Vref = 3.323Volt/1.6 = 2.076875 (Vcc was also double checked by a DMM)  
---|---  
  
6.| 2.076875/4095 = 507.1733822 µV  
---|---  
  
7.| 2180* 507.1733822 µV = 1.1056379 V  
---|---  
  
8.| So here we see the difference of the DAC output 1.000V to the measured value in single ended unsigned mode of 1.1056379 V is 0.10564 V  
---|---  
  
9.| When we subtract now the offset from the measured result (2180 - 208 = 1972) we are getting closer to the DAC B output  
---|---  
  
10.| 1972 * 507.1733822 µV = 1.0001V  
---|---  
  
'(  
Single ended input (unsigned mode)  
In unsigned mode the negative input is connected to half of the voltage reference (Vref) voltage minus a fixed device specific negative offset The approximate value corresponding to ground is around 200. This value corresponds to the digital result of ?V (0.05 * 4096). This value also depend on the selected voltage reference so you should measure the real value by first selecting the voltage reference.  
(?V = Vref * 0.05)  
  
How to measure the offset ?  
Connect the ADC input pin (Vinp) to GND and measure the offset.  
This is also called offset calibration. This value can be stored for example in EEPROM and is therefore available for all other measurements.  
  
This offset calibration value is then subtracted to each ADC output  
The offset enables the ADC to measure for example zero crossing in unsigned mode.  
```vb
')  
  
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
Config Osc = Enabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Portr.0 = Output  
```
Led0 Alias Portr.0 'LED 0  
Config Portr.1 = Output  
Led1 Alias Portr.1 'LED 1  
  
Config Com5 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Open "COM5:" For Binary As #1  
  
```vb
Dim B As Byte  
dim j as byte  
  
'First print the complete signature row  
For J = 0 To 37  
```
b = Readsig(j) : Print #1, j ;" = " ; b  
```vb
Next  
  
'Read calibration bytes from Signature row  
'ADCB  
```
B = Readsig(24) 'ADCB Calibration Byte 0  
ADCB_CALL = b 'write the value to the register  
Print #1 , "DCB Calibration Byte 0 = " ; B  
B = Readsig(25) 'ADCB Calibration Byte 1  
ADCB_CALH = b  
```vb
Print #1 , "DCB Calibration Byte 1 = " ; B  
'DACB  
```
B = Readsig(32) 'DACB Calibration Byte 0 (DACBOFFCAL)  
DACB_CH0OFFSETCAL = b 'write to the DACB offset register  
Print #1 , "DACB Calibration Byte 0 = " ; B  
B = Readsig(33) 'DACB Calibration Byte 1 (DACBGAINCAL)  
DACB_GAINCAL = 160  
```vb
Print #1 , "DACB Calibration Byte 1 = " ; B  
  
'Configure the DAC output to output  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single , Reference = Int1v , Interval = 64 , Refresh = 64  
  
Dim W As Word  
'--------------------------------------------------------------------------------  
'setup the ADC-B converter (there is no DAC A on ATXMEGA256A3BU)  
Config Adcb = Single , Convmode = Unsigned , Resolution = 12bit , Dma = Off , Reference = Intvcc , Event_mode = None , Prescaler = 32 , _  
```
Ch0_gain = 1 , Ch0_inp = Single_ended , Mux0 = &B00000000 'you can setup other channels as well  
  
Dacb0 = 4095 '1 V output on portb.2  
```vb
Do  
Wait 1  
'Connect PINB.0 with GND to measure the offset in unsigned mode  
```
W = Getadc(adcb , 0) 'Measure PINA.0  
```vb
Print #1 , "W = " ; W  
Loop  
  
End 'end program

```
Internal measure the DACB output with ADC B:

  
For this example you do not need a connection from DACB output to ADC B. 

We use the internal DACB output and measure it with ADCB so the DACB must be configured to output also internal and the ADC B must be configured to measure from internal DAC.

Don't forget to subtract the offset from the measured value as we use unsigned mode.

  
```vb
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
Config Osc = Enabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Portr.0 = Output  
```
Led0 Alias Portr.0 'LED 0  
Config Portr.1 = Output  
Led1 Alias Portr.1 'LED 1  
  
Config Com5 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Open "COM5:" For Binary As #1  
  
```vb
Dim B As Byte  
dim j as byte  
  
'First print the complete signature row  
For J = 0 To 37  
```
b = Readsig(j) : Print #1, j ;" = " ; b  
```vb
Next  
  
'Read calibration bytes from Signature row  
'ADCB  
```
B = Readsig(24) 'ADCB Calibration Byte 0  
ADCB_CALL = b 'write the value to the register  
Print #1 , "DCB Calibration Byte 0 = " ; B  
B = Readsig(25) 'ADCB Calibration Byte 1  
ADCB_CALH = b  
```vb
Print #1 , "DCB Calibration Byte 1 = " ; B  
'DACB  
```
B = Readsig(32) 'DACB Calibration Byte 0 (DACBOFFCAL)  
DACB_CH0OFFSETCAL = b 'write to the DACB offset register  
Print #1 , "DACB Calibration Byte 0 = " ; B  
B = Readsig(33) 'DACB Calibration Byte 1 (DACBGAINCAL)  
DACB_GAINCAL = b  
```vb
Print #1 , "DACB Calibration Byte 1 = " ; B  
  
'Configure the DAC output to output  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single ,INTERNAL_OUTPUT = enabled, Reference = Int1v , Interval = 64 , Refresh = 64  
  
Dim W As Word  
'--------------------------------------------------------------------------------  
'setup the ADC-B converter (there is no DAC A on ATXMEGA256A3BU)  
'For internal Measurements use Unsigned mode, 12 bit, Internal 1.00 V Reference  
Config Adcb = Single , Convmode = Unsigned , Resolution = 12bit , Dma = Off , Reference = Intvcc , Event_mode = None , Prescaler = 512 , _  
```
Ch0_gain = 1 , Ch0_inp = INTERNAL , Mux0 = &B0_0011_000 'configure MUX0 to measure internal DAC  
  
Dacb0 = 4095 '1 V  
  
```vb
Do  
Wait 1  
```
W = Getadc(adcb , 0 , &B0_0011_000) 'Measure DAC  
```vb
Print #1 , "W = " ; W  
Loop  
  
End 'end program

```

---

## CONFIG ATEMU

Action

Configures the PS/2 keyboard data and clock pins.

Syntax

CONFIG ATEMU = int , DATA = data, CLOCK=clock [,INIT=VALUE]

Remarks

Int | The interrupt used such as INT0 or INT1.  
---|---  
DATA | The pin that is connected to the DATA line. This must be the same pin as the used interrupt.  
CLOCK | The pin that is connected to the CLOCK line.  
INIT | An optional value that will identify the keyboard. By default or when omitted this is &HAB83. The code that identifies a keyboard. Some mother boards/BIOS seems to require the reverse &H83AB. By making it an option you can pass any possible value. The MSB is passed first, the LSB last.  
  
Male ![ebx_696563453](ebx_696563453.gif) (Plug) | Female  ![ebx_1116917378](ebx_1116917378.gif) (Socket) | 5-pin DIN (AT/XT):  1 - Clock 2 - Data 3 - Not Implemented 4 - Ground 5 - +5v  
---|---|---  
  
Male ![ebx_33802512](ebx_33802512.gif) (Plug) | Female ![ebx_2125574121](ebx_2125574121.gif) (Socket) | 6-pin Mini-DIN (PS/2): 1 - Data 2 - Not Implemented 3 - Ground 4 - +5v 5 - Clock 6 - Not Implemented  
---|---|---  
  
Old PCâs are equipped with a 5-pin DIN female connector. Newer PCâs have a 6-pin mini DIN female connector.

The male sockets must be used for the connection with the micro.

Besides the DATA and CLOCK you need to connect from the PC to the micro, you need to connect ground. You can use the +5V from the PC to power your microprocessor.

The config statement will setup an ISR that is triggered when the INT pin goes low. This routine you can find in the library.

The ISR will retrieve a byte from the PC and will send the proper commands back to the PC.

The SENDSCANKBD statement allows you to send keyboard commands.

Note that unlike the mouse emulator, the keyboard emulator is also recognized after your PC has booted.

![notice](notice.jpg) The PS2 Keyboard and mouse emulator needs an additional commercial addon library.

See also

[SENDSCANKBD](sendscankbd.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : ps2_kbdemul.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PS2 AT Keyboard emulator

'micro : 90S2313

'suited for demo : no, ADD ONE NEEDED

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "mcsbyteint.lbx" ' use optional lib since we use only bytes

'configure PS2 AT pins

Enable Interrupts ' you need to turn on interrupts yourself since an INT is used

Config Atemu = Int1 , Data = Pind.3 , Clock = Pinb.0

' ^------------------------ used interrupt

' ^----------- pin connected to DATA

' ^-- pin connected to clock

'Note that the DATA must be connected to the used interrupt pin

Waitms 500 ' optional delay

'rcall _AT_KBD_INIT

Print "Press t for test, and set focus to the editor window"

Dim Key2 As Byte , Key As Byte

Do

```
Key2 = Waitkey() ' get key from terminal

```vb
Select Case Key2

Case "t" :

Waitms 1500

```
Sendscankbd Mark ' send a scan code

```vb
Case Else

End Select

Loop

Print Hex(key)

```
Mark: ' send mark

Data 12 , &H3A , &HF0 , &H3A , &H1C , &HF0 , &H1C , &H2D , &HF0 , &H2D , &H42 , &HF0 , &H42

```vb
' ^ send 12 bytes

' m a r k

```

---

## CONFIG BASE

Action

This option specifies the lower boundary of all arrays.

Syntax

CONFIG BASE= value

Remarks

By default the first element of an array starts at 1. With CONFIG BASE=0 you can override this default so that all arrays start at 0. 

In some cases it is simpler that elements start at 0.

A constant named _BASE reflects the setting. You can not change the BASE at run time. 

![notice](notice.jpg)When you change this setting in existing code, you need to alter your code. For example when you used this code:

Dim a(10) as byte : a(10) = 10

And you set CONFIG BASE=0, it will mean that element 10 is invalid.

While in QB an additional element is created, this is not a good idea in bascom because it will require more space.

See also

[DIM](dim.md)

Example

```vb
CONFIG BASE=0

Dim ar(10) as byte , j as byte

For j=0 to 9 'array uses element 0-9

```
ar(j)=j

Next

Example

```vb
CONFIG BASE=1

Dim ar(10) as byte , j as byte

For j=1 to 10 ' arrays uses element 1-10

```
ar(j)=j

Next

---

## CONFIG BCCARD

Action

Initializes the pins that are connected to the BasicCard.

Syntax

CONFIG BCCARD = port , IO=pin, RESET=pin

Remarks

Port | The PORT of the micro that is connected to the BasicCard. This can be PORTB or PORTD and will depend on the used micro.  
---|---  
IO | The pin number that is connected to the IO of the BasicCard. Must be in the range from 0-7  
RESET | The pin number that is connected to the RESET of the BasicCard. Must be in the range from 0-7  
  
The variables SW1, SW2 and _BC_PCB are automatically dimensioned by the CONFIG BCCARD statement.

![notice](notice.jpg)This statements uses BCCARD.LIB, a library that is available separately from MCS Electronics.

See Also

[BCRESET](bcreset.md) , [BCDEF](bcdef.md) , [BCCALL](bccall.md)

Example

```vb
'------------------------------------------------------------------------------

' BCCARD.BAS

' This AN shows how to use the BasicCard from Zeitcontrol

' www.basiccard.com

'------------------------------------------------------------------------------

'connections:

' C1 = +5V

' C2 = PORTD.4 - RESET

' C3 = PIN 4 - CLOCK

' C5 = GND

' C7 = PORTD.5 - I/O

' /--------------------------------\

' | |

' | C1 C5 |

' | C2 C6 |

' | C3 C7 |

' | C4 C8 |

' | |

' \\--------------------------------/

'

'

'----------- configure the pins we use ------------

Config Bccard = PORTD , Io = 5 , Reset = 4

' ^ PORTD.4

' ^------------ PORTD.5

' ^--------------------- PORT D

'Load the sample calc.bas into the basiccard

' Now define the procedure in BASCOM

' We pass a string and also receive a string

```
Bcdef Calc(string)

```vb
'We need to dim the following variables

'SW1 and SW2 are returned by the BasicCard

'BC_PCB must be set to 0 before you start a session

'Our program uses a string to pass the data so DIM it

Dim S As String * 15

'Baudrate might be changed

$baud = 9600

' Crystal used must be 3579545 since it is connected to the Card too

$crystal = 3579545

'Perform an ATR

```
Bcreset

```vb
'Now we call the procedure in the BasicCard

'bccall funcname(nad,cla,ins,p1,p2,PRM as TYPE,PRM as TYPE)

```
S = "1+1+3" ' we want to calculate the result of this expression

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
' ^--- variable to pass that holds the expression

' ^------- P2

' ^----------- P1

' ^--------------- INS

' ^-------------------- CLA

' ^-------------------------- NAD

'For info about NAD, CLA, INS, P1 and P2 see your BasicCard manual

'if an error occurs ERR is set

' The BCCALL returns also the variables SW1 and SW2

Print "Result of calc : " ; S

Print "SW1 = " ; Hex(sw1)

Print "SW2 = " ; Hex(sw2)

'Print Hex(_bc_pcb) ' for test you can see that it toggles between 0 and 40

Print "Error : " ; Err

'You can call this or another function again in this session

```
S = "2+2"

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
Print "Result of calc : " ; S

Print "SW1 = " ; Hex(sw1)

Print "SW2 = " ; Hex(sw2)

'Print Hex(_bc_pcb) ' for test you can see that it toggles between 0 and 40

Print "Error : " ; Err

'perform another ATR

```
Bcreset

Input "expression " , S

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
Print "Answer : " ; S

'----and now perform an ATR as a function

Dim Buf(25) As Byte , I As Byte

```
Buf(1) = Bcreset()

```vb
For I = 1 To 25

Print I ; " " ; Hex(buf(i))

Next

'typical returns :

'TS = 3B

'T0 = EF

'TB1 = 00

'TC1 = FF

'TD1 = 81 T=1 indication

'TD2 = 31 TA3,TB3 follow T=1 indicator

'TA3 = 50 or 20 IFSC ,50 =Compact Card, 20 = Enhanced Card

'TB3 = 45 BWT blocl waiting time

'T1 -Tk = 42 61 73 69 63 43 61 72 64 20 5A 43 31 32 33 00 00

' B a s i c C a r d Z C 1 2 3

'and another test

'define the procedure in the BasicCard program

```
Bcdef Paramtest(byte , Word , Long )

```vb
'dim some variables

Dim B As Byte , W As Word , L As Long

'assign the variables

```
B = 1 : W = &H1234 : L = &H12345678

Bccall Paramtest(0 , &HF6 , 1 , 0 , 0 , B , W , L)

```vb
Print Hex(sw1) ; Spc(3) ; Hex(sw2)

'and see that the variables are changed by the BasicCard !

Print B ; Spc(3) ; Hex(w) ; " " ; Hex(l)

'try the echotest command

```
Bcdef Echotest(byte)

Bccall Echotest(0 , &HC0 , &H14 , 1 , 0 , B)

```vb
Print B

End 'end program

```

---

## CONFIG CANBUSMODE

Action

Configures the CAN bus mode.

Syntax

CONFIG CANBUSMODE =mode

Remarks

mode | The CAN bus can be set to 3 different modes. \- ENABLED : TxCAN and RxCAN are enabled. \- STANDBY : TxCAN is recessive and the receiver is disabled. The registers and mobs can be accessed. \- LISTENING : This mode is transparant for the CAN channel. It enables a hardware loop[ back from the internal TxCAN to the RxCAN. It provides a recessive level on the TxCAN output pin. It does NOT disable the RxCAN pin.  
---|---  
  
The CAN commands are intended for the AVR processor AT90CANXXX series. 

You need to terminate the bus with 120 ohm at both ends.

Your code always need a number of statements. The best solution is to use the can-elektor.bas sample to get started.

CANRESET

Will reset the CAN controller. Use this only once.

CANCLEARALLMOBS

Will clear all message objects. This is best to be done right after the CANRESET.

CANBAUD

All devices on the bus need to have the same baud rate. Set the BAUD right after you have cleared all objects.

CONFIG CANBUSMODE

Now you chose the mode the bus will work in. This is ENABLED in most cases.

CONFIG CANMOB

Here you define the properties of each Message Object. This need to be done only once. But after the message object has been used, you need to configure it again so the new MOB can be used again.

CANGIE , ON CAN_IT

Since the interrupt TX, RX and ERR interrupts are used you need to assign a value of &B10111000 to CANGIE.

You also need to assign an interrupt routine to the CANIT interrupt.

In the main code you can send data using CANSEND. 

The interrupt routine.

The CANPAGE register is saved into the _CAN_PAGE variable. This is required since the interrupt may not change the CANPAGE register.

Then CANGETINTS is used to retreive all message object interrupt flags. The value is stored in _CAN_MOBINTS.

Since multiple Message Objects can cause an interrupt we check all message objects with a For.. Next loop to test all bits. If the bit is set, the Message Object is selected with CANSELPAGE.

```vb
Then the CANSTMOB register is tested for a number of bits/flags.

If bit 5 is set, it means that a frame was received. For the demo the ID is read with CANID. 

```
The CANRECEIVE function reads the data from the frame into a variable. In the example the variable is a PORT which will change value depending on the receive data byte.

After this the CONFIG CANMOB is used with a value of -1 to indicate that the operation must be done on the current selected MOB.

The object is put back into receive mode.

If bit 6 is set it means that data was transmitted with success. Again, we use CONFIG CANMOB so the object can be used again. For transmitting we put the object into DISABLED mode.

And lastly we test bit 0, the MOB error bit. It if was set it means there was an error when data was sent using CANSEND. We must use CONFIG CANMOB so the MOB can be used again. 

We must clear the CANSIT1 and CANSIT2 flag registers before we exit the interrupt routine. We also need to reset the interrupt flags in CANGIT. This is done by writing the same value back to CANGIT. A one will clear the flag if it was set.

Last we restore the CANPAGE register by writing _CAN_PAGE back to it.

While the interrupt routine shows some PRINT statements, it is not a good idea to print inside the/a interrupt routine. You should keep the delay as short as possible otherwise you might not be able to process all CAN frames.

As you can see in the sample, the MOB's are configured at the start AND once they are used so they can be re-used. 

In the example all lines are important except for the PRINT lines. 

See also

[CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

```vb
'------------------------------------------------------------------------  
' CAN-Elektor.bas  
' bascom-avr demo for Auto-CANtroller board  
'------------------------------------------------------------------------  
$regfile = "m32can.dat" ' processor we use  
  
$crystal = 12000000 ' Crystal 12 MHz  
$hwstack = 64  
$swstack = 32  
$framesize = 40  
  
'$prog &HFF , &HCF , &HD9 , &HFF ' generated. Take care that the chip supports all fuse bytes.  
Config Porta = Output ' LED  
Config Portc = Input ' DIP switch  
```
Portc = 255 ' activate pull up  
  
Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
Open "COM2:" For Binary As #2  
  
```vb
Dim _canpage As Byte , _canid As Dword , _can_int_idx As Byte , _can_mobints As Word  
Dim Breceived As Byte , Bok As Byte , Bdil As Byte  
  
On Can_int Can_int ' define the CAN interrupt  
Enable Interrupts ' enable interrupts  
  
```
Canreset ' reset can controller  
Canclearallmobs ' clear alle message objects  
Canbaud = 125000 ' use 125 KB  
  
```vb
Config Canbusmode = Enabled ' enabled,standby,listening  
Config Canmob = 0 , Bitlen = 11 , Idtag = &H0120 , Idmask = &H0120 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled 'first mob is used for receiving data  
Config Canmob = 1 , Bitlen = 11 , Idtag = &H0120 , Msgobject = Disabled , Msglen = 1 ' this mob is used for sending data  
  
```
Cangie = &B10111000 ' CAN GENERAL INTERRUPT and TX and RX and ERR  
```vb
Print #2 , "Start"  
  
Do  
If Pinc <> Bdil Then ' if the switch changed  
```
Bdil = Pinc ' save the value  
Bok = Cansend(1 , Pinc) ' send one byte using MOB 1  
```vb
Print #2 , "OK:" ; Bok ' should be 0 if it was send OK  
End If  
Loop  
  
'*********************** CAN CONTROLLER INTERRUPT ROUTINE **********************  
'multiple objects can generate an interrupt  
```
Can_int:

_canpage = Canpage ' save can page because the main program can access the page too  
Cangetints ' read all the interrupts into variable _can_mobints  
  
```vb
For _can_int_idx = 0 To 14 ' for all message objects  
If _can_mobints._can_int_idx = 1 Then ' if this message caused an interrupt  
  
```
Canselpage _can_int_idx ' select message object  
  
If Canstmob.5 = 1 Then ' we received a frame  
_canid = Canid() ' read the identifier  
Print #2 , Hex(_canid)  
  
Breceived = Canreceive(porta) ' read the data and store in PORTA  
```vb
Print #2 , "Got : " ; Breceived ; " bytes" ' show what we received  
Print #2 , Hex(porta)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  
```
Elseif Canstmob.6 = 1 Then 'transmission ready  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  
```
Elseif Canstmob.0 = 1 Then 'ack error when sending data 'transmission ready  
```vb
Print #2 , "ERROR:" ; Hex(canstmob)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
End If  
End If  
Next  
```
Cangit = Cangit ' clear interrupt flags  
Canpage = _canpage ' restore page  
Return

---

## CONFIG CANMOB

Action

Configures one of the 15 CAN Message OBjects.

Syntax

CONFIG CANMOB=mob,BITLEN=bitlen,IDTAG=tag,IDMASK=mask,MSGOBJECT=mode,MSGLEN=msglen,AUTOREPLY=reply , CLEARMOB=clrmob

Remarks

mob | The mob(message object) is a number or variable with a range from 0-14. Number 15 is reserved by Atmel. There are 15 message objects you can use but only one set of registers. The CANPAGE register is used to select the proper MOB. This is all handled by the compiler. Internally, the mob you pass will set the CANPAGE register. When you use a value of -1 , the configuration is done on the current selected MOB (or CANPAGE). A reconfigure does not need to set the IDTAG and IDMASK again.  While you can use a constant or variable, you can not use a variable with a value of -1 to reconfigure the mob. A reconfigure requires a constant of -1.  
---|---  
bitlen | The CAN controller supports CAN messages with 11 bit ID's and with 29 bit ID's. And ID is an identifier. The lowest ID has the highest priority. Using 11 bit ID's has the advantage that it takes less time and as a result, you could send more messages. Just like with traffic, the bus capacity is limited. The baud rate and the message length all play a role. Valid values are 11 and 29. You can use a constant or variable. Using variables will increase code.   
idtag | The IDTAG is the identifier you assign to the message object. When the MOB is used for transmitting, the IDTAG is used for the CAN ID.  When the MOB is used for receiving, the IDTAG is used as a filter. Each time a message is sent or received, an interrupt is generated. This will interrupt the main process. For efficient usage, you need to set the IDTAG to filter only the ID's of interest. The IDMASK can be used together with the IDTAG to create a range. You can use a constant or variable to define the IDTAG. Using a variable will increase code.  
mask | The IDMASK is only used when the MOB is used in receiving mode.  It must be used together with IDTAG to create a range where the MOB will respond to. The following examples are for CAN rev A with 11 bit ID's. Example 1: you only want to filter ID &H0317. In this case you set the IDTAG to &H317. The IDMASK need to be set to &HFFFF in this case. A '1' for a bit in IDMASK means that the corresponding '1' in IDTAG is checked. When set a bit in IDMASK to '0' it means the corresponding bit in IDTAG can have any value. Full filtering: to accept only ID = 0x317 in part A. \- ID MSK = 111 1111 1111 b \- ID TAG = 011 0001 0111 b Example 2: you want to filter ID &H310-&H317. You can set the IDTAG to &H310 and the IDMASK to &HFFF8. The last 3 bits are set to 0 this way which means that &H310 is valid, but so is &H311, &H312, etc. Partial filtering: to accept ID from 0x310 up to 0x317 in part A. \- ID MSK = 111 1111 1000 b \- ID TAG = 011 0001 0xxx b Example 3: you want to filter from &H0000 to &H7FF. This means you need to respond to all messages. The IDMASK need to be set to 0. It will not matter to which value you set IDTAG since all 11 bits of IDMASK are set to 0. No filtering: to accept all ID from 0x000 up to 0x7FF in part A. \- ID MSK = 000 0000 0000 b \- ID TAG = xxx xxxx xxxx b You can use a constant or variable to define the IDMASK. Using a variable will increase code.  
mode | The mode in which the MOB will be used. \- DISABLED (0). The MOB is free to be used. \- TRANSMIT (1). The MOB data will be transmitted. \- RECEIVE (2). The MOB will wait for a message that matches the ID and MASK. \- RECEIVE_BUFFERED (3). This mode can be used to receive multiple frames. The CANSEND function will use the TRANSMIT mode. You should chose the DISABLED mode when configuring the MOB for transmission. Instead of the mentioned parameter names, you can also use a variable to set the mode. This variable must have a value between 0 and 3.  
msglen | This is the message length of the message in bytes. In receive mode you set it to the number of bytes you expect. The CANRECEIVE function will return the number of bytes read.  When the MOB is used for transmitting, it will define the length of the data. The length can also be 0 to send frames without data. The msglen can be a constant or variable. The maximum number of bytes that can be sent or received is 8.  
reply | This option can set ENABLED or DISABLED. If you use a variable, a 0 will disable auto reply, a 1 will enable auto reply. Auto reply can be used to reply to a remote frame. A remote frame is a frame without data. Since a remote frame has no data, you can reuse the MOB to send data as a reply to a remote frame.  
clrmob | By default all registers of a MOB are cleared when you configure the MOB. When you reconfigure the MOB, or want to respond to an auto reply, you do not want to clear the MOB. In such a case you can use CLEARMOB=NO to prevent clearing of the registers.  
  
While CONFIG CANMOB can dynamically set up the MOB (using variables instead of constants), it will increase code. So use a constant if possible.

See also

[CONFIG CANBUSMODE](config_canbusmode.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

```vb
Config Canmob = 0 , Bitlen = 11 , Idtag = &H0120 , Idmask = &H0120 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled 'first mob is used for receiving data  
Config Canmob = 1 , Bitlen = 11 , Idtag = &H0120 , Msgobject = Disabled , Msglen = 1 ' this mob is used for sending data

Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No ' reconfig with value -1 for the current MOB and do not set ID and MASK

```

---

## CONFIG CLOCK

Action

Configures the timer to be used for the Time$ and Date$ variables. 

Syntax

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] 

Syntax Xmega

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] [,RTC=rtc] [,RTC32=rtc32] [,HIGHESR=highesr]

Syntax Xtiny

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] [,RTC=rtc] , RUNMODE=runmode

Remarks

Soft | Use SOFT for using the software based clock routines. You need to add an ENABLE INTERRUPTS statement to your code since the SOFT mode uses the timer in interrupt mode. The timer interrupt is enabled automatic but the global interrupt you need to enable yourself. While the compiler could enable the global interrupt automatic, you would not have control anymore when it is enabled when using multiple interrupts. In general you enable global interrupts after all interrupts are setup. For the SOFT mode you need to connect a special low frequency crystal with a value of 32768 Hz to the ASYNC TIMER oscillator pins. Use USER to write/use your own code in combination with an I2C clock chip for example.  
---|---  
Sectic | This option allows to jump to a user routine with the label sectic. Since the interrupt occurs every second you may handle various tasks in the sectic label. It is important that you use the name SECTIC and that you return with a RETURN statement from this label. The usage of the optional SECTIC routine will use 30 bytes of the hardware stack. This option only works with the SOFT clock mode. It does not work in USER mode. [, GOSUB = SECTIC] is only for SOFT mode.  
RTC XMEGA | This option is only available for processors with an RTC (XMEGA). This option sets the RTC clock source. Valid parameters are : 1KHZ_INT32KHZ_ULP 1 kHz from internal 32 kHz ULP 1KHZ_32KHZ_CRYSTOSC 1 kHz from 32 kHz Crystal Oscillator on TOSC 1KHZ_INT32KHZ_RCOSC 1 kHz from internal 32 kHz RC Oscillator 32KHZ_32KHZ_CRYSTOSC 32 kHz from 32 kHz Crystal Oscillator on TOSC The 1KHz clocks will load the PER register with 1000-1 and the 32 KHz clock will load PER with a value of 32768-1. The overflow mode is used and you can use the compare overflow if required. Do not forget to enable the 32 KHz oscillator and the interrupts as shown in the Xmega example.  
RTC XTINY | This option is only available for processors with an RTC (XTINY). This option sets the RTC clock source. Valid parameters are : 32KHZ_32KHZ_INTOSC : 32 KHz from OSCULP32K 1KHZ_INT32KHZ_ULP : 1 KHz from OSCULP32K 32KHZ_32KHZ_CRYSTOSC : 32 KHz from XOSC32K EXT_OSC_TOSC1 : External clock from TOSC1 pin. When configuring the RTC to use either XOSC32K or the external clock on TOSC1, XOSC32K needs to be enabled and the Source Select bit (SEL) and Run Standby bit (RUNSTDBY) in the XOSC32K Control A register of the Clock Controller (CLKCTRL.XOSC32KCTRLA) must be configured accordingly.  
RTC32 | This option is available for few XMEGA chips. You can use it instead of the RTC. In fact when a processor has an RTC32, it does not have an RTC. You can not use both RTC and RTC32 together. RTC32 only accepts one value : 1KHZ_32KHZ_CRYSTOSC This also means that you must use/connect an external 32 KHz crystal. When you use the RTC32, the battery back register VBAT_CTRL is initialized and setup.   
HIGHESR | This option is available for few XMEGA chips which have RTC32 hardware. This option will set HIGH ESR mode when a value of '1' is selected. By default this option is 0/off. HIGH ESR consumes more power.   
runmode | This only applies to the XTINY. Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
  
When you use the CONFIG CLOCK (in soft or user mode) directive the compiler will DIM the following BYTE variables automatic : 

_sec 

_min 

_hour

_day 

_month

_year

![notice](notice.jpg)The DATETIME library will also be included by the compiler. For this reason it is important that you use CONFIG CLOCK when you use any of the date time functions.

The variables Time$ and Date$ will also be dimensioned. These are special variables since they are treated different. See [TIME$](time_.md) and [DATE$](date_.md).

Following a way to set Time$ and Date$ :

Date$ = "11/11/00"

Time$ = "02:20:00"

You can change the date format by using: Config Date = Mdy , Separator = "/" ' ANSI-Format

See [CONFIG DATE](config_date.md)

The _sec, _min and other internal variables can be changed by the user too.

But of course changing their values will change the Time$ and Date$ variables.

The compiler also creates an ISR that gets updated once a second. This works for AVR chips which can be asynchronously clocked from the TOSC1/2 pins.

TOSC1 = Timer Oscillator Pin 1

TOSC2 = Timer Oscillator Pin 2

For example the Timer/Counter 2 of an ATMEGA16 can be used as a Real Time Counter (RTC). The Timer/Counter 2 will then be asynchronously clocked from the TOSC Pin's. The Timer/Counter 2 can NOT be used for other tasks when configured in asynchronous mode.

![notice](notice.jpg)Notice that you need to connect a 32768 Hz crystal in order to use the timer in async mode, the mode that is used for the clock timer in SOFT mode. You also need to enable interrupts because of the interrupt service routine.

When you choose the USER option, only the internal variables are created (like _sec , _min , _hour....). 

With the USER option you need to write the clock code yourself (so the USER need to update for example the System Second or Secofday).

This means the one second clock must be generated by a "USER" source like a Timer which use the internal clock or an XTAL depending on the Xtal configuration.

There are so called "AVR Timer Calculator" online available where you input the clock frequency from xtal, which Timer you use (8 or 16 Bit) and the period you want to achieve (like 1 second or 1000ms) than it will give you number which you need to configure the timer.

You also configure the interrupt of the timer and then the program will jump to the timer interrupt routine where you can set the new system second.

Config Clock = User 'Use USER to write/use your own code  
  
You also need to include the following labels with config clock = user:  
  
Getdatetime:  
```vb
'called when date or time is read  
Return  
  
```
Setdate:  
```vb
'called when date$ is set  
Return  
  
```
Settime:  
```vb
'scanned when time$ is set  
Return

```
Example for config clock = user in Bascom-Simulator

Following example use $sim so it can be used in Bascom-Simulator. It uses config clock in user mode.

The second tick is generated by Timer1 and the time updated in the Timer interrupt service routine.

You can run this example direct in Bascom Simulator and you need to CLICK ON RUN BUTTON (in the simulator) go to Interrupts Tab and hit the OVF1 BUTTON to simulate an Timer interrupt.

Then you will see how the program jump to the interrupt service routine and updates the time !!

The Simulator output give you following:

01.09.09

00:00:01

00:00:02

00:00:03

00:00:04

00:00:05

00:00:06

00:00:07

That's it !

```vb
$regfile = "m16def.dat"  
$crystal = 12000000  
$hwstack = 80  
$swstack = 80  
$framesize = 80  
$baud = 19200  
$sim 'ONLY FOR SIMULATOR MODE !!!!  
  
Dim second_tick As Long  
  
Config Clock = User 'Use USER to write/use your own code  
Config Date = Dmy , Separator = . 'Day.Month.Year  
Config Timer1 = Timer , Prescale = 256  
On Timer1 Timer_irq  
```
Const Timer_preload = 18661 'Timervorgabe für Sekunden Takt  
  
```vb
Enable Timer1  
Enable Interrupts  
  
```
Date$ = "01.09.09"  
Time$ = "00:00:00"  
  
```vb
Print Date$  
  
Do  
```
!NOP  
```vb
Loop  
  
End 'end program  
  
```
Timer_irq: 'Timer1 IRQ (once per second)  
Incr Second_tick  
Time$ = Time(second_tick)  
Timer1 = Timer_preload  
  
```vb
Print Time$ 'only for Bascom-Simulator  
Return  
  
```
Settime:  
Return  
  
Getdatetime:  
Return  
  
Setdate:  
Return

Using a DS1307 with config clock

See the datetime_test1.bas example from the SAMPLES\DATETIME folder that shows how you can use a DS1307 clock chip for the date and time generation.

See also example below !

Using config clock with ATXMEGA

With ATXMEGA there are devices with 16-Bit RTC like ATXMEGA128A1 and 32-Bit RTC like ATXMEGA256A3B or ATXMEGA256A3BU. 

ATXMEGA with 16-Bit RTC:

•| Can be used with one of the two internal RC oscillator options or external 32.768kHz crystal oscillator  
---|---  
  
•| The internal 32 kHz Ultra Low Power (ULP) is a very low power clock source, and it is not designed for high accuracy.  
---|---  
  
•| If you want to use the internal 32Khz RC oscillator you need to enable it with config osc  
---|---  
  
Config Osc = Disabled , 32mhzosc = Enabled , 32khzosc = Enabled

ATXMEGA with 32-Bit RTC (for example ATXMEGA256A3B or ATXMEGA256A3BU):

•| An external 32.768kHz crystal oscillator must be used as the clock source  
---|---  
  
•| The 32-Bit RTC is combined with a Battery Backup System  
---|---  
  
Numeric Values to calculate with Date and Time:

•| SecOfDay: (Type LONG) Seconds elapsed since Midnight. 00:00:00 start with 0 to 85399 at 23:59:59.  
---|---  
  
•| SysSec: (Type LONG) Seconds elapsed since begin of century (at 2000-01-01!). 00:00:00 at 2000-01-01 start with 0 to 2147483647 (overflow of LONG-Type) at 2068-01-19 03:14:07  
---|---  
  
•| DayOfYear: (Type WORD) Days elapsed since first January of the current year.  
---|---  
  
•| First January start with 0 to 364 (365 in a leap year)  
---|---  
  
•| SysDay: (Type WORD) Days elapsed since begin of century (at 2000-01-01!). 2000-01-01 starts with 0 to 36524 at 2099-12-31  
---|---  
  
•| DayOfWeek: (Type Byte) Days elapsed since Monday of current week. Monday start with 0 to Sunday = 6  
---|---  
  
With the numeric type calculations with Time and date are possible. Type 1 (discrete Bytes) and 2 (Strings) can be converted to an according numeric value. Than Seconds (at SecOfDay and SysSec) or Days (at DayOfYear, SysDay), can be added or subtracted. The Result can be converted back.

See also

[TIME$](time_.md) , [DATE$](date_.md) , [CONFIG DATE](config_date.md), [Memory usage](memory_usage.md), [Date and Time Routines](datetime.md)

ASM

The following ASM routines are called from datetime.lib

_soft_clock. This is the ISR that gets called once per second.

Example 1

```vb
'-----------------------------------------------------------------------------------------

'name : megaclock.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows the new TIME$ and DATE$ reserved variables

'micro : Mega103

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m103def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'With the 8535 and timer2 or the Mega103 and TIMER0 you can

'easily implement a clock by attaching a 32768 Hz xtal to the timer

'And of course some BASCOM code

'This example is written for the STK300 with M103

Enable Interrupts

'[configure LCD]

$lcd = &HC000 'address for E and RS

$lcdrs = &H8000 'address for only E

Config Lcd = 20 * 4 'nice display from bg micro

Config Lcdbus = 4 'we run it in bus mode and I hooked up only db4-db7

Config Lcdmode = Bus 'tell about the bus mode

'[now init the clock]

Config Date = Mdy , Separator = / ' ANSI-Format

Config Clock = Soft 'this is how simple it is

'The above statement will bind in an ISR so you can not use the TIMER anymore!

'For the M103 in this case it means that TIMER0 can not be used by the user anymore

'assign the date to the reserved date$

'The format is MM/DD/YY

```
Date$ = "11/11/00"

```vb
'assign the time, format in hh:mm:ss military format(24 hours)

'You may not use 1:2:3 !! adding support for this would mean overhead

'But of course you can alter the library routines used

```
Time$ = "02:20:00"

```vb
'---------------------------------------------------

'clear the LCD display

```
Cls

Do

Home 'cursor home

Lcd Date$ ; " " ; Time$ 'show the date and time

```vb
Loop

'The clock routine does use the following internal variables:

'_day , _month, _year , _sec, _hour, _min

'These are all bytes. You can assign or use them directly

```
_day = 1

```vb
'For the _year variable only the year is stored, not the century

End

```
Xmega Sample 

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-RTC.bas  
' This sample demonstrates the Xmega128A1 RTC  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Portb = Output  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled , 32khzosc = Enabled  
' For the CLOCK we use the RTC so make sure the 32 KHZ osc is enabled!!!  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
```
Open "COM1:" For Binary As #1  
  
```vb
Config Clock = Soft , Rtc = 1khz_int32khz_ulp ' we select the internal 1 KHz clock from the 32KHz internal oscillator  
'the following clocks can be used to clock the RTC  
' 1KHZ_INT32KHZ_ULP 1 kHz from internal 32 kHz ULP  
' 1KHZ_32KHZ_CRYSTOSC 1 kHz from 32 kHz Crystal Oscillator on TOSC  
' 1KHZ_INT32KHZ_RCOSC 1 kHz from internal 32 kHz RC Oscillator  
' 32KHZ_32KHZ_CRYSTOSC 32 kHz from 32 kHz Crystal Oscillator on TOSC  
  
  
Config Priority = Static , Vector = Application , Lo = Enabled ' the RTC uses LO priority interrupts so these must be enabled !!!  
Enable Interrupts ' as usual interrupts must be enabled  
  
Do  
Print Time$ ' print the time  
Waitms 1000  
Loop  
  
'TO USE THE SECTIC in the sample you must use GOSUB=SECTIC in CONFIG CLOCK !!!

  
```
Sectic:  
```vb
Toggle Portb 'optional toggle some leds when using the gosub=sectic option  
Return

```
Example 2

  
```vb
$regfile = "m128def.dat"  
$hwstack = 80  
$swstack = 80  
$framesize = 160  
$crystal = 8000000  
$baud = 19200  
  
Enable Interrupts  
  
'[now init the clock]  
Config Date = Mdy , Separator = / ' ANSI-Format  
  
Config Clock = Soft 'this is how simple it is  
'The above statement will bind in an ISR so you can not use the TIMER anymore!  
  
'assign the date to the reserved date$  
'The format is MM/DD/YY  
```
Date$ = "11/11/05"  
  
```vb
'assign the time, format in hh:mm:ss military format(24 hours)  
'You may not use 1:2:3 !! adding support for this would mean overhead  
'But of course you can alter the library routines used  
  
```
Time$ = "23:59:50"  
```vb
Do  
Waitms 500  
Print Date$ ; Spc(3) ; Time$  
Loop

```
Example 3 (using DS1307 with Config clock)

```vb
'-------------------------------------------------------------------------------  
' DateTime_test.bas  
' This sample show how to use the Date-Time routines from the DateTime.Lib  
' written by Josef Franz Vögel  
'-------------------------------------------------------------------------------  
  
$regfile = "m328pdef.dat"  
$crystal = 12e6 '16MHz  
$hwstack = 80  
$swstack = 80  
$framesize = 160  
  
  
```
Const Clockmode = 1  
```vb
'use i2c for the clock  
  

#if Clockmode = 1  
Config Clock = Soft ' we use build in clock  
Disable Interrupts  

#else  
Config Clock = User ' we use I2C for the clock  
'configure the scl and sda pins (using software I2C routines)  
Config Sda = Portd.6  
Config Scl = Portd.5  
```
I2cinit  
  
'address of ds1307  
Const Ds1307w = &HD0 ' Addresses of Ds1307 clock  
Const Ds1307r = &HD1  

```vb
#endif  
  
  
'configure the date format  
Config Date = Ymd , Separator = - ' ANSI-Format  
'This sample does not have the clock started so interrupts are not enabled  
' Enable Interrupts  
  
'dim the used variables  
Dim Lvar1 As Long  
Dim Mday As Byte  
Dim Bweekday As Byte , Strweekday As String * 10  
Dim Strdate As String * 8  
Dim Strtime As String * 8  
Dim Bsec As Byte , Bmin As Byte , Bhour As Byte  
Dim Bday As Byte , Bmonth As Byte , Byear As Byte  
Dim Lsecofday As Long  
Dim Wsysday As Word  
Dim Lsyssec As Long  
Dim Wdayofyear As Word  
  
  
  
  
' =================== DayOfWeek =============================================  
' Example 1 with internal RTC-Clock  
  
```
_day = 4 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Bweekday = Dayofweek()  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of " ; Date$ ; " is " ; Bweekday ; " = " ; Strweekday  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 26 : Bmonth = 11 : Byear = 2  
Bweekday = Dayofweek(bday)  
Strweekday = Lookupstr(bweekday , Weekdays)  
Strdate = Date(bday)  
```vb
Print "Weekday-Number of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " is " ; Bweekday ; " (" ; Date(bday) ; ") = " ; Strweekday  
  
  
' Example 3 with System Day  
```
Wsysday = 2000 ' that is 2005-06-23  
Bweekday = Dayofweek(wsysday)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of System Day " ; Wsysday ; " (" ; Date(wsysday) ; ") is " ; Bweekday ; " = " ; Strweekday  
  
  
  
' Example 4 with System Second  
```
Lsyssec = 123456789 ' that is 2003-11-29 at 21:33:09  
Bweekday = Dayofweek(lsyssec)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Bweekday ; " = " ; Strweekday  
  
  
  
  
' Example 5 with Date-String  
```
Strdate = "04-11-02" ' we have configured Date in ANSI  
Bweekday = Dayofweek(strdate)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of " ; Strdate ; " is " ; Bweekday ; " = " ; Strweekday  
  
  
  
  
' ================= Second of Day =============================================  
' Example 1 with internal RTC-Clock  
```
_sec = 12 : _min = 30 : _hour = 18 ' Load RTC-Clock for example - testing  
  
Lsecofday = Secofday()  
```vb
Print "Second of Day of " ; Time$ ; " is " ; Lsecofday  
  
  
' Example 2 with defined Clock - Bytes (Second / Minute / Hour)  
```
Bsec = 20 : Bmin = 1 : Bhour = 7  
Lsecofday = Secofday(bsec)  
```vb
Print "Second of Day of Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(bsec) ; ") is " ; Lsecofday  
  
  
' Example 3 with System Second  
```
Lsyssec = 1234456789  
Lsecofday = Secofday(lsyssec)  
```vb
Print "Second of Day of System Second " ; Lsyssec ; "(" ; Time(lsyssec) ; ") is " ; Lsecofday  
  
  
' Example 4 with Time - String  
```
Strtime = "04:58:37"  
Lsecofday = Secofday(strtime)  
```vb
Print "Second of Day of " ; Strtime ; " is " ; Lsecofday  
  
  
  
' ================== System Second ============================================  
  
' Example 1 with internal RTC-Clock  
' Load RTC-Clock for example - testing  
```
_sec = 17 : _min = 35 : _hour = 8 : _day = 16 : _month = 4 : _year = 3  
  
Lsyssec = Syssec()  
```vb
Print "System Second of " ; Time$ ; " at " ; Date$ ; " is " ; Lsyssec  
  
  
' Example 2 with with defined Clock - Bytes (Second, Minute, Hour, Day / Month / Year)  
```
Bsec = 20 : Bmin = 1 : Bhour = 7 : Bday = 22 : Bmonth = 12 : Byear = 1  
Lsyssec = Syssec(bsec)  
Strtime = Time(bsec)  
Strdate = Date(bday)  
```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec  
  
  
' Example 3 with System Day  
  
```
Wsysday = 2000  
Lsyssec = Syssec(wsysday)  
```vb
Print "System Second of System Day " ; Wsysday ; " (" ; Date(wsysday) ; " 00:00:00) is " ; Lsyssec  
  
  
' Example 4 with Time and Date String  
```
Strtime = "10:23:50"  
Strdate = "02-11-29" ' ANSI-Date  
Lsyssec = Syssec(strtime , Strdate)  
```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec ' 91880630  
  
  
  
  
' ==================== Day Of Year =========================================  
' Example 1 with internal RTC-Clock  
```
_day = 20 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Wdayofyear = Dayofyear()  
```vb
Print "Day Of Year of " ; Date$ ; " is " ; Wdayofyear  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 24 : Bmonth = 5 : Byear = 8  
Wdayofyear = Dayofyear(bday)  
```vb
Print "Day Of Year of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(bday) ; ") is " ; Wdayofyear  
  
  
  
' Example 3 with Date - String  
```
Strdate = "04-10-29" ' we have configured ANSI Format  
Wdayofyear = Dayofyear(strdate)  
```vb
Print "Day Of Year of " ; Strdate ; " is " ; Wdayofyear  
  
  
' Example 4 with System Second  
  
```
Lsyssec = 123456789  
Wdayofyear = Dayofyear(lsyssec)  
```vb
Print "Day Of Year of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Wdayofyear  
  
  
' Example 5 with System Day  
```
Wsysday = 3000  
Wdayofyear = Dayofyear(wsysday)  
```vb
Print "Day Of Year of System Day " ; Wsysday ; " (" ; Date(wsysday) ; ") is " ; Wdayofyear  
  
  
  
  
  
' =================== System Day ======================================  
' Example 1 with internal RTC-Clock  
```
_day = 20 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Wsysday = Sysday()  
```vb
Print "System Day of " ; Date$ ; " is " ; Wsysday  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 24 : Bmonth = 5 : Byear = 8  
Wsysday = Sysday(bday)  
```vb
Print "System Day of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(bday) ; ") is " ; Wsysday  
  
  
' Example 3 with Date - String  
```
Strdate = "04-10-29"  
Wsysday = Sysday(strdate)  
```vb
Print "System Day of " ; Strdate ; " is " ; Wsysday  
  
' Example 4 with System Second  
```
Lsyssec = 123456789  
Wsysday = Sysday(lsyssec)  
```vb
Print "System Day of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Wsysday  
  
  
  
' =================== Time ================================================  
' Example 1: Converting defined Clock - Bytes (Second / Minute / Hour) to Time - String  
```
Bsec = 20 : Bmin = 1 : Bhour = 7  
Strtime = Time(bsec)  
```vb
Print "Time values: Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " converted to string " ; Strtime  
  
  
' Example 2: Converting System Second to Time - String  
```
Lsyssec = 123456789  
Strtime = Time(lsyssec)  
```vb
Print "Time of Systemsecond " ; Lsyssec ; " is " ; Strtime  
  
  
' Example 3: Converting Second of Day to Time - String  
```
Lsecofday = 12345  
Strtime = Time(lsecofday)  
```vb
Print "Time of Second of Day " ; Lsecofday ; " is " ; Strtime  
  
  
' Example 4: Converting System Second to defined Clock - Bytes (Second / Minute / Hour)  
  
```
Lsyssec = 123456789  
Bsec = Time(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(lsyssec) ; ")"  
  
  
  
' Example 5: Converting Second of Day to defined Clock - Bytes (Second / Minute / Hour)  
```
Lsecofday = 12345  
Bsec = Time(lsecofday)  
```vb
Print "Second of Day " ; Lsecofday ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(lsecofday) ; ")"  
  
' Example 6: Converting Time-string to defined Clock - Bytes (Second / Minute / Hour)  
```
Strtime = "07:33:12"  
Bsec = Time(strtime)  
```vb
Print "Time " ; Strtime ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour  
  
  
  
' ============================= Date ==========================================  
  
' Example 1: Converting defined Clock - Bytes (Day / Month / Year) to Date - String  
```
Bday = 29 : Bmonth = 4 : Byear = 12  
Strdate = Date(bday)  
```vb
Print "Dat values: Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " converted to string " ; Strdate  
  
  
' Example 2: Converting from System Day to Date - String  
```
Wsysday = 1234  
Strdate = Date(wsysday)  
```vb
Print "System Day " ; Wsysday ; " is " ; Strdate  
  
  
' Example 3: Converting from System Second to Date String  
```
Lsyssec = 123456789  
Strdate = Date(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " is " ; Strdate  
  
  
' Example 4: Converting SystemDay to defined Clock - Bytes (Day / Month / Year)  
  
```
Wsysday = 2000  
Bday = Date(wsysday)  
```vb
Print "System Day " ; Wsysday ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(wsysday) ; ")"  
  
  
' Example 5: Converting Date - String to defined Clock - Bytes (Day / Month / Year)  
```
Strdate = "04-08-31"  
Bday = Date(strdate)  
```vb
Print "Date " ; Strdate ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear  
  
  
' Example 6: Converting System Second to defined Clock - Bytes (Day / Month / Year)  
```
Lsyssec = 123456789  
Bday = Date(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(lsyssec) ; ")"  
  
  
  
' ================ Second of Day elapsed  
  
```
Lsecofday = Secofday()  
_hour = _hour + 1  
Lvar1 = Secelapsed(lsecofday)  
Print Lvar1  
  
Lsyssec = Syssec()  
_day = _day + 1  
Lvar1 = Syssecelapsed(lsyssec)  
Print Lvar1  
  
  
  
  
  
  
Looptest:  
  
' Initialising for testing  
_day = 1  
_month = 1  
_year = 1  
_sec = 12  
_min = 13  
_hour = 14  
  
  
  
```vb
Do  
If _year > 50 Then  
Exit Do  
End If  
  
```
_sec = _sec + 7  
If _sec > 59 Then  
Incr _min  
_sec = _sec - 60  
End If  
  
_min = _min + 2  
If _min > 59 Then  
Incr _hour  
_min = _min - 60  
End If  
  
_hour = _hour + 1  
If _hour > 23 Then  
Incr _day  
_hour = _hour - 24  
End If  
  
_day = _day + 1  
  
  
```vb
If _day > 28 Then  
Select Case _month  
Case 1  
```
Mday = 31  
Case 2  
Mday = _year And &H03  
If Mday = 0 Then  
Mday = 29  
Else  
Mday = 28  
```vb
End If  
Case 3  
```
Mday = 31  
Case 4  
Mday = 30  
Case 5  
Mday = 31  
Case 6  
Mday = 30  
Case 7  
Mday = 31  
Case 8  
Mday = 31  
Case 9  
Mday = 30  
Case 10  
Mday = 31  
Case 11  
Mday = 30  
Case 12  
Mday = 31  
```vb
End Select  
If _day > Mday Then  
```
_day = _day - Mday  
Incr _month  
If _month > 12 Then  
_month = 1  
Incr _year  
```vb
End If  
End If  
End If  
If _year > 99 Then  
Exit Do  
End If  
  
```
Lsecofday = Secofday()  
Lsyssec = Syssec()  
Bweekday = Dayofweek()  
Wdayofyear = Dayofyear()  
Wsysday = Sysday()  
  
  
```vb
Print Time$ ; " " ; Date$ ; " " ; Lsecofday ; " " ; Lsyssec ; " " ; Bweekday ; " " ; Wdayofyear ; " " ; Wsysday  
  
  
Loop  
End  
  
  
'only when we use I2C for the clock we need to set the clock date time  

#if Clockmode = 0  
'called from datetime.lib  
Dim Weekday As Byte  
```
Getdatetime:  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 0 ' start address in 1307  
  
I2cstart ' Generate start code  
I2cwbyte Ds1307r ' send address  
I2crbyte _sec , Ack  
I2crbyte _min , Ack ' MINUTES  
I2crbyte _hour , Ack ' Hours  
I2crbyte Weekday , Ack ' Day of Week  
I2crbyte _day , Ack ' Day of Month  
I2crbyte _month , Ack ' Month of Year  
I2crbyte _year , Nack ' Year  
I2cstop  
_sec = Makedec(_sec) : _min = Makedec(_min) : _hour = Makedec(_hour)  
_day = Makedec(_day) : _month = Makedec(_month) : _year = Makedec(_year)  
Return  
  
Setdate:  
_day = Makebcd(_day) : _month = Makebcd(_month) : _year = Makebcd(_year)  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 4 ' starting address in 1307  
I2cwbyte _day ' Send Data to SECONDS  
I2cwbyte _month ' MINUTES  
I2cwbyte _year ' Hours  
I2cstop  
Return  
  
Settime:  
_sec = Makebcd(_sec) : _min = Makebcd(_min) : _hour = Makebcd(_hour)  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 0 ' starting address in 1307  
I2cwbyte _sec ' Send Data to SECONDS  
I2cwbyte _min ' MINUTES  
I2cwbyte _hour ' Hours  
I2cstop  
```vb
Return  
  

#endif  
  
  
```
Weekdays:  
Data "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"

---

## CONFIG CLOCKDIV

Action  
  
Sets the clock divisor.

Syntax

CONFIG CLOCKDIV = constant

Remarks

constant | The clock division factor to use. Possible values are 1 , 2 , 4 , 8 ,16 , 32 ,64 , 128 and 256.  
---|---  
  
The options to set the clock divisor is available in most new chips. Under normal conditions the clock divisor is one. Thus an oscillator value of 8 MHz will result in a system clock of 8 MHz. With a clock divisor of 8, you would get a system clock of 1 MHz.

Low speeds can be used to generate an accurate system frequency and for low power consumption.

Some chips have a 8 or 16 division enabled by default by a fuse bit.

You can then reprogram the fuse bit or you can set the divisor from code.

When you set the clock divisor take care that you adjust the $CRYSTAL directive also.

$CRYSTAL specifies the clock frequency of the system. So with 8 MHz clock and divisor of 8 you would specify $CRYSTAL = 1000000.

Some older chips use a different method for clock division. These chips do not support CONFIG CLOCK but they might support [CLOCKDIVSION](clockdivision.md).

See also

[$CRYSTAL](crystal_1.md) , [CLOCKDIVISION](clockdivision.md)

Example

CONFIG CLOCKDIV = 8 'we divide 8 MHz crystal clock by 8 resulting in 1 MHz speed

---

## CONFIG COM1

Action

Configures the UART of AVR chips that have an extended UART like the M8.

Syntax

CONFIG COM1 = baud , synchrone=0|1,parity=none|disabled|even|odd,stopbits=1|2,databits=4|6|7|8|9,clockpol=0|1 

Remarks

baud | Baud rate to use. Use 'dummy' to leave the baud rate at the $baud value.  
---|---  
synchrone | 0 for asynchrone operation (default) and 1 for synchrone operation.  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 4,5,7,8 or 9.  
Clockpol | Clock polarity. 0 or 1.  
  
![notice](notice.jpg)Note that not all AVR chips have the extended UART. Most AVR chips have a UART with fixed communication parameters. These are : No parity, 1 stop bit, 8 data bits.

Normally you set the BAUD rate with $BAUD or at run time with BAUD. You may also set the baud rate when you open the COM channel. It is intended for the Mega2560 that has 4 UARTS and it is simpler to specify the baud rate when you open the channel. It may also be used with the first and second UART but it will generate additional code since using the first UART will always result in generating BAUD rate init code. 

See Also

[CONFIG COM2](config_com1.md) , [CONFIG COMx](configcomx.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M128 support in M128 mode

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$baud1 = 19200

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'By default the M128 has the M103 compatibility fuse set. Set the fuse to M128

'It also runs on a 1 MHz internal oscillator by default

'Set the internal osc to 4 MHz for this example DCBA=1100

'use the m128def.dat file when you wanto to use the M128 in M128 mode

'The M128 mode will use memory from $60-$9F for the extended registers

'Since some ports are located in extended registers it means that some statements

'will not work on these ports. Especially statements that will set or reset a bit

'in a register. You can set any bit yourself with the PORTF.1=1 statement for example

'But the I2C routines use ASM instructions to set the bit of a port. These ASM instructions may

'only be used on port registers. PORTF and PORTG will not work with I2C.

'The M128 has an extended UART.

'when CONFIG COMx is not used, the default N,8,1 will be used

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'try the second hardware UART

```
Open "com2:" For Binary As #1

```vb
'try to access an extended register

Config Portf = Output

'Config Portf = Input

Print "Hello"

Dim B As Byte

Do

Input "test serial port 0" , B

Print B

Print #1 , "test serial port 2"

Loop

```
Close #1

End

---

## CONFIG COM2

Action

Configures the UART of AVR chips that have a second extended UART like the M128.

Syntax

CONFIG COM2 = baud , synchrone=0|1,parity=none|disabled|even|odd,stopbits=1|2,databits=4|6|7|8|9,clockpol=0|1

Remarks

baud | Baud rate to use. Use 'dummy' to leave the baud rate at the $baud1 value.  
---|---  
synchrone | 0 for asynchrone operation (default) and 1 for synchrone operation.  
Parity | None, disabled, even or odd  
Stopbits | The number of stopbits : 1 or 2  
Databits | The number of databits : 4,5,7,8 or 9.  
Clockpol | Clock polarity. 0 or 1.  
  
Normally you set the BAUD rate with $BAUD or at run time with BAUD. You may also set the baud rate when you open the COM channel. It is intended for the Mega2560 that has 4 UARTS and it is simpler to specify the baud rate when you open the channel. It may also be used with the first and second UART but it will generate additional code since using the first or second UART will always result in generating BAUD rate init code. 

![notice](notice.jpg)Note that not all AVR chips have the extended UART. Most AVR chips have a UART with fixed communication parameters. They are : No parity, 1 stopbit, 8 data bits.

See Also

[CONFIG COM1](config_com1.md) , [CONFIG COMx](configcomx.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M128 support in M128 mode

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$baud1 = 19200 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'By default the M128 has the M103 compatibility fuse set. Set the fuse to M128

'It also runs on a 1 MHz internal oscillator by default

'Set the internal osc to 4 MHz for this example DCBA=1100

'use the m128def.dat file when you wanto to use the M128 in M128 mode

'The M128 mode will use memory from $60-$9F for the extended registers

'Since some ports are located in extended registers it means that some statements

'will not work on these ports. Especially statements that will set or reset a bit

'in a register. You can set any bit yourself with the PORTF.1=1 statement for example

'But the I2C routines use ASM instructions to set the bit of a port. These ASM instructions may

'only be used on port registers. PORTF and PORTG will not work with I2C.

'The M128 has an extended UART.

'when CONFIG COMx is not used, the default N,8,1 will be used

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'try the second hardware UART

```
Open "com2:" For Binary As #1

```vb
'try to access an extended register

Config Portf = Output

'Config Portf = Input

Print "Hello"

Dim B As Byte

Do

Input "test serial port 0" , B

Print B

Print #1 , "test serial port 2"

Loop

```
Close #1

End

---

## CONFIG COMx

Action

Configures the UART of AVR chips that have an extended UART like the M2560.

Syntax

CONFIG COMx = baud , synchrone=0|1,parity=none|disabled|even|odd,stopbits=1|2,databits=4|6|7|8|9,clockpol=0|1

Syntax Xmega

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits

Syntax Xtiny/MegaX

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits , Baud_Offset=baud_ofs , TX_RX_XC_XD_PIN=tx, TX=tx,RX=rx

Syntax AVRX

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits , TX_RX_XC_XD_PIN=tx, TX=tx,RX=rx

There is no baud offset in the AVRX series

Remarks normal AVR

COMx | The COM port to configure. Value in range from 1-4  
---|---  
baud | Baud rate to use.  
synchrone | 0 for asynchrone operation (default) and 1 for synchrone operation.  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 4,5,7,8 or 9.  
Clockpol | Clock polarity. 0 or 1.  
  
![notice](notice.jpg)Note that not all AVR chips have the extended UART. Most AVR chips have a UART with fixed communication parameters. These are : No parity, 1 stopbit, 8 data bits.

The Mega2560 does support 4 UART's.

Remarks Xmega

COMx | The COM port to configure. Value in range from 1-8  
---|---  
baud | Baud rate to use. If the baud rate can be generated accurately depends on the system clock.  
mode | The USART mode, this can be : \- ASYNCHRONEOUS or 0 (default) for asynchronous operation. \- SYNCHRONEOUS or 1 , for synchronous operation. \- IRDA or IRCOM for IRDA operation \- SPI or MSPI for operation as SPI controller * The mode must be provided since the baud calculation depends on the selected mode *  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 5,6,7,8 or 9.  
  
In the Xmega the registers have a fixed offset. This allows to use dynamic UARTS : you can change settings at run time by using a variable. This will use some more code when using just one UART but will save code when using multiple UARTS because you need only one copy of the code.

In the Xmega you MUST use CONFIG COM before you can use the UART. The CONFIG commands makes a call to _INIT_XMEGA_UART where the various parameters are passed to setup the UART. You also need to specify the baud rate. Do not use $BAUD.

The CLOCKPOL for the SPI mode has been removed, it will be added to a configuration command for the SPI.

The CONFIG COM will set the TX pin to output mode. This are the following pins :

UART | TX pin | RX pin | [BAUD](baud1.md)  
---|---|---|---  
COM1 - UART_C0 | PORTC.3 | PORTC.2 | BAUD  
COM2 - UART_C1 | PORTC.7 | PORTC.6 | BAUD1  
COM3 - UART_D0 | PORTD.3 | PORTD.2 | BAUD2  
COM4 - UART_D1 | PORTD.7 | PORTD.6 | BAUD3  
COM5 - UART_E0 | PORTE.3 | PORTE.2 | BAUD4  
COM6 - UART_E1 | PORTE.7 | PORTE.6 | BAUD5  
COM7 - UART_F0 | PORTF.3 | PORTF.2 | BAUD6  
COM8 - UART_F1 | PORTF.7 | PORTF.6 | BAUD7  
  
In IRDA mode, depending on the module you use, it might be necessary to invert the logic level of the TX pin with CONFIG XPIN. For example when COM1 is used for the IRDA module, you would use : CONFIG XPIN=PORTC.3, INVERTIO=ENABLED

Remarks XTINY/MEGAX/AVRX

COMx | The COM port to configure. Value in range from 1-6  
---|---  
baud | Baud rate to use. If the baud rate can be generated accurately depends on the system clock.  
mode | The USART mode, this can be : \- ASYNCHRONEOUS : (default) for asynchronous operation. \- SYNCHRONEOUS : for synchronous operation. \- IRCOM : for IRDA operation \- SPI : for operation as SPI controller * The mode must be provided since the baud calculation depends on the selected mode *  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 5,6,7,8 or 9.  
Baud_offset | The Xtiny/MegaX has an internal oscillator that runs at 16 or 20 MHz. The center frequency can be off depending on temperature and voltage. The Xtiny has 4 calibrated offset values for the oscillator which can be used to correct the BAUD. The options are : \- NONE : default, BAUD is calculated but no offset is used. All of the other values will read the signature row and will call code from xtiny.lib to compensate the BAUD value. \- OSC16_3V3 : OSC runs at 16 MHz and at 3V3 \- OSC16_5V : OSC runs at 16 MHz and at 5V \- OSC20_3V3 : OSC runs at 20 MHz and at 3V3 \- OSC20_5V : OSC runs at 20 MHz and at 5V It is up to the user to apply the selected voltage. It is up to the user to use the specified oscillator value. (change fuse bits). By default the 20 MHz internal osc is selected. So this setting does not change oscillator values, it only tells the compiler which sigrow must be loaded and used.   
TX_RX_XC_XD_PIN  
  
This option was named TXPIN before | This options selects the pins used for the UART. The XTINY/MEGAX/AVRX has a port multiplexer. This multi plexer allows to chose which pins are used for hardware connected to the port pins.  So this allows to chose one or more alternative pin locations for hardware such as USART,SPI, TWI and TIMER output. You can use CONFIG PORT_MUX when you use alternative pin positions. But [CONFIG PORT_MUX](config_port_mux.md) does not set port direction.  For the USART it is required to set the TX pin into output mode.  That is why this option exists : you can chose the alternative pin location and the compiler will set the port pin into output mode and will set the proper port multiplexer register bit. You can chose between the default location starting with DEF_ and the alternative location starting with ALTx_ Some processors also allow to disconnect the pins totally and they have a NONE option. It is important to understand that selecting an alternative pin will switch all the pins of that hardware device. For the USART this means you will switch both TX, RX, XCK and XDIR pin. You can not just change only the TX or RX. You can however change the pins dynamically at run time. Your hardware circuit should support this of course.  Please note that you only should use this option when you use the alternative pin location since using this option create more code since the multiplexer is configured. The parameter value for TX_RX_XC_XD_PIN lists all associated pins in the following order : TX, RX, XCK, XDIR. For example : Def_pb2_pb3_pb1_pb0 which means that PortB.2 is connected to TX and RX is connected to PortB.3.  ALT1_PA1_PA2_PA3_PA4 means that the alternative pin is used which is PA1 for TX in this case.   
TX | By default both the transmitter and receiver are enabled. But there are cases where you only want to use the receiver. In such a case you can DISABLE the TX pin.  
TX=DISABLED. The default is enabled and there is no need to specify this. Possible options : ENABLED and DISABLED  
RX | By default both the transmitter and receiver are enabled. But there are cases where you only want to use the transmiiter. In such a case you can DISABLE the RX pin.  
RX=DISABLED. The default is enabled and there is no need to specify this. Possible options : ENABLED and DISABLED  
  
It is preferred to use CONFIG COM instead of using $BAUD.

![notice](notice.jpg)It is important that you specify all parameters of CONFIG COM. Do not omit one. The only optional parameter is TX_RX_XC_XD_PIN for the alternative USART pins, and the TX and RX options to disable pins.

See Also

[CONFIG COM1](config_com1.md) , [CONFIG COM2](config_com1.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M2560 support

'micro : Mega2560

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m2560def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'The M128 has an extended UART.

'when CO'NFIG COMx is not used, the default N,8,1 will be used

Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com3 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com4 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'Open all UARTS

```
Open "com2:" For Binary As #1

Open "Com3:" For Binary As #2

Open "Com4:" For Binary As #3

```vb
Print "Hello" 'first uart

Dim B As Byte

Dim Tel As Word

Do

```
Incr Tel

```vb
Print Tel ; " test serial port 1"

Print #1 , Tel ; " test serial port 2"

Print #2 , Tel ; " test serial port 3"

Print #3 , Tel ; " test serial port 4"

```
B = Inkey(#3)

```vb
If B <> 0 Then

Print #3 , B ; " from port 4"

End If

Waitms 500

Loop

```
Close #1

Close #2

Close #3

End

Xtiny Example

```vb
'--------------------------------------------------------------------------------  
'name : serial.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates USART  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 16_20MHZ , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'dimension a variable  
Dim B As Byte  
  
Config PORTC.1 = Output  
Print "Test USART"  
  
Do  
Print "Hello" ; Spc(3) ; B  
Waitms 1000  
```
Incr B  
```vb
Toggle PORTC.1  
Loop  
  
  
End

```

---

## CONFIG DACA|DACB

Action

This statement configures the DACA or DACB in the Xmega.

Syntax

CONFIG DACx=dac, IO0=IO0, IO1=IO1, INTERNAL_OUTPUT =INTOTP, CHANNEL=channel, TRIGGER_CH0=trig0,  TRIGGER_CH1=trig1, REFERENCE=ref, LEFT_ADJUSTED=adjusted, EVENT_CHANNEL=event, INTERVAL=interval, REFRESH=refresh

Remarks

DACX | Chose either DACA or DACB. DACA is connected to PORTA. DACB is connected to PORTB.  
---|---  
dac | ENABLED or DISABLED. Chose ENABLED to enable the DAC.  
IO0 | ENABLED or DISABLED. Chose ENABLED to enable output 0. Each DAC has 2 outputs. When multiple outputs are used, the DAC is using S&H.  
IO1 | ENABLED or DISABLED. Chose ENABLED to enable output 1.   
Intotp | ENABLED or DISABLED. Chose ENABLED to enable the internal output.  
Channel | SINGLE or DUAL. If both outputs are used, you need to enable the second output with IO1.  
Trig0 | ENABLED or DISABLED. Chose ENABLED to enable the trigger of channel 0.  
Trig1 | ENABLED or DISABLED. Chose ENABLED to enable the trigger of channel 1.  
Ref | The DAC needs a stable voltage reference. You can chose one of the following: \- INT1V. This will select the internal 1V reference \- AVCC. This will use AVCC as reference. \- AREFA. This will use AREFA as reference. \- AREFB. This will use AREFB as reference. The output of the DAC can never be higher then the voltage reference. When you chose INT1V, the output is from 0-1V in 4096 steps.  
Adjusted | ENABLED or DISABLED. By default the DAC output is right adjusted (this means the first 8 Bit are in the Low Byte and the following 4 Bit in the High Byte of the 16-bit Register).  You can left alight the result.   
Event | The event channel to use for the event system.   
Interval | The minimum interval between 2 conversions.  This is a value of : 1,2,4,8,16,32,64 or 128. The default in the register is 64. A value of 64 will give an interval of 64 clock cycles. The value is set in clock cycles and the time in Âµ Second depend on the CLKper (Peripheral Clock) setting. The minimum in SINGLE Channel mode is 1ÂµS (1M conversions per seconds). The minimum in DUAL Channel mode (S/H mode) should no be below 1.5ÂµS (666K conversions per second). In DUAL Channel mode the 50% increase of peripheral clock cycles is AUTOMATICALLY added by the XMEGA chip.  
Refresh | The DAC channel refresh timing. This is the interval refresh time in DUAL channel mode. Possible values: OFF 16, 32, 128, 256, 512, 1014, 2048, 4096, 8192, 16384, 32768, 65536.  A value of 16 means an interval of 16 clock cycles. The default loaded is 64. Note: Higher refresh rates causes higher power consumption. Manual conversions or Events between the refresh intervals do NOT affect the refresh intervals. This means the channels will be refreshed at a constant timing even when the data register are for example updated in between.  
  
The DAC data register is available in the DACA0, DACA1 and DACB0 and DACB1 variables.

The DAC module can output conversion rates up to 1 M conversions per second with a resolution of 12 bits. 

A DAC conversion can be triggered by:

•| writing to the DAC data register (DACA0, DACA1 and DACB0 and DACB1)  
---|---  
  
•| an Event over Event System (when configured to trigger from Event system the DAC data register can be updated several times without triggering an conversion. In case of an Event the latest value in the DAC data register will be used for conversion)  
---|---  
  
Trigger mode can be different between DAC Channels. For example DAC Channel 0 can be setup to work with Events while Channel 1 can be configured to start conversion when DAC data register is updated.

How to handle the two Data Channels with one conversion Block:

  
```vb
' +-----------+ +------------------+  
' | Channel 0 | -------->| |-----> Out 0  
' +-----------+ | CONVERSION BLOCK |  
' +-----------+ | |  
' | Channel 1 | -------->| |-----> Out 1  
' +-----------+ +------------------+  
' |

' |

' Event System

```
The fact that there are two data channels but one conversion block it needs to be configured by CHANNEL.

•| If Channel is SINGLE: Channel 0 is used in continuous-drive output mode and Channel 0 is then always connected to conversion block.  
---|---  
  
•| If Channel is DUAL: Both channels work in Sample and Hold (S/H) mode. The Sample and Hold keep the DAC output values during a conversion of the other channel. To refresh the output value in DUAL channel mode the refresh timing can be set.   
---|---  
  
What can you drive with the XMEGA DAC outputs ?

\- The ouputs can drive loads of 1KOhm or capacitive loads of 100pF

It is possible to use the XMEGA DMA Controller to output data on DAC Channels. 

See [CONFIG DMACHx](config_dmachx.md), [CONFIG DMA](config_dma.md)

See also Example Nr 2 below.

Calibration of DAC:

To Calibrate to DAC you can use the values from the signature row or you can change manual the Dacb_ch0offsetcal and Dacb_gaincal register.

```vb
For example for using signature row for DACB Ch0 this is:

'DACB  
```
B = Readsig(32) 'DACB Calibration Byte 0 (DACBOFFCAL)  
Dacb_ch0offsetcal = B 'write to the DACB offset register  
Print #1 , "DACB Calibration Byte 0 = " ; B  
B = Readsig(33) 'DACB Calibration Byte 1 (DACBGAINCAL)  
Dacb_gaincal = B  
Print #1 , "DACB Calibration Byte 1 = " ; B

See also Atmel Application Note AVR1301 for further details.

See also

[START](start.md) , [STOP](stop.md),[ CONFIG EVENT_SYSTEM](config_event_system.md)

Example Nr 1:

(For another example see also the example xm128a1.bas from the samples\chips folder)

  
```vb
$regfile = "xm256a3bdef.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 'Portf.2 and Portf.3 is COM7  
```
Open "COM7:" For Binary As #1  
  
```vb
Dim Var As Byte  
  
Config Portf.0 = Output  
```
Led1 Alias Portf.0  
  
Config Portf.1 = Output  
Led2 Alias Portf.1  
  
  
  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single , Reference = Int1v , Interval = 64 , Refresh = 64  
Dacb0 = 4095 '1 V output on portb.2  
  
```vb
'Start Dacb ' to enable it  
'Stop Dacb ' to disable it  
  
Do  
  
```
Incr Var  
Waitms 500  
Dacb0 = 4095 '1 V output on portb.2  
```vb
Set Led1  
Reset Led2  
  
Waitms 500  
Reset Led1  
```
Dacb0 = 0 '0 V output on portb.2  
```vb
Set Led2  
  
Print #1 , "Tick " ; Var  
  
Loop  
  
End 'end program

```
Example Nr 2 (Ouput an Array of data from SRAM to DAC B over DMA):

(This example is generating an sawtooth wave on DAC B Channel 0 = Portb.2 on ATXMEGA256A3B)

  
```vb
' Ouput an Array of data from SRAM to DAC B over DMA  
  
' Timing: Timer/Counter TC0 feed the Event Channel 0  
' Event Channel 0 feed the DAC B Channel 0  
  
' Array Channel_0(1) is a word array filled with values  
  
' DMA Channel 0 start at Channel_0(1) and increment until 8192 Byte (= 2*4096). After the DMA transaction the source address will be reloaded  
' The destination address is the data register of DAC B Channel 0 and is incrementd once (to update the Low Byte and High Byte of the 12-Bit output value)  
  
'Frequency of output signal = 32MHz/32 = 1MHz --> 1MHz/4096 (Sample_Count) = appx. 244Hz  
  
$regfile = "xm256a3bdef.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Priority = Static , Vector = Application , Lo = Enabled  
  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 'Portf.2 and Portf.3 is COM7  
```
Open "COM7:" For Binary As #1  
  
```vb
Print #1 ,  
Print #1 , "Start DAC B Channel 0 over DMA Example"  
  
  
Dim Var As Byte  
  
Config Portf.0 = Output  
```
Led1 Alias Portf.0  
  
Config Portf.1 = Output  
Led2 Alias Portf.1  
  
  
Const Sample_count = 4096 'Number of 12-Bit Samples (Measurement Values)  
```vb
Dim Channel_0(sample_count) As Word 'Array  
Dim Dma_ready As Bit  
Dim Dma_channel_0_error As Bit  
  
  
```
Enable_dmach0 Alias Dma_ch0_ctrla.7 'Enable DMA Channel 0  
  
```vb
Dim I As Word  
  
For I = 1 To 4096 'From 0V .....3.3Volt (with Reference = avcc)  
```
Channel_0(i) = I 'Generate a Sawtooth wave  
```vb
Next  
  
  
Config Tcc0 = Normal , Prescale = 1 'Setup Timer/Counter TC0 in nomal mode , Prescale = 1 --> no prescaler  
```
Tcc0_per = 31 '31 --> 32MHz/32 = 1MHz  
  
```vb
Config Event_system = Dummy , Mux0 = Tcc0_ovf 'TCC 0 overflow --> Event Channel 0  
  
  
' The xm256a3bd only have one DAC (DAC B)  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single , Trigger_ch0 = Enabled , Event_channel = 0 , Reference = Avcc , Interval = 4 , Refresh = 16  
' DAC B Channel 0 is triggered by Event Channel 0  
  
  
' DMA Interrupt  
On Dma_ch0 Dma_ch0_int 'Interrupt will be enabled with Tci = XX in Config DMAX  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA, Double Buffer disabled  
  
' DMA Channel 0 is used here  
Config Dmach0 = Enabled , Burstlen = 2 , Chanrpt = Enabled , Tci = Lo , Eil = Lo , Singleshot = Enabled , _  
```
Sar = Transaction , Sam = Inc , Dar = Burst , Dam = Inc , Trigger = &H25 , Btc = 8192 , Repeat = 0 , Sadr = Varptr(channel_0(1)) , Dadr = Varptr(dacb_ch0datal)  
  
```vb
' Trigger = &H25 (DAC B Base Level Trigger) + Channel 0 = &H00 --> &H25  
' Burstlen is 2 byte because the DAC output value is a 12-Bit value you need to transfer 2 byte  
' Source address (the array) is incremented until all bytes transfered (8192 byte)  
' Destination address (DAC B Channel 0) is incremented once to transfer the low byte and high byte of the 12-bit value  
' BTC = 8192 BYTE (needed to transfer the 4096 word)  
' Reapeat = 0 --> repeat forever  
  
  
Enable Interrupts  
  
  
  
'Frequency of output signal = 32MHz/32 = 1MHz --> 1MHz/4096 (Sample_Count) = appx. 244Hz  
  
Do  
  
  
Loop  
  
End 'end program  
  
  
'----------------------[Interrupt Service Routines]-----------------------------  
  
' Dma_ch0_int is for DMA Channel ERROR Interrupt A N D for TRANSACTION COMPLETE Interrupt  
' Which Interrupt fired must be checked in Interrupt Service Routine  
```
Dma_ch0_int:  
  
```vb
If Dma_intflags.0 = 1 Then 'Channel 0 Transaction Interrupt Flag  
Set Dma_intflags.0 'Clear the Channel 0 Transaction Complete flag  
Set Dma_ready  
End If  
  
If Dma_intflags.4 = 1 Then 'Channel 0 ERROR Flag  
Set Dma_intflags.4 'Clear the flag  
Set Dma_channel_0_error 'Channel 0 Error  
End If  
  
Return

```

---

## CONFIG DACX

Action

This statement configures the DAC0 or DACX in the Xtiny/Megax/AVRX.

Syntax

CONFIG DACx=dac, IO0=IO0, RUNMODE=runmode, OUT_ENABLE =out

Remarks

DACX | Chose either DAC0 or DACX.  
---|---  
dac | ENABLED or DISABLED. Chose ENABLED to enable the DAC.  
runmode | Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
Out | ENABLED or DISABLED. Chose ENABLED to enable the output. This will also set PORTA.6 to output mode. Notice that only DAC0 has the ability to drive an output pin. The output pin varies per processor. The compiler will use the proper pin.  
  
The DAC data register is available in the byte variable DAC0_DATA.

When present, the register names for DAC1 and DAC2 are : DAC1_DATA and DAC2_DATA.  
In version 2086 the WRITEDAC statement exist to write to the registers.

See also

[WRITEDAC](writedac.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name : dac.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates DAC  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'configure the internal reference to be 1v1 for both the ADC and the DAC  
Config Vref = Dummy , Adc0 = 1v1 , Dac0 = 1v1  
  
'configure the DAC. We also drive the PA6 output pin  
Config Dac0 = Enabled , Out_enable = Enabled  
  
Print "Test DAC0"  
  
Do  
```
Dac0_data = Dac0_data + 10

```vb
' or use the WRITEDAC statement : WRITEDAC value  
Print "DAC0:" ; Dac0_data  
Waitms 100  
Loop  
  
End

```

---

## CONFIG DATE

Action

Configure the Format of the Date String for Input to and Output from BASCOM â Date functions

Syntax

CONFIG DATE = DMY , Separator = char

Remarks

DMY | The Day, month and year order. Use DMY, MDY or YMD.  
---|---  
Char | The character used to separate the day, month and year. Old syntax : / , - or . (dot). Preferred new syntax : MINUS, SLASH or DOT. Example: Config Date = DMY, SEPARATOR=MINUS  
  
The following table shows the common formats of date and the associated statements.

Country | Format | Statement  
---|---|---  
American | mm/dd/yy | Config Date = MDY, Separator = SLASH  
ANSI | yy.mm.dd | Config Date = YMD, Separator = DOT  
Britisch/French | dd/mm/yy | Config Date = DMY, Separator = SLASH  
German | dd.mm.yy | Config Date = DMY, Separator = DOT  
Italian | dd-mm-yy | Config Date = DMY, Separator = MINUS  
Japan/Taiwan | yy/mm/dd | Config Date = YMD, Separator = SLASH  
USA | mm-dd-yy | Config Date = MDY, Separator = MINUS  
  
When you live in Holland you would use :

CONFIG DATE = DMY, separator = MINUS

This would print 24-04-02 for 24 November 2002.

When you line in the US, you would use :

CONFIG DATE = MDY , separator = SLASH

This would print 04/24/02 for 24 November 2002.

See also

[CONFIG CLOCK](config_clock.md) , [DATE TIME functions](datetime.md) , [DayOfWeek](dayofweek.md) , [DayOfYear](dayofyear.md) , [SecOfDay](secofday.md) , [SecElapsed](secelapsed.md) , [SysDay](sysday.md) , [SysSec](syssec.md) , [SysSecElapsed](syssecelapsed.md) , [Time](time.md) , [Date](date.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : megaclock.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows the new TIME$ and DATE$ reserved variables

'micro : Mega103

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m103def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'With the 8535 and timer2 or the Mega103 and TIMER0 you can

'easily implement a clock by attaching a 32768 Hz xtal to the timer

'And of course some BASCOM code

'This example is written for the STK300 with M103

Enable Interrupts

'[configure LCD]

$lcd = &HC000 'address for E and RS

$lcdrs = &H8000 'address for only E

Config Lcd = 20 * 4 'nice display from bg micro

Config Lcdbus = 4 'we run it in bus mode and I hooked up only db4-db7

Config Lcdmode = Bus 'tell about the bus mode

'[now init the clock]

Config Date = Mdy , Separator = SLASH ' ANSI-Format

Config Clock = Soft 'this is how simple it is

'The above statement will bind in an ISR so you can not use the TIMER anymore!

'For the M103 in this case it means that TIMER0 can not be used by the user anymore

'assign the date to the reserved date$

'The format is MM/DD/YY

```
Date$ = "11/11/00"

```vb
'assign the time, format in hh:mm:ss military format(24 hours)

'You may not use 1:2:3 !! adding support for this would mean overhead

'But of course you can alter the library routines used

```
Time$ = "02:20:00"

```vb
'---------------------------------------------------

'clear the LCD display

```
Cls

Do

Home 'cursor home

Lcd Date$ ; " " ; Time$ 'show the date and time

```vb
Loop

'The clock routine does use the following internal variables:

'_day , _month, _year , _sec, _hour, _min

'These are all bytes. You can assign or use them directly

```
_day = 1

```vb
'For the _year variable only the year is stored, not the century

End

```

---

## CONFIG DCF77

Action

Instruct the compiler to use DCF-77 radio signal to get atom clock precision time

Syntax

CONFIG DCF77 = pin , timer = timer [ INVERTED=inv, CHECK=check, UPDATE=upd, UPDATETIME=updtime , TIMER1SEC=tmr1sec, SWITCHPOWER=swpwr, POWERPIN=pin, POWERLEVEL = pwrlvl , SECONDTICKS=sectick ,DEBUG=dbg , GOSUB = Sectic , PULSE=pulse ]

Remarks

PIN | The input pin that is connected to the DCF-77 signal. This can be any micro processor pin that can be used as an input.  
---|---  
TIMER | The timer that is used to generate the compare interrupts, needed to determine the level of the DCF signal. Supported timers are : TIMER1. For Xmega : TCC0,TCC1,TCE0,TCE1,TCD0,TCD1,TCF0,TCF1 Xmega needs the MED priority set with [CONFIG PRIORITY](config_priority.md) because the MED priority is used for the timer interrupt. For Xtiny platform : TCA0, TCA1, TCAx  
INVERTED | This value is 0 by default. When you specify 1, the compiler will assume you use an inverted DCF signal. Most DCF-77 receivers have a normal output and an inverted output.  
CHECK | Check is 1 by default. The possible values are : 0 \- The DCF-77 parity bits are checked. No other checks are performed. Use it when you have exceptional signal strength 1 \- The received minutes are compared with the previous received minutes. And the difference must be 1. 2 \- All received values(minutes, hours, etc. ) are compared with their previous received values. Only the minutes must differ with 1, the other values must be exactly the same. This value uses more internal ram but it gives the best check. Use this when you have bad signal reception.  
UPDATE | Upd determines how often the internal date/time variables are updated with the DCF received values. The default value is 0. There are 3 possible values : 0 \- Continuous update. The date and time variables are updated every time the correct values have been received 1 \- Hourly update. The date and time variables are updated once an hour. 2\- Daily update. The date and time variables are updated once a day. The UPDATE value also determines the maximum value of the UPDATETIME option.  
UPDATETIME | This value depends on the used UPDATE parameter. When UPDATE is 1, the value must be in the range from 0-59. Start every hour at this minute with the new update. When UPDATE is 2, the value must be in the range from 0-23. Start every day at this hour with the new update. The default is 0.  
TIMER1SEC | 16 bit timers with the right crystal value can generate a precise interrupt that fires every second. This can be used to synchronize only once a day or hour with the DCF values. The remaining time, the 1-sec interrupt will update the soft clock. By default this value is 0.  
SWITCHPOWER | This option can be used to turn on/off the DCF-77 module with the control of a port pin. The default is 0. When you specify a value of 1, the DCF receiver will be switched off to save power, as soon as the clock is synchronized.  
POWERPIN | The name of a pin like pinB.2 that will be used to turn on/off the DCF module.  
POWERLEVEL | This option controls the level of the output pin that will result in a power ON for the module. 0 - When a logic 0 is applied to the power pin, the module is ON. 1 - When a logic 1 is applied to the power pin, the module is ON. Use a transistor to power the module. Do not power it from a port PIN directly. When you do power from a pin, make sure you sink the current. Ie : connect VCC to module, and GND of the module to ground. A logic 0 will then turn on the module.  
SECONDTICKS | The number of times that the DCF signal state is read. This is the number of times per second that the interrupt is executed. This value is calculated by the compiler. The highest possible timer pre scale value is used and the lowest possible number of times that the interrupt is executed. This gives least impact on your main application. You can override the value by defining your own value. For example when you want to run some own code in the interrupt and need it to execute more often.  
DEBUG | Optional value to fill 2 variables with debug info. DEBUG is on when a value of 1 is specified. By default, DEBUG is off. This has nothing to do with other DEBUG options of the compiler, it is only for the DCF77 code! When 1 is specified the compiler will create 2 internal variable named : bDCF_Pause and bDCF_Impuls. These values contain the DCF pulse length of the pause and the impulse. In the sample these values are printed.  
GOSUB | The Sectic option will call a label in the main program every second. You have to insert this label yourself. You must also end it with a RETURN. The option is the same as used with [CONFIG CLOCK](config_clock.md)  
PULSE | This is an optional parameter that sets the pulse time in mS. The default is 150. When you have hardware that requires a shorter or longer pulse you can try a slightly higher or lower value. At all times you should use a value between 100 and 200 where 150 would be the optimum value.  
  
The DCF decoding routines use a status byte. This byte can be examined as in the example.

The bits have the following meaning.

Bit | Explanation  
---|---  
0 | The last reading of the DCF pin.  
1 | This bit is reserved.  
2 | This Bit is set, if after a complete time-stamp at second 58 the time-stamp is checked and it is OK. If after a minute mark (2 sec pause) this bit is set, the time from the DCF-Part is copied to the Clock-Part and this bit reset too. Every second mark also resets this bit. So time is only set, if after second 58 a minute mark follows. Normally this bit is only at value 1 from Second 58 to second 60/00.  
3 | This Bit indicates, that the DCF-Part should be stopped, if time is set. (at the option of updating once per hour or day).  
4 | This Bit indicated that the DCF-Part is stopped.  
5 | This bit indicates, that the CLOCK is configured the way, that during DCF-Clock is stopped, there is only one ISR-Call in one second.  
6 | This Bit determines the level of the DCF input-pin at the pulse (100/200 mSec part).  
7 | This bit indicates, that the DCF-Part has set the time of the Clock-part.  
  
See Also

[DCF77TIMEZONE](dcf77timezone.md)

![notice](notice.jpg)You can read the Status-Bit 7 (DCF_Status.7), to check whether the internal clock was synchronized by the DCF-Part. You can also reset this Bit with [RESET](reset.md) DCF_Status.7. The DCF-Part will set this bit again, if a valid time-stamp is received.

You can read all other bits, but donât change them.

The DCF-77 signal is broadcasted by the German Time and Frequency department.

The following information is copied from :[ http://www.ptb.de/en/org/4/44/_index.htm](http://www.ptb.de/en/org/4/44/_index.md)

The main task of the department time and frequency is the realization and dissemination of the base unit time (second) and the dissemination of the legal time in the Federal Republic of Germany.

The second is defined as the duration of 9 192 631 770 periods of the radiation corresponding to the transition between the two hyper fine levels of the ground state of the cesium-133 atom.

For the realization and dissemination of the unit of time, the department develops and operates cesium atomic clocks as primary standards of time and frequency. In the past decades, these, as the worldwide most accurate atomic clocks, have contributed to the international atomic time scale (TAI) and represent the basis for the legal time in Germany. Dissemination of the legal time to the various users in industry, society, and research is performed via satellite, via a low frequency transmitter DCF77 and via an internet- and telephone service.

The department participates in the tests for the future European satellite navigation system âGalileoâ.

Presently the primary clocks realizing the time unit are augmented by Cs clocks with laser cooled atoms (âCs-fountain clocksâ) whose accuracy presently exceeds the clocks with thermal beams by a factor of 10 (frequency uncertainty of 1 . 10-15).

Future atomic clocks will most likely be based on atomic transitions in the optical range of single stored ions. Such standards are presently being developed along with the means to relate their optical frequencies without errors to radio-frequencies or 1 second pulsed.

As one may expect transitions in nuclei of atoms to be better shielded from environmental perturbations than electron-shell transitions which have been used so far as atomic clock references, the department attempts to use an optical transition in the nucleus of 229Th for a future generation of atomic clocks.

The work of the department is complemented by research in nonlinear optics (Solitons) and precision time transfer techniques, funded in the frame of several European projects and by national funding by Deutsche Forschungsgemeinschaft particularly in the frame of Sonderforschungsbereich 407 jointly with Hannover University.

The following information is copied from wikipedia : <http://en.wikipedia.org/wiki/DCF77>

The signal can be received in this area:

![dcf-77-area](dcf-77-area.png)

DCF77 is a long wave time signal and standard-frequency radio station. Its primary and backup transmitter are located in Mainflingen, about 25 km south-east of Frankfurt, Germany. It is operated by T-Systems Media Broadcast, a subsidiary of Deutsche Telekom AG, on behalf of the Physikalisch-Technische Bundesanstalt, Germany's national physics laboratory. DCF77 has been in service as a standard-frequency station since 1959; date and time information was added in 1973.

The 77.5 kHz carrier signal is generated from local atomic clocks that are linked with the German master clocks in Braunschweig. With a relatively-high power of 50 kW, the station can be received in large parts of Europe, as far as 2000 km from Frankfurt. Its signal carries an amplitude-modulated, pulse-width coded 1 bit/s data signal. The same data signal is also phase modulated onto the carrier using a 511-bit long pseudo random sequence (direct-sequence spread spectrum modulation). The transmitted data repeats each minute

Map showing the range of the DCF77 signal.

Map showing the range of the DCF77 signal.

* the current date and time;

* a leap second warning bit;

* a summer time bit;

* a primary/backup transmitter identification bit;

* several parity bits.

Since 2003, 14 previously unused bits of the time code have been used for civil defence emergency signals. This is still an experimental service, aimed to replace one day the German network of civil defense sirens.

The call sign stands for D=Deutschland (Germany), C=long wave signal, F=Frankfurt, 77=frequency: 77.5 kHz. It is transmitted three times per hour in morse code.

Radio clocks have been very popular in Europe since the late 1980s and most of them use the DCF77 signal to set their time automatically.

For further reference see wikipedia, a great on line information resource.

The DCF library parameters state diagram looks as following:

![DCF-Parameter](dcf-parameter.png)

```vb
If the SECTIC option is used, the Sectic Interrupt routine should not need more time, than to the next timer interrupt. If you use a timer for dcf (and softclock) usually with 40 tics per second, the Sectic routine should take only less than 25msec. 

If the Sectic routines needs more than this limit, you will lose accuracy of the softclock time (especially during the time, where the clock is not synchronized by DCF) and also measurement of the length of the DCF-pulses. 

If the SECTIC routine needs more time than the short DCF-pulse (100ms, with some instability in DCF-receiver may be 80ms) you will lose synchronization with the DCF-signal.

```
It is the principle of the DCF-routine, that the timer-interrupt measures the DCF-Pulse length and if you need more time in the interrupt routine as the duration from one timer interrupt to the next, you will get a problem.

Thus keep the SECTIC routine as short as possible and set a flag in the SECTIC routine, which is checked in a loop of the main-program. 

See also

[CONFIG DATE](config_date.md)

ASM

_DCF77 from DCF77.LBX is included by the compiler when you use the CONFIG statement.

Example

```vb
$regfile = "M88def.dat"

$crystal = 8000000

$hwstack = 128

$swstack = 128

$framesize = 128

$baud = 19200

'Config Dcf77 = Pind.2 , Debug = 1 , Inverted = 0 , Check = 2 , Update = 0 , Updatetime = 30 , Switchpower = 0 , Secondticks = 50 , Timer1sec = 1 , Powerlevel = 1 , Timer = 1

Config Dcf77 = Pind.2 , Timer = 1 , Timer1sec = 1 , Debug = 1

Enable Interrupts

Config Date = Dmy , Separator = .

Dim I As Integer

Dim Sec_old As Byte , Dcfsec_old As Byte

```
Sec_old = 99 : Dcfsec_old = 99 ': DCF_Debug_Timer = 0

```vb
' Testroutine fÃ¼r die DCF77 Clock

Print "Test DCF77 Version 1.00"

Do

For I = 1 To 78

Waitms 10

If Sec_old <> _sec Then

Exit For

End If

If Dcfsec_old <> Dcf_sec Then

Exit For

End If

Next

Waitms 220

```
Sec_old = _sec

Dcfsec_old = Dcf_sec

```vb
Print Time$ ; " " ; Date$ ; " " ; Time(dcf_sec) ; " " ; Date(dcf_day) ; " " ; Bin(dcf_status) ; " " ; Bin(dcf_bits) ; " " ; Bdcf_impuls ; " " ; Bdcf_pause

Loop

End

```
Example Xtiny

```vb
'---------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' DCF 77 demo to demonstrate the DCF77 library from Josef Vögel  
'---------------------------------------------------------  
$regfile = "avrx64da64.dat"  
$crystal = 24000000  
  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART connected to PA0 and PA1  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
  
Config Dcf77 = PINB.2 , Timer = Tca0 , Debug = 1 , Check = 1 , Gosub = Sectic  
  
Enable Interrupts  
Config Date = Dmy , Separator =DOT  
  
  
Dim I As Integer  
Dim Sec_old As Byte , Dcfsec_old As Byte  
  
```
Sec_old = 99 : Dcfsec_old = 99  
  
```vb
' Testroutine für die DCF77 Clock  
Print "Test DCF77 Version 1.02"  
  
Print "Configuration"  
  
  
Do  
For I = 1 To 78  
Waitms 10  
If Sec_old <> _sec Then  
Exit For  
End If  
If Dcfsec_old <> Dcf_sec Then  
Exit For  
End If  
Next  
Waitms 220  
```
Sec_old = _sec  
Dcfsec_old = Dcf_sec  
```vb
Print Time$ ; " " ; Date$ ; " " ; Time(dcf_sec) ; " " ; Date(dcf_day) ; " " ; Bin(dcf_status) ; " " ; Bin(dcf_parity) ; " " ; Bin(dcf_bits) ; " " ; Bdcf_impuls ; " " ; Bdcf_pause '; " " ; db1 ; " " ; db2  
If Dcf_sec > 45 Then  
Reset Dcf_status.7  
End If  
Print "Timezone : " ; Dcf77timezone()  
Loop  
  
  
'optional, is called every second by the library  
```
Sectic:  
!nop  
```vb
Return  
  
  
End

```

---

## CONFIG DEBOUNCE

Action

Configures the delay time for the DEBOUNCE statement.

Syntax

CONFIG DEBOUNCE = time

Remarks

Time | A numeric constant which specifies the delay time in mS. The maximum delay is 65535.  
---|---  
  
When debounce time is not configured, 25 mS will be used as a default.

See also

[DEBOUNCE](debounce.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : deboun.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates DEBOUNCE

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Debounce = 30 'when the config statement is not used a default of 25mS will be used

'Debounce Pind.0 , 1 , Pr 'try this for branching when high(1)

```
Debounce Pind.0 , 0 , Pr , Sub

Debounce Pind.0 , 0 , Pr , Sub

```vb
' ^----- label to branch to

' ^---------- Branch when P1.0 goes low(0)

' ^---------------- Examine P1.0

'When Pind.0 goes low jump to subroutine Pr

'Pind.0 must go high again before it jumps again

'to the label Pr when Pind.0 is low

```
Debounce Pind.0 , 1 , Pr 'no branch

Debounce Pind.0 , 1 , Pr 'will result in a return without gosub

End

Pr:

```vb
Print "PIND.0 was/is low"

Return

```

---

## CONFIG DMA

Action

Configures the direct memory access (DMA) module of the XMEGA.

Syntax

CONFIG DMA=enabled|disabled, DOUBLEBUF=db, CPM=cpm

Remarks

DMA | By default the DMA is disabled. Use ENABLED to enable the module.   
---|---  
db | DOUBLE BUFFER This options will set the double buffer mode. By default is is DISABLED. To allow for continuous transfer, two channels can be interlinked so that the second takes over the transfer when the first is finished and vice versa. This is called double buffering. When a transmission is completed for the first channel, the second channel is enabled. When a request is detected on the second channel, the transfer starts and when this is completed the first channel is enabled again Modes : \- DISABLED : No double buffer enabled \- CH01 : Double buffer enabled on channel0/1 \- CH23 : Double buffer enabled on channel2/3 \- CH01CH23 : Double buffer enabled on channel0/1 and channel2/3  
cpm | Channel Priority Mode If several channels request data transfer at the same time a priority scheme is available to determine which channel is allowed to transfer data. Application software can decide whether one or more channels should have a fixed priority or if a round robin scheme should be used. A round robin scheme means that the channel that last transferred data will have the lowest priority Modes : RR : Round Robin CH0RR123 : Channel0 > Round Robin (Channel 1, 2 and 3) CH01RR23 : Channel0 > Channel1 > Round Robin (Channel 2 and 3) CH0123 : Channel0 > Channel1 > Channel2 > Channel3  
  
You also need to set the individual DMA channels using CONFIG DMACHx. 

See also

[CONFIG DMACHx](config_dmachx.md) , [START DMACHx](start.md) , [CONFIG EDMA](config_edma.md) , [CONFIG EDMAx](config_edmax.md)

Example

See [CONFIG DMACHx](config_dmachx.md)

---

## CONFIG DMACHx

Action

Configures the direct memory access (DMA) channel of the XMEGA.

Syntax

CONFIG DMACHx=enabled|disabled,BURSTLEN=bl, CHANRPT=chrpt, CTR=ctr, SINGLESHOT=ss, TCI=tci, EIL=eil,SAR=sar, SAM=sam,DAR=dar,DAM=dam, TRIGGER,trig, BTC=btc, REPEAT=rpt,SADR=sadr, DADR=dadr

Remarks

In order to understand the various options better, we first have a better look at DMA.

Normally, when you want to transfer data, the processor need to execute a number of operations.

The BASCOM MEMCOPY for example will use processor instructions like LD (load data) and ST(store data) in a loop.

If you want to clear 32KB of memory you need at least 32 K instructions. This will consume time, and all this time the processor can not handle other tasks.

In a PC, you do not want to use the processor to be busy when you load a file from disk. The DMA controller will handle this. It can move blocks of memory between devices.

You can also send for example an array in SRAM to an USART over DMA so the processor will not be busy handling the transfer from the Array to the USART. See also the example below.

There is also an example to receive bytes over USART to SRAM in the Bascom-AVR/Samples folders.

Before CONFIG DMACHx can be used you need to use Config Dma ([CONFIG_DMA](config_dma.md))

DMA Transaction

A complete DMA read and write operation between memories and/or peripherals is called a DMA transaction.

A transaction is done in data blocks and the size of the transaction (number of bytes to transfer) is selectable from software and controlled by the block size and repeat counter

settings. Each block transfer is divided into smaller bursts

Block Transfer and Repeat

The size of the block transfer is set by the Block Transfer Count Register, and can be anything from 1 byte to 64 KBytes.

A repeat counter can be enabled to set a number of repeated block transfers before a transaction is complete. The repeat is from 1 to 255 and unlimited repeat count can be achieved by

setting the repeat count to zero.

Burst Transfer

As the AVR CPU and DMA controller use the same data buses a block transfer is divided into smaller burst transfers. The burst transfer is selectable to 1, 2, 4, or 8 bytes.

This means that, if the DMA acquires a data bus and a transfer request is pending it will occupy the bus until all bytes in the burst transfer is transferred.

A bus arbiter controls when the DMA controller and the AVR CPU can use the bus. The CPU always has priority, so as long as the CPU request access to the bus, any pending burst transfer

must wait. The CPU requests bus access when it executes an instruction that write or read data to SRAM, I/O memory, EEPROM and the External Bus Interface

![dma](dma.jpg)

DMACHx | There are 4 DMA channels numbered 0-3. By default these DMA channels are disabled. Use ENABLED to enable the channel.   
---|---  
bl | BURSTLEN Each DMA channel has an internal transfer buffer that is used for 2, 4 and 8 byte burst transfers. When a transfer is triggered, a DMA channel will wait until the transfer buffer contains two bytes before the transfer starts. For 4 or 8 byte transfer, any remaining bytes is transferred as soon as they are ready for a DMA channel. The buffer is used to reduce the time the DMA controller occupy the bus. Options : \- 1 : 1 byte burst mode \- 2 : 2 byte burst mode \- 4 : 4 byte burst mode \- 8 : 8 byte burst mode  
chanrpt | Channel Repeat  Setting this bit enables the repeat mode. In repeat mode, this bit is cleared by hardware in the beginning of the last block transfer. The REPCNT register should be configured before setting the REPEAT bit. When using the CONFIG command, the compiler will handle this. Options : Enabled : enabled repeat mode Disabled : disabled repeat mode  
ctr | DMA Channel Transfer Request Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at the beginning of the data transfer Options : Enabled : request transfer  
ss | DMA Channel Single Shot Data transfer Setting this bit enables the single shot mode. The channel will then do a burst transfer of BL bytes on the transfer trigger. This bit can not be changed if the channel is busy.  Options : Enabled : enable SS mode.  
tci | DMA Channel Transaction Complete Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
eil | DMA Channel Error Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
sar | Source Address Reload The channel source address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA source address register is reloaded with initial value at end of  
each block transfer. BURST : DMA source address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA source address register is reloaded with initial value at  
end of each transaction.  
sam | Source Address Mode The source address can be altered the following way : FIXED : The source address remains the same. INC : The source address is incremented by one.  DEC : The source address is decremented by one. If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte.  
dar | Channel Destination Address Reload The channel destiny address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA destiny address register is reloaded with initial value at end of  
each block transfer. BURST : DMA destiny address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA destiny address register is reloaded with initial value at  
end of each transaction.  
dam | Destiny Address Mode The destiny address can be altered the following way : FIXED : The destiny address remains the same. INC : The destiny address is incremented by one.  DEC : The destiny address is decremented by one. If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the destiny address is increased after each byte. In case of a byte array it would start with array(1) and the next byte would be array(2) which will be transferred and so on.  
trigger | Trigger Source Select The trigger selected which device triggers the DMA transfer. A zero (0) will disable a trigger. You can manual start a DATA TRANSFER with START DMACHx statement. You can find the hardware trigger values in the datasheet. For example, EVENTSYS channel 0 would be 1. And EVENSTYS channel 1 would be 1. In case of for example an USART you need to add the base value and add an offset. Example: Base value for USARTC0 is &H4B Offset for (RXC) Receive complete is &H00 Offset for (DRE) Data Register Empty is &H01 So when you want to use the DRE the trigger is &H4B + &H01 = &H4C  
btc | Block Transfer Count The BTC represents the 16-bit value TRFCNT. Which also means the max value is 64Kbyte. TRFCNT defines the number of bytes in a block transfer. The value of TRFCNT is decremented after each byte read by the DMA channel. When TRFCNT reaches zero, the register is reloaded with the last value written to it. When repeat is 1, this is the total amount of bytes to send in the DMA transaction.  
repeat | Repeat Counter Register REPCNTcounts how many times a block transfer is performed. For each block transfer this register will be decremented. Unlimited repeat is activated by setting this register to 0.  
sadr | Source Address This is the address of the DMA source. For example, the address of a variable. Or the address of a register. Use [VARPTR](varptr.md)() to find the address of a variable. For example if the source address is an array: sadr = varptr(ar(1)) For example if the source address is an hardware address like from an USART: sadr = Varptr(usarte0_data) or ADC A Channel 0: Sadr = Varptr(adca_ch0_res)  
dadr | Destination Address The destiny address.  This can be also for example an array in SRAM: dadr = varptr(dest(1)) This can be also for example a hardware recourse like USART: Dadr = Varptr(usarte0_data) or for example for DAC B Channel 0: Dadr = Varptr(dacb_ch0datal)  
  
After you have configured the DMA channel, you can start the transfer with the START DMACHx statement.

This will write the TRFREQ bit in the CTRLA register.

Setting the TRFREQ Bit (DMA Channel Transfer Request) requests a DATA TRANSFER on the DMA channel.

Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at

the beginning of the data transfer.

To enable the DMA Channel you need to set the Dma_chX_ctrla.7 bit.

For example for DMA Channel 0 this is Set Dma_ch0_ctrla.7

Setting this bit enables the DMA channel. This bit is automatically cleared when the transaction

is completed.

See also

[CONFIG DMA](config_dma.md) , [START DMACHx](start.md), [ATXMEGA](atxmega.md) , [CONFIG EDMA](config_edma.md) , [CONFIG EDMAx](config_edmax.md)

Example (copy SRAM Array to another SRAM Array over DMA):

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1-DMA.bas  
' This sample demonstrates DMA with an Xmega128A1  
'-----------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled 'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
dim ar(100) as byte, dest(100) as byte,j as byte ,w as word  
  
for j=1 to 100  
```
ar(j)=j ' create an array and assign a value  
```vb
next  
  
print "DMA DEMO"  
config dma= enabled, doublebuf=disabled,cpm = RR ' enable DMA  
  
'you can configure 4 DMA channels  
config dmach0=enabled ,burstlen=8,chanrpt=enabled, tci=off,eil=off, sar=none,sam=inc,dar=none,dam=inc ,trigger=0,btc=100 ,repeat =1,sadr=varptr(ar(1)),dadr=varptr(dest(1))  
  
```
start dmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
for j=1 to 50  
print j;"-";ar(j);"-";dest(j) ' print the values  
next  
end

```
Example (send an array to USART over DMA):

  
```vb
'Terminal Output of following example:  
'(  
  
```
\----- Array to USART over DMA -----  
  
Hello Bascom  
Hello XMEGA  
  
```vb
')  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Priority = Static , Vector = Application , Lo = Enabled  
  
' DMA Interrupt  
On Dma_ch0 Dma_ch0_int  
'Interrupt will be enabled with Tci = XX in Config DMAX  
  
Config Com5 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM5:" For Binary As #5  
  
```vb
Dim My_array(15) As Byte  
Dim My_string As String * 14 At My_array(1) Overlay  
Dim Dma_ready As Bit  
Dim Dma_channel_0_error As Bit  
  
```
Enable_dmach0 Alias Dma_ch0_ctrla.7 'Enable DMA Channel 0  
  
```vb
Print #5 ,  
Print #5 , "----- Array to USART over DMA -----"  
Print #5 ,  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
'configure DMA channel  
Config Dmach0 = Disabled , Burstlen = 1 , Chanrpt = Disabled , Tci = Lo , Eil = Off , Singleshot = Enabled , Sar = Transaction , _  
```
Sam = Inc , Dar = None , Dam = Fixed , Trigger = &H8C , Btc = 14 , Repeat = 0 , Sadr = Varptr(my_array(1)) , Dadr = Varptr(usarte0_data)  
```vb
' BURSTLEN = 1  
' Tci = Lo , Eil = Off --> enable TRANSACTION COMPLETE Interrupt  
' Singleshot = Enabled --> Setting this bit enables the single shot mode. 

' The channel will then do a burst transfer of BL bytes on the transfer trigger.  
' SAR (Source Address Reload) = After each transaction  
' SAM = inc --> source address is increased after each byte  
' DAR = NONE --> No reload performed  
' DAM (Destiny Address Mode) --> Fixed --> The address remains the same  
' Trigger = &H8C --> Base Value of USARTE0 = &H8B + Offset for DRE (Data Register Empty)= 1 --> &H8C  
' BTC = 14 --> Block Transfer Count is 14 Byte  
' We start with Dmach0 = Disabled --> will be enabled when we need it  
  
' Start dmach0 --> will set the TRFREQ Bit (DMA Channel Transfer Request). 

' Setting this bit requests a DATA TRANSFER on the DMA channel.  
  
' We use here Enable_dmach0 Alias Dma_ch0_ctrla.7 This bit is automatically cleared when the DMA TRANSACTION is completed  
  
Enable Interrupts  
```
My_string = "Hello Bascom" + Chr(13) + Chr(10) ' Hello Bascom + Carriage Return + Line Feed  
  
Set Enable_dmach0 ' Enable the DMA Channel 0 (This bit is automatically cleard when transaction is completed)  
  
Bitwait Dma_ready , Set ' Wait until first DMA transaction is ready (DMA TRANSACTION COMPLETE Interrupt)  
Reset Dma_ready  
  
My_string = "Hello XMEGA" + Chr(13) + Chr(10)  
  
```vb
Set Enable_dmach0 ' Enable the DMA Channel 0 (This bit is automatically cleard when transaction is completed)  
  
End  
  
'----------[Interrupt Service Routines]-----------------------------------------  
  
' Dma_ch0_int is for DMA Channel ERROR Interrupt A N D for TRANSACTION COMPLETE Interrupt  
' Which Interrupt fired must be checked in Interrupt Service Routine  
  
```
Dma_ch0_int: ' DMA Transaction complete  
  
```vb
If Dma_intflags.0 = 1 Then ' Channel 0 Transaction Interrupt Flag  
Set Dma_intflags.0 ' Clear the Channel 0 Transaction Complete flag  
Set Dma_ready  
End If  
  
'(  
If Dma_intflags.4 = 1 Then ' Channel 0 ERROR Flag  
Set Dma_intflags.4 ' Clear the flag  
Set Dma_channel_0_error ' Channel 0 Error  
End If  
')  
  
Return

```

---

## CONFIG DMXSLAVE

Action

Configures the DMX-512 slave.

Syntax

CONFIG DMXSLAVE = com, Channels=nchannels, DmxStart = nstart, Store=nstore

Remarks

com | The UART you want to use for the communication with the DMX-512 bus. This depends on the micro processor. In most cases this is COM1.   
---|---  
Channels | A numeric constant that defines the maximum number of channels you can receive. When you like to process all DMX data, you need to use 512 since 512 is the maximum. When you make a simple device a number of 8 would be sufficient.  
DmxStart | The slave starting address. This is 1 by default. You will receive data starting at address 'Start'.  
Store | The number of bytes you will receive and store.  
  
You must chose the crystal/oscillator speed in a way that 250000 baud will give no errors. Typical 4, 8 and 16 MHz will work fine.

When you want to be sure, check the compiler report. It should have 0% error.

Since the DMX slave is running in interrupt mode on the background, you must ENABLE interrupts.

The serial interrupts used, is enabled by the CONFIG DMXSLAVE command.

So how does this work? When you configure the DMXSLAVE, it will receive data in interrupt mode. It will store the data into a byte arrays named _DMX_RECEIVED

The first byte stored into this array is the value for address 'DMXSTART' : the address you defined with DMXSTART.

The number of bytes stored in the array depends on the 'STORE' setting. 

Example : Config Dmxslave = Com1 , Channels = 16 , DmxStart = 3 , Store = 1 

This will setup an array _DMX_RECEIVED that can hold 16 bytes. So the maximum value for STORE would be 16 too. In the example our address is 3, and we store only address 3. 

We can dynamic change the DMXSTART address and the number of bytes to get !

For this purpose you can change the automatic generated internal variables _DMX_ADDRESS and _DMX_CHANNELS_TOGET

_DMX_ADDRESS defines the starting address. And _DMX_CHANNELS_TOGET defines the number of bytes to store after the address matches.

All platforms are supported. 

See also

NONE

Example

```vb
'-----------------------------------------------------------------

' dmx-receive.bas

' (c) 1995-2025 MCS Electronics

' this sample demonstates receiving a DMX datastream in the background

'-----------------------------------------------------------------

'we use a chip with 2 UARTS so we can print some data

$regfile = "m162def.dat"

'you need to use a crystal that can generate a good 250 KHz baud

'For example 8 Mhz, 16 or 20 Mhz

$crystal = 8000000

'define the stack

$hwstack = 40

$swstack = 32

$framesize = 32

'these are the pins we use. COM1/UART1 is used for the DMX data

' TX RX

' COM1 PD.1 PD.0 DMX

' COM2 PB.3 PB.2 RS-232

Config Dmxslave = Com1 , Channels = 16 , DMXstart = 3 , Store = 1

'this will set up the code. an array named _dmx_channels will contain the data

'the channels will define the size. So when you want to receive data for 8 channels, you set it to 8.

'the maximum size is 512 for retrieving all data

'START defines the starting address. By default it is 1. Thus the array will be filled starting at address 3 in the example

'STORE defines how many bytes you want to store

'By default, 1 channel is read. But you can alter the variable _dmx_channelels_toget to specify how many bytes you want to receive

'So essential you need to chose how many bytes you like to receive. Most slaves only need 1 - 3 bytes. It would be a waste of space to define more channels then,

'Then you set the slave address with the variable : _dmx_address , which is also set by the optional [START]

'And finally you chose how many bytes you want to receive that start at the specified address. You do this by setting the _dmx_channels_toget variable.

'Example :

' Config Dmxslave = Com1 , Channels = 16 , Start = 300 , Store = 4

' this would store the bytes from address 300 - 303. the maximum would be 315 since channels is set to 16

' Config Dmxslave = Com1 , Channels = 8 , Start = 1 , Store = 8

' this would store the bytes from address 1 - 8. the maximum would be 8 since channels is set to 8

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Open "COM2:" For Binary As #1

```vb
Print #1 , "MCS DMX-512 test"

'since DMX data is received in an ISR routine, you must enable the global interrupts

Enable Interrupts

Dim J As Byte

Do

If Inkey(#1) = 32 Then ' when you press the space bar

For J = 1 To _dmx_channels ' show the data we received

Print #1 , _dmx_received(j) ; " " ;

Next

Print #1,

```
Elseif Inkey(#1) = 27 Then 'you ca dynamic change the start address and the channels

```vb
Input #1 , "start " , _dmx_address

Input #1 , "channels " , _dmx_channels_toget

End If

Loop

'typical you would read a DIP switch and use the value as the address

End

```

---

## CONFIG DP

Action

This option sets the character used for the decimal point for singles and fusing.

Syntax

CONFIG DP= "dp"

Remarks

The decimal point is a dot (.) by default. The STR() and FUSING functions convert a single into a string. The fraction is separated by a dot. In a number of counties the comma is used as a separator. 

Old Syntax:

Valid options are : CONFIG DP = "." and CONFIG DP = ","

New preferred Syntax:

Valid options are : CONFIG DP = DOT and CONFIG DP = COMMA

This options only sets the character for str() and fusing for singles. In your code you still need to code with a dot : var = 1234.333

See also

NONE

Example

```vb
CONFIG DP = ","

Dim s as single

```
S = 1234.56

print s

---

## CONFIG EDMA

Action

Configures the enhanced direct memory access (DMA) module of the XMEGA.

Syntax

CONFIG EDMA=enabled|disabled, DOUBLEBUF=db, CPM=cpm , CHM=chm

Remarks

DMA | By default the DMA is disabled. Use ENABLED to enable the module.   
---|---  
db | DOUBLE BUFFER This options will set the double buffer mode. By default is is DISABLED. To allow for continuous transfer, two channels can be interlinked so that the second takes over the transfer when the first is finished and vice versa. This is called double buffering. When a transmission is completed for the first channel, the second channel is enabled. When a request is detected on the second channel, the transfer starts and when this is completed the first channel is enabled again Modes : \- DISABLED : No double buffer enabled \- CH01 : Double buffer enabled on channel0/1 \- CH23 : Double buffer enabled on channel2/3 \- CH01CH23 : Double buffer enabled on channel0/1 and channel2/3  
cpm | Channel Priority Mode If several channels request data transfer at the same time a priority scheme is available to determine which channel is allowed to transfer data. Application software can decide whether one or more channels should have a fixed priority or if a round robin scheme should be used. A round robin scheme means that the channel that last transferred data will have the lowest priority Modes : RR : Round Robin CH0RR123 : Channel0 > Round Robin (Channel 1, 2 and 3) CH01RR23 : Channel0 > Channel1 > Round Robin (Channel 2 and 3) CH0123 : Channel0 > Channel1 > Channel2 > Channel3  
chm | Channel Mode The channel mode selects the mode. Possible options for channel mode are : PER0123 : 4 peripheral channels 0,1,2,3 STD0 : 1 standard channel, 2 peripheral channels 2,3 STD2 : 2peripheral channels 0,1, 1 standard channel 2 STD02 : 2 standard channels 0,2  
  
You also need to set the individual EDMA channels using CONFIG EDMACHx. 

See also

[CONFIG DMACHx](config_dmachx.md) , [START DMACHx](start.md) , [CONFIG DMA](config_dma.md) , [CONFIG EDMAx](config_edmax.md)

Example

See [CONFIG DMACHx](config_dmachx.md)

---

## CONFIG EDMAx

Action

Configures the enhanced direct memory access (DMA) channel of the XMEGA.

Syntax

CONFIG EDMACHx=enabled|disabled,BURSTLEN=bl, CHANRPT=chrpt, CTR=ctr, SINGLESHOT=ss, TCI=tci, EIL=eil,SAR=sar, SAM=sam,DAR=dar,DAM=dam, TRIGGER,trig, BTC=btc,SADR=sadr, DADR=dadr

Remarks

In order to understand the various options better, we first have a quick look at DMA. Please consult the help topic [CONFIG DMAx](config_dmachx.md) and the atmel documentation for the EDMA.

Normally, when you want to transfer data, the processor need to execute a number of operations.

The BASCOM MEMCOPY for example will use processor instructions like LD (load data) and ST(store data) in a loop.

If you want to clear 32KB of memory you need at least 32 K instructions. This will consume time, and all this time the processor can not handle other tasks.

In a PC, you do not want to use the processor to be busy when you load a file from disk. The EDMA controller will handle this. It can move blocks of memory between devices while the processor performs other tasks.

You can also send for example an array in SRAM to an USART over EDMA so the processor will not be busy handling the transfer from the Array to the USART.

There is also an example to receive bytes over USART to SRAM in the Bascom-AVR/Samples folders.

Before CONFIG EDMACHx can be used you need to use Config EDMA ([CONFIG_DMA](config_edma.md))

DMACHx | There are 4 DMA channels numbered 0-3. By default these DMA channels are disabled. Use ENABLED to enable the channel.   
---|---  
bl | BURSTLEN Each DMA channel has an internal transfer buffer that is either 1 or 2 byte long. The buffer is used to reduce the time the DMA controller occupy the bus. Options : \- 1 : 1 byte burst mode \- 2 : 2 byte burst mode  
chanrpt | Channel Repeat  Setting this bit enables the repeat mode. In repeat mode, this bit is cleared by hardware in the beginning of the last block transfer. Options : Enabled : enabled repeat mode Disabled : disabled repeat mode  
ctr | DMA Channel Transfer Request Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at the beginning of the data transfer Options : Enabled : request transfer  
ss | DMA Channel Single Shot Data transfer Setting this bit enables the single shot mode. The channel will then do a burst transfer of BL bytes on the transfer trigger. This bit can not be changed if the channel is busy.  Options : Enabled : enable SS mode.  
tci | DMA Channel Transaction Complete Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
eil | DMA Channel Error Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
sar | Source Address Reload The channel source address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA source address register is reloaded with initial value at end of  
each block transfer. BURST : DMA source address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA source address register is reloaded with initial value at  
end of each transaction.  
sam | Source Address Mode The address can be altered the following way : FIXED : The address remains the same. INC : The address is incremented by one  If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte.  
dar | Channel Destination Address Reload The channel destiny address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA destiny address register is reloaded with initial value at end of  
each block transfer. BURST : DMA destiny address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA destiny address register is reloaded with initial value at  
end of each transaction.  
dam | Destiny Address Mode The address can be altered the following way : FIXED : The address remains the same. INC : The address is incremented by one  If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte. In case of an byte array it would start with array(1) and the next byte would be array(2) which will be transferred and so on.  
trigger | Trigger Source Select The trigger selected which device triggers the DMA transfer. A zero (0) will disable a trigger. You can manual start a DATA TRANSFER with START DMACHx statement. You can find the hardware trigger values in the datasheet. For example, EVENTSYS channel 0 would be 1. And EVENSTYS channel 1 would be 1. In case of for example an USART you need to add the base value and add an offset. Example: Base value for USARTC0 is &H4B Offset for (RXC) Receive complete is &H00 Offset for (DRE) Data Register Empty is &H01 So when you want to use the DRE the trigger is &H4B + &H01 = &H4C  
btc | Block Transfer Count The BTC represents the 16-bit value TRFCNT. Which also means the max value is 64Kbyte. TRFCNT defines the number of bytes in a block transfer. The value of TRFCNT is decremented after each byte read by the DMA channel. When TRFCNT reaches zero, the register is reloaded with the last value written to it. When repeat is 1, this is the total amount of bytes to send in the DMA transaction.  
sadr | Source Address This is the address of the DMA source. For example, the address of a variable. Or the address of a register. Use [VARPTR](varptr.md)() to find the address of a variable. For example if the source address is an array: sadr = varptr(ar(1)) For example if the source address is an hardware address like from an USART: sadr = Varptr(usarte0_data) or ADC A Channel 0: Sadr = Varptr(adca_ch0_res)  
dadr | Destination Address The destiny address.  This can be also for example an array in SRAM: dadr = varptr(dest(1)) This can be also for example a hardware recourse like USART: Dadr = Varptr(usarte0_data) or for example for DAC B Channel 0: Dadr = Varptr(dacb_ch0datal)  
  
After you have configured the DMA channel, you can start the transfer with the START EDMACHx statement.

This will write the TRFREQ bit in the CTRLA register.

Setting the TRFREQ Bit (DMA Channel Transfer Request) requests a DATA TRANSFER on the EDMA channel.

Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at

the beginning of the data transfer.

See also

[CONFIG DMA](config_dma.md) , [START DMACHx](start.md), [ATXMEGA](atxmega.md) , [CONFIG EDMA](config_edma.md)

Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1-DMA.bas  
' This sample demonstrates DMA with an Xmega32E5  
'-----------------------------------------------------------------  
$regfile = "xm32e5def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Dim Ar(100) As Byte , Dest(100) As Byte , J As Byte , W As Word  
  
For J = 1 To 100  
```
Ar(j) = J ' create an array and assign a value  
```vb
Next  
  
Print "DMA DEMO"  
Config Edma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
  
'you can configure 4 DMA channels  
Config Edmach0 = Enabled , Burstlen = 1 , Chanrpt = Enabled , Tci = Off , Eil = Off , Sar = None , Sam = Inc , Dar = None , Dam = Inc , Trigger = 0 , Btc = 100 , Sadr = Varptr(ar(1)) , Dadr = Varptr(dest(1))  
  
```
Start Edmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
For J = 1 To 50  
Print J ; "-" ; Ar(j) ; "-" ; Dest(j) ' print the values  
Next  
End

```

---

## CONFIG EEPROM

Action

Setup memory mode for EEPROM in XMEGA.

Syntax

CONFIG EEPROM=mode

Remarks

mode | MAPPED, or QUICK. In Xmega, the EEPROM can be mapped into memory so it can be used with pointer operations such as LD,ST,LDS and STS. When EEPROM is mapped, EEPROM memory will start at &H1000. The advantage of mapping the EEPROM is that reading the EEPROM becomes much more simpler.  When you use the BASCOM EEPROM routines, you must include this statement before you use the EEPROM. To maintain compatibility with code and other AVR chips you can still use address 0 for the EEPROM. The library will add an offset of &H1000 to the address.  When you use the QUICK mode, you also use mapped mode but for read operations, the library read routine will not be used but instead the address is internally increased with &H1000 and a normal pointer operation is used. This allows code like : If SomeEEPROMvar = 10000 Then  End If  
---|---  
  
See also

[Memory usage](memory_usage.md)

Example

Config Eeprom = Mapped

---

## CONFIG ERROR

Action

Instructs the compiler to ignore one or more errors.

Syntax

CONFIG ERROR=ignore, err=ignore [err1=ignore]

Remarks

In some situations you might want to ignore an error. For example if a new version adds a certain check that was not available in a previous version you will get errors. If you ignore the error, the code will compile without errors. This will not work in any situation. Some errors can not be ignored. You should never use this option for a finished product. 

See also

NONE

Example

Config Error = Ignore , 369 = Ignore

Lbl:

Dim Lbl As Word ' this would generate an error 369 without the ignore !!!

---

## CONFIG EVENT_SYSTEM

Action

This statement configures the Xmega event routing.

Syntax

CONFIG EVENT_SYSTEM = dummy, MUXx=MUX, QDx=QD, QDIx=QDI, QDIRMx=QDIRM,DIGFLTx=DIGFLT

The letter X is used to indicate that a value between 0 and 7 can be used. So there is MUX0, MUX1, MUX2,MUX3 etc.

Remarks

The Event System is a set of features for inter peripheral communication. It enables the possibility

for a change of state in one peripheral to automatically trigger actions in other peripherals.

The change of state in a peripheral that will trigger actions in other peripherals is configurable in

software. It is a simple, but powerful system as it allows for autonomous control of peripherals

without any use of interrupt, CPU or DMA resources.

There are 8 multiplexers and 8 control registers. Register 0, 2 and 4 can be used for quadrature decoding. 

MUX | There are 8 multiplexers, named MUX0-MUX7. The MUX is used to select an event source.There are many sources for events : NONE : disabled, default RTC_OVF : Real Timer overflow RTC_CMP : Real Timer compare match ACA_CH0 : analog comparator ACA, channel 0 ACA_CH1 : analog comparator ACA, channel 1 ACA_WIN : analog comparator ACA, window ACB_CH0 : analog comparator ACB, channel 0 ACB_CH1 : analog comparator ACB, channel 1 ACB_WIN : analog comparator ACB, window ADCA_CH0- ADCA_CH3 : ADCA channel 0-3 ADCB_CH0- ADCB_CH3 : ADCB channel 0-3 PORTA.0 - PORTA.7 : PORT A pin 0-7 PORTB.0 - PORTB.7 : PORT B pin 0-7 PORTC.0 - PORTC.7 : PORT C pin 0-7 PORTD.0 - PORTD.7 : PORT D pin 0-7 PORTE.0 - PORTE.7 : PORT E pin 0-7 PORTF.0 - PORTF.7 : PORT F pin 0-7 PRESCALER1, PRESCALER2, PRESCALER4, PRESCALER8, PRESCALER16, PRESCALER32, PRESCALER64,PRESCALER128,PRESCALER256,PRESCALER512,PRESCALER1024,PRESCALER2048,PRESCALER4096,PRESCALER8192,PRESCALER16384 : The clock divided by 1,2,4,8,16,32,64,128,256 etc. TCC0_OVF : Timer TC0 overflow TCC0_ERR : Timer TC0 error TCC0_CCA : Timer TC0 capture or compare match A TCC0_CCB : Timer TC0 capture or compare match B TCC0_CCC : Timer TC0 capture or compare match C TCC0_CCD : Timer TC0 capture or compare match D TCC1_OVF : Timer TC1 overflow TCC1_ERR : Timer TC1 error TCC1_CCA : Timer TC1 capture or compare match A TCC1_CCB : Timer TC1 capture or compare match B TCC1_CCC : Timer TC1 capture or compare match C TCC1_CCD : Timer TC1 capture or compare match D Dito for TCD0, TCD1, TCE0, TCE1, TCF0 and TCF1  
---|---  
QD | Enables or disables the quadrature decoder. Will only work on QD0,QD2 and QD4.  
QDI | Enables or disables the quadrature decode index. Will only work on QDI0, QDI2 and QDI4.  
QDIRM | Quadrature decode index recognition mode. This is a numeric constant between 0 and 3. Each value represents the 2 possible bit values for the two input signals. Will only work on QDIRM0, QDIRM2 and QDIRM4.  
DIGFLT | Defines the length of digital filtering used. Events will be passed through to the event channel only when the event source has been active and sampled with the same level for a number of peripheral clock for the number of cycles as defined by DIGFLT.  The number of samples is in the range from 1-8. The default is 1 sample.  
|   
  
See also

[ATXMEGA](atxmega.md)

Example 1:  
  
```vb
' Select PortC.0 as INPUT to event channel 0  
' Digflt0 = 8 --> Enable Digital Filtering for Event Channel 0. 

' The Event must be active for 8 samples in order to be passed to the Event system  
' Event Channel 1 INPUT = Timer/Counter C0 Overflow  
' Event Channel 2 INPUT = Analog Input Port A Channel 0  
' Event Channel 3 INPUT = Real Timer overflow  
Config Event_system = Dummy , _  
```
Mux0 = Portc.0 , Digflt0 = 8 , _  
Mux1 = Tcc0_ovf , _  
Mux2 = Adca_ch0 , _  
Mux3 = Rtc_ovf

Example 2:

```vb
'Event Channel 7 is input for the Timer/Counter TcD1 overflow 

Config Event_system = Dummy , Mux7 = Tcd1_ovf 

```
Example 3:

  
```vb
' Using the Counter/Timer to count events like a falling edge on Pine.5  
  
$regfile = "xm256a3bdef.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 'Portf.2 and Portf.3 is COM7  
```
Open "COM7:" For Binary As #1  
  
```vb
'Config Interrupts  
Config Priority = Static , Vector = Application , Lo = Enabled , Med = Enabled 'Enable Lo Level Interrupts  
  
Dim Timer_overflow As Bit  
  
Print #1 , "---Event Counting with Timer C0 over Event Channel 0 from PINE.5----"  
  
Config Porte.5 = Input  
Config Xpin = Porte.5 , Outpull = Pullup , Sense = Falling 'enable Pullup and reaction on falling edge  
Config Event_system = Dummy , Mux0 = Porte.5 , Digflt0 = 8 'Eventchannel 0 = PINE.5, enable digital filtering

Config Tcc0 = Normal , Prescale = E0 , Event_source = E0 , Event_action = Capture' Normal = no waveform generation, Event Source = Event Channel 0  
  
On Tcc0_ovf Timerd0_int  
Enable Tcc0_ovf , Lo 'Enable overflow interrupt in LOW Priority  
```
Tcc0_per = 5 'Interrupt when Count > 5  
```vb
Enable Interrupts  
  
'################MAINLOOP#######################################################  
Do  
  
Wait 1  
Print #1 , "TCC0_CNT = " ; Tcc0_cnt 'Actual Count  
  
If Timer_overflow = 1 Then  
Reset Timer_overflow  
Print #1 , "TCC0_OVERVLOW" 'Print it when Overflow Interrupt is fired  
End If  
  
Loop  
'################MAINLOOP#######################################################  
  
  
End  
  
```
Timerd0_int:  
```vb
Set Timer_overflow  
Return

```

---

## CONFIG EVENT_SYSTEM XTINY

Action

This statement configures the Xtiny event routing.

Syntax

```vb
CONFIG EVENT_SYSTEM = dummy, ASYNCCHx=asyncX,SYNCCHy=syncY,ASzz=asyncUserZZ,Sn=syncUserN

CONFIG EVENT_SYSTEM = dummy, ASYNCCH0=asyncX,SYNCCH00=syncY,AS00=asyncUserZZ,S0=syncUserN

```
Remarks

The Event System (EVSYS) enables direct peripheral-to-peripheral signaling. It allows a change in one peripheral (the Event Generator) to trigger actions in other peripherals (the Event Users) through Event

channels, without using the CPU. It is designed to provide short and predictable response times between peripherals, allowing for autonomous peripheral control and interaction, and also for synchronized timing

of actions in several peripheral modules. It is thus a powerful tool for reducing the complexity, size, and execution time of the software.

A change of the Event Generator's state is referred to as an Event, and usually corresponds to one of the peripheral's interrupt conditions. Events can be directly forwarded to other peripherals using the

dedicated Event routing network. The routing of each channel is configured in software, including event generation and use.

Only one trigger from an Event generator peripheral can be routed on each channel, but multiple channels can use the same generator source. Multiple peripherals can use events from the same channel.

A channel path can be either asynchronous or synchronous to the main clock. The mode must be selected based on the requirements of the application.

The Event System can directly connect analog and digital converters, analog comparators, I/O port pins, the real-time counter, timer/counters, and the configurable custom logic peripheral. Events can also be generated from software and the peripheral clock.

The are 4 asynchronous event channels (ASYNCCHx) and 2 synchronous event channels(SYNCCHy). 

ASYNCCHx | Async channel x where x is in the range from 0 to 3.  Each channel has different generators of events. For channels 0-3 : CCL_LUT0 CCL_LUT1 AC0_OUT TCD0_CMPBCLR TCD0_CMPASET TCD0_CMPBSET TCD0_PROGEV RTC_OVF RTC_CMP Channel 0 also has the following sources: PORTA.0 - PORTA.7 UPDI Channel 1 also had the following sources : PORTB.0 - PORTB.7 Channel 2 also had the following sources : PORTC.0 - PORTB.5 Channel 4 also had the following sources : PIT_DIV8192 - PIT_DIV64  
---|---  
SYNCCHy | Synchroneous channely where y is in the range from 0-1. Each channel has different generators of events. For channel 0-1 : TCB0 TCA0_OVF_LUNF TCA0_HUNF TCA0_CMP0 TCA0_CMP1 TCA0_CMP2 Channel 0 also has the following sources: PORTC.0 - PORTC.5 PORTA.0- PORTA.7 Channel 1 also has the following sources: PORTB.0 - PORTB.7  
ASzz | Asynchronous user channel input selection. There are 11 channels in the range from 0-10. Each channel selects different input which is fixed for each channel. 00 : TCB0 01 : ADC0 02 : CCL_LUT0EV0 03 : CCL_LUT1EV0 04 : CCL_LUT0EV1 05 : CCL_LUT1EV1 06 : TCD0_EV0 07 : TCD0_EV1 08 : EVOUT0 09 : EVOUT1 10 : EVOUT2 The values are fixed : \- OFF \- SYNCCH0 \- SYNCCH1 \- ASYNCCH0 \- ASYNCCH1 \- ASYNCCH2 \- ASYNCCH3  
Sn | Synchronous user channel input selection. There are 2 channels in the range from 0-1. Each channel selects different input which is fixed for each channel. 00 : TCA0 01 : USART0 The values are fixed : \- OFF \- SYNCCH0 \- SYNCCH1  
  
See also

[ ](atxmega.md)

---

## CONFIG EXTENDED_PORT

Action

Configures compiler to generate warning or error when transforming extended port register.

Syntax

CONFIG EXTENDED_PORT = WARNING|ERROR

Remarks

A lot of AVR chips have so called extended registers. When the AVR was designed the designers did not set aside enough space for the hardware registers. A number of instructions work only with the lower 32 addresses, and a number only work on registers with an address till &H3F.

SRAM memory was moved up and the space after &H5F was used for registers. These are extended registers.

For these chips, the SRAM starts at &H100 or higher. 

Because INP, OUT, SBI, SBI, SBIC, SBIS, etc. will not work on these extended registers, the compiler changes this automatic when needed. When INP or OUT is used, this is not a problem. LDS or STS can be used with the same register.

But an instruction like SBIC that will test a pin , needs a temporarily register. Register R23 is used for this.

When you write your own ASM you might want to get a warning or an error. For this purpose you can use CONFIG EXTENDED_PORT.

When you use WARNING there will be a warning in the report file. When you use ERROR, you will get an error and your code will not compile.

See also

NONE

---

## CONFIG FT800

Action

This compiler option is required to setup the FT8xx SPI interface.

Syntax

CONFIG FT8xx = spi [, FTSAVE=ftsave , FTDEBUG=ftdebug] , FTCS=ftcs [, FTPD = ftpd] [,FTCHIP=800|801] [,PLATFORM=platform] [,LCD_SCREEN-lcdscr] [,LCD_ROTATE=lcdrotate] [,LCD_CALIBRATION=calib]

Remarks

spi | The SPI interface used for the FT800/FT801/FT810 processor. This may be : \- SPI, for normal AVR processors \- SPI*, SPIC, SPID, SPIE, SPIF, for XMEGA processors. * When you use SPI on an XMEGA processor, the compiler will use SPIC, the default SPI.  
---|---  
ftsave | This is an optional parameter with a default of 0. The possible values are 0 and 1. With this option enabled, the parameters passed to the various FT800 routines are limited in range. For example when a parameter is expected in the range from 0-31 it would not matter if you pass 32. But limiting the range increases code. It is best to make sure yourself that you pass the proper values.   
ftdebug | This is an optional parameter with a default of 0. The possible values are 0 and 1. With this option enabled, the SPI communication can be monitored. A label named _FTDBG is called in your code. So when using this option you need to insert this label into your code. You also need to DIM a byte named ftdebug. This byte will be filled with the parameter sent to the SPI.  Make sure you put a RETURN after the label and save registers you use: _FTDBG Pushall print hex(ftdebug) Popall RETURN  
FTCS | The name of the SPI port pin connected to the CS pin of the FT800. This would be SS in most cases. This pin is set to output and to logic level 1.  
FTPD | The name of the port pin connected to the PD pin of the FT800. This is an optional pin, it depends on your hardware. Gameduino2 does not require it. EVE demo boards do require this pin.  
FTCHIP | The kind of FT chip. FT800 is the default and when used, FTCHIP does not need to be specified. FT801 is similar to the FT800 but has a capacitive touch screen and gestures support. Possible values :  \- 800 : FT800 (default) \- 801 : FT801 \- 810, 811,812, 813 : FT81x  
PLATFORM | The used hardware platform. Default is EVE from FTDI. Possible values : \- EVE (default) \- GAMEDUINO2 : popular alternative FTDI hardware  
LCD_SCREEN | The kind of LCD screen. Possible values :  480272 : 480x272 pixels LCD (default) 320240 : 320x240 pixels LCD 800480 : 800x480 pixels LCD 800600 : 800x600 pixels LCD As you might have noticed, the value is the same as the screen size without the x.   
LCD_ROTATE | The LCD can be used in normal horizontal mode or upside down 180 degrees.  Possible values : \- 0 : horizontal (default) \- 1 : 180 degrees rotated  
LCD_CALIBRATION | The LCD requires calibration. This need to be done once but you can force calibration using LCD_CALIBRATION parameter. Possible values : \- 0 : No calibration \- 1 : Force Calibration (default)  
  
The CONFIG FT800 statement will inform the compiler to use the FT800.LIB. It will also create an ALIAS for the CS and PD pins you specify.

The FT800 is controlled by the SPI interface. This means that you need to configure the SPI the usual way.

![notice](notice.jpg)Since FT800 was the first graphic processor, you will find FT800 mentioned in the help. But as of version 2080, there is also support for the new FT810 chip.

BASCOM FT8xx support is implemented in the following way:

\- a low level communication library FT800.LIB

\- ASM include macros which are located in the FT800.LIB. Unlike sub routines, the code is included and not called. 

\- BASCOM high level commands such as CMD32, RD8(), RD16(), etc.

\- FT80x include files : an include file with the declarations (FT81x.INC) and an include file with the actual code (FT81x_FUNCTIONS.INC).

You may modify the code from the include files. The code will reveal some new options. It is important to understand these new options.

\- Passing values using [BYREG](declare_sub.md)

\- Passing values using [BYSTACK](declare_sub.md)

\- [CMDFTSTACK](cmdftstack.md)

In version 2079, FT801 support is included. A number of constants are removed from the include file and are now a parameter of CONFIG FT800. These constants are : FT_PlatForm , FT_LCDscreen , FT_LcdCal , FT_RotateDisplay and FT_CHIP. These constants are remarked for reference.

Here are some sample configurations

AdamShield:

Config FT800 = Spi , Ftsave = 0 , Ftdebug = 0 , Ftcs = Portd.4 , Ftpd = Portd.3, ftChip=800, LcdScreen=480272, PlatForm=Eve 

GAMEDUINO2:

Config FT800=spi , ftsave=0, ftdebug=0 , ftcs=portb.0, ftChip=800, LcdScreen=480272, PlatForm=Gameduino2

VM801P - FTDI:

Config FT800 = Spi , ftsave = 0, ftdebug = 0 , Ftcs = Portb.1 , Ftpd = Portd.4, ftChip=801, LcdScreen=480272, PlatForm=Eve, Lcd_Rotate=1, Lcd_Calibration=0

See also

[FT800](ft800.md) , [CMDFTSTACK](cmdftstack.md) , [CMD32](cmd32.md) , [RD8](rd8.md), [RD16](rd16.md), [RD32](rd32.md) , [WR32](wr32.md)

Partial Example

```vb
' FT800 Gauges Application demonstrating interactive Gauges using Lines & Custom Font  
' FT800 platform.  
' Original code from http://www.ftdichip.com/Support/SoftwareExamples/EVE/FT_App_Gauges.zip  
' Requires Bascom 2.0.7.8 or greater  
  
$Regfile = "M328pdef.dat"  
$Crystal = 8000000  
$Baud = 19200  
$HwStack = 90  
$SwStack = 90  
$FrameSize = 300  
$NOTYPECHECK  
  
Config ft800=spi , ftsave=0, ftdebug=0 , ftcs=portb.2, ftpd=portb.1  
  
Config Base = 0  
Config Submode = New  
Config Spi = Hard , Interrupt = Off , Data_Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4, Noss = 1  
```
SPSR = 1 ' Makes SPI run at 8Mhz instead of 4Mhz  
  
  
```vb
' Swaps Scales  
' 1 = Resitive - Random  
' 0 = Random - Resistive  
```
Const Resistive = 0  
  

#If Resistive = 0  
Const First = 1  
Const Second = 0  

#Else  
Const First = 0  
Const Second = 1  

```vb
#EndIf  
  
$Include "FT80x.inc"  
$Include "FT80x_Functions.inc"  
  
Declare Sub cs(Byval i As Byte)  
Declare Function da (Byval i As Long) As Word  
Declare Sub Polar(byval R As Long , Byval Th As Word)  
Declare Sub Polarxy(byval R As Long , Byval Th As Word , Byref X As Long , Byref Y As Long)  
Declare Sub IntroFTDI  
Declare Sub Gauges  
Declare Function Read_Keys() As Byte  
  
' General Program Variables and Declarations  
Dim temp_tag As Byte  
Dim ox As Long  
  
  
```
Spiinit  
  
if FT800_Init()=1 then end ' Initialise the FT800

  
Gauges  
  
```vb
Do

  
Loop  
  
```
Remark

In the samples,  Noss = 1 is used for CONFIG SPI. This means that the SS pin must be set by the user. In case of CONFIG FT800, the compiler always set the specified pin for FTCS to output and to logic 1. When possible you should use NOSS=0 and use the dedicated SPI SS pin. But for multiple SPI devices on the bus that is not possible since you will have multiple CS pins, and in these cases you should use NOSS=1, so you can control the SS logic level.

---

## CONFIG FUSES

Action

This configuration option sets the value of Xtiny,MegaX and AVRX fuses and lock bits.

Syntax

CONFIG FUSES=ON|OFF, LOCK=ON|OFF,FUSEx=f,urowx=u 

Remarks

The MCS UPDI programmer can insert the current fuse values into the code. You can also create the values yourself.

FUSES | ON or OFF.  ON - When programming the specified fuses will be programmed. OFF- When programming there will be no automatic programming When the CONFIG FUSES is inserted the value will also be set to OFF. So you must manually change it to ON.   
---|---  
LOCK | ON or OFF. ON - When ON and FUSES=ON, the lock bit will be programmed when the processors is programmed.  OFF- When programming the LOCK bits will be ignored. Thus the processor will not be locked.  When CONFIG FUSES is inserted the value will be set to OFF. So you need to manually set it to ON when you want the processor to be locked. Please take in mind that when the processor is locked you can not program it any longer. You need to use the UNLOCK option.  
FUSEx | The x is in the range from 0 to 7 depending on the processor. Some processors might have even more fuses.   
f | The value the fuse is set too. This is a numeric constant.   
UROWx | The x is in the range from 0 to 31 or less/more depending on the processor.  Userrow fuses can be set by the user. They can be read in your code by their register.   
  
The Xtiny/MegaX/AVRX platform has a lot of fuses. 

The advised method of getting the proper CONFIG FUSES :

\- set the fuses using the programmer Lock & Fuses TAB. 

\- do not set the lock byte. 

\- when satisfied, set the cursor at the proper place in your code

\- click the WRITE CONFIG button.

For example :

![mcs_updi_lock_fuse](mcs_updi_lock_fuse.png)

This will create this line of code : Config Fuses=Off,Lock=OFF,Fuse0=&H00,Fuse1=&H00,Fuse2=&H00,Fuse5=&HC9,Fuse6=&H00,Fuse7=&H00,Fuse8=&H00

As you can see, a fuse will only be listed when the value differs from the value 255 (&HFF)

See also

[$PROG](_prog.md)

Example

Config Fuses=Off,Lock=OFF,Fuse0=&H00,Fuse1=&H00,Fuse2=&H00,Fuse5=&HC9,Fuse6=&H00,Fuse7=&H00,Fuse8=&H00

---

## CONFIG GRAPHLCD

Action

Configures the Graphical LCD display.

Syntax

Config GRAPHLCD = type , DATAPORT = port, CONTROLPORT=port , CE = pin , CD = pin , WR = pin, RD=pin, RESET= pin, FS=pin, MODE = mode

Remarks

Type | This must be 240X64, 128X128, 128X64 , 160X48 , 240X128, 192X64 , SED180X32 or 192X64SED. For SED displays use 128X64sed or 120X64SED or SED180X32 For 132x132 color displays, use COLOR For EADOG128x64 use 128X64EADOGM  For SSD1325 96x64 use 96X64SSD1325. See [SSD1325lib](glcdssd1325_96x64.md). For custom libs : CUSTOM.  The following options are optional for custom LCD: \- cols= num of cols in pixels \- rows= num of rows in pixels \- kind= any number to specify the lcd \- lcdname="somename" , an optional name to identify the LCD  
---|---  
Dataport | The name of the port that is used to put the data on the LCD data pins db0-db7. PORTA for example.  
Controlport | This is the name of the port that is used to control the LCD control pins. PORTC for example  
Ce | The pin number that is used to enable the chip on the LCD.  
Cd | The pin number that is used to control the CD pin of the display.  
WR | The pin number that is used to control the /WR pin of the display.  
RD | The pin number that is used to control the /RD pin of the display.  
FS | The pin number that is used to control the FS pin of the display. Not needed for SED based displays.  
RESET | The pin number that is used to control the RESET pin of the display.  
MODE | The number of columns for use as text display. Use 8 for X-pixels / 8 = 30 columns for a 240 pixel screen. When you specify 6, 240 / 6 = 40 columns can be used.  
  
| EADOG128M pins for SPI mode. This display only can write data. As a result, a number of graphical commands are not supported.  
CS1 | Chip select for EADOG128x64  
A0 | A0 line for EADOG128x64. This is the line that controls data/command  
SI | This is the serial input pin for the EADOG128x64.   
SCLK | This is the clock pin for the EADOG128x64.  
  
| ST7565R parallel data mode A 128x64 graphical display which supports all graphic commands  
dataport | The data port connected to the display. For example portJ  
CS1 | the chip enabled line  
A0 | the chip data/command mode pin  
RST | the reset pin of the chip  
WR | The /WR line of the chip  
RD | The /RD line of the chip  
C86 | This pin selects the transfer mode.  
PM | Some displays have this PM pin which sets the parallel mode  
example  | Config Graphlcd = 128 * 64eadogm ,dataport=portj, Cs1 = Porth.0 , A0 = Porth.2 , rst= Porth.1 , wr = Porth.3 , Rd = Porth.4,c86=porth.6  
  
The first graphical LCD chip supported was T6963C. There are also drivers for other LCD's such as SED and KS0108. The most popular LCD's will be supported with a custom driver.

The following connections were used for the T6963C:

PORTA.0 to PORTA.7 to DB0-DB7 of the LCD

PORTC.5 to FS, font select of LCD

PORTC.2 to CE, chip enable of LCD

PORTC.3 to CD, code/data select of LCD

PORTC.0 to WR of LCD, write

PORTC.1 to RD of LCD, read

PORTC.4 to RESET of LCD, reset LCD

The LCD used from www.conrad.de needs a negative voltage for the contrast.

Two 9V batteries were used with a pot meter.

Some displays have a Vout that can be used for the contrast(Vo)

The T6963C displays have both a graphical area and a text area. They can be used together. The routines use the XOR mode to display both text and graphics layered over each other.

The statements that can be used with the graphical LCD are :

[CLS](cls.md), will clear the graphic display and the text display

CLS GRAPH will clear only the graphic part of the display

CLS TEXT will only clear the text part of the display

[LOCATE](locate.md) row,column : Will place the cursor at the specified row and column

The row may vary from 1 to 16 and the column from 1 to 40. This depends on the size and mode of the display.

[CURSOR](cursor.md) ON/OFF BLINK/NOBLINK can be used the same way as for text displays.

[LCD](lcd_2.md) : can be handled the same way as for text displays.

[SHOWPIC](showpic.md) X, Y , Label : Show image where X and Y are the column and row and Label is the label where the picture info is placed.

[PSET](pset.md) X, Y , color : Will set or reset a pixel. X can range from 0-239 and Y from 9-63. When color is 0 the pixel will turned off. When it is 1 the pixel will be set on.

[$BGF](_bgf.md) "file.bgf" : inserts a BGF file at the current location

[LINE](line.md)(x0,y0) â (x1,y1) , color : Will draw a line from the coordinate x0,y0 to x1,y1.

Color must be 0 to clear the line and 255 for a black line.

[BOX](box.md)(x0,y0)-(x1,y1), color : Will draw a box from x0,y0 to x1,y1. Color must be 0 to clear the box and 255 for a black line.

[BOXFILL](boxfill.md)(x0,y0)-(x1,y1), color : Will draw a filled box from x0,y0 to x1,y1. Color must be 0 or 255.

The Graphic routines are located in the glib.lib or glib.lbx files.

You can hard wire the FS and RESET and change the code from the glib.lib file so these pins can be used for other tasks.

COLOR LCD

Color displays were always relatively expensive. The mobile phone market changed that. And Display3000.com , sorted out how to connect these small nice colorful displays.

You can buy brand new Color displays from Display3000. MCS Electronics offers the same displays.

There are two different chip sets used. One chipset is from EPSON and the other from Philips. For this reason there are two different libraries. When you select the wrong one it will not work, but you will not damage anything.

LCD-EPSON.LBX need to be used with the EPSON chipset.

LCD-PCF8833.LBX need to be used with the Philihps chipset.

Config Graphlcd = Color , Controlport = Portc , Cs = 1 , Rs = 0 , Scl = 3 , Sda = 2

Controlport | The port that is used to control the pins. PORTA, PORTB, etc.  
---|---  
CS | The chip select pin of the display screen. Specify the pin number. 1 will mean PORTC.1  
RS | The RESET pin of the display  
SCL | The clock pin of the display  
SDA | The data pin of the display  
  
As the color display does not have a built in font, you need to generate the fonts yourself.

You can use the [Fonteditor](font_editor.md) for this task.

A number of statements accept a color parameter. See the samples below in bold.

LINE | Line(0 , 0) -(130 , 130) , Blue  
---|---  
LCDAT | Lcdat 100 , 0 , "12345678" , Blue , Yellow  
CIRCLE | Circle(30 , 30) , 10 , Blue  
PSET | 32 , 110 , Black  
BOX | Box(10 , 30) -(60 , 100) , Red  
  
See also

[SHOWPIC](showpic.md) , [PSET](pset.md) , [$BGF](_bgf.md) , [LINE](line.md) , [LCD](lcd_1.md) , [BOX](box.md) , [BOXFILL](boxfill.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : t6963_240_128.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : T6963C graphic display support demo 240 * 128

'micro : Mega8535

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m8535.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'-----------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' T6963C graphic display support demo 240 * 128

'-----------------------------------------------------------------

'The connections of the LCD used in this demo

'LCD pin connected to

' 1 GND GND

'2 GND GND

'3 +5V +5V

'4 -9V -9V potmeter

'5 /WR PORTC.0

'6 /RD PORTC.1

'7 /CE PORTC.2

'8 C/D PORTC.3

'9 NC not conneted

'10 RESET PORTC.4

'11-18 D0-D7 PA

'19 FS PORTC.5

'20 NC not connected

'First we define that we use a graphic LCD

' Only 240*64 supported yet

Config Graphlcd = 240 * 128 , Dataport = Porta , Controlport = Portc , Ce = 2 , Cd = 3 , Wr = 0 , Rd = 1 , Reset = 4 , Fs = 5 , Mode = 8

'The dataport is the portname that is connected to the data lines of the LCD

'The controlport is the portname which pins are used to control the lcd

'CE, CD etc. are the pin number of the CONTROLPORT.

' For example CE =2 because it is connected to PORTC.2

'mode 8 gives 240 / 8 = 30 columns , mode=6 gives 240 / 6 = 40 columns

'Dim variables (y not used)

Dim X As Byte , Y As Byte

'Clear the screen will both clear text and graph display

```
Cls

```vb
'Other options are :

' CLS TEXT to clear only the text display

' CLS GRAPH to clear only the graphical part

```
Cursor Off

```vb
Wait 1

'locate works like the normal LCD locate statement

' LOCATE LINE,COLUMN LINE can be 1-8 and column 0-30

```
Locate 1 , 1

'Show some text

Lcd "MCS Electronics"

'And some othe text on line 2

Locate 2 , 1 : Lcd "T6963c support"

Locate 3 , 1 : Lcd "1234567890123456789012345678901234567890"

Locate 16 , 1 : Lcd "write this to the lower line"

Wait 2

Cls Text

```vb
'use the new LINE statement to create a box

'LINE(X0,Y0) - (X1,Y1), on/off

```
Line(0 , 0) -(239 , 127) , 255 ' diagonal line

Line(0 , 127) -(239 , 0) , 255 ' diagonal line

Line(0 , 0) -(240 , 0) , 255 ' horizontal upper line

Line(0 , 127) -(239 , 127) , 255 'horizontal lower line

Line(0 , 0) -(0 , 127) , 255 ' vertical left line

Line(239 , 0) -(239 , 127) , 255 ' vertical right line

```vb
Wait 2

' draw a line using PSET X,Y, ON/OFF

' PSET on.off param is 0 to clear a pixel and any other value to turn it on

For X = 0 To 140

```
Pset X , 20 , 255 ' set the pixel

```vb
Next

For X = 0 To 140

```
Pset X , 127 , 255 ' set the pixel

```vb
Next

Wait 2

'circle time

'circle(X,Y), radius, color

'X,y is the middle of the circle,color must be 255 to show a pixel and 0 to clear a pixel

For X = 1 To 10

```
Circle(20 , 20) , X , 255 ' show circle

Wait 1

Circle(20 , 20) , X , 0 'remove circle

```vb
Wait 1

Next

Wait 2

For X = 1 To 10

```
Circle(20 , 20) , X , 255 ' show circle

```vb
Waitms 200

Next

Wait 2

'Now it is time to show a picture

'SHOWPIC X,Y,label

'The label points to a label that holds the image data

```
Test:

Showpic 0 , 0 , Plaatje

Showpic 0 , 64 , Plaatje ' show 2 since we have a big display

Wait 2

Cls Text ' clear the text

```vb
End

'This label holds the mage data

```
Plaatje:

```vb
'$BGF will put the bitmap into the program at this location

$bgf "mcs.bgf"

'You could insert other picture data here

```

---

## CONFIG HITAG

Action

Configures the timer and HITAG variables.

Syntax

```vb
CONFIG HITAG = prescale, TYPE=tp, DOUT = dout, DIN=din , CLOCK=clock, INT=int

CONFIG HITAG = prescale, TYPE=tp, DEMOD= demod, INT=@int

```
Remarks

syntax for HTRC110

prescale | The pre scaler value that is used by TIMER0. A value of 8 and 256 will work at 8 MHz.   
---|---  
tp | The kind of RFID chip you use. Use HTRC110.  
DOUT | The pin that is connected to the DOUT pin of the HTRC110. This pin is used in input mode since DOUT is an output. A pin that support the pin-change interrupt or the PCINT should be selected.  
DIN | The pin that is connected to the DIN pin of the HTRC110. This pin is used in output mode. You can chose any pin that can be used in output mode.  
CLOCK | The pin that is connected tot the CLOCK pin of the HTRC110. This pin is used in output mode. You can chose any pin that can be used in output mode.  
INT | The interrupt used. Note that you need to precede the interrupt with an @ sign. For example for INT1 you provide : @INT1  
  
syntax for EM4095

prescale | The pre scaler value that is used by TIMER0. A value of 8 and 256 will work at 8 MHz.   
---|---  
tp | The kind of RFID chip you use. Use EM4095.  
demod | The pin that is connected to the DEMOD pin of the EM4095. This pin is used in input mode. A pin that support the pin-change interrupt or the PCINT should be selected.  
INT | The interrupt used. Note that you need to precede the interrupt with an @ sign. For example for INT1 you provide : @INT1  
  
The CONFIG HITAG command will generate a number of internal used variables and constants.

Constants : _TAG_MIN_SHORT, _TAG_MAX_SHORT , _TAG_MIN_LONG and _TAG_MAX_LONG.

See the description of READHITAG to see how they are calculated. The actual value will depend on the prescaler value you use. 

Variables for HTRC110 :

_htr_statemachine , a byte that is used to maintain a state machine.

_htcbit , a byte that will hold the received bit. 

_htcbitcount , a byte to store the number of received bits.

_htcmpulse , a byte that stores the pulse

_htr_pulse_state , a byte that is used to maintain the pulse state machine. 

_htc_retries, a byte that is used for the number of retries. 

_tagdelta , a byte that will held the delta time between 2 edges. 

_tagtime , a byte with the actual timer0 value when an edge is detected.

_taglasttime , a byte with the previous edge time, needed to calculate the

delta time.

_tagparbit , a byte that will held the parity.

_tagdata , a byte where the bits are stored before they are loaded into the serial

number array. 

_tagid , a word that points to the serial number array

The HTRC110.LBX contains a number of other constants that are used to control the HTRC chip.

The _init_Tag routine is called automatically. 

![notice](notice.jpg)The clock output of the Mega88 is used to drive the HTRC110. Since the clock output of the internal oscillator is 8 MHz, the HTRC110 is also configured to work at 8 MHz.

The .equ for Tag_set_config_page3 = &H40 + 48 + Fsel0 in the LBX. You can set it to 12 and 16 MHz too but you can not drive it from the clock output then.

The datasheet specifies the following for FSEL1 and FSEL0

FSEL1 | FSEL0 | Frequency  
---|---|---  
0 | 0 | 4 MHz  
0 | 1 | 8 MHz  
1 | 0 | 12 MHz  
1 | 1 | 16 MHz  
  
So when you want to use a different frequency you can edit the equ in the lbx.

.equ Tag_set_config_page3 = &H40 + 48 + Fsel0 ' 8 Mhz

For 16 Mhz it would become :

.equ Tag_set_config_page3 = &H40 + 48 + Fsel0 + Fsel1 ' 8 Mhz

When you want to send a custom command you can call the internal routine : _Send_htrc110_cmdR25

Just load R25 with the proper value before you do :

R25=8 'readphase command

!call _Send_htrc110_cmdR25

Variables for EM4095 :

_tagflag , a byte that stores the return flag that will be loaded with 1 when a

valid tag is detected

_tag_insync ,a byte that is used to store the state of the bit stream. 

_tag_bitcount , a byte that stores the total bits when not in sync yet 

_tag_tbit , a byte that stores the total received bits

_tag_par , a byte that stores the parity

_tag_timeout ,a byte that is loaded with the time that will be tried to 

detect an RFID chip

_taglasttime , a byte that stores the last time a valid edge was detected

_tagid , a word that points to the serial number array

See also

[READHITAG](readhitag.md)

Example HTRC110

```vb
'--------------------------------------------------------------------------

' (c) 1995-2025 , MCS Electronics

' sample : readhitag.bas

' demonstrates usage of the READHITAG() function

'--------------------------------------------------------------------------

$regfile = "m88def.dat" ' specify chip

$crystal = 8000000 ' used speed

$baud = 19200 ' baud rate

'Notice that the CLOCK OUTPUT of the micro is connected to the clock input of

```
the HTRC110

'PORTB.0 of the Mega88 can optional output the clock. You need to set the

fusebit for this option

```vb
'This way all parts use the Mega88 internal oscillator

'The code is based on Philips(NXP) datasheets and code. We have signed an

```
NDA to get the 8051 code

```vb
'You can find more info on Philips website if you want their code

Print "HTC110 demo"

Config Hitag = 64 , Type = Htrc110 , Dout = Pind.2 , Din = Pind.3 , Clock = Pind.4 , Int = @int0

' ^ use timer0 and select prescale value 64

' ^ we used htrc110 chip

' ^-- dout of HTRC110 is connected to PIND.2

```
which will be set to input mode

' ^ DIN of HTRC100 is connected

to PIND.3 which will be set to output mode

' ^clock of

HTRC110 is connected to PIND.4 which is set to output mode

```vb
' ^ interrupt

'the config statement will generate a number of constants and

```
internal variables used by the code

```vb
'the htrc110.lbx library is called

Dim Tags(5) As Byte 'each tag has 5 byte serial

Dim J As Byte ' a loop counter

'you need to use a pin that can detect a pin level change

'most INT pins have this option

'OR , you can use the PCINT interrupt that is available on some chips

'In case you want PCINT option

' Pcmsk2 = &B0000_0100 'set the mask to ONLY use the pin connected to DOUT

' On Pcint2 Checkints 'label to be called

' Enable Pcint2 'enable this interrupt

'In case you want to use INT option

On Int0 Checkints ' PIND.2 is INT0

Config Int0 = Change 'you must configure the pin to work in pin change intertupt mode

Enable Interrupts ' enable global interrupts

Do

If Readhitag(tags(1)) = 1 Then 'check if there is a new tag ID

For J = 1 To 5 'print the 5 bytes

Print Hex(tags(j)) ; ",";

Next

Else 'there was nothing

Print "Nothing"

End If

Waitms 500 'some delay

Loop

'this routine is called by the interrupt routine

```
Checkints:

Call _checkhitag 'you must call this label

```vb
'you can do other things here but keep time to a minimum

Return

```
Example EM4095

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This sample will read a HITAG chip based on the EM4095 chip

' Consult EM4102 and EM4095 datasheets for more info

'-------------------------------------------------------------------------------

' The EM4095 was implemented after an idea of Gerhard Günzel

' Gerhard provided the hardware and did research at the coil and capacitors.

' The EM4095 is much simpler to use than the HTRC110. It need less pins.

' A reference design with all parts is available from MCS

'-------------------------------------------------------------------------------

$regfile = "M88def.dat"

$baud = 19200

$crystal = 8000000

$hwstack = 40

$swstack = 40

$framesize = 40

'Make SHD and MOD low

Dim Tags(5) As Byte 'make sure the array is at least 5 bytes

Dim J As Byte

Config Hitag = 64 , Type = Em4095 , Demod = Pind.3 , Int = @int1

Print "Test EM4095"

'you could use the PCINT option too, but you must mask all pins out 

```
so it will only respond to our pin

```vb
' Pcmsk2 = &B0000_0100

' On Pcint2 Checkints

' Enable Pcint2

On Int1 Checkints Nosave 'we use the INT1 pin all regs are saved in the lib

Config Int1 = Change 'we have to config so that on each pin change the routine will be called

Enable Interrupts 'as last we have to enable all interrupts

Do

Print "Check..."

If Readhitag(tags(1)) = 1 Then 'this will enable INT1

For J = 1 To 5

Print Hex(tags(j)) ; ",";

Next

Print

Else

Print "Nothing"

End If

Waitms 500

Loop

```
Checkints:

Call _checkhitag 'in case you have used a PCINT, you could have other code here as well

Return

---

## CONFIG I2CBUS

Action

This configuration statement defines the SCL and SDA pins of an I2C multibus.

Syntax

CONFIG I2CBUS= bus , SCL=scl , SDA=sda

Remarks

bus | A numeric value in the range from 0 to 15.  
---|---  
scl | The SCL pin used for the specified bus.  
sda | The SDA pin used for the specified bus.  
  
While XMEGA supports multiple TWI busses, the normal AVR only supports on TWI or no I2C bus. The CONFIG I2CBUS is a software solution to use multiple I2C busses.

An internal variable is created named I2CBUS. This is a BYTE variable. 

You need to assign this variable a value before you use the usual I2C statements. When you want to use a different bus, you just assign the variable a new bus index value.

Have a look at the sample. It creates 4 busses. Since I2CINIT is required, a loop is used to call the I2CINIT statement for all busses.

And another loop is used to send data to all 4 busses.

![notice](notice.jpg)Both SCL and SDA pins must be on the same PORT. Also, the PIN, DDR and PORT register addresses of the processor must be in ascending order and need to exist.

For example the M1284P portA group :

PORTA = $02

DDRA = $01

PINA = $00

This is ok to use. But some processors have no DDR register because a port can only be used in output or input mode. Such a port can not be used.

An example of a bad port is PORTF in the M128. As you can see there is a gap in the address between PINF and DDRF and this will make it fail.

PORTF = $62

DDRF = $61

PINF = $00 

ASM

The I2C routines are located in the i2c_multibus.lib.

See also

[CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md), [Using the I2C protocol](using_the_i2c_protocol.md) , [I2CINIT](i2cinit.md)

Example

```vb
'------------------------------------------------------------------------------  
'name : I2C-multibus.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates I2C multibus library  
'micro : Mega88  
'suited for demo : no, lib not included in demo  
'commercial addon needed : no  
'------------------------------------------------------------------------------  
$regfile="m88def.dat"  
$crystal=8000000  
$hwstack=32  
$swstack=24  
$framesize=24  
  
config i2cbus=0,scl=portc.0,sda= portc.1 'each bus requires a configuration of the SCL and SDA pins  
config i2cbus=1,scl=portc.2,sda= portc.3 'this sample creates 4 busses  
config i2cbus=2,scl=portd.2,sda= portd.3  
config i2cbus=3,scl=portd.4,sda= portd.5  
  
Dim j as Byte  
  
For j=0 to 3 'the first bus is 0 !!!  
```
i2cbus=j 'select the BUS  
i2cinit 'init the pins and state  
```vb
Next  
  
do  
for j=0 to 3  
```
i2cbus=j 'select the bus  
I2CSend &H40, &B01010101 'send some data  
```vb
next  
waitms 100  
loop  
  
end

```

---

## CONFIG I2CDELAY

Action

Compiler directive that overrides the internal I2C delay routine.

(Only for Software I2C Routines)

Syntax

CONFIG I2CDELAY = value

Remarks

value | A numeric value in the range from 1 to 255.  A higher value means a slower I2C clock. You may use a value of 0 too but it will result in a value of 256.  
---|---  
  
For the I2C routines the clock rate is calculated depending on the used crystal. In order to make it work for all I2C devices the slow mode is used. When you have faster I2C devices you can specify a low value.

By default a value of 5 is used. This will give a 200 kHZ clock.

When you specify 10, 10 uS will be used resulting in a 100 KHz clock.

When you use a very low crystal frequency, it is not possible to work with high clock frequencies.

ASM

The I2C routines are located in the i2c.lib/i2c.lbx files.

For chips that have hardware TWI, you can use the MasterTWI lib.

See also

[CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md), [Using the I2C protocol](using_the_i2c_protocol.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : i2c.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demo: I2CSEND and I2CRECEIVE  
'micro : Mega48  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m48def.dat" ' specify the used micro  
$crystal = 4000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
'We use here the Software I2C Routines  
Config Scl = Portb.4  
Config Sda = Portb.5  
```
I2cinit  
  
```vb
Config I2cdelay = 10 '100KHz  
  
Declare Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
Declare Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
  
```
Const Addressw = 174 'slave write address  
Const Addressr = 175 'slave read address  
  
Dim B1 As Byte , Adres As Byte , Value As Byte 'dim byte  
  
Call Write_eeprom(1 , 3) 'write value of three to address 1 of EEPROM  
Call Read_eeprom(1 , Value) : Print Value 'read it back  
Call Read_eeprom(5 , Value) : Print Value 'again for address 5  
  
  
'-------- now write to a PCF8474 I/O expander -------  
I2csend &H40 , 255 'all outputs high  
I2creceive &H40 , B1 'retrieve input  
```vb
Print "Received data " ; B1 'print it  
End  
  
```
Rem Note That The Slaveaddress Is Adjusted Automaticly With I2csend & I2creceive  
Rem This Means You Can Specify The Baseaddress Of The Chip.  
  
```vb
'sample of writing a byte to EEPROM AT2404  
Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
```
I2cstart 'start condition  
I2cwbyte Addressw 'slave address  
I2cwbyte Adres 'asdress of EEPROM  
I2cwbyte Value 'value to write  
I2cstop 'stop condition  
```vb
Waitms 10 'wait for 10 milliseconds  
End Sub  
  
'sample of reading a byte from EEPROM AT2404  
Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
```
I2cstart 'generate start  
I2cwbyte Addressw 'slave adsress  
I2cwbyte Adres 'address of EEPROM  
I2cstart 'repeated start  
I2cwbyte Addressr 'slave address (read)  
I2crbyte Value , Nack 'read byte  
I2cstop 'generate stop  
```vb
End Sub  
  
' when you want to control a chip with a larger memory like the 24c64 it requires an additional byte  
' to be sent (consult the datasheet):  
' Wires from the I2C address that are not connected will default to 0 in most cases!  
  
' I2cstart 'start condition  
' I2cwbyte &B1010_0000 'slave address  
' I2cwbyte H 'high address  
' I2cwbyte L 'low address  
' I2cwbyte Value 'value to write  
' I2cstop 'stop condition  
' Waitms 10

```

---

## CONFIG I2CSLAVE

The I2C-Slave library is intended to create I2C slave chips. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>)

The I2C Slave add on can turn some chips into a I2C slave device. You can start your own chip plant this way.

Most new AVR chips have a so called TWI/I2C interface. As a customer of the I2C slave lib, you can get both libs.

The i2cslave.lib works in interrupt mode and is the best way as it adds less overhead and also less system resources.

With this add-on library you get both libraries:

| i2cslave.lib and i2cslave.lbx : This library is used for AVRâs which have no hardware TWI/I2C interface like for example ATTINY2313 or ATTINY13. In this case TIMER0 and INT0 is used for SDA and SCL (Timer0 Pin = SCL, INT0 Pin = SDA). Only AVR' with TIMER0 and INT0 on the same port can use this library like for example ATTINY2313 or ATTINY13. The i2cslave.lib file contains the ASM source. The i2cslave.lbx file contains the compiled ASM source. See CONFIG I2CSLAVE below.  
---|---  
  
| i2c_TWI-slave.LBX : This library can be used when an AVR have an TWI/I2C hardware interface like for example ATMEGA8, ATMEGA644P or ATMEGA128. In this case the hardware SDA and SCL pin's of the AVR will be used (with ATMEGA8: SCL is PORTC.5 and SDA is PORTC.4). This library will be used when USERACK = OFF. When USERACK =ON then i2c_TWI-slave-acknack.LBX will be used. See also [Config TWISLAVE](config_twislave.md)  
---|---  
  
Action

Configures the I2C slave mode for ATTINY and ATMEGA devices.

Before you begin

Copy the library files into the BASCOM-AVR\LIB directory.

Syntax

CONFIG I2CSLAVE = address , INT = interrupt , TIMER = tmr

(This function is part of the I2C-Slave library. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

Remarks

Address | The slave address you want to assign to the I2C slave chip. This is an address that must be even like &H60. So &H61 cannot be used. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases.   
---|---  
Interrupt | The interrupt that must be used. This is INT0 by default.  
Tmr | The timer that must be used. This is TIMER0 by default.  
  
The library was written for TIMER0 and INT0.

While the interrupt can be specified, you need to change the library code when you use a non-default interrupt. For example when you like to use INT1 instead of the default INT0. 

The same applies to the TIMER. You need to change the library when you like to use another timer.

You can not use these interrupts yourself. It also means that the SCL and SDA pins are fixed.

CONFIG I2CSLAVE will enable the global interrupts.

Timer0 and INT0 Pin's of Various AVR's

The I2C slave routines use the TIMER0 and INT0. 

The following table lists the pins for the various chips

Chip | SCL | SDA  
---|---|---  
AT90S1200 | PORTD.4 | PORTD.2  
AT90S2313 | PORTD.4 | PORTD.2  
AT90S2323 | PORTB.2 | PORTB.1  
AT90S2333 | PORTD.4 | PORTD.2  
AT90S2343 | PORTB.2 | PORTB.1  
AT90S4433 | PORTD.4 | PORTD.2  
ATTINY22 | PORTB.2 | PORTB.1  
ATTINY13 | PORTB.2 | PORTB.1  
ATTINY2313 | PORTD.4 | PORTD.2  
ATMEGA1280 | PORTD.7 | PORTD.0  
ATMEGA128CAN | PORTD.7 | PORTD.0  
ATMEGA168 | PORTD.4 | PORTD.2  
ATMEGA2560 | PORTD.7 | PORTD.0  
ATMEGA2561 | PORTD.7 | PORTD.0  
ATMEGA48 | PORTD.4 | PORTD.2  
ATMEGA88 | PORTD.4 | PORTD.2  
ATMEGA8 | PORTD.4 | PORTD.2  

After you have configured the slave address, you can insert your code.

A do-loop would be best:

```vb
Do  
' your code here  
Loop

```
After your main program you need to insert two labels with a return:

When the master needs to read a byte, the following label is always called.

You must put the data you want to send to the master in variable _a1 which is register R16

I2c_master_needs_data:  
```vb
'when your code is short, you need to put in a waitms statement  
'Take in mind that during this routine, a wait state is active and the master will wait  
'After the return, the waitstate is ended  
Config Portb = Input ' make it an input  
  
```
_a1 = Pinb ' Get input from portB and assign it  
Return

When the master writes a byte, the following label is always called.

It is your task to retrieve variable _A1 and do something with it

_A1 is register R16 that could be destroyed/altered by BASIC statements

For that reason it is important that you first save this variable.

I2c_master_has_data:  
```vb
'when your code is short, you need to put in a waitms statement  
'Take in mind that during this routine, a wait state is active and the master will wait  
'After the return, the waitstate is ended  
  
```
Bfake = _a1 ' this is not needed but it shows how you can store _A1 in a byte  
```vb
'after you have stored the received data into bFake, you can alter R16  
Config Portb = Output ' make it an output since it could be an input  
```
Portb = _a1 'assign _A1 (R16)  
Return

See Also

[CONFIG TWI](config_twi.md) , [CONFIG TWISLAVE](config_twislave.md), [I2C TWI Slave](i2ctwislave.md)

Debugging Hint's

If you encounter a problem first check:

•| Do you use the correct Pin's for SDA and SCL ?  
---|---  
  
•| Pull-up Resistor from SDA and SCL to Vcc ?  
---|---  
  
•| Try to reduce clockrate from I2C Master  
---|---  
  
•| Try to use waitms XX between the I2CWBYTE in the I2C Master AVR  
---|---  
  
•| Try to reduce code in the interrupt routine  
---|---  
  
Example

```vb
'-----------------------------------------------------------------------------------------

'name : i2c_pcf8574.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how you could use the I2C slave library to create a PCF8574

'micro : AT90S2313

'suited for demo : NO, ADDON NEEDED

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 3684000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'This program shows how you could use the I2C slave library to create a PCF8574

'The PCF8574 is an IO extender chip that has 8 pins.

'The pins can be set to a logic level by writing the address followed by a value

'In order to read from the pins you need to make them '1' first

'This program uses a AT90S2313, PORTB is used as the PCF8574 PORT

'The slave library needs INT0 and TIMER0 in order to work.

'SCL is PORTD.4 (T0)

'SDA is PORTD.2 (INT0)

'Use 10K pull up resistors for both SCL and SDA

'The Slave library will only work for chips that have T0 and INT0 connected to the same PORT.

'These chips are : 2313,2323, 2333,2343,4433,tiny22, tiny12,tiny15, M8

'The other chips have build in hardware I2C(slave) support.

'specify the slave address. This is &H40 for the PCF8574

'You always need to specify the address used for write. In this case &H40 ,

'The config i2cslave command will enable the global interrupt enable flag !

Config I2cslave = &B01000000 ' same as &H40

'Config I2cslave = &H40 , Int = Int0 , Timer = Timer0

'A byte named _i2c_slave_address_received is generated by the compiler.

'This byte will hold the received address.

'A byte named _i2c_slave_address is generated by the compiler.

'This byte must be assigned with the slave address of your choice

'the following constants will be created that are used by the slave library:

' _i2c_pinmask = &H14

' _i2c_slave_port = Portd

' _i2c_slave_pin = Pind

' _i2c_slave_ddr = Ddrd

' _i2c_slave_scl = 4

' _i2c_slave_sda = 2

'These values are adjusted automatic depending on the selected chip.

'You do not need to worry about it, only provided as additional info

'by default the PCF8574 port is set to input

Config Portb = Input

```
Portb = 255 'all pins high by default

```vb
'DIM a byte that is not needed but shows how you can store/write the I2C DATA

Dim Bfake As Byte

'empty loop

Do

' you could put your other program code here

'In any case, do not use END since it will disable interrupts

Loop

'here you can write your other program code

'But do not forget, do not use END. Use STOP when needed

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

' The following labels are called from the slave library

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'When the master wants to read a byte, the following label is allways called

'You must put the data you want to send to the master in variable _a1 which is register R16

```
I2c_master_needs_data:

```vb
'when your code is short, you need to put in a waitms statement

'Take in mind that during this routine, a wait state is active and the master will wait

'After the return, the waitstate is ended

Config Portb = Input ' make it an input

```
_a1 = Pinb ' Get input from portB and assign it

```vb
Return

'When the master writes a byte, the following label is always called

'It is your task to retrieve variable _A1 and do something with it

'_A1 is register R16 that could be destroyed/altered by BASIC statements

'For that reason it is important that you first save this variable

```
I2c_master_has_data:

```vb
'when your code is short, you need to put in a waitms statement

'Take in mind that during this routine, a wait state is active and the master will wait

'After the return, the waitstate is ended

```
Bfake = _a1 ' this is not needed but it shows how you can store _A1 in a byte

```vb
'after you have stored the received data into bFake, you can alter R16

Config Portb = Output ' make it an output since it could be an input

```
Portb = _a1 'assign _A1 (R16)

```vb
Return

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'You could simply extend this sample so it will use 3 pins of PORT D for the address selection

'For example portD.1 , portd.2 and portD.3 could be used for the address selection

'Then after the CONFIG I2CSLAVE = &H40 statement, you can put code like:

'Dim switches as Byte ' dim byte

'switches = PIND ' get dip switch value

'switches = switches and &H1110 ' we only need the lower nibble without the LS bit

'_i2c_slave_address = &H40 + switches ' set the proper address

```

---

## CONFIG INPUT

Action

Instruct the compiler to modify serial input line terminator behaviour

Syntax

CONFIG INPUT1 = term , ECHO=echo

Syntax Xmega

CONFIG INPUT1|INPUT2|INPUT3|INPUT4|INPUT5|INPUT6|INPUT7|INPUT8 = term , ECHO=echo

Remarks

INPUT | Use INPUT or INPUT1 for COM1, INPUT2 for COM2, INPUT3 for COM3, etc.  
---|---  
Term | A parameter with one of the following values : CR - Carriage Return (default) LF - Line Feed CRLF - Carriage Return followed by a Line Feed LFCR - Line Feed followed by a Carriage Return  
Echo | A parameter with one of the following values : CR - Carriage Return LF - Line Feed CRLF - Carriage Return followed by a Line Feed (default) LFCR - Line Feed followed by a Carriage Return  
  
The 'term' parameter specifies which character(s) are expected to terminate the [INPUT](input.md) statement with serial communication. It has no impact on the DOS file system INPUT.

In most cases, when you press <ENTER> , a carriage return(ASCII 13) will be sent. In some cases, a line feed (LF) will also be sent after the CR. It depends on the terminal emulator or serial communication OCX control you use.

The 'echo' parameter specifies which character(s) are send back to the terminal emulator after the INPUT terminator is received. By default CR and LF is sent. But you can specify which characters are sent. This can be different characters then the 'term' characters. So when you send in your VB application a string, and end it with a CR, you can send back a LF only when you want.

![notice](notice.jpg)When NOECHO is used, NO characters are sent back even while configured with CONFIG INPUT

```vb
For the XMega you can specify for each UART how it should handle input and echo.

For the first UART you may use INPUT0, INPUT1 or just INPUT. For the second UART you must use INPUT2, for UART3 -> INPUT3, etc.

```
See also

[INPUT](input.md)

ASM

NONE

Example

```vb
Config Input1 = CR , Echo = CRLF

Dim S as String * 20

Input "Hello ",s

```

---

## CONFIG INPUTBIN

Action

Configure INPUTBIN behavior

Syntax

CONFIG INPUTBIN = extended

Remarks

extended | This mode is the only mode. It allows to receive packets greater than 255 bytes. The maximum packet size is 64 KB. Because support for big packets requires more code, it is made optional.  You can not change between normal and extended mode dynamically. If you chose to use extended mode, this will be used for all your PRINTBIN code.  
---|---  
  
See also

[CONFIG PRINT](configprint.md) , [PRINTBIN](printbin.md) , [INPUTBIN](inputbin.md) , [CONFIG PRINTBIN](config_printbin.md)

Example

```vb
$regfile = "m103def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Inputbin = Extended

Dim A(1000)

```
Inputbin A(1) ; 1000

---

## CONFIG INTVECTORSELECTION

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

---

## CONFIG INTx

Action

Configures the way the interrupts 0,1 and 4-7 will be triggered.

Syntax

CONFIG INTx = state

Where X can be 0,1 and 4 to 7 in the MEGA chips.

Remarks

state | LOW LEVEL to generate an interrupt while the pin is held low. Holding the pin low will generate an interrupt over and over again. FALLING to generate an interrupt on the falling edge. RISING to generate an interrupt on the rising edge. CHANGE to generate an interrupt on the change of the edge. Not all microprocessors support CHANGE.  
---|---  
  
The MEGA103 has also INT0-INT3. These are always low level triggered so there is no need /possibility for configuration.

The number of interrupt pins depend on the used chip. Most chips only have int0 and int1.

XMEGA

For the XMEGA you need to use [CONFIG XPIN](config_xpin.md).

Example

```vb
'-----------------------------------------------------------------------------------------

'name : spi-softslave.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to implement a SPI SLAVE with software

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'Some atmel chips like the 2313 do not have a SPI port.

'The BASCOM SPI routines are all master mode routines

'This example show how to create a slave using the 2313

'ISP slave code

'define the constants used by the SPI slave

```
Const _softslavespi_port = Portd ' we used portD

Const _softslavespi_pin = Pind 'we use the PIND register for reading

Const _softslavespi_ddr = Ddrd ' data direction of port D

Const _softslavespi_clock = 5 'pD.5 is used for the CLOCK

Const _softslavespi_miso = 3 'pD.3 is MISO

Const _softslavespi_mosi = 4 'pd.4 is MOSI

Const _softslavespi_ss = 2 ' pd.2 is SS

```vb
'while you may choose all pins you must use the INT0 pin for the SS

'for the 2313 this is pin 2

'PD.3(7), MISO must be output

'PD.4(8), MOSI

'Pd.5(9) , Clock

'PD.2(6), SS /INT0

'define the spi slave lib

$lib "spislave.lbx"

'sepcify wich routine to use

$external _spisoftslave

'we use the int0 interrupt to detect that our slave is addressed

On Int0 Isr_sspi Nosave

'we enable the int0 interrupt

Enable Int0

'we configure the INT0 interrupt to trigger when a falling edge is detected

Config Int0 = Falling

'finally we enabled interrupts

Enable Interrupts

'

Dim _ssspdr As Byte ' this is out SPI SLAVE SPDR register

Dim _ssspif As Bit ' SPI interrupt revceive bit

Dim Bsend As Byte , I As Byte , B As Byte ' some other demo variables

```
_ssspdr = 0 ' we send a 0 the first time the master sends data

```vb
Do

If _ssspif = 1 Then

Print "received: " ; _ssspdr

Reset _ssspif

```
_ssspdr = _ssspdr + 1 ' we send this the next time

```vb
End If

Loop

```

---

## CONFIG KBD

Action

Configure the GETKBD() function and tell which port to use.

Syntax

CONFIG KBD = PORTx , DEBOUNCE = value [, DELAY = value] [,COLS=cols]

Remarks

PORTx | The name of the PORT to use such as PORTB or PORTD.  
---|---  
DEBOUNCE | By default the debounce value is 20. A higher value might be needed. The maximum is 255.  
Delay | An optional parameter that will cause Getkbd() to wait the specified amount of time after the key is detected. This parameter might be added when you call GetKbd() repeatedly in a loop. Because of noise and static electricity, wrong values can be returned. A delay of say 100 mS, can eliminate this problem.  
COLS | This value is 4 by default. Some chips do not have port pin 7 and for these cases you can use COLS=3, or COLS=2.  This does assume that columns are connected to the high port nibble.  
  
The GETKBD() function can be used to read the pressed key from a matrix keypad attached to a port of the uP.

You can define the port with the CONFIG KBD statement.

In addition to the default behavior you can configure the keyboard to have 6 rows instead of 4 rows.

CONFIG KBD = PORTx , DEBOUNCE = value , rows=6, row5=pinD.6, row6=pind.7

This would specify that row5 is connected to pind.6 and row7 to pind.7

Note that you can only use rows=6. Other values will not work.

See also

[GETKBD](getkbd.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : getkbd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : GETKBD

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'specify which port must be used

'all 8 pins of the port are used

Config Kbd = Portb

'dimension a variable that receives the value of the pressed key

Dim B As Byte

'loop for ever

Do

```
B = Getkbd()

```vb
'look in the help file on how to connect the matrix keyboard

'when you simulate the getkbd() it is important that you press/click the keyboard button

' before running the getkbd() line !!!

Print B

'when no key is pressed 16 will be returned

'use the Lookup() function to translate the value to another one

' this because the returned value does not match the number on the keyboad

Loop

End

```

---

## CONFIG KEYBOARD

Action

Configure the GETATKBD() function and tell which port pins to use.

Syntax

CONFIG KEYBOARD = PINX.y , DATA = PINX.y , KEYDATA = table

Remarks

KEYBOARD | The PIN that serves as the CLOCK input.  
---|---  
DATA | The PIN that serves as the DATA input.  
KEYDATA | The label where the key translation can be found. The AT keyboard returns scan codes instead of normal ASCII codes. So a translation table s needed to convert the keys. BASCOM allows the use of shifted keys too. Special keys like function keys are not supported.  
  
The AT keyboard can be connected with only 4 wires: clock,data, gnd and vcc.

Some info is displayed below. This is copied from an Atmel data sheet.

The INT0 or INT1 shown can be in fact any pin that can serve as an INPUT pin.

The application note from Atmel works in interrupt mode. For BASCOM we rewrote the code so that no interrupt is needed/used.

![BASC0085](basc0085.gif)

See also

[GETATKBD](getatkbd.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : getatkbd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PC AT-KEYBOARD Sample

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8535def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'For this example :

'connect PC AT keyboard clock to PIND.2 on the 8535

'connect PC AT keyboard data to PIND.4 on the 8535

'The GetATKBD() function does not use an interrupt.

'But it waits until a key was pressed!

'configure the pins to use for the clock and data

'can be any pin that can serve as an input

'Keydata is the label of the key translation table

Config Keyboard = Pind.2 , Data = Pind.4 , Keydata = Keydata

'Dim some used variables

Dim S As String * 12

Dim B As Byte

'In this example we use SERIAL(COM) INPUT redirection

$serialinput = Kbdinput

'Show the program is running

Print "hello"

Do

'The following code is remarked but show how to use the GetATKBD() function

' B = Getatkbd() 'get a byte and store it into byte variable

'When no real key is pressed the result is 0

'So test if the result was > 0

' If B > 0 Then

' Print B ; Chr(b)

' End If

'The purpose of this sample was how to use a PC AT keyboard

'The input that normally comes from the serial port is redirected to the

'external keyboard so you use it to type

Input "Name " , S

'and show the result

Print S

'now wait for the F1 key , we defined the number 200 for F1 in the table

Do

```
B = Getatkbd()

```vb
Loop Until B <> 0

Print B

Loop

End

'Since we do a redirection we call the routine from the redirection routine

'

```
Kbdinput:

```vb
'we come here when input is required from the COM port

'So we pass the key into R24 with the GetATkbd function

' We need some ASM code to save the registers used by the function

$asm

```
push r16 ; save used register

push r25

push r26

push r27

Kbdinput1:

rCall _getatkbd ; call the function

tst r24 ; check for zero

breq Kbdinput1 ; yes so try again

pop r27 ; we got a valid key so restore registers

pop r26

pop r25

pop r16

```vb
$end Asm

'just return

Return

'The tricky part is that you MUST include a normal call to the routine

'otherwise you get an error

'This is no clean solution and will be changed

```
B = Getatkbd()

'This is the key translation table

Keydata:

'normal keys lower case

Data 0 , 0 , 0 , 0 , 0 , 200 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , &H5E , 0

Data 0 , 0 , 0 , 0 , 0 , 113 , 49 , 0 , 0 , 0 , 122 , 115 , 97 , 119 , 50 , 0

Data 0 , 99 , 120 , 100 , 101 , 52 , 51 , 0 , 0 , 32 , 118 , 102 , 116 , 114 , 53 , 0

Data 0 , 110 , 98 , 104 , 103 , 121 , 54 , 7 , 8 , 44 , 109 , 106 , 117 , 55 , 56 , 0

Data 0 , 44 , 107 , 105 , 111 , 48 , 57 , 0 , 0 , 46 , 45 , 108 , 48 , 112 , 43 , 0

Data 0 , 0 , 0 , 0 , 0 , 92 , 0 , 0 , 0 , 0 , 13 , 0 , 0 , 92 , 0 , 0

Data 0 , 60 , 0 , 0 , 0 , 0 , 8 , 0 , 0 , 49 , 0 , 52 , 55 , 0 , 0 , 0

Data 48 , 44 , 50 , 53 , 54 , 56 , 0 , 0 , 0 , 43 , 51 , 45 , 42 , 57 , 0 , 0

'shifted keys UPPER case

Data 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0

Data 0 , 0 , 0 , 0 , 0 , 81 , 33 , 0 , 0 , 0 , 90 , 83 , 65 , 87 , 34 , 0

Data 0 , 67 , 88 , 68 , 69 , 0 , 35 , 0 , 0 , 32 , 86 , 70 , 84 , 82 , 37 , 0

Data 0 , 78 , 66 , 72 , 71 , 89 , 38 , 0 , 0 , 76 , 77 , 74 , 85 , 47 , 40 , 0

Data 0 , 59 , 75 , 73 , 79 , 61 , 41 , 0 , 0 , 58 , 95 , 76 , 48 , 80 , 63 , 0

Data 0 , 0 , 0 , 0 , 0 , 96 , 0 , 0 , 0 , 0 , 13 , 94 , 0 , 42 , 0 , 0

Data 0 , 62 , 0 , 0 , 0 , 8 , 0 , 0 , 49 , 0 , 52 , 55 , 0 , 0 , 0 , 0

Data 48 , 44 , 50 , 53 , 54 , 56 , 0 , 0 , 0 , 43 , 51 , 45 , 42 , 57 , 0 , 0

---

## CONFIG LCD

Action

Configure the LCD display and override the compiler setting.

Syntax

CONFIG LCD = LCDtype , CHIPSET=KS077 | Dogm163v5 | DOG163V3 | DOG162V5 | DOG162V3 | ST7032 [,CONTRAST=value] [,BEFORE=0|1] [,AFTER=0|1]

BEFORE and AFTER. with a parameter value of 1 a sub will be called _lcdBefore and _lcdAfter

Remarks

LCDtype | The type of LCD display used. This can be : 40x4,16x1, 16x2, 16x4, 16x4, 20x2, 20x4, 16x1a or 20x4A. Default 16x2 is assumed.  
---|---  
Chipset KS077 | Most text based LCD displays use the same chip from Hitachi. But some use the KS077 which is highly compatible but needs an additional function register to be set. This parameter will cause that this register is set when you initialize the display.  
CHIPSET DOGM | The DOGM chip set uses a special function register that need to be set. The 16 x 2 LCD displays need DOG162V3 for 3V operation or DOG162V5 for 5V operation. The 16 x 3 LCD displays need DOG163V3 for 3V operation or Dogm163v5 for 5V operation  
CHIPSET ST7032 | This chip is used on I2C lcd's. It requires library Lcd_RX1602A5. See example 3 below.  
CONTRAST | The optional contrast parameter is only supported by the EADOG displays. By default a value from the manufacture is used. But you might want to override this value with a custom setting. The default values are : \- DOGM162V5 : &H74 \- DOGM162V3 : &H78 \- DOGM163V5 : &H7C \- DOGM163V3 : &H70  
BEFORE | This is an optional parameter. A value of 1 will result in a call to a routine named _LCDBEFORE, each time LCD value|"text" is used.  This allows you as a user to turn off interrupts or perform other tasks.  
AFTER | This is an optional parameter. A value of 1 will result in a call to a routine named _LCDAFTER, each time LCD value|"text" is ended.  This allows you as a user to turn on interrupts or perform other tasks.  
  
When you have a 16x2 display, you don't have to use this statement.

The 16x1a is special. It is used for 2x8 displays that have the address of line 2, starting at location &H8.

The 20xA is also special. It uses the addresses &H00, &H20, &H40 and &H60 for the 4 lines. It will also set a special function register.

The CONFIG LCD can only be used once. You can not dynamic(at run time) change the pins.

When you want to initialize the LCD during run time, you can use the [INITLCD](initlcd.md) statement.

The BEFORE and AFTER parameters can be used to call some user code just before data is shown on the LCD, and when finished.

For example, you could toggle a LED on/off. Or set some background light. Or disable interrupts before showing data, and enable interrupts afterwards.

You must use DECLARE SUB to declare the called labels. Or you may use normal labels and exit with RETURN.

In version 2084 a constant is created named _TEXTLCDKIND which contains a value based on the selected LCD.

The values are :

LCD | Value  
---|---  
16x1 | 161  
16x2 | 162  
16x3 | 163  
16x4 | 164  
20x2 | 202  
24x2 | 242  
40x4 | 404  
20x4A | 1204  
40x2 | 402  
20x4 | 204  
16x1A | 1610  
20x4VFD | 2204  
  
See Also

[CONFIG LCDPIN](config_lcdpin.md) , [CONFIG LCDBUS](config_lcdbus.md) , [INITLCD](initlcd.md)

Example1

```vb
'-----------------------------------------------------------------------------------------

'name : lcd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'micro : Mega8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m8515.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$sim

'REMOVE the above command for the real program !!

'$sim is used for faster simulation

'note : tested in PIN mode with 4-bit

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

Config Lcdpin = Pin , Db4 = Porta.4 , Db5 = Porta.5 , Db6 = Porta.6 , Db7 = Porta.7 , E = Portc.7 , Rs = Portc.6

'These settings are for the STK200 in PIN mode

'Connect only DB4 to DB7 of the LCD to the LCD connector of the STK D4-D7

'Connect the E-line of the LCD to A15 (PORTC.7) and NOT to the E line of the LCD connector

'Connect the RS, V0, GND and =5V of the LCD to the STK LCD connector

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
Dim A As Byte

Config Lcd = 16x2 'configure lcd screen

'other options are 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

'When you dont include this option 16 * 2 is assumed

'16 * 1a is intended for 16 character displays with split addresses over 2 lines

'$LCD = address will turn LCD into 8-bit databus mode

' use this with uP with external RAM and/or ROM

' because it aint need the port pins !

```
Cls 'clear the LCD display

Lcd "Hello world." 'display this at the top line

Wait 1

Lowerline 'select the lower line

Wait 1

Lcd "Shift this." 'display this at the lower line

```vb
Wait 1

For A = 1 To 10

```
Shiftlcd Right 'shift the text to the right

```vb
Wait 1 'wait a moment

Next

For A = 1 To 10

```
Shiftlcd Left 'shift the text to the left

```vb
Wait 1 'wait a moment

Next

```
Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Wait 1 'wait a moment

Shiftcursor Right 'shift the cursor

Lcd "@" 'display this

Wait 1 'wait a moment

Home Upper 'select line 1 and return home

Lcd "Replaced." 'replace the text

Wait 1 'wait a moment

Cursor Off Noblink 'hide cursor

Wait 1 'wait a moment

Cursor On Blink 'show cursor

Wait 1 'wait a moment

Display Off 'turn display off

Wait 1 'wait a moment

Display On 'turn display on

'-----------------NEW support for 4-line LCD------

Thirdline

Lcd "Line 3"

Fourthline

Lcd "Line 4"

Home Third 'goto home on line three

Home Fourth

Home F 'first letteer also works

Locate 4 , 1 : Lcd "Line 4"

```vb
Wait 1

'Now lets build a special character

'the first number is the characternumber (0-7)

'The other numbers are the rowvalues

'Use the LCD tool to insert this line

```
Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character

'----------------- Now use an internal routine ------------

_temp1 = 1 'value into ACC

!rCall _write_lcd 'put it on LCD

End

Example2

```vb
'--------------------------------------------------------------

' EADOG-M163.bas

' Demonstration for EADOG 163 display

' (c) 1995-2025, MCS Electronics

'--------------------------------------------------------------

'

$regfile = "M8515.dat"

$crystal = 4000000

'I used the following settings

'Config Lcdpin = Pin , Db4 = Portb.2 , Db5 = Portb.3 , Db6 = Portb.4 , Db7 = Portb.5 , E = Portb.1 , Rs = Portb.0

'CONNECT vin TO 5 VOLT

Config Lcd = 16x3 , Chipset = Dogm163v5 '16*3 type LCD display

'other options for chipset are DOG163V3 for 3Volt operation

'Config Lcd = 16 * 3 , Chipset = Dogm163v3 , Contrast = &H72 '16*3 type LCD display

'The CONTRAST can be specified when the default value is not what you need

'The EADOG-M162 is also supported :

'Chipset params for the DOGM162 : DOG162V5, DOG162V3

```
Cls 'Dit maakt het scherm leeg

Locate 1 , 1 : Lcd "Hello World"

Locate 2 , 1 : Lcd "line 2"

Locate 3 , 1 : Lcd "line 3"

End

Example3

```vb
'------------------------------------------------------------------------------  
'name : LCD-RX1602A5.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates I2C LCD library  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'The used library was sponsored by Lab microelectronic GmbH  
'------------------------------------------------------------------------------  
  
$regfile = "m88def.dat"  
$crystal = 8000000  
$hwstack = 32  
$swstack = 32  
$framesize = 64  
  
```
const vmode = 3 ' 3V mode  
  
```vb
$lib "Lcd_RX1602A5.lbx"  
$lib "i2c_twi.lbx" ' use hardware twi or remark for software I2C  
  
Config Twi = 100000 ' 100kHz  
config lcd = 16x2 , chipset = st7032  
  
config SCL=PORTC.5  
config SDA=PORTC.4  
  
  
```
I2cinit  
  
lcd_reset alias portc.2 ' pin used for LCD RESET  
lcd_light alias portd.7 ' pin used for back light  
  
```vb
Config lcd_reset = Output ' Display Reset  
Config lcd_light = Output ' Display Licht  
  
  
```
lcd_light = 1 ' activate background LED  
Lcd_reset = 0 ' RESET mode  
waitms 100  
Lcd_reset = 1 ' normal mode  
  
initlcd ' init LCD  
lcdcontrast 30 'a value between 30 and 40 works best at 3V  
  
Do  
Cls  
Locate 1 , 1 : Lcd "test"  
```vb
Waitms 100 '  
Loop  
  
  
End

```
Example 4

```vb
declare sub _lcdbefore()  
declare sub _lcdafter()  
config PORTB.0=OUTPUT  
config LCD=16x2, before=1,after=1  
```
CLS  
LCD "test"  
```vb
End  
  
sub _lcdbefore()  
set portb.0  
end sub  
  
sub _lcdafter()  
reset portb.0  
end sub  
  
  


```

---

## CONFIG LCDBUS

Action

Configures the LCD data bus and overrides the compiler setting.

Syntax

CONFIG LCDBUS = constant

Remarks

Constant | 4 for 4-bit operation, 8 for 8-bit mode (default)  
---|---  
  
Use this statement together with the $LCD = address statement.

When you use the LCD display in the bus mode the default is to connect all the data lines. With the 4-bit mode, you only have to connect data lines d7-d4.

See also

[CONFIG LCD](config_lcd.md)

Example

```vb
'--------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

'--------------------------------------------------------------

' file: LCD.BAS

' demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'--------------------------------------------------------------

'note : tested in bus mode with 4-bit on the STK200

'LCD - STK200

'-------------------

'D4 D4

'D5 D5

'D6 D6

'D7 D7

'WR WR

'E E

'RS RS

'+5V +5V

'GND GND

'V0 V0

' D0-D3 are not connected since 4 bit bus mode is used!

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
$regfile = "8515def.dat"

$lcd = &HC000

$lcdrs = &H8000

Config Lcdbus = 4

Dim A As Byte

Config Lcd = 16x2 'configure lcd screen

'other options are 16 * 2 , 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

'When you dont include this option 16 * 2 is assumed

'16 * 1a is intended for 16 character displays with split addresses over 2 lines

'$LCD = address will turn LCD into 8-bit databus mode

' use this with uP with external RAM and/or ROM

' because it aint need the port pins !

```
Cls 'clear the LCD display

Lcd "Hello world." 'display this at the top line

Wait 1

Lowerline 'select the lower line

Wait 1

Lcd "Shift this." 'display this at the lower line

```vb
Wait 1

For A = 1 To 10

```
Shiftlcd Right 'shift the text to the right

```vb
Wait 1 'wait a moment

Next

For A = 1 To 10

```
Shiftlcd Left 'shift the text to the left

```vb
Wait 1 'wait a moment

Next

```
Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Wait 1 'wait a moment

Shiftcursor Right 'shift the cursor

Lcd "@" 'display this

Wait 1 'wait a moment

Home Upper 'select line 1 and return home

Lcd "Replaced." 'replace the text

Wait 1 'wait a moment

Cursor Off Noblink 'hide cursor

Wait 1 'wait a moment

Cursor On Blink 'show cursor

Wait 1 'wait a moment

Display Off 'turn display off

Wait 1 'wait a moment

Display On 'turn display on

'-----------------NEW support for 4-line LCD------

Thirdline

Lcd "Line 3"

Fourthline

Lcd "Line 4"

Home Third 'goto home on line three

Home Fourth

Home F 'first letteer also works

Locate 4 , 1 : Lcd "Line 4"

```vb
Wait 1

'Now lets build a special character

'the first number is the characternumber (0-7)

'The other numbers are the rowvalues

'Use the LCD tool to insert this line

```
Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character

'----------------- Now use an internal routine ------------

_temp1 = 1 'value into ACC

!rCall _write_lcd 'put it on LCD

---

## CONFIG LCDMODE

Action

Configures the LCD operation mode and overrides the compiler setting.

Syntax

CONFIG LCDMODE = type

Remarks

Type | PORT Will drive the LCD in 4-bit port mode and is the default. In PORT mode you can choose different PIN's from different PORT's to connect to the upper 4 data lines of the LCD display. The RS and E can also be connected to a user selectable pin. This is very flexible since you can use pins that are not used by your design and makes the board layout simple. On the other hand, more software is necessary to drive the pins. BUS will drive the LCD in bus mode and in this mode is meant when you have external RAM and so have an address and data bus on your system. The RS and E line of the LCD display can be connected to an address decoder. Simply writing to an external memory location select the LCD and the data is sent to the LCD display. This means the data-lines of the LCD display are fixed to the data-bus lines. Use [$LCD](lcd_1.md) = address and [$LCDRS](lcdrs.md) = address, to specify the addresses that will enable the E and RS lines.  
---|---  
  
See also

[CONFIG LCD](config_lcd.md) , [$LCD](lcd_1.md) , [$LCDRS](lcdrs.md)

Example

```vb
Config LCDMODE = PORT 'the report will show the settings

Config LCDBUS = 4 '4 bit mode

```
LCD "hello"

---

## CONFIG LCDPIN

Action

Override the LCD-PIN select options.

Syntax

```vb
CONFIG LCDPIN = PIN , DB4= PN,DB5=PN, DB6=PN, DB7=PN, E=PN, RS=PN [WR=PIN] [BUSY=PIN] [MODE=mode]

CONFIG LCDPIN = PIN , PORT=PORTx, E=PN, RS=PN

```
Remarks

PN | The name of the PORT pin such as PORTB.2 for example.  
---|---  
PORTX | When you want to use the LCD in 8 bit data, pin mode, you must specify the PORT to use.  
PIN | A port pin that is connected to the busy pin. The busy pin is only supported by the 20x4VFD display.  
MODE | A mode for the 20x4VFD display. Options : 0 : 4 bit parallel upper nibble first 1 : 4 bit parallel lower nibble first  
  
You can override the PIN selection from the Compiler Settings with this statement, so a second configuration lets you not choose more pins for a second LCD display.

The config command is preferred over the option settings since the code makes clear which pins are used. The CONFIG statement overrides the Options setting.

The PIN and MODE are only for the 20x4VFD display. See also [LCDAUTODIM](lcdautodim.md)

The WR pin is optional. When you select the WR pin, an alternative library will be used. This library uses the WR pin and reads the BUSY signal from the LCD.

The library lcd4busy_anypin will be used, which is based on Luciano's LUC_lcd4busy library.

Notice that since 2040 version, the compiler will generate LCD port pin info which you can use for your own libs.

By default the WR pin is optional and the WR signal of the LCD should be connected to ground. This saves the pin for other purposes. When you have enough pins, you better use the WR-pin.

If you do not connect the WR pin to ground but to a pin, and you do not specify the WR pin, but you set the logic level to 0 in your code, you have to use an INITLCD command after you have set the WR pin to 0.

See also

[CONFIG LCD](config_lcd.md) , [CONFIG LCDMODE](config_lcdmode.md) , [CONFIG LCDBUS](config_lcdbus.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : lcd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: LCD, CLS, LOWERLINE, SHIFTLCD, SHIFTCURSOR, HOME

' CURSOR, DISPLAY

'micro : Mega8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m8515.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$sim

'REMOVE the above command for the real program !!

'$sim is used for faster simulation

'note : tested in PIN mode with 4-bit

'Config Lcdpin = Pin , Db4 = Portb.1 , Db5 = Portb.2 , Db6 = Portb.3 , Db7 = Portb.4 , E = Portb.5 , Rs = Portb.6

Config Lcdpin = Pin , Db4 = Porta.4 , Db5 = Porta.5 , Db6 = Porta.6 , Db7 = Porta.7 , E = Portc.7 , Rs = Portc.6

'These settings are for the STK200 in PIN mode

'Connect only DB4 to DB7 of the LCD to the LCD connector of the STK D4-D7

'Connect the E-line of the LCD to A15 (PORTC.7) and NOT to the E line of the LCD connector

'Connect the RS, V0, GND and =5V of the LCD to the STK LCD connector

```
Rem with the config lcdpin statement you can override the compiler settings

```vb
Dim A As Byte

Config Lcd = 16x2 'configure lcd screen

'other options are 16 * 4 and 20 * 4, 20 * 2 , 16 * 1a

'When you dont include this option 16 * 2 is assumed

'16 * 1a is intended for 16 character displays with split addresses over 2 lines

'$LCD = address will turn LCD into 8-bit databus mode

' use this with uP with external RAM and/or ROM

' because it aint need the port pins !

```
Cls 'clear the LCD display

Lcd "Hello world." 'display this at the top line

Wait 1

Lowerline 'select the lower line

Wait 1

Lcd "Shift this." 'display this at the lower line

```vb
Wait 1

For A = 1 To 10

```
Shiftlcd Right 'shift the text to the right

```vb
Wait 1 'wait a moment

Next

For A = 1 To 10

```
Shiftlcd Left 'shift the text to the left

```vb
Wait 1 'wait a moment

Next

```
Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Wait 1 'wait a moment

Shiftcursor Right 'shift the cursor

Lcd "@" 'display this

Wait 1 'wait a moment

Home Upper 'select line 1 and return home

Lcd "Replaced." 'replace the text

Wait 1 'wait a moment

Cursor Off Noblink 'hide cursor

Wait 1 'wait a moment

Cursor On Blink 'show cursor

Wait 1 'wait a moment

Display Off 'turn display off

Wait 1 'wait a moment

Display On 'turn display on

'-----------------NEW support for 4-line LCD------

Thirdline

Lcd "Line 3"

Fourthline

Lcd "Line 4"

Home Third 'goto home on line three

Home Fourth

Home F 'first letteer also works

Locate 4 , 1 : Lcd "Line 4"

```vb
Wait 1

'Now lets build a special character

'the first number is the characternumber (0-7)

'The other numbers are the rowvalues

'Use the LCD tool to insert this line

```
Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character

'----------------- Now use an internal routine ------------

_temp1 = 1 'value into ACC

!rCall _write_lcd 'put it on LCD

End

---

## CONFIG MODBUS

Action

This directive sets the MAKEMODBUS data mode.

Syntax

CONFIG MODBUS = DEFAULT | VAR

Remarks

When not configured, or when DEFAULT is chosen, the number of bytes passed in MakeModBus, is determined by the data type of the variable.

When configured to VAR, the content of the variable is used to pass the number of data bytes. The maximum value is 255.

See also

[MAKEMODBUS](makemodbus.md)

Example

Print #1 , Makemodbus(2 , 1 , 8 , X); ' slave 2, function 1, address 8 , send X byes where X is loaded with the number of bytes

---

## CONFIG OPAMP

Action

This configuration statement configures the OPAMP (OPerational AMPlifier).

Syntax

CONFIG OPAMP=ENABLED|DISABLED , OPTIONn=VALUEn

The options and values depend on the processor. Below is a list of options and values. There can be multiple OPAMP'S. The X indicates the number in the range from 0-2.

Remarks

OPTION | VALUE  
---|---  
OPAMP | \- ENABLED to enable the OPAMP. \- DISABLED to disable the OPAMP.  
TIME_BASE | Controls the maximum value of a counter that counts CLK_PER cycles to achieve a time interval equal to or larger than 1 Î¼s. It should be written with one less than the number of CLK_PER cycles that are equal to or larger than 1 Î¼s. This is used for the internal timing of the warm up and settling times.  
INP_RANGE | Selects the op amp input voltage range. \- RAIL_TO_RAIL : The op amp input voltage range is rail-to-rail \- REDUCED : The op amp input voltage range and power consumption are reduced  
OPAMPx_RUNMODE | Run in standby mode. \- DISABLED : the OPx is disabled when in standby sleep mode and its output driver is disabled. \- ENABLED : the OPx will continue operating as configured in standby sleep mode.  
OPAMP0_ALWAYS_ON | Controls whether the OPAMP is always on or not. \- DISABLED : the OPx is not always on but can be enabled by the ENABLE EVENTx and disabled by the DISABLE EVENTx \- ENABLED : the OPx is always on  
OPAMP0_EVENTS | Controls event reception and generation. \- DISABLED : No events are enabled for OPx \- ENABLED : All events are enabled for OPx  
OPAMP0_OUTMODE | Selects the output mode for the output driver \- OFF : the output driver for OPx is disabled but this can overridden by the DRIVEx event \- NORMAL : the output driver for OPx is enabled in NORMAL mode  
OPAMP0_MUXWIP | Multiplexer for wiper. Selects the resistor ladder wiper (potentiometer) position \- R1_15R_R2_1R : R1=15R , R2=1R \- R1_14R_R2_2R : R1=14R , R2=2R \- R1_12R_R2_4R : R1=12R , R2=4R  \- R1_8R_R2_8R : R1=8R , R2=8R \- R1_6R_R2_10R : R1=6R , R2=10R \- R1_4R_R2_12R : R1=4R , R2=12R \- R1_2R_R2_14R : R1=2R , R2=14R \- R1_1R_R2_15R : R1=1R , R2=15R  
OPAMP0_MUXBOT | Selects the analog signal connected to the bottom resistor in the resistor ladder \- OFF : multiplexer off \- INP : positive input pin for OPx \- INN : negative input pin for OPx \- DAC : DAC output (DAC and DAC output buffer must be enabled) \- LINKOUT : OPx-1 output. When selecting LINKOUT for OP0 MUXBOT is connected to the output of OP2 \- GND : ground  
OPAMP0_MUXTOP | Selects the analog signal connected to the top resistor in the resistor ladder \- OFF : multiplexer off \- OUT : OPx output \- VDD : VDD  
OPAMP0_MUXNEG | Selects which analog signal is connected to the inverting(-) input of OPx \- INN : negative input pin for OPx \- WIP : wiper from OPx resistor ladder \- OUT : OPx output (unity gain) \- DAC : DAC output (DAC and DAC output buffer must be enabled)  
OPAMP0_MUXPOS | Selects which analog signal is connected to the non inverting(+) input of OPx \- INP : positive input pin for OPx \- WIP : wiper from OPx resistor ladder \- DAC : DAC output (DAC and DAC output buffer must be enabled) \- GND : ground \- VDDDIV2 : VDD / 2  \- LINKOUT : OPx-1 output. Only available for OP1 and OP2  \- LINKWIP : wiper from OP0 resistor ladder. Setting only available for OP2  
OPAMP0_SETTLE | Specifies the number of microseconds allowed for the opamp to settle. This value together with the value in TIME_BASE is used by an internal timer to determine when to generate the READYx event and set the SETTLED flag in the OPx_STATUS register  
OPAMP0_CAL | This value is a calibration value that adjusts the input offset voltage of the op amp. &H00 provides the most negative value of offset adjustment &H80 provides no offset adjustment, and &HFF provides the most positive value of offset adjustment  
REGMODE | \- OVERWITE : the entire register is updated.  \- PRESERVE : the register bits are preserved. See also the [AVRX](avrx.md) topic.  
  
The OPAMP has settings common for all OP's and each individual OPAMP (named OPx) has settings.

The following image from the datasheet shows a block diagram.

![opamp](opamp.png)

See also

NONE

Example

---

## CONFIG OSC XMEGA

Action

Select and enable the oscillators available to the Xmega 

See also [ATXMEGA](atxmega.md)

Syntax Xmega

CONFIG OSC=ENABLED|DISABLED , PLLOSC=ENABLED|DISABLED,  EXTOSC=ENABLED|DISABLED, 32KHZOSC=ENABLED|DISABLED,  32MHZOSC=ENABLED|DISABLED,  RANGE=range, 32KHZPOWERMODE=powermode, XOSC_SEL__STARTUP=xosc_sel_startup , PLLSOURCE=pll , PLLDIV2=plldiv , PLLMUL=pllmul , 32MHZCALIB= 32mhzcalib , 2MHZCALIB= 2mhzcalib , 2MHZDFL= 2MHZDFL , 32MHZDFL= 32MHZDFL

Remarks

OSC | Use ENABLED to enable the internal 2 MHZ oscillator. This oscillator is enabled by default. Use DISABLED to disable the internal oscillator.   
---|---  
PLLOSC | Use ENABLED to enable the PLL oscillator. The oscillator is disabled by default.  
EXTOSC | Use ENABLED to enable the external oscillator. The external oscillator is disabled by default.  
32KHZOSC | Use ENABLED to enable the internal 32 KHz oscillator. This oscillator is disabled by default.  
32MHZOSC | Use ENABLED to enable the internal 32 MHz oscillator. This oscillator is disabled by default.  
RANGE | Specify the range of the external oscillator.  \- 400KHZ_2MHZ \- 2MHZ_9MHZ \- 9MHZ_12MHZ \- 12MHZ_16MHZ This option is only needed when using the external oscillator.  
32KHZPOWERMODE | Select the power mode of the 32 KHz interal oscillator. This can be NORMAL or LOW_POWER. The default is NORMAL  
XOSC_SEL_STARTUP | The type and startup type of the crystal or resonator can be specified. Use a value of : \- EXTCLK (6 CLK) , will select external clock  \- 32KHZ (for 16 CLK) , will select 32.768 TOSC \- XTAL_256CLK (for 256 CLK), will select 0.4-16 MHz XTAL \- XTAL_1KCLK (for 1K CLK) , will select 0.4-16 MHz XTAL \- XTAL_16CLK (for 16K CLK) , will select 0.4-16 MHz XTAL  
PLLSOURCE | This option let you select the oscillator source of the PLL oscillator. Valid options are : \- RC2MHZ , the internal 2 MHz oscillator (default) \- RC32MHZ , the internal 32 MHz oscillator \- EXTCLOCK , an external clock signal or oscillator  
PLLDIV2 | This option let you select the PLL two divider. Valid options are ENABLED and DISABLED  
PLLMUL | This option let you specify the PLL multiplication factor. The numeric value must be in the range from 1-31. A value of 0 disables the multiplication.  
32MHZCALIB | This option allow you to specify the calibration source for the 32MHZ oscillator. The possible options are : \- RC32K , selects the 32.768 KHZ internal oscillator \- XOSC32, selects the 32.768 KHz crystal oscillator on TOSC \- USBSOF , selects USB start of frame  
2MHZCALIB | This option allow you to specify the calibration source for the internal 2MHZ oscillator. The possible options are : \- 32KHZINT , selects the 32.768 KHZ internal oscillator. (default) \- 32KHZ_EXT_TOSC, selects the 32.768 KHz crystal oscillator on TOSC  
32MHZDFL | This option will enable or disable the DFLL and auto calibration of the 32 MHZ oscillator. Possible values : \- ENABLED \- DISABLED  
2MHZDFL | This option will enable or disable the DFLL and auto calibration of the 2 MHZ oscillator. Possible values :  \- ENABLED \- DISABLED  
  
You can also use automatic calibration. This will calibrate the 32 MHz oscillator using the 32 KHz oscillator.

The required code :

```vb
Config Osc = (enabled or disabled), 32mhzosc = Enabled , 32khzosc = enabled

Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
```
OSC_DFLLCTRL.0 = 1 'enable   
DFLLRC32M_CTRL.0 = 1 'enable

See also

[CONFIG SYSCLOCK](config_sysclock.md)

Example

Config Osc = Enabled , 32mhzosc = Enabled ' enable 2 MHz and 32 MHz interal oscillators

PLL Example

```vb
'Clock: 32 MHz External 4 MHz Xtal, PLL x 8

Config osc = enabled , EXTOSC = enabled , pllosc = enabled , _

```
range = 2MHZ_9MHZ , startup = XTAL_16KCLK , pllsource = extclock , pllmul = 8

Config Sysclock = Pll , Prescalea = 1 , Prescalebc = 1_1

---

## CONFIG OSC XTINY

Action

Select and enables the oscillators available to the Xtiny/MegaX and AVRX

See also [AVRX](avrx.md)

Syntax

CONFIG OSC=ENABLED|DISABLED , OPTIONn=VALUEn

The options and values depend on the processor. Below is a list of options and values.

Remarks

OPTION | VALUE  
---|---  
OSC | ENABLED. The internal HF oscillator is always enabled. There is no option to disable it. So this is a kind of dummy variable.   
RUNMODE | DISABLED or ENABLED. With RUNMODE enabled the oscillator will be forced to be always on. Otherwise it is only on when required.  
AUTOTUNE | DISABLED or ENABLED. When enabled the HF oscillator can be tuned with the 32 KHz crystal oscillator. There is a CLKCTRL_OSCHFTUNE register that can be modified to tune.  
FREQUENCY | This selects the frequency of the HF oscillator. Options are : [1MHZ,2MHZ,3MHZ,4MHZ,8MHZ,12MHZ,16MHZ,20MHZ,24MHZ]. Notice that the $CRYSTAL directive should match the setting.  
PLL_RUNMODE | DISABLED or ENABLED. With RUNMODE enabled the oscillator will be forced to be always on. Otherwise it is only on when required.  
PLL_SOURCE | OSCHF or XOSCHF. THis is the clock source for the PLL. Which is either the internal HF OSC or the external HF OSC.  
PLL_MUL | DISABLED, 2 or 3. This is the PLL multiplication factor. With DISABLED, the PLL is disabled.  
OSC32_RUNMODE | DISABLED or ENABLED. With RUNMODE enabled the oscillator will be forced to be always on. Otherwise it is only on when required.  
XOSC32_RUNMODE | DISBLED or ENABLED. With RUNMODE enabled the oscillator will be forced to be always on. Otherwise it is only on when required.  
XOSC32 | DISBLED or ENABLED. This option allows to enable the EXTERNAL 32 KHZ oscillator.  
XOSC32_SEL_STARTUP | XTAL_1KCLK , XTAL_16KCLK, XTAL_32KCLK or XTAL_64KCLK. These options set the 32 OSC crystal start up time in cycles.   
XOSC32_EXT_SRC | EXT_XTAL or EXT_CLOCK_TOSC1. The source for the oscillaror. Either a crystal or an external clock signal on pin 1.  
XOSC32_LPMODE | DISABLED or ENABLED. This option sets the Low Power mode.   
XOSCHF | DISABLED,ENABLED]  
XOSCHF_RUNMODE | DISABLED or ENABLED. With RUNMODE enabled the oscillator will be forced to be always on. Otherwise it is only on when required.  
XOSCHF_SEL_STARTUP | XTAL_256CLK,XTAL_1KCLK or XTAL_4KCLK. The external HF oscillator crystal start up time.   
XOSCHF_EXT_SRC | EXT_XTAL or EXT_CLOCK_XTALHF1. This options selects the source for the external HF oscillator clock source. Either a crystal or an external clock signal on the XTALHF1 pin  
XOSCHF_RANGE | MAX_8MHZ,MAX_16MHZ,MAX_24MHZ or MAX_32MHZ. The maximum frequency supported for the external crystal. The larger the range selected the higher the current consumption by the oscillator.  
  
As you can see there are a number of oscillators available.

The internal HF oscillator. An internal 32 KHZ oscillator. An external 32 KHz xtal can be connected for an external 32 KHz oscillator, and a HF crystal can be connected to a High Frequency external crystal. 

See also

[CONFIG SYSCLOCK](config_sysclock_xtiny.md)

Example

NONE

---

## CONFIG PORT

Action

Sets the port or a port pin to the right data direction.

Syntax

```vb
CONFIG PORTx = state

CONFIG PINx = state

CONFIG PORTx.y = state

CONFIG PINx.y = state

```
Remarks

state | A numeric constant that can be INPUT or OUTPUT. INPUT will set the data direction register to input for port X. OUTPUT will set the data direction to output for port X. You can also use a number for state. &B00001111, will set the upper nibble to input and the lower nibble to output. You can either set a single port pin or a whole port to input or output. When you set a single pin , you can use INPUT, OUTPUT, 0 or 1. When you set a complete port, you can use INPUT, OUTPUT or a numeric constant that fits into a byte.  
---|---  
x | A valid port letter such as A,B,C etc.  Example : CONFIG PORTB = INPUT Example : CONFIG PINB=OUTPUT  
y | A valid pin number in the range of 0-7. Example : CONFIG PINB.0=OUTPUT Example : CONFIG PORTB.1=INPUT  
  
The best way to set the data direction for more than 1 pin, is to use the CONFIG PORT, statement and not multiple lines with CONFIG PIN statements.

You may not use variables for the port letters and pin numbers. If you need to dynamically set a pin direction, you can use this form : SET PORTB.somepin , where somepin may be a constant or a variable. 

If the the port itself is also dynamic, then you could use OUT with the proper address.

PORT and PIN can equally be used. PIN can be used to indicate that you set a single pin. And PORT can be used to indicate that you set the complete PORT. But they both do the same. 

There could be a reason to use PIN or PORT : when using an ALIAS like in this example:

Switch ALIAS PINB.0

LED ALIAS PORTB.1

```vb
CONFIG SWITCH=INPUT

CONFIG LED=OUTPUT

If SWITCH=0 THEN ' this works only on the PIN register

```
![notice](notice.jpg)When you want to read the status of an input pin you must use the PIN register.

When you want to set the output level of an output pin you must use the PORT register.

So you never write to a PIN register. Exceptions are for processors that have special ports that can toggle when you write to the PIN register. 

The compiler will handle that automatic when you use the TOGGLE statement.

The example below show how to read a pin configured to act as an input pin and how to change a pin configured as output pin.

See Also

[AVR Internal hardware ports](avr_internal_hardware_port_b.md) , [SET](set.md), [RESET](reset.md), [TOGGLE](toggle.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : port.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: PortB and PortD

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Byte , Count As Byte

'configure PORT D for input mode

Config Portd = Input

'reading the PORT, will read the latch, that is the value

'you have written to the PORT.

'This is not the same as reading the logical values on the pins!

'When you want to know the logical state of the attached hardware,

'you MUST use the PIN register.

```
A = Pind

'a port or SFR can be treated as a byte

A = A And Portd

Print A 'print it

Bitwait Pind.7 , Reset 'wait until bit is low

```vb
'We will use port B for output

Config Portb = Output

'assign value

```
Portb = 10 'set port B to 10

Portb = Portb And 2

Set Portb.0 'set bit 0 of port B to 1

Incr Portb

'Now a light show on the STK200

Count = 0

Do

Incr Count

Portb = 1

For A = 1 To 8

Rotate Portb , Left 'rotate bits left

```vb
Wait 1

Next

'the following 2 lines do the same as the previous loop

'but there is no delay

' Portb = 1

' Rotate Portb , Left , 8

Loop Until Count = 10

Print "Ready"

'Again, note that the AVR port pins have a data direction register

'when you want to use a pin as an input it must be set low first

'you can do this by writing zeros to the DDRx:

'DDRB =&B11110000 'this will set portb1.0,portb.1,portb.2 and portb.3 to use as inputs.

'So : when you want to use a pin as an input set it low first in the DDRx!

' and read with PINx

' and when you want to use the pin as output, write a 1 first

' and write the value to PORTx

End

```

---

## CONFIG PORT_MUX

Action

This configuration option allows you to configure the PORTMUX. The PORTMUX allows to chose alternative pin locations.

Syntax

CONFIG PORT_MUX = val0 , opt1=val1,opt2=val2, optx=valx

Remarks

val0 | There are 2 possible settings : \- OVERWITE : the entire register is updated.  \- PRESERVE : the register bits are preserved. See a detailed explanation below.   
---|---  
opt1, opt2, optx | These are the various options which will depend on the processor. Possible options are :  \- EVOUT0 : event output enable \- EVOUTx : event output x enable \- LUTx : alternative pin location CCL LUTx \- USARTx : alternative pin location USARTx \- SPI0 : alternative pin location SPI0 \- TWI0 : alternative pin location TWI0 \- TCA0x : alternative pin location wave output  \- TCB0x : alternative pin location wave output  
valx | The option value. It is either ENABLED or DISABLED The default register value is DISABLED.  
  
You can use the CTRL+SPACE key combination to get a list of options and values. This only works when you specified the definition file with $REGFILE. And when there are no errors in your code.

The PORTMUX is a convenient piece of hardware. It allows you to swap pin locations of hardware that share pins. As the pins are limited most pins share hardware functions.

For example for the TINY816 portA.1 : Besides being a normal port pin it is also MOSI, AIN1 and LUT0-IN1.

Now the PB2 and PB3 pins are used for TX/RX and TOSC1 and TOSC2. This means that you can not use the external oscillator AND the UART TX/RX pins. You need to chose.

But since the TX/RX pins have the option to be swapped with an alternative pin location, you can now use both !

So you would swap the USART0 pins from PB3(RX),PB2(TX),PB1(XCK) to PA1,PA2,PA3.

These PA1,PA2 and PA3 location are normally intended for the SPI and if you need that, you can also swap the SPI to PC0,PC1,PC2 and PC3.

Notice that all the device pins are swapped that belong to a device.

The following table from the data sheet make things more clear ;

![port_mux](port_mux.png)

The compiler will set the proper registers based on your configuration.

There are 2 important settings : OVERWRITE and PRESERVE. 

CONFIG PORT_MUX=PRESERVE will preserve the other settings in case they are not all configured.

Imagine a register with 4 bits and your setting only changes one bit. The compiler will read the data, change the bit and write it back.

When you change all 4 bits, the compiler will just write the new value since there is no need to preserve the old value.

When you use CONFIG PORT_MUX=OVERWRITE, the compiler will not preserve the old values, it will just write the new value. Since all registers are default 0 this is not a problem in many cases. But it could be when you dynamic change the settings.

It is important that you specify all settings on one line or use the line continuation character. This will give the best code.

When 1 register is updated, lds/sts is used while when multiple registers are updated, a pointer is used. 

So we would recommend to use OVERWRITE for the initial setup. Normally there is no need to change the configuration at run time. But when you do need to change it, use the PRESERVE mode.

Other CONFIG statements might also support the OVERWRITE/PRESERVE switch. You will find this when the REGMODE option is present among the options.

When the port multiplexer is configured it will not change the port direction settings. You need to do so yourself when that is required. 

For example when you use the default settings for the USART/COM, the TX is set to output mode. 

When you change the UART pins with the multiplexer you need to set the new TX pin to output mode. 

There is also a simpler way to just set the alternative pins for the USART. The CONFIG COMx have an option : TXPIN=xxx

Where xxx is either the default (DEF_PA0) or ALT1_PA4 or NONE. The setting values depend on the used processor.

DEF_ means that this is the default value. So you do not need to specify it. In fact when you use the default value you should not specify it since it will create more code because the port_mux is automatically set and the port mux registers are preserved.

ALT1_ means that this is the first alternative value. So PORTA4 would be used instead of PORTA.0

NONE means that none of the pins are connected. 

Since the TX pin is set to output mode, the preferred way to set the USART alternative pin is using CONFIG COM. 

The PORT_MUX will be updated automatically. In this scenario you should however use the PRESERVE mode since otherwise you might erase the USART alternative TX setting !

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : portmux.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates PORT_MUX  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 16_20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'dimension a variable  
Dim B As Byte  
  
Print "Test USART"  
  
For B = 1 To 10  
Print "Hello" ; Spc(3) ; B  
Waitms 1000  
Next  
  
'now use the port mux to switch the USART pins  
Config Port_mux = Overwrite , Usart0 = Alt1_pa1pa4 , Evout0 = Enabled  
'we need to set the new TX pin to output outselfs. This is pin PA1 for the tiny816  
Config Porta.1 = Output  
Do  
Print "ALT TX" ; Spc(3) ; B  
Waitms 1000  
```
Incr B  
```vb
Loop  
  
End

```

---

## CONFIG POWER_REDUCTION

Action

This option configures the power reduction registers to reduce power consumption.

Syntax

CONFIG POWER_REDUCTION= dummy, device=ON|OFF

Remarks

The Power Reduction (PR) registers provides a method to stop the clock to individual peripherals.

When this is done the current state of the peripheral is frozen and the associated I/O

registers cannot be read or written. Resources used by the peripheral will remain occupied;

hence the peripheral should in most cases be disabled before stopping the clock. Enabling the

clock to a peripheral again, puts the peripheral in the same state as before it was stopped. This

can be used in Idle mode and Active mode to reduce the overall power consumption significantly.

In all other sleep modes, the peripheral clock is already stopped.

Not all devices have all the peripherals associated with a bit in the power reduction registers.

Setting a power reduction bit for a peripheral that is not available will have no effect.

Device | A hardware resource of the Xmega. The following hardware resources can be deactivated to reduce power: AES EBI LCD RTC EVSYS DMA DACA, DACB ACA,ACB ADCA,ADCB TWIC,TWID,TWIE,TWIF USARTC0,USARTC1, USARTD0,USARTD1,USARTE0,USARTE1,USARTF0,USARTF1 SPIC,SPID,SPIE,SPIF TCC0,TCC1,TCD0,TCD1,TCE0,TCE1,TCF0,TCF1 HIRESC,HIRESD,HIRESE,HIRESF XCL A value of ON will leave the resource enabled and a value of OFF will activate the power reduction.  
---|---  
  
You should use the CONFIG POWER_REDUCTION at start up to disable all unused resources. All the power reduction registers will be set for the provided resources. But the existing configuration will not be preserved. When you need to enable/disable an individual resource at run time, you can manual access the register with a SET or RESET command.

For example, the DMA, EVSYS, RTC, EBI and AES bits are located in the PRGEN register. If you disable DMA and AES the compiler will write a value of 17 (dma +aes) to the PRGEN register.

It will not first read the existing value, and preserve the other bits. That is why this statement should be used once.

When you specify one value, for example DMA, it will write 1 to the PRGEN register and thus overwriting the previous AES bit that was 1, with a 0. 

The additional code to mask and set the bits did not seem useful at implementation time. At user request this behaviour can be changed in a future version.

See also

NONE

Example

```vb
'-----------------------------------------------------------  
' XM128A1-POWER-REDUCTION.BAS  
' (c) 1995-2025 MCS Electronics  
' sample provided by MAK3  
'-----------------------------------------------------------  
  
' CONFIG POWER_REDUCTION and USING EVENT SYSTEM  
  
' This Example show how to use the config power_reduction and give first insights to the XMEGA EVENT SYSTEM  
  
' Regarding the Eventsytem this example easy show after event configuration that one Port Pin is routed to another Port Pin.  
' You can see it works even during the WAIT 4 command and there are no PORT READ OR WRITE commands in the Do .... Loop !  
' It also shows how to manual fire an Event  
  
$regfile = "xm128a1def.dat"  
$crystal = 2000000 ' 2MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Enabled  
Config Sysclock = 2mhz ' 2MHz  
  
' YOU CAN MINIMIZE POWER CONSUMPTION FOR EXAMPLE WITH :  
' 1. Use Low supply voltage  
' 2. Use Sleep Modes  
' 3. Keep Clock Frequencys low (also with Precsalers)  
' 4. Use Powe Reduction Registers to shut down unused peripherals  
  
'With Power_reduction you can shut down specific peripherals that are not used in your application  
'Paramters: aes,dma,ebi,rtc,evsys,daca,dacb,adca,adcb,aca,acb,twic,usartc0,usartc1,spic,hiresc,tcc0,tcc1  
Config Power_reduction = Dummy , Aes = Off , Twic = Off , Twid = Off , Twie = Off , Aca = Off , Adcb = Off , Tcc0 = Off , Tcc1 = Off , Dma = Off  
  
'For the following we need the EVENT System therefore we do not shut down EVENT SYSTEM  
  
Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM1:" For Binary As #1  
```vb
Waitms 2  
  
Print #1 ,  
Print #1 , "-----------S T A R T-----------------"  
  
'Configure PC0 for input, triggered on falling edge  
Config Pinc.0 = Input  
```
Portc_pin0ctrl = &B00_011_010  
```vb
'^ ^  
'^ React on falling edge (010)  
'^  
'enable Pullup  
  
'Select PC0 as input to event channel 0  
'select the event source for Event Channel 0  
```
Evsys_ch0mux = &B0110_0_000 'Event Source for Event Channel 0 = Portc.0  
```vb
'^ ^  
'^ ^  
'^ Pin0  
'portC  
  
```
Evsys_ch0ctrl = &B0_00_0_0_111 '8 SAMPLES for Digital Filter  
```vb
'^  
'Digital Filter config  
Config Pinc.7 = Output  
'Event Channel 0 Ouput Configuration  
```
Portcfg_clkevout = &B0_0_01_0_0_00 'Output on PINC.7 /Clock Out must be disabled  
  
```vb
Print #1 , "Portcfg_clkevout = " ; Bin(portcfg_clkevout)  
Print #1 , "Mainloop -->"  
  
  
Do  
'IMPORTANT: YOU WILL SEE THE PIN CHANGES ALSO DURING WAIT 4 BECAUSE IT USE EVENT SYSTEM  
Wait 4  
  
'This shows how to manual fire an Event  
Set Evsys_strobe.0  
Loop  
  
End 'end program

```

---

## CONFIG POWERMODE

Action

Put the micro processor in one of the supported power reserving modes. 

Config Powermode is for ATTINY, ATMEGA and ATXMEGA devices.

Syntax

CONFIG POWERMODE = mode

Example

Config Powermode = Powerdown

or

CONFIG POWERMODE = IDLE

Remarks

The mode depends on the micro processor.

Some valid options for ATTINY and ATMEGA are :

\- IDLE

\- POWERDOWN

\- STANDBY

\- ADCNOISE

\- POWERSAVE

Valid option for ATXMEGA are:

\- Idle

\- PowerDown

\- PowerSave

\- Standby

\- ExStandby

The modes and their exact behaviour is different on all processors. The following description from the data sheet is for the Mega88P.

Keep in mind that you can only achieve the low current consumption of ATTINY and ATMEGA in PowerDown mode when you also consider the "MINIMIZING POWER CONSUMPTION" 

section in the data sheet like:

```vb
' 1. Disable/Switch off ADC  
' 2. Disable/Switch off Analog Comparator  
' 3. Disable Brown-out Detection when not needed  
' 4. Disable internal voltage reference  
' 5. Disable Watchdog Timer when not needed  
' 6. Disable the digital input buffer  
' 7. Enable Pull-up or pull-down an all unused pins

```
In case of ATXMEGA see also [CONFIG POWER_REDUCTION](config_power_reduction.md) to reduce the power consuption in all modes.

![notice](notice.jpg) If you measure the current consumption not between the LDO and AVR don't forget to use Low Quiescent Current LDO for example MCP1700, AS1375 or TPS78233 to really get close to the current consumption in the data sheet.

![notice](notice.jpg) You can also minimize power consumption by keeping the clock frequency as low as possible if sleep modes are not used.

Wake up from Sleep Modes

In the AVR data sheets you find under the sleep modes the wake up sources for sleep modes.

For example for an ATTINY25/45/85. The only wake up Sources from PowerDown are:

•| INT0 and Pin Change (For INT0, only level interrupt)  
---|---  
  
•| USI Start Condition  
---|---  
  
•| Watchdog Interrupt  
---|---  
  
The wake up sources for an ATXMEGA32A4U from powerdown are:

•| USB Resume  
---|---  
  
•| Asynchronous Port Interrupts  
---|---  
  
•| TWI Address Match Interrupts  
---|---  
  
Asynchronous pin-change sensing with ATXMEGA means that a pin change can wake the device from all sleep modes, included the modes where

no clocks are running (Synchronous sensing requires the presence of the peripheral clock, while asynchronous sensing does not require any

clock.)

See also: [ATXMEGA](atxmega.md)

You will find an example below with ATXMEGA, PowerDown and Wake up from asynchronous Port Pin.

Example for Powerdown with ATXMEGA

  
  
```vb
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Power_reduction = Dummy , Aes = Off , Twic = Off , Twid = Off , Twie = Off , Aca = Off , Adcb = Off , Tcc0 = Off , Tcc1 = Off , Dma = Off  
  
' Here you have 5 seconds to measure the current consumption with multi meter  
wait 5  
  
Config Powermode = Powerdown  
  
End

```
Example with ATXMEGA, PowerDown and Wake up from asynchronous Port Pin.

  
```vb
' The following example give you 5 seconds to measure the current in active mode  
' Then you have time to measure the current in PowerDown mode  
' after this you can wake up the XMEGA from PowerDown with Portf.2 until the ATXMEGA will

' go to PowerDown mode again after 5 seconds  
' The hardware used for this example is XMEGA-A3BU Xplained board from ATMEL  
  
$regfile = "XM256A3BUDEF.DAT"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 80  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Power_reduction = Dummy , Aes = Off , Twic = Off , Twid = Off , Twie = Off , Aca = Off , Adcb = Off , Tcc0 = Off , Tcc1 = Off , Dma = Off  
  
Config Priority = Static , Vector = Application , Lo = Enabled , Med = Enabled , Hi = Enabled  
  
'When a button is pressed it will drive the I/O line to GND.  
'We use SW2 (Switch 2) on the A3BU XPLAINED Board  
'This Switch is connected to PortF.2 which is an asynchronous Pin (Every Pin 2 is an asynchronous pin)  
  
'Other Pins can also wake up the XMEGA but only "Both Edges" and "Low Level is supported and in addition the  
'Pin value must be kept unchanged during wake up  
  
On Portf_int0 Wake_up  
Enable Portf_int0 , Hi  
  
Config Portf.2 = Input  
Config Xpin = Portf.2 , Sense = Falling  
```
Portf_int0mask = &B0000_0100 ' Assign pin F2  
  
```vb
Enable Interrupts  
  
Do  
' Here you have 5 seconds to measure the current consumption with multi meter  
wait 5  
Config Powermode = Powerdown  
Loop  
  
End  
  
```
Wake_up:  
  
Return  


IDLE MODE (ATMEGA88)

The Idle mode will stop the CPU but allowing the SPI, USART, Analog Comparator, ADC, 2-wire Serial

Interface, Timer/Counters, Watchdog, and the interrupt system to continue operating. This sleep

mode basically halts clkCPU and clkFLASH, while allowing the other clocks to run.

Idle mode enables the MCU to wake up from external triggered interrupts as well as internal

ones like the Timer Overflow and USART Transmit Complete interrupts. If wake-up from the

Analog Comparator interrupt is not required, the Analog Comparator can be powered down by

setting the ACD bit in the Analog Comparator Control and Status Register â ACSR. This will

reduce power consumption in Idle mode. If the ADC is enabled, a conversion starts automatically

when this mode is entered.

ADC NOISE REDUCTION (ATMEGA88)

This mode will stop the CPU but allowing the ADC, the external interrupts, the 2-

wire Serial Interface address watch, Timer/Counter2(1), and the Watchdog to continue operating

(if enabled). This sleep mode basically halts clkI/O, clkCPU, and clkFLASH, while allowing the other

clocks to run.

This improves the noise environment for the ADC, enabling higher resolution measurements. If

the ADC is enabled, a conversion starts automatically when this mode is entered. Apart from the

ADC Conversion Complete interrupt, only an External Reset, a Watchdog System Reset, a

Watchdog Interrupt, a Brown-out Reset, a 2-wire Serial Interface address match, a

Timer/Counter2 interrupt, an SPM/EEPROM ready interrupt, an external level interrupt on INT0

or INT1 or a pin change interrupt can wake up the MCU from ADC Noise Reduction mode.

POWERDOWN (ATMEGA88)

In this mode, the external Oscillator is stopped, while the external interrupts, the 2-

wire Serial Interface address watch, and the Watchdog continue operating (if enabled). Only an

External Reset, a Watchdog System Reset, a Watchdog Interrupt, a Brown-out Reset, a 2-wire

Serial Interface address match, an external level interrupt on INT0 or INT1, or a pin change

interrupt can wake up the MCU. This sleep mode basically halts all generated clocks, allowing

operation of asynchronous modules only.

Note that if a level triggered interrupt is used for wake-up from Power-down mode, the changed

level must be held for some time to wake up the MCU.

When waking up from Power-down mode, there is a delay from the wake-up condition occurs

until the wake-up becomes effective. This allows the clock to restart and become stable after

having been stopped. The wake-up period is defined by the same CKSEL Fuses that define the

Reset Time-out period, as described in âClock Sourcesâ

POWERSAVE (ATMEGA88)

This mode is identical to Power-down, with one exception:

If Timer/Counter2 is enabled, it will keep running during sleep. The device can wake up from

either Timer Overflow or Output Compare event from Timer/Counter2 if the corresponding

Timer/Counter2 interrupt enable bits are set in TIMSK2, and the Global Interrupt Enable bit in

SREG is set.

If Timer/Counter2 is not running, Power-down mode is recommended instead of Power-save

mode.

The Timer/Counter2 can be clocked both synchronously and asynchronously in Power-save

mode. If Timer/Counter2 is not using the asynchronous clock, the Timer/Counter Oscillator is

stopped during sleep. If Timer/Counter2 is not using the synchronous clock, the clock source is

stopped during sleep. Note that even if the synchronous clock is running in Power-save, this

clock is only available for Timer/Counter2.

STANDBY (ATMEGA88)

This mode is identical to Power-down

with the exception that the Oscillator is kept running. From Standby mode, the device wakes up

in six clock cycles.

EXTENDED STANDBY (ATMEGA88)

This mode is identical to

Power-save with the exception that the Oscillator is kept running. From Extended Standby

mode, the device wakes up in six clock cycles.

So for standby you would use : POWER STANDBY

It is also possible to use POWERDOWN, IDLE or POWERSAVE. These modes were/are supported by most processors. It is recommended to use the new CONFIG POWERMODE command because it allows to use more modes.

See also

[IDLE](idle.md), [POWERDOWN](powerdown.md) , [POWERSAVE](powersave.md), [CONFIG POWER_REDUCTION](config_power_reduction.md)

Example for Powerdown and wake up with ATTINY

  
```vb
' Using the new config powermode = PowerDown function with ATTINY13  
  
' Fuse Bits:  
' Disable DWEN (Debug Wire) Fuse Bit  
' Disable Brown-Out Detection in Fuse Bits  
' Disable Watchdog in Fuse Bits  
  
' You can also just use Config Powermode = Powerdown  
  
' But this example here also considers what the data sheet write under "MINIMIZING POWER CONSUMPTION"  
' You need to follow this when you want to achieve the current consumption which you find in the data sheet under Powerdown Mode  
  
' 1. Disable/Switch off ADC  
' 2. Disable/Switch off Analog Comparator  
' 3. Disable Brown-out Detection when not needed  
' 4. Disable internal voltage reference  
' 5. Disable Watchdog Timer when not needed  
' 6. Disable the digital input buffer  
' 7. Enable Pull-up or pull-down an all unused pins  
  
  
$regfile = "attiny13.dat"  
$crystal = 9600000 '9.6MHz  
$hwstack = 10  
$swstack = 0  
$framesize = 24  
  
  
On Int0 Int0_isr 'INT0 will be the wake-up source for Powerdown Mode  
Config Int0 = Low Level  
Enable Int0  
  
  
' Prepare Powerdown:  
' To minimize power consumption, enable pull-up or -down on all unused pins, and  
' disable the digital input buffer on pins that are connected to analog sources  
Config Portb.0 = Input  
Set Portb.0  
Config Portb.1 = Input 'INT0 --> external 47K pull-up  
'Set Portb.1  
Config Portb.2 = Input  
Set Portb.2  
Config Portb.3 = Input  
Set Portb.3  
Config Portb.4 = Input  
Set Portb.4  
Config Portb.5 = Input 'External Pull-Up (Reset)  
  
```
Didr0 = Bits(ain1d , Ain0d) 'Disable digital input buffer on the AIN1/0 pin  
  
```vb
Set Acsr.acd 'Switch off the power to the Analog Comparator  
'alternative:  
' Stop Ac  
  
Reset Acsr.acbg 'Disable Analog Comparator Bandgap Select  
  
Reset Adcsra.aden 'Switch off ADC  
'alternative:  
' Stop Adc  
  
'###############################################################################  
Do  
Wait 3 ' now we have 3 second to measure the Supply Current in Active Mode  
  
Enable Interrupts  
  
' Now call Powerdown function  
Config Powermode = Powerdown  
  
'Here you have time to measure PowerDown current consumption until a Low Level on Portb.1 which is the PowerDown wake-up  
Loop  
'###############################################################################  
End  
  
  
```
Int0_isr:  
```vb
' wake_up  
Return

```
Example for Idle and wake up with ATTINY

  
```vb
' Using the new config powermode = Idle function with ATTINY13  
  
' Idle: This sleep mode basically halts clkCPU and clkFLASH, while allowing the other clocks to run.  
  
' Fuse Bits:  
' Disable DWEN (Debug Wire) Fuse Bit  
' Disable Brown-Out Detection in Fuse Bits  
' Disable Watchdog in Fuse Bits  
  
  
  
$regfile = "attiny13.dat"  
$crystal = 1200000 '1.2MHz (9.6MHz/DIV8 = 1.2MHz)  
$hwstack = 10  
$swstack = 0  
$framesize = 24  
  
  
On Int0 Int0_isr 'INT0 will be the wake-up source for Idle Mode  
Config Int0 = Low Level  
Enable Int0  
  
  
'###############################################################################  
Do  
Wait 3 ' now we have 3 second to measure the Supply Current in Active Mode  
  
Enable Interrupts  
  
' Now call Idle function  
Config Powermode = Idle  
  
'Here you have time to measure Idle current consumption until a Low Level on Portb.1 which is the Idle wake-up  
Loop  
'###############################################################################  
End  
  
  
```
Int0_isr:  
```vb
' wake_up  
Return

  


```

---

## CONFIG PRINT

Action

Configure the UART to be used for RS-485

Syntax

```vb
CONFIG PRINT0 = pin, mode = mode [, delay=ms]

CONFIG PRINT1 = pin, mode = mode [, delay=ms]

CONFIG PRINT2 = pin, mode = mode [, delay=ms]

CONFIG PRINT3 = pin, mode = mode [, delay=ms]

CONFIG PRINT4 = pin, mode = mode [, delay=ms]

CONFIG PRINT5 = pin, mode = mode [, delay=ms]

CONFIG PRINT6 = pin, mode = mode [, delay=ms]

CONFIG PRINT7 = pin, mode = mode [, delay=ms]

```
Remarks

pin | The name of the PORT pin that is used to control the direction of an RS-485 driver such as PORTB.1  
---|---  
mode | SET or RESET  
delay | Optional delay in mS. This delay is used before the direction is switched back after the transmit buffer is empty. This to compensate for slow RS485 drivers.  
  
Use PRINT or PRINT0 for the first serial port. Use PRINT1 for the second serial port. PRINT2 for the third UART and PRINT3 for the fourth UART.

When you use RS-485 half duplex communication you need a pin for the direction of the data. The CONFIG PRINT automates the manual setting/resetting. It will either SET or RESET the logic level of the specified pin before data is printed with the BASCOM print routines. After the data is sent, it will inverse the pin so it goes into receive mode.

![notice](notice.jpg)You need to set the direction of the used pin to output mode yourself.

When CONFIG PRINT is used, the PRINT and PRINTBIN statements will switch the pin logic level, send the data, wait till all data is sent, optional wait the specified time in mS, and then will switch the pin logic level back.

```vb
CONFIG PRINT will not work with dynamic Xmega UARTS (BUART). You need to use a constant channel with the Xmega like PRINTBIN #1.

CONFIG PRINT does not work with buffered serial output. 

```
A popular line driver for RS485 communication is the MAX485. But most driver chips are similar. 

The driver usually has an /RE pin (/ means inverted) which need to be made low in order to enable the receiver. 

The driver also has a DE pin. Which is the driver output enable. This pin is not inverted. You need to make it high in order to enable the data driver output.

So when using the MAX485 as a master in half duplex mode to send data as in the example below, you would connect portb.0 to the DE pin. And you would use SET in the configuration since in order to print the driver must be SET high.

See also

[CONFIG PRINTBIN](config_printbin.md)

Example

```vb
'------------------------------------------------------------------------------

'name : rs485.bas

'copyright : (c) 1995-2054, MCS Electronics

'purpose : demonstrates

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'------------------------------------------------------------------------------

$regfile = "m48def.dat" ' we use the M48

$crystal = 8000000

$baud = 19200

$hwstack = 32

$swstack = 32

$framesize = 32

Config Print0 = Portb.0 , Mode = Set

Config Pinb.0 = Output 'set the direction yourself

Dim Resp As String * 10

Do

Print "test message"

Input Resp ' get response

Loop

```

---

## CONFIG PRINTBIN

Action

Configure PRINTBIN behavior

Syntax

CONFIG PRINTBIN = mode

Remarks

mode | The mode value is either EXTENDED or NORMAL. EXTENDED The extended mode is the only mode you can configure. It allows to send packets greater than 255 bytes.  For example when you need to send an array with more than 255 elements. The maximum packet size is 64 KB. Because support for big packets requires more code, it is made optional. You can not change between normal and extended mode dynamically. If you chose to use extended mode, this will be used for all your PRINTBIN code. The internal constant named _PBIN_EXTENDED will be set to 1. When you do not configure PRINTBIN, it will have the default value of 0. NORMAL The normal mode is the default. When you do not use CONFIG PRINTBIN, the default NORMAL mode is selected.  You can not switch dynamic between the 2 modes.  
---|---  
  
See also

[CONFIG PRINT](configprint.md) , [PRINTBIN](printbin.md)

Example

```vb
$regfile = "m103def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Printbin = Extended

Dim A(1000)

```
Printbin A(1) ; 1000

---

## CONFIG PRIORITY XMEGA

Action

Configures the interrupt system and priority for Xmega 

Syntax

CONFIG PRIORITY= prio, VECTOR= vector, HI= hi, LO= lo, MED= med 

Remarks

prio | STATIC or ROUNDROBIN. In the AVR the lowest interrupt address has the highest priority. When you chose STATIC the interrupts behave as in non-Xmega chips. To prevent that a low priority interrupt never get executed you can select ROUNDROBIN  
---|---  
vector | APPLICATION or BOOT. Application is the default. This will place the interrupt vectors at address 0, the starting address.  When you chose BOOT, the interrupt vectors are placed at the beginning of the boot section. This makes it possible to use interrupts in a boot application.  
hi | ENABLED or DISABLED. Chose ENABLED to enable the HI priority interrupts.  
lo | ENABLED or DISABLED. Chose ENABLED to enable the LO priority interrupts.  
med | ENABLED or DISABLED. Chose ENABLED to enable the MED priority interrupts.  
  
In the XMEGA, you must enable HI, LO or MED interrupts before you can use them.

When you enable an interrupt you also must specify the priority.

For example : Enable Usartc0_rxc , Lo 

This would enable the USARTC0_RX interrupt and would assign it a low priority. 

In this case, at least the LO priority should be enabled :

Config Priority = Static , Vector = Application , Lo = Enabled 

When you use LO and MED interrupts, you need to enable the both.

![notice](notice.jpg)When you do not specify the priority when enabling an interrupt like : ENABLE Tcc0_ovf , the compiler will use the MED interrupt level. This means that you must enable this as well when using CONFIG PRIORITY. When you do NOT use CONFIG PRIORITY, but only ENABLE INTERRUPTS, the compiler will activate the MED interrupt automatically. 

So when not using CONFIG PRIORITY all will work out just fine, but when using CONFIG PRIORITY, do not forget to enable the MED priority.

See also

[ENABLE](enable.md) , [DISABLE](disable.md) , [ON](on_interrupt.md)

Example

```vb
Config Priority = Static , Vector = Application , Lo = Enabled

On Usartc0_rxc Rxc_isr

Enable Usartc0_rxc , Lo

Enable Interrupts

```

---

## CONFIG PRIORITY XTINY

Action

Configures the interrupt system and priority for Xmega 

Syntax

CONFIG PRIORITY= prio, VECTOR= vector, COMPACT= compact , HI= hi

Remarks

prio | STATIC or ROUNDROBIN. In the AVR the lowest interrupt address has the highest priority. When you chose STATIC the interrupts behave as in non-Xmega chips. To prevent that a low priority interrupt never get executed you can select ROUNDROBIN  
---|---  
vector | APPLICATION or BOOT. Application is the default. This will place the interrupt vectors at address 0, the starting address.  When you chose BOOT, the interrupt vectors are placed at the beginning of the boot section. This makes it possible to use interrupts in a boot loader application.  
compact | ENABLED or DISABLED. Chose ENABLED to write a compact interrupt table.  
hi | The interrupt that should be given a HIGH priority. Only one interrupt can be given a HIGH priority.  Possible values : NMI,VLM,PORTA_INT,PORTB_INT,PORTC_INT,RTC_OVF,PIT_OVF,TCA0_LUNF,TCA0_HUNF,TCA0_CMP0,TCA0_CMP1,TCA0_CMP2,TCB0_INT,TCD0_OVF,TCD0_TRIG,AC0_COMP0,ADC0_RDY,ADC0_WCOMP,TWI0_SLAVE,TWI0_MASTER,SPI0_INT,USART0_RXC,USART0_DRE,USART0_TXC,NVM_EE  
  
In the XTINY, you can provide one interrupt to be serviced with a HIGH priority.

By default the interrupt address with the lowest address will get the highest interrupt. This is NMI with address 0. 

After that the PORT interrupts will get priority over all the other interrupts.

When you would like that USART0_RXC would get a HIGH (or the highest) interrupt, you can specify the interrupt name so it will be serviced with the highest priority.

Config Priority = Static , Vector = Application , HI = USART0_RXC 

See also

[ENABLE](enable.md) , [DISABLE](disable.md) , [ON](on_interrupt.md)

Example

```vb
Config Priority = Static , Vector = Application , Hi = USART0_RXC

On Usartc0_rxc Rxc_isr

Enable Usartc0_rxc 

Enable Interrupts

```

---

## CONFIG PS2EMU

Action

Configures the PS2 mouse data and clock pins.

Syntax

CONFIG PS2EMU= int , DATA = data, CLOCK=clock

Remarks

Int | The interrupt used such as INT0 or INT1.  
---|---  
DATA | The pin that is connected to the DATA line. This must be the same pin as the used interrupt.  
CLOCK | The pin that is connected to the CLOCK line.  
  
![ps2-male](ps2-male.gif) | ![ps2-female](ps2-female.gif) | 5-pin DIN (AT/XT):  1 - Clock 2 - Data 3 - Not Implemented 4 - Ground 5 - +5v  
---|---|---  
  
![ps2-male6](ps2-male6.gif) | ![ps2-female6](ps2-female6.gif) | 6-pin Mini-DIN (PS/2): 1 - Data 2 - Not Implemented 3 - Ground 4 - +5v 5 - Clock 6 - Not Implemented  
---|---|---  
  
Old PCâs are equipped with a 5-pin DIN female connector. Newer PCâs have a 6-pin mini DIN female connector.

The male sockets must be used for the connection with the micro.

Besides the DATA and CLOCK you need to connect from the PC to the micro, you need to connect ground. You can use the +5V from the PC to power your microprocessor.

The config statement will setup an ISR that is triggered when the INT pin goes low. This routine you can find in the library.

The ISR will retrieve a byte from the PC and will send the proper commands back to the PC.

The SENDSCAN and PS2MOUSEXY statements allow you to send mouse commands.

Note that the mouse emulator is only recognized after you have booted your PC. Mouse devices can not be plugged into your PC once it has booted. Inserting a mouse or mouse device when the PC is already booted, may damage your PC.

See also

[SENDSCAN](sendscan.md), [PS2MOUSEXY](ps2mousexy.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : ps2_emul.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PS2 Mouse emulator

'micro : 90S2313

'suited for demo : NO, commercial addon needed

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "mcsbyteint.lbx" ' use optional lib since we use only bytes

'configure PS2 pins

Config Ps2emu = Int1 , Data = Pind.3 , Clock = Pinb.0

' ^------------------------ used interrupt

' ^----------- pin connected to DATA

' ^-- pin connected to clock

'Note that the DATA must be connected to the used interrupt pin

Waitms 500 ' optional delay

Enable Interrupts ' you need to turn on interrupts yourself since an INT is used

Print "Press u,d,l,r,b, or t"

Dim Key As Byte

Do

```
Key = Waitkey() ' get key from terminal

```vb
Select Case Key

Case "u" : Ps2mousexy 0 , 10 , 0 ' up

Case "d" : Ps2mousexy 0 , -10 , 0 ' down

Case "l" : Ps2mousexy -10 , 0 , 0 ' left

Case "r" : Ps2mousexy 10 , 0 , 0 ' right

Case "b" : Ps2mousexy 0 , 0 , 1 ' left button pressed

```
Ps2mousexy 0 , 0 , 0 ' left button released

```vb
Case "t" : Sendscan Mouseup ' send a scan code

Case Else

End Select

Loop

```
Mouseup:

Data 3 , &H08 , &H00 , &H01 ' mouse up by 1 unit

---

## CONFIG RAINBOW

Action

This configuration command sets up the number of rainbow channels and their ports & pins.

Syntax

CONFIG RAINBOW=channels, [,RGB=rgb] , RBx_LEN=leds, RBx_PORT=port, RBx_PIN=pin

Remarks

Channels | The number of channels. This is a numeric value in the range from 1-16. Each channel drives a port pin.  
---|---  
RGB | An optional parameter that has to be defined second when used. The WS2812 leds are GRB leds. (green, red, blue). 24 bits of data are sent. RGBW leds have an additional white led and are mapped RGBW. 32 bits of data are sent.  The possible options are : 3 - The default. Leds like WS2811/WS2812 with GRB order. 4 - RGBW leds like SK6812RGBW. Notice that 1 more byte internal memory is needed for each led. This option will use RAINBOWBSCN.lib   
RBx_LEN | The number of LED's for the channel. The minimum number of leds is 1. Each LED is made of 3 colors : R(ed), G(reen), and B(lue). A byte array named RAINBOW0_ will be created with a size of len * 3. Thus RB0_LEN=8 will create an array of RAINBOW0_(24).  For RGBW LEDS, the array will have a length of len * 4 to store the additional white color.  
RBx_PORT | The name of the PORT which is connected to the DI of the rainbow led(stripe). This is a port like PORTB.  
RBx_PIN | The pin number of the port pin which is connected to the DI of the rainbow led(stripe). This is a number between 0-7.  
  
* The x should be replaced by a numeric value from 0-7.

Rainbow leds come in different forms and shapes. There are single LED, stripes with 8 leds, round circles with 24 leds, etc. All have a built in WS2812 RGB controller. The nice thing is that you can cascade leds by connecting the DO (output) to another DI (input). These stripes only requires 5V, GND and DI. You can connect different stripes to different port pins. 

The original rainbow library is written by Galahat from the German bascom-forum. It is an excellent example on how to write your own libraries. 

The MCS version is for the BASCOM integrated statements and functions. It is named rainbowBSC.lib. The lib uses a few routines from mcs.lib

![notice](notice.jpg)A minimum CPU-speed of 8 MHz is required. Tests with WS1812b- types showed, it also works with frequencies down to 6.5 MHz because of the tolerance bandwidth by the chips.

Each LED requires 3 or 4 bytes of memory to store the color. Internally, the color info is stored in RGB order. And for RGBW LEDS in RGBW color.

In version 2081 the library was updated to support RGBW LEDS. Some functions in the old lib manipulated the wrong colors. We corrected this in the new library. But to ensure compatibility, we also include the old library.

When you use RGB=4 you will use the new library automatically. Without this option, or when using a value of 3 : RGB=3 , you will use the old library.

In order to use the new library with option 3, you need to include the library in your code using the $LIB directive : $lib "RAINBOWBSCN.lib" 

This must be done BEFORE the CONFIG RAINBOW statement.

When using a normal AVR processor the used port must have a low IO address. Most ports have such an address. But processors like the Mega2560 also have some ports with an extended address. PORTH, PORTJ, PORTK and PORTL for example will not work. 

See also

[RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md)

Example

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_Knightrider.bas  
' based on sample from Galahat  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
Config RAINBOW=1, RB0_LEN=8, RB0_PORT=PORTB,rb0_pin=0  
' ^ connected to pin 0  
' ^------------ connected to portB  
' ^-------------------------- 8 leds on stripe  
' ^------------------------------------- 1 channel  
  
  
'Global Color-variables  
Dim Color(3) as Byte  
```
R alias Color(_base) : G alias Color(_base + 1) : B alias Color(_base + 2)  
  
'CONST  
const numLeds=8  
  
```vb
'----[MAIN]---------------------------------------------------------------------  
Dim n as Byte  
  
```
RB_SelectChannel 0 ' select first channel  
R = 50 : G = 0 : B = 100 ' define a color  
RB_SetColor 0 , color(1) ' update leds  
RB_Send  
  
```vb
Do  
For n = 1 to Numleds-1  
```
rb_Shiftright 0 , Numleds 'shift to the right all leds except the last one  
Waitms 100  
RB_Send  
```vb
Next  
For n = 1 to Numleds-1  
```
rb_Shiftleft 0 , Numleds 'shift to the left all leds except the last one  
Waitms 100  
RB_Send  
```vb
Next  
waitms 500 'wait a bit  
Loop  


```
EXAMPLE RGBW

```vb
'-------------------------------------------------------------------------------  
' rainbow_ws2812_KnightriderDual-RGBW.bas  
' based on sample from Galahat  
'-------------------------------------------------------------------------------  
$Regfile = "m88pdef.dat"  
$Crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 32  
  
Config RAINBOW = 1 , rgb = 4 , RB0_LEN = 8 , RB0_PORT = PORTB , rb0_pin = 0  
' ^-- using rgbW leds #### MUST BE FIRST PARAMETER when defined ###  
' ^ connected to pin 0  
' ^------------ connected to portB  
' ^-------------------------- 8 leds on stripe  
' ^------------------------------------- 1 channel  
  
  
'Global Color-variables  
Dim Color(4) as Byte  
```
R alias Color(_base) : G alias Color(_base + 1) : B alias Color(_base + 2) : W alias color(_base + 3)  
  
'CONST  
const numLeds = 8  
  
```vb
'----[MAIN]---------------------------------------------------------------------  
Dim n as Byte  
  
```
RB_SelectChannel 0 ' select first channel  
R = 50 : G = 0 : B = 100 : w = 10 ' define a color  
RB_SetColor 0 , color(_base) ' update led on the left  
RB_SetColor numleds - 1 , color(_base) ' update led on the right  
RB_Send  
```vb
waitms 2000  
  
Do  
For n = 1 to Numleds / 2 - 1  
```
rb_Shiftright 0 , Numleds / 2 'shift to the right  
rb_Shiftleft Numleds / 2 , Numleds / 2 'shift to the left all leds except the last one  
Waitms 1000  
RB_Send  
```vb
Next  
For n = 1 to Numleds/2 - 1  
```
rb_Shiftleft 0 , Numleds / 2 'shift to the left all leds except the last one  
rb_Shiftright Numleds / 2 , Numleds / 2 'shift to the right  
Waitms 1000  
RB_Send  
```vb
Next  
waitms 500 'wait a bit  
Loop

```

---

## CONFIG RC5

Action

Overrides the RC5 pin assignment from the [Option Compiler Settings](options_compiler_i2c__spi__1wire.md).

Syntax

CONFIG RC5 = pin [,TIMER=2] [,WAIT=value] [,MODE=BACKGROUND]

Syntax XTINY

CONFIG RC5 = pin [,TIMER=TCAx|TCBx] [,WAIT=value] [,MODE=BACKGROUND]

Remarks

Pin | The port pin to which the RC5 receiver is connected.  
---|---  
TIMER | Must be 2. The micro must have a timer2 when you want to use this option. This additional parameter will cause that TIMER2 will be used instead of the default TIMER0. XTINY : for the normal mode the timer can be TCAx or TCBx. For example TCA0. XTINY : for the background mode the timer can be only a TCBx timer like TCB0.  
WAIT | The default value is 100. Each unit is ca. 64 us. This gives a time out of 6.4 ms. Since a start bit is 3.5 ms, you can reduce the value to 56. When you make it lower, it will not work. When you want the old behavior you need to specify a value of 2000 which is ca. 131 ms. The WAIT parameter only has effect on the normal mode. It will not work with the BACKGROUND mode. When no valid RC5 start bit is detected, both command and address will be set to 255.   
MODE | The only possible value is BACKGROUND. The MODE parameter is optional. When used, an alternative library will be used to decode the RC5 signals on the background. This means that GETRC5 will not wait for a signal but that a bit will be set to indicate that a valid RC5 signal is received. This is bit : _rc5_bits.4 The variable _rc5_bits is automatically created when you use the MODE=BACKGROUND. This option is not available in the DEMO. The background mode will use a 16 bit timer in capture mode. It also means that you need to connect the IR-transmitter output pin to the ICP capture pin of the timer.  When using the background mode, you must specify a 16 bit timer. When you include a constant in your code like : CONST=_RC5_TOGGLE=1 , you will get the toggle bit in the address byte.5. Without this constant you will not get this bit. The prescaler value is calculated depending on the used crystal. Some desirable prescale values do not exist is some processors. Such as the 16 divider. In such a case you can override the automatic calculated value by specifying : PRESCALER=64. Typical you would try this when you get a compile error about a missing prescaler value. It is important that the PRESCALER precedes the MODE. Example : Config Rc5 = Pind.6 , Timer = 1 , PRESCALER=64, Mode = Background XTINY : For the Xtiny platform a TCBx timer is used. But the advantage of Xtiny is that you can use any processor pin. The Xtiny platform does require an additional configuration : the event system must be configured in a way that the the pin used for RC5 detection is routed to the timer TCB capture event.  We can do that like this :  
```vb
'setup RC5 and specify pin to use, and the timer which should be a timer type TCB !!!  
Config Rc5 = Pind.1 , Mode = Background , Timer = Tcb1  
Config Event_system = Dummy , Ch2 = Pd1 , Evsys_usertcb1capt = Ch2  
```
The PD1 (PIND.1) pin is the event generator since it will receive RC5 pulses. The timer TCB1 in the above sample, is the event user : it will get the generated event. We use the timer capture unit. In this example channel 2 is used to connect the event and the user. Notice that each channel can access a number of events. Other pins might requires a different channel! It is important that PIND.1 of config-rc5 matches the PD1 of config event_system.  And ch2 of PD1 must match the channel of the evsys_userTCBxcapt register.  
  
When you use different pins in different projects, you can use this statement to override the Options Compiler setting for the RC5 pin. This way you will remember which pin you used because it is in your code and you do not have to change the settings from the options. In BASCOM-AVR the settings are also stored in the project.CFG file. We recommend to use the CONFIG commands.

See also

[GETRC5](getrc5.md) , [RC5SEND](rc5send.md)

Example

```vb
'-------------------------------------------------------------------  
' RC5.BAS  
' (c) 1995-2025 MCS Electronics  
' based on Atmel AVR410 application note  
'-------------------------------------------------------------------  
$RegFile = "m88def.dat"  
  
$Baud = 19200  
$Crystal = 16000000  
  
'This example shows how to decode RC5 remote control signals  
'with a SFH506-35 IR receiver.  
  
'Connect to input to PIND.2 for this example  
'The GETRC5 function uses TIMER0 and the TIMER0 interrupt.  
'The TIMER0 settings are restored however so only the interrupt can not  
'be used anymore for other tasks  
  
  
'tell the compiler which pin we want to use for the receiver input  
  
Config Rc5 = PIND.2 , Wait = 2000  
Config Timer1 = Timer , Prescale = 1  
  
'the interrupt routine is inserted automatic but we need to make it occur  
'so enable the interrupts  
Enable Interrupts  
  
'reserve space for variables  
Dim Address As Byte , Command As Byte  
Print "Waiting for RC5..."  
  
Do  
'now check if a key on the remote is pressed  
'Note that at startup all pins are set for INPUT  
'so we dont set the direction here  
'If the pins is used for other input just unremark the next line  
'Config Pind.2 = Input  
'Print Timer1 disable this line to see the different with the various WAIT constants  
```
GetRC5(Address , Command)  
  
```vb
'we check for the TV address and that is 0  
If Address = 0 Then  
'clear the toggle bit  
'the toggle bit toggles on each new received command  
'toggle bit is bit 7. Extended RC5 bit is in bit 6  
```
Command = Command And &B01111111  
```vb
Print Address ; " " ; Command  
End If  
Loop  
End

```
Example MODE=background 

```vb
'----------------------------------------------------------------------------------------------------------  
' (c) 1995-2025  
' RC5-background.bas  
' this sample receives RC5 on the background. it will not block your code like getrc5  
' it requires a 16 bit timer with input capture. you can not use the timer yourself.  
' some processors have multiple 16 bit timers.  
'----------------------------------------------------------------------------------------------------------  
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Rc5 = Pinb.0 , Timer = 1 , Mode = Background  
' ^--- background interrupt mode  
' ^--- this must be a 16 bit timer  
' ^---- this is the timer input capture pin  
  
Enable Interrupts ' you must enable interrupts since input capture and overflow are used  
  
  
Print "RC5 demo"  
  
Do  
If _rc5_bits.4 = 1 Then ' if there is RC5 code received  
```
_rc5_bits.4 = 0 ' you MUST reset this flag in order to receive a new rc5 command  
  
```vb
Print "Address: " ; Rc5_address ' Address  
Print "Command: " ; Rc5_command ' Command  
End If  
Loop

```
Xtiny Background Example

```vb
'--------------------------------------------------------------------------------  
'name : avrx128da28-rc5-background.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 in background mode using timer TCB1  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 64  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24MHZ  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'setup RC5 and specify pin to use, and the timer which should be a timer type TCB !!!  
Config Rc5 = Pind.1 , Mode = Background , Timer = Tcb1  
Config Event_system = Dummy , Ch2 = Pd1 , Evsys_usertcb1capt = Ch2  
'it is very important that you also configure the event system  
'you need to chose a channel that has access to the PIN used for the RC5 input in this case PIND.1  
'this pin will create an event when it changes. And you need to connect the TCB CAPTURE user to this channel  
'In this example we use TCB1 thus EVSYS_USER will be evsys_userTCB1CAPT, and since PD1 (pin D.1) is connected to  
'channel 2, we also need to select channel 2.  
'Now there is a path from PIN2.1 to TCB0, capture event  
'The compiler could have created this link too but then it is not clear to the user that this event channel is used  
'for this reason you need to configure it manual  
  
print "RC5 test"  
  
Dim B As Byte  
Enable Interrupts 'since interrupts are used we must enable the global interrupt switch  
  
  
do  
If _rc5_bits.4 = 1 Then 'this variable is automatically created  
```
_rc5_bits.4 = 0  
  
```vb
Print "Address: " ; Rc5_address 'auto created variable  
Print "Command: " ; Rc5_command 'auto created variable  
End If  
loop  
  
End

```

---

## CONFIG RC5SEND

Action

Defines the RC5SEND timer and WaveOutput pin.

Syntax

CONFIG RC5SEND = timer, WO=wo

Remarks

TIMER | The TIMER must be TCA0 or when available TCA1 or any oher TCA timer.  
---|---  
WO | The Wave Output pin (WO). This is WO0, WO1 or WO2.  
  
RC5SEND uses a TCA timer in frequency generating mode in order to create a 36 KHz carrier wave.

You can chose any available WO pin. You can also use the PORTMUX to use a different port. 

You must set the corresponding pin to OUTPUT mode using : CONFIG pin statement. The pin must also be set to 1. 

While the compiler could do all this it would need to deal with the portmux. The portmux is a great piece of hardware that allows you to chose alternative pin locations. 

When the compiler performs this automatic it would not be visible to the user. So we have chosen that we leave this to the user.

See also

[GETRC5](getrc5.md) , [RC5SEND](rc5send.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name : avrx128da28-rc5-background-send-receive.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates GETRC5 in background mode using timer TCB1  
' and RC5 transmission using TCA0  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 64  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'setup RC5 receive and specify pin to use, and the timer which should be a timer type TCB !!!  
Config Rc5 = Pind.1 , Mode = Background , Timer = Tcb1  
Config Event_system = Dummy , Ch2 = Pd1 , Evsys_usertcb1capt = Ch2  
'it is very important that you also configure the event system  
'you need to chose a channel that has access to the PIN used for the RC5 input in this case PIND.1  
'this pin will create an event when it changes. And you need to connect the TCB CAPTURE user to this channel  
'In this example we use TCB1 thus EVSYS_USER will be evsys_userTCB1CAPT, and since PD1 (pin D.1) is connected to  
'channel 2, we also need to select channel 2.  
'Now there is a path from PIN2.1 to TCB0, capture event  
'The compiler could have created this link too but then it is not clear to the user that this event channel is used  
'for this reason you need to configure it manual  
  
'for the RC5 transmission we need a TCA0 WOx pin. This pin is used in output mode.  
'we will use WO2 which is connected to PA2. you could use config port_mux to chose an altenative pin  
'the IR diode anode is connected to the power(vcc) and the cathode is connected to a 220 ohm resistor  
' the other end of the resistor is connected to the WO2 pin, porta.2 in this case  
Config Pina.2 = Output : Porta.2 = 1 'set the port direction and also set the pin high  
  
'we need this new command to select the timer (tca0 or when available tca1) and the WO pin  
'the timer is operated in frequency generation mode, 36 KHz for RC5  
Config Rc5send = Tca0 , Wo = Wo2  
  
Dim Bcmd As Byte  
Enable Interrupts 'since interrupts are used we must enable the global interrupt switch  
  
Print "RC5 test,REV:" ; Hex(syscfg_revid)  
  
Do  
```
Incr Bcmd  
Rc5send 0 , 0 , Bcmd 'send RC5 code  
```vb
Waitms 500 'wait 500 msec  
  
'this is the background mode part that receives from the IR led or a remote control  
If _rc5_bits.4 = 1 Then 'this variable is automatically created  
```
_rc5_bits.4 = 0  
```vb
Print "Address: " ; Rc5_address 'auto created variable  
Print "Command: " ; Rc5_command 'auto created variable  
End If  
loop  
  
End  
  
  


```

---

## CONFIG RND

Action

This option will set the randomize configuration.

Syntax

CONFIG RND = 16|32

Remarks

By default rnd() is created using 16 bit multiplying and division. This limits the maximum number to a word. The ___Rseed variable is a word.

When you need to have a bigger random number you can use the CONFIG RND = 32 option.

When using 32 bit resolution, only division is used to limit the number with the specified number. 

Using 32 bit the ___Rseed will be a DWORD and not a WORD.

See also

[RND](rnd.md)

Example

```vb
' Plot  
' FT800 platform.  
' Original code from http://gameduino2.proboards.com/thread/11/screen-plotting  
  
' Comments by James Bowman:  
' Sets up the whole screen as a framebuffer, in PALETTED mode, which should be good for the fractals.  
' setpal() sets palette entry 'i' to a 32-bit ARGB color, and plot(x, y, i) sets a single pixel to index 'i'.  
  
' Requires Bascom 2.0.7.8 or greater  
  
$Regfile = "M328pdef.dat"  
$Crystal = 8000000  
$Baud = 19200  
$HwStack = 80  
$SwStack = 80  
$FrameSize = 300  
$NOTYPECHECK  
  
Config ft800=spi , ftsave=0, ftdebug=0 , ftcs=portb.2, ftpd=portb.1  
  
Config Base = 0  
Config Submode = New  
Config Spi = Hard, Interrupt = Off, Data_Order = Msb, Master = Yes, Polarity = Low, Phase = 0, Clockrate = 4, Noss = 1  
```
SPSR = 1 ' Makes SPI run at 8Mhz instead of 4Mhz  
  
  
```vb
Config RND = 32  
  
$Include "FT800.inc"  
$Include "FT800_Functions.inc"  
  
Declare Sub setup  
Declare Sub setpal (Byval i As Byte, Byval argb As Long)  
Declare Sub plot (Byval x As Integer, Byval y As Integer, Byval i As Long)  
  
dim dw as Dword  
dim d1 as Dword  
dim d2 as Dword  
  
```
Spiinit  
  
  
```vb
If FT800_Init() = 1 Then  
print "END"  
END ' Initialise the FT800  
end if  
  
```
Setup  
  
Do  
d1 = rnd(Ft_DispWidth-1)  
d2 = rnd(Ft_DispHeight-1)  
plot d1, d2, rnd(255)  
```vb
Loop  
  
  
  
END  
  
'------------------------------------------------------------------------------------------------------------  
Sub Setup  
'------------------------------------------------------------------------------------------------------------  
  
```
Local i As Byte  
  
CmdMemset 0, 0, Ft_DispWidth * Ft_DispHeight  
ClearScreen  
BitmapLayout PALETTED, Ft_DispWidth , Ft_DispHeight  
BitmapSize NEAREST, BORDER, BORDER, Ft_DispWidth, Ft_DispHeight  
BitmapSource 0  
Begin_G BITMAPS  
Vertex2ii 0, 0, 0, 0  
  
UpdateScreen  
  
setpal 0, &H00000000  
  
For i = 1 to 255  
setpal i, rnd(16777216) or &Hff000000  
```vb
Next  
End Sub ' Setup  
  
'------------------------------------------------------------------------------------------------------------  
Sub SetPal (Byval i As Byte, Byval argb As Long)  
'------------------------------------------------------------------------------------------------------------  
  
```
Local Temp1 As Long  
  
Temp1 = i * 4  
Temp1 = Temp1 + Ram_Pal  
Wr32 Temp1 , argb  
  
```vb
End Sub ' SetPal  
  
'------------------------------------------------------------------------------------------------------------  
Sub Plot(Byval x As Integer, Byval y As Integer, Byval i As Long)  
'------------------------------------------------------------------------------------------------------------  
  
```
Local Temp1 As Long  
  
If x < Ft_DispWidth AND y < Ft_DispHeight Then  
  
Temp1 = Ft_DispWidth * y  
Temp1 = Temp1 + x  
Wr8 Temp1, i  
  
```vb
End If  
  
End Sub ' Plot

```

---

## CONFIG SCL

Action

Overrides the SCL pin assignment from the [Option Compiler Settings](options_compiler_i2c__spi__1wire.md).

Syntax

CONFIG SCL = pin

Remarks

Pin | The port pin to which the I2C-SCL line is connected.  
---|---  
  
When you use different pins in different projects, you can use this statement to override the Options Compiler setting for the SCL pin. This way you will remember which pin you used because it is in your code and you do not have to change the settings from the options. Of course BASCOM-AVR also stores the settings in a project.CFG file.

When using the Hardware TWI, you only need CONFIG SCL when you use the I2CINIT statement

See also

[CONFIG SDA](config_sda.md) , [CONFIG I2CDELAY](config_i2cdelay.md) , [I2CINIT](i2cinit.md), [Using the I2C protocol](using_the_i2c_protocol.md)

Example 1

CONFIG SCL = PORTB.5 'PORTB.5 is the SCL line

Example 2

```vb
'-----------------------------------------------------------------------------------------  
'name : i2c.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demo: I2CSEND and I2CRECEIVE  
'micro : Mega48  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m48def.dat" ' specify the used micro  
$crystal = 4000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
'We use here the Software I2C Routines  
Config Scl = Portb.4  
Config Sda = Portb.5  
```
I2cinit  
  
```vb
Config I2cdelay = 10 '100KHz  
  
Declare Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
Declare Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
  
```
Const Addressw = 174 'slave write address  
Const Addressr = 175 'slave read address  
  
Dim B1 As Byte , Adres As Byte , Value As Byte 'dim byte  
  
Call Write_eeprom(1 , 3) 'write value of three to address 1 of EEPROM  
Call Read_eeprom(1 , Value) : Print Value 'read it back  
Call Read_eeprom(5 , Value) : Print Value 'again for address 5  
  
'-------- now write to a PCF8474 I/O expander -------  
I2csend &H40 , 255 'all outputs high  
I2creceive &H40 , B1 'retrieve input  
```vb
Print "Received data " ; B1 'print it  
End  
  
```
Rem Note That The Slaveaddress Is Adjusted Automaticly With I2csend & I2creceive  
Rem This Means You Can Specify The Baseaddress Of The Chip.  
  
  
  
```vb
'sample of writing a byte to EEPROM AT2404  
Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
```
I2cstart 'start condition  
I2cwbyte Addressw 'slave address  
I2cwbyte Adres 'asdress of EEPROM  
I2cwbyte Value 'value to write  
I2cstop 'stop condition  
```vb
Waitms 10 'wait for 10 milliseconds  
End Sub  
  
  
'sample of reading a byte from EEPROM AT2404  
Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
```
I2cstart 'generate start  
I2cwbyte Addressw 'slave adsress  
I2cwbyte Adres 'address of EEPROM  
I2cstart 'repeated start  
I2cwbyte Addressr 'slave address (read)  
I2crbyte Value , Nack 'read byte  
I2cstop 'generate stop  
```vb
End Sub  
  
' when you want to control a chip with a larger memory like the 24c64 it requires an additional byte  
' to be sent (consult the datasheet):  
' Wires from the I2C address that are not connected will default to 0 in most cases!  
  
' I2cstart 'start condition  
' I2cwbyte &B1010_0000 'slave address  
' I2cwbyte H 'high address  
' I2cwbyte L 'low address  
' I2cwbyte Value 'value to write  
' I2cstop 'stop condition  
' Waitms 10

```

---

## CONFIG SDA

Action

Overrides the SDA pin assignment from the [Option Compiler Settings](options_compiler_i2c__spi__1wire.md).

Syntax

CONFIG SDA = pin

Remarks

Pin | The port pin to which the I2C-SDA line is connected.  
---|---  
  
When you use different pins in different projects, you can use this statement to override the Options Compiler setting for the SDA pin. This way you will remember which pin you used because it is in your code and you do not have to change the settings from the options. In BASCOM-AVR the settings are also stored in the project.CFG file.

When using the Hardware TWI, you only need CONFIG SDA when you use the I2CINIT statement

See also

[CONFIG SCL](config_scl.md) , [CONFIG I2CDELAY](config_i2cdelay.md) , [I2CINIT](i2cinit.md), [Using the I2C protocol](using_the_i2c_protocol.md)

Example 1

CONFIG SDA = PORTB.7 'PORTB.7 is the SDA line

Example 2

```vb
'-----------------------------------------------------------------------------------------  
'name : i2c.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demo: I2CSEND and I2CRECEIVE  
'micro : Mega48  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m48def.dat" ' specify the used micro  
$crystal = 4000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
'We use here the Software I2C Routines  
Config Scl = Portb.4  
Config Sda = Portb.5  
```
I2cinit  
  
```vb
Config I2cdelay = 10 '100KHz  
  
Declare Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
Declare Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
  
```
Const Addressw = 174 'slave write address  
Const Addressr = 175 'slave read address  
  
Dim B1 As Byte , Adres As Byte , Value As Byte 'dim byte  
  
Call Write_eeprom(1 , 3) 'write value of three to address 1 of EEPROM  
Call Read_eeprom(1 , Value) : Print Value 'read it back  
Call Read_eeprom(5 , Value) : Print Value 'again for address 5  
  
  
'-------- now write to a PCF8474 I/O expander -------  
I2csend &H40 , 255 'all outputs high  
I2creceive &H40 , B1 'retrieve input  
```vb
Print "Received data " ; B1 'print it  
End  
  
```
Rem Note That The Slaveaddress Is Adjusted Automaticly With I2csend & I2creceive  
Rem This Means You Can Specify The Baseaddress Of The Chip.  
  
```vb
'sample of writing a byte to EEPROM AT2404  
Sub Write_eeprom(byval Adres As Byte , Byval Value As Byte)  
```
I2cstart 'start condition  
I2cwbyte Addressw 'slave address  
I2cwbyte Adres 'asdress of EEPROM  
I2cwbyte Value 'value to write  
I2cstop 'stop condition  
```vb
Waitms 10 'wait for 10 milliseconds  
End Sub  
  
  
'sample of reading a byte from EEPROM AT2404  
Sub Read_eeprom(byval Adres As Byte , Value As Byte)  
```
I2cstart 'generate start  
I2cwbyte Addressw 'slave adsress  
I2cwbyte Adres 'address of EEPROM  
I2cstart 'repeated start  
I2cwbyte Addressr 'slave address (read)  
I2crbyte Value , Nack 'read byte  
I2cstop 'generate stop  
```vb
End Sub  
  
  
' when you want to control a chip with a larger memory like the 24c64 it requires an additional byte  
' to be sent (consult the datasheet):  
' Wires from the I2C address that are not connected will default to 0 in most cases!  
  
' I2cstart 'start condition  
' I2cwbyte &B1010_0000 'slave address  
' I2cwbyte H 'high address  
' I2cwbyte L 'low address  
' I2cwbyte Value 'value to write  
' I2cstop 'stop condition  
' Waitms 10

```

---

## CONFIG SERIALIN

Action

Configures the hardware UART to use a buffer for input

Syntax

CONFIG SERIALIN | SERIALIN1 | SERIALIN2 | SERIALIN3 |SERIALx = BUFFERED , SIZE | BIGSIZE = size [, BYTEMATCH=ALL|BYTE|NONE] [,CTS=pin, RTS=pin , Threshold_full=num , Threshold_empty=num ] 

Remarks

SerialIn | Some chips have multiple HW UARTS. Use the following parameter values: | •| SERIALIN or SERIALIN0 : first UART/UART0  
---|---  
  
•| SERIALIN1 : second UART/UART1  
---|---  
  
•| SERIALIN2 : third UART/UART2  
---|---  
  
•| SERIALIN3 : fourth UART/UART3  
---|---  
  
•| SERIALIN4 : fifth UART/UART4  
---|---  
  
•| SERIALIN5 : sixth UART/UART5  
---|---  
  
•| SERIALIN6 : seventh UART/UART6  
---|---  
  
•| SERIALIN7 : eight UART/UART7  
---|---  
  
Size | A numeric constant that specifies how large the input buffer should be. The space is taken from the SRAM. The maximum is 255.  
BigSize | Instead of using Size you can use BigSize for COM1. It allows to create a bigger buffer than using Size. While Size works with a byte buffer, BigSize works with a word size buffer. It requires more code and does not handle CTS/RTS. For some applications it can be useful to have a big buffer. This is an overloaded version of the code from mcs.lib. You need to include bigbuf.lib using the $LIB directive in your code.   
Bytematch | The ASCII value of the byte that will result in calling a user label. When you specify ALL, the user label will be called for every byte that is received. You must include the label yourself in your code and end it with a return. The following label names must be used when you check for a specific byte value: | •| Serial0CharMatch (for SERIALIN or the first UART/UART0)  
---|---  
  
•| Serial1CharMatch (for SERIALIN1 or the second UART/UART1)  
---|---  
  
•| Serial2CharMatch (for SERIALIN2 or the third UART/UART2)  
---|---  
  
•| Serial3CharMatch (for SERIALIN3 or the fourth UART/UART3)  
---|---  
  
The following label names must be used when you check for any value:

•| Serial0ByteReceived (for SERIALIN or the first UART/UART0)  
---|---  
  
•| Serial1ByteReceived (for SERIALIN1 or the second UART/UART1)  
---|---  
  
•| Serial2ByteReceived (for SERIALIN2 or the third UART/UART2)  
---|---  
  
•| Serial3ByteReceived (for SERIALIN3 or the fourth UART/UART3)  
---|---  
  
When you specify NONE, it is the same as not specifying this optional parameter.  
  
CTS | The pin used for the CTS.(Clear to send). For example PIND.6. This pin will be used in the INPUT mode since it will be connected to the other parties RTS pin.  
RTS | The pin used for RTS. (Ready to send). For example PIND.7 This pin will be used in OUTPUT mode. It is set to 0 to indicate that the other party may send data and it will become 1 to signal to the other party that the buffer is almost full.   
Threshold_full | The number of bytes that will cause RTS to be set to '1'. This is an indication to the sender, that the buffer is full. If your buffer is 100 bytes, you could set it to 80 so after receiving 80 bytes, the RTS pin will change and there are still 20 bytes in the buffer to compensate timing at high baud rates.  
Threshold_empty | The number of free bytes that must be in the buffer before RTS is enabled ( made '0' ) again. If the buffer is 100 bytes, you could set it to 10.  
  
![notice](notice.jpg)The following description is for the normal buffer which uses bytes.

When using the BIGSIZE option instead of SIZE these variables will be of the word type. The mechanism is exactly the same.

The following internal variables will be generated for UART0:

_RS_HEAD_PTR0 , a byte counter that stores the head of the buffer

_RS_TAIL_PTR0 , a byte counter that stores the tail of the buffer.

_RS232INBUF0 , an array of bytes that serves as a ring buffer for the received characters.

_RS_BUFCOUNTR0, a byte that holds the number of bytes that are in the buffer.

For the other UARTS, the variables are named similar. But they do have a different number.

A 1 for the second UART, a 3 for the third UART and a 4 for the fourth UART. Yes, the '2' is skipped.

While you can read and write the internal variables, we advise not to write to them. The variables are updated inside interrupts routines, and just when you write a value to them, an ISR can overwrite the value.

The optional BYTEMATCH can be used to monitor the incoming data bytes and call a label when the specified data is found. This label is a fixed label as mentioned in the table above. The label is called after the data is stored in the buffer. 

This way you can determine the start of a serial stream when you work with a unique header byte. Or you can determine when the data is received into the buffer when you work with a unique trailer byte. 

While bytematch allows you to trap the incoming data bytes, take care that you do not delay the program execution too much. After all the serial input interrupt is used in order not to miss incoming data. When you add delays or code that will delay execution too much you might loose incoming data.

![important](important.jpg)When using the BYTEMATCH option, you must preserve the registers you alter. If you do not know which one, use [PUSHALL](pushall.md) and [POPALL](popall.md).

![important](important.jpg)When using BYTEMATCH and CTS/RTS, do not print data in the bytematch routine to the same UART. This can disturb the communication when the output buffer becomes full.

![notice](notice.jpg)To clear the buffer, use [CLEAR](clear.md) SERIALIN. Do not read and write the internal buffer variables yourself.

CTS-RTS is hardware flow control. Both the sender and receiver need to use CTS-RTS when CTS-RTS is used. When one of the parties does not use CTS-RTS, no communication will be possible.

CTS-RTS requires two additional wires. The receiver must check the CTS pin to see if it may send. The CTS pin is an input pin as the receiver looks at the level that the sender can change.

The receiver can set the RTS pin to indicate to the sender that it can accept data.

In the start condition, RTS is made '0' by the receiver. The sender will then check this logic level with it's CTS pin, and will start to send data. The receiver will store the data into the buffer and when the buffer is almost full, or better said, when the Threshold_full is the same as the number of bytes in the receive buffer, the receiver will make RTS '1' to signal to the sender, that the buffer is full. The sender will stop sending data. And will continue when the RTS is made '0' again.

The receiver can send data to the sender and it will check the CTS pin to see if it may send data.

In order to work with CTS-RTS, you need both a serial input buffer, and a serial output buffer. So use both CONFIG SERIALIN and CONFIG SERIALOUT to specify the buffers.

The CTS-RTS can only be configured with the CONFIG SERIALIN statement.

The thresholds are needed for high baud rates where it will take some time to react on a CTS-RTS.

You need to experiment with the thresholds but good start values are 80% full, and 20% empty.

![notice](notice.jpg)You need to use a pin that is bit addressable. For most chips this is a pin from port A, B, C or D.

![notice](notice.jpg)Some serial devices use the RTS pin as an output pin, while other devices use RTS pin as an input pin to indicate that it need to be connected TO an RTS pin. You always need to have a good look at the data sheet and see in which mode the RTS/CTS pins are used.

In BASCOM RTS is an output pin and CTS is an input pin. 

Additional Infos for XMEGA Devices:

Since buffered serial input and output uses interrupts, you must enable the global interrupts in your code with : ENABLE INTERRUPTS.

```vb
For the XMEGA, if you set the priority with CONFIG PRIORITY, you must enable the MED priority.

If you only use ENABLE INTERRUPTS, the MED priority is enabled automatically. This means you only need to specify MED when you manually configure the priority.

```
Buffer full

So what happens when the buffer is full and a new character arrives and cts/rts are not used?

The byte is still read out and the ERR variable is set. But the data is NOT stored in the buffer. It is lost just as when you would have not used any buffering.

When BYTEMATCH is used, this will still be used/called. 

ASM

Routines called from MCS.LIB :

_GotChar. This is an ISR that gets called when ever a character is received.

When there is no room for the data it will not be stored.

So the buffer must be emptied periodic by reading from the serial port using the normal statements like INKEY() and INPUT.

Since URXC interrupt is used by _GotChar, you can not use this interrupt anymore. Unless you modify the _gotchar routine of course.

See also

[CONFIG SERIALOUT](config_serialout.md) , [ISCHARWAITING](ischarwaiting.md) , [CLEAR](clear.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rs232buffer.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example shows the difference between normal and buffered

' serial INPUT

'micro : Mega161

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m161def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 9600 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'first compile and run this program with the line below remarked

Config Serialin = Buffered , Size = 20

Dim Na As String * 10

'the enabling of interrupts is not needed for the normal serial mode

'So the line below must be remarked to for the first test

Enable Interrupts

Print "Start"

Do

'get a char from the UART

If Ischarwaiting() = 1 Then 'was there a char?

Input Na 

Print Na  'print it

End If

Wait 1 'wait 1 second

Loop

'You will see that when you slowly enter characters in the terminal emulator

'they will be received/displayed.

'When you enter them fast you will see that you loose some chars

'NOW remove the remarks from line 11 and 18

'and compile and program and run again

'This time the chars are received by an interrupt routine and are

'stored in a buffer. This way you will not loose characters providing that

'you empty the buffer

'So when you fast type abcdefg, they will be printed after each other with the

'1 second delay

'Using the CONFIG SERIAL=BUFFERED, SIZE = 10 for example will

'use some SRAM memory

'The following internal variables will be generated :

'_Rs_head_ptr0 BYTE , a pointer to the location of the start of the buffer

'_Rs_tail_ptr0 BYTE , a pointer to the location of tail of the buffer

'_RS232INBUF0 BYTE ARRAY , the actual buffer with the size of SIZE

```
Example2

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M2560 support

'micro : Mega2560

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m2560def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'$timeout = 1000000

'The M128 has an extended UART.

'when CO'NFIG COMx is not used, the default N,8,1 will be used

Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com3 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com4 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Enable Interrupts

Config Serialin = Buffered , Size = 20

Config Serialin1 = Buffered , Size = 20 , Bytematch = 65

Config Serialin2 = Buffered , Size = 20 , Bytematch = 66

Config Serialin3 = Buffered , Size = 20 , Bytematch = All

'Open all UARTS

```
Open "COM2:" For Binary As #2

Open "COM3:" For Binary As #3

Open "COM4:" For Binary As #4

```vb
Print "Hello" 'first uart

Dim B1 As Byte , B2 As Byte , B3 As Byte , B4 As Byte

Dim Tel As Word , Nm As String * 16

'unremark to test second UART

'Input #2 , "Name ?" , Nm

'Print #2 , "Hello " ; Nm

Do

```
Incr Tel

```vb
Print Tel ; " test serial port 1"

Print #2 , Tel ; " test serial port 2"

Print #3 , Tel ; " test serial port 3"

Print #4 , Tel ; " test serial port 4"

```
B1 = Inkey() 'first uart

B2 = Inkey(#2)

B3 = Inkey(#3)

B4 = Inkey(#4)

```vb
If B1 <> 0 Then

Print B1 ; " from port 1"

End If

If B2 <> 0 Then

Print #2 , B2 ; " from port 2"

End If

If B3 <> 0 Then

Print #3 , B3 ; " from port 3"

End If

If B4 <> 0 Then

Print #4 , B4 ; " from port 4"

End If

Waitms 500

Loop

'Label called when UART2 received an A

```
Serial1charmatch:

```vb
Print #2 , "we got an A"

Return

'Label called when UART2 received a B

```
Serial2charmatch:

```vb
Print #3 , "we got a B"

Return

'Label called when UART3 receives a char

```
Serial3bytereceived:

```vb
Print #4 , "we got a char"

Return

End

```
Close #2

Close #3

Close #4

$eeprom

Data 1 , 2

---

## CONFIG SERIALOUT

Action

Configures the hardware UART to use a buffer for output

Syntax

CONFIG SERIALOUT | SERIALOUT1 | SERIALOUT2 | SERIALOUT3 |SERIALOUTx = BUFFERED , SIZE = size

Remarks

SerialOut | Some chips have multiple HW UARTS. Use the following parameter values: | •| SERIALOUT or SERIALOUT0 : first UART/UART0  
---|---  
  
•| SERIALOUT1 : second UART/UART1  
---|---  
  
•| SERIALOUT2 : third UART/UART2  
---|---  
  
•| SERIALOUT3 : fourth UART/UART3  
---|---  
  
•| SERIALOUT4 : fifth UART/UART4  
---|---  
  
•| SERIALOUT5 : sixth UART/UART5  
---|---  
  
•| SERIALOUT6 : seventh UART/UART6  
---|---  
  
•| SERIALOUT7 : eight UART/UART7  
---|---  
  
size | A numeric constant that specifies how large the output buffer should be. The space is taken from the SRAM. The maximum value is 255.  
  
The following internal variables will be used when you use CONFIG SERIALOUT

_RS_HEAD_PTRW0 , byte that stores the head of the buffer

_RS_TAIL_PTRW0 , byte that stores the tail of the buffer

_RS232OUTBUF0, array of bytes for the ring buffer that stores the printed data.

_RS_BUFCOUNTW0, a byte that holds the number of bytes in the buffer.

For the other UARTS, the variables are named similar. But they do have a different number.

A 1 for the second UART, a 3 for the third UART and a 4 for the fourth UART. Yes, the '2' is skipped.

Serial buffered output can be used when you use a low baud rate. It would take relatively much time to print all data without a buffer. When you use a buffer, the data is printed on the background when the micro UART byte buffer is empty. It will get a byte from the buffer then and transmit it.

As with any buffer you have, you must make sure that it is emptied at one moment in time.

You can not keep filling it as it will become full. When you do not empty it, you will have the same situation as without a buffer !!! When the roof is leaking and you put a bucket on the floor and in the morning you empty it, it will work. But when you will go away for a day, the bucket will overflow and the result is that the floor is still wet.

Another important consideration is data loss. When you print a long string of 100 bytes, and there is only room in the buffer for 80 bytes, there is still a wait evolved since after 80 bytes, the code will wait for the buffer to become empty. When the buffer is empty it will continue to print the data. The advantage is that you do not loose any data, the disadvantage is that it blocks program execution just like a normal un-buffered PRINT would do.

Since buffered serial output uses interrupts, you must enable the global interrupts in your code with : ENABLE INTERRUPTS.

For the XMEGA, if you set the priority with CONFIG PRIORITY, you must enable the MED priority.

ASM

Routines called from MCS.LIB :

_CHECKSENDCHAR. This is an ISR that gets called when ever the transmission buffer is empty.

Since UDRE interrupt is used , you can not use this interrupt anymore. Unless you modify the _CheckSendChar routine of course.

When you use the PRINT statement to send data to the serial port, the UDRE interrupt will be enabled. And so the _CheckSendChar routine will send the data from the buffer.

See also

[CONFIG SERIALIN](config_serialin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rs232bufferout.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates how to use a serial output buffer

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 9600 ' use baud rate

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'setup to use a serial output buffer

'and reserve 20 bytes for the buffer

Config Serialout = Buffered , Size = 20

'It is important since UDRE interrupt is used that you enable the interrupts

Enable Interrupts

Print "Hello world"

Print "test1"

Do

Wait 1

'notice that using the UDRE interrupt will slown down execution of waiting loops like waitms

Print "test"

Loop

End

```

---

## CONFIG SERVOS

Action

Configures how much servoâs will be controlled.

Syntax

```vb
CONFIG SERVOS = X , ServoN = Portb.0 , Reload = rl [, INTERVAL=t] 

CONFIG SERVOS = X , ServoN = Portb.0 , MODE=mode , PRESCALE=pre

```
Syntax Xmega

CONFIG SERVOS = X , ServoN = Portb.0 , MODE=mode , TIMER= tmr, PRESCALE=pre

Remarks

Servoâs need a variable pulse in order to operate. The CONFIG SERVOS directive will set up a byte array with the servo pulse width values and will initialize an ISR that uses TIMER0.

X | The number of servoâs you want to control. Each used servo will use one byte of SRAM.  
---|---  
servoN | The port pin the servo is attached too. N represents a value between 1 and 10. When you specify that you will use multiple servo's you need to specify a pin for each servo. Like : config servos=3, servo1=portb.0, servo2=portb.2, servo3=portC.4  
reload | The reload value for the ISR in uS. This is the overflow rate of the timer. So when 100 is used, it means that each 100 uS an interrupt will occur to update the servo variables.  
Interval | The update interval. Using the interval option will result in using alternative servo code optimized for servos.  
Mode | The normal default modes use software PWM with a relatively high frequency. This will give a big processor load since the timer ISR is executed many times. It allows to create create precise pulses in small steps. But when controlling a simple RC servo, it is also possible to use a lower refresh rate which will result in lower processor load.  MODE=SERVO will work for normal AVR and XMEGA. You do not need to specify the interval or reload value.   
Prescale | The prescale value is calculated so that the 8 bit timer interrupt is executed every 2 ms. Inside the interrupt, the servo pin is made high for the value of the servo() array. Then the next time inside the ISR, the pin is set low for the reset of the time. It depends on the processor frequency if you get a good range. In the report you can find the used prescale value as a constant named _SERVO_PRESCALER. When you do not get a full servo swing, you might want to try a higher prescale value. The prescale parameter overrides the automatic calculation.  
Timer | This is for XMEGA only. Specify the name of the timer that will be used in interrupt mode.  
  
PWM MODE

When you use for example :

Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10

The internal ISR will execute every 10 uS.

An arrays named SERVO() will be created and it can hold 2 bytes : servo(1) and servo(2).

By setting the value of the servo() array you control how long the positive pulse will last. After it has reached this value it will be reset to 0.

The reload value should be set to 10. After 20 mS, a new pulse will be generated.

You can use other reload values but it will also mean that the repeat value will change.

The PORT pins specified must be set to work as an output pin by the user.

CONFIG PINB.0 = OUTPUT

Will set a pin to output mode.

The CONFIG SERVOS only works with servo's that rotate 180 degrees. These are the servo's found in RC models.

There are also continuous rotation servos which work different. The servo code will NOT work on these servos.

Alternative Servocode

When using the INTERVAL option, you can use alternative code which is optimized for servo's.(this is however not the MODE=SERVO)

You should use a RELOAD value of 100 in that case and an interval of 100 should be used for best results.

Using a reload of 100 uS will give more time to the main application. This does give lower resolution but this is not a problem for most model servos. With an interval of 100, the refresh will be done in 100x100 us which results in 10 mS.

The following test code was used:

Config Servos = 2 , Servo1 = Portd.7 , Servo2 = Portb.1 , Reload = 100 , Interval = 100

Servo(1) = 10

Servo(2) = 5

```vb
Enable Interrupts

Do

For J = 8 To 16

```
Servo(1) = J

```vb
Waitms 5000 ' some time to check if the servo is stable

Next

Waitms 5000

Loop

```
SERVO mode

The MODE=SERVO can be used for normal AVR and XMEGA. It results in a lower processor load.

XMEGA

The Xmega has several timers. You must specify the timer to be used. 

The Xmega has 16 bit timers and instead of a byte array, a word array is created for the servo values.

The Xmega can also create pulses with it's timers without the need of interrupts. But this mode demands that you use fixed CCx pins. The software servo pulse mode, allows you to chose any pin.

Resources used

TIMER0 is used to create the ISR. Xmega will use TCxx.

NOTE

The servo() value is not absolute. It will depend on the processor clock. This means that these values might need an adjustment when you alter the $crystal value.

Example PWM mode

```vb
'-----------------------------------------------------------------------------------------

'name : servos.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates the SERVO option

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'Servo's need a pulse in order to operate

'with the config statement CONFIG SERVOS we can specify how many servo's we

'will use and which port pins are used

'A maximum of 14 servos might be used

'The SERVO statements use one byte for an interrupt counter and the TIMER0

'This means that you can not use TIMER0 anymore

'The reload value specifies the interval of the timer in uS

'Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10

Config Servos = 1 , Servo1 = Portb.0 , Reload = 10

'as an option you can use TIMER1

'Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10 , Timer = Timer1

'we use 2 servos with 10 uS resolution(steps)

'we must configure the port pins used to act as output

Config Portb = Output

'finally we must turn on the global interrupt

Enable Interrupts

'the servo() array is created automatic. You can used it to set the

'time the servo must be on

```
Servo(1) = 10 '10 times 10 = 100 uS on

```vb
'Servo(2) = 20 '20 times 10 = 200 uS on

Do

Loop

Dim I As Byte

Do

For I = 0 To 100

```
Servo(1) = I

```vb
Waitms 1000

Next

For I = 100 To 0 Step -1

' Servo(1) = I

Waitms 1000

Next

Loop

End

```
Example SERVO mode

```vb
'-----------------------------------------------------------------------------------  
' (c) 1995-2025, MCS Electronics  
' servos-timer0.bas  
'-----------------------------------------------------------------------------------  
$regfile = "m88def.dat"  
$crystal = 8000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
  
  
Config Com1 = 19200 , Parity = None , Stopbits = 1 , Databits = 8  
Print "Servo test"  
  
Config Servos = 2 , Mode = Servo , Servo1 = Portb.0 , Servo2 = Portb.1  
'Config Servos = 2 , Mode = Servo , Servo1 = Portb.0 , Servo2 = Portb.1 , Prescale= 256  
  
' you need to chose SERVO mode for lowest system resources  
Enable Interrupts ' you must enable interrupts since timer 0 is used in interrupt mode  
  
  
Dim Key As Byte  
'notice that servo() array is a byte array, which is created automatic  
  
Do  
```
Key = Inkey() ' get data from serial port  
If Key = "l" Then 'left  
Servo(1) = 100  
Servo(2) = 100  
Elseif Key = "m" Then ' middle  
Servo(1) = 170  
Servo(2) = 170  
Elseif Key = "r" Then ' right  
Servo(1) = 255  
Servo(2) = 255  
Elseif Key <> 0 Then ' enter user value  
Input "Servo1 " , Servo(1)  
Servo(2) = Servo(1)  
```vb
End If  
Loop

```
Example XMEGA SERVO mode

```vb
'-----------------------------------------------------------------------------------  
' (c) 1995-2025, MCS Electronics  
' xmega-servo.bas  
'-----------------------------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Print "Servo test"  
  
Config Servos = 2 , Mode = Servo , Timer = Tcc0 , Servo1 = Portb.0 , Servo2 = Portb.1  
' you need to chose SERVO mode and you must provide the name of the timer that will be used for the system tick  
Enable Interrupts ' you must enable interrupts since timer TCC0 is used in interrupt mode  
  
  
Dim Key As Byte  
'notice that servo() array is a word array, which is created automatic  
  
Do  
```
Key = Inkey() ' get data from serial port  
If Key = "l" Then 'left  
Servo(1) = 12800  
Servo(2) = 12800  
Elseif Key = "m" Then ' middle  
Servo(1) = 19200  
Servo(2) = 19200  
Elseif Key = "r" Then ' right  
Servo(1) = 40000  
Servo(2) = 40000  
Elseif Key <> 0 Then ' enter user value  
Input "Servo1 " , Servo(1)  
Servo(2) = Servo(1)  
```vb
End If  
Loop

```

---

## CONFIG SHIFTIN

Action

Instruct the compiler to use new behaviour of the SHIFTIN statement.

Syntax

CONFIG SHIFTIN = value

Remarks

value | This must be COMPATIBLE or NEW. By default the old behaviour is used. So in order to use the new behaviour you must use : CONFIG SHIFTIN=NEW  
---|---  
  
The SHIFTOUT has been enhanced with a number of options which make it incompatible to the old SHIFTOUT.

In order to maintain compatibility with your old code, this option has been added so you have control over which SHIFTIN version is used.

See also

[SHIFTIN](shiftin.md)

---

## CONFIG SINGLE

Action

Instruct the compiler to use an alternative conversion routine for representation of a single.

Syntax

CONFIG SINGLE = SCIENTIFIC , DIGITS = value

Remarks

Single | SCIENTIFIC for scientific notation. Use NORMAL for the normal default notation. Using both modes will increase your code size.  
---|---  
Digits | A numeric constant with a value between 0 and 7. A value of 0 will result in no trailing zero's. A value between 1-7 can be used to specify the number of digits behind the comma.  
  
When a conversion is performed from numeric single variable, to a string, for example when you PRINT a single, or when you use the STR() function to convert a single into a string, a special conversion routine is used that will convert into human readable output. You will get an output of digits and a decimal point.

This is well suited for showing the value on an LCD display. But there is a downside also. The routine is limited in the way that it can not shown very big or very small numbers correct.

The CONFIG SINGLE will instruct the compiler to use a special version of the conversion routine. This version will use scientific notation such as : 12e3.

You can specify how many digits you want to be included after the decimal point.

It is possible to switch between notations by using multiple CONFIG SINGLE statements. As soon at the compiler encounters a CONFIG SINGLE, it will change to output to the selected format. You should not use CONFIG SINGLE inside a sub/function since this is not a dynamic feature that can be changed at run time.

See also

[FUSING](fusing.md), [STR](str.md)

ASM

Uses single.lbx library

Example

```vb
'----------------------------------------------------------------

' (c) 1995-2025, MCS

' single_scientific.bas

' demonstation of scientific , single output

'----------------------------------------------------------------

$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

'you can view the difference by compiling and simulating this sample with the

'line below remarked and active

Config Single = Scientific , Digits = 7

Dim S As Single

```
S = 1

Do

S = S / 10

```vb
Print S

Loop

```

---

## CONFIG SPI

Action

Configures the SPI mode and pins.

Syntax for software SPI

CONFIG SPI|SPISOFT = SOFT, DIN = PIN, DOUT = PIN , SS = PIN|NONE, CLOCK = PIN , SPIIN=value , MODE=mode, SPEED=speed, SETUP=setup , EXTENDED=ext

Syntax for hardware SPI

CONFIG SPI|SPIHARD = HARD, INTERRUPT=ON|OFF, DATA_ORDER = LSB|MSB , MASTER = YES|NO , POLARITY = HIGH|LOW , PHASE = 0|1, CLOCKRATE = 4|16|64|128 , NOSS=1|0 , SPIIN=value , EXTENDED=ext

Syntax for hardware SPI1

CONFIG SPI1 = HARD, INTERRUPT=ON|OFF, DATA_ORDER = LSB|MSB , MASTER = YES|NO , POLARITY = HIGH|LOW , PHASE = 0|1, CLOCKRATE = 4|16|64|128 , NOSS=1|0 , SPIIN=value

When you just want to use one SPI slave chip using the HW SPI, use this : Config Spi = Hard , Interrupt = Off , Data_Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 128

When you want more details, read more about the details and options below.

Remarks software SPI

SPI | SOFT for software emulation of SPI, this allows you to choose the pins to use. Only works in master mode. HARD for the internal SPI hardware, that will use fixed pins of the microprocessor.  
---|---  
DIN | Data input or MISO. Pin is the pin number to use such as PINB.0  
DOUT | Data output or MOSI. Pin is the pin number to use such as PORTB.1  
SS | Slave Select. Pin is the pin number to use such as PORTB.2 Use NONE when you do not want the SS signal to be generated. See remarks. Or as an alternative you can use : NOSS=1.  
CLOCK | Clock. Pin is the pin number to use such as PORTB.3  
DATA ORDER | Selects if MSB or LSB is transferred first. For soft SPI you need to use the MODE option as well. Otherwise only MSB order is available.  
MASTER | Selects if the SPI is run in master or slave mode.  
SPIIN | When reading from the SPI slave, it should not matter what kind of data you send. But some chips require a value of 255 while others require a value of 0. By default, when the SPIIN option is not provided, a value of 0 will be sent to the SPI slave. With this SPIIN option you can override this value.   
MODE | A constant in the range from 0-3 which defines the SPI MODE. Without MODE, the default mode 1 will be used. Also, when using MODE, new SPI code will be used.  When using MODE, you can also specify SPEED and SETUP. MODE is for Software SPI only ! | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 | Rising, Sample | Falling, Setup  
1 | Rising, Setup | Falling, Sample  
2 | Falling, Sample | Rising, Setup  
3 | Falling, Setup | Rising, Sample  
  
SPEED | Is a numeric constant for an optional delay. This delay is in us. When you specify 1, it will result in 2 us delay : 1 us before and 1 us after the clock. By default there is no delay. Only slow slave chips might require a delay.  SPEED only applies when MODE is specified.  
SETUP | Setup is the delay in uS before sampling the MISO pin. A numeric constant must be used. SETUP is for Software SPI only and when MODE is used !  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes.  
  
Software SPI allows you to chose the processor pins for the SPI operation. Typically you need a MISO, MOSI, CLOCK and SS pin.

While this is an advantage, the disadvantage is that software SPI uses more processor resources.

In software spi mode the [SPIINIT](spiinit.md) statement will set the SPI pins to the proper logic level. For example to :

sbi PORTB,5 ;set latch bit hi (inactive)SS

sbi DDRB,5 ;make it an output SS

cbi PORTB,4 ;set clk line lo

sbi DDRB,4 ;make it an output

cbi PORTB,6 ;set data-out lo MOSI

sbi DDRB,6 ;make it an output MOSI

cbi DDRB,7 ;MISO input

Ret

This is just an example. The actual code differs from processor to processor. And also depends on the used port pins. 

In most cases, there is just one slave chip to control/address. In such a case you need only one slave select(SS) pin to control this chip. But SPI can also be used to control multiple SPI slaves.

These slaves need to use the same mode. You can not dynamically change the SPI mode at run time. 

BASCOM will automatically set the SS pin to logic level 0 when you use a SPI command. And when the SPI command has executed, it will set the SS pin back to a logic 1. 

When the slave chip has in inverted SS pin (it requires a 1 to be active) you can not use this automatic SS signal generation.

When you want to address multiple slaves with the software SPI you need multiple pins to select the different slave chips. In this case you also can not use the automatic SS signal generation.

The solution is to specify NONE for SS. This will eliminate the automatic SS signal generation. But it also means that you as a user need to handle this. In practice this means :

\- choose a port pin to serve as SS pin

\- set it to output and to the right logic level (1 in most cases to disable the slave)

\- before using a SPI statement, select the slave by making SS logic 0.

\- after the SPI statement, set the SS logic level back to 1.

Example user controlled SS pin.

Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = NONE , Clock = Portb.3  
MySS alias portb.2  
```vb
Config MySS=OUTPUT : MySS=1 ' deactivate  
Dim var As Byte  
```
SPIINIT ' Init SPI state and pins.  
MySS=0 ' select SS  
SPIOUT var , 1 ' send 1 byte  
MySS=1 ' deselect SS

Remarks Hardware SPI

SPI | SOFT for software emulation of SPI, this allows you to choose the pins to use. Only works in master mode. HARD for the internal SPI hardware, that will use fixed pins of the microprocessor.  
---|---  
DATA_ORDER | Selects if MSB or LSB is transferred first.  
MASTER | Selects if the SPI is run in master or slave mode.  
POLARITY | Select HIGH to make the CLOCK line high while the SPI is idle. LOW will make clock LOW while idle.  
PHASE | Refer to a data sheet to learn about the different settings in combination with polarity.  
CLOCKRATE | The clock rate selects the division of the of the oscillator frequency that serves as the SPI clock. So with 4 you will have a clock rate of 4.000000 / 4 = 1 MHz , when a 4 MHZ XTAL is used.  
NOSS | 1 or 0. Use 1 when you do not want the SS signal to be automatically generated in master mode.   
INTERRUPT | Specify ON or OFF. ON will enable the SPI interrupts to occur. While OFF disables SPI interrupts. ENABLE SPI and DISABLE SPI will accomplish the same.  
SPIIN | When reading from the SPI slave, it should not matter what kind of data you send. But some chips require a value of 255 while others require a value of 0. By default, when the SPIIN option is not provided, a value of 0 will be sent to the SPI slave. With this SPIIN option you can override this value.   
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes.  
  
Hardware SPI is the best option when it is available. Hardware SPI can be used in master and slave mode. All BASCOM SPI statements are master mode routines.

The only disadvantage is that you must use the dedicated hardware pins, the SS pin included!

When you use CONFIG SPI = HARD without any other parameter, the SPI will only be enabled. It will work in slave mode then with CPOL =0 and CPH=0.

In hardware spi mode the [SPIINIT](spiinit.md) statement will set the SPI pins to :

SCK = Ouput

MISO = Input

MOSI = Output 

In Master mode, the SS pin will be set to output too.

As explained for Software SPI, it is not always desirable to use the SS pin to control the SPI slave chip. Because you want to use a different pin, use multiple slave, or the slaves has an inverted SS signal.

Since the hardware SPI always has an SS pin, there is an override for this with a different name than for soft spi : NOSS=0|1

So where SS=NONE is used for SOFT SPI to disable automatic SPI signal generation, the HARDWARE SPI use the option NOSS=1 to do the same. NOSS means NO SS signal generation.

When NOSS is not used or NOSS=0, the default will be used where the dedicated SS pin will create the slave select signals.

One big difference with software SPI, is that in order to use the SPI in master mode, the SS pin must be set to output mode. Even if you do not use the dedicated SS pin to control a SPI slave chip !

When the SS pin is in input mode, a logic 0 at the input will turn the master mode into slave mode. A pull up resistor could do the same but our advise : use the SS pin as an output pin.

The SS pin is set to output mode when the MASTER mode is selected. So even if NOSS=1, the SS pin is set to output mode when MASTER=YES.

![notice](notice.jpg)When using NOSS=1 : In order to use the Hardware SPI in master mode, you need to set the SS pin to output. In input mode, this pin can be used to set the SPI bus into slave mode. You only need to set the pin to output when you use the NOSS=1 option. With NOSS=0, the compiler will set the SS pin to output and makes SS pin logic 1.

When NOSS=1 is used, the SS pin is only made an output pin in MASTER mode. No logic level is set when NOSS=1.

This table show how SS pin is set with the various options for HW mode.

MODE | NOSS | SS PIN  
---|---|---  
MASTER | 0 | output, logic 1  
  
| 1 | output, logic level unchanged  
SLAVE | 0 | input  
  
| 1 | input  
  
All SPI routines are SPI-master routines. In the samples directory you will also find a SPI hardware master and SPI hardware slave sample.

The SPI protocol is explained in the chapter : [Using the SPI protocol](using_the_spi_protocol.md)

![notice](notice.jpg)When using a processor for both the master and slave : Take in mind that the SPI master processor clock frequency must be 1/4 of the SPI slave processor frequency. 

Chips with 2 full SPI ports

Some new processors like the ATMEGA328PB have 2 SPI ports. In order to use this second SPI port you have to add a '1' to the statement. 

CONFIG SPI1

SPI1IN

SPI1OUT

SPI1INIT

SPI1MOVE

See also

[SPIIN](spiin.md) , [SPIOUT](spiout.md) , [SPIINIT](spiinit.md) , [SPI](using_the_spi_protocol.md) , [SPIMOVE](spimove.md)

Example for Software SPI

```vb
Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = Portb.2 , Clock = Portb.3  
Dim var As Byte  
```
SPIINIT 'Init SPI state and pins.  
SPIOUT var , 1 'send 1 byte

Example for Hardware SPI, 1 slave

Config Spi = Hard, Interrupt = Off, Data_Order = Msb, Master = Yes, Polarity = High, Phase = 1, Clockrate = 4, Noss = 0

Spiinit

---

## CONFIG SPIx XMEGA

Action

Configures the SPI mode of the Xmega.

Syntax

CONFIG SPIx = HARD, MASTER = YES|NO , MODE=0-3, CLOCKDIV=div, DATA_ORDER = LSB|MSB , EXTENDED=0|1

Remarks

SPIx | There are 4 SPI interfaces on the Xmega. You need to specify SPIC, SPID, SPIE or SPIF for SPIx. The value must be HARD.  
---|---  
MASTER | Selects if the SPI is running in master or slave mode. Possible values : YES(1), NO(0).  
MODE | The mode of the SPI interface. There are 4 modes in the range from 0-3. The mode decides weather the first edge in a clock cycles is rising or falling, and if data setup and sample is on leading or trailing edge. | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 CPOL=0, CPHA=0 | Rising, Sample | Falling, Setup  
1 CPOL=0, CPHA=1 | Rising, Setup | Falling, Sample  
2 CPOL=1, CPHA=0 | Falling, Sample | Rising, Setup  
3 CPOL=1, CPHA=1 | Falling, Setup | Rising, Sample  
  
CLOCKDIV | The SPI is clocked by the system clock which is divided by a the SPI divider. If you select a division factor of 4, and the system clock is 4 MHz, then the SPI clock will be 1 MHz. The possible values are : CLK2, CLK4, CLK8, CLK16, CLK32, CLK64 and CLK128. Some modes use the internal CLK2X bit. In SLAVE mode, the maximum clock rate is CLK4.  
DATA ORDER | Selects if MSB or LSB is transferred first. The SPI can send the Least Significant bit (LSB) or the Most Significant Bit(MSB) first.   
SS | Slave select option. The possible values are : \- NONE, the SS will not be set or used \- AUTO, the dedicated pin is used, this is portC.4 for SPIC, portD.4 for SPID, portE.4 for SPIE and portF.4 for SPIF.  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes. When defined for one SPI interface like SPIC, it will also work for all other SPI interfaces like SPID, SPIE and SPIF.  
  
The SPI settings for the Xmega differ from the SPI settings for normal AVR chips.

In order to be able to use the four different SPI interfaces the Xmega uses a channel which you need to OPEN.

After you have opened the device, you can send/receive data using PRINT and INPUT.

There are 2 manuals available from ATMEL for every ATXMEGA Chip

1.| One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual  
---|---  
  
2.| Another Manual for the single chips like for example for an ATXMEGA128A1 it is the ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the Alternate Pin Functions. So you can find which Pin MISO, MOSI etc.  
---|---  
  
The SS pin, MOSI and CLOCK pins are set to output mode automatic in master mode.

The SS pin is also made high. The SS pin is only configured when you have selected SS=AUTO.

![notice](notice.jpg)If you need to use a different pin for SS or when you need to switch the logic level yourself for SS, and thus you use the SS=NONE option, you must setup the SS pin, even if you do not use it yourself. You must prevent that the SS pin will be made low in input mode since that will set the SPI into SLAVE mode, even while it was in MASTER mode. 

When SS is in auto mode, the SS pin will be made low before each SPI transfer and be made high when the SPI transfer is finished. SS can be used when multiple slaves are used, or to synchronize data packets.

![notice](notice.jpg)The pins are configured before the SPI control register is set. If you do not use the AUTO mode, you must set the pin direction and state yourself before using the CONFIG SPI. The following table shows which pins you have to set when NOT using the AUTO mode.

Pin | Master Mode | Slave Mode  
---|---|---  
MOSI | User set | Input  
MISO | Input | User set  
SCK | User set | Input  
SS | User set | Input  
  
It is very important that you set the pin direction and level BEFORE you use the CONFIG SPI statement. This because the CONFIG SPI will enable the SPI interface and once enabled you can not change data direction/level.

If you want to change pin levels , you must disable the SPI interface first by clearing bit 6 :

Spid_ctrl.6 = 0 ' disable

```vb
Config Portd.4 = Output ' set direction

Set Portd.0.4 ' set level

```
Spid_ctrl.6 = 1 ' enable 

See also

[INPUT](input.md), [PRINT](print.md), [OPEN](open.md)

[SPIIN](spiin.md) , [SPIOUT](spiout.md) , [SPIINIT](spiinit.md) , [SPI](using_the_spi_protocol.md) , [SPIMOVE](spimove.md)

Example

Dim Bspivar As Byte , Ar(4) As Byte , W As Word

Bspivar = 1

```vb
Config Spic = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk2 , Data_order = Msb

Config Spid = Hard , Master = Yes , Mode = 1 , Clockdiv = Clk8 , Data_order = Lsb

Config Spie = Hard , Master = Yes , Mode = 2 , Clockdiv = Clk4 , Data_order = Msb

Config Spif = Hard , Master = Yes , Mode = 3 , Clockdiv = Clk32 , Data_order = Msb

```
Open "SPIC" For Binary As #10

Open "SPID" For Binary As #11

Open "SPIE" For Binary As #12

Open "SPIF" For Binary As #13

Open "SPI" For Binary As #bspivar ' use a dynamic channel

```vb
'SPI channel only suppor PRINT and INPUT

Print #10 , "to spi" ; W

Input #10 , Ar(1) , W

Print #bspivar , W

Input #bspivar , W

```

---

## CONFIG SPIx XTINY

Action

Configures the SPI mode of the Xtiny.

Syntax

CONFIG SPIx = HARD, MASTER = YES|NO , MODE=0-3, CLOCKDIV=div, DATA_ORDER = LSB|MSB , EXTENDED=0|1 , SPIPIN=pins

Remarks

SPIx | There is 1 SPI interfaces on the Xtiny. You need to specify SPI0. The DB series has 2 SPI interfaces. You can use the second interface with SPI1. The only supported option is HARD for hardware mode.  
---|---  
MASTER | Selects if the SPI is running in master or slave mode. Possible values : YES(1), NO(0).  
MODE | The mode of the SPI interface. There are 4 modes in the range from 0-3. The mode decides weather the first edge in a clock cycles is rising or falling, and if data setup and sample is on leading or trailing edge. | Mode | Leading Edge | Trailing Edge  
---|---|---  
0 | Rising, Sample | Falling, Setup  
1 | Rising, Setup | Falling, Sample  
2 | Falling, Sample | Rising, Setup  
3 | Falling, Setup | Rising, Sample  
  
CLOCKDIV | The SPI is clocked by the system clock which is divided by a the SPI divider. If you select a division factor of 4, and the system clock is 4 MHz, then the SPI clock will be 1 MHz. The possible values are : CLK2, CLK4, CLK8, CLK16, CLK32, CLK64 and CLK128. Some modes use the internal CLK2X bit. In SLAVE mode, the maximum clock rate is CLK4.  
DATA_ORDER | Selects if MSB or LSB is transferred first. The SPI can send the Least Significant bit (LSB) or the Most Significant Bit(MSB) first.   
SS | Slave select option. The possible values are : \- NONE, the SS will not be set or used \- AUTO, the dedicated pin is used, the pin depends on the used processor.  
EXTENDED | An optional parameter to extend the maximum data read/write size. A value of 0 is default and will cause the SPIIN, SPIIOUT, SPIMOVE routines to handle a maximum data size of 255 bytes.   
A value of 1 will extended the data size from bytes to words which means you can move data of 65535 bytes. When defined for one SPI interface like SPI0, it will also work for all other SPI interfaces like SPI1, SPI2 and SPI3.  
SPIPIN | This option allows to select the alternative pin locations. The default option is always the first listed. When you use the default option there is no need to specify it with SPIPIN. The MOSI, CLOCK and SS pin will be set to output mode. The SS pin will only be set to output mode when you use the SS=AUTO option. Otherwise you need to set the pin you use yourself to output mode. When you select the NONE option which means that the SPI is not connected to any of the port pins, no pins will be initialized to output. The mx4809 for example has these options : DEF_PA4567,ALT1_PC0123,ALT2_PE0123,NONE The first listed is DEF_PA4567 which means that this is the default location when you do not use the PORTMUX. PA means port A. And the pins are listed in MOSI,MISO,CLOCK,SS order. Thus PORTA.4 is connected to MOSI, PA.5 to MISO, etc. When you select ALT1_PC0123 it means that you select the alternative pin location 1. This will use PORTC0-3.  And the NONE option means that none of the SPI pins are connected.  The compiler will set the proper port direction and levels. It will also configure the PORTMUX in case the SPIPIN option is used. So when you use the default location, do not use SPIPIN in order to get less code.  
  
The SPI settings for the Xtiny differs only for the hardware name : SPI0 instead of SPI.

SPIINIT is not required for Xtiny. The pins are initialized as part of the CONFIG statement.

SPIINIT is ignored for Xtiny.

![notice](notice.jpg)If you need to use a different pin for SS or when you need to switch the logic level yourself for SS, and thus you use the SS=NONE option, you must setup the SS pin, even if you do not use it yourself. You must prevent that the SS pin will be made low in input mode since that will set the SPI into SLAVE mode, even while it was in MASTER mode. 

When SS is in auto mode, the SS pin will be made low before each SPI transfer and be made high when the SPI transfer is finished. SS can be used when multiple slaves are used, or to synchronize data packets.

![notice](notice.jpg)The pins are configured before the SPI control register is set. If you do not use the AUTO mode, you must set the pin direction and state yourself before using the CONFIG SPI. The following table shows which pins you have to set when NOT using the AUTO mode.

Pin | Master Mode | Slave Mode  
---|---|---  
MOSI | User set | Input  
MISO | Input | User set  
SCK | User set | Input  
SS | User set | Input  
  
It is very important that you set the pin direction and level BEFORE you use the CONFIG SPI statement. This because the CONFIG SPI will enable the SPI interface and once enabled you can not change data direction/level.

See Also

[SPIOUT](spiout.md), [SPIIN](spiin.md), [SPIMOVE](spimove.md) , SPI1OUT, SPI1IN, SPI1MOVE 

Example

```vb
'--------------------------------------------------------------------------------  
'name : spi.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates SPI  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'configure the SPI to master mode  
Config Spi0 = Hard , Clockdiv = Clk32 , Data_order = Msb , Mode = 0 , Master = Yes , Ss = Auto  
  
  
'dimension a variable  
Dim B As Word  
```
B = &B1010_1010  
  
Print "Test SPI"  
Spiinit 'initialize SPI is not required for Xtiny  
  
  
Do  
Spiout B , 1 'send some data  
```vb
Waitms 1000  
Loop  
  
End

```

---

## CONFIG STRCHECK

Action

Configures string check

Syntax

CONFIG STRCHECK = ON|OFF

Remarks

By default the string check is OFF. You can turn it on for additional string overwrite checking.

Why is it a problem to overwrite a string? A string is in fact a series of bytes that end with a null byte. For this reason a string always uses one more byte than it can store.

DIM S As string * 4 , can hold 4 characters. The internal size is 5 bytes. The extra byte could store the size too, but the advantage of using 0 strings is that you can DIM a large string say 1000 bytes, and still need 1 byte to mark the end. And as always there is a disadvantage too : you can not store a character with a 0 value since it marks the end. 

Consider code like this : 

Dim S as String * 4, b as byte, Z as string * 10 

The data is stored after each other. When you write a too long string to S, you will overwrite the variable B since it is allocated after the string S.

In some cases the compiler can check if you overwrite a string. For example when you assign a constant to a string that is too small to hold the content.

You always get an error in such a case. For example : S = "abcd" is ok, but S="abcdE" will give an error.

The problem is when you use another string to assign a string. Code like this :

Z="abcdefg" : S = Z 

This will overwrite B.

For this purpose the CONFIG STRCHECK=ON can be used.

It will use an alternative piece of code that will check against overwriting. 

When a string will not fit, only the part that will fit will be assigned. 

So this option can give unexpected results as well. But at least no other data will be overwritten.

As the example will show it is still not always possible to guard against overwriting of strings.

Example

```vb
'--------------------------------------------------------------------------------  
'name : string-check.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates string overwrite protection  
'micro : avrDA28  
'suited for demo : no  
'commercial addon needed : yes but change the DAT file to test with any other micro  
'--------------------------------------------------------------------------------  
$regfile = "avrx128da28.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
'$bigstrings  
  
```
Const Cigoneerror = 1 'make 1 to compile without errors  
Const Cstrcheck = 1 'check strings for overwrite  
Const Cspeclen = 1 'specify length for better checking  
  
```vb
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1 'select system clock and frequency  
  
Config Osc = Enabled, FREQUENCY=24MHZ  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  

#if Cstrcheck  
Config Strcheck = On 'when ON there will be a check so memory is not overwritten. it will create slightly mode code since  
'the size must be passed and checked  

#endif  
Dim Bdummy As Byte 'Xtiny and Xmega auto create internal variables after the first DIM  
dim idx as byte 'index for array  
dim sTarget as string * 10 'this is a string we are going to assign  
Dim Bbeyond As Byte 'put a byte here  
dim sSource as string * 20 'this is the source string  
dim sAr(5) as string * 10 'test an array as well  
  
```
Const Csomestring10 = "0123456789" ' a test constant  
Const Csomestring11 = Csomestring10 + "A" ' and one string 1 byte longer  
Const Csomestring20 = "0123456789abcdefghij" ' a test constant  
```vb
'by default there is no protection against string overwrites. This is because the first processors had little RAM.  
'using large strings on them was not possible. A string is just an array of bytes with a zero byte at the end.  
'for this reason a string can not hold a 0 value.  
'A string always takes 1 more byte in memory than the length of the actual string  
'The length info is not stored inside the string. This has pros and cons. The pro is that you can DIM a string longer than 255 bytes and it will  
'still work. The con is that when you pass strings to sub routines and functions, the maximum length is not passed a long. So there is no check possible.  
  
'first assigna value to bBeyond which is located after the string we assign  
```
Bbeyond = 123 ' the idea is that this remains 123  
  
'There can be a number of problems.  
Starget = Csomestring10 ' this should be fine  

#if Cigoneerror = 0  
Starget = Csomestring11 'here you get an error 119 since you assign a constant with a known length that is too long to fit  

#ENDIF  
  
Ssource = Csomestring11 ' this is no problem since it will fit  
Starget = "a" + Starget ' this is a problem since this will write beyond the string  
  
print bBeyond  
Bbeyond = 123 'the idea is that this remains 123  
  
'--- array test ---  
sAr(2)="0123456789" 'create a string and check if it is not overwritten  
Idx = 1 : Sar(idx) = "ABC" : Sar(idx) = Sar(idx) + Csomestring10 'lets check if it works for arrays as well  
print bBeyond  
Bbeyond = 123 'the idea is that this remains 123  
  

```vb
#if Cspeclen  
declare sub somesub(byval s1 as string * 10,s2 as string * 10)  

#else  
Declare Sub Somesub(byval S1 As String , S2 As String)  

#endif  
declare function myfunc() as string  
  
```
sSource= csomestring11  
Somesub Ssource , Ssource  
```vb
'somesub csomestring11 ,sSource 'will create error in case length is specified  
print bBeyond  
  
```
sTarget=Myfunc()  
print bBeyond  
  
sSource= csomestring20  
Idx = 15 : Starget = Left(ssource , Idx) 'check this too  
  
```vb
end  
  
's1 passed by value, s2 by reference  

#if cSpecLen  
sub somesub(byval s1 as string * 10,s2 as string * 10)  

#else  
sub somesub(byval s1 as string,s2 as string)  

#endif  
```
local test as byte  
test=123  
  
sTarget=s1  
print bBeyond  
bBeyond=123 'the idea is that this remains 123  
  
starget=s2  
print bBeyond  
  
s1="aa"  
s1=s1+csomestring10  
```vb
'when you watch the local test value you will see it is overwritten.  
'so here is a potential problem too  
end sub  
  
  
function myfunc() as string  

#IF cIgoneError=0  
```
myfunc = csomestring11 'this will give an error  

#endif  
myfunc= "a" 'this will work  
myfunc=myfunc + csomestring10 'but here we have a problem !!!  
```vb
'despite the test enabled, we can not know the actual size since  
'this means that when you assign a string with a user string function you need to be careful  
end function

```

---

## CONFIG SUBMODE

Action

This option sets how the compiler deals with Subs, Functions and Declarations.

Syntax

CONFIG SUBMODE = NEW|OLD

Remarks

When the SUBMODE option is not configured, the default 'OLD' will be used.

This is the old mode used in versions up to 2070.

This old mode demands that you DECLARE a function or sub, before you call/use it.

It also binds in the sub/function at the same location as in your code.

When working with $include files, this requires that you insert an $include file with the SUBS/FUNCTIONS at the end of your code, and that you insert an $include file with the DECLARE statements at the start of your code.

Or you can put the DECLARE and actual implementation in one file and use a GOTO to jump over the Sub/Function code.

```vb
For example consider this code :

print "code here"

Sub test()

print

End Sub

```
When using the OLD method, this will give problems since the code will run into the Sub test, without it actual being called.

We can solve that like this by placing the sub/functions after the END statement:

```vb
print "code here"

END

Sub test()

print

End Sub

```
or we can use a GOTO:

```vb
print "code here"

GOTO skip

Sub test()

print

End Sub

```
skip:

print "more code here"

When you use CONFIG SUBMODE=NEW, most behaviour is changed :

\- there is no need to DECLARE a sub/function before you call it. But, the actual sub/function code must be placed before the actual call!

\- only the used sub/functions are included

\- the compiled sub/function code is placed after the main program. this is something you do not need to worry about.

\- you can $include the modules without a GOTO to jump over the code because code is stored automatically after the END statement.

\- sub/functions behave like macro's : only when used they are included

\- Any Dead code or Un-used code will not be Compiled!

This means you can $Include a file with all your collection of Sub or Functions and the Compiler will determine which items are to be used during Compilation saving you unnecessary wastage of Flash space.

See also

[DECLARE SUB](declare_sub.md), [SUB](sub.md), [DECLARE FUNCTION](declare_function.md) , [CALL](call.md)

Example

  
```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
config submode=new  
  
declare sub test1() ' not required  
  
sub test2() ' this sub is not used and will not be compiled  
print "test2"  
end sub  
  
function myfunc() as byte ' called from test1  
```
myfunc = 1  
```vb
end function  
  
sub test1()  
print "test1"  
print myfunc() ' uses myfunc  
end sub  
  
print "test"  
```
test1 ' call test1  
end '12

---

## CONFIG SYSCLOCK XMEGA

Action

Selects the oscillator source for the system clock.

See also [ATXMEGA](atxmega.md)

Syntax

CONFIG SYSCLOCK=sysclock , PRESCALEA=prescaleA,  PRESCALEBC=prescaleBC

Remarks

SYSCLOCK | The oscillator used for generation of the system clock. This oscillator must be running. You MUST use CONFIG OSC before you use CONFIG SYSCLOCK. The CONFIG SYSCLOCK will wait till the oscillator is running stable. Possible values: \- 2MHZ \- 32MHZ \- EXTERNAL \- PLL  
---|---  
PRESCALEA | The Xmega has 3 prescalers. With PRESCALEA you configure the clock division of the first prescaler. Possible values: 1 , 2 ,4, 8, 16, 32, 64, 128,256,512  
PRESCALEBC | The Xmega has 3 prescalers. With PRESCALEBC you configure the clock division of the second and the third prescaler. Possible values: \- 1_1 (1 + 1 division) \- 1_2 (1+2 division) \- 4_1 (4 + 1 division) \- 2_2 (2 + 2 division) This 1_2 will make the second prescaler divide by 1 and the third prescaler divide by 2.  
  
See also

[CONFIG OSC](config_osc.md)

Example

Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1 ' use 32 MHz

---

## CONFIG SYSCLOCK XTINY

Action

Selects the oscillator source for the system clock.

Syntax

CONFIG SYSCLOCK=sysclock ,  PRESCALE=prescale , CLOCKOUT=clockOtp, CLOCKOUT_PIN=pinmode

Remarks

SYSCLOCK | The oscillator used for generation of the system clock. This oscillator must be running.  Possible values: \- 16_20MHz : internal 20 MHz oscillator or 16 MHz oscillator. This depends on the fuse you set. \- 32KHz_INT : internal ultra low power oscillator \- 32KHz_EXT : 32 Khz external crystal oscillator \- EXTERNAL : external clock  
---|---  
PRESCALE | The Xtiny can divide the oscillator clock with the following values : 1,2,4,8,10,12,16,24,32,48 and 64.  
|   
CLOCKOUT | The Xtiny can route the clock output to a pin. Select ENABLED or DISABLED. Even in input mode the clock signal will be present on the designated pin. But the signal is best when the pin is set to output mode.  
CLOCKOUT_PIN | This option will set the CLOCKOUT put pin into output mode. The only possible value is : OUTPUT  
  
When using the CLOCKOUT option you can either set the output pin yourself into output mode or use the CLOCKOUT_PIN opiont.

Some processors do not have the CLOCKOUT pin. For these processors this option is not present in the DAT files.

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : serial-osc.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates USART  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
'the clockout_pin is PB.5  
Config Sysclock = 16_20mhz , Prescale = 1 , Clockout = Enabled , Clockout_pin = Output  
  
'configure the USART

'use calibrated offset to compensate the BAUD  
Config Com1 = 250000 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1 , Baud_offset = Osc20_5v  
  
Waitms 2000  
  
Print "Test USART"  
Dim B As Byte  
  
Do  
Print "this is a baud test"  
Print Hex(clkctrl_osc20mcaliba)   
```
B = Inkey()  
If B = "+" Then  
Cpu_ccp = &HD8  
Incr Clkctrl_osc20mcaliba  
Elseif B = "-" Then  
Cpu_ccp = &HD8  
Decr Clkctrl_osc20mcaliba  
```vb
End If  
Waitms 500  
Loop  
  


```

---

## CONFIG TCA0

Action

This configuration statement configures timer TCA0 found in the XTINY.

Syntax

CONFIG TCA0=mode, PRESCALE=prescale, RUN=run, LUPD=lupd , COMPAREx=compareX, RESOLUTION=resolution, EVENT_ACTION=event_action, OVF_INT=int, CMP0_INT=int, CMP1_INT=int, CMP2_INT=int

Remarks

At the moment of writing, all XTINY processors have one TIMER TCA0. This is a 16 bit timer with the following capabilities :

â¢ 16-Bit Timer/Counter

â¢ Three Compare Channels

â¢ Double Buffered Timer Period Setting

â¢ Double Buffered Compare Channels

â¢ Waveform Generation:

â Frequency generation

â Single-slope PWM (pulse-width modulation)

â Dual-slope PWM

â¢ Count on Event

â¢ Timer Overflow Interrupts/Events

â¢ One Compare Match per Compare Channel

â¢ Two 8-Bit Timer/Counters in Split Mode

We do not want to copy the data sheet info. You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer and/or Wave Generation mode.  Possible values : \- NORMAL, no wave generation (NORMAL) \- FREQ , frequency generation (FRQ) \- PWM , pulse width modulation single slope (SINGLESLOPE) \- PWM_TOP, pwm dual slope (DSTOP) \- PWM_TOPBOT, pwm dual slope (DSBOTH) \- PWM_BOT, pwm dual slope (DSBOTOM) \- A value between 0-7 will load the mode. See table 2.  
---|---  
PRESCALE | The pre scaler can divide the system clock that is applied to the timer. The pre scaler will only divide the system clock. Possible values : \- 1 , 2, 4, 8, 64, 256, 1024 \- OFF, timer is disabled  
RUN | This enables or disables the timer. Possible values : ON : timer will run OFF : timer will stop  
LUPD | Lock update. Possible values : MANUAL : LUPD in TCA.CTRLE not altered by system AUTO : LUPD in TCA.CTRLE set and cleared automatically  
CompareX COMPARExL COMPARExH | In the FRQ or PWM Waveform Generation mode, the PORT output register for the corresponding pin can be overridden. COMPARE0 will enable/disable WO0 COMPARE1 will enable/disable WO1 COMPARE2 will enable/disable WO2 DISABLE means : Port output settings for the pin with WOn output respected. ENABLE means : Port output settings for pin with WOn output overridden in FRQ or PWM Waveform Generation mode In SPLIT mode the counters are split into two 8 bit timers. The name COMPARE0 becomes COMPARE0L and COMPARE0H. Instead of WO0,WO1 and WO2, there are 3 additional outputs : WO3, WO4 and WO5.  
RESOLUTION | This option sets the resolution of the timer.  Possible value : \- NORMAL : 16 bit \- SPLIT : two 8 bit timers  
EVENT_ACTION | This option defines what kind of event action will increment or decrement. Possible values : \- DISABLED : counting on event input is disabled \- ENABLED, COUNT_POS_EDGE : count on positive edge event \- COUNT_ANY_EDGE : count on any edge event \- COUNT_HIGH_LVL : count on prescaled clock while event line is 1 \- COUNT_UPDOWN : count on prescaled clock. The event controls the count direction. Up counting when the event line is 0, down counting when the event line is 1.  
OVF_INT CMP0_INT CMP1_INT CMP2_INT | You can enable/disable interrupts in BASCOM using the ENABLE/DISABLE statement. You can also enable interrupts using the CONFIG statement. Possible values : ENABLED and DISABLED Possible interrupt sources you can set : OVF_INT : timer overflow/underflow interrupt CMP0_INT : compare channel 0 interrupt CMP1_INT : compare channel 1 interrupt CMP2_INT : compare channel 2 interrupt  
  
Table 2.

Value | Mode | TOP | UPDATE | EVENT  
---|---|---|---|---  
0 | NORMAL | PER | TOP | TOP  
1 | FREQ | CMP0 | TOP | TOP  
2 | reserved |   

3 | PWM, single slope | PER | BOTTOM | BOTTOM  
4 | reserved |   

5 | PWM, dual slope | PER | BOTTOM | TOP  
6 | PWM, dual slope | PER | BOTTOM | TOP and BOTTOM  
7 | PWM, dual slope | PER | BOTTOM | BOTTOM  
  
In normal AVR the ICR register is used to define the PWM frequency. In Xtiny the PER register must be used : TCA0_per = 8000 

The duty cycle can be loaded in the TCA0_CMP0 register (or a register of the other channels)

In normal AVR processors the timers had an alias to the counter register named TIMER0, TIMER1 , etc. 

Thus TIMER1 would access TIMER1 registers TCNT1L and TCNT1H. 

In the Xtiny, megaX. AVRX these aliases do not exist. There is however an alias to access word registers like a word. 

You can find these aliases in the DAT file under the [WIO] section.

For TCA0 you will find :

\- TCA0_CNT the timer counter register

\- TCA0_PER the period register

\- TCA0_CMP0 the compare 0 register

\- TCA0_CMP1 the compare 1 register

\- TCA0_CMP2 the compare 2 register

All relevant registers that form a word register like :

TCA0_CNTL=2592 ; 0A20 byte alias LSB see WIO

TCA0_CNTH=2593 ; 0A21 byte alias MSB see WIO

Will have an entry under the WIO section.

This is simply the name without the L/H

And the address is always the low register address.

Because the name is under the WIO section the variable/register will be treated as a 16 bit word. The correct read/write order will be used by the compiler which is different for AVR/XMEGA/XTINY

When you like to use your own definition or alias you could add an alias. Just take care that an update will replace the DAT files. 

For example if you like TIMER1 or TCA0 you can add it to the WIO section like this :

TCA0_CNT=2592 ; 0A20 word ## EXISTING ENTRY

TCA0 = 2592 ; NEW ENTRY

If you like an alias to be used you best write to support. When there is enough demand we add it.

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : TCA0-PWM.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates TCA0  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
'set the system clock and prescaler  
  
Config Sysclock = 16_20mhz , Prescale = 1 , Clockout = Enabled  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Waitms 2000  
  
Print "Test TCA0"  
  
Config Portb.0 = Output 'WO0 output  
  
Config Tca0 = Pwm_bot , Prescale = 1 , Resolution = Normal , Compare0 = Enabled , Run = On  
```
Tca0_per = 8000 'PWM frequency (period)  
Tca0_cmp0 = 2000 '25% duty cycle on pin PB0 (WO0)  
  
Do  
nop  
Loop

---

## CONFIG TCB0-TCB1

Action

This configuration statement configures timer TCB0/TCB1 found in the XTINY.

Syntax

CONFIG TCB0|TCB1=mode, RUN=run, PRESCALE=prescale, RUNMODE=runmode , SYNCUPDATE=syncupdate, ASYNC=async, CCMP_INIT=ccmp_init, CCMP_OTP=ccmp_otp, FILTER=filter, EDGE=edge, CAPT_EVENT=ecapt_event, CAPT_INT=capt_int

Remarks

At the moment of writing, all XTINY processors have one TIMER TCB0. Some processors have 2 TCB timers like the tiny3216.

The second TCB timer is named TCB1.

The TCB is is a 16 bit timer with the following capabilities :

â¢ 16-Bit Counter Operation Modes:

â Periodic interrupt

â Time-out check

â Input capture

â¢ On event

â¢ Frequency measurement

â¢ Pulse-width measurement

â¢ Frequency and pulse-width measurement

â Single shot

â 8-bit Pulse-Width Modulation (PWM)

â¢ Noise Canceler on Event Input

â¢ Optional: Operation Synchronous with TCA0

You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer mode. Possible values : \- PERIODIC_INT : Periodic interrupt \- TIME_OUT_CHECK : time out check \- INP_CAP_EVENT : input capture event \- INP_CAP_FREQ : input capture frequency \- INP_CAP_PWM : input capture pulse with measurement \- INP_CAP_FREQ_PWM : input capture frequency width measurement \- SINGLE_SHOT : single shot \- PWM : 8 bit PWM \- A value between 0-7 will load the mode. See table 2.  
---|---  
PRESCALE | The pre scaler can divide the system clock that is applied to the timer. The pre scaler will divide the system clock. Possible values : \- 1 , 2 \- TCA0 : uses CLK_TCA from timer TCA0 \- OFF, timer is disabled  
RUN | This enables or disables the timer. Possible values : ON : timer will run OFF : timer will stop  
RUNMODE | Run in standby mode.  ENABLED : the timer runs in standby sleep mode.  Except when PRESCALE is set to TCA0. DISABLED : timer is stopped in standby sleep mode.  
SYNCUPDATE | Synchronize Update. ENABLED : TCB will restart whenever the TCA0 counter is restarted or overflows. This can be used to synchronize capture with the PWM period DISABLED : no sync   
ASYNC | Asynchronous Enabling. ENABLED : asynchronous updates of the TCB signal in single shot mode  The output will go HIGH when an event arrives DISABLED : The output will go HIGH when the counter starts after synchronization.  
CCMP_INIT | Compare/Capture PIN initial value. This setting is used to set the initial output value of the pin when an pin output is used. This bit has no effect in 8 bit PWM and single shot mode. LOW : initial pin state is low HIGH : initial pin state is high  
CCMP_OTP | Compare/Capture output enable. This option is used to set the output value of the compare/capture output DISABLED : Compare/capture output is zero. ENABLED : Compare/capture output has a valid value  
FILTER | Filter capture noise cancellation filter.  ENABLED : the input capture noise cancellation unit is enabled DISABLED : input capture noise cancellation unit is disabled.  
EDGE | Event Edge. This selects the event edge. The effect of this depends on the selected count mode.  | Mode | Edge | Positive Edge | Negative Edge  
---|---|---|---  
PERIODIC_INT | 0 1 | NA NA | NA NA  
TIME_OUT_CHECK | 0 1 | Start counter Stop counter | Stop counter Start counter  
INP_CAP_EVENT | 0 1 | Input capture freq and pulse with measurement mode NA | NA capture=count  
INP_CAP_FREQ | 0 1 | capture=count,init,int NA | NA capture=count, init, int  
INP_CAP_PWM | 0 1 | init capture=count, int | capture=count,int init  
SINGLE_SHOT | 0 1 | Start counter Start counter | NA Start counter  
PWM | 0 1 | NA NA | NA NA  
INP_CAP_FREQ_PWM | 0 | On 1st positive : init On following negative : capture On second positive : stop, int  
  
| 1 | On 1st negative : init On following positive : capture On second negative : stop, int  
  
CAPT_EVENT | Capture Event input enable. ENABLED : event input capture is enabled. DISABLED : event input capture is disabled  
CAPT_INT | All interrupts can be enabled/disabled using the ENABLE/DISABLE statements. The Capture interrupt enable can be enabled/disabled using the configuration parameter. ENABLED : capture interrupt is enabled DISABLED : capture interrupt is disabled  
  
See also

[CONFIG TCA0](config_tca0.md), [CONFIG_TCD0](config_tcd0.md)

Example

---

## CONFIG TCD0

Action

This configuration statement configures timer TCD0 found in the XTINY.

Syntax

CONFIG TCD0=mode, PRESCALE=prescale , CLOCK_SOURCE=clock_source , SYNC_PRESCALER=sync_prescaler, RUN=run , CMPD_SEL=cmpd_sel , 

CMPC_SEL=cmpc_sel, FIFTY=fifty , AUT_UPDATE=auto_update , CMP_OVR=cmp_over , CMP_VAL=cmp_val , 

EVENTA_CONFIG=eventA_config , EVENTB_CONFIG=eventb_config , EVENTA_ACTION=eventa_action , EVENTB_ACTION=eventb_action ,

EVENTA_TRIG=eventa_trig, EVENTB_TRIG=eventb_trig , TRIGA_INT=triga_int , TRIGB_INT=trigb_int , OVF_INT=over_int , 

INP_MODEA=inp_modea ,INP_MODEB=inp_modeb ,CMPAEN=cmpaen, CMPBEN=cmpben ,CMPCEN=cmpcen ,CMPDEN=cmpden, 

CMPA=cmpa, CMPB=cmpb , CMPC=cmpc ,CMPD=cmpd, DLY_PRESCALER=dly_prescaler , DLY_TRIGGER=dly_trigger

DLY_SEL=dly_sel ,DLY_VAL=dly_val , DIT_CTRL=dit_ctrl , DIT_VAL=dit_val , 

DIS_EOC=dis_eoc , SOFT_CAPB=soft_capb , SOFT_CAPA=soft_capa , RESTART_STROBE=restart_strobe , SYNC_STROBE=sync_strobe, 

SYNC_EOC=sync_eoc

Remarks

The timer TCD0 is found in a number of XTINY processors.

The TCD0 is is a 12 bit timer with the following capabilities :

â¢ 12-bit timer/counter

â¢ Programmable prescaler

â¢ Double buffered compare registers

â¢ Waveform generation

â One ramp mode

â Two ramp mode

â Four ramp mode

â Dual-slope mode

â¢ Two separate input capture, double buffered

â¢ Connection to event system

â Programmable filter

â¢ Conditional waveform on external events

â Fault handling

â Input blanking

â Overload protection function

â Fast emergency stop by hardware

â¢ Supports both half bridge and full bridge output

You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer wave generation mode. Possible values : \- ONE_RAMP : One ramp mode \- TWO_RAMP : Two ramp mode \- FOUT_RAMP : Four ramp mode \- DUAL_SLOPE : dual slope mode \- A value between 0-3 will load the mode.   
---|---  
PRESCALE | The counter prescaler selects the division factor of the TCD counter clock. Possible values : \- 1 , 4 and 32  
CLOCK_SOURCE | The clock source for the TCD clock \- OSC16_20MHZ : the internal 16/20 MHz oscillator \- EXTERNAL : an external clock signal \- SYSTEM : system clock  
SYNC_PRESCALER | The synchronization prescaler select the division factor of the TCD clock.  Possible values : 1, 2 , 4 and 8  
RUN | This enables or disables the timer. Possible values : ENABLED : TCD is enabled and running DISABLED : TCD is disabled  
CMPD_SEL | Compare D output select \- PWMA : Waveform A \- PWMB : Waveform B  
CMPC_SEL | Compare C output select \- PWMA : Waveform A \- PWMB : Waveform B  
FIFTY | Fifty percent waveform.  \- ENABLED : chose this when two waveforms have identical characterics. This will cause any values written to CMPBSET/CLR register also to be written to register CMPASET/CLR  
AUT_UPDATE | Automatic Update. ENABLED : A synchronization at the end of the TCD cycle is automatically requested after the compare B Clear High register (CMPBCLRH) is written, DISABLED : no sync   
CMP_OVR | Compare output value override.  ENABLED : default values of the waveform outputs A and B are overridden by the values written in the compare X value in active state bit fields in the control D register CTRLD.CMPnxVAL. DISABLED : no action  
CMP_VAL | The CMPVAL register contains compare values for compare A and B. This is only used when CMP_OVR is enabled. A numeric value must be used between 0-255. The upper nible writes to CMPBVAL. The lower nibble writes to CMPAVAL. | CMPxVAL | A_off | A_on | B_off | B_on  
---|---|---|---|---  
PWMA | CMPAVAL[0] | CMPAVAL[1] | CMPAVAL[2] | CMPAVAL[3]  
PWMB | CMPBVAL[0] | CMPBVAL[1] | CMPBVAL[2] | CMPBVAL[3]  
  
In One Ramp mode, PWMA will only use A_off and A_on values and PWMB will only use B_off and B_on values.

This is due to possible overlap between the values A_off, A_on, B_off and B_on.  
  
| The following config options are intended to be used alone. For example : config tcd0=mode,DIS_EOC=ENABLED The datasheet does not make it clear if these commands can be combined.   
DIS_EOC | Disable at end of TCD cycle strobe. When ENABLED the ENRDY bit in TCD0_STATUS will keep low until the TCD is disabled. Writing to this bit only has effect if there no ongoing synchronization of Enable. (RUN=ENABLED) The ENRDY bit tells when the ENABLE value is synchronized to the TCD domain and is ready to be written again. The following clears the ENRDY bit :  \- writing to the ENABLE bit (RUN=ENABLED|DISABLED) \- DIS_EOC strobe=ENABLED  
SOFT_CAPB | Software Capture B strobe. When ENABLED a software capture to capture register B is done as soon as the strobe is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SOFT_CAPA | Software Capture A strobe. When ENABLED a software capture to capture register A is done as soon as the strobe is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
RESTART_STROBE | Restart Strobe. When ENABLED a restart of the TCD counter is executed as soon as this bit is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SYNC_STROBE | Synchronize Strobe When ENABLED the double buffered registers will be loaded to the TCD domain as soon as this bit is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SYNC_EOC | Synchronize end of TCD cycle strobe. When ENABLED the double buffered registers will be loaded to the TCD domain at the end of the next TCD cycle. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
|   
EVENTA_CONFIG EVENTB_CONFIG | Event A|B configuration. When the Input Capture Noise canceler is activated (FILTERON), the Event input is filtered. The filter function requires four successive equal valued samples of the Retrigger pin for changing its output. The Input Capture is therefore delayed by four clock cycles when the noise canceler is enabled. When the Asynchronous Event is enabled (ASYNCON), the Event input will qualify the output directly. Possible values : \- NEITHER : Neither Filter nor Asynchronous Event is enabled. \- FILTER_ON : Input Capture Noise Cancellation Filter enabled. \- ASYNC_ON : Asynchronous Event output qualification enabled.  
EVENTA_EDGE EVENTB_EDGE | Edge Selection This bit is used to select the active edge or level of the event interrupt \- FALL_LOW : The falling edge or low level of the Event input generates Retrigger or Fault action. \- RISE_HIGH : The rising edge or high level of the Event input generates Retrigger or Fault action.  
EVENTA_ACTION EVENTB_ACTION | Event Action. This bit enables Capture on Event input. By default, the input will trigger a Fault, depending on the Input x register input mode (TCD.INPUTx). It is also possible to trigger a Capture on the Event input. Possible values :  \- FAULT : FAULT Event triggers a Fault. \- CAPTURE : CAPTURE Event triggers a Fault and Capture.  
EVENTA_TRIG EVENTB_TRIG | Trigger Event Input Enable This options enabled or disables the Event as a trigger to input A|B  
TRIGA_INT TRIGB_INT OVF_INT | Interrupts can be enabled/disabled by using the ENABLE and DISABLE statements. Using the timer interrupt names you can also enable/disable them using the CONFIG statement. \- ENABLED : the interrupt will be enabled \- DISABLED : the interrupt is disabled TRIGA_INT : event is executed when trigger input A is received TRIGB_INT : event is executed when trigger input B is received OVF_INT : event is executed when the timer overflows or restarts  
INP_MODEA INP_MODEB | Input mode options. Possible values : \- NONE : input has no action \- JMPWAIT : stop output, jump to opposite compare cycle and wait \- EXECWAIT : stop output, execute opposite compare cycle and wait \- EXECFAULT : stop output , execute opposite compare cycle while fault active \- FREQ : stop all outputs, maintain frequency \- EXECDT : stop all outputs, execute dead time while fault active \- WAIT : stop all outputs, jump to next compare cycle and wait \- WAITSW : stop all outputs, wait for software action \- EDGETRIG : stop all output on edge, jump to next compare cycle \- EDGETRIGFREQ : stop output on edge, maintain frequency \- LVLTRIGFREQ : stop output at level, maintain frequency  
CMPAEN CMPBEN CMPCEN CMPDEN | Compare Enable output pin.  ENABLED : The compare output pin is enabled. DISABLED : The compare output pin disabled (no output) At reset the settings are loaded from FUSE.TCDFG. So configuration should not be required.  
CMPA CMPB CMPC CMPD | Compare value. These bits set the default state from Reset or when a input event triggers a fault causing changes to the output. At reset the content is kept and during the reset sequence loaded from the TCD configuration fuse so configuration should not be required. ENABLED : set the bit to 1. DISABLED : reset the bit to 0.  
DLY_PRESCALER | Delay Prescaler. This option controls the prescaler setting for the blanking or output event delay Possible prescaler values : 1,2,4 and 8  
DLY_TRIGGER | Delay Trigger. These option control what should trigger the blanking or output event delay. \- CMPASET : CMPASET triggers delay \- CMPACLR : CMPACLR triggers delay \- CMPBSET : CMPBSET triggers delay \- CMPBCLR : CMPASET troggers delay (end of cycle)  
DLY_SEL | Delay Select. This option controls what function should be used by the delay trigger the blanking or output event delay \- OFF : delay function not used \- INBLANK : input blanking enabled \- EVENT : event delay enabled  
DLY_VAL | Delay value. This value specifies the blanking output event delay time or event output synchronization in number of prescaled TCD cycles. This is an 8 bit value from 0-255. The default is 0.  
DIT_CTRL | Dither Control. This option configures which compare register is using the dither function. \- ONTIMEB : On-time ramp B \- ONTIMEAB : On-time ramp A and B \- DEADTIMEB : Dead-time ramp B \- DEADTIMEAB : Dead-time ramp A and B  
DIT_VAL | Dither value. These bits configure the fractional adjustment of the on-time or off-time according to Dither Selection bits (DITHERSEL) in the Dither Control register (TCD.DITCTRL). The DITHER value is added to a 4-bit accumulator at the end of each TCD cycle. When the accumulator overflows the frequency adjustment will occur. The DITHER bits are doubled buffered so the new value is copied in at an update condition. The value has a range from 0-15. Default value is 0.  
  
See also

[CONFIG TCA0](config_tca0.md) , [CONFIG_TCB](config_tcb0_tcb1.md)

Example

---

## CONFIG TCPIP

Action

Configures the TCP/IP chip's from WIZNET (<http://www.wiznet.co.kr/>).

This chip's can be found on various modules and shields but the Config Tcpip is always depending on the WIZNET chip.

Supported chip's are W3100A, W5100, W5200 and W5300.

Syntax W3100A

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, TX= tx, RX= rx , NOINIT= 0|1 [, TWI=address] [, Clock = speed] [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=W3100A] 

Syntax W5100

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, TX= tx, RX= rx , NOINIT= 0|1 [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=5100] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] 

Syntax W5200

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [,TimeOut=tmOut] [,CHIP=W5200] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] [TXn= tx] [, RXn= rx] 

Syntax W5300

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=W5300] [,INT=imsg] [,NOUDP=noudp] [align=align] [TXn= tx] [, RXn= rx] [SOCKMEM=sockmem]

Syntax W5500

CONFIG TCPIP = NOINT , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [,TimeOut=tmOut] [,CHIP=W5500] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] [TXn= tx] [, RXn= rx] 

Remarks

Int | The interrupt to use such as INT0, INT1 or INTn. For the Easy TCP/IP PCB, use INT0. W5100,W5200,W5300 also support the NOINT option. This option will not use any interrupt. The internal status array s_status will not be created and is not available either.  When you do use interrupts, the s_status array will contain the status of each socket. s_status(1) will contain the status of the first socket. In interrupt mode you can also get a notification that a socket was updated when you use the INT=1 option. Using interrupts does use more code and resources.  W5500 only supports the NOINT option.  
---|---  
MAC | The MAC address you want to assign to the ethernet chip. The MAC address is a unique number that identifies your chip. You must use a different address for every ethernet chip in your network. Example : 00.00.12.34.56.78 You need to specify 6 bytes that must be separated by dots. The bytes must be specified in decimal notation. For some networks it is important that the MAC address starts with a zero. So we advise to start the MAC address with a 0.  
IP | The IP address you want to assign to the chip. The IP address must be unique for every ethernet chip in your network. When you have a LAN, 192.168.0.10 can be used. 192.168.0.x is used for LANâs since the address is not an assigned internet address. The same applies to 10.0.0.0.  
SUBMASK | The sub mask you want to assign to the ethernet chip. The sub mask is in most cases 255.255.255.0  
GATEWAY | This is the gateway address of the ethernet chip. The gateway connects your LAN with the internet. The gateway address you can determine with the IPCONFIG command at the command prompt : C:\>ipconfig Windows 2000 IP Configuration Ethernet adapter Local Area Connection 2: Connection-specific DNS Suffix . : IP Address. . . . . . . . . . . . : 192.168.0.3 Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 192.168.0.1 Use 192.168.0.1 in this case.  
LOCALPORT | A word value that is assigned to the LOCAL_PORT internal variable. See also [Getsocket](getsocket.md). As a default you can assign a value of 5000.  
TX | W3100A,W5100 A byte which specifies the transmit buffer size of the W3100A/W5100. The W3100A/W5100 has 4 sockets. A value of 00 will assign 1024 bytes, a value of 01 will assign 2048 bytes. A value of 10 will assign 4096 bytes and a value of 11 will assign 8192 bytes. This is binary notation. And the Most Significant bits (bit 6 and 7) specify the size of socket 3. For example, you want to assign 2048 bytes to each socket for transmission : TX = &B01010101 Since the transmission buffer size may be 8KB in total, you can split them up in 4 parts of 2048 bytes : 01. When you want to use 1 socket with 8KB size, you would use : TX = &B11. You can use only 1 socket in that case : socket 0. Consult the W3100A/W5100 pdf for more info.  
RX | W3100A,W5100 A byte which specifies the receive buffer size of the W3100A/W5100. The W3100A/W5100 has 4 sockets. A value of 00 will assign 1024 bytes, a value of 01 will assign 2048 bytes. A value of 10 will assign 4096 bytes and a value of 11 will assign 8192 bytes. This is binary notation. And the Most significant bits specify the size of socket 3. For example, you want to assign 2048 bytes to each socket for reception : RX = &B01010101 Since the receive buffer size may be 8KB in total, you can split them up in 4 parts of 2048 bytes : 01. When you want to use 1 socket with 8KB size, you would use : RX = &B11. You can use only 1 socket in that case : socket 0. Consult the W3100A/W5100 pdf for more info.  
TXn | W5200, W5300,w5500 A constant which specifies the socket size of the transmit buffer of socket n. N is in range of 1-8. This notation is only used by W5200 and W5300 where you can define the size in KB. By default the W5200 sockets are 2 KB each and the W5300 are 8 KB each. The following values are possible : | Value | W5200,W5500 | W5300  
---|---|---  
1 | 1 KB | 1 KB  
2 | 2 KB default | 2 KB  
4 | 4 KB | 4 KB  
8 | 8 KB | 8 KB default  
15 | 16 KB | 15 KB  
any other value between 1-64 | invalid  | size in KB  
  
The total amount may not exceed the available socket memory. For example the W5200 can use 8x2=16 KB of TX memory. But you can also use 2 sockets with 8 KB each.   
  
RXn | W5200,W5300,W5500 This will set the socket receive buffer size similar as described above for TXn.  
sockmem | W5300 The w5300 allows to configure how much of the memory is used for the transmit and receive buffers. The default is &HFF00 which will split the memory in even parts. See the W5300 datasheet for more details.  
Noinit | Make this option 1 when you want to configure the TCP, MAC, Subnetmask and GateWay dynamic. Noinit will only make some important settings and you need to use [SETTCP](settcp.md) in order to finish the setup.  
TWI | W3100A only The slave address of the W3100A/NM7010. When you specify TWI, your micro must have a TWI interface such as Mega128, Mega88, Mega32. TWI is only supported by the W3100A.  
Clock | W3100A only The clock frequency to use with the TWI interface. Use this in combination with the TWI option.  
Baseaddress | W3100A,W5100,W5300 An optional value for the chip select of the ethernet chip. This is default &H8000 when not specified. When you create your own board, you can override it. See also: [Adding XRAM with External Memory Interface](adding_xram.md)  
TimeOut | W3100A You can specify an optional timeout when sending UDP data. The Wiznet API does wait for the CSEND status. But it means that it will block your application. In such cases, you can use the timeout value. The timeout constant is a counter which decreases every time the status is checked. When it reaches 0, it will get out of the loop. Thus a higher value will result in a longer delay. Notice that it has nothing to do with the chip timeout registers/values. Without the software timeout, the chip will also time out.  W5100,W5200 and W5300 have a time out option in the hardware.  
CHIP | The wiznet chip you use. By default this is W3100. Specify W5100 for the W5100 chip. This chip has 4 sockets and a SPI interface instead of an I2C/TWI interface. Specify W5200 for the W5200 chip. This chip has 8 sockets and only a SPI interface. This SPI interface has a high speed. Specify W5300 for the W5300 chip. This chip has 8 sockets and can work in bus mode only. Specify W5500 for the W5500 chip. This chip has 8 sockets and only a SPI interface. This SPI interface supports high speed and blockmode.  
SPI | This option is intended to be used with the W5100/W5200 chips. When you want to use the W5100 or W5200 in SPI mode, make this parameter value 1.  When you do not specify his parameter, or set it to 0, the external memory mode will be used.  For the Xmega you can specify SPIC, SPID, SPIE of SPIF. For normal AVR with multiple SPI such as M328PB you can specify SPI1 When using SPI, you must configure it before configuring the TCPIP. SPI must be configured in mode 0. Example : Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0 'Init the spi pins  
Spiinit  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1 , Cs = Portb.4  
imsg | In interrupt mode, you can get a notification about changed socket status such as new data arrived, or socket closed. Use INT=1 for this option. The library will call a routine named TCP_INT. So your code need to include this label or sub routine. You can test the s_status() array but you can also test the _tcp_intflags variable. This variable contains the flags from the IR register. You must dimension the variable _tcp_intflags if you want to use this option.  
cs | This is an optional parameter used in combination with the SPI option. By default the compiler will use the standard SS pin for the SPI. But if you have multiple SPI slaves, or want to use a different pin to control the CS of the W5100/W5200, you can add this parameter. The name of a port pin is expected such as PORTB.4 ![notice](notice.jpg)You should use a normal port register. Do not use an extended address port like PORTL.  
noudp | By default UDP variables PEERADDRESS, PEERPORT and PEERSIZE are created by the compiler. If you do not use any UDP statement, you can use NOUDP=1. This will save 8 bytes of memory.  
align | The W5300 has an align option. Align is ignored for all other chips. The align modes : 0 \- this will disable alignment. This will add a header packet for TCP data with the size. You must use TCPREADHEADER to read the actual data size. [Socketstat](socketstat.md) will not return the actual data size. After you have determined there is data in the receive buffer, you must use TCPREADHEADER to get the actual size. You may only use TCPREADHEADER once since it will read 2 bytes from the receive buffer. 1\- this will enable alignment. This will not add the header packet to TCP data. SocketStat will return the actual data size. You must not use TCPREADHEADER in this case. 2\- since using alignment caused some unexpected problems in tcp traffic, (see wiznet forum) there is also the smart and default option which makes tcp reading compatible to the other chips. When using mode 2, the mode 0 will be used, and socketstat will automatic read the buffer size packet in case there is data in the received buffer and this it will return the correct size. Since it will read from the receive buffer, you must empty the buffer with tcpread, after you have determined that there is data waiting. You must not call [socketstat](socketstat.md) again before you have read all the pending data.  
  
The CONFIG TCPIP statement may be used only once.

If you do use interrupts, you must enable them before you use CONFIG TCPIP. When using the NOINT option this is not required.

Configuring the ethernet chip will initialize the chip.

After the CONFIG TCPIP, you can already PING the chip!

![notice](notice.jpg)As all the samples show, the CONFIG TCPIP must be used in the main program. The CONFIG TCPIP should be used early as possible in your code. This is especially important for processors with multiple pages. (>64KB). The reason is that the configuration data is stored in flash and read with LPM instruction. LPM can only reach page 0. 

W3100A

The TWI mode works only when your micro support the TWI mode. You need to have 4k7 pull up resistors.

MCS Electronics has a small adapter PCB and KIT available that can be connected easily to your microprocessor.

The TWI mode makes your PCB design much simpler. TWI is not as fast as bus mode. While you can use every supported TCP/IP function, it will run at a lower speed.

W5100

The W5100 is the successor of the W3100A. It is an improved chip without shadow registers. This means that less code is required to use the chip. 

Because the W5100 has different constants compared to the W3100A, the constants are removed from the samples. The constants are automatically created with a value depending on the chip you use.

From the user perspective the W5100 library is almost the same as the W3100 library. But there are some differences. 

\- The peersize, peerport and peeraddress have a different order in the W5100. To avoid mistakes, the compiler will create these variables automatic in the proper order. The NOUDP=1 option can disable this feature if you do not use UDP.

\- When reading UDP, you need to use the [UDPREADHEADER](udpreadheader.md) statement to read the UDP header. After reading the header, the peersize, peerport and peeraddress variables are set. You then should use the peersize variable to determine the number of bytes to retrieve. You must read all these bytes. 

\- The W5100 has a command to disconnect the socket in TCP/IP mode. It is named [SOCKETDISCONNECT](socketdisconnect.md).

\- The CLOSESOCKET statement has been renamed into [SOCKETCLOSE](socketclose.md). You can use both names. 

The MCS web shop offers the [WIZ810MJ](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=266&category_id=22&option=com_phpshop&Itemid=1>) ethernet module and the [TCPADB5100](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=267&category_id=22&option=com_phpshop&Itemid=1>) adapter board. 

W5200

The W5200 is a SPI only version of the W5100 so read the comment above about the W5100 first.

The W5200 chip has less pins and is smaller and simpler to use. It has 8 sockets instead of 4 and it has a faster SPI mode. One example where the W5200 is used is the Wiz820io module. See example below. 

This Chip need specific reset times before you can use config TCPIP (see example below).

It has been reported that when the RETRY_TIME and RETRY_COUNT registers are altered, sending UDP data can have a variable delay the first time the data will actually be sent. 

W5300

The W5300 is a bus mode only version of the W5100 so read the comment above about the W5100 first

The W5300 chip has a fast 8/16 bit bus and has 8 sockets with increased socket size. 

See also the W5300 examples in: [Adding XRAM with External Memory Interface](adding_xram.md) regarding base address.

W5500

The W5500 is a SPI only version of the W5100 so read the comment above about the W5100 first.

The W5500 chip has less pins and is smaller and simpler to use. It has 8 sockets instead of 4 and it has a faster SPI mode. It is similar to W5200.

For samples, use the W5200 samples and change CHIP to W5500.

The W5500 library has specific provision to be used in a boot loader.

WIZ810

REV 1.0 of the WIZ810 leaves the SPI_EN Pin floating (REV1.1 has an internal pulldown). When using REV1.0 in parallel mode, you will have to tie that pin to ground.

See also

[GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md) , [SETTCP](settcp.md) , [UDPREAD](udpread.md), [UDPWRITE](udpwrite.md), [UDPWRITESTR](udpwritestr.md) , [UDPREADHEADER](udpreadheader.md), [TCPREADHEADER](tcpreadheader.md) , [TCPCHECKSUM](tcpchecksum.md), [SNTP](sntp.md) , , [GETTCPREGS](gettcpregs.md) , [SETTCPREGS](settcpregs.md)

Syntax Example using W3100:

Config Tcpip = Int0 , Mac = 00.00.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Now use PING at the command line to send a ping:

PING 192.168.0.8

Or use the easytcp application to ping the chip.

Syntax Example using W5100  
```vb
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 80 ' default use 40 for the frame space  
$lib "datetime.lbx" ' this example uses date time routines  
  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
Print "Init done"  
  
Dim Var As Byte ' for i2c test  
Dim Ip As Long ' IP number of time server  
Dim Idx As Byte ' socket number  
Dim Lsntp As Long ' long SNTP time  
  
Print "SNTP demo"  
  
'assign the IP number of a SNTP server  
```
Ip = Maketcp(64.90.182.55 ) ' assign IP num NIST time.nist.gov port 37  
```vb
Print "Connecting to : " ; Ip2str(ip)  
  
'we will use Dutch format  
Config Date = Dmy , Separator = -  
  
'we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx ; " " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
'The SNTP uses port 37 which is fixed in the tcp asm code  
  
Do  
Waitms 5000  
  
```
Lsntp = Sntp(idx , Ip) ' get time from SNTP server  
```vb
' Print Idx ; Lsntp  
'notice that it is not recommended to get the time every sec  
'the time server might ban your IP  
'it is better to sync once or to run your own SNTP server and update that once a day  
  
'what happens is that IP number of timer server is send a diagram too  
'it will put the time into a variable lsntp and this is converted to BASCOM date/time format  
'in case of a problem the variable is 0  
Print Date(lsntp) ; Spc(3) ; Time(lsntp)  
Loop  
  


```
Example for using W5200 Chip on a WIZ820io module with ATXMEGA:

Hardware connections:

WIZ820io [SCLK] <\-----> ATXMEGA128A1 PortC.7 [SCK]

WIZ820io [MOSI] <\-----> ATXMEGA128A1 PortC.5 [MOSI]

WIZ820io [MISO] <\-----> ATXMEGA128A1 PortC.6 [MISO]

WIZ820io [nSS] <\-----> ATXMEGA128A1 PortC.4 [SS]

WIZ820io [nReset]<\-----> ATXMEGA128A1 PortC.2

WIZ820io [nINT] <\-----> ATXMEGA128A1 PortC.3

Because it is a SPI based communication interface to the W5200 you need to setup the SPI interface (SPI on Port C is used in this example):

```vb
Config Spic = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk2 , Data_order = Msb , Ss = Auto 

Config Pinc.2 = Output  
```
W5200_nreset Alias Portc.2  
```vb
Set W5200_nreset  
  
Config Pinc.3 = Input  
```
W5200_nint Alias Portc.3

```vb
Reset the WIZ820io Module:

Reset W5200_nreset  
Waitms 1  
Set W5200_nreset  
Waitms 150

Config TCP Syntax Example for WIZ820io (using SPI on Port C and Port.4 as Slave Select (Chip Select)):

Config Tcpip = Noint , _  
```
Mac = 0.11.22.33.44.55 , _  
Ip = 192.168.1.254 , _  
Submask = 255.255.255.0 , _  
Gateway = 192.168.1.1 , _  
Localport = 80 , _  
Chip = W5200 , _  
Spi = Spic , _  
Cs = Portc.4

Now use PING at the command line to send a ping:

PING 192.168.1.254

Example for using W5300 Chip:

Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.253 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Chip = W5300 , Baseaddress = &HFC00

Now use PING at the command line to send a ping:

PING 192.168.1.253

See also the W5300 examples in: [Adding XRAM with External Memory Interface](adding_xram.md) regarding base address.

Example for using W5500 Chip:

```vb
'-----------------------------------------------------------------------------------------  
'name : sntp_W5500.bas RFC 2030  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : test SNTP() function  
'micro : xMega128A1  
'suited for demo : no, needs library only included in the full version  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64 ' default use 32 for the hardware stack  
$swstack = 128 'default use 10 for the SW stack  
$framesize = 64 'default use 40 for the frame space  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
'configure UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
  
Config Spie = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk32 , Data_order = Msb , Ss = Auto  
'SPI on Port E is used  
'portx.7 - SCK  
'portx.6 - MISO  
'portx.5 - MOSI  
'portx.4 - SS  
  
Waitms 1000  
Print "Init , set IP to 192.168.1.88" ' display a message  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.88 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Chip = W5500 , Spi = Spie , Cs = Porte.4  
Print "Init Done"  
  
  
$lib "datetime.lbx" 'this example uses date time routines  
  
  
Dim Ip As Long ' IP number of time server  
Dim Idx As Byte ' socket number  
Dim Lsntp As Long ' long SNTP time  
  
Print "SNTP demo"  
  
'assign the IP number of a SNTP server  
```
Ip = Maketcp(129.6.15.30 ) 'assign IP num NIST time.nist.gov port 37  
```vb
Print "Connecting to : " ; Ip2str(ip)  
  
  
'we will use Dutch format  
Config Date = Dmy , Separator = Minus  
  
  
'we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
'The SNTP uses port 37 which is fixed in the tcp asm code  
  
  
Do  
  
Waitms 5000  
  
```
Lsntp = Sntp(idx , Ip) ' get time from SNTP server  
```vb
'notice that it is not recommended to get the time every sec  
'the time server might ban your IP  
'it is better to sync once or to run your own SNTP server and update that once a day  
  
'what happens is that IP number of timer server is send a diagram too  
'it will put the time into a variable lsntp and this is converted to BASCOM date/time format  
'in case of a problem the variable is 0  
Print Date(lsntp) ; Spc(3) ; Time(lsntp)  
Loop  
  
  
  
End

```

---

## CONFIG TCXX

Action

Configures the Xmega TIMER.

Syntax

CONFIG TCxx = wg , PRESCALE=pre, COMPAREA=ca, COMPAREB=cb, COMPAREC=cc, COMPARED=cd, EVENT_SOURCE= event, EVENT_ACTION=act, EVENT_DELAY=ed, RESOLUTION=res

Remarks

Depending on the Xmega processor of your choice, there are one or more timers. The Xmega uses the name of the port as part of the name. The first port that has a timer is portC. The first timer is named TCC0. Most timer ports have 2 timers. The next timer is named TCC1. Xmega timers are 16 bit but can be cascaded to 32 bit timers or be set to 8 bit mode.

The possible timer names are : TCC0, TCC1, TCD0, TCD1, TCE0, TCE1, TCF0 and TCF1. 

WG | This options sets the Timer and/or Wave Generation mode.  Possible values : \- NORMAL, no wave generation \- FREQ , frequency generation \- PWM , pulse width modulation single slope \- PWM_TOP, pwm dual slope \- PWM_BOT, pwm dual slope \- PWM_TOPBOT, pwm dual slope \- A value between 0-7 will load the mode. See table 2. \- TIMER2. This will set the timer into byte mode.  
---|---  
PRESCALE or CLOCKSEL | The prescaler can divide the system clock that is applied to the timer. Possible values : \- 1 , 2, 4, 8, 64, 256, 1024 \- OFF, timer is disabled \- E0, E1, E2, E3, E4, E5, E6, E7 . Event channel 0-7 \- value between 0-15. This will write the value to the CTRLA register.  In the XMEGA, CLOCKSEL (clock selection) describes the parameter better than PRESCALE because of the additional options.  But the coded explorer will use PRESCALE from the DAT files.  In order not to break code the CLOCKSEL name will be dropped in a future version.  
COMPAREx | Where x is A, B, C, or D. This is the COMPARE or CAPTURE register setup. You may use either COMPARE or CAPTURE since the same registers are used. Each COMPARE/CAPTURE pin must be enabled if the input/output pin is used. By default they are disabled. Each TCx0 timer has 4 compare registers/pins. The TCx1 timer has two capture registers/pins. Possible values : ENABLED : this will enable the capture/compare register DISABLED : this will disable the capture/compare register 0 : this will set the logic level of the compare output pin to 0. 1 : this will set the logic level of the compare output pin to 1. In FREQ and PWM modes the compare pins will be set to output mode. In CAPTURE mode, the capture pin will be set to input mode. NOTE : NOT valid in TIMER2 mode.  
COMPAREx TIMER2 mode | In TIMER2 mode, there are 8 compare outputs. They have the names : CAPTUREAL , CAPTUREAH ,CAPTUREBL , CAPTUREBH, CAPTURECL, CAPTURECH,CAPTUREDL and CAPTUREDH. The last character indicates the Low or High byte. Each COMPARE/CAPTURE pin must be enabled if the input/output pin is used. By default they are disabled.  Possible values : ENABLED : this will enable the capture/compare ouput pin DISABLED : this will disable the capture/compare output pin 0 : this will set the logic level of the compare output pin to 0. 1 : this will set the logic level of the compare output pin to 1.  
EVENT_SOURCE | The event channel source. Possible values : \- OFF (default) \- E0-E7 \- A value between 0-15 NOTE : NOT valid in TIMER2 mode.  
EVENT_ACTION | The event action the timer will perform. Possible values : \- OFF \- CAPTURE, input capture \- UPDOWN, external controlled up/down count \- QDEC, quadrature decode \- RESTART , restart waveform period \- FREQ, frequency capture \- PWC, pulse width capture NOTE : NOT valid in TIMER2 mode.  
EVENT_DELAY | Enabled, or disabled(default). When this bit is set, the selected event source is delayed by one peripheral clock cycle. This feature is intended for 32-bit input capture operation. Adding the event delay is necessary for compensating for the carry propagation delay that is inserted when cascading two counters via the Event System. NOTE : NOT valid in TIMER2 mode.  
RESOLUTION | Valid options : NORMAL, BYTE, SPLIT. Timer resolution is 16 by default (NORMAL). A value of BYTE will set the timer to 8 bit resolution. SPLIT is reserved for future use.(cascading 32 bit timers ). When WG mode TIMER2 is chosen, the timer will be set into BYTE mode automatically.   
  
Table 2.

Value | Mode | TOP | UPDATE | EVENT  
---|---|---|---|---  
0 | NORMAL | PER | TOP | TOP  
1 | FREQ | CCA | TOP | TOP  
2 | reserved |   

3 | PWM, single slope | PER | BOTTOM | BOTTOM  
4 | reserved |   

5 | PWM, dual slope | PER | BOTTOM | TOP  
6 | PWM, dual slope | PER | BOTTOM | TOP and BOTTOM  
7 | PWM, dual slope | PER | BOTTOM | BOTTOM  
  
A CONFIG TCxx statement will update the timer control registers immediately. A pre scale value other than OFF will also [START](start.md) the timer at once.

![notice](notice.jpg)CONFIG TCxx statement must be placed in the main code. Or you may include it in the main code using $INCLUDE.

\- you can use CONFIG TCxx multiple times

\- do not use CONFIG TCxx in a SUB/FUNCTION in combination with SUBMODE=NEW. 

See Also

[START](start.md) , [STOP](stop.md)

Example 1:

```vb
'Counter/Timer D1 is used for overflow counter at --> 400ms  
'32MHz/256 = 125000

'32MHz/256 = 125000 --> 125000/2.5 = 50000 '400ms

'Or in other words: 50000 counts at 125Khz (8µSec per tick) = 50000 * 8µSec = 400mSec = 0.4 sec  
Config Tcd1 = Normal , Prescale = 256  
```
Tcd1_per = 50000 

You could use the overflow for example now as an interrupt (every 400ms) or feed it to the Event System (every 400ms).

Example 2:

The following example configuration counts the incoming events from Event Channel 7. You can use the Tcd0_cnt register to analyze the number of events.

Config Tcd0 = Normal , Prescale = E7 , Event_source = 7 , Event_action = Capture 

Example 3:

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-TIMER-S1.bas  
' This sample demonstrates the TIMER sample 1 from AVR1501  
' This sample uses TIMER TCD0 since TCC0 isused for the UART  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
'include the following lib and code, the routines will be replaced since they are a workaround  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
'connect portE bit 0 and 1 to some LED  
Config Porte = Output  
  
'config timer to normal mode  
Config Tcd0 = Normal , Prescale = 64  
```
Tcd0_per = &H30 ' period register  
  
```vb
Do  
If Inkey() <> 0 Then  
```
Tcd0_per = Tcd0_per + 100 ' increase period  
```vb
Print "period:" ; Tcd0_per ' you will see that a larger PERIOD value will cause the TIMER to

' overflow later and this generating a bigger delay  
End If  
```
Bitwait Tcd0_intflags.0 , Set ' wait for overflow  
Tcd0_intflags.0 = 1 ' clear flag by writing 1  
```vb
Toggle Porte ' toggle led  
Loop

```

---

## CONFIG TIMER0

Action

Configure TIMER0.

Syntax

```vb
CONFIG TIMER0 = COUNTER , EDGE=RISING/FALLING , CLEAR_TIMER = 1|0 [,CONFIGURATION=NAME]

CONFIG TIMER0 = TIMER , PRESCALE= 1|8|64|256|1024 [,CONFIGURATION=NAME]

CONFIG TIMER2 = TIMER | PWM , ASYNC=ON |OFF,PRESCALE = 1 | 8 | 32 | 64 | 128 | 256 | 1024 ,COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,PWM = ON | OFF ,COMPARE_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT ,CLEAR_TIMER = 1|0 [,CONFIGURATION=NAME]

```
Remarks

TIMER0 is an 8 bit counter. See the hardware description of TIMER0.

When configured as a COUNTER:

EDGE | You can select whether the TIMER will count on the falling or rising edge.  
---|---  
  
When configured as a TIMER:

PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024  
---|---  
  
Note that some new AVR chips have different pre scale values. You can use these.

CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

![notice](notice.jpg) Notice that the Help was written with the AT90S2313 and AT90S8515 timers in mind.

When you use the CONFIG TIMER0 statement, the mode is stored by the compiler and the TCCRO register is set.

When you use the STOP TIMER0 statement, the TIMER is stopped.

When you use the START TIMER0 statement, the TIMER TCCR0 register is loaded with the last value that was configured with the CONFIG TIMER0 statement.

So before using the [START](start.md) and [STOP](stop.md) TIMER0 statements, use the CONFIG statement first.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : timer0.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to use TIMER0 related statements

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'First you must configure the timer to operate as a counter or as a timer

'Lets configure it as a COUNTER now

'You must also specify if it will count on a rising or falling edge

Config Timer0 = Counter , Edge = Rising

'Config Timer0 = Counter , Edge = falling

'unremark the line aboven to use timer0 to count on falling edge

'To get/set the value from the timer access the timer/counter register

'lets reset it to 0

```
Tcnt0 = 0

```vb
Do

Print Tcnt0

Loop Until Tcnt0 >= 10

'when 10 pulses are count the loop is exited

'or use the special variable TIMER0

```
Timer0 = 0

```vb
'Now configire it as a TIMER

'The TIMER can have the systemclock as an input or the systemclock divided

'by 8,64,256 or 1024

'The prescale parameter excepts 1,8,64,256 or 1024

Config Timer0 = Timer , Prescale = 1

'The TIMER is started now automaticly

'You can STOP the timer with the following statement :

```
Stop Timer0

```vb
'Now the timer is stopped

'To START it again in the last configured mode, use :

```
Start Timer0

```vb
'Again you can access the value with the tcnt0 register

Print Tcnt0

'or

Print Timer0

'when the timer overflows, a flag named TOV0 in register TIFR is set

'You can use this to execute an ISR

'To reset the flag manual in non ISR mode you must write a 1 to the bit position

'in TIFR:

Set Tifr.1

'The following code shows how to use the TIMER0 in interrupt mode

'The code is block remarked with '( en ')

'(

'Configute the timer to use the clock divided by 1024

Config Timer0 = Timer , Prescale = 1024

'Define the ISR handler

On Ovf0 Tim0_isr

'you may also use TIMER0 for OVF0, it is the same

Enable Timer0 ' enable the timer interrupt

Enable Interrupts 'allow interrupts to occur

Do

'your program goes here

Loop

'the following code is executed when the timer rolls over

```
Tim0_isr:

```vb
Print "*";

Return

')

End

```

---

## CONFIG TIMER1

Action

Configure TIMER1.

Syntax

CONFIG TIMER1 = COUNTER | TIMER | PWM ,

EDGE=RISING | FALLING , PRESCALE= 1|8|64|256|1024 ,

NOISE_CANCEL=0 |1, CAPTURE_EDGE = RISING | FALLING ,

CLEAR_TIMER = 1|0,

COMPARE_A = CLEAR | SET | TOGGLE | DISCONNECT ,

COMPARE_B = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = 8 | 9 10 ,

COMPARE_A_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT

COMPARE_B_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT

[,CONFIGURATION=NAME]

Remarks

The TIMER1 is a 16 bit counter. See the hardware description of TIMER1.

It depends on the chip if COMPARE_B is available or not.

Some chips even have a COMARE_C.

The syntax shown above must be on one line. Not all the options need to be selected.

Here is the effect of the various options.

EDGE | You can select whether the TIMER will count on the falling or rising edge. Only for COUNTER mode.  
---|---  
CAPTURE_ EDGE | You can choose to capture the TIMER registers to the INPUT CAPTURE registers With the CAPTURE_EDGE = FALLING/RISING, you can specify to capture on the falling or rising edge of pin ICP  
NOISE_ CANCELING | To allow noise canceling you can provide a value of 1.  
PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024 PRESCALE can't be used in COUNTER mode.  
  
The TIMER1 also has two compare registers A and B

When the timer value matches a compare register, an action can be performed

COMPARE_A | The action can be: SET will set the OC1X pin CLEAR will clear the OC1X pin TOGGLE will toggle the OC1X pin DISCONNECT will disconnect the TIMER from output pin OC1X  
---|---  
  
And the TIMER can be used in PWM mode.

You have the choice between 8, 9 or 10 bit PWM mode

Also you can specify if the counter must count UP or down after a match to the compare registers

Note that there are two compare registers A and B

PWM | Can be 8, 9 or 10.  
---|---  
COMPARE_A_PWM | PWM compare mode. Can be CLEAR_UP or CLEAR_DOWN  
  
Using COMPARE_A, COMPARE_B, COMPARE_A_PWM or COMPARE_B_PWM will set the corresponding pin for output. When this is not desired you can use the alternative NO_OUTPUT version that will not alter the output pin.

For example : COMPARE_A_NO_OUTPUT , COMPARE_A_PWM NO_OUTPUT

CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : timer1.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show using Timer1

'micro : 90S8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8515def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim W As Word

'The TIMER1 is a versatile 16 bit TIMER.

'This example shows how to configure the TIMER

'First like TIMER0 , it can be set to act as a TIMER or COUNTER

'Lets configure it as a TIMER that means that it will count and that

'the input is provided by the internal clock.

'The internal clock can be divided by 1,8,64,256 or 1024

Config Timer1 = Timer , Prescale = 1024

'You can read or write to the timer with the COUNTER1 or TIMER1 variable

```
W = Timer1

Timer1 = W

```vb
'To use it as a COUNTER, you can choose on which edge it is trigereed

Config Timer1 = Counter , Edge = Falling 

'Config Timer1 = Counter , Edge = Rising

'Also you can choose to capture the TIMER registers to the INPUT CAPTURE registers

'With the CAPTURE EDGE = , you can specify to capture on the falling or rising edge of

'pin ICP

Config Timer1 = Counter , Edge = Falling , Capture_Edge = Falling 

'Config Timer1 = Counter , Edge = Falling , Capture Edge = Rising

'To allow noise canceling you can also provide :

Config Timer1 = Counter , Edge = Falling , Capture_Edge = Falling , Noise_Cancel = 1 

'to read the input capture register :

```
W = Capture1

'to write to the capture register :

Capture1 = W

```vb
'The TIMER also has two compare registers A and B

'When the timer value matches a compare register, an action can be performed

Config Timer1 = Counter , Edge = Falling , Compare_A = Set , Compare_B = Toggle , Clear_Timer = 1

'SET , will set the OC1X pin

'CLEAR, will clear the OC1X pin

'TOGGLE, will toggle the OC1X pin

'DISCONNECT, will disconnect the TIMER from output pin OC1X

'CLEAR TIMER will clear the timer on a compare A match

'To read write the compare registers, you can use the COMPARE1A and COMPARE1B variables

```
Compare1a = W

W = Compare1a

```vb
'And the TIMER can be used in PWM mode

'You have the choice between 8,9 or 10 bit PWM mode

'Also you can specify if the counter must count UP or down after a match

'to the compare registers

'Note that there are two compare registers A and B

Config Timer1 = Pwm , Pwm = 8 , Compare_A_Pwm = Clear_Up , Compare_B_Pwm = Clear_Down , Prescale = 1

'to set the PWM registers, just assign a value to the compare A and B registers

```
Compare1a = 100

Compare1b = 200

'Or for better reading :

Pwm1a = 100

Pwm1b = 200

End

---

## CONFIG TIMER2

Action

Configure TIMER2.

Syntax for the 8535

CONFIG TIMER2 = TIMER | PWM , ASYNC=ON |OFF,

PRESCALE = 1 | 8 | 32 | 64 | 128 | 256 | 1024 ,

COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = ON | OFF ,

COMPARE_PWM = CLEAR_UP| CLEAR_DOWN | DISCONNECT ,

CLEAR_TIMER = 1|0

[,CONFIGURATION=NAME]

Syntax for the M103

CONFIG TIMER2 = COUNTER| TIMER | PWM ,

EDGE= FALLING |RISING,

PRESCALE = 1 | 8 | 64 | 256 | 1024 ,

COMPARE = CLEAR | SET | TOGGLE | DISCONNECT ,

PWM = ON | OFF ,

COMPARE_PWM = CLEAR UP| CLEAR DOWN | DISCONNECT ,

CLEAR _TIMER = 1|0

[,CONFIGURATION=NAME]

Remarks

The TIMER2 is an 8 bit counter.

It depends on the chip if it can work as a counter or not.

The syntax shown above must be on one line. Not all the options need to be selected.

Some chips support multiple COMPARE outputs. Use COMPARE_A, COMPARE_B, COMPARE_C , etc.

Here is the effect of the various options.

EDGE | You can select whether the TIMER will count on the falling or rising edge. Only for COUNTER mode.  
---|---  
  
PRESCALE | The TIMER is connected to the system clock in this case. You can select the division of the system clock with this parameter. Valid values are 1 , 8, 64, 256 or 1024 or 1 , 8, 32 , 64 , 256 or 1024 for the M103 Prescale can not be used in COUNTER mode.  
---|---  
  
The TIMER2 also has a compare registers

When the timer value matches a compare register, an action can be performed

COMPARE | The action can be: SET will set the OC2 pin CLEAR will clear the OC2 pin TOGGLE will toggle the OC2 pin DISCONNECT will disconnect the TIMER from output pin OC2  
---|---  
  
And the TIMER can be used in 8 bit PWM mode

You can specify if the counter must count UP or down after a match to the compare registers

COMPARE PWM | PWM compare mode. Can be CLEAR_UP or CLEAR_DOWN  
---|---  
  
CONFIGURATION is optional. When you add configuration=mysetting, you can use this setting when you start the timer : START TIMER0 , mysetting

If you have multiple settings, you can start the timer with these different settings.

Example

```vb
Dim W As Byte

Config Timer2 = Timer , ASYNC = 1 , Prescale = 128

On TIMER2 Myisr

ENABLE INTERRUPTS

ENABLE TIMER2

DO

LOOP

```
MYISR:

```vb
'get here every second with a 32768 Hz xtal

RETURN

'You can read or write to the timer with the COUNTER2 or TIMER2 variable

```
W = Timer2

Timer2 = W

---

## CONFIG TWI, TWIx

Action

Configure the TWI (two wire serial interface) when using hardware I2C/TWI.

Syntax

```vb
CONFIG TWI = clockspeed

CONFIG TWI1 = clockspeed

```
Syntax XMEGA

CONFIG TWIC | TWID | TWIE | TWIF = clockspeed

(Config TWI and TWI1 is for ATMEGA and Config TWIX is for ATXMEGA chips)

Syntax XTINY

CONFIG TWI|TWI0|TWI1 = clockspeed

The XTINY uses TWI0. TWI and TWI0 are similar and can be exchanged. For devices with an additional TWI interface you can use TWI1.

Remarks

clockspeed | The desired clock frequency for SCL  
---|---  
  
CONFIG TWI will set TWSR pre scaler bits 0 and 1, and TWBR depending on the used [$CRYSTAL](crystal_1.md) frequency and the desired SCL clock speed.

Typical you need a speed of 400 KHz. Some devices will work on 100 KHz as well.

When TWI is used in SLAVE mode, you need to have a faster clock speed as the master.

![notice](notice.jpg)There is no dynamic channel support for I2C

![notice](notice.jpg) To use the hardware I2C routines and not the Software I2C routines you need to use the $lib "i2c_twi.lbx"! (NOT FOR XMEGA/XTINY)

XMEGA

The XMEGA can contain up to 4 TWI units. When not specifying TWIC, TWID, TWIE or TWIF, the TWIC will be used as the default. 

Because the XMEGA can contains multiple TWI busses, a channel identifier MUST be used when addressing TWID,TWIE or TWIF.

This means that your normal I2C code is fully compatible but only with TWIC. Thus omitting the channel identifiers, will automatically use TWIC.

You MUST dimension a variable named TWI_START as a byte. It is used by the xmega TWI library code. Without it, you will get an error.

There are 2 manuals available from ATMEL for every ATXMEGA Chip

1.| One Family Manual like for example for a ATXMEGA128A1 it is Atmel AVR XMEGA A Manual  
---|---  
  
2.| Another Manual for the single chips like for example for an ATXMEGA128A1 it is the ATxmega64A1/128A1/192A1/256A1/384A1 Manual. In this Manual you find for example the Alternate Pin Functions. So you can find which Pin on Port C is the SDA and SCL Pin when you want to use the I2C/TWI Interface of this Port.  
---|---  
  
![notice](notice.jpg) It is important that you specify the proper crystal frequency. Otherwise it will result in a wrong TWI clock frequency.

XTINY

The XTINY can contain up to 2 TWI units. 

Because the XTINY can contains multiple TWI busses, a channel identifier MUST be used when addressing TWI1 or up. 

This means that your normal I2C code is fully compatible but only with TWI/TWI0. Thus omitting the channel identifiers, will automatically use TWI0.

You MUST dimension a variable named TWI_START as a byte. It is used by the xtiny TWI library code. Without it, you will get an error.

Some processors support multiple TWI interfaces like the MEGA328PB. Use CONFIG TWI1 to configure the second TWI named TWI1. The first TWI which is named TWI0 is referred to as TWI.

See also

[$CRYSTAL](crystal_1.md) , [OPEN](open.md), [Using the I2C protocol](using_the_i2c_protocol.md), [I2CINIT](i2cinit.md)

Example using Hardware I2C Pin's over Library: i2c_twi.lbx

```vb
'-----------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' This demo shows an example of the TWI  
' Not all AVR chips have TWI (hardware I2C)  
'------------------------------------------------------------------------  
  
'The chip will work in TWI/I2C master mode  
'Connected is a PCF8574A 8-bits port extender  
  
  
$regfile="M8def.dat"' the used chip  
$crystal= 4000000 ' frequency used  
$baud = 19200 ' baud rate  
$hwstack = 40  
$swstack = 30  
$framesize = 40  
  
  
$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI  
Config Scl = Portc.5 ' we need to provide the SCL pin name  
Config Sda = Portc.4 ' we need to provide the SDA pin name  
```
I2cinit ' we need to set the pins in the proper state  
  
```vb
'On the Mega8, On the PCF8574A  
'scl=PC5 , pin 28 pin 14  
'sda=PC4 , pin 27 pin 15  
  
Config Twi = 100000 ' wanted clock frequency when using $lib "i2c_twi.lbx"   
'will set TWBR and TWSR  
'Twbr = 12 'bit rate register  
'Twsr = 0 'pre scaler bits  
  
Dim B As Byte , X As Byte  
Print "TWI master"  
  
Do  
```
Incr B ' increase value  
I2csend &B01110000 , B ' send the value  
Print "Error : " ; Err ' show error status  
I2creceive &B01110000 , X ' get a byte  
```vb
Print X ; " " ; Err ' show error  
Waitms 500 ' wait a bit  
Loop  
End

```
XMEGA SAMPLE

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-TWI.bas  
' This sample demonstrates the Xmega128A1 TWI  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
Dim S As String * 20  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Dim N As String * 16 , B As Byte  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Config Input1 = Cr , Echo = Crlf ' CR is used for input, we echo back CR and LF  
  
```
Open "COM1:" For Binary As #1  
```vb
' ^^^^ change from COM1-COM8  
  
Print #1 , "Xmega revision:" ; Mcu_revid ' make sure it is 7 or higher !!! lower revs have many flaws  
  
```
Const Usechannel = 1  
  
  
```vb
Dim B1 As Byte , B2 As Byte  
Dim W As Word At B1 Overlay  
  
  
```
Open "twic" For Binary As #4 ' or use TWID,TWIE oR TWIF  
```vb
Config Twic = 100000 'CONFIG TWI will ENABLE the TWI master interface  
'you can also use TWIC, TWID, TWIE of TWIF  
'!!!!!!!!!!! WITHOUT a channel identifier, TWIC will be used !!!!!!!!!!!!!!  
  

#if Usechannel = 1  
```
I2cinit #4  

#else  
I2cinit  

```vb
#endif  
  
  
Do  
```
I2cstart 'since not # is used, TWIC will be used  
Waitms 20  
I2cwbyte &H70 ' slave address write  
Waitms 20  
I2cwbyte &B10101010 ' write command  
Waitms 20  
I2cwbyte 2  
Waitms 20  
I2cstop  
```vb
Print "Error : " ; Err ' show error status  
  
'waitms 50  
Print "start"  
```
I2cstart  
Print "Error : " ; Err ' show error  
I2cwbyte &H71  
Print "Error : " ; Err ' show error  
I2crbyte B1 , Ack  
Print "Error : " ; Err ' show error  
I2crbyte B2 , Nack  
Print "Error : " ; Err ' show error  
I2cstop  
```vb
Print "received A/D : " ; W ; "-" ; B1 ; "-" ; B2  
Waitms 500 'wait a bit  
Loop  
  
  
  
Dim J As Byte , C As Byte , K As Byte  
Dim Twi_start As Byte ' you MUST dim this variable since it is used by the lib  
  
'determine if we have an i2c slave on the bus  
For J = 0 To 200 Step 2  
Print J  

#if Usechannel = 1  
```
I2cstart #4  

#else  
I2cstart  

#endif  
  
I2cwbyte J  
```vb
If Err = 0 Then ' no errors  
Print "FOUND : " ; Hex(j)  
'write some value to the pcf8574A  

#if Usechannel = 1  
```
I2cwbyte &B1100_0101 , #4  

#else  
I2cwbyte &B1100_0101  

```vb
#endif  
Print Err  
Exit For  
End If  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
Next  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
  

#if Usechannel = 1  
```
I2cstart #4  
I2cwbyte &H71 , #4 'read address  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack , #4  
Print Bin(j) ; " err:" ; Err  
I2cstop #4  

#else  
I2cstart  
I2cwbyte &H71 'read address  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack  
Print Bin(j) ; " err:" ; Err  
I2cstop  

```vb
#endif  
  
'try a transaction  

#if Usechannel = 1  
```
I2csend &H70 , 255 , #4 ' all 1  
Waitms 1000  
I2csend &H70 , 0 , #4 'all 0  

#else  
I2csend &H70 , 255  
Waitms 1000  
I2csend &H70 , 0  

```vb
#endif  
Print Err  
  
  
'read transaction  
Dim Var As Byte  
```
Var = &B11111111  

#if Usechannel = 1  
I2creceive &H70 , Var , 1 , 1 , #4 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 , #4 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#else  
```
I2creceive &H70 , Var , 1 , 1 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#endif  
  
End

```
XTINY SAMPLE

```vb
'------------------------------------------------------------------  
' (c) 1995-2025 MCS  
' xtiny-TWI-scanner.bas  
'purpose : scan all i2c addresses to find slave chips  
'Micro: tiny816  
'------------------------------------------------------------------  
$regfile = "atxtiny816.dat" ' the used chip  
$crystal = 20000000 ' frequency used  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Config Sysclock = 20mhz , Prescale = 1  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Waitms 3000 'small delay  
Print "XTINY:" ; Hex(rstctrl_rstfr) 'print reset cause  
  
Config Twi0 = 100000 'CONFIG TWI will ENABLE the TWI master interface  
```
I2cinit  
  
```vb
Dim Twi_start As Byte , B As Byte  
Do  
Print "Scan start"  
For B = 0 To 254 Step 2 'for all odd addresses  
```
I2cstart 'send start  
I2cwbyte B 'send address  
```vb
If Err = 0 Then 'we got an ack  
Print "Slave at : " ; B ; " hex : " ; Hex(b) ; " bin : " ; Bin(b)  
End If  
```
I2cstop 'free bus  
```vb
Next  
Print "End Scan"  
Waitms 2000 'some delay and then repeat  
Loop

```

---

## CONFIG TWISLAVE

Action

Configure the TWI Slave address and bit rate

Syntax

CONFIG TWISLAVE = address , BTR = value , BITRATE = value , SAVE=option [,GENCALL=value] [,USERACK=ack]

(I2C TWI Slave is part of the I2C-Slave library. This is an add-on library that is not included in Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

See also: [I2C TWI Slave](i2ctwislave.md), [USING I2C Protocol](using_the_i2c_protocol.md), [Using USI](using_usi_universal_serial_int.md), [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md)

Remarks

Address | The slave address that is assigned to the slave chip. This must be an Even number. Bit 0 of the address is used to activate the general call address. The GENCAL option will set this bit automatic. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
BTR | Bytes to receive. With this constant you specify how many bytes will be expected when the master reads data from the slave. And thus how many bytes will be sent to the master.  
Bit rate | This is the I2C/TWI clock frequency. Most chips support 400 KHz (400000) but all I2C chips support 100000.  
SAVE | SAVE = NOSAVE : this can be used when you do not change a lot of registers in the interrupt. SAVE = SAVE : this is best to be used when you do not use ASM in the TWI interrupt. See the explanation below. When you do not specify SAVE, the default will be SAVE=SAVE.  
GENCALL | General call address activated or not. When you specify 1 or YES, the General call address will be activated which mean that the slave will respond not only to it's own address, but also to the general call address 0.  When you omit the option or specify 0 or NO, the general call address will not be honored.   
USERACK | Default is OFF. When you use ON, an alternative library will be used. This library will create a variable named TWI_ACK.  Each time your code is called this variable is filled with the value 255. If you do not alter the value, the slave will send an ACK as it is supposed to. If you reset the value to 0, the slave will send a NACK. You can use this to send data with variable length to the slave. In this case, BTR only serves as an index. You must make sure to reset TWI_ACK when you have send the last byte to the master.  
  
The variables Twi , Twi_btr and Twi_btw are created by the compiler. These are all bytes

The TWI interrupt is enabled but you need to enabled the global interrupt

The TWI Slave code is running as an interrupt process. Each time there is a TWI interrupt some slave code is executed. Your BASIC code is called from the low level slave code under a number of events. You must include all these labels in your Slave application. You do not need to write code in all these sub routines. All the time your user code is executed, the clock line is stretched. This will reduce the TWI bus speed. So it is important that you do not put delays in your code. 

Label | Event  
---|---  
Twi_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata | The master has sent data. The variable TWI holds the received value. The byte TWI_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte | The master reads from the slave and needs a value. The variable TWI_BTR can be inspected to see which index byte was needed. With the CONFIG BTR, you specify how many bytes the master will read.  
  
In most cases your main application is just an empty DO LOOP. But when you write a slave that performs other tasks on the background these other tasks are interrupted by the TWI traffic.

Take in mind that the interrupt with the lowest address has the highest priority.

So do NOT write blocking code inside an interrupt. While servicing another interrupt, the TWI interrupt can not be serviced.

The TWI Slave code will save all used registers.

But since it will call your BASIC application when the TWI interrupt occurs, your BASIC code could be in the middle of say a PRINT statement.

When you then execute another PRINT statement , you will destroy registers.

So keep the code in the sub routines to a minimum, and use SAVE option to save all registers. This is the default.

While two printing commands will give odd results (print 12345 and 456 in the middle of the first print will give 1234545) at least no register is destroyed.

A typical configuration is shown below.

![i2c_slave](i2c_slave.png)

To test the above hardware, use the samples : twi-master.bas and twi-slave.bas

Optional you can use i2cscan.bas to test the general call address.

When you want to change the address of the slave at run time you need to write to the TWAR register.

The TWAR register contains the slave address. Bit 0 which is used to indicate a read or write transaction should be cleared. When you set it, the slave will also recognize the general call address. The GENCALL option just sets bit 0 of the slave.

See also

[CONFIG TWI](config_twi.md) , [CONFIG SCL](config_scl.md) , [CONFIG SDA](config_sda.md) , [I2C TWI Slave](i2ctwislave.md), [Using the I2C protocol](using_the_i2c_protocol.md)

ASM

NONE

Example1(master)

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This demo shows an example of the TWI

' Not all AVR chips have TWI (hardware I2C)

'-------------------------------------------------------------------------------

'The chip will work in TWI/I2C master mode

'Connected is a PCF8574A 8-bits port extender

$regfile = "M88def.dat" ' the used chip

$crystal = 8000000 ' frequency used

$baud = 19200 ' baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "i2c_twi.lbx" ' we do not use software emulated I2C but the TWI

Config Scl = Portc.5 ' we need to provide the SCL pin name

Config Sda = Portc.4 ' we need to provide the SDA pin name

'On the Mega88, On the PCF8574A

'scl=PC5 , pin 28 pin 14

'sda=PC4 , pin 27 pin 15

```
I2cinit ' we need to set the pins in the proper state

```vb
Config Twi = 100000 ' wanted clock frequency

'will set TWBR and TWSR

'Twbr = 12 'bit rate register

'Twsr = 0 'pre scaler bits

Dim B As Byte , X As Byte

Print "TWI master"

Do

```
Incr B ' increase value

I2csend &H0 , B ' send the value to general call address

I2csend &H70 , B ' send the value

Print "Error : " ; Err ' show error status

I2creceive &H70 , X ' get a byte

```vb
Print X ; " " ; Err ' show error

Waitms 500 'wait a bit

Loop

End

```
Example2(slave)

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This demo shows an example of the TWI in SLAVE mode

' Not all AVR chips have TWI (hardware I2C)

' IMPORTANT : this example ONLY works when you have the TWI slave library

' which is a commercial add on library, not part of BASCOM

'Use this sample in combination with i2cscan.bas and/or twi-master.bas

'-------------------------------------------------------------------------------

$regfile = "M88def.dat" ' the chip we use

$crystal = 8000000 ' crystal oscillator value

$baud = 19200 ' baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Print "MCS Electronics TWI-slave demo"

Config Twislave = &H70 , Btr = 1 , Bitrate = 100000 , Gencall = 1

'In i2c the address has 7 bits. The LS bit is used to indicate read or write

'When the bit is 0, it means a write and a 1 means a read

'When you address a slave with the master in bascom, the LS bit will be set/reset automatic.

'The TWAR register in the AVR is 8 bit with the slave address also in the most left 7 bits

'This means that when you setup the slave address as &H70, TWAR will be set to &H0111_0000

'And in the master you address the slave with address &H70 too.

'The AVR TWI can also recognize the general call address 0. You need to either set bit 0 for example

'by using &H71 as a slave address, or by using GENCALL=1

'as you might need other interrupts as well, you need to enable them all manual

Enable Interrupts

'this is just an empty loop but you could perform other tasks there

Do

```
nop

```vb
Loop

End

'A master can send or receive bytes.

'A master protocol can also send some bytes, then receive some bytes

'The master and slave must match.

'the following labels are called from the library

```
Twi_stop_rstart_received:

```vb
Print "Master sent stop or repeated start"

Return

```
Twi_addressed_goread:

```vb
Print "We were addressed and master will send data"

Return

```
Twi_addressed_gowrite:

```vb
Print "We were addressed and master will read data"

Return

'this label is called when the master sends data and the slave has received the byte

'the variable TWI holds the received value

```
Twi_gotdata:

```vb
Print "received : " ; Twi

Return

'this label is called when the master receives data and needs a byte

'the variable twi_btr is a byte variable that holds the index of the needed byte

'so when sending multiple bytes from an array, twi_btr can be used for the index

```
Twi_master_needs_byte:

Print "Master needs byte : " ; Twi_btr

Twi = 65 ' twi must be filled with a value

```vb
Return

'when the mast has all bytes received this label will be called

```
Twi_master_need_nomore_byte:

```vb
Print "Master does not need anymore bytes"

Return

```

---

## CONFIG TWIxSLAVE

Action  
  
Configure the Xmega TWIC,TWID,TWIE or TWIF hardware to be used a a slave.

Syntax

```vb
CONFIG TWICSLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIDSLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIESLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIFSLAVE = address , BTR = value ,GENCALL=value

```
(I2C TWI Slave is part of the I2C-Slave library. This is an add-on library which is not included with Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

See also: [I2C TWI Slave](i2ctwislave.md), [USING I2C Protocol](using_the_i2c_protocol.md), [Using USI](using_usi_universal_serial_int.md), [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md)

Remarks

Address | The slave address which is assigned to the slave chip. This must be an Even number. Bit 0 of the address is used to activate the general call address. The GENCAL option will set this bit automatic. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
BTR | Bytes to receive. With this constant you specify how many bytes will be expected when the master reads data from the slave. And thus how many bytes will be sent to the master. This value can be changed dynamically.  
GENCALL | General call address activated or not. When you specify 1, the General call address will be activated which mean that the slave will respond not only to it's own address, but also to the general call address 0.  When you omit the option or specify 0, the general call address will not be honored.   
  
The variables TwiX , TwiX_btr, TwiX_CBTR and TwiX_btw are created by the compiler. These are all byte variables.

The X represents the TWI interface letter which can be C, D, E or F.

The TWIx interrupt is enabled as well but you need to enabled the global interrupt

The TWI Slave code is running as an interrupt process. Each time there is a TWI interrupt some slave code is executed. Your BASIC code is called from the low level slave code by a number of events. You must include all these labels in your Slave application. You do not need to write code in all these sub routines.

Label | Event  
---|---  
Twi_stop_rstart_received TwiD_stop_rstart_received TwiE_stop_rstart_received TwiF_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread TwiD_addressed_goread TwiE_addressed_goread TwiF_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite TwiD_addressed_gowrite TwiE_addressed_gowrite TwiF_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata TwiD_gotdata TwiE_gotdata TwiF_gotdata | The master has sent data. The variable TWIx holds the received value. The byte TWIx_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte TwiD_master_needs_byte TwiE_master_needs_byte TwiF_master_needs_byte | The master reads from the slave and needs a value. The variable TWIx_BTR can be inspected to see which index byte was requested. With the CONFIG parameter BTR, you specify how many bytes the master will read. This value is stored in the variable TWIx_CBTR. You can alter this value but you should not do that in the middle of a transaction.  
  
The name of the label called depends on the used TWI interface. TWIC is the default TWI interface. All I2C commands work with TWIC by default.

In order to make the normal slave code compatible with the Xmega, the TWIC interface uses the same label names as used for normal AVR TWI interface.

This means that your BASCOM slave code for the M32 should work for the TWIC interface without much changes.

![notice](notice.jpg)It is important that you do not use the MASTER TWI routines when using the TWI as a slave. Just supply or read data at the provided routines.

In most cases your main application is just an empty DO LOOP. But when you write a slave that performs other tasks on the background these other tasks are interrupted by the TWI traffic.

Do NOT write blocking code inside an interrupt. While servicing another interrupt, the TWI interrupt can not be serviced.

Also, do not block execution by putting delays in the called routines such as TWI_GOTDATA. All these labels are called from the TWIX SLAVE library which is an interrupt routine that will halt the main application and other interrupts.

The TWI Slave code will save all used registers.

In order to get a working slave it is important that the slave matches the protocol used by the master. Thus if the slave reads data from the master and only expects 2 bytes, the master should not send less or more. We advise to make a simple slave first like a PCF8574 clone.

See also

[CONFIG TWIX](config_twi.md)

Example

The following example uses two TWI interfaces. TWID is used in master mode while TWIC is used as the slave.

```vb
'------------------------------------------------------------------------------  
'name : xmega-twi-slave.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Xmega TWI slave add on  
'micro : Xmega128A1  
'suited for demo : yes  
'commercial addon needed : yes  
'------------------------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
'Config Serialin = Buffered , Size = 50  
  
'Enable Interrupts  
```
Open "COM1:" For Binary As #1  
  
Open "twid" For Binary As #4 ' or use TWIC,TWIE oR TWIF  
```vb
Config Twid = 100000 'CONFIG TWI will ENABLE the TWI master interface  
'you can also use TWIC, TWID, TWIE of TWIF  
'!!!!!!!!!!! WITHOUT a channel identifier, TWIC will be used !!!!!!!!!!!!!!  
'SCL is on pin 1  
'SDA is on pin 0  
'This demo uses TWID as master and TWIC as SLAVE  
'Thus portc.0 connects with portD.0 and  
' portc.1 connects with portD.1  
  
'The TWIC when used as a slave has megaAVR compatible labels  
'The TWID,TWIE and TWIF have unique new labelnames  
'These labels are the labels in your code which are called from the slave ISR.  
'For example : Twi_addressed_gowrite is named TwiD_addressed_gowrite for TWID  
  
  
Dim Twi_start As Byte , j as byte , b as byte  
```
I2cinit #4 'init the master  
```vb
config TWIcslave = &H70 , btr = 2 'use address &H70 which is &H38 in 7-bit i2c notation  
  
Enable INTERRUPTS 'for the slave to work we must enable global interrupts  
  
do  
Print #1 , "test xmega"  
  
For J = 0 To 120 Step 1 'notice that we scan odd and even addresses  
```
I2cstart #4 'send start  
I2cwbyte J , #4 'send value of J  
```vb
If Err = 0 Then ' no errors  
Print #1 , "FOUND : " ; Hex(j)  
if j.0 = 0 then 'ONLY if R/W bit is not set we may write data !!!  
```
I2cwbyte 100 , #4 'just write to values to the slave  
I2cwbyte 101 , #4  
else 'read  
I2crbyte b , Ack , #4 : print #1 , "GOT : " ; b 'read 2 bytes  
I2crbyte b , nAck , #4 : print #1 , "GOT : " ; b  
```vb
end if  
End If  
```
I2cstop #4 'done  
```vb
Next  
waitms 2000 'wait some time  
loop  
  
  
'the following labels are called from the library when master send stop or start  
'notice that these label names are valid for TWIC.  
'for TWID the name would be TWID_stop_rstart_received:  
```
Twi_stop_rstart_received:  
```vb
Print #1 , "Master sent stop or repeated start"  
Return  
  
'master sent our slave address and will not send data  
```
Twi_addressed_goread:  
```vb
Print #1 , "We were addressed and master will send data"  
Return  
  
  
```
Twi_addressed_gowrite:  
```vb
Print #1 , "We were addressed and master will read data"  
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWIx holds the received value  
'The x is the TWI interface letter  
```
Twi_gotdata:  
```vb
Print #1 , "received : " ; Twic ; " byte no : " ; Twic_btw  
'here you would do something with the received data  
' Select Case Twic_btw  
' Case 1 : Portb = Twi ' first byte  
' Case 2: 'you can set another port here for example  
' End Select   
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twix_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twix_btr can be used for the index  
'again the variable name depends on the twi interface  
```
Twi_master_needs_byte:  
```vb
Print #1 , "Master needs byte : " ; Twic_btr  
Select Case Twic_btr  
Case 1: ' first byte  
```
twic = 66 'we assign a value but this could be any value you want  
Case 2 ' send second byte  
twic = 67  
```vb
End Select  
Return  
  
  
'when the mast has all bytes received this label will be called  
```
Twi_master_need_nomore_byte:  
```vb
Print #1 , "Master does not need anymore bytes"  
Return  
  
End

```

---

## CONFIG USB

Action

Create settings related to USB.

Syntax

CONFIG USB = dev, Language= lang, Manufact= "man", Product="prod" , Serial="serial"

Remarks

Dev | The possible options are Device and Host. Host is not supported yet.  
---|---  
Lang | A language identifier. &H0409 for US/English  
Man | A string constant with the manufacture name.   
Prod | A string constant with the product name.  
Serial  | A string constant with the serial number.  
  
The above settings determine how your device is displayed by the operating system.

Since these settings end up in flash code space, it is best to chose short names. There is no limit to the length other then the USB specifications impose, but keep it short as possible. Strings in USB are UNI coded. Which mean that a word is used for each character. with normal ASCII coding, only a byte is used for each character.

For a commercial USB device you need to give it a unique VID & PID combination. When you plan to use it at home, this is not needed.

You can buy a Vendor ID (VID) from the USB organization. This cost 2000 $.

As a service MCS offers a PID in the on line shop. This cost little and it gives you a unique Product ID(PID) but with the MCS Electronics VID.

![notice](notice.jpg)Notice that using CONFIG USB will include a file named USBINC.BAS. This file is not part of the BASCOM setup/distribution. It is available as a commercial add on. The add on package includes 3 samples , the include file, and a special activeX for the HID demo.

None of the samples require a driver. A small UB162 module with normal pins is available from the on line shop too.

The first supported USB devices are USB1287, USB162.

See also

NONE

Example

```vb
$regfile = "usb162.dat"

$crystal = 8000000

$baud = 19200

```
Const Mdbg = 1

```vb
Config Clockdiv = 1

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Const Vendor_id = &H16D0 ' MCS Vendor ID

Const Product_id = &H201D ' MCS product ID, you can buy a VID&PID in the MCS shop

Const Ep_control_length = 32

Const User_conf_size = 41

Const Size_of_report = 53

Const Device_class = 0

Const Device_sub_class = 0

Const Device_protocol = 0

Const Release_number = &H1000

Const Length_of_report_in = 8

Const Length_of_report_out = 8

Const Interface_nb = 0

Const Alternate = 0

Const Nb_endpoint = 2

Const Interface_class = 3 ' HID

Const Interface_sub_class = 0

Const Interface_protocol = 0

Const Interface_index = 0

```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Print "USB GENERIC test"

Declare Sub Usb_user_endpoint_init

Declare Sub Hid_test_hit()

Declare Sub Hid_task()

Declare Sub Hid_task_init()

```
Const Usb_config_attributes_reserved = &H80

Const Usb_config_buspowered = Usb_config_attributes_reserved

Const Usb_config_selfpowered = Usb_config_attributes_reserved Or &H40

Const Usb_config_remotewakeup = Usb_config_attributes_reserved Or &H20

Const Nb_interface = 1

Const Conf_nb = 1

Const Conf_index = 0

Const Conf_attributes = Usb_config_buspowered

Const Max_power = 50 ' 100 mA

Const Interface_nb_mouse = 0

Const Alternate_mouse = 0

Const Nb_endpoint_mouse = 1

Const Interface_class_mouse = 3 ' HID Class

Const Interface_sub_class_mouse = 1 ' Sub Class is Mouse

Const Interface_protocol_mouse = 2 ' Mouse

Const Interface_index_mouse = 0

Const Nb_endpoints = 2 ' number of endpoints in the application including control endpoint

Const Ep_kbd_in = 1 ' Number of the mouse interrupt IN endpoint

Const Ep_hid_in = 1

Const Ep_hid_out = 2

Const Endpoint_nb_1 = Ep_hid_in Or &H80

Const Ep_attributes_1 = 3 ' BULK = 0x02, INTERUPT = 0x03

Const Ep_in_length_1 = 8

Const Ep_size_1 = Ep_in_length_1

Const Ep_interval_1 = 20 ' Interrupt polling interval from host

Const Endpoint_nb_2 = Ep_hid_out

Const Ep_attributes_2 = 3 ' BULK = 0x02, INTERUPT = 0x03

Const Ep_out_length = 8

Const Ep_size_2 = Ep_out_length

Const Ep_interval_2 = 20 ' interrupt polling from host

```vb
Config Usb = Device , Language = &H0409 , Manufact = "MCS" , Product = "MCSHID162" , Serial = "MC0001"

'Dim some user vars

Dim Usb_kbd_state As Byte , Usb_key As Byte , Usb_data_to_send As Byte

Dim Dummy As Byte , Dummy1 As Byte , Dummy2 As Byte

Print "task init"

```
Usb_task_init

Hid_task_init

Do

Usb_task

Hid_task

```vb
'you can call your sub program here

Loop

'nothing needed to init

Sub Hid_task_init()

'nothing

end sub

'HID task must be checked regular

Sub Hid_task()

If Usb_connected = 1 Then ' Check USB HID is enumerated

```
Usb_select_endpoint Ep_hid_out ' Get Data Repport From Host

If Ueintx.rxouti = 1 Then ' Is_usb_receive_out())

Dummy1 = Uedatx : Print "Got : " ; Dummy1

Dummy2 = Uedatx : Print "Got : " ; Dummy2

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Usb_ack_receive_out

```vb
End If

If Dummy1 = &H55 And Dummy2 = &HAA Then ' Check if we received DFU mode command from host

```
Usb_detach ' Detach Actual Generic Hid Application

```vb
Waitms 500

Goto &H1800 'goto bootloader

'here you could call the bootloader then

End If

```
Usb_select_endpoint Ep_hid_in ' Ready to send these information to the host application

If Ueintx.txini = 1 Then ' Is_usb_in_ready())

Uedatx = 1

Uedatx = 2

Uedatx = 3

Uedatx = 4

Uedatx = 5

Uedatx = 6

Uedatx = 7

Uedatx = 8

Usb_ack_fifocon ' Send data over the USB

```vb
End If

End If

End Sub

Function Usb_user_read_request(type As Byte , Request As Byte) As Byte

#if Mdbg

Print "USB_USER_READ_REQ"

#endif

```
Usb_string_type = Uedatx 'Usb_read_byte();

Usb_descriptor_type = Uedatx 'Usb_read_byte();

Usb_user_read_request = 0

```vb
Select Case Request

Case Get_descriptor:

Select Case Usb_descriptor_type

Case Report : Call Hid_get_report()

```
Usb_user_read_request = 1

Case Hid : Call Hid_get_hid_descriptor()

Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

Case Set_configuration:

Select Case Usb_descriptor_type

Case Set_report : Call Hid_set_report()

```
Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

Case Get_interface:

'// usb_hid_set_idle();

```
Call Usb_hid_get_interface()

Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

End Function

'usb_init_device.

'This function initializes the USB device controller and

'configures the Default Control Endpoint.

Sub Usb_init_device()

#if Usbfunc

```
Usb_select_device

```vb
#endif

#if Usbfunc

If Usbsta.id = 1 Then 'is it an USB device?

#endif

```
Uenum = Ep_control ' select USB endpoint

If Ueconx.epen = 0 Then ' usb endpoint not enabled yet

Call Usb_configure_endpoint(ep_control , Type_control , Direction_out , Size_32 , One_bank , Nyet_disabled)

```vb
End If

#if Usbfunc

End If

#endif

End Sub

Sub Usb_user_endpoint_init(byval Nm As Byte)

```
Call Usb_configure_endpoint(ep_hid_in , Type_interrupt , Direction_in , Size_8 , One_bank , Nyet_enabled)

Call Usb_configure_endpoint(ep_hid_out , Type_interrupt , Direction_out , Size_8 , One_bank , Nyet_enabled)

End Sub

Usb_dev_desc:

Data 18 , Device_descriptor 'size and device_descriptor

Data 0 , 2 'Usb_write_word_enum_struc(USB_SPECIFICATION)

Data Device_class , Device_sub_class ' DEVICE_CLASS and DEVICE_SUB_CLASS

Data Device_protocol , Ep_control_length ' device protol and ep_control_length

Data Vendor_id% ' Usb_write_word_enum_struc(VENDOR_ID)

Data Product_id% ' Usb_write_word_enum_struc(PRODUCT_ID)

Data Release_number% ' Usb_write_word_enum_struc(RELEASE_NUMBER)

Data Man_index , Prod_index ' MAN_INDEX and PROD_INDEX

Data Sn_index , Nb_configuration ' SN_INDEX and NB_CONFIGURATION

Usb_conf_desc:

Data 9 , Configuration_descriptor ' length , CONFIGURATION descriptor

Data User_conf_size% ' total length of data returned

Data Nb_interface , Conf_nb ' number of interfaces for this conf. , value for SetConfiguration resquest

Data Conf_index , Conf_attributes ' index of string descriptor , Configuration characteristics

Data Max_power ' maximum power consumption

Data 9 , Interface_descriptor 'length , INTERFACE descriptor type

Data Interface_nb , Alternate 'Number of interface , value to select alternate setting

Data Nb_endpoint , Interface_class 'Number of EP except EP 0 ,Class code assigned by the USB

Data Interface_sub_class , Interface_protocol 'Sub-class code assigned by the USB , Protocol code assigned by the USB

Data Interface_index 'Index Of String Descriptor

Data 9 , Hid_descriptor 'length , HID descriptor type

Data Hid_bdc% , 8 ' Binay Coded Decimal Spec. release , Hid_country_code

Data Hid_class_desc_nb , Hid_descriptor_type 'Number of HID class descriptors to follow , Report descriptor type

Data Size_of_report% 'HID KEYBOARD LENGTH

Data 7 , Endpoint_descriptor ' Size Of This Descriptor In Bytes , ENDPOINT descriptor type

Data Endpoint_nb_1 , Ep_attributes_1 ' Address of the endpoint ,Endpoint's attributes

Data Ep_size_1% ' Maximum packet size for this EP , Interval for polling EP in ms

Data Ep_interval_1

Data 7 , Endpoint_descriptor ' Size Of This Descriptor In Bytes , ENDPOINT descriptor type

Data Endpoint_nb_2 , Ep_attributes_2 ' Address of the endpoint , Endpoint's attributes

Data Ep_size_2% ' Maximum packet size for this EP

Data Ep_interval_2 ' Interval for polling EP in ms

Usb_hid_report:

Data &H06 , &HFF , &HFF ' 04|2 , Usage Page (vendordefined?)

Data &H09 , &H01 ' 08|1 , Usage (vendordefined

Data &HA1 , &H01 ' A0|1 , Collection (Application)

' // IN report

Data &H09 , &H02 ' 08|1 , Usage (vendordefined)

Data &H09 , &H03 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , Logical Minimum(0 for signed byte?)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte?)

Data &H75 , &H08 ' 74|1 , Report Size(8) = field size in bits = 1 byte

Data &H95 , Length_of_report_in ' 94|1:ReportCount(size) = repeat count of previous item

Data &H81 , &H02 ' 80|1: IN report (Data,Variable, Absolute)

' // OUT report

Data &H09 , &H04 ' 08|1 , Usage (vendordefined)

Data &H09 , &H05 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , Logical Minimum(0 for signed byte?)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte?)

Data &H75 , &H08 ' 74|1 , Report Size(8) = field size in bits = 1 byte

Data &H95 , Length_of_report_out ' 94|1:ReportCount(size) = repeat count of previous item

Data &H91 , &H02 ' 90|1: OUT report (Data,Variable, Absolute)

' // Feature report

Data &H09 , &H06 ' 08|1 , Usage (vendordefined)

Data &H09 , &H07 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , LogicalMinimum(0 for signed byte)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte)

Data &H75 , &H08 ' 74|1 , Report Size(8) =field size in bits = 1 byte

Data &H95 , &H04 ' 94|1:ReportCount

Data &HB1 , &H02 ' B0|1: Feature report

Data &HC0 ' C0|0 , End Collection

---

## CONFIG USI

Action

Configures the hardware USI.

Syntax

```vb
CONFIG USI=usimode , Address=adr , ALTPIN=port

CONFIG USI=usimode , Mode=mode , ALTPIN=port

```
Remarks

The USI(universal serial Interface) is found in most atTiny processors. It can be used for various tasks. At the moment only the TWI slave and TWI master modes are supported. The other modes you need to configure/code yourself.

The CONFIG USI = TWISLAVE mode requires a library that is part of the i2c slave add on which is a commercial add on.

The CONFIG USI = TWIMASTER also requires a library which is included in the commercial distribution. 

usiMode | The supported mode is :  \- TWISLAVE. This will set the USI in TWI slave mode. The USI works in interrupt mode on the background. The library i2c_usi_slave.lib contains the USI slave code. -TWIMASTER. This will set the USI in TWI master mode. This mode does not use interrupts. The library i2c_usi.lib contains the USI master code.  
---|---  
Address | This is the I2C/TWI slave address. Notice that bascom uses the 8-bit address notation. The address is only required when using the USI as a slave.  
Mode | The mode is only intended to be used with the USI in master mode. The options are : FAST and NORMAL. Normal will result in a 100 KHz clock signal. And FAST will use a 400 KHz signal if possible.  
Altpin | Some processor have an option to swap the USI pins. For example tiny261 can swap from default portB to portA. When not specified, the default pins will be used. When a different port is defined than the default, a constant will be created that is used inside the library. The USIPP register will be set to swap the pins.  It is not possible to swap pins dynamically.  
  
TWI SLAVE MODE

When USI is used in TWI/I2C mode, it does require that SCL and SDA have pull up resistors. You can not freely choose the SCL and SDA pins : you must use the fixed SCL en SDA pins.

The variables TWI_USI_OVS , TWI_slaveAddress, Twi , Twi_btr and Twi_btw are created by the compiler. These are all bytes.

The USI interrupts are enabled but you need to enabled the global interrupt using ENABLE INTERRUPTS

The USI Slave code is running as an interrupt process. Each time there is an USI interrupt some slave code is executed. Your BASIC code is called from the low level slave code at a number of events.

You must include all these labels in your Slave application. You do not need to write code in all these sub routines.

Label | Event  
---|---  
Twi_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata | The master has sent data. The variable TWI holds the received value. The byte TWI_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte | The master reads from the slave and needs a value. The variable TWI_BTR can be inspected to see which index byte was needed.   
  
TWI MASTER MODE

When USI is used in TWI/I2C mode, it does require that SCL and SDA have pull up resistors. You can not freely choose the SCL and SDA pins : you must use the fixed SCL en SDA pins.

The master mode does NOT require or use any variables. It also does not use any interrupts.

See also

[Using USI](using_usi_universal_serial_int.md) , [CONFIG TWISLAVE](config_twislave.md), [CONFIG TWIXSLAVE ](config_twixslave.md)

Example, USI SLAVE

```vb
'-------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' This demo demonstrates the USI I2C slave  
' Not all AVR chips have an USI !!!!  
'-------------------------------------------------------------------------------  
  
$regfile = "attiny2313.dat"  
  
$crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 24  
  
```
const cPrint = 0 'make 0 for chips that have NO UART, make 1 when the micro has a UART and you want to show data on the terminal  
  

```vb
#if cPrint  
$baud = 19200 'only when the processor has a UART  

#endif  
  
config usi = twislave , address = &H40 'bascom uses 8 bit i2c address (7 bit shifted to the left with one bit)  
  

#if cPrint  
print "USI DEMO"  

#endif  
  
'do not forget to enable global interrupts since USI is used in interrupt mode  
enable interrupts 'it is important you enable interrupts  
  
do  
```
! nop ; nothing to do here  
```vb
loop  
  
  
  
'The following labels are called from the library. You need to insert code in these subroutines  
'Notice that the PRINT commands are remarked.  
'You can unmark them and see what happens, but it will increase code size  
'The idea is that you write your code in the called labels. And this code must execute in as little time  
'as possible. So when you slave must read the A/D converter, you can best do it in the main program  
'then the data is available when the master requires it, and you do not need to do the conversion which cost time.  
  
  
'A master can send or receive bytes.  
'A master protocol can also send some bytes, then receive some bytes  
'The master and slave address must match.  
  
'the following labels are called from the library when master send stop or start  
```
Twi_stop_rstart_received:  
```vb
' Print "Master sent stop or repeated start"  
Return  
  
'master sent our slave address and will not send data  
```
Twi_addressed_goread:  
```vb
' Print "We were addressed and master will send data"  
Return  
  
  
```
Twi_addressed_gowrite:  
```vb
' Print "We were addressed and master will read data"  
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWI holds the received value  
```
Twi_gotdata:  
```vb
' Print "received : " ; Twi ; " byte no : " ; Twi_btw  
Select Case Twi_btw  
Case 1 : 'Portd = Twi ' first byte  
Case 2: 'you can set another port here for example  
End Select  
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twi_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twi_btr can be used for the index  
```
Twi_master_needs_byte:  
```vb
' Print "Master needs byte : " ; Twi_btr  
Select Case Twi_btr  
Case 1 : twi = 68 ' first byte  
Case 2 : twi = 69 ' send second byte  
End Select 'you could also return the state of a port pin or A/D converter  
Return

```
Example, USI Master

```vb
'------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' USI-MASTER.bas  
' USI used as TWI master demo  
'------------------------------------------------------------------------------  
  
$regfile = "attiny2313.dat"  
$crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 24  
$baud = 19200  
  
config usi = twimaster , mode = fast  
  
dim b as byte  
  
```
i2cinit  
  
do  
i2cstart  
i2cwbyte &H40 'send slave WRITE address for PCF8574  
i2cwbyte &B10101010 'send a pattern  
i2crepstart 'repeated start  
  
i2cwbyte &H41 'send slave READ address  
i2crbyte b , ack 'read a byte  
i2crbyte b , nack 'and again  
i2cstop 'end transaction and free bus  
  
```vb
waitms 100 'some delay not required only when you print  
loop

```

---

## CONFIG VARPTRMODE

Action

This options sets the behavior of the VARPTR() function.

Syntax

CONFIG VARPTRMODE= Relave | Absolute

Remarks

Different AVR processors have different memory architectures. 

Plan old AVR like atmega8 start with the 32 registers, then IO registers with address 0-&H3F then a gap of 32 bytes after which the SRAM memory starts.

The registers R0-R31 are accessible using memory pointer ST/LD. They occupy the absolute address 0-31.

The IO registers with address 0-&H3F can be indexed as well. But an offset of 32 must be added. So IO register TWBR which is at location 0 requires an offset of 32 when using a pointer like LD/ST. Port operations like IN/OUT requires the address from the DAT file thus 0-&H3F.

The Xmega works different. Here the registers R0-R31 can not be accessed by pointers. So here we use the relative address. 

And the same applies to the Xtiny platorm processors. There is no way you can address registers by a pointer either. 

When you use VARPTR with an IO register to assign a constant the absolute address was returned up to version 2086.

This was wrong since the absolute address was returned instead of the relative address.

Now this is fixed in 2087. But you need to add a CONFIG statement in order to fix this. 

In order not to break code this bug can be corrected with a new CONFIG directive.

You may change the behavior between the 2 modes.

The default is the wrong absolute mode.

```vb
CONFIG VarptrMode= Relative will set the mode to the relative address. This will give the desired output which will match that of the report file and the Code Explorer. The Code Explorer will always show the relative value which will match the value from the DAT file.

CONFIG VarptrMode = Absolute will set the mode to absolute address so it will be ideal for BASIC INP/OUT operations. Do not confuse with ASM IN/OUT instructions which will always require the relative address !

```
See also

[VARPTR](varptr.md)

Example

```vb
$Regfile="m2560def.dat"  
$Crystal=16000000  
$hwstack=40  
$swstack=32  
$framesize=32  
  
' the default is the old 2086 mode which gives a wrong result for normal AVR IO registers  
Config VarptrMode=relative  
  
'pina=0  
```
Const Test1 = VarPtr(PINA) ' IO &h00  
Const Test2 = VarPtr(EECR) ' IO &h1F  
Const Test3 = VarPtr(EEDR) ' IO &h20  
Const Test4 = VarPtr(SREG) ' IO &h3F  
Const Test5 = VarPtr(WDTCSR) ' extIO &h60  
Const Test6 = VarPtr(UDR3) ' extIO &h136  
'(  
Report:  
TEST1 &H00  
TEST2 &H1F  
TEST3 &H20  
TEST4 &H3F  
TEST5 &H60  
TEST6 &H136  
```vb
')  
  
Print "&h";Hex(VarPtr(PINA)) ' IO &h00  
Print "&h";Hex(VarPtr(EECR)) ' IO &h1F  
Print "&h";Hex(VarPtr(EEDR)) ' IO &h20  
Print "&h";Hex(VarPtr(SREG)) ' IO &h3F  
Print "&h";Hex(VarPtr(WDTCSR)) ' extIO &h60  
Print "&h";Hex(VarPtr(UDR3)) ' extIO &h136  
Print  
'(  
```
Output:  
&h0020  
&h003F  
&h0040  
&h005F  
&h0060  
&h0136  
```vb
')  
  
' when you set the mode to relative you get the correct value  
Config VarptrMode=relative  
'pina=0  
```
Const Test11 = VarPtr(PINA) ' IO &h00  
```vb
print hex(test11) 'prints 00  
End

```

---

## CONFIG VPORT

Action

Maps an XMEGA port to a virtual port.

Syntax

CONFIG VPORT0 = port [, VPORT1=port, VPORT2=port, VPORT3=port]

Remarks

VPORT | There are 4 virtual port registers. When setting up these registers, you need to use VPORTx, where X is 0,1,2 or 3, indicating the virtual port. The virtual port itself is accesed via it's registers PORTy, PINy and DDRy where Y is a 0,1 ,2 or 3.  The normal ports have named like PORTA, PORTB, etc. A virtual port will access the same port but using a different register.  
---|---  
port | The last letter of the real port name. For example A for PORTA, B for PORTB, C for PORTC etc.  
  
![notice](notice.jpg)You must specify multiple virtual ports on one CONFIG line. You should not split up the lines in multiple statements because a new CONFIG VPORT will write a new value, erasing the previous setting. When you need to configure 2 virtual ports, put them on one config line like : Config VPort0 = D , VPort1 = E

When you split the command like :

```vb
Config VPort0 = D 

Config VPort1 = E

```
The second config will erase the setting of the first config. 

![notice](notice.jpg)Some processors like the ones from the E5 series have a fixed relation. These chips have virtual port registers (port,ddr,pin) and do not need a CONFIG VPORT).For the E5 this relation is :

PORT0 - Virtual port A

PORT1 - Virtual port C

PORT2 - Virtual port D

PORT3 - Virtual port R

All ports in the Xmega are located in the extended address area. This space can only be accessed with instructions like LDS,STS, LD and ST.

Special bit instructions only work on the lower IO-registers. 

Xmega example :

again:

Lds r24, PINA ; read port input value

sbrs r24,7 ; skip next instruction if bit 7 is set (1)

rjmp again ; try again

Now the same code for a normal AVR

again:

sbis PINA,7 ; skip if pina.7 is set

rjmp again

Not only less code is required, but the LDS takes 3 cycles

With the virtual mapping, you can access any PORT register (PORT,PIN and DDR) via it's virtual name PORT0, PIN0 or DDR0.

Since there are 4 virtual mapping registers, you can define PORT0, PORT1, PORT2 and PORT3.

When you write to PORTn, the compiler can use the smaller/quicker code. 

Devices like graphical LCD can benefit from this. 

XTINY

Xtiny also have virtual port registers. And these are fixed as well. There is no config required. The benefit of the virtual port is again that it is located in lower memory so shorter/faster assembly instructions are possible.

We would recommend to use the virtual port names. 

See Also

[CONFIG PORT](config_port.md)

Example

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' Mapping Real Ports to Virtual Ports.bas  
' This sample demonstrates mapping ports to virtual ports  
' based on MAK3's sample  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'include the following lib and code, the routines will be replaced since they are a workaround  
$lib "xmega.lib"  
$external _xmegafix_clear  
$external _xmegafix_rol_r1014  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Print "Map VPorts"  
'map portD to virtual port0, map portE to virtual port1, map portC to virtual port2  
'map portR to virtual port 3  
Config VPort0 = D , VPort1 = E , VPort2 = C , VPort3 = R  
  
'Each virtual port is available as PORT0, PORT1, PORT2 and PORT3  
' data direct is available as DDR0 , DDR1, DDR2 and DDR3  
' PIN input is available as PIN0 , PIN1, PIN2 and PIN3  
  
'The advantage of virtual port registers is that shorter asm instruction can be used which also use only 1 cycle  
Dim Var As Byte  
  
  
'Real Port Direction  
```
Ddr1 = &B0000_0000 ' Port E = INPUT  
Ddr0 = &B1111_1111 ' Port D = OUTPUT  
  
  
```vb
'Continously copy the value from PORTE to PORTD using the virtual ports.  
Do  
```
Var = Pin1 'Read Virtual Port 0  
Port0 = Var 'Write Virtual Port 1  
```vb
Loop  
  
End 'end program

```

---

## CONFIG VREF

Action

This configuration statement will configure the XTINY voltage reference.

Syntax

CONFIG VREF=Dummy, ADCx=ref1,DACx|AC0=ref2, force_adcX=opt1,force_dacX|force_acX=opt2 

Remarks

dummy | There is no actual global setting for VREF so the only option is dummy  
---|---  
ADCx | This will set the voltage reference for the ADC0/ADC1 to the specified value of ref1. The X represents the number 0 or 1 which represents ADC0 and ADC1. The voltage reference for the ADC ref1 can be : \- 0.55V \- 1.1V \- 4.3V \- 1.5V The default is 0.55V The voltage reference can not exceed the supply voltage. So 4.3 is only possible when VCC is 5V  
force_adcX | This option allows to force the reference to be running even if it is not requested.  A value of ENABLED will force the reference to be on. A value of DISABLED which is the default will set the reference in automatic mode. In this mode the reference is turned on when requested. This will save power.  
DACx AC0 | This will set the voltage reference for the DACx and/or ACx to the specified value of ref2. Note that ADCx and DACx/ACx reference can be set in depended of each other. The X indicates a number 0,1 or 2 which represents DAC0, DAC1 and DAC2. The voltage reference for the DAC which can be : \- 0.55V \- 1.1V \- 4.3V \- 1.5V The voltage reference can not exceed the supply voltage. So 4.3 is only possible when VCC is 5V  
force_dacX force_acX | This option allows to force the reference to be running even if it is not requested.  A value of ENABLED will force the reference to be on. A value of DISABLED which is the default will set the reference in automatic mode. In this mode the reference is turned on when requested. This will save power. As for the other options, the X represents the peripheral DAC/AC.  
  
Note that not all processors have an ADC and/or DAC. It depends on the processor.

Some processors have multiple ADC and/or DAC. 

The DAC and AC are grouped together. The IDE will show the proper options depending on the chosen processor when using CTRL+SPACE

See also

[CONFIG ADC0](config_adc0_adcx.md)

Example

---

## CONFIG VREGPWR

Action

Configures the voltage regulator.

Syntax

CONFIG VREGPWR= AUTO|FULL , HTMP_LOWLEAK=DISABLED|ENABLED , REGMODE=OVERWRITE|PRESERVE

Remarks

The CONFIG VREGPWR sets the power controller related to the sleep controller options.

VREGPWR | Configures the mode.  \- AUTO : the regulator will run at the full performance unless the 32 KHz oscillator is selected, then it runs in lower power mode \- FULL : full performance voltage regulator drive strength in all modes  
---|---  
HTMP_LOWLEAK | Selects the high temperature low leakage mode \- DISABLED : high temperature low leakage disabled \- ENABLED : high temperature low leakage enabled When enabled the leakage is reduced when operating at temperature above 70 Celsius. This setting has an effect only in power down mode when the VREGPWR mode is set to AUTO. It must be configured before the [CONFIG POWERMODE](config_powermode.md) option.   
REGMODE | \- OVERWITE : the entire register is updated.  \- PRESERVE : the register bits are preserved. See also the [AVRX](avrx.md) topic.  
  
See also

[CONFIG POWERMODE](config_powermode.md)

Example

NONE

---

## CONFIG WAITSUART

Action

Compiler directive that specifies that software UART waits after sending the last byte.

Syntax

CONFIG WAITSUART = value

Remarks

value | A numeric value in the range of 1-255. A higher value means a longer delay in mS.  
---|---  
  
When the software UART routine are used in combination with serial LCD displays it can be convenient to specify a delay so the display can process the data.

See also

[OPEN](open.md)

Example

See [OPEN](open.md) example for more details.

---

## CONFIG WATCHDOG

Action

Configures the watchdog timer.

Syntax

CONFIG WATCHDOG = time 

Syntax XTINY

CONFIG WATCHDOG = time [,window=time]

Remarks

Time | The interval constant in ms the watchdog timer will count to before it will reset your program. Possible settings : 16 , 32, 64 , 128 , 256 , 512 , 1024 and 2048. Some newer chips : 4096, 8192. The XMEGA has a 1 KHz clocked watchdog. For Xmega the following value in millisecond need to be used : 8 ,16,32,64,125,250,500,1000,2000,4000,8000  So 2000 will sets a timeout of 2 seconds. The XTINY platform accepts the following values : 0 - will turn off the WD 8 - 8 clock cycles which is 7.8 ms 16 - 16 clock cycles which is 16.625 ms 32 - 32 clock cycles which is 32.25 ms 64 - 64 clock cycles which is 62.5 ms 128 - 128 clock cycles which is 0.125 ms 256 - 256 clock cycles which is 0.250 ms 512 - 512 clock cycles which is 0.500 ms 1000 - 1000 clock cycles which is 1 sec 2000 - 2000 clock cycles which is 2 sec 4000 - 4000 clock cycles which is 4 sec 8000 - 8000 clock cycles which is 8 sec The Xtiny also has an optional window value that can be set.  
---|---  
  
Note that some new AVR's might have additional reset values such as 4096 and 8192.

Normal AVR

When the WatchDog is started, a reset will occur after the specified number of mS.

With a value of 2048, a reset will occur after 2 seconds, so you need to reset the WD in your programs periodically with the RESET WATCHDOG statement.

Some AVR's might have the WD timer enabled by default. You can change this by changing the Fuse Bits.

![notice](notice.jpg)Global Interrupts should be disabled when they are active. The reason is that changing the WD, a special timed sequence is required. An interrupt could extend the time, making the timed sequence fail.

![notice](notice.jpg)After the CONFIG WATCHDOG statement, the watchdog timer is disabled. You can also use CONFIG WATCHDOG to change the time out value. This will stop the watchdog timer and load the new value.

After a CONFIG WATCHDOG, you always need to start the Watchdog with the START WATCHDOG statement.

Most new AVR chips have an MCUSR register that contains some flags. One of the flags is the WDRF bit. This bit is set when the chip was reset by a Watchdog overflow. The CONFIG WATCHDOG will clear this bit, provided that the register and bit are available in the micro.

When it is important to examine at startup if the micro was reset by a Watchdog overflow, you need to examine this MCUSR.WDRF flag before you use CONFIG WATCHDOG, since that will clear the flag.

ALL PLATFORMS

![notice](notice.jpg)For chips that have an enhanced WD timer, the WD timer is cleared as part of the chip initialize procedure. This because otherwise the WD timer will only work once. If it is important to know the cause of the reset, you can read the register R0 before you run other code.

When the chip resets, the status registers with the reset cause bits is saved into register R0.

This is done because the compiler need to reset these flags since otherwise they can not occur again. And before clearing the bits, the status is saved into register R0.

The sample below demonstrates how to store the WDRF bit if you need it, and print it later. 

The compiler will read R0 from the correct register which depends on the used platform (normal AVR, Xmega, Xtiny)

XTINY

The XTINY platform differs from the normal AVR. The WD timer will be turned off with a value of 0. Normal AVR use a bit for that.

When you use STOP WATCHDOG, a value of 0 will be written to the control register to turn off the WD.

This also means that when you configure the Watchdog with a value other than 0, it will start immediately.

Since there is no control bit it means that START WATCHDOG will only work when the WD timer has been previously configured with a value other than 0.

This value will be written to the Watchdog in order to start it.

When there is no window value provided, the watchdog timer is in the normal mode. In the normal mode a single time out period is set for the WDT. 

If the WDT is not reset during the defined time-out period, the WDT will issue a system reset.

In order to prevent overflow of the WDT a reset must be done using : RESET WATCHDOG statement.

When a window value is defined the WDT will be in window mode. In window mode the WDT uses two different time-out periods :

\- the closed window time-out period (TOwdtw) define a duration from 8 ms to 8 sec where the WDT can not be reset. If the WDT is reset during this period, the WDT will issue a system reset.

\- the open window time-out period (TOwdt) which is also 8 ms to 8s sec, defines the open period during which the WDT can (and needs to) be reset. The open period will always follow the closed period, so the total duration of the time-out perio is the sum of the closed window and the open window time-out periods.

The following picture is taken from the datasheet 

![wd_xtiny_window](wd_xtiny_window.png)

![notice](notice.jpg)When setting the Watchdog FUSE , this value is loaded when the processor boots. After that this value can not be changed since a LOCK bit is set.

This also means that when using the FUSE you can not stop the watchdog.

See also

[START WATCHDOG ](start.md), [STOP WATCHDOG ](stop.md), [RESET WATCHDOG](reset.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : watchd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates the watchdog timer

'micro : Mega88

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m88def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 32 ' default use 32 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

Dim Wdbit As Bit

Dim bWD As Byte

```
bWD= R0 ' read the wd flag

```vb
Print "Watchdog test" 

If bwd.wdrf = 1 Then ' there was a WD overflow

```
Wdbit = 1 'store the flag

```vb
End If

Config Watchdog = 2048 'reset after 2048 mSec

If Wdbit = 1 Then 'just print it now since it is important that CONFIG WATCHDOG runs early as possible

Print "Micro was reset by Watchdog overflow"

End If

```
Start Watchdog 'start the watchdog timer

```vb
Dim I As Word

For I = 1 To 1000

Waitms 100

Print I 'print value

```
B = Inkey() ' get a key from the serial port

If B = 65 Then 'letter A pressed

Stop Watchdog ' test if the WD will stop

Elseif B = 66 Then 'letter B pressed

Config Watchdog = 4096 'reconfig to 4 sec

Start Watchdog 'CONFIG WATCHDOG will disable the WD so start it

Elseif B = 67 Then 'C pressed

```vb
Config Watchdog = 8192 ' some have 8 sec timer

'observe that the WD timer is OFF

```
Elseif B = 68 Then 'D pressed

Start Watchdog ' start it

```vb
End If

'Reset Watchdog

'you will notice that the for next doesnt finish because of the reset

'when you unmark the RESET WATCHDOG statement it will finish because the

'wd-timer is reset before it reaches 2048 msec

'When you press 'A' you will see that the WD will stop

'When you press 'B' you will see that the WD will time out after 4 Sec

'When you press 'C' you will see the WD will stop

'When you press 'D' you will see the WD will start again timing out after 8 secs

Next

End

```
And this shows how to read the register r0:

Dim Breset As Byte

Breset = R0

When you show this value on an LCD display you will see a value of 7 the first time, and later a value of 15 when the WD reset occured.

Xmega Sample

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-WD.bas  
' This sample demonstrates the Xmega128A1 Watchdog  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Config Input1 = Cr , Echo = Crlf ' CR is used for input, we echo back CR and LF  
  
```
Open "COM1:" For Binary As #1  
```vb
' ^^^^ change from COM1-COM8  
  
Print #1 , "Xmega revision:" ; Mcu_revid ' make sure it is 7 or higher !!! lower revs have many flaws  
  
Config Watchdog = 4000 'after 4 seconds a reset will occur if the watchdog is enabled  
'possible value : 8 ,16,32,64,125,250,500,1000,2000,4000,8000  
'these values are clock cycles, based on a 1 KHz clock !!!  
  
Dim W As Word , B As Byte  
Do  
```
W = W + 1  
```vb
Print W  
Waitms 500  
```
B = Inkey()  
If B = "a" Then  
Start Watchdog  
Print "start"  
Elseif B = "b" Then  
Stop Watchdog  
Print "stop"  
Elseif B = "c" Then  
```vb
Config Watchdog = 8000  
Print "8 sec"  
```
Elseif B = "d" Then  
```vb
Reset Watchdog  
Print "reset"  
End If  
Loop

```
XTINY Sample

```vb
'--------------------------------------------------------------------------------  
'name : watchdog-avrx128da28.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Watchdog  
'micro : avra128DA28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Submode = New  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Clock = Soft , Rtc = 32khz_32khz_intosc  
'the RTC requires that global interrupts are enabled  
Enable Interrupts  
  
  
Print "Test WD"  
  
'time out after 8 sec  
'a configuration other then 0 will start the watchdog  
'a configuration of 0 will turn off the watchdog  
Config Watchdog = 8000  
Dim B As Byte  
  
  
Do  
```
B = Inkey()  
```vb
Select Case B  
Case "r" : Reset Watchdog 'reset WD  
Case "s" : Config Watchdog = 8000 'set back to value used in config above  
Case "q" : Config Watchdog = 0 'turn off WD  
Case "1" : Config Watchdog = 1000 'set time out to 1 sec  
Case "2" : Config Watchdog = 2000 'set time out to 2 sec  
Case "4" : Config Watchdog = 4000 'set time out to 4 sec  
Case "8" : Config Watchdog = 8000 'set time out to 8 sec  
End Select  
  
Print "WD:" ; Time$ 'now watch the time  
Waitms 1000  
Loop  
  
End

```
Xtiny Example 2

```vb
'--------------------------------------------------------------------------------  
'name : watchdog.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Watchdog  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atxtiny816.dat"  
$crystal = 20000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Dim Bwd As Byte  
```
R0 = Bwd 'store R0 into variable so we can check the reset cause  
```vb
'set the system clock and prescaler  
Config Sysclock = 16_20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Clock = Soft , Rtc = 32khz_32khz_intosc  
'the RTC requires that global interrupts are enabled  
Enable Interrupts  
  
  
Print "Test WD, reset cause:"  
If Bwd.0 = 1 Then  
Print "power on reset"  
End If  
If Bwd.1 = 1 Then  
Print "brown out reset"  
End If  
If Bwd.2 = 1 Then  
Print "external reset"  
End If  
If Bwd.3 = 1 Then  
Print "watchdog reset"  
End If  
If Bwd.4 = 1 Then  
Print "software reset"  
End If  
If Bwd.5 = 1 Then  
Print "UPDI reset"  
End If  
  
'time out after 8 sec  
Config Watchdog = 8000  
  
Do  
Print "WD:" ; Time$  
Waitms 1000  
Loop  
  
End

```

---

## CONFIG X10

Action

Configures the pins used for X10.

Syntax

CONFIG X10 = pinZC , TX = portpin

Remarks

PinZC | The pin that is connected to the zero cross output of the TW-523. This is a pin that will be used as INPUT.  
---|---  
Portpin | The pin that is connected to the TX pin of the TW-523. TX is used to send X10 data to the TW-523. This pin will be used in output mode.  
  
The TW-523 RJ-11 connector has the following pinout:

Pin | Description | Connect to micro  
---|---|---  
1 | Zero Cross | Input pin. Add 5.1K pull up.  
2 | GND | GND  
3 | RX | Not used.  
4 | TX | Output pin. Add 1K pull up.  
  
See also

[X10DETECT](x10detect.md) , [X10SEND](x10send.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : x10.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example needs a TW-523 X10 interface

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'define the house code

```
Const House = "M" ' use code A-P

```vb
Waitms 500 ' optional delay not really needed

'dim the used variables

Dim X As Byte

'configure the zero cross pin and TX pin

Config X10 = Pind.4 , Tx = Portb.0

' ^--zero cross

' ^--- transmission pin

'detect the TW-523

```
X = X10detect()

```vb
Print X ' 0 means error, 1 means 50 Hz, 2 means 60 Hz

Do

Input "Send (1-32) " , X

'enter a key code from 1-31

'1-16 to address a unit

'17 all units off

'18 all lights on

'19 ON

'20 OFF

'21 DIM

'22 BRIGHT

'23 All lights off

'24 extended code

'25 hail request

'26 hail acknowledge

'27 preset dim

'28 preset dim

'29 extended data analog

'30 status on

'31 status off

'32 status request

```
X10send House , X ' send the code

```vb
Loop

Dim Ar(4) As Byte

```
X10send House , X , Ar(1) , 4 ' send 4 additional bytes

End

---

## CONFIG XPIN

Action

Configures additional features of a processor port or pin.

Syntax

CONFIG XPIN=PORT|PIN, OUTPULL=pull

Syntax Xmega

CONFIG XPIN=PORT|PIN, INVERTIO=invio, SLEWRATE=slew, PULLUP=pull, SENSE=sense

Syntax Xtiny

CONFIG XPIN=PORT|PIN, INVERTIO=invio, PULLUP=pull, SENSE=sense

Remarks

Normal AVR port pins can be configured as an input or output. When configured as an input (CONFIG PIN=INPUT) they can also be set to tri-state (write a 0 to the PORT register) or to activate the pull up resistor(write a 1 to the PORT register).

Some new AVR processors use a special PUD register to control the pull up. The CONFIG XPIN automatically uses the proper registers to control the pull up state.

![notice](notice.jpg)The XPIN option was added for the Xmega which uses the term Outpull instead of Pullup. The compiler will accept both names but the Code Explorer and Intellisense expect PULLUP.

Normal AVR

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
PULLUP | Sets the output or pull mode. The following options are available: \- OFF :no pull up \- PULLUP : input pull up  
  
Normal AVR processors (tiny,mega) have only one option : PULLUP. 

The compiler will either write a 1 or 0 to the PORT register or the PUEx register.

You can control a single pin using a port pin name like PORTB.0 or the whole register like PORTB.

Normal AVR code that use : PORTX.Y=1 to activate the pull up, should be written as : CONFIG XPIN=PORTX.Y,PULLUP=PULLUP

XMEGA

You still need to use PORTx = state or PINx.y = state to configure the data direction of that port or pin in addition to CONFIG XPIN.

The xmega has many more options. The Xmega manual explains all the options.

The CONFIG XPIN statement will set the proper registers.

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
INVERTIO | This option will invert the data for both input and output modes. Possible values : ENABLED (will invert data), DISABLED(normal mode)   
SLEWRATE | Will enable or disable the slewrate. Enabling the slew rate will increase the rise/fall time by 50%-150%. Possible values : ENABLED, DISABLED ![notice](notice.jpg)For the Xmega E-series, the slewrate is set for the whole port. While the other Xmega series allow setting of sleware for an individual pin.  
PULLUP | Sets the output or pull mode. The following options are available: \- TOTEM : output totem pole \- BUSKEEPER : output totem pole, input bus keeper \- PULLDOWN : output totem pole, input pull down \- PULLUP : output totem pole, input pull up \- WIREDOR : output wired OR \- WIREDAND: output wired AND -WIREDORPULL : output wired OR, input pull down -WIREDANDPULL : output wired AND, input pull up  
SENSE | In input mode, the trigger sense can be configured. Possible values : \- BOTH : sense both edges \- RISING : sense rising edge -FALLING : sense falling edge -LOW_LEVEL :sense low level -INP_DISABLED : digital input buffer disabled (only PORTA-PORTF)  
  
Xtiny

You still need to use PORTx = state or PINx.y = state to configure the data direction of that port or pin in addition to CONFIG XPIN.

The xtiny has many more options.

The CONFIG XPIN statement will set the proper registers.

PORT PIN | The pin to be configured. For example PORTC.0 When configuring the whole port (all the pins must have the same functionality), use PORT. For example : PORTD  
---|---  
INVERTIO | This option will invert the data for both input and output modes. Possible values : ENABLED (will invert data), DISABLED(normal mode)   
PULLUP | Sets the output or pull mode. The following options are available: \- DISABLED or OFF : pull up disabled \- PULLUP : output totem pole, input pull up  
SENSE | In input mode, the trigger sense can be configured. Possible values : \- INT_DISABLED : interrupt disabled but input buffer enabled \- BOTH : sense both edges \- RISING : sense rising edge -FALLING : sense falling edge -LOW_LEVEL :sense low level -INP_DISABLED : digital input buffer disabled   
  
See also

[CONFIG PIN](config_port.md), [CONFIG INT](config_intx.md)

Example:

```vb
Config Porte.5 = Input  
Config Xpin = Porte.5 , Pullup = Pullup , Sense = Falling 'enable Pull up and reaction on falling edge

```
Example

```vb
$regfile = "xm256a3budef.dat"  
$Crystal = 32000000 '32MHz  
  
Config Xpin = Portc.0 , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
Config Xpin = Portc.1 , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
  
'setup the whole port at once  
Config Xpin = Portd , Slewrate = Enabled , Pullup = Buskeeper , Sense = Low_level  
  


```

---

## CONFIG XRAM

Action

Instruct the compiler to set options for external memory access.

Syntax

CONFIG XRAM = mode [ , WaitstateLS=wls] [ , WaitStateHS=whs ]

Syntax Older chips

CONFIG XRAM = mode , Waitstate=wls

Syntax Xmega

CONFIG XRAM = mode, sdbus=sdbus,lpc=lpc,sdcol=sdcol,sdcas=sdcas,sdrow=sdrow,refresh=refresh,initdelay=initdelay,modedelay=modedelay,rowcycledelay=rowcycledelay,rowprechargedelay=rowprechargedelay,wrdelay=wrdelay,ersdelay=esrdelay, rowcoldelay=rowcoldelay,modesel0=sel,adrsize0=adr,baseadr0=base,modesel1=sel,adrsize1=adr,baseadr1=base,modesel2=sel,adrsize2=adr,baseadr2=base,modesel3=sel,adrsize3=adr,baseadr3=base

See also: [Adding XRAM with External Memory Interface](adding_xram.md)

Remarks AVR

Mode | The memory mode. This is either enabled or disabled. By default, external memory access is disabled.  
---|---  
Wls | When external memory access is enabled, some chips allow you to set a wait state. The number of modes depend on the chip. A modern chip such as the Mega8515 has 4 modes : 0 - no wait states 1 - 1 cycle wait state during read/write 2 - 2 cycle wait state during read/write 3 - 2 cycle wait state during read/write and 1 before new address output WLS works on the lower sector. Provided that the chip supports this.  
Whs | When external memory access is enabled, some chips allow you to set a wait state. The number of modes depend on the chip. A modern chip such as the Mega8515 has 4 modes : 0 - no wait states 1 - 1 cycle wait state during read/write 2 - 2 cycle wait state during read/write 3 - 2 cycle wait state during read/write and 1 before new address output WHS works on the high sector. Provided that the chip supports this.  
  
Wait states are needed in case you connect equipment to the bus, that is relatively slow. Especial older electronics/chips.

Some AVR chips also allow you to divide the memory map into sections. By default the total XRAM memory address is selected when you set a wait state.

Older chips like the 90S8515 do not have a lower and upper sector. The setting is for all the memory in that case.

The $XA directive should not be used anymore. It is the same as CONFIG XRAM=Enabled.

![notice](notice.jpg)When using IDLE or another power down mode, it might be needed to use CONFIG XRAM again, after the chip wakes from the power down mode. 

[[See also Adding XRAM]](<adding_xram.htm>)

XMEGA

Mode | The memory mode. There are 4 options: \- DISABLED, this will turn off the EBI and is the default \- 3PORT. For using EBI in 3 PORT mode. \- 4PORT. For using EBI in 4 PORT mode. \- 2PORT. For using EBI in 2 PORT mode. The EBI uses specific ports for each of the modes.  
---|---  
sdbus | When using SDRAM, you need to configure 4 bit or 8 bit data width. For the 3 PORT mode you need to use 4 bit SDRAM. Options are : 4 and 8.  
  
|   
  
sdcol | When using SDRAM, you need to configure the number of columns of the chip. This depends on the chip. You can find this info in the datasheet of the SDRAM chip. For example a chip with column address A0-A9 would use 10 bits. Options : 8 ,9, 10 or 11.  
sdrow | When using SDRAM, you need to configure the number of rows of the chip. This depends on the chip. You can find this info in the datasheet of the SDRAM chip.  Options : 11 or 12.  
sdcas | When using SDRAM you can configure the CAS latency as a number of Peripheral 2x Clock cycles. By default this is two Peripheral 2x Clock cycles.  Options are : -2 : CAS latency is two Peripheral 2x Clock cycles -3 : CAS latency is three Peripheral 2x Clock cycles  
refresh | When using SDRAM this value sets the refresh period as a number of peripheral clock cycles. Use a value between 0-1023. The value depends on the chip.  
initdelay | When using SDRAM this value sets the delay of the initialization sequence that is sent after the voltages have been stabilized and the SDRAM clock is stable. The value is in the range of 0-16384  
modedelay | When using SDRAM this value select the delay between Mode Register command and an Activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-3  
rowcycledelay | When using SDRAM this value select the delay between a refresh an and Activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
rowprechargedelay | When using SDRAM this value select the delay between a pre-charge command and another command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
wrdelay | When using SDRAM this value selects the write recovery time in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-3  
esrdelay | When using SDRAM this value selects the delay between CKE set high and activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
rowcoldelay | When using SDRAM this value selects the delay between an activate command and a read/write command as a number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
  
| The options ending with x, are available multiple times.(0-3) So there is an option named selfrefresh0, selfrefresh1, selfrefresh2 and selfrefresh3.  
selfrefreshX | When using SDRAM this options can turn on/off self refresh of the SDRAM. Not all SDRAM have this capability. Valid options are : \- ENABLED \- DISABLED. This is the default.  
sdmodeX | When using SDRAM this option sets the SDRAM mode. This is either NORMAL (default) or LOAD.  
modeselX | This option selects the MODE of the CS line.  There are 4 CS lines and modes. When using SDRAM you can only select modesel3 to configure the SDRAM. The following options are possible: \- DISABLE \- SRAM \- LPC (this is SRAM in low pin count mode) \- SDRAM  
adrsizeX | This options sets the address size for the chip select. This is the size of the block above the base address and determines which address lines are compared to generate the CS. Options are: 256b , 256 bytes, address 8:23 512b, 512 bytes, address 9:23  1K , 1 KB , address 10:23 2K , 2 KB , address 11:23 4K , 4 KB , address 12:23 8K, 8 KB , address 13:23 16K , 16 KB , address 14:23 32K , 32 KB , address 15:23 64K , 64 KB , address 16:23 128K , 128 KB, address 17:23 256K , 256 KB , address 18:23 512K , 512 KB , address 19:23 1M , 1 MB, address 20:23 2M , 2 MB , address 21:23 4M , 4 MB , address 22:23 8M , 8 MB, address 23 16M , 16 MB   
baseadrX | This option sets the chip base address which is the lowest address in the address space enabled by the chip select. The value is a word and sets address bits 12:23. Bits 0:11 are unused and need to be 0. For an 8 MB SDRAM the valid values are 0 and &H800000. Since the lower bits are not used the address is divided by 256 by the compiler. When using 0, the memory overlaps the SRAM which is not a big problem with 8MB of ram!  
  
|   
  
| In SRAM mode there are some other options you must set  
lpc | This sets the ALE mode in LPC SRAM mode.  Options are :  ALE1 : data multiplexed with address byte 0 ALE12 : data multiplexed with address byte 0 and 1  
ale | This sets the ALE mode in normal SRAM mode. Options are : ALE1 : address byte 0 and 1 multiplexed ALE2 : address byte 0 and 2 multiplexed ALE12 : address byte 0, 1 and 2 multiplexed NOALE : No address multiplexing  
waitstateX | The wait state selects the wait states for SRAM and SRAM LPC access as a number of peripheral 2x clock cycles. This is a value in the range from 0-7  
  
![notice](notice.jpg)While the EBI (External Bus Interface) can be configured to use a big 8 MB or 16 MB SDRAM, the compiler was changed in order to support more then 64KB of RAM (you need BASCOM-AVR Verison 2.0.7.4 or higher).

For 3PORT , 4-bit SDRAM mode the ports are set to the right direction and level. For all other modes you need to do this.

An example on how to determine the columns and rows is shown below:

![sdram](sdram.png)

In 4 bit data mode, you use 16 Meg x 4, the row addressing is A0-A11 thus 12 bit and the column addressing is A0-A9 thus 10 bit.

See also

[$XA](xa.md) , [$WAITSTATE](_waitstate.md), [Memory Usage](memory_usage.md), [Adding Xram](adding_xram.md)

ASM

NONE

Example

CONFIG XRAM = Enabled, WaitstateLS=1 , WaitstateHS=2

Xmega SRAM Example

CONFIG XRAM=3PORT , MODESEL3=SRAM, ADRSIZE3=1M , BASEADR3=&h100000 , ALE

= ALE1 , WAITSTATE3 = 0

Xmega Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-XRAM-SDRAM-XPLAIN.bas  
' This sample demonstrates the Xmega128A1 XRAM SDRAM  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
$xramsize = &H800000  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
'for xplain we need 9600 baud  
Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Dim B As Byte , B1 As Byte , B2 As Byte  
Config Porte = Output  
For B = 1 To 5  
Toggle Porte  
Waitms 1000  
Next  
  
Print "Xplain SDRAM test"  
'the XPLAIN has a 64 MBit SDRAM which is 8 MByte, it is connected in 3 port, 4 bit databus mode  
'in the PDF of the SDRAM you can see it is connected as 16 Meg x 4. Refreshcount is 4K and the row address is A0-A11, column addressing is A0-A9  
Config Xram = 3port , Sdbus = 4 , Sdcol = 10 , Sdcas = 3 , Sdrow = 12 , Refresh = 500 , Initdelay = 3200 , Modedelay = 2 , Rowcycledelay = 7 , Rowprechargedelay = 7 , Wrdelay = 1 , Esrdelay = 7 , Rowcoldelay = 7 , Modesel3 = Sdram , Adrsize3 = 8m , Baseadr3 = &H0000  
'the config above will set the port registers correct. it will also wait for Ebi_cs3_ctrlb.7  
'for all other modes you need to do this yourself !  
  
Dim X(65000) As Xram Byte , B as byte  
  
Print "SRAM"  
```
X(10000) = 100 ' this will use normal SRAM  
B = X(10000)  
```vb
Print "result : " ; B  
  
End

```
Another ATXMEGA Example:

  
```vb
'Example to copy a SRAM Array to a XRAM Array over Direct Memory Access (DMA)  
  
  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
' for xplain you need 9600 baud  
' Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Config Com5 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM5:" For Binary As #1  
  
```vb
'SRAM Variables  
Dim Ar(100) As Byte , J As Word , W As Word  
Dim B As Byte  
  
  
' Demoboards like XPLAIN has a 64 MBit SDRAM (MT48LC16M4A2TG) which is 8 MByte, it is connected in 3 port, 4 bit databus mode  
' http://www.micron.com/products/ProductDetails.html?product=products/dram/sdram/MT48LC16M4A2TG-75  
' in the PDF of the SDRAM you can see it is connected as 16 Meg x 4. Refreshcount is 4K and the row address is A0-A11, column addressing is A0-A9  
' SDRAM = SYNCHRONOUS DRAM  
Config Xram = 3port , Sdbus = 4 , Sdcol = 10 , Sdcas = 3 , Sdrow = 12 , Refresh = 500 , Initdelay = 3200 , Modedelay = 2 , Rowcycledelay = 7 , Rowprechargedelay = 7 , Wrdelay = 1 , Esrdelay = 7 , Rowcoldelay = 7 , Modesel3 = Sdram , Adrsize3 = 8m , Baseadr3 = &H0000  
' the config above will set the port registers correct. it will also wait for Ebi_cs3_ctrlb.7  
' for all other modes you need to do this yourself !  
  
$xramsize = 8000000 ' 8 MByte  
  
'XRAM Variables  
Dim Dummy(100000) As Xram Byte 'Xram Variable with 100000 Bytes to ensure we are working above 64KByte  
Dim Dest(100) As Xram Byte 'Next Xram Var with 100 Byte  
  
  
For J = 1 To 100  
```
Ar(j) = J ' create an array and assign a value  
```vb
Next  
  
Print #1 , "Start DMA DEMO --> copy SRAM Array to XRAM Array"  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
  
  
'you can configure 4 DMA channels  
Config Dmach0 = Enabled , Burstlen = 8 , Chanrpt = Enabled , Tci = Off , Eil = Off , Sar = None , Sam = Inc , Dar = None , Dam = Inc , Trigger = 0 , Btc = 100 , Repeat = 1 , Sadr = Varptr(ar(1)) , Dadr = Varptr(dest(1))  
  
```
Start Dmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
'-------------------------------------------------------------------------------  
For J = 1 To 50  
```
B = Dest(j) 'This step is needed to work with XRAM above 64KByte  
```vb
Print #1 , J ; "-" ; Ar(j) ; "-" ; B ' print the values  
Next  
  
'-------------------------------------------------------------------------------  
  
  
  
End  
  
'end program  
  
  
  
  
'(  
```
Terminal Output of example:  
  
Start DMA DEMO --> copy SRAM Array to XRAM Array  
1-1-1  
2-2-2  
3-3-3  
4-4-4  
5-5-5  
6-6-6  
7-7-7  
8-8-8  
9-9-9  
10-10-10  
11-11-11  
12-12-12  
13-13-13  
14-14-14  
15-15-15  
16-16-16  
17-17-17  
18-18-18  
19-19-19  
20-20-20  
21-21-21  
22-22-22  
23-23-23  
24-24-24  
25-25-25  
26-26-26  
27-27-27  
28-28-28  
29-29-29  
30-30-30  
31-31-31  
32-32-32  
33-33-33  
34-34-34  
35-35-35  
36-36-36  
37-37-37  
38-38-38  
39-39-39  
40-40-40  
41-41-41  
42-42-42  
43-43-43  
44-44-44  
45-45-45  
46-46-46  
47-47-47  
48-48-48  
49-49-49  
50-50-50  
')

---

## CONFIG ZCDx

Action

This statement configures the ZCD(Zero Cross Detector) of the AVRX.

Syntax

CONFIG ZCDx = mode , RUNMODE=runmode, INVERT=invert, OUT_ENABLE=out_enable [, REGMODE=regmode]

Remarks

There can be up to 3 Zero Cross Detectors. The first detector is 0. CONFIG ZCD0 configures the first ZCD.

OPTION | DESCRIPTION  
---|---  
x | Number that identifies the ZCD. Typical from 0-2. Depends on the processor.  
mode | \- DISABLED : The ZCD is disabled.  \- ENABLED : The ZCD is enabled. Enabling the ZCD   
runmode | \- DISABLED : The ZCD is only active when required. \- ENABLED : the ZCD remains active when the device enters standby sleep mode.  
invert | \- DISABLED : The output pin is normal. \- ENABLED : The output pin has inverted output  
out_enable | \- DISABLED : The output pin is not connected to the supported pin \- ENABLED : The output pin is connected to the supported pin  
regmode | \- OVERWRITE : this is the default mode. When using 1 option, the other bits are not preserved and set back to 0(disable).  \- PRESERVE : bits that are not changed are preserved.  See also the [AVRX](avrx.md) description.  
  
You can check the zero cross output in the ZCDx_STATUS register bit 4. 

The ZCD has an interrupt as well. It can be triggered on the rising or falling edge. Or on both. By default interrupts are disabled.

Since there is only one interrupt with 3 settings, you can use ENABLE ZCD0_RISING , ZCD0_FALLING or ZCD0_BOTH. They all trigger the same interrupt.

When you use DISABLE ZCD0_RISING it will disable the interrupt. It does not matter which name you use. We do advise to keep them the same for clarity.

Thus when you ENABLE ZCD0_RISING, use DISABLE ZCD0_RISING to disable when required.

See also

NONE

Example

---

## CONFIGURATION



---
