# ATMEGA324PB

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![m324pb](m324pb.png).

There is a bug in the chip : When you configure the second UART, the timer1 channel B will not work.

This info came from microchip :

Yes, your observation is correct. It is a known device bug. We already 

report this bug to our concern team.

This is due to the fact that timer 1 channel B is shared with XCK1 pin 

of UART1

Usually this functionality should take priority over timer 1 channel B 

only when UART is configured in Synchronous mode but after discussing 

with our internal team confirmed that timer 1 channel B is 

disconnected based on UART1 activation

No matter even if the UART is configured in Asynchronous mode(in which 

case there is no use of XCK1) timer 1 channel B still gets disconnected.

This issue also presents in UART2 XCK2/OC2A.