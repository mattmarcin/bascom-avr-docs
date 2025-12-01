# CONFIG VREGPWR

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