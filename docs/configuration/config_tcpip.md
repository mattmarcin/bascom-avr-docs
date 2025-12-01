# CONFIG TCPIP

Action

Configures the TCP/IP chip's from WIZNET (<http://www.wiznet.co.kr/>).

This chip's can be found on various modules and shields but the Config Tcpip is always depending on the WIZNET chip.

Supported chip's are W3100A, W5100, W5200 and W5300.

Syntax W3100A

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, TX= tx, RX= rx , NOINIT= 0|1 [, TWI=address] [, Clock = speed] [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=W3100A] 

Syntax W5100

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, TX= tx, RX= rx , NOINIT= 0|1 [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=5100] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] 

Syntax W5200

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [,TimeOut=tmOut] [,CHIP=W5200] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] [TXn= tx] [, RXn= rx] 

Syntax W5300

CONFIG TCPIP = int , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [, baseaddress = address] [,TimeOut=tmOut] [,CHIP=W5300] [,INT=imsg] [,NOUDP=noudp] [align=align] [TXn= tx] [, RXn= rx] [SOCKMEM=sockmem]

Syntax W5500

CONFIG TCPIP = NOINT , MAC = mac , IP = ip, SUBMASK = mask, GATEWAY = gateway, LOCALPORT= port, NOINIT= 0|1 [,TimeOut=tmOut] [,CHIP=W5500] [,SPI=spi] [,INT=imsg] [,CS=cs] [,NOUDP=noudp] [TXn= tx] [, RXn= rx] 

Remarks

Int | The interrupt to use such as INT0, INT1 or INTn. For the Easy TCP/IP PCB, use INT0. W5100,W5200,W5300 also support the NOINT option. This option will not use any interrupt. The internal status array s_status will not be created and is not available either.  When you do use interrupts, the s_status array will contain the status of each socket. s_status(1) will contain the status of the first socket. In interrupt mode you can also get a notification that a socket was updated when you use the INT=1 option. Using interrupts does use more code and resources.  W5500 only supports the NOINT option.  
---|---  
MAC | The MAC address you want to assign to the ethernet chip. The MAC address is a unique number that identifies your chip. You must use a different address for every ethernet chip in your network. Example : 00.00.12.34.56.78 You need to specify 6 bytes that must be separated by dots. The bytes must be specified in decimal notation. For some networks it is important that the MAC address starts with a zero. So we advise to start the MAC address with a 0.  
IP | The IP address you want to assign to the chip. The IP address must be unique for every ethernet chip in your network. When you have a LAN, 192.168.0.10 can be used. 192.168.0.x is used for LANâs since the address is not an assigned internet address. The same applies to 10.0.0.0.  
SUBMASK | The sub mask you want to assign to the ethernet chip. The sub mask is in most cases 255.255.255.0  
GATEWAY | This is the gateway address of the ethernet chip. The gateway connects your LAN with the internet. The gateway address you can determine with the IPCONFIG command at the command prompt : C:\>ipconfig Windows 2000 IP Configuration Ethernet adapter Local Area Connection 2: Connection-specific DNS Suffix . : IP Address. . . . . . . . . . . . : 192.168.0.3 Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 192.168.0.1 Use 192.168.0.1 in this case.  
LOCALPORT | A word value that is assigned to the LOCAL_PORT internal variable. See also [Getsocket](getsocket.md). As a default you can assign a value of 5000.  
TX | W3100A,W5100 A byte which specifies the transmit buffer size of the W3100A/W5100. The W3100A/W5100 has 4 sockets. A value of 00 will assign 1024 bytes, a value of 01 will assign 2048 bytes. A value of 10 will assign 4096 bytes and a value of 11 will assign 8192 bytes. This is binary notation. And the Most Significant bits (bit 6 and 7) specify the size of socket 3. For example, you want to assign 2048 bytes to each socket for transmission : TX = &B01010101 Since the transmission buffer size may be 8KB in total, you can split them up in 4 parts of 2048 bytes : 01. When you want to use 1 socket with 8KB size, you would use : TX = &B11. You can use only 1 socket in that case : socket 0. Consult the W3100A/W5100 pdf for more info.  
RX | W3100A,W5100 A byte which specifies the receive buffer size of the W3100A/W5100. The W3100A/W5100 has 4 sockets. A value of 00 will assign 1024 bytes, a value of 01 will assign 2048 bytes. A value of 10 will assign 4096 bytes and a value of 11 will assign 8192 bytes. This is binary notation. And the Most significant bits specify the size of socket 3. For example, you want to assign 2048 bytes to each socket for reception : RX = &B01010101 Since the receive buffer size may be 8KB in total, you can split them up in 4 parts of 2048 bytes : 01. When you want to use 1 socket with 8KB size, you would use : RX = &B11. You can use only 1 socket in that case : socket 0. Consult the W3100A/W5100 pdf for more info.  
TXn | W5200, W5300,w5500 A constant which specifies the socket size of the transmit buffer of socket n. N is in range of 1-8. This notation is only used by W5200 and W5300 where you can define the size in KB. By default the W5200 sockets are 2 KB each and the W5300 are 8 KB each. The following values are possible : | Value | W5200,W5500 | W5300  
---|---|---  
1 | 1 KB | 1 KB  
2 | 2 KB default | 2 KB  
4 | 4 KB | 4 KB  
8 | 8 KB | 8 KB default  
15 | 16 KB | 15 KB  
any other value between 1-64 | invalid  | size in KB  
  
