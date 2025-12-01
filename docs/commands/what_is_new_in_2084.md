# What is new in 2084

version 2084.001  
  
\- mega4809 added to xtiny platform. See also [MEGAX](megax.md)

\- xtiny support added to i2cslave add on. 

\- [LCD I2C](lcd_i2c_pcf8574.md) driver from O-Family included that supports up to 8 LCD.

\- xtiny alias portx,ddrx and pinx have been changed from the port_out to the virtual address. this also required the following :

\- 1wire,i2c,getrc,pulsein,pulseout,serout,serin,i2cbus and rainbow changed for new port mapping

\- [config COM](configcomx.md) for xtiny has a new option to chose the alternative pin. TXPIN=option

\- xtiny TCB0: CCMP_OTP renamed into CCMP_OUTPUT. Also reversed enable/disable. And ASYNC enabled/disabled were reversed too.

\- xmega dat files corrected for DACA/DACB. 

\- xmega config eeprom=quick|mapped did not simulate properly

\- xtiny config port_mux did not set the proper register value for TCAx and TCBx

\- portmux support complete rewritten. data is stored in the dat files. see also [config_portmux](config_port_mux.md) for important information.

most choices list the pin number name now.

\- [sizeof](sizeof.md)() function added. it returns the size of a variable in memory. 

\- xtiny config sysclock prescaler value 6 was missing.

\- simulator fix for xtiny (register offset). Also register name length extended to 32 characters

\- htrc110.LBX added * for used equ so they can be adjusted by the user

\- DTR option for terminal emulator. you can set the DTR pin level for the terminal emulator just like you can for the RTS pin.

\- mysmartusb light programmer problem with EEPROM programming solved

\- const [_TEXTLCDKIND](config_lcd.md) added which contains the text LCD kind like : 162 for 16x2

\- the tool tip info (SHIFT key) shows the length of a string constant when moving over a string constant.

\- xtiny support added for AVR-DOS

\- serin/serout implemented for xmega and xtiny

\- [SWAP](swap.md) can swap a long/dword too

\- glcdST7565R.lib adjusted for RAMPX boundary in showpic

\- xtiny enable/disable set wrong bits for the timers

\- xtiny start/stop switch the enable bit for timers

\- datetime.lib modified for xtiny

\- split() did not raise an error when using non-strings. The result array must be a string array.

\- syntax check/compile did reset the stk200 programmer reset pin

\- xtiny tcb1 added which was missing.

\- UPDI programmer speed increased. baud is selectable. 225000 is the maximum for the default updi clock.

\- IDE did not compile for the right processor when multiple $regfile directives were used with #IF#ENDIF.

\- Font size increased in IDE. Default is now SEGUI 12. When you use a different language in options, this might not be visible. 

Also changed IDE so that high resolution monitor should show better font when bigger fonts are chosen. The icons/images still need to be changed to vector drawn images so they can scale better. 

\- more xtiny samples

\- IDE can [update](updates.md) a number of add ons