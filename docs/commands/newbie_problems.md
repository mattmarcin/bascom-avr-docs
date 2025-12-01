# Newbie problems

When you are using the AVR like ATTINY, ATMEGA, ATXMEGA without knowledge of the architecture you can experience some problems as a Newbie.

Regarding XMEGA see also [ATXMEGA](atxmega.md)

![notice](notice.jpg) As a newbie always use stack and framesize (until you know what you do) !

```vb
$hwstack = 24  
$swstack = 10  
$framesize = 30

```
![notice](notice.jpg) When you encounter problems always try to increase the values behind the stack's and framesize and test the program again.

If you want to learn more about hwstack, swstack and framesize start with [Memory usage](memory_usage.md)

![notice](notice.jpg) Do not include too much in Interrupt Service Routines (ISR). Keep the ISR as short as possible !

Avoid something like print function in ISR (temporarily for debugging this is OK).

See also [Language Fundamentals](language_fundamentals.md)

FAQ:

Question: What can I use as the first "Hello World" Bascom-AVR program ?

Answer: Following a "Hello World" example:

  
```vb
$regfile = "m16def.dat" ' specify the used AVR  
$crystal = 8000000 ' used crystal frequency  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
$baud = 19200 ' use baud rate 19200 baud  
  
Do  
Print "Hello World" ' Print Hello World  
Waitms 1000 ' Wait 1000ms = 1 second  
Loop  
  
End ' end program

```
With ATTINY and ATMEGA you need to check if the fuse bits are set correct for the 8MHz (for this example). Some chips will be shipped by the manufacturer (Atmel) with 1MHz frequency fuse bit settings.

If you want to change the UART Interface (like stopbits) use this here in addition to $baud.

(Dummy is used because the baudrate is already configured with $baud = 19200 )

Config Com1 = Dummy, Synchrone = 0, Parity = None, Stopbits = 1, Databits = 8, Clockpol = 0 

Q: How can I program (flash) the AVR with Bascom ?

A: You can use an external programmer. See [Supported Programmers](supported_programmers.md) (For ATTINY you need to use an external hardware programmer)

You can also use the MCS bootloader [MCS Bootloader](mcsbootloader.md) (ATMEGA or ATXMEGA)

See also Application Note: 143

