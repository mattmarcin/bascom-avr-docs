# SNTP

Action

This function retrieves the date and time from an SNTP server using the TCP/IP W3100 or W5100.

Syntax

result=SNTP(socket,IP)

Remarks

Result | A long or dword that is assigned with the date/time. If there is no data, the result will be 0.  
---|---  
socket | The socket number of the connection.  
IP | The IP number of the SNTP server you want to connect to. This may be a number like 192.168.0.2 or a LONG variable that is assigned with an IP number.  
  
SNTP means Network Time Protocol. It is an internet protocol used to synchronize clocks. SNTP uses UTC as reference time.

The SNTP function is intended to be used with a W3100A or W5100 chip. The SNTP function uses UDP routines from the library to fetch the time.

See also

NONE

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : sntp_SPI.bas RFC 2030  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : test SNTP() function  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
  
  
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
  
'toggle the variable  
Toggle Var  
  
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
  
  
End

```