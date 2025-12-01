# ISCHARWAITING

Action

Returns one(1) when a character is waiting in the hardware UART buffer.

Syntax

var = ISCHARWAITING()

var = ISCHARWAITING(#channel)

Remarks

Var | Byte, Integer, Word or Long variable.  
---|---  
Channel | A constant number that identifies the opened channel.  
  
```vb
If there is no character waiting, a zero will be returned.

If there is a character waiting, a one (1) will be returned.

```
The character is not retrieved or altered by the function.

While the Inkey() will get the character from the HW UART when there is a character in the buffer, it will return a zero when the character is zero. This makes it unusable to work with binary data that might contain the value 0.

With IsCharWaiting() you can first check for the presence of a character and when the function returns 1, you can retrieve the character with Inkey or Waitkey.

IsCharWaiting can NOT be used with a software uart (SW-UART). This because a SW-UART does not buffer the data it receives or sends.

See also

[WAITKEY](waitkey.md) , [INKEY](inkey.md) , [$TIMEOUT](_timeout.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Byte , S As String * 2

Do

```
A = Ischarwaiting()

If A = 1 Then 'we got something

A = Waitkey() 'get it

```vb
Print "ASCII code " ; A ; " from serial"

End If

Loop Until A = 27 'until ESC is pressed

```