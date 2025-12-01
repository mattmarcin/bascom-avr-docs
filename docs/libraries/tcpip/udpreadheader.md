# UDPREADHEADER

Action

This statement reads the UDP header from the specified socket.

Syntax

UDPREADHEADER socket

Remarks

UDP packets start with a 8 byte header. This header contains the peer address, port and packet size. The UDPREADHEADER reads the header and places the information into the variables PEERADDRESS, PEERPORT and PEERSIZE.

After you have read the UDP header, you can use PEERSIZE to read the number of bytes available in the packet. 

Socket is a constant or variable in the range from 0-3. And 0-7 for the W5200/W5300.

UDPREADHEADER is only available for the W5x00.

See also

[UDPREAD](udpread.md), [CONFIG TCPIP](config_tcpip.md) , [TCPREADHEADER](tcpreadheader.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : udptest_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : start the easytcp.exe program after the chip is programmed and  
' press UDP button  
'micro : Mega88  
'suited for demo : no  
'commercial addon needed : yes  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 64 ' default use 32 for the hardware stack  
$swstack = 64 ' default use 10 for the SW stack  
$framesize = 50 ' default use 40 for the frame space  
  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
```vb
Print "Init , set IP to 192.168.1.70" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 5000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
  
  
  
Dim Idx As Byte ' socket number  
Dim Result As Word ' result  
Dim S(255) As Byte  
Dim Sstr As String * 255  
Dim Temp As Byte , Temp2 As Byte ' temp bytes  
  
```
Const Showresult = 1  
  
```vb
Print "UDP demo"  
  
Dim Ip As Long  
```
Ip = Maketcp(192.168.1.3) 'assign IP num  
  
```vb
'like with TCP, we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx ; " " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
Do  
```
Temp = Inkey() ' wait for terminal input  
If Temp = 27 Then ' ESC pressed  
Sstr = "Hello"  
Result = Udpwritestr(ip, 5000, Idx, Sstr, 255)  
Elseif Temp = 32 Then ' space  
```vb
Do  
Waitms 200  
Dim Tel As Long : Incr Tel  
```
Sstr = "0000000000111111111122222222223333333333 " + Str(tel)  
Result = Udpwritestr(ip , 5000 , Idx , Sstr , 255)  
```vb
Loop  
End If  
```
Result = Socketstat(idx, Sel_recv) ' get number of bytes waiting  
```vb
If Result > 0 Then  
Print "Bytes waiting : " ; Result  
  
```
Udpreadheader Idx ' read the udp header  
  

```vb
#if Showresult  
Print  
Print Peersize; " "; Peeraddress; " "; Peerport ' these are assigned when you use UDPREAD  
Print Ip2str(peeraddress) ' print IP in usual format  

#endif  
  
  
If Peersize > 0 Then ' the actual number of bytes  
Print "read" ; Peersize  
```
Temp = Udpread(idx, S(1), Peersize) ' read the result  
  

```vb
#if Showresult  
For Temp = 1 To Peersize  
Print S(temp); " " ; ' print result  
Next  
Print "done"  

#endif  
```
Result = Udpwrite(ip, Peerport, Idx, S(1), Peersize) ' write the received data back  
```vb
End If  
End If  
Loop  
'the sample above waits for data and send the data back for that reason temp2 is subtracted with 8, the header size  
  
  
End

```