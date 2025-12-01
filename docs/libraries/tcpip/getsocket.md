# GETSOCKET

Action

Creates a socket for TCP/IP communication.

Syntax

Result = GETSOCKET(socket, mode, port, param)

Remarks

Result | A byte that is assigned with the socket number you requested. When the operation fails, it will return 255.  
---|---  
socket | A numeric constant or variable with the socket number. The socket number is in range of 0-3. And 0-7 for the W5200 and W5300.  
Mode | The socket mode. Use sock_stream(1), sock_dgram(2), sock_ipl_raw(3) or macl_raw(4). The modes are defined with constants. The W5100,W5200,W5300 also have the sock_ppoe(5) mode. For TCP/IP communication you need to specify sock_stream or the equivalent value 1. For UDP communication you need to specify sock_dgram or the equivalent value 2.  
Port | This is the local port that will be used for the communication. You may specify any value you like but each socket must have itâs own local port number. When you use 0, the value of LOCAL_PORT will be used. LOCAL_PORT is assigned with CONFIG TCPIP. After the assignment, LOCAL_PORT will be increased by 1. So the simplest way is to setup a local port with CONFIG TCPIP, and then use 0 for port.  
Param | Optional parameter. Use 0 for default. W3100 128 : send/receive broadcast message in UDP 64 : use register value with designated timeout value 32 : when not using no delayed ack 16: when not using silly window syndrome Consult the W3100A documentation for more information. W5100,W5200,W5300 128 : enable multicasting in UDP 32 : enable 'No delayed ACK' operation. Only for TCP/IP. In case of UDP multicast : 1 : use IGMP version 1, otherwise V 2. Consult the wiznet documentation for more information.  
  
After the socket has been initialized you can use SocketConnect to connect to a client, or SocketListen to act as a server.

W5100

When GetSocket does not return a valid socket number you can use a [SOCKETDISCONNECT](socketdisconnect.md) when it is in status &H18. For some reason the socket can remain in status &H18 for over a minutes and a SOCKETDISCONNECT will free the socket quicker.

See also

[CONFIG TCPIP](config_tcpip.md), [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

I = Getsocket(0 , Sock_stream , 5000 , 0)' get a new socket