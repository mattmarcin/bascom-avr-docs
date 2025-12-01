# CONFIG SYSCLOCK XMEGA

Action

Selects the oscillator source for the system clock.

See also [ATXMEGA](atxmega.md)

Syntax

CONFIG SYSCLOCK=sysclock , PRESCALEA=prescaleA,  PRESCALEBC=prescaleBC

Remarks

SYSCLOCK | The oscillator used for generation of the system clock. This oscillator must be running. You MUST use CONFIG OSC before you use CONFIG SYSCLOCK. The CONFIG SYSCLOCK will wait till the oscillator is running stable. Possible values: \- 2MHZ \- 32MHZ \- EXTERNAL \- PLL  
---|---  
PRESCALEA | The Xmega has 3 prescalers. With PRESCALEA you configure the clock division of the first prescaler. Possible values: 1 , 2 ,4, 8, 16, 32, 64, 128,256,512  
PRESCALEBC | The Xmega has 3 prescalers. With PRESCALEBC you configure the clock division of the second and the third prescaler. Possible values: \- 1_1 (1 + 1 division) \- 1_2 (1+2 division) \- 4_1 (4 + 1 division) \- 2_2 (2 + 2 division) This 1_2 will make the second prescaler divide by 1 and the third prescaler divide by 2.  
  
See also

[CONFIG OSC](config_osc.md)

Example

Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1 ' use 32 MHz