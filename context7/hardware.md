# AVR Hardware

> AVR internal hardware documentation

## Additional Hardware

Of course just running a program on the chip is not enough. You will probably connect many types of electronic devices to the processor ports.

BASCOM supports a lot of hardware and so it has lots of hardware related statements.

Before explaining about programming the additional hardware, it might be better to talk about the chip.

[The AVR internal hardware](avr_internal_hardware.md)

[Attaching an LCD display](attaching_an_lcd_display.md)

[Using the I2C protocol](using_the_i2c_protocol.md)

[Using the 1WIRE protocol](using_the_1_wire_protocol.md)

[Using the SPI protocol](using_the_spi_protocol.md)

You can connect additional hardware to the ports of the microprocessor.

The following are hardware related:

[I2CSEND](i2csend.md) and [I2CRECEIVE](i2creceive.md) and other I2C related statements.

[CLS,](cls.md)[LCD,](lcd_2.md)[DISPLAY](display.md) and other related LCD-statements.

[1WRESET](1wreset.md) , [1WWRITE](1wwrite.md) and [1WREAD](1wread.md)

There are many more hardware specific statements and functions. 

[Adding XRAM](adding_xram.md)

[Adding XRAM to XMEGA using EBI](adding_xram_to_xmega_using_ebi.md)

[Adding SRAM 4-port Non Multiplexed](adding_sram_4_port_non_multipl.md)

[Using a BOOTLOADER](using_a_bootloader.md)

---

## AVR Internal Hardware

The AVR chips all have internal hardware that can be used.

For this description of the hardware the 90S8515 was used. Newer chips like the Mega8515 may differ and have more or less internal hardware.

You will need to read the manufacturers data sheet for the processor you are using to learn about the special internal hardware available.

Timer / Counters

The AT90S8515 provides two general purpose Timer/Counters - one 8-bit T/C and one 16-bit T/C. The Timer/Counters have individual pre-scaling selection from the same 10-bit pre-scaling timer. Both Timer/Counters can either be used as a timer with an internal clock time base or as a counter with an external pin connection which triggers the counting.

![basc0073](basc0073.jpg)

More about [TIMERO](avr_internal_hardware_timer0.md)

More about [TIMER1](avr_internal_hardware_timer1.md)

[The WATCHDOG Timer](avr_internal_hardware_watchdog_timer.md)

Almost all AVR chips have the ports B and D. The 40 or more pin devices also have ports A and C that also can be used for addressing an external RAM chip ([XRAM](adding_xram.md)). Since all ports are similar except that PORT B and PORT D have alternative functions, only these ports are described.

[PORT B](avr_internal_hardware_port_b.md)

[PORT D](avr_internal_hardware_port_d.md)

---

## AVR Internal Hardware Port B

Port B

Port B is an 8-bit bi-directional I/O port. Three data memory address locations are allocated for the Port B, one each for the Data Register - PORTB, $18($38), Data Direction Register - DDRB, $17($37) and the Port B Input Pins - PINB, $16($36). The Port B Input Pins address is read only, while the Data Register and the Data Direction Register are read/write.

All port pins have individually selectable pull-up resistors. The Port B output buffers can sink 20mA and thus drive LED displays directly. When pins PB0 to PB7 are used as inputs and are externally pulled low, they will source current if the internal pull-up resistors are activated.

The Port B pins with alternate functions are shown in the following table:

When the pins are used for the alternate function the DDRB and PORTB register has to be set according to the alternate function description.

Port B Pins Alternate Functions

Port | Pin | Alternate Functions  
---|---|---  
PORTB.0 | T0 | (Timer/Counter 0 external counter input)  
PORTB.1 | T1 | (Timer/Counter 1 external counter input)  
PORTB.2 | AIN0 | (Analog comparator positive input)  
PORTB.3 | AIN1 | (Analog comparator negative input)  
PORTB.4 | SS | (SPI Slave Select input)  
PORTB.5 | MOSI | (SPI Bus Master Output/Slave Input)  
PORTB.6 | MISO | (SPI Bus Master Input/Slave Output)  
PORTB.7 | SCK | (SPI Bus Serial Clock)  
  
The Port B Input Pins address - PINB - is not a register, and this address enables access to the physical value on each Port B pin. When reading PORTB, the PORTB Data Latch is read, and when reading PINB, the logical values present on the pins are read.

PortB As General Digital I/O

