# CONFIG PRINTBIN

Action

Configure PRINTBIN behavior

Syntax

CONFIG PRINTBIN = mode

Remarks

mode | The mode value is either EXTENDED or NORMAL. EXTENDED The extended mode is the only mode you can configure. It allows to send packets greater than 255 bytes.  For example when you need to send an array with more than 255 elements. The maximum packet size is 64 KB. Because support for big packets requires more code, it is made optional. You can not change between normal and extended mode dynamically. If you chose to use extended mode, this will be used for all your PRINTBIN code. The internal constant named _PBIN_EXTENDED will be set to 1. When you do not configure PRINTBIN, it will have the default value of 0. NORMAL The normal mode is the default. When you do not use CONFIG PRINTBIN, the default NORMAL mode is selected.  You can not switch dynamic between the 2 modes.  
---|---  
  
See also

[CONFIG PRINT](configprint.md) , [PRINTBIN](printbin.md)

Example

```vb
$regfile = "m103def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Printbin = Extended

Dim A(1000)

```
Printbin A(1) ; 1000