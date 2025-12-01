# CRC8

Action

Returns the CRC8 value of a variable or array.

Syntax

Var = CRC8( source , L)

Remarks

Var | The variable that is assigned with the CRC8 of variable source.  
---|---  
Source | The source variable or first element of the array to get the CRC8 of.  
L | The number of bytes to check.  
  
CRC8 is used in communication protocols to check if there are no transmission errors.

The 1wire for example returns a CRC byte as the last byte from itâs ID.

The code below shows a VB function of CRC8

```vb
Function Docrc8(s As String) As Byte

Dim j As Byte

Dim k As Byte

Dim crc8 As Byte

```
crc8 = 0

For m = 1 To Len(s)

x = Asc(Mid(s, m, 1))

For k = 0 To 7

j = 1 And (x Xor crc8)

crc8 = Fix(crc8 / 2) And &HFF

x = Fix(x / 2) And &HFF

If j <> 0 Then

crc8 = crc8 Xor &H8C

```vb
End If

Next k

Next

```
Docrc8 = crc8

End Function

![notice](notice.jpg)When you want to use a different polynome, you can override the default by defining a constant named CRC8_POLY

Const CRC8_POLY = &HAA 'use a different value

![notice](notice.jpg)Please notice that the CRC8 function is the CRC8-MAXIM function. It is primarily intended for the 1WIRE routines. There exist a lot of different CRC8 variants. They differ in the start value, the polynom , if the result is XOR-ed and if the data is reflected or not. Reflection means that data is flipped. (See [FLIP](flip2.md))

CRC8 supports big strings in 2083.

See also

[CHECKSUM](checksum.md) , [CRC16](crc16.md), [CRC16UNI](crc16uni.md) , [CRC32](crc32.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRCMB](crcmb.md)

ASM

The following routine is called from mcs.lib : _CRC8

The routine must be called with Z pointing to the data and R24 must contain the number of bytes to check.

On return, R16 contains the CRC8 value.

The used registers are : R16-R19, R25.

;##### X = Crc8(ar(1) , 7)

Ldi R24,$07 ; number of bytes

Ldi R30,$64 ; address of ar(1) 

Ldi R31,$00 ; load constant in register

Rcall _Crc8 ; call routine

Ldi R26,$60 ; address of X

St X,R16 ; store crc8

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

```
Ar(1) = 1

Ar(2) = 2

Ar(3) = 3

J = Crc8(ar(1) , 3) 'calculate value which is 216

```vb
Print J

End

```