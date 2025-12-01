# CONFIG ADC0-ADCX

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