All 8 bits in port B are equal when used as digital I/O pins. PORTB.X, General I/O pin: The DDBn bit in the DDRB register selects the direction of this pin, if DDBn is set (one), PBn is configured as an output pin. If DDBn is cleared (zero), PBn is configured as an input pin. If PORTBn is set (one) when the pin configured as an input pin, the MOS pull up resistor is activated.

To switch the pull up resistor off, the PORTBn has to be cleared (zero) or the pin has to be configured as an output pin.

DDBn Effects on Port B Pins

DDBn | PORTBn | I/O | Pull up | Comment  
---|---|---|---|---  
0 | 0 | Input | No | Tri-state (Hi-Z)  
0 | 1 | Input | Yes | PBn will source current if ext. pulled low.  
1 | 0 | Output | No | Push-Pull Zero Output  
1 | 1 | Output | No | Push-Pull One Output  
  
By default, the DDR and PORT registers are 0. CONFIG PORTx=OUTPUT will set the entire DDR register. CONFIG PINX.Y will also set the DDR register for a single bit/pin. When you need the pull up to be activated, you have to write to the PORT register.

---

## AVR Internal Hardware Port D

Port D

Port D Pins Alternate Functions

Port | Pin | Alternate Function  
---|---|---  
PORTD.0 | RDX | (UART Input line )  
PORTD.1 | TDX | (UART Output line)  
PORTD.2 | INT0 | (External interrupt 0 input)  
PORTD.3 | INT1 | (External interrupt 1 input)  
PORTD.5 | OC1A | (Timer/Counter1 Output compareA match output)  
PORTD.6 | WR | (Write strobe to external memory)  
PORTD.7 | RD | (Read strobe to external memory)  
  
RD - PORTD, Bit 7

RD is the external data memory read control strobe.

WR - PORTD, Bit 6

WR is the external data memory write control strobe.

OC1- PORTD, Bit 5

Output compare match output: The PD5 pin can serve as an external output when the Timer/Counter1 com-pare matches.

The PD5 pin has to be configured as an out-put (DDD5 set (one)) to serve this f unction. See the Timer/Counter1 description for further details, and how to enable the output. The OC1 pin is also the output pin for the PWM mode timer function.

INT1 - PORTD, Bit 3

External Interrupt source 1: The PD3 pin can serve as an external interrupt source to the MCU. See the interrupt description for further details, and how to enable the source

INT0 - PORTD, Bit 2

INT0, External Interrupt source 0: The PD2 pin can serve as an external interrupt source to the MCU. See the interrupt description for further details, and how to enable the source.

TXD - PORTD, Bit 1

Transmit Data (Data output pin for the UART). When the UART transmitter is enabled, this pin is configured as an output regardless of the value of DDRD1.

RXD - PORTD, Bit 0

Receive Data (Data input pin for the UART). When the UART receiver is enabled this pin is configured as an output regardless of the value of DDRD0. When the UART forces this pin to be an input, a logical one in PORTD0 will turn on the internal pull-up.

When pins TXD and RXD are not used for RS-232 they can be used as an input or output pin.

No PRINT, INPUT or other RS-232 statement may be used in that case.

The UCR register will by default not set bits 3 and 4 that enable the TXD and RXD pins for RS-232 communication. It is however reported that this not works for all chips. In this case you must clear the bits in the UCR register with the following statements:

```vb
RESET UCR.3

RESET UCR.4

```
or as an alernative : UCR=0

---

## AVR Internal Hardware TIMER0

The 8-Bit Timer/Counter0

![notice](notice.jpg) The 90S8515 was used for this example. Other chips might have a somewhat different timer.

The 8-bit Timer/Counter0 can select its clock source from CK, pre-scaled CK, or an external pin. In addition it can be stopped (no clock).

The overflow status flag is found in the Timer/Counter Interrupt Flag Register - TIFR. Control signals are found in the Timer/Counter0 Control Register - TCCR0. The interrupt enable/disable settings for Timer/Counter0 are found in the Timer/Counter Interrupt Mask Register - TIMSK.

When Timer/Counter0 is externally clocked, the external signal is synchronized with the oscillator frequency of the CPU. To assure proper sampling of the external clock, the minimum time between two external clock transitions must be at least one internal CPU clock period. The external clock signal is sampled on the rising edge of the internal CPU clock.

![basc0074](basc0074.jpg)

The 8-bit Timer/Counter0 features both a high resolution and a high accuracy mode with lower pre-scaling values. Similarly, high pre-scaling values make the Timer/Counter0 useful for lower speed functions or exact timing functions with infrequent actions.

---

## AVR Internal Hardware TIMER1

The 16-Bit Timer/Counter1

