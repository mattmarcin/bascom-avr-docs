# CONFIG ADC

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