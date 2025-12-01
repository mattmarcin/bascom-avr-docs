# CONFIG SERIALIN

Action

Configures the hardware UART to use a buffer for input

Syntax

CONFIG SERIALIN | SERIALIN1 | SERIALIN2 | SERIALIN3 |SERIALx = BUFFERED , SIZE | BIGSIZE = size [, BYTEMATCH=ALL|BYTE|NONE] [,CTS=pin, RTS=pin , Threshold_full=num , Threshold_empty=num ] 

Remarks

SerialIn | Some chips have multiple HW UARTS. Use the following parameter values: | •| SERIALIN or SERIALIN0 : first UART/UART0  
---|---  
  
•| SERIALIN1 : second UART/UART1  
---|---  
  
•| SERIALIN2 : third UART/UART2  
---|---  
  
•| SERIALIN3 : fourth UART/UART3  
---|---  
  
•| SERIALIN4 : fifth UART/UART4  
---|---  
  
•| SERIALIN5 : sixth UART/UART5  
---|---  
  
•| SERIALIN6 : seventh UART/UART6  
---|---  
  
•| SERIALIN7 : eight UART/UART7  
---|---  
  
Size | A numeric constant that specifies how large the input buffer should be. The space is taken from the SRAM. The maximum is 255.  
BigSize | Instead of using Size you can use BigSize for COM1. It allows to create a bigger buffer than using Size. While Size works with a byte buffer, BigSize works with a word size buffer. It requires more code and does not handle CTS/RTS. For some applications it can be useful to have a big buffer. This is an overloaded version of the code from mcs.lib. You need to include bigbuf.lib using the $LIB directive in your code.   
Bytematch | The ASCII value of the byte that will result in calling a user label. When you specify ALL, the user label will be called for every byte that is received. You must include the label yourself in your code and end it with a return. The following label names must be used when you check for a specific byte value: | •| Serial0CharMatch (for SERIALIN or the first UART/UART0)  
---|---  
  
•| Serial1CharMatch (for SERIALIN1 or the second UART/UART1)  
---|---  
  
•| Serial2CharMatch (for SERIALIN2 or the third UART/UART2)  
---|---  
  
•| Serial3CharMatch (for SERIALIN3 or the fourth UART/UART3)  
---|---  
  
The following label names must be used when you check for any value:

•| Serial0ByteReceived (for SERIALIN or the first UART/UART0)  
---|---  
  
•| Serial1ByteReceived (for SERIALIN1 or the second UART/UART1)  
---|---  
  
•| Serial2ByteReceived (for SERIALIN2 or the third UART/UART2)  
---|---  
  
•| Serial3ByteReceived (for SERIALIN3 or the fourth UART/UART3)  
---|---  
  
When you specify NONE, it is the same as not specifying this optional parameter.  
  
CTS | The pin used for the CTS.(Clear to send). For example PIND.6. This pin will be used in the INPUT mode since it will be connected to the other parties RTS pin.  
RTS | The pin used for RTS. (Ready to send). For example PIND.7 This pin will be used in OUTPUT mode. It is set to 0 to indicate that the other party may send data and it will become 1 to signal to the other party that the buffer is almost full.   
Threshold_full | The number of bytes that will cause RTS to be set to '1'. This is an indication to the sender, that the buffer is full. If your buffer is 100 bytes, you could set it to 80 so after receiving 80 bytes, the RTS pin will change and there are still 20 bytes in the buffer to compensate timing at high baud rates.  
Threshold_empty | The number of free bytes that must be in the buffer before RTS is enabled ( made '0' ) again. If the buffer is 100 bytes, you could set it to 10.  
  
![notice](notice.jpg)The following description is for the normal buffer which uses bytes.

When using the BIGSIZE option instead of SIZE these variables will be of the word type. The mechanism is exactly the same.

The following internal variables will be generated for UART0:

_RS_HEAD_PTR0 , a byte counter that stores the head of the buffer

_RS_TAIL_PTR0 , a byte counter that stores the tail of the buffer.

