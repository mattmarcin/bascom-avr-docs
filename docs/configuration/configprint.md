# CONFIG PRINT

Action

Configure the UART to be used for RS-485

Syntax

```vb
CONFIG PRINT0 = pin, mode = mode [, delay=ms]

CONFIG PRINT1 = pin, mode = mode [, delay=ms]

CONFIG PRINT2 = pin, mode = mode [, delay=ms]

CONFIG PRINT3 = pin, mode = mode [, delay=ms]

CONFIG PRINT4 = pin, mode = mode [, delay=ms]

CONFIG PRINT5 = pin, mode = mode [, delay=ms]

CONFIG PRINT6 = pin, mode = mode [, delay=ms]

CONFIG PRINT7 = pin, mode = mode [, delay=ms]

```
Remarks

pin | The name of the PORT pin that is used to control the direction of an RS-485 driver such as PORTB.1  
---|---  
mode | SET or RESET  
delay | Optional delay in mS. This delay is used before the direction is switched back after the transmit buffer is empty. This to compensate for slow RS485 drivers.  
  
Use PRINT or PRINT0 for the first serial port. Use PRINT1 for the second serial port. PRINT2 for the third UART and PRINT3 for the fourth UART.

When you use RS-485 half duplex communication you need a pin for the direction of the data. The CONFIG PRINT automates the manual setting/resetting. It will either SET or RESET the logic level of the specified pin before data is printed with the BASCOM print routines. After the data is sent, it will inverse the pin so it goes into receive mode.

![notice](notice.jpg)You need to set the direction of the used pin to output mode yourself.

When CONFIG PRINT is used, the PRINT and PRINTBIN statements will switch the pin logic level, send the data, wait till all data is sent, optional wait the specified time in mS, and then will switch the pin logic level back.

```vb
CONFIG PRINT will not work with dynamic Xmega UARTS (BUART). You need to use a constant channel with the Xmega like PRINTBIN #1.

CONFIG PRINT does not work with buffered serial output. 

```
A popular line driver for RS485 communication is the MAX485. But most driver chips are similar. 

The driver usually has an /RE pin (/ means inverted) which need to be made low in order to enable the receiver. 

The driver also has a DE pin. Which is the driver output enable. This pin is not inverted. You need to make it high in order to enable the data driver output.

So when using the MAX485 as a master in half duplex mode to send data as in the example below, you would connect portb.0 to the DE pin. And you would use SET in the configuration since in order to print the driver must be SET high.

See also

[CONFIG PRINTBIN](config_printbin.md)

Example

```vb
'------------------------------------------------------------------------------

'name : rs485.bas

'copyright : (c) 1995-2054, MCS Electronics

'purpose : demonstrates

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'------------------------------------------------------------------------------

$regfile = "m48def.dat" ' we use the M48

$crystal = 8000000

$baud = 19200

$hwstack = 32

$swstack = 32

$framesize = 32

Config Print0 = Portb.0 , Mode = Set

Config Pinb.0 = Output 'set the direction yourself

Dim Resp As String * 10

Do

Print "test message"

Input Resp ' get response

Loop

```