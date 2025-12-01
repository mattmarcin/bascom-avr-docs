# MAKEMODBUS

Action

Creates a MODBUS master/client frame.

Syntax

PRINT [#x,] MAKEMODBUS(slave, function, address, varbts )

Remarks

slave | The slave to address. This is a variable or constant with a valid MODBUS slave to address.  
---|---  
function | The function number. This must be a constant. At the moment the following functions are supported : | •| 01 : read coils  
---|---  
  
•| 02 : read discrete inputs  
---|---  
  
•| 03 : read register(s)  
---|---  
  
•| 04 : read input registers  
---|---  
  
•| 06 : write single register  
---|---  
  
•| 16 : write multiple registers  
---|---  
  
address | The starting address of the register  
varbts | For a function that sends data like function 6 and 16, this must be a variable. For function 06 which can only write a single register, this can be a byte or integer or word. For function 16 it may be a long, single or double. For function 6 and 16 the address of the variable is passed to the function. For function 1,2,3 and 4 you may also specify the number of bytes to receive. Or you can use a variable. When you specify a byte, a word will be used anyway since a word (2 bytes) is the minimum in MODBUS protocol. But when sending data, you can send content of a byte. For the MSB the value 0 will be sent in that case. With : CONFIG MODBUS = VAR  you can change the varbts mode. In VAR mode, you have to pass the number of bytes in the variable.   
  
The MAKEMODBUS function need to be used in combination with the PRINT statement. It can only be used with the hardware UART(1-4).

The MODBUS protocol is an industry standard. The protocol can be used with RS-232, RS-485 or TCP/IP or CAN. 

The current BASCOM implementation only works with RS-232 or RS485. 

In MODBUS we use client/master and server/slave. You may see it as a web server and a web browser. The web server is the client/slave that reacts on the master/web browser.

A slave will only respond when it is addressed. All other slaves just keep listening till they are addressed.

An addressed slave will process the data and send a response.

In MODBUS the data is sent with MSB first and LSB last. The special CRC16 checksum is sent LSB first and MSB last.

When multiple registers are sent with function 16, the data is split up into words, and for each word, the MSB-LSB order is used.

For example a LONG is 4 bytes. LSB, NSB1, NSB2, MSB. It would be sent as : NSB1, LSB, MSB, NSB2.

In order to use the MODBUS functionality, you need to include the MODBUS.LBX with the $LIB directive.

See also

[PRINT](print.md) , [CONFIG MODBUS](config_modbus.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rs485-modbus-master.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo file for MAKEMODBUS

'micro : Mega162

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m162def.dat" ' specify the used micro

$crystal = 8000000

$baud = 19200 ' use baud rate

$hwstack = 42 ' default use 42 for the hardware stack

$swstack = 40 ' default use 40 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "modbus.lbx" ' specify the additional library

Config Print1 = Portb.1 , Mode = Set ' specify RS-485 and direction pin

```
Rs485dir Alias Portb.1 'make an alias

Config Rs485dir = Output 'set direction register to output

Rs485dir = 0 ' set the pin to 0 for listening

Portc.0 = 1 ' a pin is used with a switch

```vb
'The circuit from the help is used. See Using MAX485

' TX RX

' COM0 PD.1 PD.0 rs232 used for debugging

' COM1 PB.3 PB.2 rs485 used for MODBUS halve duplex

' PB.1 data direction rs485

'configure the first UART for RS232

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'configure the second UAR for RS485/MODBUS. Make sure all slaves/servers use the same settings

Config Com2 = 9600 , Synchrone = 0 , Parity = Even , Stopbits = 1 , Databits = 8 , Clockpol = 0

'use OPEN/CLOSE for using the second UART

```
Open "COM2:" For Binary As #1

```vb
'dimension some variables

Dim B As Byte

Dim W As Word

Dim L As Long

```
W = &H4567 'assign a value

L = &H12345678 'assign a value

```vb
Print "RS-485 MODBUS master"

Do

If Pinc.0 = 0 Then ' test switch

Waitms 500 ' delay

Print "send request to slave/server"

' Send one of the following three messages

' Print #1 , Makemodbus(2 , 3 , 8 , 2); ' slave 2, function 3, start address 8, 2 bytes

' Print #1 , Makemodbus(2 , 6 , 8 , W); ' slave 2, function 6, address 8 , value of w

Print #1 , Makemodbus(2 , 16 , 8 , L); ' slave 2, function 16, address 8 , send a long

End If

If Ischarwaiting(#1) <> 0 Then 'was something returned?

```
B = Waitkey(#1) 'then get it

```vb
Print Hex(b) ; ","; 'print the info

End If

Loop

End

```