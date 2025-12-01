# ATTINY44

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![attiny24_44_84](attiny24_44_84.png)

The data sheet does not specify that HWMUL is supported. The DAT file reflect this :

HWMUL=0 ; this chip does not have hardware multiplication

Some users reported that the HWMUL did work. Some batches might support the HW MUL, but since we found chips that did not, the value is set to 0. You can change it at your own risk.