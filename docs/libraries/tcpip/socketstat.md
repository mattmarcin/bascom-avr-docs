# SOCKETSTAT

Action

Returns information about a socket.

Syntax

Result = SOCKETSTAT( socket , mode)

Remarks

Result | A word variable that is assigned with the result.  
---|---  
Socket | The socket number you want to get information of in the range from 0-3. Or 0-7 for W5200/W5300)  
Mode | A parameter which specifies what kind of information you want to retrieve. SEL_CONTROL or 0 : returns the status register value SEL_SEND or 1 : returns the number of bytes that might be placed into the transmission buffer. Or in other words : the free transmission buffer space. SEL_RECV or 2 : returns the number of bytes that are stored in the reception buffer. Or in other words : the number of bytes received.  
  
The SocketStat function contains actual 3 functions. One to get the status of the connection, one to determine how many bytes you might write to the socket, and one to determine how many bytes you can read from the buffer.

When you specify mode 0, one of the following byte values will be returned:

W3100A

Value | State | Description  
---|---|---  
0 | SOCK_CLOSED | Connection closed  
1 | SOCK_ARP | Standing by for reply after transmitting ARP request  
2 | SOCK_LISTEN | Standing by for connection setup to the client when acting in passive mode  
3 | SOCK_SYNSENT | Standing by for SYN,ACK after transmitting SYN for connecting setup when acting in active mode  
4 | SOCK_SYNSENT_ACK | Connection setup is complete after SYN,ACK is received and ACK is transmitted in active mode  
5 | SOCK_SYNRECV | SYN,ACK is being transmitted after receiving SYN from the client in listen state, passive mode  
6 | SOCK_ESTABLISHED | Connection setup is complete in active, passive mode  
7 | SOCK_CLOSE_WAIT | Connection being terminated  
8 | SOCK_LAST_ACK | Connection being terminated  
9 | SOCK_FIN_WAIT1 | Connection being terminated  
10 | SOCK_FIN_WAIT2 | Connection being terminated  
11 | SOCK_CLOSING | Connection being terminated  
12 | SOCK_TIME_WAIT | Connection being terminated  
13 | SOCK_RESET | Connection being terminated after receiving reset packet from peer.  
14 | SOCK_INIT | Socket initializing  
15 | SOCK_UDP | Applicable channel is initialized in UDP mode.  
16 | SOCK_RAW | Applicable channel is initialized in IP layer RAW mode  
17 | SOCK_UDP_ARP | Standing by for reply after transmitting ARP request packet to the destination for UDP transmission  
18 | SOCK_UDP_DATA | Data transmission in progress in UDP RAW mode  
19 | SOCK_RAW_INIT | W3100A initialized in MAC layer RAW mode  
  
W5100,W5200,W5300

Value | State | Description  
---|---|---  
0 | SOCK_CLOSED | Connection closed  
&H11 | SOCK_ARP | Standing by for reply after transmitting ARP request  
&H14 | SOCK_LISTEN | Standing by for connection setup to the client when acting in passive mode  
&H15 | SOCK_SYNSENT | Standing by for SYN,ACK after transmitting SYN for connecting setup when acting in active mode  
&H16 | SOCK_SYNRECV | SYN,ACK is being transmitted after receiving SYN from the client in listen state, passive mode  
&H17 | SOCK_ESTABLISHED | Connection setup is complete in active, passive mode  
&H1C | SOCK_CLOSE_WAIT | Connection being terminated  
&H1D | SOCK_LAST_ACK | Connection being terminated  
&H18 | SOCK_FIN_WAIT | Connection being terminated  
&H1A | SOCK_CLOSING | Connection being terminated  
&H1B | SOCK_TIME_WAIT | Connection being terminated  
&H13 | SOCK_INIT | Socket initializing  
&H22 | SOCK_UDP | Applicable channel is initialized in UDP mode.  
&H32 | SOCK_RAW | Applicable channel is initialized in IP layer RAW mode  
&H42 | SOCK_MACRAW | Applicable channel is initialized in MAC layer RAW mode  
&H5F | SOCK_PPOE | Applicable channel is initialized in PPOE mode  
  
The SocketStat function is also used internal by the library.

For the W5300, if you use ALIGN=2, you need to take in mind that you must read the data buffer if it contains data. Do not call SocketStat again since it will read another 2 bytes to determine the received data size.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

Tempw = Socketstat(i , 0)' get status

```vb
Select Case Tempw

Case Sock_established

Case Else

End Select

```