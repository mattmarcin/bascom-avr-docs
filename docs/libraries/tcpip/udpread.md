# UDPREAD

Action

Reads data via UDP protocol.

Syntax

Result = UDPREAD( socket , var, bytes)

Remarks

Result | A byte variable that will be assigned with 0, when no errors occurred. When an error occurs, the value will be set to 1. When there are not enough bytes in the reception buffer, the routine will wait until there is enough data or the socket is closed.  
---|---  
socket | The socket number you want to read data from (0-3). Or 0-7 for W5200/W5300  
Var | The name of the variable that will be assigned with the data from the socket.  
Bytes | The number of bytes to read.  
  
Reading strings is not supported for UDP.

When you need to read a string you can use the OVERLAY option of DIM.

There will be no check on the length so specifying to receive 2 bytes for a byte will overwrite the memory location after the memory location of the byte.

W3100

The socketstat function will return a length of the number of bytes + 8 for UDP. This because UDP also includes an 8 byte header. It contains the length of the data, the IP number of the peer and the port number.

The UDPread function will fill the following variables with this header data:

Peersize, PeerAddress, PeerPort

These variables are dimensioned automatically when you use CONFIG TCPIP.

W5100,W5200,W5300

The peersize, peerport and peeraddress have a different order in the W5x00. To avoid mistakes, the compiler will create these variables automatic in the proper order. The NOUDP=1 option can disable this feature if you do not use UDP.

When reading UDP, you need to use the [UDPREADHEADER](udpreadheader.md) statement to read the UDP header. After reading the header, the peersize, peerport and peeraddress variables are set.

You then should use the peersize variable to determine the number of bytes to retrieve. You must read all these bytes. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITE](udpwrite.md), [UDPWRITESTR](udpwritestr.md) , [UDPREADHEADER](udpreadheader.md) , [IP2STR](ip2str.md), [URL2IP](url2ip.md)

Example W3100

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