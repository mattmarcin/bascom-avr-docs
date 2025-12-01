# ATMEGA1284P

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![m1284p](m1284p.png)

The M1284 seems to have an internal problem where large amounts of serial data can choke the processor.

A capacitor of 100pF on the RX pin to ground can solve this problem.

More info : [http://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=viewtopic&p=60860#60860](<http://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=viewtopic&p=60860#60860>)