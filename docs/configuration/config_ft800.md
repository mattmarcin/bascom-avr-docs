# CONFIG FT800

Action

This compiler option is required to setup the FT8xx SPI interface.

Syntax

CONFIG FT8xx = spi [, FTSAVE=ftsave , FTDEBUG=ftdebug] , FTCS=ftcs [, FTPD = ftpd] [,FTCHIP=800|801] [,PLATFORM=platform] [,LCD_SCREEN-lcdscr] [,LCD_ROTATE=lcdrotate] [,LCD_CALIBRATION=calib]

Remarks

spi | The SPI interface used for the FT800/FT801/FT810 processor. This may be : \- SPI, for normal AVR processors \- SPI*, SPIC, SPID, SPIE, SPIF, for XMEGA processors. * When you use SPI on an XMEGA processor, the compiler will use SPIC, the default SPI.  
---|---  
ftsave | This is an optional parameter with a default of 0. The possible values are 0 and 1. With this option enabled, the parameters passed to the various FT800 routines are limited in range. For example when a parameter is expected in the range from 0-31 it would not matter if you pass 32. But limiting the range increases code. It is best to make sure yourself that you pass the proper values.   
ftdebug | This is an optional parameter with a default of 0. The possible values are 0 and 1. With this option enabled, the SPI communication can be monitored. A label named _FTDBG is called in your code. So when using this option you need to insert this label into your code. You also need to DIM a byte named ftdebug. This byte will be filled with the parameter sent to the SPI.  Make sure you put a RETURN after the label and save registers you use: _FTDBG Pushall print hex(ftdebug) Popall RETURN  
FTCS | The name of the SPI port pin connected to the CS pin of the FT800. This would be SS in most cases. This pin is set to output and to logic level 1.  
FTPD | The name of the port pin connected to the PD pin of the FT800. This is an optional pin, it depends on your hardware. Gameduino2 does not require it. EVE demo boards do require this pin.  
FTCHIP | The kind of FT chip. FT800 is the default and when used, FTCHIP does not need to be specified. FT801 is similar to the FT800 but has a capacitive touch screen and gestures support. Possible values :  \- 800 : FT800 (default) \- 801 : FT801 \- 810, 811,812, 813 : FT81x  
PLATFORM | The used hardware platform. Default is EVE from FTDI. Possible values : \- EVE (default) \- GAMEDUINO2 : popular alternative FTDI hardware  
LCD_SCREEN | The kind of LCD screen. Possible values :  480272 : 480x272 pixels LCD (default) 320240 : 320x240 pixels LCD 800480 : 800x480 pixels LCD 800600 : 800x600 pixels LCD As you might have noticed, the value is the same as the screen size without the x.   
LCD_ROTATE | The LCD can be used in normal horizontal mode or upside down 180 degrees.  Possible values : \- 0 : horizontal (default) \- 1 : 180 degrees rotated  
LCD_CALIBRATION | The LCD requires calibration. This need to be done once but you can force calibration using LCD_CALIBRATION parameter. Possible values : \- 0 : No calibration \- 1 : Force Calibration (default)  
  
The CONFIG FT800 statement will inform the compiler to use the FT800.LIB. It will also create an ALIAS for the CS and PD pins you specify.

The FT800 is controlled by the SPI interface. This means that you need to configure the SPI the usual way.

![notice](notice.jpg)Since FT800 was the first graphic processor, you will find FT800 mentioned in the help. But as of version 2080, there is also support for the new FT810 chip.

BASCOM FT8xx support is implemented in the following way:

\- a low level communication library FT800.LIB

\- ASM include macros which are located in the FT800.LIB. Unlike sub routines, the code is included and not called. 

\- BASCOM high level commands such as CMD32, RD8(), RD16(), etc.

\- FT80x include files : an include file with the declarations (FT81x.INC) and an include file with the actual code (FT81x_FUNCTIONS.INC).

