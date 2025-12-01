# Using the UART

UART

A Universal Asynchronous Receiver and Transmitter (UART) can be used to send and receive data between two devices. More specific these devices can be PC-to-PC, PC-to-micro controller and micro controller-to-micro controller. The UART communicates using TTL voltages +5V and 0V or LVTTL depending on your micro controllers VCC voltage.

If you wish to connect to a PC you need to use RS232 protocol specifications. This means that the hardware communication is done with specific voltage levels. (+15V and -15V) This can be achieved by using a MAX232 level shifter.

The hardware is explained in this schematic:

![UART](uart.png)

The DB-9 connector has 9 pins but you only need to use 3 of them. Notice that the drawing above shows the FRONT VIEW thus remember that you are soldering on the other side. On most connectors the pin outs can also be found on the connector itself.

If your controller has no UART you can use a software UART see below. If your controller has one UART you connect controller pins TxD and RxD to TxD and RxD in the schematic above. If your controller has more than one UART you connect controller pins TxD0 and RxD0 to TxD and RxD in the schematic above.

You now need to initialize the program in your micro controller, open a new .bas file and add the following code in the beginning of your program.

```vb
$regfile = "your micro here def.dat"

$crystal = 8000000

$baud = 19200

```
Make sure to define your micro controller after $regfile for example if you use the ATMega32

$regfile = "m32def.dat"

Some new chips can use an internal oscillator, also some chips are configured to use the internal oscillator by default. Using an internal oscillator means you do not need an external crystal.

Perform this step only if you have an internal oscillator.

Open the BASCOM-AVR programmer like this:

![UART_PG](uart_pg.png)

•| Select the âLock and Fuse Bitsâ tab and maximize the programmer window.  
---|---  
  
•| Check if you see the following in the âFusebitâ section:  
---|---  
  
"1:Divide Clock by 8 Disabled"

and

"Int. RC Osc. 8 MHz; Start-up time: X CK + X ms; [CKSEL=XXXX SUT=XX]"

![UART_fusebits](uart_fusebits.png)

These options are not available for all AVRâs, if you donât have the option do not change any fuse bits.

If these options are available, but in a wrong setting. Change the setting in the drop down box and click another Fuse section. Finally click the "Program FS" button. Click "Refresh" to see the actual setting.

Now connect a straight cable between the DB-9 connector, micro controller side and the PC side.

Program a test program into your micro controller, it should look like this:

```vb
$regfile = "m32def.dat" 'Define your own

$crystal = 8000000 

$baud = 19200 

Do

Print "Hello World"

Waitms 25

Loop

End

```
Now open the BASCOM-AVR Terminal and set your connection settings by clicking âTerminalâ -> âSettingsâ Select your computers COM port and select baud 19200, Parity none, Data bits 8, Stop bits 1, Handshake none, emulation none.

![UART_terminal](uart_terminal.png) ![UART_TerminalShow](uart_terminalshow.png)

If you see the Hello World displayed in the BASCOM-AVR Terminal emulator window, your configuration is OK. Congratulations.

Example

You can also try this example with the BASCOM Terminal emulator, it shows you how to send and receive with various commands.

```vb
$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

Dim Akey As Byte 'Here we declare a byte variable

Print

Print "Hello, hit any alphanumerical key..."

```
Akey = Waitkey() 'Waitkey waits untill a char is received from the UART

```vb
Print Akey

Wait 1

Print

Print "Thanks!, as you could see the controller prints a number"

Print "but not the key you pressed."

Wait 1

Print

Print "Now try the enter key..."

```
Akey = Waitkey()

Akey = Waitkey()

```vb
Print Akey

Print

Print "The number you see is the ASCII value of the key you pressed."

Print "We need to convert the number back to the key..."

Print 'Notice what this line does

Print "Please try an alphanumerical key again..."

```
Akey = Waitkey()

```vb
Print Chr(akey) 'Notice what this does

Print "That's fine!"

Wait 1

Print

Print "For a lot of functions, just one key is not enough..."

Print "Now type your name and hit enter to confirm"

Dim Inputstring As String * 12 'Declare a string variable here

Do

```
Akey = Waitkey()

If Akey = 13 Then Goto Thanks 'On enter key goto thanks

Inputstring = Inputstring + Chr(akey) 'Assign the string

Loop

Thanks:

```vb
Print "Thank you " ; Inputstring ; " !" 'Notice what ; does

Wait 1

Print

Print "Take a look at the program code and try to understand"

Print "how this program works. Also press F1 at the statements"

Print

Print "If you understand everything continue to the next experiment"

End

```
ASCII

