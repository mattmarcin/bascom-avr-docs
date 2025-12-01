# $BAUD1

Action

Instruct the compiler to set the baud rate for the second hardware UART.

Syntax

$BAUD1 = var

Remarks

Var | The baud rate that you want to use. This must be a numeric constant.  
---|---  
  
In the generated report, you can view which baud rate is actually generated.

When you simulate a program you will not notice any problems when the baud rate is not set to the value you expected. In real hardware a wrong baud rate can give weird results on the terminal emulator screen. For best results use a crystal that is a multiple of the baud rate.

Some AVR chips have 2 UARTS. For example the Mega161, Mega162, Mega103 and Mega128. There are several other's and some new chips even have 4 UARTS.

In the simulator you need to select the UART1-TAB to view the output of the UART1, or to send data to this UART.

See also

[$CRYSTAL](crystal_1.md) , [BAUD](baud_2.md) , [$BAUD](baud_1.md)

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

$hwstack = 32

$swstack = 8

$framesize = 24

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