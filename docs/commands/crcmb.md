# CRCMB

Action

Returns the Modbus CRC value of a variable or array.

Syntax

Var = CRCMB( source , L)

Remarks

Var | The variable that is assigned with the modbus checksum of variable source. This should be a word variable.  
---|---  
Source | The source variable or first element of the array to get the checksum of.  
L | The number of bytes to check.  
  
CRC8 is used in communication protocols to check if there are no transmission errors.

The Modbus checksum uses a different polynome.

Modbus.lbx or modbus.lib need to be included in your project using the $LIB directive

See also

[CHECKSUM](checksum.md) , [CRC16](crc16.md), [CRC16UNI](crc16uni.md) , [CRC32](crc32.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRC8](crc8.md) , [CRC8UNI](crc8uni.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim Ar(10) As Byte

Dim W As Word

```
Ar(1) = 1

Ar(2) = 2

Ar(3) = 3

W = CrcMB(ar(1) , 3) 'calculate value

```vb
Print W

End

```