# UDPWRITE

Action

Write UDP data to a socket.

Syntax

Result = UDPwrite( IP, port, socket , var , bytes)

Result = UDPwrite( IP, port, socket , EPROM, address , bytes)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
IP | The IP number you want to send data to. Use the format 192.168.0.5 or use a LONG variable that contains the IP number.  
Port | The port number you want to send data too.  
Socket | The socket number you want to send data to(0-3).  
Var | A constant string like "test" or a variable. When you send a constant string, the number of bytes to send does not need to be specified.  
Bytes | A word variable or numeric constant that specifies how many bytes must be send.  
Address | The address of the data stored in the chips internal EEPROM. You need to specify EPROM too in that case.  
EPROM | An indication for the compiler so it knows that you will send data from EPROM.  
  
The UDPwrite function can be used to write data to a socket that is stored in EEPROM or in memory.

When you want to send data from an array, you need to specify the element : var(idx) for example.

Note that UDPwrite is almost the same as TCPwrite. Since UDP is a connection-less protocol, you need to specify the IP address and the port number.

![notice](notice.jpg) UDP only requires an opened socket. The is no connect or close needed.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [UDPWRITESTR](udpwritestr.md) , [UDPREAD](udpread.md) , [UDPREADHEADER](udpreadheader.md), [URL2IP](url2ip.md)

Example

See [UDPwriteStr](udpwritestr.md)