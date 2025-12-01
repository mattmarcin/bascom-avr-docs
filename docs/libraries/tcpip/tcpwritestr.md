# TCPWRITESTR

Action

Sends a string to an open socket connection.

Syntax

Result = TCPWRITESTR( socket , var , param)

Remarks

Result | A word variable that will be assigned with the number of bytes actually written to the socket. When the free transmission buffer is large enough to accept all the data, the result will be the same as BYTES. When there is not enough space, the number of written bytes will be returned. When there is no space, 0 will be returned.  
---|---  
Socket | The socket number you want to send data to (0-3). 0-7 for W5200/W5300.  
Var | The name of a string variable.  
Param | A parameter that might be 0 to send only the string or 255, to send the string with an additional CR + LF This option was added because many protocols expect CR + LF at the end of the string.  
  
The TCPwriteStr function is a special variant of the TCPwrite function.

It will use TCPWrite to send the data.

See also

[CONFIG TCPIP](config_tcpip.md), [GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md), [SOCKETDISCONNECT](socketdisconnect.md), [URL2IP](url2ip.md)

Example

```vb
'-------------------------------------------------------------------------------

' SMTP.BAS

' (c) 1995-2025 MCS Electronics

' sample that show how to send an email with SMTP protocol

'-------------------------------------------------------------------------------

$regfile = "m161def.dat" ' used processor

$crystal = 4000000 ' used crystal

$baud = 19200 ' baud rate

```
Const Debug = -1 ' for sending feeback to the terminal

```vb
#if Debug

Print "Start of SMTP demo"

#endif

Enable Interrupts ' enable interrupts

'specify MAC, IP, submask and gateway

'local port value will be used when you do not specify a port value while creating a connection

'TX and RX are setup to use 4 connections each with a 2KB buffer

Config Tcpip = Int0 , Mac = 00.44.12.34.56.78 , Ip = 192.168.0.8 , Submask = 255.255.255.0 , Gateway = 192.168.0.1 , Localport = 1000 , Tx = $55 , Rx = $55

'dim the used variables

Dim S As String * 50 , I As Byte , J As Byte , Tempw As Word

#if Debug

Print "setup of W3100A complete"

#endif

'First we need a socket

```
I = Getsocket(0 , Sock_stream , 5000 , 0)

```vb
' ^ socket numer ^ port

#if Debug

Print "Socket : " ; I

'the socket must return the asked socket number. It returns 255 if there was an error

#endif

If I = 0 Then ' all ok

'connect to smtp server

```
J = Socketconnect(i , 194.09.0. , 25) ' smtp server and SMTP port 25

```vb
' ^socket

' ^ ip address of the smtp server

' ^ port 25 for smtp

' DO NOT FORGET to ENTER a valid IP number of your ISP smtp server

#if Debug

Print "Connection : " ; J

Print S_status(1)

#endif

If J = 0 Then ' all ok

#if Debug

Print "Connected"

#endif

Do

```
Tempw = Socketstat(i , 0) ' get status

```vb
Select Case Tempw

Case Sock_established ' connection established

```
Tempw = Tcpread(i , S) ' read line

```vb
#if Debug

Print S ' show info from smtp server

#endif

If Left(s , 3) = "220" Then ' ok

```
Tempw = Tcpwrite(i , "HELO username{013}{010}" ) ' send username

```vb
' ^^^ fill in username there

#if Debug

Print Tempw ; " bytes written" ' number of bytes actual send

#endif

```
Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S ' show response

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "MAIL FROM:<tcpip@test.com>{013}{010}") ' send from address

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "RCPT TO:<tcpip@test.com>{013}{010}") ' send TO address

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "DATA{013}{010}") ' speicfy that we are going to send data

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "354" Then ' ok

```
Tempw = Tcpwrite(i , "From: tcpip@test.com{013}{010}")

Tempw = Tcpwrite(i , "To: tcpip@test.com{013}{010}")

Tempw = Tcpwrite(i , "Subject: BASCOM SMTP test{013}{010}")

Tempw = Tcpwrite(i , "X-Mailer: BASCOM SMTP{013}{010}")

Tempw = Tcpwrite(i , "{013}{010}")

Tempw = Tcpwrite(i , "This is a test email from BASCOM SMTP{013}{010}")

Tempw = Tcpwrite(i , "Add more lines as needed{013}{010}")

Tempw = Tcpwrite(i , ".{013}{010}") ' end with a single dot

Tempw = Tcpread(i , S) ' get response

```vb
#if Debug

Print S

#endif

If Left(s , 3) = "250" Then ' ok

```
Tempw = Tcpwrite(i , "QUIT{013}{010}") ' quit connection

Tempw = Tcpread(i , S)

```vb
#if Debug

Print S

#endif

End If

End If

End If

End If

End If

End If

Case Sock_close_wait

Print "CLOSE_WAIT"

```
Closesocket I ' close the connection

```vb
Case Sock_closed

Print "Socket CLOSED" ' socket is closed

End

End Select

Loop

End If

End If

End 'end program

```