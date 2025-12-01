# TCPIP

The TCPIP library allows you to use the W3100A internet chip from [www.iinchip.com](<http://www.iinchip.com>)

There are also libraries for W5100, W5200 and W5300.

MCS has developed a special development board that can get you started quickly with TCP/IP communication. Look at [http://www.mcselec.com](<http://mcselec.com/index.php?option=com_content&task=view&id=18&Itemid=41>) for more info.

All tcpip lbx files areshipped with BASCOM-AVR

The following functions are provided:

[CONFIG TCPIP](config_tcpip.md) | Configures the W3100 chip.  
---|---  
[GETSOCKET](getsocket.md) | Creates a socket for TCP/IP communication.  
[SOCKETCONNECT](socketconnect.md) | Establishes a connection to a TCP/IP server.  
[SOCKETSTAT](socketstat.md) | Returns information of a socket.  
[TCPWRITE](tcpwrite.md) | Write data to a socket.  
[TCPWRITESTR](tcpwritestr.md) | Sends a string to an open socket connection.  
[TCPREAD](tcpread.md) | Reads data from an open socket connection.  
[CLOSESOCKET](socketclose.md) | Closes a socket connection.  
[SOCKETLISTEN](socketlisten.md) | Opens a socket in server(listen) mode.  
[GETDSTIP](getdstip.md) | Returns the IP address of the peer.  
[GETDSTPORT](getdstport.md) | Returns the port number of the peer.  
[BASE64DEC](base64dec.md) | Converts Base-64 data into the original data.  
[BASE64ENC](base64enc.md) | Convert a string into a BASE64 encoded string.  
[MAKETCP](maketcp.md) | Encodes a constant or 4 byte constant/variables into an IP number  
[UDPWRITE](udpwrite.md) | Write UDP data to a socket.  
[UDPWRITESTR](udpwritestr.md) | Sends a string via UDP.  
[UDPREAD](udpread.md) | Reads data via UDP protocol.  
  
The MCS webshop offers the WIZ810MJ ethernet module, and a special converter board so it has few connections.

[WIZ810MJ module](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=266&category_id=22&option=com_phpshop&Itemid=1>)

[TCPADB5100 adapter board. ](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=267&category_id=22&option=com_phpshop&Itemid=1>)