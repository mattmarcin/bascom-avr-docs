# CONFIG OSC XTINY

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