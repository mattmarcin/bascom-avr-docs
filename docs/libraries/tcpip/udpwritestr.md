# UDPWRITESTR

Action

Sends a string via UDP.

Syntax

Result = UDPwriteStr( IP, port, socket , var , param)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
IP | The IP number you want to send data to. Use the format 192.168.0.5 or use a LONG variable that contains the IP number.  
Port | The port number you want to send data too.  
Socket | The socket number you want to send data to (0-3).  
Var | The name of a string variable.  
Param | A parameter that might be 0 to send only the string or 255, to send the string with an additional CR + LF This option was added because many protocols expect CR + LF after the string.  
  
The UDPwriteStr function is a special variant of the UDPwrite function.

It will use UDPWrite to send the data.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITE](udpwrite.md), [UDPREAD](udpread.md), [URL2IP](url2ip.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : udptest.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : start the easytcp.exe program after the chip is programmed and

' press UDP button

'micro : Mega161

'suited for demo : no

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "m161def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

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

Dim Idx As Byte ' socket number

Dim Result As Word ' result

Dim S(80) As Byte

Dim Sstr As String * 20

Dim Temp As Byte , Temp2 As Byte ' temp bytes

'--------------------------------------------------------------------------------------------

'When you use UDP, you need to dimension the following variables in exactly the same order !

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

'--------------------------------------------------------------------------------------------

Declare Function Ipnum(ip As Long) As String ' a handy function

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

Result = Udpwritestr(192.168.0.3 , 5000 , Idx , Sstr , 255)

End If

Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

```vb
If Result > 0 Then

Print "Bytes waiting : " ; Result

```
Temp2 = Result - 8 'the first 8 bytes are always the UDP header which consist of the length, IP number and port address

Temp = Udpread(idx , S(1) , Result) ' read the result

```vb
For Temp = 1 To Temp2

Print S(temp) ; " " ; ' print result

Next

Print

Print Peersize ; " " ; Peeraddress ; " " ; Peerport ' these are assigned when you use UDPREAD

Print Ipnum(peeraddress) ' print IP in usual format

```
Result = Udpwrite(192.168.0.3 , Peerport , Idx , S(1) , Temp2) ' write the received data back

```vb
End If

Loop

'the sample above waits for data and send the data back for that reason temp2 is subtracted with 8, the header size

'this function can be used to display an IP number in normal format

Function Ipnum(ip As Long) As String

```
Local T As Byte , J As Byte

Ipnum = ""

For J = 1 To 4

T = Ip And 255

Ipnum = Ipnum + Str(t)

If J < 4 Then Ipnum = Ipnum + "."

Shift Ip , Right , 8

```vb
Next

End Function

End

```