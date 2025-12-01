# TCPREADHEADER

Action

This statement reads the TCP packet header from the specified socket.

Syntax

TCPREADHEADER socket

Remarks

This option is only available for the W5300 which includes a packet header with the packet size when align is set to 0.

TCP packets start with a 2 byte size header. 

After you have read the TCP header, you can use TCPDATASIZE to read the number of bytes available in the packet. 

TCPDATASIZE is a word variable you need to dimension yourself. 

Socket is a constant or variable in the range from 0-7.

See also

[UDPREAD](udpread.md), [CONFIG TCPIP](config_tcpip.md) , [UDPREADHEADER](udpreadheader.md), [URL2IP](url2ip.md), [URL2IP](url2ip.md)

Example