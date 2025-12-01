# USB Libraries

> USB communication

## AT90USB1286

![at90usb1287](at90usb1287.png)

---

## AT90USB1287

![at90usb1287](at90usb1287.png)

---

## AT90USB162

The USB162 is supported by the optional USB Add On. PORTC.4 is used to sense the power of the USB bus.

![at90usb_82_162](at90usb_82_162.png)

---

## AT90USB646

![at90usb1287](at90usb1287.png)

---

## LIBUSB

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

---

## mySmartUSB Light

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

---

## USB Add On

The USB Add On is a commercial add on which is available from the MCS Electronics Web Shop.

The CONFIG USB statement needs this add on. The add on is written in BASCOM BASIC mixed with assembler. Since the examples from Atmel were not really consistent, it took some effort to create reusable code. At a later stage, a number of routines will be moved to an assembler library. 

The advantage of the BASCOM code is that it is similar to the C-code examples. 

![notice](notice.jpg)Please read this entire topic first before you start with experiments. 

The Add On only supports the device mode. There is no support for host mode yet. In fact the add on is just the first step into USB support. 

To use the USB Add on, unzip all the files to the SAMPLES\USB directory. 

You will find three samples :

•| hid_generic-162.bas  
---|---  
  
•| virtcom-162.bas  
---|---  
  
•| hid_keyboard-162.bas  
---|---  
  
The same samples are also provided for the USB1287.

And you will find the include file : usbinc.bas. It is not allowed to distribute any of the files. 

Further, you will find a subdirectory named VB which contains a simple VB generic HID sample that uses the HIDX.OCX from the OCX subdirectory.

The PDF directory contains a PDF with a translation between PS2 scan codes and USB key codes.

The TOOLS directory contains the USBDEVIEW.EXE which can be used to display all USB devices,

The CDC-Driver directory contains the INF file you need for the CDC/Virtual COM port example.

The USB162 has a boot loader which can be programmed by USB using FLIP. BASCOM will also support this USB boot loader in version 1.11.9.2.

It is great for development but of course the boot loader uses some space which you probably need. The chip is also programmable via the normal way with the ISP protocol. when you do not use FLIP, and you erase the chip, the boot loader from Atmel is erased too! You can always reprogram the Atmel boot loader. But not using FLIP which depends on the boot loader.

For USB to work properly the chip needs a good oscillator. The internal oscillator is not good enough. For that reason, the USB162 module from MCS has a 8 MHz crystal. Your hardware should use a crystal or crystal oscillator too.

It is not the intention of MCS or the documentation to learn you everything about USB. There is a lot of information available from various sources. It is the goal of MCS to make it easy to use USB with your AVR micro. When there is enough demand for it, a special Wizard will be created to be able to generate HID applications.

HID Keyboard

Let's begin with a simple program. Load the hid_keyboard-162.bas sample and compile it. Use either FLIP or a different programmer to program the chip. Each program has some important settings.

Const Mdbg = 1 ' add print to see what is happening

Const Chiddevice = 1 ' this is a HID device

MDBG is a constant that can be set to 0 since all the print statements will use flash code. When you are new to USB and want to look at the events, it is good to have it turned on. You can view all events from the program.

cHIDdevice need to be set to 1 when the application is a HID device. Most of your own devices will be HID devices. But the virtual COM example uses a different USB class and in that program, the constant is set to 0.

These constants are used in the add on to keep all code generic for all applications.

Since not all USB chips have the same options, the code also checks which microprocessor is used.

The USB1287 is a kind of M128 with USB support. It supports host and device mode. The USB162 is a cheap host chip. It does not support the HOST mode and it does not have all registers found in the USB1287. It also can not detect when a device is plugged/unplugged.

Atmel solved this in the STK526 in a simple way that we recommend too : A voltage divider is connected to PORTC.4 which serves as a simple way to detect plug/unplug. 

In the USB_TASK() routine you will find this code :

If Usb_connected = 0 And Pinc.4 = 1 Then ' portc.4 is used as vbus detection on stk526

This is used with the STK526. If you want to use a different pin, you have to change PINC.4.

