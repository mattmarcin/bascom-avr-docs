# MAKETCP

Action

Creates a TCP/IP formatted long variable.

Syntax

var = MAKETCP(b1,b2,b3,b4 [opt])

var = MAKETCP(num)

Remarks

var | The target variable of the type LONG that is assigned with the IP number  
---|---  
b1-b4 | Four variables of numeric constants that form the IP number. b1 is the MSB of the IP/long b4 is the LSB of the IP/long example var = MakeTCP(192,168,0, varx). We can also use reverse order with the optional parameter : example var = MakeTCP(var3,0,168, 192, 1 ). A value of 1 will use reverse order while a value of 0 will result in normal order. When you use a constant, provide only one parameter : example var = MakeTCP(192.168.0.2). Notice the dots !  
  
MakeTCP is a helper routine for the TCP/IP library.

See also

[CONFIG TCPIP](config_tcpip.md) , [IP2STR](ip2str.md), [URL2IP](url2ip.md)

Example

NONE