![notice](notice.jpg) The 90S8515 was used for the documentation. Other chips might have a somewhat different timer.

The 16-bit Timer/Counter1 can select its clock source from CK, pre-scaled CK, or an external pin. In addition it can be stopped (no clock).

The different status flags (overflow, compare match and capture event) and control signals are found in the Timer/Counter1 Control Registers - TCCR1A and TCCR1B.

The interrupt enable/disable settings for Timer/Counter1 are found in the Timer/Counter Interrupt Mask Register - TIMSK.

When Timer/Counter1 is externally clocked, the external signal is synchronized with the oscillator frequency of the CPU. To assure proper sampling of the external clock, the minimum time between two external clock transitions must be at least one internal CPU clock period.

The external clock signal is sampled on the rising edge of the internal CPU clock.

The 16-bit Timer/Counter1 features both a high resolution and a high accuracy usage with lower pre-scaling values.

Similarly, high pre-scaling values make the Timer/Counter1 useful for lower speed functions or exact timing functions with infrequent actions.

The Timer/Counter1 supports two Output Compare functions using the Output Compare Register 1 A and B -OCR1A and OCR1B as the data values to be compared to the Timer/Counter1 contents.

The Output Compare functions include optional clearing of the counter on compareA match, and can change the logic levels on the Output Compare pins on both compare matches.

Timer/Counter1 can also be used as a 8, 9 or 10-bit Pulse Width Modulator (PWM). In this mode the counter and the OCR1A/OCR1B registers serve as a dual glitch-free stand-alone PWM with centered pulses.

The Input Capture function of Timer/Counter1 provides a capture of the Timer/Counter1 value to the Input Capture Register - ICR1, triggered by an external event on the Input Capture Pin - ICP. The actual capture event settings are defined by the Timer/Counter1 Control Register -TCCR1B.

In addition, the Analog Comparator can be set to trigger the Capture.

![basc0075](basc0075.jpg)

---

## AVR Internal Hardware Watchdog timer

The Watchdog Timer

The Watchdog Timer is clocked from a separate on-chip oscillator which runs at approximately 1MHz. This is the typical value at VCC = 5V.

By controlling the Watchdog Timer pre-scaler, the Watchdog reset interval can be adjusted from 16K to 2,048K cycles (nominally 16 - 2048 ms). The BASCOM RESET WATCHDOG - instruction resets the Watchdog Timer.

Eight different clock cycle periods can be selected to determine the reset period.

If the reset period expires without another Watchdog reset, the AT90Sxxxx resets and program execution starts at the reset vector address.

---

## AVR Internal Registers

You can manipulate the internal register values directly from BASCOM. They are also reserved words. Each register acts like a memory location or program variable, except that the bits of each byte have a special meaning. The bits control how the internal hardware functions, or report the status of internal hardware functions. Read the data sheet to determine what each bit function is for.

The internal registers for the AVR90S8515 are : (other processors are similar, but vary)

