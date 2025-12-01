# OPEN

Action

Opens a device.

Syntax

OPEN "device" for MODE As #channel

OPEN file FOR MODE as #channel

Remarks

Device | The default device is COM1 and you don't need to open a channel to use INPUT/OUTPUT on this device. With the implementation of the software UART, the compiler must know to which pin/device you will send/receive the data. So that is why the OPEN statement must be used. It tells the compiler about the pin you use for the serial input or output and the baud rate you want to use. COMB.0:9600,8,N,2 will use PORT B.0 at 9600 baud with 2 stop bits. The format for COM1 and COM2 is : COM1: or COM2: There is no speed/baud rate parameter since the default baud rate will be used which is specified with $BAUD or $BAUD1 The format for the software UART is: COMpin:speed,8,N,stopbits[,INVERTED] Where pin is the name of the PORT-pin. Speed must be specified and stop bits can be 1 or 2. 7 bit data or 8 bit data may be used. For parity N, O or E can be used. An optional parameter ,INVERTED can be specified to use inverted RS-232. Open "COMD.1:9600,8,N,1,INVERTED" For Output As #1 , will use pin PORTD.1 for output with 9600 baud, 1 stop bit and with inverted RS-232. For the AVR-DOS file system, Device can also be a string or filename constant like "readme.txt" or sFileName For the Xmega, you can also open SPIC, SPID, SPIE and SPIF for SPI communication. Or for TWI you can use TWIC, TWID, TWIE or TWIF.  
---|---  
MODE | You can use BINARY or RANDOM for COM1 and COM2, but for the software UART pins, you must specify INPUT or OUTPUT. For the AVR-DOS file system, MODE may be INPUT, OUTPUT, APPEND or BINARY.  
Channel | The number of the channel to open. Must be a positive constant >0. For the AVR-DOS file system, the channel may be a positive constant or a numeric variable. Note that the AVD-DOS file system uses real file handles. The software UART does not use real file handles. For the Xmega UART, you may use a variable that starts with BUART. This need to be a numeric variable like a byte. Using a variable allows you to use the UART dynamic.  
  
UART

The statements that support the device are [PRINT](print.md) , [INPUT](input.md) , [INPUTHEX](inputhex.md) , [INKEY](inkey.md) and [WAITKEY](waitkey.md)

Every opened device must be closed using the CLOSE #channel statement. Of course, you must use the same channel number.

In DOS the #number is a DOS file number that is passed to low level routines. In BASCOM the channel number is only used to identify the channel but there are no file handles. So opening a channel, will not use a channel. Closing a channel is not needed for UARTS. When you do so, it is ignored. If you OPEN the channel again, you will get an error message.

So use OPEN in the begin of your program, and if you use CLOSE, use it at the end of your program.

What is the difference?

In VB you can close the channel in a subroutine like this:

OPEN "com1:" for binary as #1

Call test

Close #1

```vb
End

Sub test

Print #1, "test"

End Sub

```
This will work since the file number is a real variable in the OS.

In BASCOM it will not work : the CLOSE must come after the last I/O statement:

OPEN "com1:" for binary as #1

Call test

```vb
End

Sub test

Print #1, "test"

End Sub

```
Close #1

The INPUT statement in combination with the software UART, will not echo characters back because there is no default associated pin for this.

AVR-DOS

The AVR-DOS file system uses real file handles. This means that the CLOSE statement can be used at any place in your program just as with VB.

There are a few file modes, all inherited from VB/QB. They work exactly the same.

File mode | Description  
---|---  
OUTPUT | Use OUTPUT to create a file, and to write ASCII data to the file. A readme.txt file on your PC is an example of an ASCII file. ASCII files have a trailing CR+LF for each line you print. The PRINT statement is used in combination with OUTPUT mode.  
INPUT | This mode is intended to OPEN an ASCII file and to read data only. You can not write data in this mode. The file need to exist, and must contain ASCII data. LINEINPUT can be used to read data from the file.  
APPEND | APPEND mode is used on ASCII files and will not erase the file, but will append data to the end of the file. This is useful when you want to log data to a file. Opening in OUTPUT mode would erase the file if it existed. When a file does not exist yet, it will be created. This is not the case in QB/VB.  
BINARY | In BINARY mode you have full read and write access to all data in the file. You can open a text file to get binary access, or you can open a binary file such as an image file. GET and PUT can be used with binary files.  
  
![notice](notice.jpg)The following information from the author is for advanced users only. 

GET/PUT is not supposed to work with INPUT/OUTPUT due to the rules in VB/QBASIC.

In the file CONFIG_AVR-DOS.bas (nearly at the of the file) you will find the constants 

' permission Masks for file access routine regarding to the file open mode

Const cFileWrite_Mode = &B00101010 ' Binary, Append, Output

Const cFileRead_Mode = &B00100001 ' Binary, Input

Const cFileSeekSet_Mode = &B00100000 ' Binary

Const cFileInputLine = &B00100001 ' Binary, Input

Const cFilePut_Mode = &B00100000 ' Binary

Const cFileGet_Mode = &B00100000 â Binary

Where you can control, which routines can used in each file open mode. There you can see, that in standard usage GET and PUT is only allowed in BINARY.

Some time ago I wrote the Bootloader with AVR-DOS and I had the problem to keep Flash usage as low as possible. In the Bootloader I had to work with GET to read in the bytes, because the content is no ASCII text. On the other side, if you open a file in INPUT mode, you need less code. So I tested to open the File in input mode and allow to use GET in Input Mode.

