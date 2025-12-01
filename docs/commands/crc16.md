# CRC16

Action

Returns the CRC16 value of a variable or array.

Syntax

Var = CRC16( source , L)

Remarks

Var | The variable that is assigned with the CRC16 of variable source. Should be a word or integer variable.  
---|---  
Source | The source variable or first element of the array to get the CRC16 value from. By default only normal RAM variables are supported. You can also use EEPROM memory when you add a constant to your project :   
Const CRC16_EEPROM=1   
L | The number of bytes to check. This can be a numeric constant , byte or word variable. The maximum size to check is 65535.  
  
CRC16 is used in communication protocols to check if there are no transmission errors.

The 1wire for example returns a CRC byte as the last byte from itâs ID.

Use CRC8 for the 1wire routines.

There are a lot of different CRC16 routines. There is no real standard since the polynomial will vary from manufacture to manufacture.

The equivalent code in VB is shown below. There are multiple ways to implement it in VB. This is one of them.

VB CRC16 Sample

Private Sub Command1_Click()

```vb
Dim ar(10) As Byte

Dim b As Byte

Dim J As Integer

```
ar(1) = 1

ar(2) = 2

ar(3) = 3

b = Docrc8(ar(), 3) ' call funciton

```vb
Print b

'calculate value which is 216

```
J = CRC16(ar(), 3) ' call function

```vb
Print J

End Sub

Function Docrc8(ar() As Byte, bts As Byte) As Byte

Dim J As Byte

Dim k As Byte

Dim crc8 As Byte

```
crc8 = 0

For m = 1 To bts

x = ar(m)

For k = 0 To 7

J = 1 And (x Xor crc8)

crc8 = Fix(crc8 / 2) And &HFF

x = Fix(x / 2) And &HFF

If J <> 0 Then

crc8 = crc8 Xor &H8C

```vb
End If

Next k

Next

```
Docrc8 = crc8

```vb
End Function

'*****************************************************************

```
Public Function CRC16(buf() As Byte, lbuf As Integer) As Integer

```vb
Dim CRC1 As Long

Dim b As Boolean

```
CRC1 = 0 ' init CRC

For i = 1 To lbuf ' for each byte

CRC_MSB = CRC1 \ 256

crc_LSB = CRC1 And 255

CRC_MSB = CRC_MSB Xor buf(i)

CRC1 = (CRC_MSB * 256) + crc_LSB

For J = 0 To 7 Step 1 ' for each bit

CRC1 = shl(CRC1, b)

```vb
If b Then CRC1 = CRC1 Xor &H1021

Next J

Next i

```
CRC16 = CRC1

```vb
End Function

'Shift Left function

Function shl(n As Long, ByRef b As Boolean) As Long

Dim L As Long

```
L = n

L = L * 2

If (L > &HFFFF&) Then

b = True

Else

b = False

End If

shl = L And &HFFFF&

End Function

See also

[CHECKSUM](checksum.md) , [CRC8](crc8.md), [CRC16UNI](crc16uni.md) , [CRC32](crc32.md) , [TCPCHECKSUM](tcpchecksum.md) , [CRCMB](crcmb.md) , [CRC8UNI](crc8uni.md)

ASM

The following routine is called from mcs.lib : _CRC16

The routine must be called with X pointing to the data. The soft stack âY must contain the number of bytes to scan.

On return, R16 and R17 contain the CRC16 value.

The used registers are : R16-R19, R25.

;##### X = Crc16(ar(1) , 7)

Ldi R24,$07 ; number of bytes

St ây, R24

Ldi R26,$64 ; address of ar(1) 

Ldi R27,$00 ; load constant in register

Rcall _Crc16 ; call routine

Ldi R26,$60 ; address of X

St X+,R16 ; store crc16 LSB

St X , R17 ; store CRC16 MSB

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

L = Crc32(ar(1) , 3) '494976085

End