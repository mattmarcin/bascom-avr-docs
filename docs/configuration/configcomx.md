# CONFIG COMx

Action

Configures the UART of AVR chips that have an extended UART like the M2560.

Syntax

CONFIG COMx = baud , synchrone=0|1,parity=none|disabled|even|odd,stopbits=1|2,databits=4|6|7|8|9,clockpol=0|1

Syntax Xmega

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits

Syntax Xtiny/MegaX

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits , Baud_Offset=baud_ofs , TX_RX_XC_XD_PIN=tx, TX=tx,RX=rx

Syntax AVRX

CONFIG COMx = baud , Mode=mode, Parity=parity, Stopbits=stopbits, Databits=databits , TX_RX_XC_XD_PIN=tx, TX=tx,RX=rx

There is no baud offset in the AVRX series

Remarks normal AVR

COMx | The COM port to configure. Value in range from 1-4  
---|---  
baud | Baud rate to use.  
synchrone | 0 for asynchrone operation (default) and 1 for synchrone operation.  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 4,5,7,8 or 9.  
Clockpol | Clock polarity. 0 or 1.  
  
![notice](notice.jpg)Note that not all AVR chips have the extended UART. Most AVR chips have a UART with fixed communication parameters. These are : No parity, 1 stopbit, 8 data bits.

The Mega2560 does support 4 UART's.

Remarks Xmega

COMx | The COM port to configure. Value in range from 1-8  
---|---  
baud | Baud rate to use. If the baud rate can be generated accurately depends on the system clock.  
mode | The USART mode, this can be : \- ASYNCHRONEOUS or 0 (default) for asynchronous operation. \- SYNCHRONEOUS or 1 , for synchronous operation. \- IRDA or IRCOM for IRDA operation \- SPI or MSPI for operation as SPI controller * The mode must be provided since the baud calculation depends on the selected mode *  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 5,6,7,8 or 9.  
  
In the Xmega the registers have a fixed offset. This allows to use dynamic UARTS : you can change settings at run time by using a variable. This will use some more code when using just one UART but will save code when using multiple UARTS because you need only one copy of the code.

In the Xmega you MUST use CONFIG COM before you can use the UART. The CONFIG commands makes a call to _INIT_XMEGA_UART where the various parameters are passed to setup the UART. You also need to specify the baud rate. Do not use $BAUD.

The CLOCKPOL for the SPI mode has been removed, it will be added to a configuration command for the SPI.

The CONFIG COM will set the TX pin to output mode. This are the following pins :

UART | TX pin | RX pin | [BAUD](baud1.md)  
---|---|---|---  
COM1 - UART_C0 | PORTC.3 | PORTC.2 | BAUD  
COM2 - UART_C1 | PORTC.7 | PORTC.6 | BAUD1  
COM3 - UART_D0 | PORTD.3 | PORTD.2 | BAUD2  
COM4 - UART_D1 | PORTD.7 | PORTD.6 | BAUD3  
COM5 - UART_E0 | PORTE.3 | PORTE.2 | BAUD4  
COM6 - UART_E1 | PORTE.7 | PORTE.6 | BAUD5  
COM7 - UART_F0 | PORTF.3 | PORTF.2 | BAUD6  
COM8 - UART_F1 | PORTF.7 | PORTF.6 | BAUD7  
  
In IRDA mode, depending on the module you use, it might be necessary to invert the logic level of the TX pin with CONFIG XPIN. For example when COM1 is used for the IRDA module, you would use : CONFIG XPIN=PORTC.3, INVERTIO=ENABLED

Remarks XTINY/MEGAX/AVRX

COMx | The COM port to configure. Value in range from 1-6  
---|---  
baud | Baud rate to use. If the baud rate can be generated accurately depends on the system clock.  
mode | The USART mode, this can be : \- ASYNCHRONEOUS : (default) for asynchronous operation. \- SYNCHRONEOUS : for synchronous operation. \- IRCOM : for IRDA operation \- SPI : for operation as SPI controller * The mode must be provided since the baud calculation depends on the selected mode *  
Parity | None, disabled, even or odd  
Stopbits | The number of stop bits : 1 or 2  
Databits | The number of data bits : 5,6,7,8 or 9.  
Baud_offset | The Xtiny/MegaX has an internal oscillator that runs at 16 or 20 MHz. The center frequency can be off depending on temperature and voltage. The Xtiny has 4 calibrated offset values for the oscillator which can be used to correct the BAUD. The options are : \- NONE : default, BAUD is calculated but no offset is used. All of the other values will read the signature row and will call code from xtiny.lib to compensate the BAUD value. \- OSC16_3V3 : OSC runs at 16 MHz and at 3V3 \- OSC16_5V : OSC runs at 16 MHz and at 5V \- OSC20_3V3 : OSC runs at 20 MHz and at 3V3 \- OSC20_5V : OSC runs at 20 MHz and at 5V It is up to the user to apply the selected voltage. It is up to the user to use the specified oscillator value. (change fuse bits). By default the 20 MHz internal osc is selected. So this setting does not change oscillator values, it only tells the compiler which sigrow must be loaded and used.   
TX_RX_XC_XD_PIN  
  
