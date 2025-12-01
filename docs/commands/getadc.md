# GETADC

Action

Retrieves the analog value from the specified channel.

Syntax

var = GETADC(channel [,offset])

Syntax Xmega

var = GETADC( ADC , channel [,MUX])

Syntax Xtiny

var = GETADC()

var = GETADC(channel)

var = GETADC(ADC , channel)

Remarks AVR

Var | The variable that is assigned with the A/D value. This should be a Word or other 16 bit variable.  
---|---  
Channel | The channel to measure. This is actual the MUX value that will be used. Most older chips with A/D converter only have 8 channels with singled ended input. Here you would use values from 0-7. Newer chips like the ATMEGA2560 have multiple modes. A MUX value of 0-7 would use single ended input mode and would read ADC0-ADC7. But a value from 8-15 would select differential mode using ADC0-ADC3 with different gain factors. Please have a look in the data sheet to see how the channel value translates into the mode and channel. It is different for most chips.  
Offset | An optional numeric variable of constant that specifies gain or mode. This option has effect on newer AVR microâs only. The offset will be added to the channel value and inserted into the ADMUX register. This way you can control gain.  
  
Remarks XMEGA

var | The variable that is assigned with the A/D value. This should be a Word or other 16 bit variable.  
---|---  
ADC | The ADC to use. This is either ADCA or ADCB.  
Channel | The channel to use. There are 4 channels in the range from 0-3.  
MUX | An optional numeric variable or constant that specifies the MUX value thus which input pin is used for the measurement. The MUX number is coded with negative and positive input pin info. The positive pins are have an offset of 8. So PIN0 in single ended mode would need a value of 8. When you do not supply the mux value, the value used by the CONFIG ADC command will be used. If you supply it, it will change the MUX register of the corresponding channel.  
  
Remarks Xtiny

var | The variable that is assigned with the A/D value. This should be a Word or other 16 bit variable.  
---|---  
ADC | The ADC to use. This is either ADC0 or ADC1.  
Channel | The channel to use. This value depends on the processor. Some channel values access the internal reference or temperature sensor. This value will set the MUX register. When there is no channel provided the current MUX setting will be used. When you define a constant named _adc_kelvin reading the internal temp sensor will return the result in Kelvin.  The value of _adc_kelvin is not important. When you include this constant, the ADC routine will check if the internal temperature sensor is read. If so, the result is compensated with the temp gain and offset. To convert Kelvin to Celsius you can subtract 273.15 from the result.   
  
Note:

It is the users responsibility to check the Channel values are in range.

Please check and consult your Microcontroller Datasheet.

The GETADC() function only will work on microprocessors that have an A/D converter.

The pins of the A/D converter input can be used for digital I/O too.

But it is important that no I/O switching is done while using the A/D converter.

NORMAL AVR

Make sure you turn on the AD converter with the [START](start.md) ADC statement or by setting the proper bit in the ADC configuration register.

Some microâs have more then 7 channels. This is supported as well. The ADCSRB register contains a bit named MUX5 that must be set when a channel higher then 7 is used. The compiler will handle this automatic. This is true for new chips like Mega1280, Mega2560 and probably other new chips with 100 pins.

An example on how to read singled ended input on a Mega1280:

W = Getadc(0, 32) ' from data sheet : 100000 ADC8

W = Getadc(1, 32) ' from data sheet : 100001 ADC9

This will read channel 0 and 1. The offset is 32 in order to use singled ended input. 

ADC8 is portK.0

Without the offset, you need to provide the proper value for the channel.

So GetADC(0,32) would become : GetADC(32)

And GetADC(1,32) would become : GetADC(33)

GetADC() returns a word variable since the A/D converter data registers consist of 2 registers. The resolution depends on the chip.

The variable ADCD can be used to access the data register directly. The compiler will handle access to the byte registers automatically.

See also

[CONFIG ADC](config_adc.md) , [CONFIG ADCA](config_adca.md) , [CONFIG ADC0](config_adc0_adcx.md)

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
Example Xmega

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-ADC.bas  
' This sample demonstrates the Xmega128A1 ADC  
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
  
Print "ADC test"  
  
'setup the ADC-A converter  
Config Adca = Single , Convmode = Unsigned , Resolution = 12bit , Dma = Off , Reference = Int1v , Event_mode = None , Prescaler = 32 , Ch0_gain = 1 , Ch0_inp = Single_ended , Mux0 = &B000_00 _  
```
Ch1_gain = 1 , Ch1_inp = Single_ended , Mux1 = &B1_000 , Ch2_gain = 1 , Ch2_inp = Single_ended , Mux2 = &B10_000 , Ch3_gain = 1 , Ch3_inp = Single_ended , Mux3 = &B11_000  
  
```vb
Dim W As Word , I As Byte , Mux As Byte  
Do  
```
Mux = I * 8 ' or you can use shift left,3 to get the proper offset  
W = Getadc(adca , 0 , Mux)  
```vb
' W = Getadc(adca , 0) 'when not using the MUX parameter the last value of the MUX will be used!  
' use ADCA , use channel 0, and use the pinA.0-pinA.3  
Print "RES:" ; I ; "-" ; W  
```
Incr I  
```vb
If I > 3 Then I = 0  
Waitms 500  
Loop Until Inkey(#1) = 27

```
Example Xtiny

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
  
'configure the internal reference to be 1v1 for both the ADC and the DAC  
Config Vref = Dummy , Adc0 = 1v1 , Dac0 = 1v1  
  
'configure the ADC0 to read the DAC  
Config Adc0 = Single , Resolution = 10bit , Adc = Enabled , Reference = Internal , Prescaler = 32 , Sample_len = 1 , Sample_cap = Above_1v , Init_delay = 32 , Mux = Dac0  
  
'configure the DAC. We do not output the signal on a port pin otherwise out_enable would be required too  
Config Dac0 = Enabled  
  
'dimension a variable  
Dim W As Word , B As Byte  
  
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
```
Incr B  
```vb
Loop Until B = 3  
  
'now read the internal temp sensor  
```
Const _adc_kelvin = 1  
Do  
W = Getadc(&H1e) 'get internal temp sensor value  
```vb
Print W 'this is in KELVIN  
'to adjust to Celsius, sub 273.15  
Waitms 1000  
Loop  
  
End

```