When you use the USB1287 this is not needed since the 1287 has a Usbsta register which can determine if a device is plugged or removed.

The USB program structure is always the same :

1.| constants are defined that describe the end points, interfaces, vendor ID, product ID  
---|---  
  
2.| you call a subroutine that initializes your variables  
---|---  
  
3.| In a loop you call :  
---|---  
  
4.| the generic USB_TASK routine so that the USB communication with the PC is executed  
---|---  
  
5.| the specific task is called  
---|---  
  
6.| your other code is called  
---|---  
  
This is clear in the keyboard sample :

Print "init usb task"

Usb_task_init

Do

Usb_task

Kbd_task

```vb
'call your other code here

Loop

While the word Task might give you the idea that multi task switching is used, this is not the case! The USB_Task must be called by your code in order to process pending USB events. It will also find out if a device is plugged or unplugged. Events are handled in the background by the Usb_gen_int interrupt. 

```
In the example the KBD_TASK is a user routine which is called in regular intervals. There is always the normal USB_TASK and there is an additional task specific to the program. In the generic-hid example this is the hid_task routine.

HID classes are simple to use since they do not require additional drivers. FTDI chips need additional drivers. But the Atmel USB chips do not need additional drivers since they use standard implemented HID classes.

When you compile the program and program it into a chip you are ready to test it. 

When you use FLIP you need to switch to application mode so your device can be recognized by windows. Windows will show some info that your device is found. And after installing the driver, it will report that your device is ready to be used.

On the terminal emulator, press a space, and set the focus to notepad or the bascom editor. The text data from the keys: label is send as if it was typed on a keyboard! You in fact created a HID-keyboard, or USB keyboard. The document translatePS2-HID.pdf contains HID key codes which are different then PS2 key scan codes. 

When you do not have a terminal emulator connected you can also modify the program and connect a push button. Which makes more sense for a keyboard :-)

So modify the code into : If Inkey() = 32 Or Pinb.0 = 0 Then 'if you press SPACE BAR or make PINB.0 low

Now you can test the code without the terminal emulator.

All USB programs are similar. You specify the number of end points , the interfaces and the class. There is a lot of information available at 

<http://www.usb.org/home>

Atmel has a number of samples and you will find tools and info at various places. 

MCS will publish some convenient tools too.

FLIP

The USB chips are programmed with a boot loader. This is very convenient since you do not need any hardware to program the chip. FLIP can be downloaded from the Atmel site.

URL : <http://www.atmel.com/dyn/resources/prod_documents/Flip%20Installer%20-%203.3.1.exe>