I changed:

Const cFileGet_Mode = &B00100001

So GET can work in INPUT too in the BOOTLOADER.

If you switch in the constants cFileGet_Mode the last 0 to a 1, you can use GET in INPUT Open mode to. With the bootloader.bas I changed the Config_AVR-DOS.bas too. With this changed Config_AVR-DOS.bas GET can used in INPUT, with the standard CONFIG_AVR-DOS not.

This change makes no problem in code, but I think this is only something for experienced AVR-DOS user.

Whether he can use GET in INPUT mode depends only on this last bit in the constant cFileGET_Mode in the file Config_AVR-DOS.bas. This bit controls, what can be used in INPUT mode.

Xmega-SPI

The Xmega has 4 SPI interfaces. The channel is used to communicate with the different devices. 

And just as with the Xmega UART, you can use the SPI dynamic. When the channel variable starts with BSPI, you can pass a variable channel. 

An example you will find at [CONFIG SPIx](config_spix.md)

You can OPEN a SPI device only in BINARY mode.

Xmega-TWI

The Xmega has 4 TWI interfaces. The channel is used to communicate with the different devices. 

You can OPEN a TWI device only in BINARY mode. Only constants are allowed for the channel.

See also

[CLOSE](close.md) , [CRYSTAL](crystal_2.md), [PRINT](print.md), [LINE INPUT](line_input.md) , [LOC](loc.md) , [LOF](lof.md) , [EOF](eof.md)

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
Example XMEGA TWI

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-TWI.bas  
' This sample demonstrates the Xmega128A1 TWI  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Dim S As String * 20  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Dim N As String * 16 , B As Byte  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Config Input1 = Cr , Echo = Crlf ' CR is used for input, we echo back CR and LF  
  
```
Open "COM1:" For Binary As #1  
```vb
' ^^^^ change from COM1-COM8  
  
Print #1 , "Xmega revision:" ; Mcu_revid ' make sure it is 7 or higher !!! lower revs have many flaws  
  
```
Const Usechannel = 1  
  
  
```vb
Dim B1 As Byte , B2 As Byte  
Dim W As Word At B1 Overlay  
  
  
  
  
  
```
Open "twic" For Binary As #4 ' or use TWID,TWIE oR TWIF  
```vb
Config Twi = 100000 'CONFIG TWI will ENABLE the TWI master interface  
'you can also use TWIC, TWID, TWIE of TWIF  
  

#if Usechannel = 1  
```
I2cinit #4  

#else  
I2cinit  

```vb
#endif  
  
  
Do  
```
I2cstart  
Waitms 20  
I2cwbyte &H70 ' slave address write  
Waitms 20  
I2cwbyte &B10101010 ' write command  
Waitms 20  
I2cwbyte 2  
Waitms 20  
I2cstop  
```vb
Print "Error : " ; Err ' show error status  
  
'waitms 50  
Print "start"  
```
I2cstart  
Print "Error : " ; Err ' show error  
I2cwbyte &H71  
Print "Error : " ; Err ' show error  
I2crbyte B1 , Ack  
Print "Error : " ; Err ' show error  
I2crbyte B2 , Nack  
Print "Error : " ; Err ' show error  
I2cstop  
```vb
Print "received A/D : " ; W ; "-" ; B1 ; "-" ; B2  
Waitms 500 'wait a bit  
Loop  
  
  
  
Dim J As Byte , C As Byte , K As Byte  
Dim Twi_start As Byte ' you MUST dim this variable since it is used by the lib  
  
'determine if we have an i2c slave on the bus  
For J = 0 To 200 Step 2  
Print J  

#if Usechannel = 1  
```
I2cstart #4  

#else  
I2cstart  

#endif  
  
I2cwbyte J  
```vb
If Err = 0 Then ' no errors  
Print "FOUND : " ; Hex(j)  
'write some value to the pcf8574A  

#if Usechannel = 1  
```
I2cwbyte &B1100_0101 , #4  

#else  
I2cwbyte &B1100_0101  

```vb
#endif  
Print Err  
Exit For  
End If  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
Next  

#if Usechannel = 1  
```
I2cstop #4  

#else  
I2cstop  

```vb
#endif  
  

#if Usechannel = 1  
```
I2cstart #4  
I2cwbyte &H71 , #4 'read address  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack , #4  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack , #4  
Print Bin(j) ; " err:" ; Err  
I2cstop #4  

#else  
I2cstart  
I2cwbyte &H71 'read address  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Ack  
Print Bin(j) ; " err:" ; Err  
I2crbyte J , Nack  
Print Bin(j) ; " err:" ; Err  
I2cstop  

```vb
#endif  
  
'try a transaction  

#if Usechannel = 1  
```
I2csend &H70 , 255 , #4 ' all 1  
Waitms 1000  
I2csend &H70 , 0 , #4 'all 0  

#else  
I2csend &H70 , 255  
Waitms 1000  
I2csend &H70 , 0  

```vb
#endif  
Print Err  
  
  
'read transaction  
Dim Var As Byte  
```
Var = &B11111111  

#if Usechannel = 1  
I2creceive &H70 , Var , 1 , 1 , #4 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 , #4 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#else  
```
I2creceive &H70 , Var , 1 , 1 ' send and receive  
Print Bin(var) ; "-" ; Err  
I2creceive &H70 , Var , 0 , 1 ' just receive  
```vb
Print Bin(var) ; "-" ; Err  

#endif  
  
End

```