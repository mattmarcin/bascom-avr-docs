# TCPCHECKSUM

Action

Return a TCP/IP checksum, also called Internet Checksum, or IP Checksum.

Syntax

res= TCPCHECKSUM(buffer , bytes [,w1] [,w2])

Remarks

Res | A word variable that is assigned with the TCP/IP checksum of the buffer  
---|---  
Buffer | A variable or array to get the checksum of.  
Bytes | The number of bytes that must be examined.  
w1,w2 | Optional words that will be included in the checksum.  
  
Checksum's are used a lot in communication protocols. A checksum is a way to verify that received data is the same as it was sent. In the many Internet Protocols (TCP, UDP, IP, ICMP â¦) a special Internet checksum is used. Normally the data to calculate the checksum on is stored in an array of bytes, but in some cases like TCP, and UDP, a pseudo header is added. The optional words (w1, w2) can be used for these cases. Most often w1 and w2 will be used for the Protocol number, and the UDP or TCP packet length.

This checksum is calculated by grouping the bytes in the array into 2-byte words. If the number of Bytes is an odd number, then an extra byte of zero is used to make the last 2-byte word. All of the words are added together, keeping the total in a 4-byte Long variable. If the optional words w1, w2, are included, they are also added to the total. Next, the 4-byte Long total is split into two, 2-byte words, and these words are added together to make a new 2-byte Word total. Finally the total is inverted. This is the value returned as Res.

This function using w1, w2, are very useful when working directly with Ethernet chips like the RTL8019AS or with protocols not directly supported by the WIZnet chips.

See the samples directory for more examples of use (IP_Checksum.bas). 

You can use it for the PING sample below.

See also

[CRC8](crc8.md) , [CRC16](crc16.md), [CRC32](crc32.md) , [CHECKSUM](checksum.md)

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

```vb
'we do the usual

Print "Init TCP" ' display a message

Enable Interrupts ' before we use config tcpip , we need to enable the interrupts

Config Tcpip = Int0, Mac = 12.128.12.34.56.78, Ip = 192.168.0.8, Submask = 255.255.255.0, Gateway = 192.168.0.1, Localport = 1000, Tx = $55, Rx = $55, Twi = &H80, Clock = 400000

Print "Init done"

Dim Peersize As Integer , Peeraddress As Long , Peerport As Word

Dim Idx As Byte , Result As Word , J As Byte , Res As Byte

Dim Ip As Long

Dim Dta(12) As Byte , Rec(12) As Byte

```
Dta(1) = 8 ' type is echo

Dta(2) = 0 ' code

Dta(3) = 0 ' for checksum initialization

Dta(4) = 0 ' checksum

Dta(5) = 0 ' a signature can be any number

Dta(6) = 1 ' signature

Dta(7) = 0 ' sequence number - any number

Dta(8) = 1

Dta(9) = 65

Dim W As Word At Dta + 2 Overlay ' same as dta(3) and dta(4)

W = Tcpchecksum(dta(1) , 9) ' calculate checksum and store in dta(3) and dta(4)

```vb
#if Debug

For J = 1 To 9

Print Dta(j)

Next

#endif

```
Ip = Maketcp(192.168.0.16) ' try to check this server

Print "Socket " ; Idx ; " " ; Idx

Setipprotocol Idx , 1 ' set protocol to 1

'the protocol value must be set BEFORE the socket is openend

Idx = Getsocket(idx , 3 , 5000 , 0)

Do

Result = Udpwrite(ip , 7 , Idx , Dta(1) , 9) ' write ping data 

```vb
Print Result

Waitms 100

```
Result = Socketstat(idx , Sel_recv) ' check for data

```vb
Print Result

If Result >= 11 Then

Print "Ok"

```
Res = Tcpread(idx , Rec(1) , Result) ' get data with TCPREAD !!!

```vb
#if Debug

Print "DATA RETURNED :" ; Res 

For J = 1 To Result

Print Rec(j) ; " " ;

Next

Print

#endif

Else ' there might be a problem

Print "Network not available"

End If

Waitms 1000

Loop

```