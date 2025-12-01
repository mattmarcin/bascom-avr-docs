# Tips and tricks

Tips & Tricks:

1\. You can specify a binary number with the &B and you can use underscore "_" like:

Dim Var As Byte  
  
Var = &B00_110000  
Var = &B0000_1111  
Var = &B00_11_00_11

2\. How to use longer formulas:

```vb
Dim A As Byte  
Dim B As Byte  
Dim C As Byte  
  
' Now you want to use following formula: a = B / 4 + C  
' In Bascom you write  
  
```
A = B / 4  
A = A + C

3\. You can use more than one Bascom statement in one line with colons ":"

```vb
Dim A As Byte  
Dim B As Byte  
Dim C As Byte  
  
' Now you want to use following formula: a = B / 4 + C  
' In Bascom you write  
  
```
A = B / 4 : A = A + C

4\. You can use overlay to have easy access to the low byte and high byte of a WORD

(the same approach also work for e.g. LONG)

```vb
Dim My_word As Word  
Dim Low_byte As Byte At My_word Overlay  
Dim High_byte As Byte At My_word + 1 Overlay  
  
```
Low_byte = &B0000_1111  
High_byte = &B1111_0000  
  
```vb
' This is how it will be stored in SRAM  
' <\-------my_word-------->  
' +-----------+----------+  
' | Low_byte |High_byte |  
' +-----------+----------+

```
5\. To split a word into High byte and Low byte you can also use [HIGH](high.md) and [LOW](low.md)

6\. Here is a way to print the content of a variable or AVR register:

Use Print Bin(X)

Example:

```vb
$regfile = "m88def.dat" ' we use the M88  
$crystal = 8000000  
$baud = 19200  
$hwstack = 32  
$swstack = 8  
$framesize = 24  
  
  
Dim A As Byte  
  
```
A = &B00000001  
A = A * 2  
```vb
Print Bin(a)   
  
End ' end program

```
7\. If you do not want that Bascom-AVR is sending Carriage + Return after a print command use semi-colon ";" after the print funtion:

Example:

```vb
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
Print "Hello World" ;  
  
End

```
8\. For the user who want to use external editors:

The bascomp.exe has been updated. It can be downloaded from the download section.

It now supports a simpler way to be called.

The utility has been updated and now will retrieve all info from the source file, but only when your main program contains these directive :

$regfile, $hwstack, $swstack, $framesize

Example :

bascomp.exe "c:\my folder\source\sample.bas" auto

The 'auto' is a switch so the utility will retrieve the settings from your code.

9\. You can use $initmicro if you want to run special tasks at startup:

See [$INITMICRO](_initmicro.md)

10\. You can use $include to make larger projects better readable: See [$INCLUDE](include.md)

11\. Your LCD is not working and you need a list of steps what do check:

a. Check fuse bit settings

b. Are the AVR pins are OK ?

To test the AVR pins you can do following:

Write a program that toggles all the lcd pins and then measure the logic level.

```vb
Then check with a DVM or led-series resistor if all pins change level. if they do, there is a problem with the lcd

If the pin do not toggle:

```
\- pin defect

\- track or solder problem. 

Here the test program:

```vb
$regfile = "m328pdef.dat" ' Specify The Used Micro  
$crystal = 16000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for thehardware stack  
$swstack = 10 ' default use 10 for theSW stack  
$framesize = 40 ' default use 40 for theframe space  
  
Config Clockdiv = 1 ' divide xtal clock by 1, default fuse bit is set ' to 8 by elektor  
  
Config Portc.3 = Output ' RW  
Config Portd.4 = Output ' Db4  
Config Portd.5 = Output ' Db5  
Config Portd.6 = Output ' Db6  
Config Portd.6 = Output ' Db7  
Config Portc.1 = Output ' E  
Config Portc.2 = Output ' RS  
  
do  
toggle portc  
toggle portd  
waitms 1000  
Loop  
  
End ' end program

```
12\. With the Lib Manager you can compile a Library (*.lib) into an *.lbx file.

See here: [Tools LIB Manager](tools_lib_manager.md)

13\. There is a timeout function for hardware and software UART

See [$TIMEOUT](_timeout.md)

14\. How to use the Powerdown function:

See also: [CONFIG POWERMODE](config_powermode.md)

If you can not measure the same power down current as written in the data sheet you also need to use a

Low Quiescent Current LDO Regulator to meet that specs (if you measure the current including the Current LDO Regulator).

Examples for 3.3Volt Low Quiescent Current LDO Regulator :

•| MCP1702 --> typical 2µA  
---|---  
  
•| MCP1700 --> typical 1.6µA  
---|---  
  
•| AS1375 low power LDO --> 1µA (typ.) of quiescent current  
---|---  
  
•| TPS78233 3,3V --> 0.4µA  
---|---  
  
  
```vb
' Using the new config powermode = PowerDown function with ATTINY13  
  
' Used Bascom-AVR Version 2.0.7.3  
  
' Fuse Bits:  
' Disable DWEN (Debug Wire) Fuse Bit  
' Disable Brown-Out Detection in Fuse Bits  
' Disable Watchdog in Fuse Bits  
  
' You can also just use Config Powermode = Powerdown  
  
' But this example here also considers what the data sheet write under "MINIMIZING POWER CONSUMPTION"  
' You need to follow this when you want to achieve the current consumption which you find in the

' data sheet under Powerdown Mode.  
  
' 1. Disable/Switch off ADC  
' 2. Disable/Switch off Analog Comparator  
' 3. Disable Brown-out Detection when not needed  
' 4. Disable internal voltage reference  
' 5. Disable Watchdog Timer when not needed  
' 6. Disable the digital input buffer  
' 7. Enable Pull-up or pull-down an all unused pins  
  
$regfile = "attiny13.dat"  
$crystal = 9600000 ' 9.6MHz  
$hwstack = 10  
$swstack = 0  
$framesize = 24  
  
On Int0 Int0_isr ' INT0 will be the wake-up source for Powerdown Mode  
Config Int0 = Low Level  
Enable Int0  
  
' Prepare Powerdown:  
' To minimize power consumption, enable pull-up or -down on all unused pins, and  
' disable the digital input buffer on pins that are connected to analog sources  
Config Portb.0 = Input  
Set Portb.0  
Config Portb.1 = Input ' INT0 --> external 47K pull-up  
'Set Portb.1  
Config Portb.2 = Input  
Set Portb.2  
Config Portb.3 = Input  
Set Portb.3  
Config Portb.4 = Input  
Set Portb.4  
Config Portb.5 = Input ' External Pull-Up (Reset)  
  
```
Didr0 = Bits(ain1d , Ain0d) ' Disable digital input buffer on the AIN1/0 pin  
  
```vb
Set Acsr.acd ' Switch off the power to the Analog Comparator  
' alternative:  
' Stop Ac  
  
Reset Acsr.acbg ' Disable Analog Comparator Bandgap Select  
  
Reset Adcsra.aden ' Switch off ADC  
' alternative:  
' Stop Adc  
  
'###############################################################################  
Do  
Wait 3 ' now we have 3 second to measure the Supply Current

' in Active Mode  
Enable Interrupts  
' Now call Powerdown function  
Config Powermode = Powerdown

' Here you have time to measure PowerDown current consumption until a Low Level 

' on Portb.1 which is the PowerDown wake-up  
Loop  
'###############################################################################  
End  
  
```
Int0_isr:  
```vb
' wake_up  
Return

```