_RS232INBUF0 , an array of bytes that serves as a ring buffer for the received characters.

_RS_BUFCOUNTR0, a byte that holds the number of bytes that are in the buffer.

For the other UARTS, the variables are named similar. But they do have a different number.

A 1 for the second UART, a 3 for the third UART and a 4 for the fourth UART. Yes, the '2' is skipped.

While you can read and write the internal variables, we advise not to write to them. The variables are updated inside interrupts routines, and just when you write a value to them, an ISR can overwrite the value.

The optional BYTEMATCH can be used to monitor the incoming data bytes and call a label when the specified data is found. This label is a fixed label as mentioned in the table above. The label is called after the data is stored in the buffer. 

This way you can determine the start of a serial stream when you work with a unique header byte. Or you can determine when the data is received into the buffer when you work with a unique trailer byte. 

While bytematch allows you to trap the incoming data bytes, take care that you do not delay the program execution too much. After all the serial input interrupt is used in order not to miss incoming data. When you add delays or code that will delay execution too much you might loose incoming data.

![important](important.jpg)When using the BYTEMATCH option, you must preserve the registers you alter. If you do not know which one, use [PUSHALL](pushall.md) and [POPALL](popall.md).

![important](important.jpg)When using BYTEMATCH and CTS/RTS, do not print data in the bytematch routine to the same UART. This can disturb the communication when the output buffer becomes full.

![notice](notice.jpg)To clear the buffer, use [CLEAR](clear.md) SERIALIN. Do not read and write the internal buffer variables yourself.

CTS-RTS is hardware flow control. Both the sender and receiver need to use CTS-RTS when CTS-RTS is used. When one of the parties does not use CTS-RTS, no communication will be possible.

CTS-RTS requires two additional wires. The receiver must check the CTS pin to see if it may send. The CTS pin is an input pin as the receiver looks at the level that the sender can change.

The receiver can set the RTS pin to indicate to the sender that it can accept data.

In the start condition, RTS is made '0' by the receiver. The sender will then check this logic level with it's CTS pin, and will start to send data. The receiver will store the data into the buffer and when the buffer is almost full, or better said, when the Threshold_full is the same as the number of bytes in the receive buffer, the receiver will make RTS '1' to signal to the sender, that the buffer is full. The sender will stop sending data. And will continue when the RTS is made '0' again.

The receiver can send data to the sender and it will check the CTS pin to see if it may send data.

In order to work with CTS-RTS, you need both a serial input buffer, and a serial output buffer. So use both CONFIG SERIALIN and CONFIG SERIALOUT to specify the buffers.

The CTS-RTS can only be configured with the CONFIG SERIALIN statement.

The thresholds are needed for high baud rates where it will take some time to react on a CTS-RTS.

You need to experiment with the thresholds but good start values are 80% full, and 20% empty.

![notice](notice.jpg)You need to use a pin that is bit addressable. For most chips this is a pin from port A, B, C or D.

![notice](notice.jpg)Some serial devices use the RTS pin as an output pin, while other devices use RTS pin as an input pin to indicate that it need to be connected TO an RTS pin. You always need to have a good look at the data sheet and see in which mode the RTS/CTS pins are used.

In BASCOM RTS is an output pin and CTS is an input pin. 

Additional Infos for XMEGA Devices:

Since buffered serial input and output uses interrupts, you must enable the global interrupts in your code with : ENABLE INTERRUPTS.

```vb
For the XMEGA, if you set the priority with CONFIG PRIORITY, you must enable the MED priority.

If you only use ENABLE INTERRUPTS, the MED priority is enabled automatically. This means you only need to specify MED when you manually configure the priority.

```
Buffer full

So what happens when the buffer is full and a new character arrives and cts/rts are not used?

The byte is still read out and the ERR variable is set. But the data is NOT stored in the buffer. It is lost just as when you would have not used any buffering.

When BYTEMATCH is used, this will still be used/called. 

ASM

Routines called from MCS.LIB :

