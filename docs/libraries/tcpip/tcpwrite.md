# TCPWRITE

Action  
  
Write data to a socket.

Syntax

Result = TCPWRITE( socket , var , bytes)

Result = TCPWRITE( socket , EPROM, address , bytes)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
Socket | The socket number you want to send data to in the range from 0-3. Or 0-7 for the W5200/W5300.  
Var | A constant string like "test" or a variable. When you send a constant string, the number of bytes to send does not need to be specified.  
Bytes | A word variable or numeric constant that specifies how many bytes must be send.  
Address | The address of the data stored in the chips internal EEPROM. You need to specify EPROM too in that case.  
EPROM | An indication for the compiler so it knows that you will send data from EPROM.  
  
The TCPwrite function can be used to write data to a socket that is stored in EEPROM or in memory.

When you want to send data from an array, you need to specify the element : var(idx) for example.

The amount of data you can send depends on the socket TX size. With CONFIG TCPIP you can define the TX buffer size.

For example, for the W5100, the maximum TX socket size is 2 KB. In this case the maximum data size you can send is 2048 bytes.

Bigger data should be send in multiple chucks. 

You should also consider the maximum packet size. If the packet size is 1460, sending more data will send multiple fragmented packets.

If you have enough RAM available, the best option is to use a buffer with the same size as the packet size. But if your memory it limited, you can let the chip handle this. 

The following sample function demonstrates how you can send multiple chunks. The sample uses a buffer named eth_buffer() with a size of 2048 bytes.

  
Function Write_databuf(byval Txsize As Word) As Word  
Local Strt As Word  
Strt = 1  
```vb
Do  
If Txsize > 2048 Then  
```
Write_databuf = Tcpwrite(idx_http , Eth_buffer(strt) , 2048)  
Txsize = Txsize - 2048 : Strt = Strt + 2048  
Else  
Write_databuf = Tcpwrite(idx_http , Eth_buffer(strt) , Txsize)  
```vb
Exit Do  
End If  
Loop  
```
Http_speed = Http_speed + txSize  
End function  
  


See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md) , [SETTCPREGS](settcpregs.md), [URL2IP](url2ip.md)

Example

Result = Tcpwrite(idx , "Hello from W3100A{013}{010}")