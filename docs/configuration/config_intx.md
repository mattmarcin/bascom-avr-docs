# CONFIG INTx

Action

Configures the way the interrupts 0,1 and 4-7 will be triggered.

Syntax

CONFIG INTx = state

Where X can be 0,1 and 4 to 7 in the MEGA chips.

Remarks

state | LOW LEVEL to generate an interrupt while the pin is held low. Holding the pin low will generate an interrupt over and over again. FALLING to generate an interrupt on the falling edge. RISING to generate an interrupt on the rising edge. CHANGE to generate an interrupt on the change of the edge. Not all microprocessors support CHANGE.  
---|---  
  
The MEGA103 has also INT0-INT3. These are always low level triggered so there is no need /possibility for configuration.

The number of interrupt pins depend on the used chip. Most chips only have int0 and int1.

XMEGA

For the XMEGA you need to use [CONFIG XPIN](config_xpin.md).

Example

```vb
'-----------------------------------------------------------------------------------------

'name : spi-softslave.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to implement a SPI SLAVE with software

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'Some atmel chips like the 2313 do not have a SPI port.

'The BASCOM SPI routines are all master mode routines

'This example show how to create a slave using the 2313

'ISP slave code

'define the constants used by the SPI slave

```
Const _softslavespi_port = Portd ' we used portD

Const _softslavespi_pin = Pind 'we use the PIND register for reading

Const _softslavespi_ddr = Ddrd ' data direction of port D

Const _softslavespi_clock = 5 'pD.5 is used for the CLOCK

Const _softslavespi_miso = 3 'pD.3 is MISO

Const _softslavespi_mosi = 4 'pd.4 is MOSI

Const _softslavespi_ss = 2 ' pd.2 is SS

```vb
'while you may choose all pins you must use the INT0 pin for the SS

'for the 2313 this is pin 2

'PD.3(7), MISO must be output

'PD.4(8), MOSI

'Pd.5(9) , Clock

'PD.2(6), SS /INT0

'define the spi slave lib

$lib "spislave.lbx"

'sepcify wich routine to use

$external _spisoftslave

'we use the int0 interrupt to detect that our slave is addressed

On Int0 Isr_sspi Nosave

'we enable the int0 interrupt

Enable Int0

'we configure the INT0 interrupt to trigger when a falling edge is detected

Config Int0 = Falling

'finally we enabled interrupts

Enable Interrupts

'

Dim _ssspdr As Byte ' this is out SPI SLAVE SPDR register

Dim _ssspif As Bit ' SPI interrupt revceive bit

Dim Bsend As Byte , I As Byte , B As Byte ' some other demo variables

```
_ssspdr = 0 ' we send a 0 the first time the master sends data

```vb
Do

If _ssspif = 1 Then

Print "received: " ; _ssspdr

Reset _ssspif

```
_ssspdr = _ssspdr + 1 ' we send this the next time

```vb
End If

Loop

```