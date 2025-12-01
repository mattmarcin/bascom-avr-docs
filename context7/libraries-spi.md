# SPI Libraries

> SPI communication protocol

## CmdSpinner

Action

Start an animated spinner.

Syntax

CmdSpinner x, y, style, range

Remarks

x | The X coordinate of top left of spinner  
---|---  
y | The Y coordinate of top left of spinner  
style | The style of spinner. Valid range is from 0 to 3  
range | The scaling coefficient of spinner. 0 means no scaling  
  
The spinner is an animated overlay that shows the user that some task is continuing. To trigger the spinner, create a display list and then use CMD_SPINNER. The co-processor engine overlays the spinner on the current display list, swaps the display list to make it 

visible, then continuously animates until it receives CMD_STOP. REG_MACRO_0 and REG_MACRO_1 registers are utilized to perform the animation kind of effect. The frequency of points movement is with respect to the display frame rate configured. 

Typically for 480x272 display panels the display rate is ~60fps. 

```vb
For style 0 and 60fps the point repeats the sequence within 2 seconds. 

For style 1 and 60fps the point repeats the sequence within 1.25 seconds. 

For style 2 and 60fps the clock hand repeats the sequence within 2 seconds. 

For style 3 and 60fps the moving dots repeat the sequence within 1 second.

```
Note that only one of [CmdSketch](cmdsketch.md), [CmdScreenSaver](cmdscreensaver.md) or [CmdSpinner](cmdspinner.md) can be active at one time.

Example

```vb
' Pseudocode

' Create a display list, then start the spinner

```
Clear_B 1,1,1

CmdText 80, 30, 27, OPT_CENTER, "Please wait..."

CmdSpinner 80, 60, 0, 0

![clip0056](clip0056.png)

' Spinner style 0, a circle of dots

CmdSpinner 80, 60, 0, 0

![clip0057](clip0057.png)

' Style 1, a line of dots

CmdSpinner 80, 60, 1, 0

![clip0058](clip0058.png)

' Style 2, a rotating clock hand

CmdSpinner 80, 60, 2, 0

![clip0059](clip0059.png)

' Style 3, two orbiting dots

CmdSpinner 80, 60, 3, 0

![clip0060](clip0060.png)

' Half screen, scale 1

CmdSpinner 80, 60, 0, 1

![clip0061](clip0061.png)

' Full screen, scale 2

CmdSpinner 80, 60, 0, 2

![clip0062](clip0062.png)

---

## How to add another SPI device with the FT800

Bascom continuously Streams Data to the SPI bus trying to minimize additional commands sent over the SPI bus by taking advantage of some the the FT800 capabilities. Because of method used you have to be aware you can just add another SPI device and just let your micro talk to it.

What happens here, is that the CHIP Select line is held LOW for most of the time (depending on what code the Bascom FT800 is running at the time), if another SPI device wants to communicate with that micro then the data from that device will also be sent to the FT800 which means that you will get unexpected results!.

Wait, don't fear, here is some example code to show you how it can be done easily.

Our friend is Endtransfer

In the example below AVR-DOS needs to enable the Chip Select to do it's job (reading/writing), before doing so you have to call Endtransfer which tells the Micro to Set the Chip Select line to the FT800.

Note: The Chip Select line for the FT800 should/will automatically Reset next time it has to execute commands.

```vb
'-------------------------------------------------------------------------------------------  
Sub LoadJpeg( Byval file As Byte)  
'-------------------------------------------------------------------------------------------  
' API's used to upload the image to GRAM from SD card  
  
```
Local fsize As Dword  
Local BlockLen As Word, Ptr1 As Word, Ptr2 As Word, Ptr3 As Word  
  
Endtransfer '<\--------  
Open imagename(file) for Binary as #1  
  
fsize = Lof(1)  
  
Ptr1 = 1 ' Start at the first byte  
BlockLen = Chunk  
```vb
While fsize > 0  
If fsize > Chunk Then BlockLen = Chunk Else BlockLen = fsize  
```
fsize = fsize - BlockLen  
Endtransfer '<\--------  
Get #1, Dat, Ptr1, BlockLen  
  
ALign4 BlockLen  
  
Ptr2 = BlockLen  
Ptr3 = _base  
  
While Ptr2 > 0  
Cmd8 aDat(Ptr3)  
Incr Ptr3  
Decr Ptr2  
Wend  
  
EndTransfer '<\--------  
WaitCmdFifoEmpty  
  
