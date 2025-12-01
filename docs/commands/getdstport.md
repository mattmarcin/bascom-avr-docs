# GETDSTPORT

Action

Returns the port number of the peer.

Syntax

Result = GETDSTPort( socket)

Remarks

Result | A WORD variable that is assigned with the port number of the peer or destination port number.  
---|---  
Socket | The socket number in the range from 0-3  
  
When you are in server mode, it might be desirable to detect the port number of the connecting client.

You can use this for logging, security, etc.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [GETDSTIP](getdstip.md), [URL2IP](url2ip.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : servertest_TWI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : start the easytcp after the chip is programmed  
' and create 2 connections  
'micro : Mega88  
'suited for demo : no  
'commercial addon needed : yes  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
  
$hwstack = 128 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 128 ' default use 40 for the frame space  
' xram access  
Print "Init , set IP to 192.168.1.70" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
  
  
Dim Bclient As Byte ' socket number  
Dim Idx As Byte  
Dim Result As Word , Result2 As Word ' result  
Dim S As String * 80  
Dim Flags As Byte  
Dim Peer As Long  
Dim L As Long  
  
  
Do  
Waitms 1000  
For Idx = 0 To 3  
```
Result = Socketstat(idx , 0) ' get status  
```vb
Select Case Result  
Case Sock_established  
If Flags.idx = 0 Then ' if we did not send a welcome message yet  
```
Flags.idx = 1  
Result = Tcpwrite(idx , "Hello from W3100A{013}{010}") ' send welcome  
End If  
Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting  
```vb
Print "Received : " ; Result  
If Result > 0 Then  
Do  
Print "Result : " ; Result  
```
Result = Tcpread(idx , S)  
Print "Data from client: " ; Idx ; " " ; Result ; " " ; S  
Peer = Getdstip(idx)  
```vb
Print "Peer IP " ; Ip2str(peer)  
Print "Peer port : " ; Getdstport(idx)  
'you could analyse the string here and send an appropiate command  
'only exit is recognized  
If Lcase(s) = "exit" Then  
```
Closesocket Idx  
Elseif Lcase(s) = "time" Then  
Result2 = Tcpwrite(idx , "12:00:00{013}{010}")' you should send date$ or time$  
```vb
End If  
Loop Until Result = 0  
End If  
Case Sock_close_wait  
Print "close_wait"  
```
Closesocket Idx  
```vb
Case Sock_closed  
Print "closed"  
```
Bclient = Getsocket(idx , Sock_stream , 5000 , 64) ' get socket for server mode, specify port 5000  
Print "Socket " ; Idx ; " " ; Bclient  
  
Socketlisten Idx  
Print "Result " ; Result  
Flags.idx = 0 ' reset the hello message flag  
```vb
Case Sock_listen ' this is normal  
Case Else  
Print "Socket status : " ; Result  
End Select  
Next  
Loop  
  
  
  
End

```