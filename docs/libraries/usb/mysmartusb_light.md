# mySmartUSB Light

The mySmartUSB Light programmer is an affordable and versatile ISP programmer. It supports the AVR911 and STK500V2 protocols.

The mySmartUSB Light programmer is available form the [MCS Webshop](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=273&category_id=3&option=com_phpshop&Itemid=1>). It is an USB programmer that requires a virtual COM port driver. When your PC is connected to the internet, the driver will be installed automatically by Windows.

The programmer is either shipped with the AVR911 protocol or the STK500V2 protocol.

The support in BASCOM is for the STK500V2 mode. 

MyAVR has a simple utility that you can use to check and/or change the firmware.

Download it [here](<http://shop.myavr.de/index.php?ws=download_file.ws.php&dlid=197&filename=software/tool_myavr-support-box_en_de.zip>)

When you run the tool you get a window similar to this one:

![myavr_firmware](myavr_firmware.png)

The window above shows that the current firmware is STK500 which is OK.

When the version is AVR911, you can change it by selecting the STK500 1.11.xxxx in the list and click 'BRENNEN' (burning)

The tool also allows to set the voltage of the programmer to 3V or 5V.

And you can turn on the power while burning (this will use internal USB power)

The above options are available from BASCOM as well.

When you press manual program, the following window will be shown:

![mysmartusb_light](mysmartusb_light.png)

The usual options are available. Please read [STK500 Programmer](stk500_programmer.md) for more info.

The MyAVR programmer has a special menu accessible from the Board menu.

Board, MyAVR, Voltage, 3V or 5V. This selects the output voltage of the programmer

Board, MyAVR, Power On Program. This option can be set and cleared. When set, the programmer will route power to the target circuit during programming. 

Board, MyAVR, Board Power, turn on/off. These options can be used to power the target board while not programming. 

When using the options to power the circuit, you should notice that this power is taken from the USB bus. You should take care that your circuit does not draw too much current.

For the manual see : <http://www.myavr.info/download/produkte/mysmartusb_light/techb_mySmartUSB-light_de_en.pdf>