Addr. | Register  
---|---  
```vb
$3F | SREG I T H S V N Z C  
$3E | SPH SP15 SP14 SP13 SP12 SP11 SP10 SP9 SP8  
$3D | SPL SP7 SP6 SP5 SP4 SP3 SP2 SP1 SP0  
$3C | Reserved  
$3B | GIMSK INT1 INT0 - - - - - -  
$3A | GIFR INTF1 INTF0  
$39 | TIMSK TOIE1 OCIE1A OCIE1B - TICIE1 - TOIE0 -  
$38 | TIFR TOV1 OCF1A OCF1B -ICF1 -TOV0 -  
$37 | Reserved  
$36 | Reserved  
$35 | MCUCR SRE SRW SE SM ISC11 ISC10 ISC01 ISC00  
$34 | Reserved  
$33 | TCCR0 - - - - - CS02 CS01 CS00  
$32 | TCNT0 Timer/Counter0 (8 Bit)  
$31 | Reserved  
$30 | Reserved  
$2F | TCCR1A COM1A1 COM1A0 COM1B1 COM1B0 - -PWM11 PWM10  
$2E | TCCR1B ICNC1 ICES1 - - CTC1 CS12 CS11 CS10  
$2D | TCNT1H Timer/Counter1 - Counter Register High Byte  
$2C | TCNT1L Timer/Counter1 - Counter Register Low Byte  
$2B | OCR1AH Timer/Counter1 - Output Compare Register A High Byte  
$2A | OCR1AL Timer/Counter1 - Output Compare Register A Low Byte  
$29 | OCR1BH Timer/Counter1 - Output Compare Register B High Byte  
$28 | OCR1BL Timer/Counter1 - Output Compare Register B Low Byte  
$27 | Reserved  
$26 | Reserved  
$25 | ICR1H Timer/Counter1 - Input Capture Register High Byte  
$24 | ICR1L Timer/Counter1 - Input Capture Register Low Byte  
$23 | Reserved  
$22 | Reserved  
$21 | WDTCR - - - WDTOE WDE WDP2 WDP1 WDP0  
$20 | Reserved  
$1F | Reserved - - - - - - - EEAR8  
$1E | EEARL EEPROM Address Register Low Byte  
$1D | EEDR EEPROM Data Register  
$1C | EECR - - - - - EEMWE EEWE EERE  
$1B | PORTA PORTA7 PORTA6 PORTA5 PORTA4 PORTA3 PORTA2 PORTA1 PORTA0  
$1A | DDRA DDA7 DDA6 DDA5 DDA4 DDA3 DDA2 DDA1 DDA0  
$19 | PINA PINA7 PINA6 PINA5 PINA4 PINA3 PINA2 PINA1 PINA0  
$18 | PORTB PORTB7 PORTB6 PORTB5 PORTB4 PORTB3 PORTB2 PORTB1 PORTB0  
$17 | DDRB DDB7 DDB6 DDB5 DDB4 DDB3 DDB2 DDB1 DDB0  
$16 | PINB PINB7 PINB6 PINB5 PINB4 PINB3 PINB2 PINB1 PINB0  
$15 | PORTC PORTC7 PORTC6 PORTC5 PORTC4 PORTC3 PORTC2 PORTC1 PORTC0  
$14 | DDRC DDC7 DDC6 DDC5 DDC4 DDC3 DDC2 DDC1 DDC0  
$13 | PINC PINC7 PINC6 PINC5 PINC4 PINC3 PINC2 PINC1 PINC0  
$12 | PORTD PORTD7 PORTD6 PORTD5 PORTD4 PORTD3 PORTD2 PORTD1 PORTD0  
$11 | DDRD DDD7 DDD6 DDD5 DDD4 DDD3 DDD2 DDD1 DDD0  
$10 | PIND PIND7 PIND6 PIND5 PIND4 PIND3 PIND2 PIND1 PIND0  
$0F | SPDR SPI Data Register  
$0E | SPSR SPIF WCOL - - - - - -  
$0D | SPCR SPIE SPE DORD MSTR CPOL CPHA SPR1 SPR0  
$0C | UDR UART I/O Data Register  
$0B | USR RXC TXC UDRE FE OR - - -  
$0A | UCR RXCIE TXCIE UDRIE RXEN TXEN CHR9 RXB8 TXB8  
$09 | UBRR UART Baud Rate Register  
$08 | ACSR ACD - ACO ACI ACIE ACIC ACIS1 ACIS0  
$00 | Reserved  
  
```
The registers and their addresses are defined in the xxx.DAT files which are placed in the BASCOM-AVR application directory.

The registers can be used as normal byte variables.

PORTB = 40 will place a value of 40 into port B.

Note that internal registers are reserved words. This means that they can't be dimensioned as BASCOM variables!

So you can't use the statement DIM SREG As Byte because SREG is an internal register.

You can however manipulate the register with the SREG = value statement, or var = SREG statement.

---

## Statements and Hardware Resources

Some of the BASCOM statements and functions use a hardware resource.

This is a list of hardware resources and the statement/functions that use them.

USART0

$BAUD, BAUD

USART1

$BAUD1 , BAUD1, 

USARTx

BUFSPACE, CLEAR, ECHO, WAITKEY, ISCHARWAITING, INKEY, INPUTBIN, INPUTHEX, INPUT, PRINT, PRINTBIN

TIMER0

DCF77 , READHITAG , GETRC5 , CONFIG SERVOS , TIME$, DATE$ 

TIMER1

DTMFOUT , RC5SEND, RC6SEND , SONYSEND. 

TIMER2

TIME$, DATE$ 

ADC

GETADC

EEPROM

READEEPROM, WRITEEPROM

TWI

I2CINIT, I2CRECEIVE, I2CSEND, I2START I2CSTOP I2CRBYTE I2CWBYTE

SPI

SPIIN, SPIINIT, SPIMOVE, SPIOUT - SPI

CAN

CONFIG CANBUS, CONFIG CANMOB, CANBAUD, CANRESET, CANCLEARMOB, CANCLEARALLMOBS, CANSEND, CANRECEIVE, CANID, CANSELPAGE, CANGETINTS

---
