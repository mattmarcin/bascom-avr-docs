# CONFIG VREF

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