Ptr1 = Ptr1 + BlockLen  
Wend  
Close #1  
  
End Sub ' LoadJpeg

---

## SPI



---

## SPI1INIT, SPI1IN, SPI1OUT, SPI1MOVE

Some of the new MEGA processors like ATMEGA328PB have a second SPI bus. This is not a USART that can work in SPI mode but a full SPI bus.

In order to use the second SPI which is named SPI1, you have to add a '1' to the SPI commands :

[CONFIG SPI1 ](config_spi.md)

[SPI1INIT](spiinit.md)

[SPI1IN](spiin.md)

[SPI1OUT](spiout.md)

[SPI1MOVE](spimove.md)

The statements above link to the description of the SPI statements (SPI0). 

  
```vb
'in this demo we only use the second SPI interface  
Config Spi1 = Hard , Interrupt = Off , Data_order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 128  
  
'second SPI  
```
Spi1init  
B = 5  
Spi1out A(1) , B  
Spi1in A(1) , B  
A(1) = Spi1move(a(2))  
  
  
Some XTINY processors also have a second SPI bus. They also support the BASCOM SPI commands.

---

## SPIIN

Action  
  
Reads a value from the SPI-bus.

Syntax

SPIIN var, bytes

Syntax SPI1

SPI1IN var, bytes 

Remarks

Var | The variable which receives the value read from the SPI-bus.  
---|---  
Bytes | The number of bytes to read. The maximum is 255.  
  
In order to be able to read data from the SPI slave, the master need to send some data first. The master will send the value 0.

SPI is a 16 bit shift register. Thus writing 1 byte will cause 1 byte to be clocked out of the device which the SPIIN will read.

SPIIN always work on the first SPI interface (SPI0)

SPI1IN works on the second SPI interface (SPI1)

See also

