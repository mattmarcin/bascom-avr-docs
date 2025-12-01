# $TIMEOUT

Action

Enable timeout on the hardware UART and software UART.

Syntax

$TIMEOUT = value

Remarks

Value | A constant that fits into a LONG , indicating how much time must be waited before the waiting is terminated.  
---|---  
  
All RS-232 serial statements and functions(except INKEY) that use the hardware UART or software UART, will halt the program until a character is received. Only with buffered serial input you can process your main program while the buffer receives data on the background.

![notice](notice.jpg) $TIMEOUT is an alternative for normal serial reception. It is not intended to be used with buffered serial reception. As of version 2077, the first (and only the first) UART supports the $TIMEOUT feature. The latest version supports timeout on ALL UARTS.

When you assign a constant to $TIMEOUT, you actual assign a value to the internal created value named ___TIMEOUT.

This value will be decremented in the routine that waits for serial data. When it reaches zero, it will terminate.

So the bigger the value, the longer the wait time before the timeout occurs. The timeout is not in seconds or microseconds, it is a relative number. Only the speed of the oscillator has effect on the duration. And the value of the number of course.

When the time out is reached, a zero/null will be returned to the calling routine. Waitkey() will return 0 when used with a byte. When you use INPUT with a string, the timeout will be set for every character. And when 3 characters are received but no CR and/or LF, these 3 characters will be returned. 

![notice](notice.jpg)When you activate $TIMEOUT, and your micro has two UARTS(Mega128 for example) it will be active for both UART0 and UART1. And for an ATMEGA2560 with 4 UARTS, it will be enabled for all 4 UARTS, but only when no serial input buffer is configured.

$TIMEOUT is also supported by the software UART. In fact, when you enable it for the hardware UART, you enable it for the software UART as well.

Note that for the SW UART the maximum timeout value is lower. The maximum is &HFF_FF_FF. This because 1 byte less is used.

See Also

[INPUT](input.md) , [WAITKEY](waitkey.md) , [INKEY](inkey.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : timeout.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of the $timeout option

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'most serial communication functions and routines wait until a character

'or end of line is received.

'This blocks execution of your program. SOmething you can change by using buffered input

'There is also another option : using a timeout

'$timeout Does Not Work With Buffered Serial Input

Dim Sname As String * 10

Dim B As Byte

Do

$timeout = 1000000

Input "Name : " , Sname

Print "Hello " ; Sname

$timeout = 5000000

Input "Name : " , Sname

Print "Hello " ; Sname

Loop

'you can re-configure $timeout

```