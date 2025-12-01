# USB-ISP Programmer

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