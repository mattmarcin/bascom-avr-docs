# SETIPPROTOCOL

Action

Configures socket RAW-mode protocol

Syntax

SETIPPROTOCOL socket, value

Remarks

Socket | The socket number. (0-3)  
---|---  
Value | The IP-protocol value to set.  
  
In order to use W3100Aâs IPL_RAW Mode, the protocol value of the IP Layer to be used (e.g., 01 in case

of ICMP) needs to be set before socket initialization.

As in UDP, data transmission and reception is possible when the corresponding channel is initialized.

The PING example demonstrates the usage.

As a first step, SETIPPROTOCOL is used :

Setipprotocol Idx , 1

And second, the socket is initialized :

Idx = Getsocket(idx , 3 , 5000 , 0)

The W3100A data sheet does not provide much more details about the IPR register.

See also

[SETTCPREGS](settcpregs.md), [GETSOCKET](getsocket.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : PING_TWI.bas http://www.faqs.org/rfcs/rfc792.html

'copyright : (c) 1995-2025, MCS Electronics

'purpose : Simple PING program

'micro : Mega88

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m32def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 80 ' default use 32 for the hardware stack

$swstack = 128 ' default use 10 for the SW stack

$framesize = 80 ' default use 40 for the frame space

```
Const Debug = 1

Const Sock_stream = $01 ' Tcp

Const Sock_dgram = $02 ' Udp

Const Sock_ipl_raw = $03 ' Ip Layer Raw Sock

Const Sock_macl_raw = $04 ' Mac Layer Raw Sock

Const Sel_control = 0 ' Confirm Socket Status

Const Sel_send = 1 ' Confirm Tx Free Buffer Size

Const Sel_recv = 2 ' Confirm Rx Data Size

'socket status

Const Sock_closed = $00 ' Status Of Connection Closed

Const Sock_arp = $01 ' Status Of Arp

Const Sock_listen = $02 ' Status Of Waiting For Tcp Connection Setup

Const Sock_synsent = $03 ' Status Of Setting Up Tcp Connection

Const Sock_synsent_ack = $04 ' Status Of Setting Up Tcp Connection

Const Sock_synrecv = $05 ' Status Of Setting Up Tcp Connection

Const Sock_established = $06 ' Status Of Tcp Connection Established

Const Sock_close_wait = $07 ' Status Of Closing Tcp Connection

Const Sock_last_ack = $08 ' Status Of Closing Tcp Connection

Const Sock_fin_wait1 = $09 ' Status Of Closing Tcp Connection

Const Sock_fin_wait2 = $0a ' Status Of Closing Tcp Connection

Const Sock_closing = $0b ' Status Of Closing Tcp Connection

Const Sock_time_wait = $0c ' Status Of Closing Tcp Connection

Const Sock_reset = $0d ' Status Of Closing Tcp Connection

Const Sock_init = $0e ' Status Of Socket Initialization

Const Sock_udp = $0f ' Status Of Udp

Const Sock_raw = $10 ' Status of IP RAW

```vb
'we do the usual

Print "Init TCP" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0 , Mac = 12.128.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Twi = &H80 , Clock = 400000

Print "Init done"

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

Dim Idx As Byte , Result As Word , J As Byte , Res As Byte

Dim Ip As Long

Dim Dta(12) As Byte , Rec(12) As Byte

```
Dta(1) = 8 'type is echo

Dta(2) = 0 'code

Dta(3) = 0 ' for checksum initialization

Dta(4) = 0 ' checksum

Dta(5) = 0 ' a signature can be any number

Dta(6) = 1 ' signature

Dta(7) = 0 ' sequence number - any number

Dta(8) = 1

Dta(9) = 65

Dim W As Word At Dta + 2 Overlay 'same as dta(3) and dta(4)

W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)

```vb
#if Debug

For J = 1 To 9

Print Dta(j)

Next

#endif

```
Ip = Maketcp(192.168.0.16) 'try to check this server

Print "Socket " ; Idx ; " " ; Idx

Setipprotocol Idx , 1 'set protocol to 1

'the protocol value must be set BEFORE the socket is openend

Idx = Getsocket(idx , 3 , 5000 , 0)

Do

Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) 'write ping data '

```vb
Print Result

Waitms 100

```
Result = Socketstat(idx , Sel_recv) 'check for data

```vb
Print Result

If Result >= 11 Then

Print "Ok"

```
Res = Tcpread(idx , Rec(1) , Result) 'get data with TCPREAD !!!

```vb
#if Debug

Print "DATA RETURNED :" ; Res '

For J = 1 To Result

Print Rec(j) ; " " ;

Next

Print

#endif

Else 'there might be a problem

Print "Network not available"

End If

Waitms 1000

Loop

```