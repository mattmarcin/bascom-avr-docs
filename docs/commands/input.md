# INPUT

Action

Allows input from the keyboard, file or SPI during program execution.

Syntax

```vb
INPUT [" prompt" ] , var[ , varn ]

INPUT #ch, var[ , varn ]

```
Syntax SPI

INPUT #ch, var [;bts] [ , varn [;bts] ]

Remarks

Prompt | An optional string constant printed before the prompt character.  
---|---  
Var,varn | A variable to accept the input value or a string.  
Ch | A channel number, which identifies an opened file. This can be a hard coded constant or a variable.  
bts | An optional number of byes to read. Only for SPI.  
  
The INPUT routine can be used when you have an RS-232 interface on your uP.

The RS-232 interface can be connected to a serial communication port of your computer.

This way you can use a terminal emulator and the keyboard as an input device.

You can also use the built-in terminal emulator.

For usage with the AVR-DOS file system, you can read variables from an opened file. Since these variables are stored in ASCII format, the data is converted to the proper format automatically.

When you use INPUT with a file, the prompt is not supported.

When [$BIGSTRINGS](bigstrings.md) is used you can read read up to 65535 bytes.

Difference with VB

In VB you can specify &H with INPUT so VB will recognize that a hexadecimal string is being used.

BASCOM implements a new statement : INPUTHEX.

Xmega-SPI

When receiving data from the SPI interface, you need to activate the SS pin. Some chips might need an active low, others might need an active high. This will depends on the slave chip.

When you use the SS=AUTO option, the level of SS will be changed automatic. Thus SS is made low, then the data bytes are received, and finally , SS is made high again. 

Receiving data works by sending a data byte and returning the data that is shifted out. The data that will be sent is a 0. You can alter this in the library, _inputspivar routine.

You can not sent constants using the INPUT with SPI. So INPUT #10, "SPI", var is not supported. 

INPUT used with SPI will not wait for a return either. It will wait for the number of bytes that fits into the variable. See [CONFIG SPIx](config_spix.md) for an example.

Number of Bytes

The compiler will receive 1 byte for a variable which was dimensioned as a BYTE.

It will receive 2 bytes for a WORD/INTEGER, 4 bytes for a LONG/SINGLE and 8 bytes for a DOUBLE.

As with all routines in BASCOM, the least significant Byte will be received first.

If you specify an array, one element will be received.

SPI

With an optional parameter you can provide how many bytes must be received. You must use a semicolon (;) to specify this parameter. This because the comma (,) is used to receive multiple variables. 

```vb
Dim Tmparray(5) As Byte , Spi_send_byte As Byte , W as Word

Input #12 , Spi_receive_byte ; 1 ' READ 1 byte

Input #12 , Tmparray(1) ; 1 , Tmparray(2) ; B ' read 1 byte and 'b' bytes starting at element 2

```
The optional parameter is only supported for the SPI channel. When required with serial data, you can also use INPUTBIN.

See also

[INPUTHEX](inputhex.md) , [PRINT](print.md) , [ECHO](echo.md) , [WRITE](write.md) , [INPUTBIN](inputbin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : input.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: INPUT, INPUTHEX

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

Dim V As Byte , B1 As Byte

Dim C As Integer , D As Byte

Dim S As String * 15

Input "Use this to ask a question " , V

Input B1 'leave out for no question

Input "Enter integer " , C

Print C

```
Inputhex "Enter hex number (4 bytes) " , C

Print C

Inputhex "Enter hex byte (2 bytes) " , D

```vb
Print D

Input "More variables " , C , D

Print C ; " " ; D

Input C Noecho 'supress echo

Input "Enter your name " , S

Print "Hello " ; S

Input S Noecho 'without echo

Print S

End

```