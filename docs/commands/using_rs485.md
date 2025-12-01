# USING RS485

RS485

RS485 is used for serial communication and well suited for transmission over large distances.

Similar to RS232 we need a level shifter.

![rs485-example](rs485-example.png)The sample above uses a MEGA161 or MEGA162 which has 2 UARTS. This way you can have both a RS232 and RS485 interface.

The RS232 is used for debugging.

In order to test you need 2 or more similar circuits. One circuit would be the master.

The other(s) would be a slave.

The same hardware is used to test the MODBUS protocol. The bus need to be terminated at both ends with a resistor. 100 ohm is a typical used value.

The GND of both circuits may not be connected ! Only connect point A and B from both circuits. For industrial usage it is best to use an optical isolated level shifter.

Simple MASTER sample

```vb
$regfile = "m162def.dat" ' specify the used micro

$crystal = 8000000

$baud = 19200 ' use baud rate

$hwstack = 42 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "modbus.lbx"

Config Print1 = Portb.1 , Mode = Set ' use portb.1 for the direction

```
Rs485dir Alias Portb.1

Config Rs485dir = Output

Rs485dir = 0 ' go to receive mode

Portc.0 = 1 ' a switch is connected to pinc.0 so activate pull up resistor

```vb
' TX RX

' COM0 PD.1 PD.0 monitor

' COM1 PB.3 PB.2 rs485

' PB.1 data direction rs485

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = 9600 , Synchrone = 0 , Parity = Even , Stopbits = 1 , Databits = 8 , Clockpol = 0 ' MUST MATCH THE SLAVE

'use OPEN/CLOSE for using the second UART

```
Open "COM2:" For Binary As #1

```vb
'dimension some variables

Dim B As Byte

Dim W As Word

Dim L As Long

```
W = &H4567 ' set some values

L = &H12345678

```vb
Print "RS-485 MODBUS master"

Do

If Pinc.0 = 0 Then ' test button

Waitms 500 ' delay since we want to send just 1 frame

Print "send request to slave/server" ' to debug terminal

' Print #1 , Makemodbus(2 , 3 , 8 , 2); 'slave 2, function 3, start address 8, 2 bytes

' Print #1 , Makemodbus(2 , 6 , 8 , W); 'slave 2, function 6, address 8 , value of w

Print #1 , Makemodbus(b , 16 , 8 , L); 'send a long

End If

If Ischarwaiting(#1) <> 0 Then 'did we got something back?

```
B = Waitkey(#1) ' yes so get it

```vb
Print Hex(b) ; ","; ' print it

End If

Loop

```
A slave would simply listen to data, and once enough data received, send it back.