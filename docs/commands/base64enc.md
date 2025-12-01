# BASE64ENC

Action

Converts a string into the Base-64 representation.

Syntax

Result = BASE64ENC( source)

Result = BASE64ENC( array, length)

Remarks

Result | A string variable that is assigned with the base64 coded string.  
---|---  
Source | The source string that must be coded.  
array | The first element of a byte array.   
length | The number of elements to convert. Maximum 255.   
  
Base-64 is not an encryption protocol. It sends data in 7-bit ASCII data format. MIME, web servers, and other Internet servers and clients use Base-64 coding.

The provided Base64Enc() function is an encoding function. You need it when you want to send attachments with POP3 for example.

The target string will use 1 additional byte for every 3 bytes. This means that the target string is ca. 33 % longer than the source string.

So make sure the target string is dimensioned longer then the original string.

Because strings can not contain a 0 byte, there is an alternative syntax. Instead of a string you pass the address of a byte array that contains the data you want to convert.

Because there is no end of string marker, you must provide the number of elements to convert. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [BASE64DEC](base64dec.md), [URL2IP](url2ip.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "tcpip.lbx"

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim S As String * 15 , Z As String * 15

```
S = "bWFyazptYXJr"

Z = Base64dec(s)

Print Z 'mark:mark

s = Base64Enc(z)

```vb
Print s

End

```
Example 2

```vb
$regfile = "m32U4def.dat"  
$crystal = 16000000  
$baud = 19200  
  
Dim S As String * 80 , Z As String * 80 , B As Byte , J As Byte  
Dim Ar(81) As Byte At S Overlay  
  
```
S = "This is a test"  
'while we load the array with string data, we could load it with any data that can contain a 0.  
  
B = Len(s) + 1 'get the length and the 0 byte  
Z = Base64enc(ar(1) , B) 'use an array  
Print Z  
  
Ar(1) = Base64dec(z , B) 'now B will hold the number of elements  
  
```vb
Print B  
  
'Another example  
```
Ar(1) = 0 : Ar(2) = 1 : Ar(3) = 2  
Z = Base64enc(ar(1) , 3) 'use an array  
Print Z  
  
  
Ar(1) = Base64dec(z , B) 'now B will hold the number of elements  
```vb
For J = 1 To B  
Print Ar(j)  
Next  
End  


```