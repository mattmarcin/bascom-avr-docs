# URL2IP

Action

This function returns the IP address of an URL.

Syntax

ip=URL2IP(URL)

Remarks

This function performs a DNS query to the google DNS server with address 8.8.8.8.

It returns either a 0 IP address or the IP address of the URL.

The URL must be a string or string constant.

At the moment, this function is only supported by the W5100 and W5200.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [BASE64ENC](base64enc.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : PING_SPI.bas http://www.faqs.org/rfcs/rfc792.html  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : Simple PING program  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 64 for the hardware stack  
$swstack = 64 ' default use 64 for the SW stack  
$framesize = 180 ' default use 80 for the frame space  
  
  
```
Const Cdebug = 1  
  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
  
'Configuration Of The SPI bus  
Config Spi = Hard , Interrupt = Off , Data_order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
  
```vb
'we do the usual  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1 , Cs = Portb.2  
Print "Init done"  
  
Dim Idx As Byte , Result As Word , J As Byte , Res As Byte  
Dim Ip As Long  
Dim Dta(12) As Byte , Rec(12) As Byte  
  
  
```
Dta(1) = 8 'type is echo  
Dta(2) = 0 'code  
  
Dta(3) = 0 ' for checksum initialization  
Dta(4) = 0 ' checksum  
Dta(5) = 0 ' a signature can be any number  
Dta(6) = 1 ' signature  
Dta(7) = 0 ' sequence number - any number  
Dta(8) = 1  
Dta(9) = 65  
  
```vb
Dim W As Word At Dta(1) + 2 Overlay 'same as dta(3) and dta(4)  
Dim B As Byte  
```
W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)  
  

```vb
#if Cdebug  
For J = 1 To 9  
Print Dta(j)  
Next  

#endif  
  
```
Ip = Url2ip( "mcselec.com")  
```vb
Print Ip2str(ip)  
If Ip = 0 Then End  
  
  
Print "Socket " ; Idx ; " " ; Idx  
```
Setipprotocol Idx , 1 'set protocol to 1  
'the protocol value must be set BEFORE the socket is openend  
  
Idx = Getsocket(idx , 3 , 5000 , 0)  
  
```vb
Do  
' Result = Gettcpregs(&H403 , 2) : Print Hex(result)  
  
' Print Hex(s_status(1))  
```
Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) 'write ping data '  
```vb
Print "W:" ; Result  
Waitms 300 ' depending on the hops, speed, etc  
```
Result = Socketstat(idx , Sel_recv) 'check for data  
```vb
Print "REC:" ; Result  
If Result >= 11 Then  
Print "Ok"  
```
Res = Tcpread(idx , Rec(1) , Result) 'get data with TCPREAD !!!  

```vb
#if Cdebug  
Print "DATA RETURNED :" ; Res '  
For J = 1 To Result  
Print Rec(j) ; " " ;  
Next  
Print  

#endif  
Else 'there might be a problem  
Print "Network not available"  
End If  
Waitms 10000  
Loop

```