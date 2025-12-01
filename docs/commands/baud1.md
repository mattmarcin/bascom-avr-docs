# BAUD1-BAUDx

Action

Changes the baud rate for the specified hardware UART.

Syntax

BAUD = var

BAUD1 = var

BAUD2 = var

BAUD3 = var

Syntax Xmega

BAUD = var

BAUD1 = var

BAUD2 = var

BAUD3 = var

BAUD4 = var

BAUD5 = var

BAUD6 = var

BAUD7 = var

Xmega Syntax

BAUDx = constant

Remarks

Var | The baud rate that you want to use.  
---|---  
baud | COM1, USART0, xmega and normal AVR  
baud1 | COM2, USART1, xmega and normal AVR  
baud2 | COM2, USART2, xmega and normal AVR  
baud3 | COM3, USART3, xmega and normal AVR  
baud4 | COM4, USART4, xmega  
baud5 | COM5, USART5, xmega  
baud6 | COM6, USART6, xmega  
baud7 | COM7, USART7, xmega  
  
Do not confuse the BAUD1 statement with the $BAUD1 compiler directive.

And do not confuse [$CRYSTAL](crystal_1.md) and [CRYSTAL](crystal_2.md)

$BAUD1 overrides the compiler setting for the baud rate while BAUD1 will change the current baud rate.

BAUD1 = ... will work on the hardware UART.

BAUDn = ... will work on the specified hardware UART.

mega

For the mega, the X represents the UART number. BAUD means, the first UART which you refer to with OPEN as COM1, BAUD1 the second UART, and BAUD3 is the last UART. A channel number is not supported.

You need to use a constant for the baud rate. Variables are not supported. 

Xmega

```vb
For the xmega, the X represents the UART number. BAUD means, the first UART which you refer to with OPEN as COM1, BAUD1 the second UART, and BAUD7 is the last UART. A channel number is not supported.

For the Xmega you need to use a constant for the baud rate. Variables are not supported. 

```
See also

[$CRYSTAL](crystal_1.md) , [$BAUD](baud_1.md) , [$BAUD1](_baud1.md) , [BAUD](baud_2.md), [CONFIG COMx](configcomx.md)

ASM

NONE

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega162

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates BAUD1 directive and BAUD1 statement

'-------------------------------------------------------------------------------

$regfile = "M162def.dat"

$baud1 = 2400

$crystal= 14000000 ' 14 MHz crystal

```
Open "COM2:" For BINARY As #1

```vb
Print #1 , "Hello"

'Now change the baud rate in a program

```
Baud1 = 9600 '

Print #1 , "Did you change the terminal emulator baud rate too?"

Close #1

End