# CONFIG ADCA|ADCB

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