[SPIOUT](spiout.md), [SPIINIT](spiinit.md), [CONFIG SPI](config_spi.md) , [SPIMOVE](spimove.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : spi.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo :SPI

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

Dim A(10) As Byte

```
Spiinit

B = 5

Spiout A(1) , B

Spiin A(1) , B

A(1) = Spimove(a(2))

End

---

## SPIINIT

Action

Initiate the SPI pins.

Syntax

SPIINIT

Syntax SPI1

SPI1INIT

Remarks

After the configuration of the SPI pins, you must initialize the SPI pins to set them for the right data direction. When the pins are not used by other hardware/software, you only need to use SPIINIT once.

When the SPI bus is used in master mode, the MOSI, CLOCK and SS pins will be set to output. 

When the SPI bus is used in slave mode, the MISO is set to output mode.

If you need to change the logic levels of the SPI pins, you need to disable the SPI. You can do this by setting the SPE bit to 0 in SPCR.

When other routines change the state of the SPI pins, use SPIINIT again before using SPIIN and SPIOUT.

SPIINIT is only required for normal AVR. Xmega and Xtiny do not require this statement. 

SPIINIT always work on the first SPI interface (SPI0)

SPI1INIT works on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIOUT](spiout.md), [config spi](config_spi.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

ASM

Calls _init_spi

Example

See [SPIIN](spiin.md)

---

## SPIMOVE

Action

Sends and receives a value or a variable to the SPI-bus.

Syntax

var = SPIMOVE( source [,count] )

Syntax Xmega

var = SPIMOVE( source ,count , channel )

Syntax SPI1

var = SPI1MOVE( source [,count] )

Remarks

Var | The variable that is assigned with the received byte(s) from the SPI-bus.  
---|---  
Source | The variable or constant whose content must be send to the SPI-bus.  
Count | Optional byte value which specifies how many bytes need to be moved. Notice that for Xmega this parameter is not optional but mandatory.  
Channel | For Xmega only : the channel number or channel variable  
  
SPIMOVE always work on the first SPI interface (SPI0)

SPI1MOVE works on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIINIT](spiinit.md) , [CONFIG SPI](config_spi.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = Portb.2 , Clock = Portb.3

Spiinit

Dim a(10) as Byte , X As Byte

Spiout A(1) , 5 'send 5 bytes

Spiout X , 1 'send 1 byte

A(1) = Spimove(5) ' move 5 to SPI and store result in a(1)

A(1) = Spimove(a(2),4) ' move 4 bytes from a(2) to a(1)

End

Example Xmega

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1_SPI_MOVE.bas  
' This sample demonstrates the Xmega128A1 SPI master mode SPIMOVE  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz '--> 32MHz  
  
  
Config Com1 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Waitms 2  
```
Open "COM1:" For Binary As #1  
```vb
Print #1 ,  
Print #1 , "------------SPI MASTER-Slave Test----------------"  
  
' Master = ATXMEGA128A1 running at 3.3 Volt  
' Slave = ATMEGA328P running at 3.3 Volt  
  
'We use Port E for SPI  
'Ddre = &B1011_0000  
'Bit7 = SCK = Output ------> SCK ATMEGA328P (PinB.5)  
'Bit6 = MISO = Input ------> MISO ATMEGA328P (PinB.4)  
'Bit5 = MOSI = Output ------> MOSI ATMEGA328P (PinB.3)  
'Bit4 = SS = Output ------> SS ATMEGA328P (PinB.2)  
```
Slave_select Alias Porte.4  
```vb
Set Slave_select  
  
Dim Switch_bit As Bit  
  
```
Switch Alias Pine.0 ' Switch connected to GND  
```vb
Config Xpin = Porte.0 , Outpull = Pullup  
  
  
  
Dim Bspivar As Byte  
Dim Spi_send_byte As Byte  
Dim Spi_receive_byte As Byte  
Dim Ar(4) As Byte  
  
  
'SPI, Master|Slave , MODE, clock division  
Config Spie = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk32 , Data_order = Msb , Ss = Auto  
'SS = Auto set the Slave Select (SS) automatically before a print #X or input #X command (including initialization of the pin)  
'Master SPI clock = 1MHz  
```
Open "SPIE" For Binary As #12  
  
  
```vb
Config Debounce = 50  
  
Do  
  
```
Debounce Switch , 0 , Switch_sub , Sub 'Switch Debouncing  
  
```vb
If Switch_bit = 1 Then 'When Switch pressed  
Reset Switch_bit  
  
```
Incr Spi_send_byte  
```vb
Print "Spi_send_byte = " ; Spi_send_byte  
  
'SEND TO SLAVE  
Print #12 , Spi_send_byte 'SEND ONE BYTE TO SLAVE  
  
Waitms 3  
  
'READ FROM SLAVE  
Input #12 , Spi_receive_byte 'READ ONE BYTE FROM SLAVE  
  
Print #1 , "Spi_receive_byte = " ; Spi_receive_byte  
  
'Lets move some bytes  
```
Ar(1) = Spimove(ar(1) , 4 , #12)  
```vb
End If  
  
  
Loop  
  
  
  
End 'end program  
  
'there is NO CLOSE for SPI  
  
  
```
Switch_sub:  
```vb
Set Switch_bit  
Return

```

---

## SPIOUT

Action

Sends a value of a variable to the SPI-bus.

Syntax

SPIOUT var , bytes

Syntax SPI1

SPI1OUT var , bytes

Remarks

var | The variable whose content must be send to the SPI-bus.  
---|---  
bytes | The number of bytes to send. Maximum value is 255.  
  
When SPI is used in HW(hardware) mode, there might be a small delay/pause after each byte that is sent. This is caused by the SPI hardware and the speed of the bus. After a byte is transmitted, SPSR bit 7 is checked. This bit 7 indicates that the SPI is ready for sending a new byte.

SPIOUT will always work on the first SPI interface (SPI0).

SPI1OUT will work on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIINIT](spiinit.md) , [CONFIG SPI](config_spi.md) , [SPIMOVE](spimove.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

```vb
Dim A(10) As Byte

Config Spi = Soft , Din =Pinb.0 , Dout =Portb.1 , Ss =Portb.2 , Clock =Portb.3

```
Spiinit

Spiout A(1), 4 'write 4 bytes a(1), a(2) , a(3) and a(4)

End

---

## SPISLAVE

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

---

## Using the SPI protocol

General description of the SPI

The SPI allows high-speed synchronous data transfer between the AVR and peripheral devices or between several AVR devices. On most parts the SPI has a second purpose where it is used for In System Programming (ISP).

The interconnection between two SPI devices always happens between a master device and a slave device. Compared to some peripheral devices like sensors which can only run in slave mode, the SPI of the AVR can be configured for both master and slave mode.

The mode the AVR is running in is specified by the settings of the master bit (MSTR) in the SPI control register (SPCR).

Special considerations about the /SS pin have to be taken into account. This will be described later in the section "Multi Slave Systems - /SS pin Functionality".

The master is the active part in this system and has to provide the clock signal a serial data transmission is based on. The slave is not capable of generating the clock signal and thus can not get active on its own.

The slave just sends and receives data if the master generates the necessary clock signal. The master however generates the clock signal only while sending data. That means that the master has to send data to the slave to read data from the slave.

![hardware_SPI_mstrslave](hardware_spi_mstrslave.jpg)

Data transmission between Master and Slave

The interaction between a master and a slave AVR is shown in Figure 1. Two identical SPI units are displayed. The left unit is configured as master while the right unit is configured as slave. The MISO, MOSI and SCK lines are connected with the corresponding lines of the other part.

The mode in which a part is running determines if they are input or output signal lines. Because a bit is shifted from the master to the slave and from the slave to the master simultaneously in one clock cycle both 8-bit shift registers can be considered as one 16-bit circular shift register. This means that after eight SCK clock pulses the data between master and slave will be exchanged.

The system is single buffered in the transmit direction and double buffered in the receive direction. This influences the data handling in the following ways:

1\. New bytes to be sent can not be written to the data register (SPDR) / shift register before the entire shift cycle is completed.

2\. Received bytes are written to the Receive Buffer immediately after the transmission is completed.

3\. The Receive Buffer has to be read before the next transmission is completed or data will be lost.

4\. Reading the SPDR will return the data of the Receive Buffer.

After a transfer is completed the SPI Interrupt Flag (SPIF) will be set in the SPI Status Register (SPSR). This will cause the corresponding interrupt to be executed if this interrupt and the global interrupts are enabled. Setting the SPI Interrupt Enable (SPIE) bit in the SPCR enables the interrupt of the SPI while setting the I bit in the SREG enables the global interrupts.

Pins of the SPI

The SPI consists of four different signal lines. These lines are the shift clock (SCK), the Master Out Slave In line (MOSI), the Master In Slave Out line (MISO) and the active low Slave Select line (/SS). When the SPI is enabled, the data direction of the MOSI, MISO, SCK and /SS pins are overridden according to the following table.

Table 1. SPI Pin Overrides

Pin Direction Overrides | Master SPI Mode Direction Overrides | Slave SPI Modes  
---|---|---  
MOSI | User Defined | Input  
MISO | Input | User Defined  
SCK | User Defined | Input  
SS | User Defined | Input  
  
This table shows that just the input pins are automatically configured. The output pins have to be initialized manually by software. The reason for this is to avoid damages e.g. through driver contention.

Multi Slave Systems - /SS pin Functionality

The Slave Select (/SS) pin plays a central role in the SPI configuration. Depending on the mode the part is running in and the configuration of this pin, it can be used to activate or deactivate the devices. The /SS pin can be compared with a chip select pin which has some extra features. In master mode, the /SS pin must be held high to ensure master SPI operation if this pin is configured as an input pin. A low level will switch the SPI into slave mode and the hardware of the SPI will perform the following actions:

1\. The master bit (MSTR) in the SPI Control Register (SPCR) is cleared and the SPI system becomes a slave. The direction of the pins will be switched according to Table 1.

2\. The SPI Interrupt Flag (SPIF) in the SPI Status Register (SPSR) will be set. If the SPI interrupt and the global interrupts are enabled the interrupt routine will be executed. This can be useful in systems with more than one master to avoid that two masters are accessing the SPI bus at the same time. If the /SS pin is configured as output pin it can be used as a general purpose output pin which does not affect the SPI system.

Note: In cases where the AVR is configured for master mode and it can not be ensured that the /SS pin will stay high between two transmissions, the status of the MSTR bit has to be checked before a new byte is written. Once the MSTR bit has been cleared by a low level on the /SS line, it must be set by the application to re-enable SPI master mode.

In slave mode the /SS pin is always an input. When /SS is held low, the SPI is activated and MISO becomes output if configured so by the user. All other pins are inputs. When /SS is driven high, all pins are inputs, and the SPI is passive, which means that it will not receive incoming data.

Table 2 shows an overview of the /SS Pin Functionality.

Note: In slave mode, the SPI logic will be reset once the /SS pin is brought high. If the /SS pin is brought high during a transmission, the SPI will stop sending and receiving immediately and both data received and data sent must be considered as lost.

TABLE 2. Overview of SS pin.

Mode | /SS Config | /SS Pin level | Description  
---|---|---|---  
Slave | Always input | High | Slave deactivated  
Low | Slave activated  
Master | Input | High | Master activated  
Low | Master deactivated  
Output | High | Master activated  
Low  
  
As shown in Table 2, the /SS pin in slave mode is always an input pin. A low level activates the SPI of the device while a high level causes its deactivation. A Single Master Multiple Slave System with an AVR configured in master mode and /SS configured as output pin is shown in Figure 2. The amount of slaves, which can be connected to this AVR is only limited by the number of I/O pins to generate the slave select signals.

![hardware_SPI_multislave](hardware_spi_multislave.gif)

The ability to connect several devices to the same SPI-bus is based on the fact that only one master and only one slave is active at the same time. The MISO, MOSI and SCK lines of all the other slaves are tri stated (configured as input pins of a high impedance with no pull up resistors enabled). A false implementation (e.g. if two slaves are activated at the same time) can cause a driver contention which can lead to a CMOS latch up state and must be avoided. Resistances of 1 to 10 k ohms in series with the pins of the SPI can be used to prevent the system from latching up. However this affects the maximum usable data rate, depending on the loading capacitance on the SPI pins.

Unidirectional SPI devices require just the clock line and one of the data lines. If the device is using the MISO line or the MOSI line depends on its purpose. Simple sensors for instance are just sending data (see S2 in Figure 2), while an external DAC usually just receives data (see S3 in Figure 2).

SPI Timing

The SPI has four modes of operation, 0 through 3. These modes essentially control the way data is clocked in or out of an SPI device. The configuration is done by two bits in the SPI control register (SPCR). The clock polarity is specified by the CPOL control bit, which selects an active high or active low clock. The clock phase (CPHA) control bit selects one of the two fundamentally different transfer formats. To ensure a proper communication between master and slave both devices have to run in the same mode. This can require a reconfiguration of the master to match the requirements of different peripheral slaves.

The settings of CPOL and CPHA specify the different SPI modes, shown in Table 3. Because this is no standard and specified different in other literature, the configuration of the SPI has to be done carefully.

Table 3. SPI Mode configuration

SPI Mode | CPOL | CPHA | Shift SCK edge | Capture SCK edge  
---|---|---|---|---  
0 | 0 | 0 | Falling | Rising  
1 | 0 | 1 | Rising | Falling  
2 | 1 | 0 | Rising | Falling  
3 | 1 | 1 | Falling | Rising  
  
The clock polarity has no significant effect on the transfer format. Switching this bit causes the clock signal to be inverted (active high becomes active low and idle low becomes idle high). The settings of the clock phase, how-ever, selects one of the two different transfer timings, which are described closer in the next two chapters. Since the MOSI and MISO lines of the master and the slave are directly connected to each other, the diagrams show the timing of both devices, master and slave. The /SS line is

the slave select input of the slave. The /SS pin of the master is not shown in the diagrams. It has to be inactive by a high level on this pin (if configured as input pin) or by configuring it as an output pin.

A.) CPHA = 0 and CPOL = 0 (Mode 0) and CPHA = 0 and CPOL = 1 (Mode 1)

The timing of a SPI transfer where CPHA is zero is shown in Figure 3. Two wave forms are shown for the SCK signal -one for CPOL equals zero and another for CPOL equals one.

![hardware_SPI_CPHA0](hardware_spi_cpha0.jpg)

When the SPI is configured as a slave, the transmission starts with the falling edge of the /SS line. This activates the SPI of the slave and the MSB of the byte stored in its data register (SPDR) is output on the MISO line. The actual transfer is started by a software write to the SPDR of the master. This causes the clock signal to be generated. In cases where the CPHA equals zero, the SCK signal remains zero for the first half of the first SCK cycle. This ensures that the data is stable on the input lines of both the master and the slave. The data on the input lines is read with the edge of the SCK line from its inactive to its active state (rising edge if CPOL equals zero and falling edge if CPOL equals one). The edge of the SCK line from its active to its inactive state (falling edge if CPOL equals zero and rising edge if CPOL equals one) causes the data to be shifted one bit further so that the next bit is output on the MOSI and MISO lines.

After eight clock pulses the transmission is completed. In both the master and the slave device the SPI interrupt flag (SPIF) is set and the received byte is transferred to the receive buffer.

B.) CPHA = 1 and CPOL = 0 (Mode 2) and CPHA = 1 and CPOL = 1 (Mode 3)

