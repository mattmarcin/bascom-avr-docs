# ATXMEGA64A1

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega128](atxmega128.png)

Here a note about the spike detector :

>The calibration byte in the production signature row show 0xFF and 0x00  
>for the ADC Calibration byte. Are these really the calibration values ?  
>And I'm not able to set the HIGH Byte of the calibration register.  
>Errata of Rev H don't show something from calibration bytes.

Reply from Atmel :

The voltage spike detector has been removed from the latest revision of the XMEGA A manual.  
This is because we have, unfortunately, not been able to validate the spike detector fully.  
The module is disabled in currently available parts to avoid unforeseen problems for any customers.