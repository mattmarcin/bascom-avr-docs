# CONFIG INPUTBIN

Action

Configure INPUTBIN behavior

Syntax

CONFIG INPUTBIN = extended

Remarks

extended | This mode is the only mode. It allows to receive packets greater than 255 bytes. The maximum packet size is 64 KB. Because support for big packets requires more code, it is made optional.  You can not change between normal and extended mode dynamically. If you chose to use extended mode, this will be used for all your PRINTBIN code.  
---|---  
  
See also

[CONFIG PRINT](configprint.md) , [PRINTBIN](printbin.md) , [INPUTBIN](inputbin.md) , [CONFIG PRINTBIN](config_printbin.md)

Example

```vb
$regfile = "m103def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Inputbin = Extended

Dim A(1000)

```
Inputbin A(1) ; 1000