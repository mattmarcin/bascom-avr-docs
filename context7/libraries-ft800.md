# FT800 Libraries

> FT800/FT810 GPU display controller

## FT800

![clip0002](clip0002.png)

The FT800 is no toy, this is a proper GPU (Graphics Processor Unit) which has some outstanding abilities.

The Bascom FT800 Library is set up and written to give the user the Framework needed to use this IC.

Please also check some of the video demos to appreciate what you can accomplish! [YouTube demos](<https://www.youtube.com/watch?v=3trUUc-tFKY&feature=youtu.be>)

Some methods and habits need to change when using the FT800 in respect to a standard graphics LCD.

Here are some points and features (additional points added from the Manufacturers advertisement).

•| You now have to update/refresh Screen on every graphics changes (think of it as the old Cartoon drawings flicking through paper).  
---|---  
  
•| You don't need to keep on update/refresh Screen if you want a static image, you can do something else in the meantime.  
---|---  
  
•| For the Experienced, look also at the FT800 Interrupts Int_CmdFlag, looks likes some benefits can be made.  
---|---  
  
•| You can update/refresh the FT800 up to 60Hz, many types of animations can be implemented.  
---|---  
  
•| Don't need many I/O pins, SPI or I2C is all you need (SPI is recommended).  
---|---  
  
•| If you are in the graphics loop careful when you want to access Serial data or other hardware reads, the loop can only cycle at 60Hz so this can slow you down miss data if you are not aware (use other methods).  
---|---  
  
•| Careful using other SPI devices on the same SPI bus, see [How to add another SPI device with the FT800](how_to_another_spi_device_with.md)  
---|---  
  
•| To create more extensive fancy Graphics, previous experience with other Graphics engines is very helpful, requires some knowledge.  
---|---  
  
•| Unfortunately the FT800 version is only for small LCD screen (largest found is 5" 480x272 - as of 10/2014)  
---|---  
  
•| No custom hardware required, see [Getting Started](getting_started.md) for some links of ready made boards/bezels to get your project started.  
---|---  
  
•| No real Reset but Hybrid Software type.  
---|---  
  
•| If using any Arduino model boards - use a descent (thick) USB cable if you are trying to program and power using the same cable.  
---|---  
  
Some USB cables are not good quality, when trying to power the LCD and the Arduino board, you can get a voltage drop getting unexpected results not knowing what is wrong at the time. It is highly recommended you use and external power supply especially if you are a beginner!.

•| It's got sound synthesizer and audio playback (mono).  
---|---  
  
Many of the Documentation and Specifications can be downloaded directly from FTDI's website : [FTDI/FT800](http://www.ftdichip.com/Products/ICs/FT800.md)

Please note:

The Help File for the Bascom FT800 is very much taken from FTDI's FT800 Series Programmer Guide.PDF with some changes.

Currently the Help file is a Work in Progress which means it may contain some error(s) and may not be complete, so if in doubt try to consult with the FT800 Series Programmer Guide.PDF from FTDI if/when having any difficulties. Some of the FTDI explanations are not clear and require better more work, though some sperate Document have been released giving more detail. 

And last if you find any errors or have suggestions/improvements or even any feedback, please send an email to [support@mcselec.com.](<mailto:support@mcselec.com.>)

FT801

In version 2079, support for FT801 is included. The INC files have been renamed to reflect this. 800 is renamed into 80x. This means that in order to use the updates and/or new features, you need to change the names of the used include files in your project. 

FT810

In version 2080, support for FT810 is included. The INC files have been renamed to reflect this. 800 is renamed into 81x. This means that in order to use the updates and/or new features, you need to change the names of the used include files in your project. 

Note from MCS

The text above and all FT800 help topics and sample files are written by Peter Maroudas. Peter made the BASCOM implementation possible.

MCS has written the low level ASM FT800 library and the required compiler changes and modifications of the include files based on Peters work.

For version 2079, Peter included FT801 support.

See [CONFIG FT800](config_ft800.md) for configuration of the library.

---