As you could have seen in the previous example we use the PRINT statement to send something to the UART. Actually we do not send just text. We send ASCII characters. ASCII means American Standard Code for Information Interchange. Basically ASCII is a list of 127 characters.

ASCII Table (Incomplete)

Decimal Hex Binary Value

\------- --- ------ -----

000 000 00000000 NUL (Null char.)

008 008 00001000 BS (Backspace)

009 009 00001001 HT (Horizontal Tab)

010 00A 00001010 LF (Line Feed)

012 00C 00001100 FF (Form Feed)

013 00D 00001101 CR (Carriage Return)

048 030 00110000 0

049 031 00110001 1

052 034 00110100 4

065 041 01000001 A

066 042 01000010 B

067 043 01000011 C

You can find a complete ASCII table [here](asciichart.md)

CARRIAGE RETURN (CR) AND LINE FEED (LF)

In the previous example you can also see that a second print statement always prints the printed text to the following line. This is caused by the fact that the print statement always adds the CR and LF characters.

Basically if we state:

Print âABCâ

We send 65 66 67 13 10 to the UART. (In binary format)

The carriage return character (13) returns the cursor back to column position 0 of the current line. The line feed (10) moves the cursor to the next line.

Print âABCâ ;

When we type a semicolon ( ; ) at the end of the line...

Bascom does not send a carriage return/line feed, so you can print another text after the ABC on the same line.

Print âABCâ ; Chr(13) ;

This would send only ABC CR. The next print would overwrite the ABC.

OVERVIEW

Here are some other commands that you can use for UART communications:

Waitkey()

Waitkey will until a character is received in the serial buffer.

Ischarwaiting()

Returns 1 when a character is waiting in the hardware UART buffer.

Inkey()

Inkey returns the ASCII value of the first character in the serial input buffer.

Print

Sends a variable or non-variable string to the UART

ANOTHER EXAMPLE

This example shows how to use Ischarwaiting to test if there is a key pressed. And if there is, read to a variable.

```vb
'Print "Press B key to start"

Dim Serialcharwaiting As Byte, Serialchar As Byte

```
Serialcharwaiting = Ischarwaiting() 'Check if B or b pressed then goto

If Serialcharwaiting = 1 Then

Serialchar = Inkey()

```vb
If Serialchar = 66 Or Serialchar = 98 Then

Goto MyRoutine

End If

End If

Goto Main

```
Myroutine:

'Statements

Main:

```vb
'Statements

End

```
BUFFERING SERIAL DATA

If you wish to send and receive data at high speed, you need to use serial input and serial output buffers. This buffering is implemented in BASCOM-AVR and can only be used for hardware UARTâs.

To configure a UART to use buffers, you need to use the Config statement.

Config Serialout = Buffered , Size = 20

and/or

Config Serialin = Buffered , Size = 20

More information can be found in BASCOM-Help. Search topic = "[config serialin"](config_serialin.md). There is also a sample program âRS232BUFFER.BASâ in the samples folder if you wish a demonstration of the buffering.

SOFTWARE UART

The previous examples used the hardware UART. That means the compiler uses the internal UART registers and internal hardware (RxD(0) and TxD(0)) of the AVR. If you donât have a hardware UART you can also use a software UART.

The Bascom compiler makes it easy to âcreateâ additional UARTâs. Bascom creates software UARTâs on virtually every port pin. 

Remember that a software UART is not as robust as a hardware UART, thus you can get timing problems if you have lots of interrupts in your program.

For this example we use micro controller pins portc.1 and portc.2.

Connect portc.1 to TxD and portc.2 to RxD see the schematic above.

Change the $regfile and program this example:

```vb
$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

Dim B As Byte

Waitms 100

'Open a TRANSMIT channel for output

```
Open "comc.1:19200,8,n,1" For Output As #1

```vb
Print #1 , "serial output"

'Now open a RECEIVE channel for input

```
Open "comc.2:19200,8,n,1" For Input As #2

```vb
'Since there is no relation between the input and output pin

'there is NO ECHO while keys are typed

Print #1 , "Press any alpha numerical key"

'With INKEY() we can check if there is data available

'To use it with the software UART you must provide the channel

Do

'Store in byte

```
B = Inkey(#2)

```vb
'When the value > 0 we got something

If B > 0 Then

Print #1 , Chr(b) 'Print the character

End If

Loop

```
Close #2 'Close the channels

Close #1

End

After you have programmed the controller and you connected the serial cable, open the terminal emulator by clicking on ![terminal-icon](terminal-icon.png) in Bascom.

You should see the program asking for an alphanumerical input, and it should print the input back to the terminal.