_GotChar. This is an ISR that gets called when ever a character is received.

When there is no room for the data it will not be stored.

So the buffer must be emptied periodic by reading from the serial port using the normal statements like INKEY() and INPUT.

Since URXC interrupt is used by _GotChar, you can not use this interrupt anymore. Unless you modify the _gotchar routine of course.

See also

[CONFIG SERIALOUT](config_serialout.md) , [ISCHARWAITING](ischarwaiting.md) , [CLEAR](clear.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rs232buffer.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : example shows the difference between normal and buffered

' serial INPUT

'micro : Mega161

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m161def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 9600 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'first compile and run this program with the line below remarked

Config Serialin = Buffered , Size = 20

Dim Na As String * 10

'the enabling of interrupts is not needed for the normal serial mode

'So the line below must be remarked to for the first test

Enable Interrupts

Print "Start"

Do

'get a char from the UART

If Ischarwaiting() = 1 Then 'was there a char?

Input Na 

Print Na  'print it

End If

Wait 1 'wait 1 second

Loop

'You will see that when you slowly enter characters in the terminal emulator

'they will be received/displayed.

'When you enter them fast you will see that you loose some chars

'NOW remove the remarks from line 11 and 18

'and compile and program and run again

'This time the chars are received by an interrupt routine and are

'stored in a buffer. This way you will not loose characters providing that

'you empty the buffer

'So when you fast type abcdefg, they will be printed after each other with the

'1 second delay

'Using the CONFIG SERIAL=BUFFERED, SIZE = 10 for example will

'use some SRAM memory

'The following internal variables will be generated :

'_Rs_head_ptr0 BYTE , a pointer to the location of the start of the buffer

'_Rs_tail_ptr0 BYTE , a pointer to the location of tail of the buffer

'_RS232INBUF0 BYTE ARRAY , the actual buffer with the size of SIZE

```
Example2

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M2560 support

'micro : Mega2560

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m2560def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'$timeout = 1000000

'The M128 has an extended UART.

'when CO'NFIG COMx is not used, the default N,8,1 will be used

Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com3 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com4 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Enable Interrupts

Config Serialin = Buffered , Size = 20

Config Serialin1 = Buffered , Size = 20 , Bytematch = 65

Config Serialin2 = Buffered , Size = 20 , Bytematch = 66

Config Serialin3 = Buffered , Size = 20 , Bytematch = All

'Open all UARTS

```
Open "COM2:" For Binary As #2

Open "COM3:" For Binary As #3

Open "COM4:" For Binary As #4

```vb
Print "Hello" 'first uart

Dim B1 As Byte , B2 As Byte , B3 As Byte , B4 As Byte

Dim Tel As Word , Nm As String * 16

'unremark to test second UART

'Input #2 , "Name ?" , Nm

'Print #2 , "Hello " ; Nm

Do

```
Incr Tel

```vb
Print Tel ; " test serial port 1"

Print #2 , Tel ; " test serial port 2"

Print #3 , Tel ; " test serial port 3"

Print #4 , Tel ; " test serial port 4"

```
B1 = Inkey() 'first uart

B2 = Inkey(#2)

B3 = Inkey(#3)

B4 = Inkey(#4)

```vb
If B1 <> 0 Then

Print B1 ; " from port 1"

End If

If B2 <> 0 Then

Print #2 , B2 ; " from port 2"

End If

If B3 <> 0 Then

Print #3 , B3 ; " from port 3"

End If

If B4 <> 0 Then

Print #4 , B4 ; " from port 4"

End If

Waitms 500

Loop

'Label called when UART2 received an A

```
Serial1charmatch:

```vb
Print #2 , "we got an A"

Return

'Label called when UART2 received a B

```
Serial2charmatch:

```vb
Print #3 , "we got a B"

Return

'Label called when UART3 receives a char

```
Serial3bytereceived:

```vb
Print #4 , "we got a char"

Return

End

```
Close #2

Close #3

Close #4

$eeprom

Data 1 , 2