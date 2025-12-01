# START

Action

Start the specified hardware source.

Syntax

START device [ , cfg]

Remarks

Device | TIMER0, TIMER1, COUNTER0 or COUNTER1, WATCHDOG, AC (Analog comparator power), ADC(A/D converter power) or DAC(D/A converter).  
---|---  
XMEGA | For the Xmega you can also specify : DACA or DACB for the Digital/Analog Converters A and B. ADCA and ADCB for the A/D converters. For the timers you can use TCC0, TCC1, TCD0, TCD1, TCE0, TCE1, TCF0 and TCF1. To start a DMA soft transfer, you can use DMACH0, DMACH1, DMACH2 or DMACH3. The transfer starts after the DMA channel is ready.  For Xmega with Enhanced DMA, use EDMACH0, EDMACH1, EDMACH2 and EDMACH3.  
cfg | The optional cfg is only used for the TIMER when the optional CONFIGURATION is used. If CONFIG TIMERx = option , CONFIGURATION=mysetting was used, you would specify START TIMERx, mysetting.  
  
When you configure a timer (CONFIG TIMER), the TIMER is started automatically when a pre-scaler value is provided.

When you want to halt the timer you can use the STOP TIMER statement. To start the timer after it has been stopped, you can use the START TIMER statement. The START TIMER statement will only work correctly when you have selected a clock source or pre-scaler value with the CONFIG TIMER statement.

When you stored settings using the option CONFIGURATION=setting , then you can specify which configuration the timer must use by providing the setting name as a parameter : START TIMER1 , mysetting

When a timer is used in interrupt mode, it must be running otherwise the interrupt will never occur. 

TIMER0 and COUNTER0 are the same device. And so are TIMER1 and COUNTER1. 

The AC, ADC and DAC parameters will switch power to the device and thus enabling it to work.

The WATCHDOG parameter will activate the Watchdog.

See also

[STOP](stop.md)

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

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'configure single mode and auto prescaler setting

'The single mode must be used with the GETADC() function

'The prescaler divides the internal clock by 2,4,8,16,32,64 or 128

'Because the ADC needs a clock from 50-200 KHz

'The AUTO feature, will select the highest clockrate possible

Config Adc = Single , Prescaler = Auto

'Now give power to the chip

```
Start Adc

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