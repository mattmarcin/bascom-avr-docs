# CONFIG ZCDx

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