The timing of a SPI transfer where CPHA is one is shown in Figure 4. Two wave forms are shown for the SCK signal -one for CPOL equals zero and another for CPOL equals one.

![hardware_SPI_CPHA1](hardware_spi_cpha1.jpg)

Like in the previous cases the falling edge of the /SS lines selects and activates the slave. Compared to the previous cases, where CPHA equals zero, the transmission is not started and the MSB is not output by the slave at this stage. The actual transfer is started by a software write to the SPDR of the master what causes the clock signal to be generated. The first edge of the SCK signal from its inactive to its active state (rising edge if CPOL equals zero and falling edge if CPOL equals one) causes both the master and the slave to output the MSB of the byte in the SPDR.

As shown in Figure 4, there is no delay of half a SCK-cycle like in Mode 0 and 1. The SCK line changes its level immediately at the beginning of the first SCK-cycle. The data on the input lines is read with the edge of the SCK line from its active to its inactive state (falling edge if CPOL equals zero and rising edge if CPOL equals one).

Mode | Leading Edge | Trailing Edge  
---|---|---  
0 CPOL=0, CPHA=0 | Rising, Sample | Falling, Setup  
1 CPOL=0, CPHA=1 | Rising, Setup | Falling, Sample  
2 CPOL=1, CPHA=0 | Falling, Sample | Rising, Setup  
3 CPOL=1, CPHA=1 | Falling, Setup | Rising, Sample  
  
