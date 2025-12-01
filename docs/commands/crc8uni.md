# CRC8UNI

Action

Returns the CRC value of a variable or array.

Syntax

Var = CRC8UNI( source , L)

Remarks

Var | The variable that is assigned with the CRC8 of variable source.  
---|---  
Source | The source variable or first element of the array to get the CRC8 of.  
L | The number of bytes to check.  
  
CRC is used in communication protocols to check if there are no transmission errors.

The [CRC8](crc8.md) function in BASCOM is mainly intended to be used with 1WIRE.

The CRC8UNI uses the CCITT with polynome value 7.

![notice](notice.jpg)When you want to use a different polynome, you can override the default by defining a constant named CRC8_POLY

Const CRC8_POLY = &HAA 'use a different value

See also

[CHECKSUM](checksum.md) , [CRC16](crc16.md), [CRC16UNI](crc16uni.md) , [CRC32](crc32.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRCMB](crcmb.md) , [CRC8](crc8.md)

Example

```vb
'------------------------------------------------------------------------------  
'name : crc8-16-32.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates CRC  
'micro : Mega48  
'suited for demo : yes  
'commercial addon needed : no  
'------------------------------------------------------------------------------  
  
$regfile = "m48def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
  
Dim Ar(10) As Byte  
Dim J As Byte  
Dim W As Word  
Dim L As Long  
Dim S As String * 16  
  
  
```
S = "123456789"  
  
Ar(1) = 1  
Ar(2) = 2  
Ar(3) = 3  
  
  
J = Crc8(ar(1) , 3) 'calculate value which is 216  
j = Crc8Uni(ar(1) , 3) 'calculate unsing CCITT which is 72  
W = Crc16(ar(1) , 3) '24881  
L = Crc32(ar(1) , 3) '1438416925  
  
```vb
' data , length, intial value , Poly, reflect input, reflect output  
  
Print Hex(Crc16Uni(S , 9 , 0 , &H1021 , 0 , 0)) 'CRC-CCITT (0x0000) 31C3  
Print Hex(Crc16Uni(S , 9 , &HFFFF , &H1021 , 0 , 0)) 'CRC-CCITT (0xFFFF) 29B1  
Print Hex(Crc16Uni(S , 9 , &H1D0F , &H1021 , 0 , 0)) 'CRC-CCITT (0x1D0F) E5CC  
Print Hex(Crc16Uni(S , 9 , 0 , &H8005 , 1 , 1)) 'crc16 BB3D  
Print Hex(Crc16Uni(S , 9 , &HFFFF , &H8005 , 1 , 1)) 'crc16-modbus 4B37  
  
End

```