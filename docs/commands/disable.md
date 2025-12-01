# DISABLE

Action

Disable specified interrupt.

Syntax

DISABLE interrupt [device]

Remarks

Interrupt | Description  
---|---  
INT0 | External Interrupt 0  
INT1 | External Interrupt 1  
OVF0,TIMER0, COUNTER0 | TIMER0 overflow interrupt  
OVF1,TIMER1, COUNTER1 | TIMER1 overflow interrupt  
CAPTURE1, ICP1 | INPUT CAPTURE TIMER1 interrupt  
COMPARE1A,OC1A | TIMER1 OUTPUT COMPARE A interrupt  
COMPARE1B,OC1B | TIMER1 OUTPUT COMPARE B interrupt  
SPI | SPI interrupt  
URXC | Serial RX complete interrupt  
UDRE | Serial data register empty interrupt  
UTXC | Serial TX complete interrupt  
SERIAL | Disables URXC, UDRE and UTXC  
ACI | Analog comparator interrupt  
ADC | A/D converter interrupt  
  
By default all interrupts are disabled.

To disable all interrupts specify INTERRUPTS.

To enable the enabling and disabling of individual interrupts use ENABLE INTERRUPTS.

The ENABLE INTERRUPTS serves as a master switch. It must be enabled/set in order for the individual interrupts to work.

The interrupts that are available will depend on the used microprocessor. The available interrupts are shown automatically in the editor.

![notice](notice.jpg) To disable the JTAG you can use DISABLED JTAG. The JTAG is not an interrupt but a device.

XTINY/MEGAX/AVRX

The newest processors can configure each pin of a port. This is done using the CONFIG XPIN statement.

The sense parameter controls how the pin is used :

INT_DISABLED : no interrupt will occur but input buffer is enabled

BOTH : on a rising or falling edge an interrupt will occur

RISING : a rising edge will trigger an interrupt

FALLING : a falling edge will trigger an interrupt

INP_DISABLED : input and digital input buffer are disabled

LOW_LEVEL : interrupt will occur on a low level

So instead of using ENABLE you need to use CONFIG XPIN and select the proper trigger mode.

Instead of DISABLE you need to use CONFIG XPIN and select INT_DISABLED for the sense mode.

See also

[ENABLE](enable.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : serint.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : serial interrupt example for AVR

'micro : 90S8535

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8535def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

```
Const Cmaxchar = 20 ' number of characters

```vb
Dim B As Bit ' a flag for signalling a received character

Dim Bc As Byte ' byte counter

Dim Buf As String * Cmaxchar ' serial buffer

Dim D As Byte

'Buf = Space(20)

'unremark line above for the MID() function in the ISR

'we need to fill the buffer with spaces otherwise it will contain garbage

Print "Start"

On Urxc Rec_isr ' define serial receive ISR

Enable Urxc ' enable receive isr

Enable Interrupts ' enable interrupts to occur

Do

If B = 1 Then ' we received something

Disable Serial

Print Buf ' print buffer

Print Bc ' print character counter

'now check for buffer full

If Bc = Cmaxchar Then ' buffer full

```
Buf = "" ' clear

Bc = 0 ' rest character counter

```vb
End If

Reset B ' reset receive flag

Enable Serial

End If

Loop

```
Rec_isr:

```vb
Print "*"

If Bc < Cmaxchar Then ' does it fit into the buffer?

```
Incr Bc ' increase buffer counter

If Udr = 13 Then ' return?

Buf = Buf + Chr(0)

Bc = Cmaxchar

Else

Buf = Buf + Chr(udr) ' add to buffer

```vb
End If

' Mid(buf , Bc , 1) = Udr

'unremark line above and remark the line with Chr() to place

'the character into a certain position

'B = 1 ' set flag

End If

```
B = 1 ' set flag

Return