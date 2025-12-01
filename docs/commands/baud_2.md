# BAUD

Action

Changes the baud rate for the hardware or software UART.

Syntax

BAUD = const

Syntax Software UART

BAUD #x , const

Remarks

X | The channel number of the software UART.  
---|---  
Const | A numeric constant for the baud rate that you want to use.  
  
![notice](notice.jpg) Do not confuse the BAUD statement with the [$BAUD](baud_1.md) compiler directive.

And do not confuse [$CRYSTAL](crystal_1.md) and [CRYSTAL](crystal_2.md)

$BAUD overrides the compiler setting for the baud rate while BAUD will change the current baud rate.

So $BAUD is a global project setting in your source code while BAUD will change the baud rate during run time.

You could use BAUD to change the baud rate during run time after the user changes a setting.

BAUD = ... will work on the hardware UART.

BAUD #x, yyyy will work on the software or HW UART. The specified channel must be the same as used with the OPEN statement.

When you use a software UART and change the baud rate at run time using BAUD, you must set the baud rate after the OPEN statements as well.

When you do not use BAUD, there is no need to set it. So for example :

Open "COMC.1:9600,8,N,1" For Output As #1

print #1 , "this is a test 9600" 'no need for BAUD since one baud rate is used

But when BAUD is changed :

Open "COMC.1:9600,8,N,1" For Output As #1

baud #1 , 9600 'we need to set it since we change baud at run time

print #1 , "this is a test 9600"

baud #1 , 115200

print #1 , "this is a test 115200"

![notice](notice.jpg)Variables are not supported. Only constants. 

See also

[$CRYSTAL](crystal_1.md) , [$BAUD](baud_1.md) , [BAUD1](baud1.md)

ASM

NONE

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Print "Hello"

'Now change the baud rate in a program

```
Baud = 9600

```vb
Print "Did you change the terminal emulator baud rate too?"

End

```