# CONFIG COM1

Action

Configures the UART of AVR chips that have an extended UART like the M8.

Syntax

CONFIG COM1 = baud , synchrone=0|1,parity=none|disabled|even|odd,stopbits=1|2,databits=4|6|7|8|9,clockpol=0|1 

Remarks

baud | Baud rate to use. Use 'dummy' to leave the baud rate at the $baud value.  
---|---  
synchrone | 0 for asynchrone operation (default) and 1 for synchrone operation.  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 4,5,7,8 or 9.  
Clockpol | Clock polarity. 0 or 1.  
  
![notice](notice.jpg)Note that not all AVR chips have the extended UART. Most AVR chips have a UART with fixed communication parameters. These are : No parity, 1 stop bit, 8 data bits.

Normally you set the BAUD rate with $BAUD or at run time with BAUD. You may also set the baud rate when you open the COM channel. It is intended for the Mega2560 that has 4 UARTS and it is simpler to specify the baud rate when you open the channel. It may also be used with the first and second UART but it will generate additional code since using the first UART will always result in generating BAUD rate init code. 

See Also

[CONFIG COM2](config_com1.md) , [CONFIG COMx](configcomx.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M128 support in M128 mode

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$baud1 = 19200

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'By default the M128 has the M103 compatibility fuse set. Set the fuse to M128

'It also runs on a 1 MHz internal oscillator by default

'Set the internal osc to 4 MHz for this example DCBA=1100

'use the m128def.dat file when you wanto to use the M128 in M128 mode

'The M128 mode will use memory from $60-$9F for the extended registers

'Since some ports are located in extended registers it means that some statements

'will not work on these ports. Especially statements that will set or reset a bit

'in a register. You can set any bit yourself with the PORTF.1=1 statement for example

'But the I2C routines use ASM instructions to set the bit of a port. These ASM instructions may

'only be used on port registers. PORTF and PORTG will not work with I2C.

'The M128 has an extended UART.

'when CONFIG COMx is not used, the default N,8,1 will be used

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'try the second hardware UART

```
Open "com2:" For Binary As #1

```vb
'try to access an extended register

Config Portf = Output

'Config Portf = Input

Print "Hello"

Dim B As Byte

Do

Input "test serial port 0" , B

Print B

Print #1 , "test serial port 2"

Loop

```
Close #1

End