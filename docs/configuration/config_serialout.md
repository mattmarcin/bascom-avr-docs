# CONFIG SERIALOUT

Action

Configures the hardware UART to use a buffer for output

Syntax

CONFIG SERIALOUT | SERIALOUT1 | SERIALOUT2 | SERIALOUT3 |SERIALOUTx = BUFFERED , SIZE = size

Remarks

SerialOut | Some chips have multiple HW UARTS. Use the following parameter values: | •| SERIALOUT or SERIALOUT0 : first UART/UART0  
---|---  
  
•| SERIALOUT1 : second UART/UART1  
---|---  
  
•| SERIALOUT2 : third UART/UART2  
---|---  
  
•| SERIALOUT3 : fourth UART/UART3  
---|---  
  
•| SERIALOUT4 : fifth UART/UART4  
---|---  
  
•| SERIALOUT5 : sixth UART/UART5  
---|---  
  
•| SERIALOUT6 : seventh UART/UART6  
---|---  
  
•| SERIALOUT7 : eight UART/UART7  
---|---  
  
size | A numeric constant that specifies how large the output buffer should be. The space is taken from the SRAM. The maximum value is 255.  
  
The following internal variables will be used when you use CONFIG SERIALOUT

_RS_HEAD_PTRW0 , byte that stores the head of the buffer

_RS_TAIL_PTRW0 , byte that stores the tail of the buffer

_RS232OUTBUF0, array of bytes for the ring buffer that stores the printed data.

_RS_BUFCOUNTW0, a byte that holds the number of bytes in the buffer.

For the other UARTS, the variables are named similar. But they do have a different number.

A 1 for the second UART, a 3 for the third UART and a 4 for the fourth UART. Yes, the '2' is skipped.

Serial buffered output can be used when you use a low baud rate. It would take relatively much time to print all data without a buffer. When you use a buffer, the data is printed on the background when the micro UART byte buffer is empty. It will get a byte from the buffer then and transmit it.

As with any buffer you have, you must make sure that it is emptied at one moment in time.

You can not keep filling it as it will become full. When you do not empty it, you will have the same situation as without a buffer !!! When the roof is leaking and you put a bucket on the floor and in the morning you empty it, it will work. But when you will go away for a day, the bucket will overflow and the result is that the floor is still wet.

Another important consideration is data loss. When you print a long string of 100 bytes, and there is only room in the buffer for 80 bytes, there is still a wait evolved since after 80 bytes, the code will wait for the buffer to become empty. When the buffer is empty it will continue to print the data. The advantage is that you do not loose any data, the disadvantage is that it blocks program execution just like a normal un-buffered PRINT would do.

Since buffered serial output uses interrupts, you must enable the global interrupts in your code with : ENABLE INTERRUPTS.

For the XMEGA, if you set the priority with CONFIG PRIORITY, you must enable the MED priority.

ASM

Routines called from MCS.LIB :

_CHECKSENDCHAR. This is an ISR that gets called when ever the transmission buffer is empty.

Since UDRE interrupt is used , you can not use this interrupt anymore. Unless you modify the _CheckSendChar routine of course.

When you use the PRINT statement to send data to the serial port, the UDRE interrupt will be enabled. And so the _CheckSendChar routine will send the data from the buffer.

See also

[CONFIG SERIALIN](config_serialin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rs232bufferout.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates how to use a serial output buffer

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 9600 ' use baud rate

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'setup to use a serial output buffer

'and reserve 20 bytes for the buffer

Config Serialout = Buffered , Size = 20

'It is important since UDRE interrupt is used that you enable the interrupts

Enable Interrupts

Print "Hello world"

Print "test1"

Do

Wait 1

'notice that using the UDRE interrupt will slown down execution of waiting loops like waitms

Print "test"

Loop

End

```