# LIBUSB

Using USB programmers in BASCOM-AVR

Please read this document completely before starting to install software.

Like every other USB device, an USB programmer requires a windows driver. Some programmers use drivers that are provided (built into) by windows. For example the KamProg uses the HID class and does not require an additional third party driver.

A programmer like the AVRISP mkII does need an additional driver. This device driver is installed when you install AVR Studio.

Studio is using device drivers from JUNGO. 

When you plug in the programmer and Windows informs you that it requires a driver you know that you need to install a third party driver.

When Windows does not complain it will use a driver already available on your PC.

Most USB devices need software installed before you plug them in for the first time. In many cases there is a warning sticker that you should first install the software.

BASCOM uses LIBUSB to access USB devices. LIBUSB is available as a device driver or as a filter driver. 

When your device is using a device driver you must access the device with a filter driver.

Some devices do not have a vendor supplied driver (USBASP programmer) and those require a device driver.

Scenario one : you have a 32 bit or 64 bit OS and have a product that uses a device driver.

In this example we use the AVRISP mkII that is supported by AVR Studio. When you do not have AVR Studio installed you can download it from Atmels website for free.

The original programmer comes with a CD-ROM too. But many imitation/self build devices exist that do not come with a CD. For those you need to download and install AVR Studio.

The next step is to plug your programmer, and see if it works with AVR Studio.

Windows will recognize it, and install the device driver. 

When windows is ready, press the connect button in Studio.

![libusb_selectavrprog](libusb_selectavrprog.jpg)

If you open Studio, and press the CON(nection) button, the window shown above will open.

Now select your programmer, in this sample AVRISP mkII and press Connect

When it functions, a new window will open 

![libusb_stk500](libusb_stk500.jpg)

You can select the device, the programming mode and ISP frequency. This frequency should be 125 KHz (or better said, should not exceed a quarter of the chip oscillator frequency).

When you do not get this window but you return to the connection window, it means your programmer is not working.

You have to solve this first before you can continue.

The programmer will only work in BASCOM when it functions with the original software!

In the windows device manager, you can find this info: (right click Computer, select manage, and chose device manager)

![libusb_devmng](libusb_devmng.jpg)

The screen above shows the JUNGO usb driver which Atmel AVR Studio uses and the AVRISP mkII driver for the AVRISP mkII. 

If you install AVR Studio with the USB drivers, it will install JUNGO and the WinDriver. The AVRISP mkII entry you only get when you plug the programmer. 

To make it work with BASCOM, you need to install LIBUSB. LIBUSB is used by many different programs. Atmels FLIP is using it too. So there is a big change that it is available on your system already.

You can install LIBUSB as a FILTER driver or a DEVICE driver.

We install the FILTER driver, so we can use the programmer with Studio AND bascom.

![notice](notice.jpg)Before you install LIBUSB it is a good idea to make a restore point.

![notice](notice.jpg)When installing the USB driver, disconnect ALL USB devices. Obvious, you can not install from an USB flash drive since this is an USB device as well.

You can read about LIBUSB and download it from : <http://sourceforge.net/apps/trac/libusb-win32/wiki>

The last version is : <http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.4.0/libusb-win32-devel-filter-1.2.4.0.exe/download>

Notice that this an executable you can install. You MUST have ADMIN rights when you install this executable.

After LIBUSB has been installed you can test if it is functional.

\- Look in the Program Files\LibUSB-Win32 folder (also named on Windows-7 64 bit !!!)  
You will find a sub folder named bin which contains a number of executables.

\- Run the testlibusb-win.exe application. When LIBUSB is functional you will see a screen with all USB devices. 

When it does not work, try to install again with compatibility mode set to XP SP2.

Do this by selecting the the setup exe file properties, and select 'Compatibility'. 

![libusb-compat](libusb-compat.png)

Click Apply and/or OK. And run setup again.

On Windows 7 - 64 bit, this was NOT required. 

Once the testlibusb-win.exe works, you can continue to the next step.

Install the filter driver for the device

You need to install a filter driver for your programmer. Each different programmer requires it's own filter driver. So you must repeat these steps if you have different programmers.

\- Plug in your programmer if it was not plugged in yet

\- Run the install-filter-win.exe application from the BIN folder. 

\- You will see this window:

![libusb_filter_driver](libusb_filter_driver.jpg)

Select 'Install a device filter' and press Next.

![libusb_filter_driver_atmel](libusb_filter_driver_atmel.jpg)

Select the programmer and press Install.

After some moments, you will get a confirmation:

![libusb_filter_ok](libusb_filter_ok.jpg)

Now the programmer will work in BASCOM. Just select the proper programmer, and timeout of 100 ms. You can try lower time outs too to make it quicker. When you get errors, increase the time out. 100 ms should do for all programmers.

Scenario two: you do not have a device driver.

In this case you can follow scenario one till the filter driver installation.

Instead of running install-filter-win.exe , you will run inf-wizard.exe.

![libusb_infwiz](libusb_infwiz.jpg)

Press Next. And the following window will be shown.

![libusb_infwizusbasp](libusb_infwizusbasp.jpg)

As you can see, the USBASP was inserted in this sample. Select it (or your programmer) and press Next.

![libusb_infwiz_devsel](libusb_infwiz_devsel.jpg)

Press Next again and select a folder to store the device driver files.

These files are required to install the device. 

![libusb_infwiz_save](libusb_infwiz_save.jpg)

After you have saved the files, you have the option to install the driver. Press Install Now.. button to do so.

![libusb_dev_ready](libusb_dev_ready.jpg)

When ready :

![libusb_infwiz5](libusb_infwiz5.jpg)

Final note

The USB-ISP programmer form EMBUD, uses drivers from FTDI. It does not require LIBUSB.

The Kamprog programmer from KAMAMI uses a HID class and does not require LIBUSB.

Some devices gave a problem in 1.2.3.0. This problem is solved in 1.2.4.0.

<http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.4.0/libusb-win32-devel-filter-1.2.4.0.exe/download>