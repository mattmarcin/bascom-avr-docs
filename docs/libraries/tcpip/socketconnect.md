# SOCKETCONNECT

Action

Establishes a connection to a TCP/IP server.

Syntax

Result = SOCKETCONNECT(socket, IP, port [,nowait])

Remarks

Result | A byte that is assigned with 0 when the connection succeeded. It will return 1 when an error occurred.  
---|---  
socket | The socket number in the range of 0-3. Or 0-7 for W5200/W5300.  
IP | The IP number of the server you want to connect to. This may be a number like 192.168.0.2 or a LONG variable that is assigned with an IP number. Note that the LSB of the LONG, must contain the MSB of the IP number.  
Port | The port number of the server you are connecting to.  
NoWait | This is an optional parameter. Make it 1 to suppress waiting for a connection. By default, when you create a connection, the code waits for the connect flag. But waiting will block program execution. When you specify, not to wait, the code returns immediately. But you must use [SOCKETSTAT](socketstat.md) to determine the outcome of the socketconnect.  NOWAIT parameter is implemented for :  -W5100 -W5200 -W5500  
  
You can only connect to a server. Standardized servers have dedicated port numbers. For example, the HTTP protocol(web server) uses port 80.

After you have established a connection the server might send data. This depends entirely on the used protocol. Most servers will send some welcome text, this is called a banner.

You can send or receive data once the connection is established.

The server might close the connection after this or you can close the connection yourself. This also depends on the protocol.

You need to obtain a valid socket first with the GETSOCKET function.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : servertest_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : start the easytcp after the chip is programmed  
' and create 2 connections  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
  
$hwstack = 128 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 128 ' default use 40 for the frame space  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit ' xram access  
```vb
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
Result = Tcpwrite(idx , "Hello from W5100A{013}{010}") ' send welcome  
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
Result2 = Tcpwrite(idx ,"12:00:00{013}{010}") ' you should send date$ or time$  
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