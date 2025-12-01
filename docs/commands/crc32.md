# CRC32

Action

Returns the CRC32 value of a variable.

Syntax

Var = CRC32( source , L)

Remarks

Var | The LONG variable that is assigned with the CRC32 of variable source.  
---|---  
Source | The source variable or first element of the array to get the CRC 32 value from.  
L | The number of bytes to check. This can be a word variable.   
  
CRC32 is used in communication protocols to check if there are no transmission errors.

See also

[CHECKSUM](checksum.md) , [CRC8](crc8.md), [CRC16](crc16.md) , [CRC16UNI](crc16uni.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRCMB](crcmb.md) , [CRC8UNI](crc8uni.md)

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

Dim J As Byte

Dim W As Word

Dim L As Long

```
Ar(1) = 1

Ar(2) = 2

Ar(3) = 3

J = Crc8(ar(1) , 3) 'calculate value which is 216

W = Crc16(ar(1) , 3) '24881

L = Crc32(ar(1) , 3) '1438416925

End