After eight clock pulses the transmission is completed. In both the master and the slave device the SPI interrupt flag (SPIF) is set and the received byte is transferred to the receive buffer.

Considerations for high speed transmissions

Parts which run at higher system clock frequencies and SPI modules capable of running at speed grades up to half the system clock require a more specific timing to match the needs of both the sender and receiver. The following two diagrams show the timing of the AVR in master and in slave mode for the SPI Modes 0 and 1. The exact values of the displayed times vary between the different pars and are not an issue in this application note. However the functionality of all parts is in principle the same so that the following considerations apply to all parts.

![ebx_732972804](ebx_732972804.gif)

The minimum timing of the clock signal is given by the times "1" and "2". The value "1" specifies the SCK period while the value "2" specifies the high / low times of the clock signal. The maximum rise and fall time of the SCK signal is specified by the time "3". These are the first timings of the AVR to check if they match the requirements of the slave.

The Setup time "4" and Hold time "5" are important times because they specify the requirements the AVR has on the interface of the slave. These times determine how long before the clock edge the slave has to have valid output data ready and how long after the clock edge this data has to be valid.

If the Setup and Hold time are long enough the slave suits to the requirements of the AVR but does the AVR suit to the requirements of the slave?

The time "6" (Out to SCK) specifies the minimum time the AVR has valid output data ready before the clock edge occurs. This time can be compared to the Setup time "4" of the slave.