[http://www.mcselec.com/index.php?option=com_content&task=view&id=159&Itemid=57](<http://www.mcselec.com/index.php?option=com_content&task=view&id=159&Itemid=57>)

Instead of using the BASCOM-AVR build in programmer you can also use our stand alone Bootloader application (for Windows):

[http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=153&Itemid=54](<http://www.mcselec.com/index.php?option=com_docman&task=doc_download&gid=153&Itemid=54>)

Q: I'm using an Arduino hardware with Bascom-AVR. How can I program it ?

A: See [ARDUINO](arduino.md)

Q: I can not set a pin high or low ? I can not read the input on a pin ?

A: The AVR has 3 registers for each port. A port normally consists of 8 pins. A port is named with a letter from A-F (ATMEGA) and even more with ATXMEGA. All parts have PORTB. When you want to set a single pin high or low you can use the SET and RESET statements. But before you use them the AVR chip must know in which direction you are going to use the pins.

Therefore there is a register named DDRx for each port. In our sample it is named DDRB. 

When you write a 0 to the bit position of the pin you can use the pin as an input. 

When you write a 1 you can use it as output. 

You can also use CONFIG PORTX.Y = INPUT|OUTPUT

After the direction bit is set you must use either the PORTx register to set a logic level or the PINx register to READ a pin level.

Yes the third register is the PINx register. In our sample, PINB.

```vb
For example we like to use PORTB.7 as an OUTPUT pin:

CONFIG PORTB.7=OUTPUT ' will write a '1' to DDRB.7  
SET PORTB.7 ' will set the MS bit to +5V  
RESET PORTB.7 ' will set MS bit to 0 V

```
When using a PIN in INPUT mode, you can also activate an internal pull up resistor. 

Pull up means that the pin is connected with an internal resistor to VCC.

To enable the pull up resistor, you need to write a '1' to the PORT register.

Example to read PORTB.0 pin :

CONFIG PORTB.0=INPUT ' clears DDRB.0  
PORTB.0=1 ' activate pull up  
Print PINB.0  ' will read LS bit and send it to the RS-232

You may also read from PORTx but it will return the value that was last written to it and not the input of the pin.

To read or write whole bytes use :

PORTB = 0 ' write 0 to register making all pins low  
```vb
PRINT PINB ' print input on pins

Config a Pin as output:

Config Porte.0 = Output

```
which is the same as:

DDRE = &B00000001

or can be written as:

```vb
set DDRE.0

Set Output:

Set porte.0

```
which is the same as:

porte.0 = 1

```vb
Reset Output:

Reset porte.0

```
which is the same as:

porte.0 = 0

```vb
Config a Pin as Input:

Config Pine.0 = Input

```
which is the same as:

DDRE.0 = 0

or can be written as:

DDRE = &B00000000

Read Input:

Variabel = PINE.0

To check one pin for status in an if .... statement:

```vb
If Pine.0 = 1 Then  
' do someting....  
End If

```
Q: I want to write a special character but they are not printed correct ?

A: Well this is not a newbie problem but I put it here so you could find it.

Some ASCII characters above 127 are interpreted wrong depending on country settings. To print the right value use : PRINT "Test{123}?"

The {xxx} will be replaced with the correct ASCII character.

You must use 3 digits otherwise the compiler will think you want to print {12} for example. This should be {012}

Q: My application was working but with a new micro it is slow and print funny ?

A: Most new microâs have an internal oscillator that is enabled by default. As it runs on 1 or 2 or 4 or 8 or 32 MHz, this might be slower or faster then your external or internal crystal. This results in slow operation.

As the baud rate is derived from the clock, it will also result in wrong baud rates.

Solution : change frequency with $crystal so the internal clock will be used.

Or change the fuse bits (or change config with XMEGA) so correct clock source like external xtal will be used.

Q: Some bits on Port C are not working ?

A: Some chips have a JTAG interface. Disable it with the proper fuse bit . Or use DISABLE JTAG in your code.

Q: Can I use an ATTINY or ATMEGA as TWI/I2C Slave ?

A: Yes, there is a commercial add on Bascom library available

Here the link: [I2CSLAVE Library (Download version) ](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1> "I2CSLAVE Library \(Download version\) ")

See also: [CONFIG TWISLAVE](config_twislave.md)

Q: What is Overlay ?

A: See [DIM](dim.md)

Q: Is there a way to use a buffer with software UART ?

A: No, this is not supported.

Q: I have an ATTINY without UART or I need an additional UART on ATMEGA. Is there a "Software UART" in Bascom-AVR ?

A: See [Using the UART](uart.md) and scroll down to SOFTWARE UART

Q: How can I start with ATXMETGA and Bascom-AVR ?

A: See [ATXMEGA](atxmega.md)

Q: How to declare a subroutine or function ?

A: See [DECLARE SUB](declare_sub.md) or [DECLARE FUNCTION](declare_function.md)

Q: I have a number like 1234.888999 but I just want to have one digit after decimal point (1234.8). How can I do that ?

A: See [CONFIG SINGLE](configsingle.md)

Q: How can I set or reset single bits in byte/integer/long variables ?

A: There are several ways to write or read a single bit:

1\. You can use [NBITS](nbits.md) or [BITS](bits.md) to set or reset one or more bits

2\. You can use it following way:

Example on how to set/reset single bits in a variable.

Dim my_long_var As Long  
My_long_var.0 = 1

You can also use SET or RESET  
  
```vb
Set My_long_var.31

Reset My_long_var.31  


```
You even can use a variable as index 

  
Dim Idx As Byte  
Idx = 3  
```vb
Reset My_long_var.idx

For a long variable Idx can be from 0......31

For an integer Idx can be from 0....15

For a byte Idx can be from 0......7

```
3\. You can use BITWAIT to wait until a bit is set (1) or reset (0).

Example:

Dim A As Bit  
Bitwait A , Set ' wait until bit a is set  
```vb
'the above will never continue because it is not set i software  
'it could be set in an ISR routine  
  
```
Bitwait Pinb.7 , Reset ' wait until bit 7 of Port B is 0.

4\. You can use [TOGGLE](toggle.md) to invert the state of a bit

```vb
Dim my_long_var As Long  
Toggle My_long_var.31  


```
Q: Can I create BIT ARRAYS larger then a LONG variable ?

A: Yes, here is a way to do it:

```vb
$regfile = "m162def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Dim Byte_arr(32) As Byte  
Dim Idx As Byte  
  
```
Byte_arr(1).8 = 1  
Print "Byte_arr(2) = " ; Bin(byte_arr(2))  
  
Byte_arr(1).15 = 1  
Print "Byte_arr(2) = " ; Bin(byte_arr(2))  
  
Byte_arr(1).29 = 1  
Print "Byte_arr(4) = " ; Bin(byte_arr(4))  
  
Idx = 63  
Byte_arr(1).idx = 1  
Print "Byte_arr(8) = " ; Bin(byte_arr(8))  
  
Idx = 255  
Byte_arr(1).idx = 1  
```vb
Print "Byte_arr(32) = " ; Bin(byte_arr(32))  
  
'(  
```
Bascom Simulator Output =  
  
Byte_arr(2) = 00000001  
Byte_arr(2) = 10000001  
Byte_arr(4) = 00100000  
Byte_arr(8) = 10000000  
Byte_arr(32) = 10000000  
  
```vb
')  
  
End

```
Q: Can I pass a BIT variable to SUB routines or user FUNCTION ?

A: You can not pass BIT variables to SUB routines or user FUNCTION

Use a BYTE for that.

Here is one of many workarounds for that:

```vb
$regfile = "m162def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Config Submode = New  
  
Dim C As Byte

  
Sub Test(byref B As Byte)  
```
Local C As Byte  
C = B And &B00000001  
  
```vb
If C = 1 Then   
Print "B = 1"  
Else  
Print "B = 0"  
End If  
End Sub  
  
'Main program  
  
Set C.0  
```
Call Test(c)  
  
Reset C.0  
Call Test(c)  
  
End ' end program

Q: Can I dimension a LOCAL variable in a function or sub routine as BIT ?

A: You can not. BIT variables are not possible because they are GLOBAL to the system.

Q: I still have a problem. What to do ?

A: Here is the link to the Bascom-AVR forum: [http://www.mcselec.com/index2.php?option=com_forum&Itemid=59](<http://www.mcselec.com/index2.php?option=com_forum&Itemid=59>)

![notice](notice.jpg) At first please try to search the forum (often you can find users with the same problem) . The search page is here:

[http://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=search](<http://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=search>)

If the forum can not help you, here is the Email address for support: [support@mcselec.com](<mailto:support@mcselec.com>)

PLEASE provide as much as possible information in your post or Email:

\- Include the Bascom-AVR version number and your serial number in the Email to support 

![notice](notice.jpg) Do not post your serial number in the Forum !!! ![notice](notice.jpg)

\- Always test with the latest available version, support is only available for the latest version

\- Include a small sample that will demonstrate the error.

\- Make sure you include all required files for compilation or for showing the problem.

\- Be clear if the problem exist in the simulator or the hardware and what kind of hardware you use