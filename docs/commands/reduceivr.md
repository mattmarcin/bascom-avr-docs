# $REDUCEIVR

Action

This directive will inform the compiler to reduce the IVR (interrupt vector table) to the smallest possible size.

Syntax

$REDUCEIVR

Remarks

The flash memory of the processor always starts with the IVR (interrupt vector table). The user code is placed after this table.

So what is this IVR ?

This table contains an address for each interrupt. When an interrupt occurs, the processor will jump to a specific and fixed address in code memory.

The address depends on the interrupt itself, and on the processor. For example the MEGA88 has 25 interrupt sources. You can find them in the dat file :

INTname1=INT0,$001,EIMSK.INT0,EIFR.INTF0

INTname2=INT1,$002,EIMSK.INT1,EIFR.INTF1

INTname3=PCINT0,$003,PCICR.PCIE0,PCIFR.PCIF0

INTname4=PCINT1,$004,PCICR.PCIE1,PCIFR.PCIF1

INTname5=PCINT2,$005,PCICR.PCIE2,PCIFR.PCIF2

INTname6=WDT@WATCHDOG,$006,WDTCSR.WDIE,WDTCSR.WDIF

INTname7=OC2A@COMPARE2A,$007,TIMSK2.OCIE2A,TIFR2.OCF2A

INTname8=OC2B@COMPARE2B,$008,TIMSK2.OCIE2B,TIFR2.OCF2B

INTname9=OVF2@TIMER2,$009,TIMSK2.TOIE2,TIFR2.TOV2

INTname10=ICP1@CAPTURE1,$00A,TIMSK1.TICIE1,TIFR1.ICF1

INTname11=OC1A@COMPARE1A,$00B,TIMSK1.OCIE1A,TIFR1.OCF1A

INTname12=OC1B@COMPARE1B,$00C,TIMSK1.OCIE1B,TIFR1.OCF1B

INTname13=OVF1@TIMER1,$00D,TIMSK1.TOIE1,TIFR1.TOV1

INTname14=OC0A@COMPARE0A,$00E,TIMSK0.OCIE0A,TIFR0.OCF0A

INTname15=OC0B@COMPARE0B,$00F,TIMSK0.OCIE0B,TIFR0.OCF0B

INTname16=OVF0@TIMER0,$010,TIMSK0.TOIE0,TIFR0.TOV0

INTname17=SPI,$011,SPCR.SPIE,SPSR.SPIF

INTname18=URXC@SERIAL,$012,UCSR0B.RXCIE0,UCSR0A.RXC0

INTname19=UDRE,$013,UCSR0B.UDRIE0,UCSR0A.UDRE0

INTname20=UTXC,$014,UCSR0B.TXCIE0,UCSR0A.TXC0

INTname21=ADCC@ADC,$015,ADCSRA.ADIE,ADCSRA.ADIF

INTname22=ERDY,$016,EECR.EERIE

INTname23=ACI,$017,ACSR.ACIE,ACSR.ACI

INTname24=TWI,$018,TWCR.TWIE,TWCR.TWINT

INTname25=SPM,$019,SPMCSR.SPMIE

You can see that INT0 comes first. And that the address is $001 which is &H0001. So when INT0 occurs, the processor will jump to address 1.

When you did not define an ISR (ON INT0) , the compiler will insert a RETI instruction. So nothing bad will happen to your code.

When you did define an ISR , the compiler will insert a JUMP to your interrupt routine. When your interrupt ends, the RETI will let the processor continue where it was when the interrupt occurred.

In the example when we only use the ISR with the lowest address all other addresses in the table would get a RETI instruction. And the user code could start at &H1A (one address after $19). 

Now that is not so bad but there are also processors with bigger tables and with tables that require 2 words for a JUMP. You waste a lot of space this way.

So what does $REDUCEIVR do? It will determine which interrupt you have used has the highest address. And it will use the address after that as the user code start.

This means that if we use only INT0 and we use $REDUCEIVR, the user code will start at address &H2 ($2). So you will save a lot of code space this way.

Ok so why isn't this enabled by default? There is a catch : when your code has an interrupt enabled and there is no matching ON <INT> the processor will jump into the user code and this will create a crash almost for sure.

So our advise : use this when you understand what this option does, and use it when your application is finished. In any case, retest the complete application when the option is enabled.

See also

[$LOADER](loader.md) , [CONFIG INTVECTORSELECTION](config_intvectorselection.md) , [$BOOTVECTOR](bootvector.md)

Example

$REDUCEIVR