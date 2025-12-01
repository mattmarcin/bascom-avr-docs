# CONFIG INPUT

Action

Instruct the compiler to modify serial input line terminator behaviour

Syntax

CONFIG INPUT1 = term , ECHO=echo

Syntax Xmega

CONFIG INPUT1|INPUT2|INPUT3|INPUT4|INPUT5|INPUT6|INPUT7|INPUT8 = term , ECHO=echo

Remarks

INPUT | Use INPUT or INPUT1 for COM1, INPUT2 for COM2, INPUT3 for COM3, etc.  
---|---  
Term | A parameter with one of the following values : CR - Carriage Return (default) LF - Line Feed CRLF - Carriage Return followed by a Line Feed LFCR - Line Feed followed by a Carriage Return  
Echo | A parameter with one of the following values : CR - Carriage Return LF - Line Feed CRLF - Carriage Return followed by a Line Feed (default) LFCR - Line Feed followed by a Carriage Return  
  
The 'term' parameter specifies which character(s) are expected to terminate the [INPUT](input.md) statement with serial communication. It has no impact on the DOS file system INPUT.

In most cases, when you press <ENTER> , a carriage return(ASCII 13) will be sent. In some cases, a line feed (LF) will also be sent after the CR. It depends on the terminal emulator or serial communication OCX control you use.

The 'echo' parameter specifies which character(s) are send back to the terminal emulator after the INPUT terminator is received. By default CR and LF is sent. But you can specify which characters are sent. This can be different characters then the 'term' characters. So when you send in your VB application a string, and end it with a CR, you can send back a LF only when you want.

![notice](notice.jpg)When NOECHO is used, NO characters are sent back even while configured with CONFIG INPUT

```vb
For the XMega you can specify for each UART how it should handle input and echo.

For the first UART you may use INPUT0, INPUT1 or just INPUT. For the second UART you must use INPUT2, for UART3 -> INPUT3, etc.

```
See also

[INPUT](input.md)

ASM

NONE

Example

```vb
Config Input1 = CR , Echo = CRLF

Dim S as String * 20

Input "Hello ",s

```