The total amount may not exceed the available socket memory. For example the W5200 can use 8x2=16 KB of TX memory. But you can also use 2 sockets with 8 KB each.   
  
RXn | W5200,W5300,W5500 This will set the socket receive buffer size similar as described above for TXn.  
sockmem | W5300 The w5300 allows to configure how much of the memory is used for the transmit and receive buffers. The default is &HFF00 which will split the memory in even parts. See the W5300 datasheet for more details.  
Noinit | Make this option 1 when you want to configure the TCP, MAC, Subnetmask and GateWay dynamic. Noinit will only make some important settings and you need to use [SETTCP](settcp.md) in order to finish the setup.  
TWI | W3100A only The slave address of the W3100A/NM7010. When you specify TWI, your micro must have a TWI interface such as Mega128, Mega88, Mega32. TWI is only supported by the W3100A.  
Clock | W3100A only The clock frequency to use with the TWI interface. Use this in combination with the TWI option.  
Baseaddress | W3100A,W5100,W5300 An optional value for the chip select of the ethernet chip. This is default &H8000 when not specified. When you create your own board, you can override it. See also: [Adding XRAM with External Memory Interface](adding_xram.md)  
TimeOut | W3100A You can specify an optional timeout when sending UDP data. The Wiznet API does wait for the CSEND status. But it means that it will block your application. In such cases, you can use the timeout value. The timeout constant is a counter which decreases every time the status is checked. When it reaches 0, it will get out of the loop. Thus a higher value will result in a longer delay. Notice that it has nothing to do with the chip timeout registers/values. Without the software timeout, the chip will also time out.  W5100,W5200 and W5300 have a time out option in the hardware.  
CHIP | The wiznet chip you use. By default this is W3100. Specify W5100 for the W5100 chip. This chip has 4 sockets and a SPI interface instead of an I2C/TWI interface. Specify W5200 for the W5200 chip. This chip has 8 sockets and only a SPI interface. This SPI interface has a high speed. Specify W5300 for the W5300 chip. This chip has 8 sockets and can work in bus mode only. Specify W5500 for the W5500 chip. This chip has 8 sockets and only a SPI interface. This SPI interface supports high speed and blockmode.  
SPI | This option is intended to be used with the W5100/W5200 chips. When you want to use the W5100 or W5200 in SPI mode, make this parameter value 1.  When you do not specify his parameter, or set it to 0, the external memory mode will be used.  For the Xmega you can specify SPIC, SPID, SPIE of SPIF. For normal AVR with multiple SPI such as M328PB you can specify SPI1 When using SPI, you must configure it before configuring the TCPIP. SPI must be configured in mode 0. Example : Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0 'Init the spi pins  
Spiinit  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1 , Cs = Portb.4  
imsg | In interrupt mode, you can get a notification about changed socket status such as new data arrived, or socket closed. Use INT=1 for this option. The library will call a routine named TCP_INT. So your code need to include this label or sub routine. You can test the s_status() array but you can also test the _tcp_intflags variable. This variable contains the flags from the IR register. You must dimension the variable _tcp_intflags if you want to use this option.  
cs | This is an optional parameter used in combination with the SPI option. By default the compiler will use the standard SS pin for the SPI. But if you have multiple SPI slaves, or want to use a different pin to control the CS of the W5100/W5200, you can add this parameter. The name of a port pin is expected such as PORTB.4 ![notice](notice.jpg)You should use a normal port register. Do not use an extended address port like PORTL.  
noudp | By default UDP variables PEERADDRESS, PEERPORT and PEERSIZE are created by the compiler. If you do not use any UDP statement, you can use NOUDP=1. This will save 8 bytes of memory.  
align | The W5300 has an align option. Align is ignored for all other chips. The align modes : 0 \- this will disable alignment. This will add a header packet for TCP data with the size. You must use TCPREADHEADER to read the actual data size. [Socketstat](socketstat.md) will not return the actual data size. After you have determined there is data in the receive buffer, you must use TCPREADHEADER to get the actual size. You may only use TCPREADHEADER once since it will read 2 bytes from the receive buffer. 1\- this will enable alignment. This will not add the header packet to TCP data. SocketStat will return the actual data size. You must not use TCPREADHEADER in this case. 2\- since using alignment caused some unexpected problems in tcp traffic, (see wiznet forum) there is also the smart and default option which makes tcp reading compatible to the other chips. When using mode 2, the mode 0 will be used, and socketstat will automatic read the buffer size packet in case there is data in the received buffer and this it will return the correct size. Since it will read from the receive buffer, you must empty the buffer with tcpread, after you have determined that there is data waiting. You must not call [socketstat](socketstat.md) again before you have read all the pending data.  
  
