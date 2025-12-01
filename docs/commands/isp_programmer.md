# ISP programmer

BASCOM supports the STK200 and STK200+ and STK300 ISP programmer from Atmel.

This is a very reliable parallel printer port programmer.

The STK200 ISP programmer is included in the STK200 starter kit.

Most programs were tested with the STK200.

For those who don't have this kit and the programmer the following schematic shows how to make your own programmer:

The dongle has a chip with no identification but since the schematic is all over the web, it is included. MCS also sells a STK200 compatible programmer.

Here is a tip received from a user :

If the parallel port is disconnected from the interface and left floating, the '244 latch outputs will waver, causing your micro controller to randomly reset during operation. The simple addition of a 100K pull-up resistor between pin 1 and 20 of the latch, and another between pin 19 and 20, will eliminate this problem. You'll then have HIGH-Z on the latch outputs when the cable is disconnected (as well as when it's connected and you aren't programming), so you can use the MOSI etc. pins for I/O.

![ISP](isp.gif)

Since parallel printer ports do not exist in new equipment you better use an USB programmer.