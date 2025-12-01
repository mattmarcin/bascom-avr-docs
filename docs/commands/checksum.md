# CHECKSUM CHECKSUMXOR

Action

Returns a checksum of a string.

Syntax

PRINT Checksum(var)

b = Checksum(var)

b = ChecksumXOR(var)

Remarks

Var | A string variable.  
---|---  
B | A numeric variable that is assigned with the checksum.  
  
The checksum is computed by counting all the bytes of the string variable.

The checksumXOR is computed by Xor-ing all the bytes of the string variable.

Checksums are often used with serial communication.

The checksum is a byte checksum. The following VB code is equivalent :

Dim Check as Byte

Check = 0

For x = 1 To Len(s$)

Check = check + ASC(mid$(s$,x,1))

Next

The following VB code is equivalent for ChecksumXOR

Dim Check as Byte

Check = 0

For x = 1 To Len(s$)

Check = check XOR ASC(mid$(s$,x,1))

Next

See also

[CRC8](crc8.md) , [CRC16](crc16.md) , [CRC32](crc32.md) , [CRC16UNI](crc16uni.md), [CRCMB](crcmb.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim S As String * 10 'dim variable

```
S = "test" 'assign variable

```vb
Print Checksum(s) 'print value (192)

End

```