# AVR Internal Registers

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