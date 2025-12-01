# CONFIG OSC XMEGA

Action

Select and enable the oscillators available to the Xmega 

See also [ATXMEGA](atxmega.md)

Syntax Xmega

CONFIG OSC=ENABLED|DISABLED , PLLOSC=ENABLED|DISABLED,  EXTOSC=ENABLED|DISABLED, 32KHZOSC=ENABLED|DISABLED,  32MHZOSC=ENABLED|DISABLED,  RANGE=range, 32KHZPOWERMODE=powermode, XOSC_SEL__STARTUP=xosc_sel_startup , PLLSOURCE=pll , PLLDIV2=plldiv , PLLMUL=pllmul , 32MHZCALIB= 32mhzcalib , 2MHZCALIB= 2mhzcalib , 2MHZDFL= 2MHZDFL , 32MHZDFL= 32MHZDFL

Remarks

OSC | Use ENABLED to enable the internal 2 MHZ oscillator. This oscillator is enabled by default. Use DISABLED to disable the internal oscillator.   
---|---  
PLLOSC | Use ENABLED to enable the PLL oscillator. The oscillator is disabled by default.  
EXTOSC | Use ENABLED to enable the external oscillator. The external oscillator is disabled by default.  
32KHZOSC | Use ENABLED to enable the internal 32 KHz oscillator. This oscillator is disabled by default.  
32MHZOSC | Use ENABLED to enable the internal 32 MHz oscillator. This oscillator is disabled by default.  
RANGE | Specify the range of the external oscillator.  \- 400KHZ_2MHZ \- 2MHZ_9MHZ \- 9MHZ_12MHZ \- 12MHZ_16MHZ This option is only needed when using the external oscillator.  
32KHZPOWERMODE | Select the power mode of the 32 KHz interal oscillator. This can be NORMAL or LOW_POWER. The default is NORMAL  
XOSC_SEL_STARTUP | The type and startup type of the crystal or resonator can be specified. Use a value of : \- EXTCLK (6 CLK) , will select external clock  \- 32KHZ (for 16 CLK) , will select 32.768 TOSC \- XTAL_256CLK (for 256 CLK), will select 0.4-16 MHz XTAL \- XTAL_1KCLK (for 1K CLK) , will select 0.4-16 MHz XTAL \- XTAL_16CLK (for 16K CLK) , will select 0.4-16 MHz XTAL  
PLLSOURCE | This option let you select the oscillator source of the PLL oscillator. Valid options are : \- RC2MHZ , the internal 2 MHz oscillator (default) \- RC32MHZ , the internal 32 MHz oscillator \- EXTCLOCK , an external clock signal or oscillator  
PLLDIV2 | This option let you select the PLL two divider. Valid options are ENABLED and DISABLED  
PLLMUL | This option let you specify the PLL multiplication factor. The numeric value must be in the range from 1-31. A value of 0 disables the multiplication.  
32MHZCALIB | This option allow you to specify the calibration source for the 32MHZ oscillator. The possible options are : \- RC32K , selects the 32.768 KHZ internal oscillator \- XOSC32, selects the 32.768 KHz crystal oscillator on TOSC \- USBSOF , selects USB start of frame  
2MHZCALIB | This option allow you to specify the calibration source for the internal 2MHZ oscillator. The possible options are : \- 32KHZINT , selects the 32.768 KHZ internal oscillator. (default) \- 32KHZ_EXT_TOSC, selects the 32.768 KHz crystal oscillator on TOSC  
32MHZDFL | This option will enable or disable the DFLL and auto calibration of the 32 MHZ oscillator. Possible values : \- ENABLED \- DISABLED  
2MHZDFL | This option will enable or disable the DFLL and auto calibration of the 2 MHZ oscillator. Possible values :  \- ENABLED \- DISABLED  
  
You can also use automatic calibration. This will calibrate the 32 MHz oscillator using the 32 KHz oscillator.

The required code :

```vb
Config Osc = (enabled or disabled), 32mhzosc = Enabled , 32khzosc = enabled

Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
```
OSC_DFLLCTRL.0 = 1 'enable   
DFLLRC32M_CTRL.0 = 1 'enable

See also

[CONFIG SYSCLOCK](config_sysclock.md)

Example

Config Osc = Enabled , 32mhzosc = Enabled ' enable 2 MHz and 32 MHz interal oscillators

PLL Example

```vb
'Clock: 32 MHz External 4 MHz Xtal, PLL x 8

Config osc = enabled , EXTOSC = enabled , pllosc = enabled , _

```
range = 2MHZ_9MHZ , startup = XTAL_16KCLK , pllsource = extclock , pllmul = 8

Config Sysclock = Pll , Prescalea = 1 , Prescalebc = 1_1