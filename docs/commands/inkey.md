# INKEY

Action

Returns the ASCII value of the first character in the serial input buffer.

Syntax

var = INKEY()

var = INKEY(#channel)

Remarks

Var | Byte, Integer, Word, Long or String variable.  
---|---  
Channel | A constant number that identifies the opened channel if software UART mode  
  
If there is no character waiting, a zero will be returned.

Use the IsCharWaiting() function to check if there is a byte waiting.

The INKEY routine can be used when you have a RS-232 interface on your uP.

The RS-232 interface can be connected to a comport of your computer.

As zero(0) will be returned when no character is waiting, the usage is limited when the value of 0 is used in the serial transmission. You can not make a difference between a byte with the value 0 and the case where no data is available.

In that case you can use IsCharwaiting to deterimine if there is a byte waiting.

See also

[WAITKEY](waitkey.md) , [ISCHARWAITING](ischarwaiting.md) , [$TIMEOUT](_timeout.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : inkey.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: INKEY , WAITKEY

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

Dim A As Byte , S As String * 2

Do

```
A = Inkey() 'get ascii value from serial port

```vb
's = Inkey()

If A > 0 Then 'we got something

Print "ASCII code " ; A ; " from serial"

End If

Loop Until A = 27 'until ESC is pressed

```
A = Waitkey() 'wait for a key

```vb
's = waitkey()

Print Chr(a)

'wait until ESC is pressed

Do

Loop Until Inkey() = 27

'When you need to receive binary data and the bibary value 0 ,

'you can use the IScharwaiting() function.

'This will return 1 when there is a char waiting and 0 if there is no char waiting.

'You can get the char with inkey or waitkey then.

End

```