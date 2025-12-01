# SOCKETCLOSE

Action

Closes a socket connection.

Syntax

SOCKETCLOSE socket [ , prm]

Remarks

Socket | The socket number you want to close in the range of 0-3 (0-7 for W5200/W5300). When the socket is already closed, no action will be performed.  
---|---  
Prm | An optional parameter to change the behavior of the CloseSocket statement. The following values are possible : | •| 0 - The code will behave as if no parameter has been set.  
---|---  
  
•| 1 - In normal cases, there is a test to see if all data written to the chip has been sent. When you set bit 0 (value of 1) , this test is not performed.  
---|---  
  
•| 2 - In normal cases, there is a test to see if the socket is actually closed after the command has been given to the chip. When it is not closed, you can not re-use the socket. The statement will block program execution however and you could test at a later time if the connection has been closed.  
---|---  
  
You may combine the values. So 3 will combine parameter value 1 and 2.

It is advised to use option value 1 with care.  
  
You must close a socket when you receive the SOCK_CLOSE_WAIT status.

You may also close a socket if that is needed by your protocol.

You will receive a SOCK_CLOSE_WAIT status when the server closes the connection.

When you use CloseSocket you actively close the connection.

Note that it is not needed to wait for a SOCK_CLOSE_WAIT message in order to close a socket connection.

After you have closed the connection, you need to use GetSocket in order to use the socket number again.

In normal conditions, without using the optional parameter, the statement can block your code for a short or longer time, depending on the connection speed.

The CLOSESOCKET statement is equivalent with SOCKETCLOSE. 

SOCKETCLOSE VS SOCKETDISCONNECT

In the W3x00 chips there was no socket disconnect function. A socket close (SOCKETCLOSE) would create a disconnect. 

But in the W5x00 chips, there is an additional function to disconnect a socket. So for these chips you must use SOCKETDISCONNECT to terminate a connection. After that you can still use SOCKETCLOSE to free the resource of the socket.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : clienttest.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : start the easytcp.exe program and listen to port 5000

'micro : Mega161

'suited for demo : no

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "M161def.dat"

$crystal = 4000000

$baud = 19200

$hwstack = 40 ' default use 40 for the hardware stack

$swstack = 40 ' default use 40 for the SW stack

$framesize = 64 ' default use64 for the frame space

```
Const Sock_stream = $01 ' Tcp

Const Sock_dgram = $02 ' Udp

Const Sock_ipl_raw = $03 ' Ip Layer Raw Sock

Const Sock_macl_raw = $04 ' Mac Layer Raw Sock

Const Sel_control = 0 ' Confirm Socket Status

Const Sel_send = 1 ' Confirm Tx Free Buffer Size

Const Sel_recv = 2 ' Confirm Rx Data Size

'socket status

Const Sock_closed = $00 ' Status Of Connection Closed

Const Sock_arp = $01 ' Status Of Arp

Const Sock_listen = $02 ' Status Of Waiting For Tcp Connection Setup

Const Sock_synsent = $03 ' Status Of Setting Up Tcp Connection

Const Sock_synsent_ack = $04 ' Status Of Setting Up Tcp Connection

Const Sock_synrecv = $05 ' Status Of Setting Up Tcp Connection

Const Sock_established = $06 ' Status Of Tcp Connection Established

Const Sock_close_wait = $07 ' Status Of Closing Tcp Connection

Const Sock_last_ack = $08 ' Status Of Closing Tcp Connection

Const Sock_fin_wait1 = $09 ' Status Of Closing Tcp Connection

Const Sock_fin_wait2 = $0a ' Status Of Closing Tcp Connection

Const Sock_closing = $0b ' Status Of Closing Tcp Connection

Const Sock_time_wait = $0c ' Status Of Closing Tcp Connection

Const Sock_reset = $0d ' Status Of Closing Tcp Connection

Const Sock_init = $0e ' Status Of Socket Initialization

Const Sock_udp = $0f ' Status Of Udp

Const Sock_raw = $10 ' Status of IP RAW

```vb
$lib "tcpip.lbx" ' specify the tcpip library

Print "Init , set IP to 192.168.0.8" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 0.0.0.0 , Localport = 1000 , Tx = $55 , Rx = $55

'Use the line below if you have a gate way

'Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Dim Bclient As Byte ' socket number

Dim Idx As Byte

Dim Result As Word ' result

Dim S As String * 80

For Idx = 0 To 3 ' for all sockets

```
Bclient = Getsocket(idx , Sock_stream , 0 , 0) ' get socket for client mode, specify port 0 so loal_port is used

```vb
Print "Local port : " ; Local_port ' print local port that was used

Print "Socket " ; Idx ; " " ; Bclient

```
Result = Socketconnect(idx , 192.168.0.3 , 5000) ' connect to easytcpip.exe server

```vb
Print "Result " ; Result

Next

Do

If Ischarwaiting() <> 0 Then ' is there a key waiting in the uart?

```
Bclient = Waitkey() ' get the key

```vb
If Bclient = 27 Then

Input "Enter string to send " , S ' send WHO , TIME or EXIT

For Idx = 0 To 3

```
Result = Tcpwritestr(idx , S , 255)

```vb
Next

End If

End If

For Idx = 0 To 3

```
Result = Socketstat(idx , 0) ' get status

```vb
Select Case Result

Case Sock_established

```
Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

```vb
If Result > 0 Then

Do

```
Result = Tcpread(idx , S)

```vb
Print "Data from server: " ; Idx ; " " ; S

Loop Until Result = 0

End If

Case Sock_close_wait

Print "close_wait"

```
Closesocket Idx

```vb
Case Sock_closed

'Print "closed"

End Select

Next

Loop

End

```