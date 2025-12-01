# XTEAENCODE

Action

Encrypts a variable or array using the XTEA protocol.

Syntax

XTEAENCODE Msg , Key , size

Remarks

Msg | The variable to encrypt. Encryption is performed in blocks of 8 bytes. This means that you need to specify an array that has a minimal size of 8 bytes. For example, 2 Longs will be 8 bytes in size. After the encryption is performed, Msg will contain the encrypted data. The original data will be overwritten.  
---|---  
Key | The 128 bit key which is used to encrypt the message data. You need to pass this as an array of 16 bytes.   
Size | The number of bytes to encrypt. This must be a multiple of 8.   
  
The XTEA encryption/decryption is described well at <http://en.wikipedia.org/wiki/XTEA>

The XTEA is an enhanced version of the TEA encryption protocol.

The XTEA encoding/decoding routines have a small footprint. You could use the XTEADECODE in a bootloader and encrypt your firmware.

When you use other tools to encode your data, you will find differences because of memory order. You can use the xtea2.lib for using the same memory order.

Include it in your code like : $LIB "xtea2.lib" 

See also

[$LOADER](loader.md) , [$AESKEY](_aeskey.md) , [AESENCRYPT](aesencrypt.md) , [AESDECRYPT](aesdecrypt.md) , [DESENCRYPT](desencrypt.md) , [DESDECRYPT](desdecrypt.md) , [$XTEAKEY](xteakey.md) , [XTEADECODE](xteadecode.md)

Example

```vb
'----------------------------------------------------------  
' XTEA.BAS  
' This sample demonstrates the XTEA encryption/decryption  
' statements  
' (c) 1995-2025 MCS Electronics  
'----------------------------------------------------------  
$regfile = "m88def.dat"  
$hwstack = 40  
$swstack = 32  
  
  
'The XTEA encryption/decryption has a small footprint  
'XTEA processes data in blocks of 8 bytes. So the minimum length of the data is 8 bytes.  
'A 128 bit key is used to encrypt/decrypt the data. You need to supply this in an array of 8 bytes.  
  
'Using the encoding on a string can cause problems when the data contains a 0. This is the end of the string marker.  
  
Dim Key(16) As Byte ' 128 bit key  
Dim Msg(32) As Byte ' this need to be a multiple of 8  
  
Dim B As Byte ' counter byte  
  
For B = 1 To 16 ' create a simple key and also fill the data  
```
Key(b) = B  
Msg(b) = B  
Next  
  
  
Xteaencode Msg(1) , Key(1) , 32 ' encode the data  
  
```vb
For B = 1 To 16  
Print Hex(msg(b)) ; " , " ;  
Next  
Print  
  
  
```
Xteadecode Msg(1) , Key(1) , 32 ' decode the data  
  
```vb
For B = 1 To 16  
Print Hex(msg(b)) ; " , " ;

Next ' it should print 1-16 now  
Print  
  
End

```