You may modify the code from the include files. The code will reveal some new options. It is important to understand these new options.

\- Passing values using [BYREG](declare_sub.md)

\- Passing values using [BYSTACK](declare_sub.md)

\- [CMDFTSTACK](cmdftstack.md)

In version 2079, FT801 support is included. A number of constants are removed from the include file and are now a parameter of CONFIG FT800. These constants are : FT_PlatForm , FT_LCDscreen , FT_LcdCal , FT_RotateDisplay and FT_CHIP. These constants are remarked for reference.

Here are some sample configurations

AdamShield:

Config FT800 = Spi , Ftsave = 0 , Ftdebug = 0 , Ftcs = Portd.4 , Ftpd = Portd.3, ftChip=800, LcdScreen=480272, PlatForm=Eve 

GAMEDUINO2:

Config FT800=spi , ftsave=0, ftdebug=0 , ftcs=portb.0, ftChip=800, LcdScreen=480272, PlatForm=Gameduino2

VM801P - FTDI:

Config FT800 = Spi , ftsave = 0, ftdebug = 0 , Ftcs = Portb.1 , Ftpd = Portd.4, ftChip=801, LcdScreen=480272, PlatForm=Eve, Lcd_Rotate=1, Lcd_Calibration=0

See also

[FT800](ft800.md) , [CMDFTSTACK](cmdftstack.md) , [CMD32](cmd32.md) , [RD8](rd8.md), [RD16](rd16.md), [RD32](rd32.md) , [WR32](wr32.md)

Partial Example

```vb
' FT800 Gauges Application demonstrating interactive Gauges using Lines & Custom Font  
' FT800 platform.  
' Original code from http://www.ftdichip.com/Support/SoftwareExamples/EVE/FT_App_Gauges.zip  
' Requires Bascom 2.0.7.8 or greater  
  
$Regfile = "M328pdef.dat"  
$Crystal = 8000000  
$Baud = 19200  
$HwStack = 90  
$SwStack = 90  
$FrameSize = 300  
$NOTYPECHECK  
  
Config ft800=spi , ftsave=0, ftdebug=0 , ftcs=portb.2, ftpd=portb.1  
  
Config Base = 0  
Config Submode = New  
Config Spi = Hard , Interrupt = Off , Data_Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4, Noss = 1  
```
SPSR = 1 ' Makes SPI run at 8Mhz instead of 4Mhz  
  
  
```vb
' Swaps Scales  
' 1 = Resitive - Random  
' 0 = Random - Resistive  
```
Const Resistive = 0  
  

#If Resistive = 0  
Const First = 1  
Const Second = 0  

#Else  
Const First = 0  
Const Second = 1  

```vb
#EndIf  
  
$Include "FT80x.inc"  
$Include "FT80x_Functions.inc"  
  
Declare Sub cs(Byval i As Byte)  
Declare Function da (Byval i As Long) As Word  
Declare Sub Polar(byval R As Long , Byval Th As Word)  
Declare Sub Polarxy(byval R As Long , Byval Th As Word , Byref X As Long , Byref Y As Long)  
Declare Sub IntroFTDI  
Declare Sub Gauges  
Declare Function Read_Keys() As Byte  
  
' General Program Variables and Declarations  
Dim temp_tag As Byte  
Dim ox As Long  
  
  
```
Spiinit  
  
if FT800_Init()=1 then end ' Initialise the FT800

  
Gauges  
  
```vb
Do

  
Loop  
  
```
Remark

In the samples,  Noss = 1 is used for CONFIG SPI. This means that the SS pin must be set by the user. In case of CONFIG FT800, the compiler always set the specified pin for FTCS to output and to logic 1. When possible you should use NOSS=0 and use the dedicated SPI SS pin. But for multiple SPI devices on the bus that is not possible since you will have multiple CS pins, and in these cases you should use NOSS=1, so you can control the SS logic level.