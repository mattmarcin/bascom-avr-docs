# PRINT

Action

Send output to the UART.

Writes a string to a file.

Writes data to a device.

Syntax

PRINT [#channel , ] var ; " constant"

Remarks

Var | The variable or constant to print.  
---|---  
  
You can use a semicolon (;) to print multiple variables or constants after each other.

When you end a line with a semicolon, no linefeed and carriage return will be added.

The PRINT routine can be used when you have a RS-232 interface on your processor.

The RS-232 interface can be connected to a serial communication port of your computer.

This way you can use a terminal emulator as an output device.

You can also use the build in terminal emulator.

When using RS-485 you can use CONFIG PRINT to set up a pin for the direction.

When printing arrays, you can only print one element at the time. When you need to print the content of a complete array, you need to use [PRINTBIN](printbin.md).

PRINT will automatic convert numeric variables into the string representation.

This means that when you have a byte variable named B with the value of 123, the numeric variable is converted into a string "123" and then printed.

In this case, print will print 3 characters or bytes. When you want to print the byte you can use the chr() function : print chr(b);

This will send just one byte to the UART.

You can connect the processors UART (TX/RX pins) to a MAX232, an FTDI232RL, a Bluetooth module or a GPS modem. Always check the logic level vcc of the UART and the device you connect to. Connecting 5V devices to a 3v3 device might damage the 3v3 device. 

A serial port can be used to update firmware with a so called boot loader. 

AVR-DOS

The AVR-DOS file system also supports PRINT. But in that case, only strings can be written to disk.

When you need to print to the second hardware UART, or to a software UART, you need to specify a channel : PRINT #1, "test"

The channel must be opened first before you can print to it. Look at [OPEN](open.md) and [CLOSE](close.md) for more details about the optional channel. For the first hardware UART, there is no need to use channels. The default for PRINT without a channel specifier, is the first UART.

So : PRINT " test" will always use the first hardware UART.

Xmega-SPI

When sending data to the SPI interface, you need to activate the SS pin. Some chips might need an active low, others might need an active high. This will depends on the slave chip.

When you use the SS=AUTO option, the level of SS will be changed automatic. Thus SS is made low, then the data bytes are sent, and finally , SS is made high again. 

For SPI, no CRLF will be sent. Thus a trailing ; is not needed. 

SPI Number of Bytes

The compiler will send 1 byte for variable which was dimensioned as a BYTE.

It will send 2 bytes for a WORD/INTEGER, 4 bytes for a LONG/SINGLE and 8 bytes for a DOUBLE.

As with all routines in BASCOM, the least significant Byte will be send first.

When you send a numeric constant, the binary value will be sent : 123 will be send a 1 byte with the value of 123.

If you send an array element, one element will be send.

With an optional parameter you can provide how many bytes must be sent. You must use a comma (,) to specify this parameter. This because the semi colon (;) is used to send multiple variables. 

![notice](notice.jpg)The delimiter for sending multiple variables is a semi colon (;) while INPUT uses the comma (,) to separate multiple variables.

Sample

```vb
Dim Tmparray(5) As Byte, Spi_send_byte As Byte, W as Word 

Config Spid = Hard, Master = Yes, Mode = 0, Clockdiv = Clk32, Data_order = Msb , Ss = Auto

```
Open "SPID" For Binary As #12 

```vb
Print #12, Spi_send_byte; W ' send ONE BYTE and 2 bytes of W

Print #12, Tmparray(1) , 2 ' send 2 bytes of tmparray, starting at element 1

Print #12, Tmparray(1) ' send 1 byte

Print #12, Tmparray(3) , 2 ' send 2 bytes starting at index 3

Print #12, 123; 1000; Tmparray(1), B' send byte with value 123, 2 bytes with value 1000, and 'b' bytes of array

```
See also

[INPUT](input.md)[,OPEN](open.md) , [CLOSE](close.md) , [SPC](spc.md) , [PRINTBIN](printbin.md) , [HEX](hex.md), [BIN](bin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : print.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: PRINT, HEX

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Byte , B1 As Byte , C As Integer , S As String * 4

```
A = 1

```vb
Print "print variable a " ; A

Print ' new line

Print "Text to print." ' constant to print

```
B1 = 10

Print Hex(b1) ' print in hexa notation

C = &HA000 ' assign value to c%

```vb
Print Hex(c) ' print in hex notation

Print C ' print in decimal notation

```
C = -32000

```vb
Print C

Print Hex(c)

```
Rem Note That Integers Range From -32767 To 32768

Print "You can also use multiple" _

; "lines using _"

```vb
Print "use it for long lines"

'From version 1.11.6.4 :

```
A = &B1010_0111

Print Bin(a)

S = "1001"

A = Binval(s)

```vb
Print A '9 dec

End

```