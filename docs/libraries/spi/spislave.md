# SPISLAVE

SPISLAVE.LIB (LBX) is a library that can be used to create a SPI slave chip when the chip does not have a hardware SPI interface.

Although most AVR chips have an ISP interface to program the chip, the 2313 for example does not have a SPI interface.

When you want to control various microâs with the SPI protocol you can use the SPISLAVE library.

The SPI-softslave.bas sample from the samples directory shows how you can use the SPISLAVE library.

Also look at the spi-slave.bas sample that is intended to be used with hardware SPI.

The sendspi.bas sample from the samples directory shows how you can use the SPI hardware interface for the master controller chip.

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
When the chip has a SPI interface, you can also use the following example:

```vb
'-----------------------------------------------------------------------------------------

'name : spi-slave.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to create a SPI SLAVE

'micro : AT90S8515

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8515def.dat" ' specify the used micro

$crystal = 3680000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

' use together with sendspi.bas

'------------------------------------------------------------------

' Tested on the STK500. The STK200 will NOT work.

' Use the STK500 or another circuit

Dim B As Byte , Rbit As Bit , Bsend As Byte

'First configure the MISO pin

Config Pinb.6 = Output ' MISO

'Then configure the SPI hardware SPCR register

Config Spi = Hard , Interrupt = On , Data Order = Msb , Master = No , Polarity = Low , Phase = 0 , Clockrate = 128

'Then init the SPI pins directly after the CONFIG SPI statement.

```
Spiinit

```vb
'specify the SPI interrupt

On Spi Spi_isr Nosave

'enable global interrupts

Enable Interrupts

'show that we started

Print "start"

```
Spdr = 0 ' start with sending 0 the first time

```vb
Do

If Rbit = 1 Then

Print "received : " ; B

Reset Rbit

```
Bsend = Bsend + 1 : Spdr = Bsend 'increase SPDR

```vb
End If

' your code goes here

Loop

'Interrupt routine

'since we used NOSAVE, we must save and restore the registers ourself

'when this ISR is called it will send the content from SPDR to the master

'the first time this is 0

```
Spi_isr:

push r24 ; save used register

in r24,sreg ; save sreg

push r24

B = Spdr

Set Rbit ' we received something

pop r24

!out sreg,r24 ; restore sreg

pop r24 ; and the used register

Return ' this will generate a reti