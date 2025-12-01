# USBprog Programmer / AVR ISP mkII

The USBprog programmer is a neat small USB programmer which is fully compatible with the AVR ISP mkII programmer.

When you select this programmer, you will get the same interface as for the [STK500 native](stk500_programmer.md) programmer.

F4 will launch the programmer. For more details read the help section for the STK500 programmer.

When programming XMEGA chips the interface for the fuse bits will be different. See [STK600](stk600.md) programmer for a description.

The default clock is 125 KHz. This because most/all chips ship with a clock frequency of 1 MHz. And since the clock frequency maximum is a quarter of the oscillator frequency, the default is 125 KHz, low enough to be able to program all chips. Once your chip runs at say 8 MHz, you can select 2 MHz as the maximum.

You must have the [LIBSUSB](libusb.md) drivers installed on your PC. Without it, it will not work.

Options

In the Configuration options you can adjust the clock speed and the timeout of the USB.

When you are using USB 1.1 and a lot of devices that generate a lot of USB traffic, you might need to increase the default timeout of 100 (msec). 

XMEGA

When used in PDI mode, take care about the following for some of the processors:

JTAG is activated by default which preventing from using the PDI because both interfaced share the same pins. In this case :

1 - Disable the JTAG before using the PDI. > You need a JTAG programmer

2 - Use a 47Kohm resistor to Pull down the clock pin to ground which allow you to have both JTAG and PDI working simultaneously.