The CONFIG TCPIP statement may be used only once.

If you do use interrupts, you must enable them before you use CONFIG TCPIP. When using the NOINT option this is not required.

Configuring the ethernet chip will initialize the chip.

After the CONFIG TCPIP, you can already PING the chip!

![notice](notice.jpg)As all the samples show, the CONFIG TCPIP must be used in the main program. The CONFIG TCPIP should be used early as possible in your code. This is especially important for processors with multiple pages. (>64KB). The reason is that the configuration data is stored in flash and read with LPM instruction. LPM can only reach page 0. 

W3100A

The TWI mode works only when your micro support the TWI mode. You need to have 4k7 pull up resistors.

MCS Electronics has a small adapter PCB and KIT available that can be connected easily to your microprocessor.

The TWI mode makes your PCB design much simpler. TWI is not as fast as bus mode. While you can use every supported TCP/IP function, it will run at a lower speed.

W5100

The W5100 is the successor of the W3100A. It is an improved chip without shadow registers. This means that less code is required to use the chip. 

Because the W5100 has different constants compared to the W3100A, the constants are removed from the samples. The constants are automatically created with a value depending on the chip you use.

From the user perspective the W5100 library is almost the same as the W3100 library. But there are some differences. 

\- The peersize, peerport and peeraddress have a different order in the W5100. To avoid mistakes, the compiler will create these variables automatic in the proper order. The NOUDP=1 option can disable this feature if you do not use UDP.

\- When reading UDP, you need to use the [UDPREADHEADER](udpreadheader.md) statement to read the UDP header. After reading the header, the peersize, peerport and peeraddress variables are set. You then should use the peersize variable to determine the number of bytes to retrieve. You must read all these bytes. 

\- The W5100 has a command to disconnect the socket in TCP/IP mode. It is named [SOCKETDISCONNECT](socketdisconnect.md).

\- The CLOSESOCKET statement has been renamed into [SOCKETCLOSE](socketclose.md). You can use both names. 

The MCS web shop offers the [WIZ810MJ](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=266&category_id=22&option=com_phpshop&Itemid=1>) ethernet module and the [TCPADB5100](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=267&category_id=22&option=com_phpshop&Itemid=1>) adapter board. 

