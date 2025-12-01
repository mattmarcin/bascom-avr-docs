# SOCKETLISTEN

Action

Opens a socket in server(listen) mode.

Syntax

SOCKETLISTEN socket

Remarks

Socket | The socket number you want to use for the server in the range of 0 -3. Or 0-7 for W5200/W5300.  
---|---  
  
The socket will listen to the port you specified with the GetSocket function.

When a client connects, the socket status changes in sock_established. When a connection is established, you can send or receive data.

After the connection is closed by either the client or the server, a new connection need to be created and the SocketListen statement must be used again.

When the status has changed to sock_closed, there still could be some pending data in the receive buffer. So you could check with the SOCKETSTAT function if there is data waiting. And if data is waiting, you can read it with TCPREAD before opening the socket again. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETDISCONNECT](socketdisconnect.md)

Example

See [SOCKETCONNECT](socketconnect.md) example