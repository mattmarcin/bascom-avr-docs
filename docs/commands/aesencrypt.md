# AESENCRYPT

Action

This statement of function uses the Xmega AES encryption engine to encrypt a block of data.

Syntax

AESENCRYPT  key, var , size

targ = AESENCRYPT ( key, var , size)

Remarks

key | The name of a label that contains 16 bytes of key data. Or an array holding 16 bytes of key data.  
---|---  
var | A variable or array containing the data to be encrypted. When you use the statement, this variable will contain the encrypted data after the conversion.  
size | The number of bytes to encrypt. Encryption is done with blocks of 16 bytes. So the size should be a multiple of 16. If you supply only 14 bytes this is ok too, but the result will still be 16 bytes. It is important that your array is big enough to hold the result.  Without the full 16 byte result, you can not decrypt the data.  
targ | In case you use the function, this variable will hold the result.   
  
This function only works for Xmega chips that have an AES encryption unit.

128 bit encryption is used.

You can either use a label with a fixed key, or use a variable.

You should use the same key data for encryption and decryption.

See also

[$LOADER](loader.md) , [$AESKEY](_aeskey.md) , [AESDECRYPT](aesdecrypt.md) , [DESENCRYPT](desencrypt.md) , [DESDECRYPT](desdecrypt.md) , [$XTEAKEY](xteakey.md) , [XTEAENCODE](xteaencode.md), [XTEADECODE](xteadecode.md)

Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-AES.bas  
' This sample demonstrates the Xmega128A1 AES encryption/decryption  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
'$external _aes_enc  
  
Dim Key(16) As Byte ' room for key  
Dim Ar(34) As Byte  
Dim Arenc(34) As Byte  
Dim J As Byte  
Print "AES test"  
  
```
Restore Keydata  
For J = 1 To 16 ' load a key to memory  
Read Key(j)  
```vb
Next  
  
'load some data  
For J = 1 To 32 ' fill some data to encrypt  
```
Ar(j) = J  
Next  
  
  
Aesencrypt Keydata , Ar(1) , 32  
```vb
Print "Encrypted data"  
For J = 1 To 32 ' fill some data to encrypt  
Print Ar(j)  
Next  
  
  
```
Aesdecrypt Keydata , Ar(1) , 32  
```vb
Print "Decrypted data"  
For J = 1 To 32 ' fill some data to encrypt  
Print Ar(j)  
Next  
  
Print "Encrypt function"  
```
Arenc(1) = Aesencrypt(keydata , Ar(1) , 32)  
```vb
For J = 1 To 32 ' fill some data to encrypt  
Print Ar(j) ; "-" ; Arenc(j)  
Next  
  
Print "Decrypt function"  
```
Ar(1) = Aesdecrypt(keydata , Arenc(1) , 32)  
  
```vb
For J = 1 To 32  
Print J ; ">" ; Ar(j) ; "-" ; Arenc(j)  
Next  
  
End  
  
  
  
```
Keydata:  
Data 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16