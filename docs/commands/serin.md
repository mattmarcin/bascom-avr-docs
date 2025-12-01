# SERIN

Action

Reads serial data from a dynamic software UART.

Syntax

SERIN var , bts , port , pin, baud , parity , dbits , sbits

Remarks

While the OPEN and CLOSE statements can be used for software UARTS, they do not permit to use the same pin for input and output. The settings used when opened the communication channel can also not be changed at run time.

The SERIN and SEROUT statements are dynamic software UART routines to perform input and output. You can use them on the same pin for example send some data with SEROUT and get back an answer using SERIN.

Since the SERIN and SEROUT routines can use any pin and can use different parameter values, the code size of these routines is larger.

Parameter | Description  
---|---  
Var | A variable that will be assigned with the received data.  
Bts | The number of bytes to receive. String variables will wait for a return (ASCII 13). There is no check if the variable you assign is big enough to hold the result.  
Port | The name of the port to use. For example: portA.  
Pin | The pin number you want to use of the port. This must be in the range from 0-7.  
Baud | The baud rate you want to use. For example 19200.  
Parity | A number that codes the parity. 0= NONE, 1 = EVEN, 2 = ODD  
Dbits | The number of data bits. Use 7 or 8.  
Sbits | The number of stop bits. 1 to 2.  
  
The use of SERIN will create an internal variable named ___SER_BAUD. This is a LONG variable. It is important that you specify the correct crystal value with $CRYSTAL so the correct calculation can be made for the specified baud rate.

Note that ___SER_BAUD will not hold the passed baud rate but will hold the bit delay used internal.

Since the SW UART is dynamic you can change all the parameters at run time. For example you can store the baud rate in a variable and pass this variable to the SERIN routine.

Your code could change the baud rate under user control this way.

It is important to realize that software timing is used for the bit timing. Any interrupt that occurs during SERIN or SEROUT will delay the transmission. Disable interrupts while you use SERIN or SEROUT.

ASM

The routine called is named _serin and is stored in mcs.lib

```vb
For Xmega it is located in Xmega.lib and Xtiny in Xtiny.lib

For the baud rate calculation, _calc_baud is called.

```
See also

[SEROUT](serout.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : serin_out.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of DYNAMIC software UART

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'tip : Also look at OPEN and CLOSE

'some variables we will use

Dim S As String * 10

Dim Mybaud As Long

'when you pass the baud rate with a variable, make sure you dimesion it as a LONG

```
Mybaud = 19200

```vb
Do

'first get some data

```
Serin S , 0 , PORTD , 0 , Mybaud , 0 , 8 , 1

'now send it

Serout S , 0 , PORTD , 1 , Mybaud , 0 , 8 , 1

```vb
' ^ 1 stop bit

' ^---- 8 data bits

' ^------ even parity (0=N, 1 = E, 2=O)

' ^-------------- baud rate

' ^-------------------- pin number

' ^----------------------- port so PORTA.0 and PORTA.1 are used

' ^--------------------------- for strings pass 0

' ^-------------------------------- variable

Wait 1

Loop

End

'because the baud rate is passed with a variable in this example, you could change it under user control

'for example check some DIP switches and change the variable mybaud

```