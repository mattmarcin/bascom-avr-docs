# USBASP

The USBASP is a popular USB programmer created by Thomas Fischl

The programmer uses a Mega8 or other AVR chip as an USB device.

You can find the programmer at Thomas website :  <http://www.fischl.de/usbasp>

Make sure when programming the fuse and lock bits that the selected clock frequency is not too high. The clock frequency of the ISP programmer should be less then one quarter of the oscillator frequency. When your micro is running at 8 MHz, you can select up to 2 MHz. On the safe size, 125 KHz is always ok.

By default most AVR processors run at 8 MHz with an 8-divider resulting in 1 MHz clock frequency. So 250 KHz is a safe value for most processors.

![usbasp](usbasp.png)

You can select various clock frequencies. 

See also [LIBUSB](libusb.md) for installation of LIBUSB