# ATTINY4313

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![tiny2313](tiny2313.zoom80.png)

The tiny4313 has an internal oscillator that can run at various frequencies. The 4 MHz seems not to work precise. when using the UART for serial communication you can get wrong output. You can best use the 8 MHz internal oscillator , or tweak the UBRR register. For example, UBRR=UBRR+1

That worked for 4 Mhz, at 19200 baud.