The time "7" (SCK to Out) specifies the maximum time after which the AVR outputs the next data bit while the time "8" (SCK to Out high) the minimum time specifies during which the last data bit is valid on the MOSI line after the SCK was set back to its idle state.

![ebx_-87387816](ebx_-87387816.gif)

In principle the timings are the same in slave mode like previously described in master mode. Because of the switching of the roles between master and slave the requirements on the timing are inverted as well. The minimum times of the master mode are now maximum times and vice versa.

SPI Transmission Conflicts

A write collision occurs if the SPDR is written while a transfer is in progress. Since this register is just single buffered in the transmit direction, writing to SPDR causes data to be written directly into the SPI shift register. Because this write operation would corrupt the data of the current transfer, a write-collision error in generated by setting the WCOL bit in the SPSR. The write operation will not be executed in this case and the transfer continues undisturbed. A write collision is generally a slave error because a slave has no control over when a master will initiate a transfer. A master, however, knows when a transfer is in progress. Thus a master should not generate write collision errors, although the SPI logic can detect these errors in a master as well as in a slave mode.

When you set the SPI option from the Options, Compiler, SPI menu SPCR will be set to 01010100 which means ; enable SPI, master mode, CPOL = 1

When you want to control the various options with the hardware SPI you can use the [CONFIG SPI](config_spi.md) statement.

See also: [config SPI](config_spi.md), [Config SPIx](config_spix.md), [SPISLAVE](spislave.md), [SPIINIT](spiinit.md), [SPIOUT](spiout.md), [SPIIN](spiin.md), [Using USI (Universal Serial Interface)](using_usi_universal_serial_int.md)

---
