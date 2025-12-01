# MEGAX

At MCS we refer to the new range of MEGA processors as the MEGAX. This because they look like Xmega processors but smaller.

Since the name XMEGA was taken by the actual XMEGA, and we use XTINY for the attinyX processors, we use MEGAX.

So why this distinction? And not use the atmel/microchip name? The answer is simple. 

By using different names for the DAT file we want to make it clear that some hardware is different. 

In fact these are all AVR chips but the core differs. As a user you do not need to care much. You can use the processors as usual.

The only important change is the programmer interface which is UPDI. Which is supported by BASCOM.

XMEGA and XTINY users will find many similar options. We based XTINY support on XMEGA. And MEGAX support on XTINY.

If you are unfamiliar with XTINY/MEGAX you best read the information about [XTINY](xtiny.md).

In fact we list all the differences under the XTINY topic. When not mentioned otherwise, the same applies for MEGAX.

The MEGAX is a bigger XTINY with more memory and hardware.

Some also come in DIP form.

We will only list the differences here with the XTINY.

![notice](notice.jpg)When you find info about the XTINY in the help, this info is also for the MEGAX unless there is a note about a difference. So when you read XTINY you can consider it equal to MEGAX.

Like the XTINY the MEGAX requires an add on. This is the same add on as the XTINY. So the XTINY Add On supports the MEGAX processors as well. 

Use the update function to update the add on. 

All tests have been performed using the MEGA4809-40 pins DIP. 

\- The biggest difference with XMEGA is that the MEGAX voltage range goes up to 5V. 

\- Biggest difference with XTINY is that there is more hardware like multiple USART's.

See also

[AVRX](avrx.md) , [XTINY](xtiny.md)