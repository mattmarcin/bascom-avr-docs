# CLOSE

Action

Closes an opened device.

Syntax

OPEN "device" for MODE As #channel

CLOSE #channel

Remarks

Device | The default device is COM1 and you don't need to open a channel to use INPUT/OUTPUT on this device. With the implementation of the software UART, the compiler must know to which pin/device you will send/receive the data. So that is why the OPEN statement must be used. It tells the compiler about the pin you use for the serial input or output and the baud rate you want to use. COMB.0:9600,8,N,2 will use PORT B.0 at 9600 baud with 2 stop bits. The format for COM1 is : COM1: Some chips have 2 UARTS. You can use COM2: to open the second HW UART. Other chips might have 4 or 8 UARTS. The format for the software UART is: COMpin:speed,8,N,stop bits[,INVERTED] Where pin is the name of the PORT-pin. Speed must be specified and stop bits can be 1 or 2. An optional parameter ,INVERTED can be specified to use inverted RS-232. Open "COMD.1:9600,8,N,1,INVERTED" For Output As #1 , will use pin PORTD.1 for output with 9600 baud, 1 stop bit and with inverted RS-232.  
---|---  
MODE | You can use BINARY or RANDOM for COM1 and COM2, but for the software UART pins, you must specify INPUT or OUTPUT.  
Channel | The number of the channel to open. Must be a positive constant >0.  
  
The statements that support the device are PRINT , INPUT and INPUTHEX , INKEY, WAITKEY.

Using CLOSE on a serial device is optional. Only a file as used with AVR-DOS requires a CLOSE.

The best place for the CLOSE statement is at the end of your program.

The INPUT statement in combination with the software UART, will not echo characters back because there is no default associated pin for this.

![notice](notice.jpg) For the AVR-DOS file system, you may place the CLOSE at any place in your program. This because the file system supports real file handles.

For the UART, SPI or other devices, you do not need to close the device. Only AVR-DOS needs a CLOSE so the file will be flushed. 

See also

[OPEN](open.md) , [PRINT](print.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : open.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates software UART

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 10000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

'Optional you can fine tune the calculated bit delay

'Why would you want to do that?

'Because chips that have an internal oscillator may not

'run at the speed specified. This depends on the voltage, temp etc.

'You can either change $CRYSTAL or you can use

'BAUD #1,9610

'In this example file we use the DT006 from www.simmstick.com

'This allows easy testing with the existing serial port

'The MAX232 is fitted for this example.

'Because we use the hardware UART pins we MAY NOT use the hardware UART

'The hardware UART is used when you use PRINT, INPUT or other related statements

'We will use the software UART.

Waitms 100

'open channel for output

```
Open "comd.1:19200,8,n,1" For Output As #1

```vb
Print #1 , "serial output"

'Now open a pin for input

```
Open "comd.0:19200,8,n,1" For Input As #2

```vb
'since there is no relation between the input and output pin

'there is NO ECHO while keys are typed

Print #1 , "Number"

'get a number

Input #2 , B

'print the number

Print #1 , B

'now loop until ESC is pressed

'With INKEY() we can check if there is data available

'To use it with the software UART you must provide the channel

Do

'store in byte

```
B = Inkey(#2)

```vb
'when the value > 0 we got something

If B > 0 Then

Print #1 , Chr(b) 'print the character

End If

Loop Until B = 27

```
Close #2

Close #1

```vb
'OPTIONAL you may use the HARDWARE UART

'The software UART will not work on the hardware UART pins

'so you must choose other pins

'use normal hardware UART for printing

'Print B

'When you dont want to use a level inverter such as the MAX-232

'You can specify ,INVERTED :

'Open "comd.0:300,8,n,1,inverted" For Input As #2

'Now the logic is inverted and there is no need for a level converter

'But the distance of the wires must be shorter with this

End

```