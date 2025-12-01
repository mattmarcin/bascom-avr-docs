# CONFIG POWERMODE

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