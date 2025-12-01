# SOCKETDISCONNECT

Action

Disconnects a socket connection.

Syntax

SOCKETDISCONNECT socket

Remarks

Socket | The socket number you want to close in the range of 0-3 (0-7 for W5200/W5300). When the socket is already closed, no action will be performed.  
---|---  
  
The socketdisconnect statement sends a connection termination request. 

You can also use SOCKETCLOSE to close the socket and free it's resources.

After you have closed the connection, you need to use GetSocket in order to use the socket number again.

If you only disconnect the socket, you can use socketconnect witout Getsocket.

The socketdisconnect is only intended for TCP connections. (UDP does not have connections).

![notice](notice.jpg)This statement is only available for the W5100/W5200/W5300. The W3100A does not support it.

SOCKETCLOSE VS SOCKETDISCONNECT

In the W3x00 chips there was no socket disconnect function. A socket close (SOCKETCLOSE) would create a disconnect. 

But in the W5x00 chips, there is an additional function to disconnect a socket. So for these chips you must use SOCKETDISCONNECT to terminate a connection. After that you can still use SOCKETCLOSE to free the resource of the socket.

See also

[CONFIG TCPIP](config_tcpip.md), [SOCKETCLOSE](socketclose.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETLISTEN](socketlisten.md) , [SETTCP](settcp.md), [URL2IP](url2ip.md)

Example

NONE