The FLIP website you can find at : [http://www.atmel.com/dyn/products/tools_card.asp?family_id=604&family_name=8051+Architecture&tool_id=3886](<http://www.atmel.com/dyn/products/tools_card.asp?family_id=604&family_name=8051+Architecture&tool_id=3886>)

FLIP is a Java application. The BASCOM-IDE can use the FLIP software to program the chip too. But in order to use the FLIP programmer, you need to install FLIP first. 

When FLIP is working, you can select FLIP from Options, Programmer, in order to program quickly without the FLIP executable.

On Vista there is a problem with loading some of the FLIP DLL's. In case you get an error, copy the FLIP DLL's to the BASCOM application directory.

You need to copy the following files :

•| atjniisp.dll  
---|---  
  
•| AtLibUsbDfu.dll  
---|---  
  
•| msvcp60.dll  
---|---  
  
•| msvcrt.dll  
---|---  
  
You can run the flipDLLcopy.cmd file from the BASCOM application directory to copy these files.

The content of the command file :

copy "c:\program files\atmel\flip 3.3.1\bin\atjniisp.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\AtLibUsbDfu.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\msvcp60.dll" .

copy "c:\program files\atmel\flip 3.3.1\bin\msvcrt.dll" .

pause

The last line pauses so you can view the result. Notice the . (dot) that will copy the file to the current directory, which is the reason that you need to run this file from the BASCOM application directory.

As with other programmers, you press F4 to program the HEX file into the chip. A small window will become visible.

A number of dialogs are possible:

![flip_error_wrongdevice](flip_error_wrongdevice.png)

In this case, you try to program a chip which is not supported by FLIP. The Mega88 is not an USB chip so the error makes sense.

The next dialog informs you about a missing DFU device. 

![flip_reset](flip_reset.png)

In this case, the boot loader is not found. You can run the boot loader by following the sequence from the dialog box.

In order to make this work, the HWB and RST input both need a small switch to ground.

When HWB is pressed(low) during a reset, the boot loader will be executed. 

In the device manager you will find the USB device :

![usb_dev_manager](usb_dev_manager.png)

When you have a different chip, a different device will be shown !

When the programming succeeds, and there is no verify error, the application mode will be selected. This will disconnect the DFU and will connect your USB device !

![flip_ok](flip_ok.png)

The FLIP programmer window will be closed automatic when the programming succeeds.

The USB device will be shown :

![usb_device_KB](usb_device_kb.png)

Since you created a keyboard device, the device will be shown under the KEYBOARDS node. 

When you load a generic HID device it will be shown under HUMAN INTERFACE DEVICES

![usb_generic](usb_generic.png)

HID Generic

The generic HID class is the class that is well suited for transferring bytes between the PC and the micro processor.

As with any USB application, you specify the number of end points, The example just transfers 8 bytes in and 8 bytes out.

You need to change the Ep_in_length_1 , Ep_out_length, Length_of_report_in and Length_of_report_out constants when you want to transfer a different amount of bytes.

You also need to take into account the maximum data size which will depend on the used chip.

The  Usb_user_endpoint_init sub routine also need to be adjusted. The size_8 constant specifies how many bytes are used by the endpoint.

```vb
'init the user endpoints

Sub Usb_user_endpoint_init(byval Nm As Byte)

```
Call Usb_configure_endpoint(ep_hid_in , Type_interrupt , Direction_in , Size_8 , One_bank , Nyet_enabled)

Call Usb_configure_endpoint(ep_hid_out , Type_interrupt , Direction_out , Size_8 , One_bank , Nyet_enabled)

End Sub

As with all USB program, we first initialize the USB task and the HID task. Then we call the tasks in a loop ;

Usb_task_init ' init the usb task

Hid_task_init ' init the USB task

Do

Usb_task 'call this subroutine once in a while

Hid_task 'call this subroutine once in a while

```vb
'you can call your sub program here

Loop

```
The Hid_task itself is very simple :

```vb
Sub Hid_task()

If Usb_connected = 1 Then ' Check USB HID is enumerated

```
Usb_select_endpoint Ep_hid_out ' Get Data Repport From Host

If Ueintx.rxouti = 1 Then ' Is_usb_receive_out())

Dummy1 = Uedatx : Print "Got : " ; Dummy1 ' it is important that you read the same amount of bytes here as were sent by the host !

Dummy2 = Uedatx : Print "Got : " ; Dummy2

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Usb_ack_receive_out

```vb
End If

If Dummy1 = &H55 And Dummy2 = &HAA Then ' Check if we received DFU mode command from host

```
Usb_detach ' Detach Actual Generic Hid Application

```vb
Waitms 500

Goto &H1800 'goto bootloader

'here you could call the bootloader then

End If

```
Usb_select_endpoint Ep_hid_in ' Ready to send these information to the host application

If Ueintx.txini = 1 Then ' Is_usb_in_ready())

Uedatx = 1

Uedatx = 2

Uedatx = 3

Uedatx = 4

Uedatx = 5

Uedatx = 6

Uedatx = 7

Uedatx = 8

Usb_ack_fifocon ' Send data over the USB

```vb
End If

End If

End Sub

```
We first check if the device is connected to the USB bus. Then we use Usb_select_endpoint with the number of the end point, to select the end point. 

When we want to communicate with an end point, we always have to select this end point using the Usb_select_endpoint procedure.

In the sample, we first select the EP_HID_OUT end point. We check the UEINTX.RXOUTI flag to determine if we received an interrupt with data. If that is the case, we read the UEDATX register to read the data byte.

The UEDATX register is the USB data register. When you read it, you read data from the USB bus. When you write it, you write data to the USB bus.

After reading the bytes you MUST acknowledge with the Usb_ack_receive_out macro.

The sample also shows how to run the boot loader from your code. In order to run the boot loader you must detach the current device from the USB bus. Then there is some delay to have windows process it. Finally the GOTO jumps to the boot loader address of the USB162. 

If you want to write some data back, you need to select the end point, and check if you may send data. If that is the case, you assign the data to the UEDATX register and finally, you MUST acknowledge with the USB_ACK_FIFOCON macro.

Finally, you will find in the report data the length of the end points specified : Data &H75 , &H08 

You need to adjust these values when you want to send/receive more data.

HIDX.OCX

There are plenty of examples on the internet that show how to communicate with HID devices using the windows API.

The HIDX.OCX is an OCX control that can be used for simple communication. 

Like all OCX controls, you must register it first with REGSVR32 : regsvr32 hidx.ocx

After it has been registered you can run the VB test application named HIDdemo.exe.

The application will list all HID devices :

![hid_ocx1](hid_ocx1.png)

Our device is the device with VID 16D0 and PID 201D.

There can only be one application/process at the time that communicates with an USB device. 

You must click the checkout-button the device to start communication. This will call the SelectDevice method of the OCX.

As soon as you do this, you will notice that the OnDataRead event will receive data.

![hid_ocx2](hid_ocx2.png)

The event has the following parameters :

(ByVal Device As Long, ByVal ReportID As Long, ByVal Data As String, ByVal Size As Long)

The device is a number with the index of all HID devices. The first device will have number 0. The report number is passed in ReportID. The data is passed as a string. 

You can use MID to access this data : firstByte= Asc(Mid(data,1,1))

To write to the device, you can use the WriteDevice method. The same parameters are used as with the OnDataRead event.

Example : WriteDevice curdev, 0, s, 8

Curdev is the index of the device. 0 is the report ID and s contains the data. You must specify the length of the data to send. 

To stop communication you can click the Checkin-button.This will call the ReleaseDevice method.

When the device changes, or will be removed or inserted, you will receive a notification.

In the sample program, all these events will result in a release of the device. This is done since the curdev variable can change when a new device is added. The index will not correspond to the existing index then anymore. The sample is very simple. In an application you could add a function or procedure that will examine the new list of devices and return the index of our device. When our device is found we could open it automatic again. 

Notice that you can not add too much lines to a listbox in VB. Since data arrives at a very high rate, it will not take long before VB/Windows will give some error.

Property | Description  
---|---  
NumCheckedInDevices | Number of available devices  
NumCheckedOutDevices | Number of devices that are checked out and communicating.  
NumUnpluggedDevices |   
  
DevThreadSleepTime | The time in mS that the HID thread will sleep. You can see this as a timer interval. The lower the interval the more process time it will take. 100 mS is a good value for most applications.  
Version | The version of the control  
DeviceCount | The number of devices.  
  
|   
  
Methods |   
  
SelectDevice | Parameters | •| Device : LONG that specifies the index of the device to select. The index starts at 0.  
---|---  
  
ReleaseDevice | Parameters | •| Device : LONG that specifies the index of the device to release. The index starts at 0.  
---|---  
  
WriteDevice | Parameters | •| Device : LONG that specifies the index of the device to write to. The index starts at 0.  
---|---  
  
•| Report : LONG that specifies the report number. This would be 0 in most cases.  
---|---  
  
•| Data : string that contains the data to send.   
---|---  
  
•| Size : the length of the data to send.   
---|---  
  
  
|   
  
Events |   
  
OnDeviceChange | Parameters | •| none.   
---|---  
  
This event fires when a device changes. This can be because a new device is added, or a device is removed.  
  
OnDeviceArrival | Parameters | •| Device : LONG that specifies the index of the device that arrived. The index starts at 0.  
---|---  
  
This event fires when a device is inserted. When a device is added or removed, the index that was used previously, does not need to match the new index anymore. For this reason you have to checkout the device again.  
  
OnDeviceRemoval | Parameters | •| Device : LONG that specifies the index of the device that has been removed. The index starts at 0.  
---|---  
  
This event fires when a device is removed. When a device is added or removed, the index that was used previously, does not need to match the new index anymore. For this reason you have to checkout the device again.  
  
OnDataRead | Parameters | •| Device : LONG that specifies the index of the device that sent data. The index starts at 0.  
---|---  
  
•| ReportID : LONG with the report ID of the device that sent the data.  
---|---  
  
•| Data : string that contains the data. This string might contain 0-bytes.   
---|---  
  
•| Size : LONG that contains the length of the received data.   
---|---  
  
When data is received you can read it in this event. For example :

```vb
dim ar(8) as Byte

For J=1 to Size

```
ar(j) = ASC(Mid(data,J,1)) ' fill the array

Next  
  
|   
  
  
The OCX can be used with all programming languages that can host OCX controls. The OCX was tested with Delphi and VB.

Your windows must support USB in order to use the OCX. So it will not work on Windows 95.

Virtual COM sample

The virtual COM demo shows how to implement an USB device with a virtual COM port. The Demo will echo data sent to the UART to the USB and vise versa.

When you compile and program the sample, you will notice that you find a new COM port in the device manager.

![notice](notice.jpg)When you press CTRL+D, BASCOM will launch the device manager.

![dev_mng](dev_mng.png)

As you can see, the CDC class is used for the virtual COM port. As with most virtual COM devices, you can change the settings :

![virtual COM](virtual com.png)

In the BASCOM application the procedure Cdc_get_line_coding is called when the PC need to know the settings.

The Cdc_set_line_coding is called when the settings are changed by the user. You need to change the settings according to the received parameters.

Notice that these settings are virtual too : for the USB it does not matter how the baud rate is set ! Only for a real UART this is important. For an USB-RS232 converter for example it is very convenient to be able to change the baud rate and other settings. But when you just use the USB port for communication, and choose to use the COM port in your program as a way for communication, then you do not really need the settings. 

When you want to send date to the USB/COM you can use the Uart_usb_putchar procedure. Like any USB routine, it will select the proper end point. After the end point for sending data is selected it will wait if it may send data, and finally it will send this data. 

The Uart_usb_getchar() function can be used to receive data from the USB/COM. 

When you create your own device, the virtual COM port has the advantage that the PC application is simple. In most cases you already have the experience to read/write data to the PC COM port.

The disadvantage is that it requires mode code. It also need an INF file. This INF file you can change to suite your own needs.

When you create your own device, the HID device is the simplest way to go.

CDC INF file 

The CDC INF file looks like this. The bold parts need to be changed if you want to customize with your own text and VID/PID.

; Windows 2000, XP & Vista setup File for AT90USBxx2 demo

[Version] 

Signature="$Windows NT$" 

Class=Ports 

ClassGuid={4D36E978-E325-11CE-BFC1-08002BE10318} 

Provider=%ATMEL% 

LayoutFile=layout.inf 

DriverVer=10/15/1999,5.0.2153.1 

[Manufacturer] 

%ATMEL%=ATMEL 

[ATMEL] 

%ATMEL_CDC%=Reader, USB\VID_03EB&PID_2018 

[Reader_Install.NTx86] 

;Windows2000 

[DestinationDirs] 

DefaultDestDir=12 

Reader.NT.Copy=12 

[Reader.NT]

include=mdmcpq.inf

CopyFiles=Reader.NT.Copy 

AddReg=Reader.NT.AddReg 

[Reader.NT.Copy] 

usbser.sys 

[Reader.NT.AddReg] 

HKR,,DevLoader,,*ntkern 

HKR,,NTMPDriver,,usbser.sys 

HKR,,EnumPropPages32,,"MsPorts.dll,SerialPortPropPageProvider" 

[Reader.NT.Services] 

AddService = usbser, 0x00000002, Service_Inst 

[Service_Inst] 

DisplayName = %Serial.SvcDesc% 

ServiceType = 1 ; SERVICE_KERNEL_DRIVER 

StartType = 3 ; SERVICE_DEMAND_START 

ErrorControl = 1 ; SERVICE_ERROR_NORMAL 

ServiceBinary = %12%\usbser.sys 

LoadOrderGroup = Base 

[Strings] 

ATMEL = "ATMEL, Inc." 

ATMEL_CDC = "AT90USBxxx CDC USB to UART MGM" 

Serial.SvcDesc = "USB Serial emulation driver" 

;---- END OF INF FILE

You can also change the key names.

---

## USB-ISP Programmer

The USB-ISP Programmer is a special USB programmer that is fully compatible with BASCOM's advanced programmer options.

Since many new PC's and especial Laptop's do not have a parallel programmer anymore, MCS selected the USB-ISP programmer from EMBUD.

The drivers can be downloaded from the MCS Electronics website.

Please download from [http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=204&Itemid=54](<http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=204&Itemid=54>)

After downloading, unzip the files in the BASCOM-AVR application directory in a sub directory named USB.

![usb-1](usb-1.jpg)

When you connect the programmer, Windows (98, ME, 2000, XP) will recognize the new device automatically.

![usb-2](usb-2.jpg)

Then the Hardware wizard will be started :

![u2b-2](u2b-2.jpg)

Select 'No, not this time' and click Next, as there is no driver at Microsoft's web.

The Wiz will show :

![usb-3](usb-3.jpg)

You need to select 'Install from a list or specific location' and click Next.

![usb-4](usb-4.jpg)

You can specify the path of the USB driver. This is by default :

C:\Program Files\MCS Electronics\BASCOM-AVR\USB

Use the Browse-button to select it, or a different location, depending on your installation.

As the driver is not certified by Micros ft, you will see the following window:

![usb-5](usb-5.jpg)

You need to select 'Continue Anyway'. A restore point will be made if your OS supports this and the driver will be installed.

After installation you must see the following window :

![usb-6](usb-6.jpg)

After you press Finish you will see Windows can use the programmer :

![usb-7](usb-7.jpg)

In BASCOM , Options, Programmer you can select the new programmer now.

![usb_prog](usb_prog.png)

New models of the USB programmer allow to set the speed. 

The USB-ISP programmer is very quick and supports all options that the Sample Electronics and STK200 programmers support. It is good replacement for the STK200.

When you use other USB devices that use the FTDI drivers, there might occur a problem. Manual install the drivers of these other devices, then install the USB-ISP driver.

USB-ISP on VISTA

For Vista and Vista 64, please follow the this installation description. 

![usb_isp_vista1](usb_isp_vista1.png)

When connection the ISP-PROG I to your PC the following window will show up. Here I have to select the top selection: Locate and Install driver software (recommended)   
Vista starts it search for the driver and will come finally with the question to Insert the driver disk.

![usb_isp_vista2](usb_isp_vista2.png)

As we have no driver CD, you have to select: I donât have the disc. Show me other options  


![usb_isp_vista3](usb_isp_vista3.png)

Now we select the Browse selection and locate the driver folder.

![usb_isp_vista4](usb_isp_vista4.png)

And select Next button. 

As Vista 64 only allows certified drivers the following message will pop-up. 

![usb_isp_vista5](usb_isp_vista5.png)

Just select Install this driver software anyway and Vista 64 will now start with installing the driver. Be patient as it depends on your system configuration how long it will take.

![usb_isp_vista7](usb_isp_vista7.png)

Finally Vista 64 will tell you that the driver is installed. To check your configuration you can go to your device manager to see if it is there.

![usb_isp_vista8](usb_isp_vista8.png)

---

## USBASP

The USBASP is a popular USB programmer created by Thomas Fischl

The programmer uses a Mega8 or other AVR chip as an USB device.

You can find the programmer at Thomas website :  <http://www.fischl.de/usbasp>

Make sure when programming the fuse and lock bits that the selected clock frequency is not too high. The clock frequency of the ISP programmer should be less then one quarter of the oscillator frequency. When your micro is running at 8 MHz, you can select up to 2 MHz. On the safe size, 125 KHz is always ok.

By default most AVR processors run at 8 MHz with an 8-divider resulting in 1 MHz clock frequency. So 250 KHz is a safe value for most processors.

![usbasp](usbasp.png)

You can select various clock frequencies. 

See also [LIBUSB](libusb.md) for installation of LIBUSB

---
