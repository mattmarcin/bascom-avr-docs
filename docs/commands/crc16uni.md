# CRC16UNI

Action

Returns the CRC16 value of a variable or array.

Syntax

Var = CRC16UNI( source ,length , initial, polynomial,refin,refout)

Remarks

var | The variable that is assigned with the CRC16 of variable source. Should be a word or integer variable.  
---|---  
source | The source variable or first element of the array to get the CRC16 value from.  
length | The number of bytes to check. The maximum value is 65535. (&HFFFF)  
initial | The initial value of the CRC. This is usual 0 or &HFFFF.  
polynomial | The polynomial value to use.   
refin | Reflect the data input bits. Use 0 to disable this option. Use a non-zero value to enable this option.  
refout | Reflect the data output. Use 0 to disable this option. Use a non-zero value to enable this option.  
  
CRC16 is used in communication protocols to check if there are no transmission errors.

The 1wire for example returns a CRC byte as the last byte from itâs ID.

Use CRC8 for the 1wire routines.

There are a lot of different CRC16 routines. There is no real standard since the polynomial will vary from manufacture to manufacture. 

At <http://www.ross.net/crc/download/crc_v3.txt> you can find a great document about CRC calculation from Ross N. Williams. At the end you will find an example that is good for dealing with most CRC variations. The BASCOM CRC16UNI function is a conversion of this example. 

There is a difference however : The CRC16UNI function does not XOR the output bytes. This because most CRC functions XOR with 0. 

The example will show some of the most used combinations.

In version 2083 the function can handle more than 255 bytes. In previous versions the amount was limited to a maximum of 255.

See also

[CHECKSUM](checksum.md) , [CRC8](crc8.md), [CRC16](crc16.md) , [CRC32](crc32.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRCMB](crcmb.md) , [CRC8UNI](crc8uni.md)

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

W = Crc16(ar(1) , 3) '24881

L = Crc32(ar(1) , 3) '494976085

```vb
' data , length, intial value , Poly, reflect input, reflect output

Print Hex(crc16uni(s , 9 , 0 , &H1021 , 0 , 0)) 'CRC-CCITT (0x0000) 31C3

Print Hex(crc16uni(s , 9 , &HFFFF , &H1021 , 0 , 0)) 'CRC-CCITT (0xFFFF) 29B1

Print Hex(crc16uni(s , 9 , &H1D0F , &H1021 , 0 , 0)) 'CRC-CCITT (0x1D0F) E5CC

Print Hex(crc16uni(s , 9 , 0 , &H8005 , 1 , 1)) 'crc16 BB3D

Print Hex(crc16uni(s , 9 , &HFFFF , &H8005 , 1 , 1)) 'crc16-modbus 4B37

End

```