W5200

The W5200 is a SPI only version of the W5100 so read the comment above about the W5100 first.

The W5200 chip has less pins and is smaller and simpler to use. It has 8 sockets instead of 4 and it has a faster SPI mode. One example where the W5200 is used is the Wiz820io module. See example below. 

This Chip need specific reset times before you can use config TCPIP (see example below).

It has been reported that when the RETRY_TIME and RETRY_COUNT registers are altered, sending UDP data can have a variable delay the first time the data will actually be sent. 

W5300

The W5300 is a bus mode only version of the W5100 so read the comment above about the W5100 first

The W5300 chip has a fast 8/16 bit bus and has 8 sockets with increased socket size. 

See also the W5300 examples in: [Adding XRAM with External Memory Interface](adding_xram.md) regarding base address.

W5500

The W5500 is a SPI only version of the W5100 so read the comment above about the W5100 first.

The W5500 chip has less pins and is smaller and simpler to use. It has 8 sockets instead of 4 and it has a faster SPI mode. It is similar to W5200.

For samples, use the W5200 samples and change CHIP to W5500.

The W5500 library has specific provision to be used in a boot loader.

WIZ810

REV 1.0 of the WIZ810 leaves the SPI_EN Pin floating (REV1.1 has an internal pulldown). When using REV1.0 in parallel mode, you will have to tie that pin to ground.

See also

[GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [CLOSESOCKET](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [SOCKETDISCONNECT](socketdisconnect.md) , [SETTCP](settcp.md) , [UDPREAD](udpread.md), [UDPWRITE](udpwrite.md), [UDPWRITESTR](udpwritestr.md) , [UDPREADHEADER](udpreadheader.md), [TCPREADHEADER](tcpreadheader.md) , [TCPCHECKSUM](tcpchecksum.md), [SNTP](sntp.md) , , [GETTCPREGS](gettcpregs.md) , [SETTCPREGS](settcpregs.md)

Syntax Example using W3100:

Config Tcpip = Int0 , Mac = 00.00.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

Now use PING at the command line to send a ping:

PING 192.168.0.8

Or use the easytcp application to ping the chip.

Syntax Example using W5100  
```vb
$regfile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 80 ' default use 40 for the frame space  
$lib "datetime.lbx" ' this example uses date time routines  
  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
Print "Init done"  
  
Dim Var As Byte ' for i2c test  
Dim Ip As Long ' IP number of time server  
Dim Idx As Byte ' socket number  
Dim Lsntp As Long ' long SNTP time  
  
Print "SNTP demo"  
  
'assign the IP number of a SNTP server  
```
Ip = Maketcp(64.90.182.55 ) ' assign IP num NIST time.nist.gov port 37  
```vb
Print "Connecting to : " ; Ip2str(ip)  
  
'we will use Dutch format  
Config Date = Dmy , Separator = -  
  
'we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx ; " " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
'The SNTP uses port 37 which is fixed in the tcp asm code  
  
Do  
Waitms 5000  
  
```
Lsntp = Sntp(idx , Ip) ' get time from SNTP server  
```vb
' Print Idx ; Lsntp  
'notice that it is not recommended to get the time every sec  
'the time server might ban your IP  
'it is better to sync once or to run your own SNTP server and update that once a day  
  
'what happens is that IP number of timer server is send a diagram too  
'it will put the time into a variable lsntp and this is converted to BASCOM date/time format  
'in case of a problem the variable is 0  
Print Date(lsntp) ; Spc(3) ; Time(lsntp)  
Loop  
  


```
Example for using W5200 Chip on a WIZ820io module with ATXMEGA:

Hardware connections:

WIZ820io [SCLK] <\-----> ATXMEGA128A1 PortC.7 [SCK]

WIZ820io [MOSI] <\-----> ATXMEGA128A1 PortC.5 [MOSI]

WIZ820io [MISO] <\-----> ATXMEGA128A1 PortC.6 [MISO]

WIZ820io [nSS] <\-----> ATXMEGA128A1 PortC.4 [SS]

WIZ820io [nReset]<\-----> ATXMEGA128A1 PortC.2

WIZ820io [nINT] <\-----> ATXMEGA128A1 PortC.3

Because it is a SPI based communication interface to the W5200 you need to setup the SPI interface (SPI on Port C is used in this example):

```vb
Config Spic = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk2 , Data_order = Msb , Ss = Auto 

Config Pinc.2 = Output  
```
W5200_nreset Alias Portc.2  
```vb
Set W5200_nreset  
  
Config Pinc.3 = Input  
```
W5200_nint Alias Portc.3

```vb
Reset the WIZ820io Module:

Reset W5200_nreset  
Waitms 1  
Set W5200_nreset  
Waitms 150

Config TCP Syntax Example for WIZ820io (using SPI on Port C and Port.4 as Slave Select (Chip Select)):

Config Tcpip = Noint , _  
```
Mac = 0.11.22.33.44.55 , _  
Ip = 192.168.1.254 , _  
Submask = 255.255.255.0 , _  
Gateway = 192.168.1.1 , _  
Localport = 80 , _  
Chip = W5200 , _  
Spi = Spic , _  
Cs = Portc.4

Now use PING at the command line to send a ping:

PING 192.168.1.254

Example for using W5300 Chip:

Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.253 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Chip = W5300 , Baseaddress = &HFC00

Now use PING at the command line to send a ping:

PING 192.168.1.253

See also the W5300 examples in: [Adding XRAM with External Memory Interface](adding_xram.md) regarding base address.

Example for using W5500 Chip:

```vb
'-----------------------------------------------------------------------------------------  
'name : sntp_W5500.bas RFC 2030  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : test SNTP() function  
'micro : xMega128A1  
'suited for demo : no, needs library only included in the full version  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64 ' default use 32 for the hardware stack  
$swstack = 128 'default use 10 for the SW stack  
$framesize = 64 'default use 40 for the frame space  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
'configure UART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
  
Config Spie = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk32 , Data_order = Msb , Ss = Auto  
'SPI on Port E is used  
'portx.7 - SCK  
'portx.6 - MISO  
'portx.5 - MOSI  
'portx.4 - SS  
  
Waitms 1000  
Print "Init , set IP to 192.168.1.88" ' display a message  
Config Tcpip = Noint , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.88 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Chip = W5500 , Spi = Spie , Cs = Porte.4  
Print "Init Done"  
  
  
$lib "datetime.lbx" 'this example uses date time routines  
  
  
Dim Ip As Long ' IP number of time server  
Dim Idx As Byte ' socket number  
Dim Lsntp As Long ' long SNTP time  
  
Print "SNTP demo"  
  
'assign the IP number of a SNTP server  
```
Ip = Maketcp(129.6.15.30 ) 'assign IP num NIST time.nist.gov port 37  
```vb
Print "Connecting to : " ; Ip2str(ip)  
  
  
'we will use Dutch format  
Config Date = Dmy , Separator = Minus  
  
  
'we need to get a socket first  
'note that for UDP we specify sock_dgram  
```
Idx = Getsocket(idx , Sock_dgram , 5000 , 0) ' get socket for UDP mode, specify port 5000  
```vb
Print "Socket " ; Idx  
  
'UDP is a connection less protocol which means that you can not listen, connect or can get the status  
'You can just use send and receive the same way as for TCP/IP.  
'But since there is no connection protocol, you need to specify the destination IP address and port  
'So compare to TCP/IP you send exactly the same, but with the addition of the IP and PORT  
'The SNTP uses port 37 which is fixed in the tcp asm code  
  
  
Do  
  
Waitms 5000  
  
```
Lsntp = Sntp(idx , Ip) ' get time from SNTP server  
```vb
'notice that it is not recommended to get the time every sec  
'the time server might ban your IP  
'it is better to sync once or to run your own SNTP server and update that once a day  
  
'what happens is that IP number of timer server is send a diagram too  
'it will put the time into a variable lsntp and this is converted to BASCOM date/time format  
'in case of a problem the variable is 0  
Print Date(lsntp) ; Spc(3) ; Time(lsntp)  
Loop  
  
  
  
End

```