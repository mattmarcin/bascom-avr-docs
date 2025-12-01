# DESENCRYPT

Action

This statement of function uses the Xmega DES encryption engine to encrypt a block of data.

Syntax

targ = DESENCRYPT ( key, var , size)

Remarks

key | The name of a label that contains 16 bytes of key data. Or an array holding 16 bytes of key data.  
---|---  
var | A variable or array containing the data to be encrypted.  
size | The number of bytes to encrypt. Encryption is done with blocks of 16 bytes. So the size should be a multiple of 16. If you supply only 14 bytes this is ok too, but the result will still be 16 bytes. It is important that your array is big enough to hold the result.  Without the full 16 byte result, you can not decrypt the data.  
targ | An array of variable that will hold the result. Since the result will be at least 16 bytes long, this is only practical with arrays.   
  
This function only works for Xmega chips that have an DES encryption unit.

Normal DES encryption is used. The DES encryption is faster than the AES but also weaker. 

You can either use a label with a fixed key, or use a variable.

You should use the same key data for encryption and decryption.

See also

[$LOADER](loader.md) , [$AESKEY](_aeskey.md) , [AESENCRYPT](aesencrypt.md) , [AESDECRYPT](aesdecrypt.md) , [DESDECRYPT](desdecrypt.md) , [$XTEAKEY](xteakey.md) , [XTEAENCODE](xteaencode.md), [XTEADECODE](xteadecode.md)

Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-DES.bas  
' This sample demonstrates the Xmega128A3 DES encryption/decryption  
' Notice that you need to encrypt blocks with at least 8 bytes  
'-----------------------------------------------------------------  
$regfile = "xm128a3def.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
'configure used UART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "com1:" For Binary As #1  
  
```vb
Dim Key(8) As Byte ' room for key  
Dim Ar(34) As Byte  
Dim Arenc(34) As Byte  
Dim J As Byte  
  
Print #1 , "DES test"  
  
```
Restore Keydata  
For J = 1 To 8 ' load a key to memory  
Read Key(j)  
```vb
Next  
  
  
'load some data  
For J = 1 To 16 ' fill some data to encrypt  
```
Ar(j) = J  
```vb
Next  
  
  
Print #1 , "Encrypt function"  
```
Arenc(1) = Desencrypt(key(1) , Ar(1) , 16) 'encrypt 16 bytes  
  
  
```vb
For J = 1 To 16  
Print #1 , Ar(j) ; "-" ; Arenc(j) 'print result and original data  
Next  
  
  
Print #1 , "Decrypt function"  
```
Ar(1) = Desdecrypt(keydata , Arenc(1) , 16) 'decrypt and return in ar()  
  
```vb
For J = 1 To 16  
Print #1 , J ; ">" ; Ar(j) ; "-" ; Arenc(j) 'print index, decrypted data and encrypted data  
Next  
  
Do  
  
Loop  
  
End  
  
  
  
```
Keydata: ' key data can go into flash ROM or into sram  
Data 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8