This option was named TXPIN before | This options selects the pins used for the UART. The XTINY/MEGAX/AVRX has a port multiplexer. This multi plexer allows to chose which pins are used for hardware connected to the port pins.  So this allows to chose one or more alternative pin locations for hardware such as USART,SPI, TWI and TIMER output. You can use CONFIG PORT_MUX when you use alternative pin positions. But [CONFIG PORT_MUX](config_port_mux.md) does not set port direction.  For the USART it is required to set the TX pin into output mode.  That is why this option exists : you can chose the alternative pin location and the compiler will set the port pin into output mode and will set the proper port multiplexer register bit. You can chose between the default location starting with DEF_ and the alternative location starting with ALTx_ Some processors also allow to disconnect the pins totally and they have a NONE option. It is important to understand that selecting an alternative pin will switch all the pins of that hardware device. For the USART this means you will switch both TX, RX, XCK and XDIR pin. You can not just change only the TX or RX. You can however change the pins dynamically at run time. Your hardware circuit should support this of course.  Please note that you only should use this option when you use the alternative pin location since using this option create more code since the multiplexer is configured. The parameter value for TX_RX_XC_XD_PIN lists all associated pins in the following order : TX, RX, XCK, XDIR. For example : Def_pb2_pb3_pb1_pb0 which means that PortB.2 is connected to TX and RX is connected to PortB.3.  ALT1_PA1_PA2_PA3_PA4 means that the alternative pin is used which is PA1 for TX in this case.   
TX | By default both the transmitter and receiver are enabled. But there are cases where you only want to use the receiver. In such a case you can DISABLE the TX pin.  
TX=DISABLED. The default is enabled and there is no need to specify this. Possible options : ENABLED and DISABLED  
RX | By default both the transmitter and receiver are enabled. But there are cases where you only want to use the transmiiter. In such a case you can DISABLE the RX pin.  
RX=DISABLED. The default is enabled and there is no need to specify this. Possible options : ENABLED and DISABLED  
  
It is preferred to use CONFIG COM instead of using $BAUD.

![notice](notice.jpg)It is important that you specify all parameters of CONFIG COM. Do not omit one. The only optional parameter is TX_RX_XC_XD_PIN for the alternative USART pins, and the TX and RX options to disable pins.

See Also

[CONFIG COM1](config_com1.md) , [CONFIG COM2](config_com1.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name :

'copyright : (c) 1995-2025, MCS Electronics

'purpose : test for M2560 support

'micro : Mega2560

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m2560def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$hwstack = 40 ' default use 32 for the hardware stack

$swstack = 40 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'The M128 has an extended UART.

'when CO'NFIG COMx is not used, the default N,8,1 will be used

Config Com1 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com3 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Config Com4 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'Open all UARTS

```
Open "com2:" For Binary As #1

Open "Com3:" For Binary As #2

Open "Com4:" For Binary As #3

```vb
Print "Hello" 'first uart

Dim B As Byte

Dim Tel As Word

Do

```
Incr Tel

```vb
Print Tel ; " test serial port 1"

Print #1 , Tel ; " test serial port 2"

Print #2 , Tel ; " test serial port 3"

Print #3 , Tel ; " test serial port 4"

```
B = Inkey(#3)

```vb
If B <> 0 Then

Print #3 , B ; " from port 4"

End If

Waitms 500

Loop

```
Close #1

Close #2

Close #3

End

Xtiny Example

```vb
'--------------------------------------------------------------------------------  
'name : serial.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates USART  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
Config Sysclock = 16_20MHZ , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'dimension a variable  
Dim B As Byte  
  
Config PORTC.1 = Output  
Print "Test USART"  
  
Do  
Print "Hello" ; Spc(3) ; B  
Waitms 1000  
```
Incr B  
```vb
Toggle PORTC.1  
Loop  
  
  
End

```