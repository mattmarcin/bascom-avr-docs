# GETDSTIP

Action

Returns the IP address of the peer.

Syntax

Result = GETDSTIP( socket)

Remarks

Result | A LONG variable that will be assigned with the IP address of the peer or destination IP address.  
---|---  
Socket | The socket number (0-3)  
  
When you are in server mode, it might be desirable to detect the IP address of the connecting client.

You can use this for logging, security, etc.

The IP number MSB, is stored in the LS byte of the variable.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [GETDSTPORT](getdstport.md), [URL2IP](url2ip.md)

Partial Example

Dim L as Long

L = GetdstIP(i) ' store current IP number of socket i