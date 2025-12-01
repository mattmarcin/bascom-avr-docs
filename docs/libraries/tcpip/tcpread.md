# TCPREAD

Action

Reads data from an open socket connection.

Syntax

Result = TCPREAD( socket , var, bytes)

Remarks

Result | A byte variable that will be assigned with 0, when no errors occurred. When an error occurs, the value will be set to 1. When there are not enough bytes in the reception buffer, the routine will wait until there is enough data or the socket is closed.  
---|---  
socket | The socket number you want to read data from (0-3). Or 0-7 for W5200/W5300.  
Var | The name of the variable that will be assigned with the data from the socket.  
Bytes | The number of bytes to read. Only valid for non-string variables.  
  
When you use TCPread with a string variable, the routine will wait for CR + LF and it will return the data without the CR + LF.

```vb
For strings, the function will not overwrite the string.

For example, your string is 10 bytes long and the line you receive is 80 bytes long, you will receive only the first 10 bytes after CR + LF is encountered.

```
Also, for string variables, you do not need to specify the number of bytes to read since the routine will wait for CR + LF.

For other data types you need to specify the number of bytes.

There will be no check on the length so specifying to receive 2 bytes for a byte will overwrite the memory location after the memory location of the byte.

You should only attempt to read data if you have determined with the SocketStat function, that there is actual data in the receive buffer.

$BIGSTRINGS are not supported by TCPREAD. 

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Partial Example

Result = Socketstat(idx , Sel_recv) ' get number of bytes waiting

If Result > 0 Then

Result = Tcpread(idx , S)

End If