# XTINY

The names XTINY, MEGAX, AVRX and UPDI are used in this manual. We do mean the same thing ; the microchip processor with UPDI interface. Since the XTINY was the first platform implemented, you find that XTINY is used a lot.

But it will apply to MEGAX and AVRX as well which were implemented later unless specified otherwise.

At MCS we refer to the new range of TINY processors as the XTINY. This because they look like Xmega processors but smaller.

The XTINY processor is a great new processor. It uses the AVR instruction set. But it has a lot of the hardware found in the Xmega.

But do not make a mistake : these processors are different in many ways. They are the next generation of AVR processors. 

They use little power. 

When XMega was supported we had to make some decisions about this support. The goal is to keep the code BASCOM compatible. And for Xtiny we were faced with the same dilemmas. 

So again there will be new CONFIG statements and because the hardware is different, there will be other changes as well. 

You should read the data sheet of the processor like ATTINY816. We used the attiny 816/817 for testing. 

The processors are not available anymore in DIP. But you can use SOIC with a converter board. Like Xmega, this makes the processor less usable for hobbyists. At least for those that do not make their own PCB's.

Like the Xmega the internal registers can not be addressed by a pointer. So we had to change code using register pointers.

The DAT files contain a constant that identifies the platform. This constant is named _XTINY. For normal AVR and Xmega is is absent.

Platform Value

XTINY 1

MEGAX 2

AVRX DA, DB, DD 3

AVRX EA 4

Since the NVM controller differs among platforms, this constant is used in the xtiny.lib for writing the EEPROM.

UPDI

A big difference is that you once again need a new programmer since the programming interface is using UPDI.

The good news however is that you can use a simple serial port and a resistor to do the programming.

BASCOM-AVR supports the [UPDI](updi_programmer.md) protocol with a dedicated programmer. 

You will notice when you read the fuses that there are a lot of fuses and other settings. 

OSC

Like the Xmega, the Xtiny has extensive internal and external oscillator support. This means that you need to chose the system clock using the CONFIG SYSCLOCK statement.

This is essentially the only difference in code you need to make compared to the normal AVR.

The options and values differ from the Xmega. 

UART

In order to use the UART, you need to use CONFIG COMx. There is no default configuration when you use $baud. We would recommend to use CONFIG COM anyway. It can set all relevant settings. 

Also notice that the UART has separate registers for reading and writing. That is something new, not seen earlier. For this purpose we mapped registers UDRW and UDRR to the USART0_RXDATA / TXDATA registers.

ERAM

The EEPROM is more complex since it only works with pages. But the good news is that the EEPROM can be read like normal variables. 

PORTS

The ports have more options compared to normal AVR but less compared to Xmega. While Xmega can do a setting for an entire port, this feature is missing in Xtiny. The virtual port option is also different. In Xtiny there is just a register in the lower IO space mapped to the three most important port registers : DDR, PORT and PIN. These are named VPORTA_DIR, _OUT and _IN. 

In the first XTINY support we added DDR0, PORT0, PIN0 to make them compatible with Xmega. We also added VDDRA, VPORTA, and VPINA. All these registers are located in lower IO memory. In 2084 we removed these aliases. 

IMPORTANT CHANGE in 2084

It turned out that using the same scheme as for the Xmega was not optimal. So for 2084 we changed some ALIAS. 

We suggest you read the following information.

In the normal AVR there are PIN, PORT and DDR registers. They always have a low IO address so the instructions like CBI/SBI can be used.

This means that only 1 asm instruction is required to set/reset a bit of a port related register.

For example for the 2313def.dat we have PORTD:

PORTD =$12

DDRD =$11

PIND =$10

Since low IO space is limited and AVR processors with more ports were made, these ports got an extended IO address. Which means that the address is higher.

It also means that instructions like CBI/SBI will not work since they only work on low memory addresses.

For example from the m128RFA1.DAT

PORTL= $10b 

DDRL= $10a 

PINL= $109 

To change a bit in such a register, the value must be loaded, altered and written back.

With Xmega the port related addresses got a high address. But also a virtual port was added. These are dynamic virtual ports. Which means that you can chose at run time to which port a virtual register is mapped to. These virtual port addresses are placed in the low IO address space. So CBI/SBI could be used.

For example for the xm128A4Udef.dat these are some virtual registers

VPORT0_DIR = 16

VPORT0_OUT = 17

VPORT0_IN = 18

These registers can be made to map to PORTA, PORTB, etc. And you can change this at run time. So there is no fixed relation between the virtual and the actual port. Writing to a virtual port will write to the actual register. Thus when VPORT0 is mapped to PORTA, both writing to PORTA and VPORT0 will do the same thing.

Since there is no fixed relation, an ALIAS to PORTA points to PORTA_OUT. This because there is no PORT/DDRA/PINA register. So as a user you can use the port as you always did.

```vb
For the XTINY there is again a virtual register but it has a fixed relation. 

For example for the attiny816 :

```
VPORTA_DIR=0 ; 0000

VPORTA_OUT=1 ; 0001

VPORTA_IN=2 ; 0002

The relation is fixed. Each port has a virtual register. 

So instead of pointing to PORTA_OUT for PORTA, we now point to the VPORTA_OUT register. 

This will give better code. 

But it also required compiler changes. The problem with the virtual address is that the order is different. It would have been great if the traditional order was used. 

Because the ports are similar to xmega ports we point to PORTx_DIR.

Lets have a look at VPORTA in the DAT file :

VPORTA_DIR=0 ; 0000

DDRA=0 ; 0000 alias

VPORTA_OUT=1 ; 0001

PORTA=1 ; 0001 alias

VPORTA_IN=2 ; 0002

PINA=2 ; 0002 alias

The alias we use are DDRA, PORTA and PINA.

Since all ports are aliased all port related code should work without problems.

Pull Up

The pin behavior can be further configured using [CONFIG XPIN](config_xpin.md). 

This is important since the pull up need to be configured. The pull up can no longer be activated by writing a 1 to the PORT register !

INTERRUPTS

The interrupt system is extended with an option to specify one high priority interrupt.

So this is a nice extension.

You should also notice that a lot of interrupts need to be cleared manually. For example using a PIN interrupt requires to reset the INTFLAG register by writing a 1. 

While normal AVR pin interrupts let you guess which pin caused the interrupt, the Xtiny has registers that tell which pin caused the interrupt.

WATCHDOG

The watchdog works different since it has no on/off control. A timeout value of 0 will turn off the WD timer.

Any other time will start the WD timer.

START WATCHDOG will use the last value found from CONFIG WATCHDOG. When not found or available an error will be thrown by the compiler

STOP WATCHDOG will write a value of 0 to turn of the WD.

DAT files

When you look in the DAT file you will notice that almost all registers have new names. Also compared to Xmega. Of course BASCOM will use the right register when you use BASCOM code. 

When using ASM you need to check the datasheet and the DAT file.

When you are familiar with Xmega the transition should be smooth.

ADC and DAC

The Xtiny chips are very complete. They also have AD converter and a DA converter on board. 

TWI/I2C

The TWI is almost identical to the TWI in Xmega. This also means that when using TWI you need to create a byte variable named TWI_START in your user code.

The reason for this is that the TWI hardware sends a START and the slave address at once. 

Traditionally this was separated by an I2CSTART and I2CWBYTE. 

The TWI_START variable holds the state of I2CSTART. And when you write the address, it will use the proper instruction to send start and slave address. 

When you want to use soft I2C, you need to use the $FORCESOFTI2C directive. 

Do NOT include the "i2c_twi.lbx" library since this library is only for old AVR processors.

1WIRE

Since the ports have a different mapping, the 1wire code needed to be rewritten as well. The code is placed in the xtiny.lib

LIB

All Xtiny specific code you can find in Xtiny.lib

It contains overloaded versions of the code found in mcs.lib

Xtiny specific code in mcs.lib or other libs can be found by looking for the _XTINY constant.

This constant is set when you use a processor from the Xtiny range.

For normal Xtiny the value is set to 1. For megaX (like M4809) it is set to 2. 

BOOT

The XTINY has a different memory model. The BOOT area is located at the start of memory. After this memory the normal memory is located. With a FUSE you can set how many pages of the BOOT area you would like to use for boot code. A value of 1 will reserve a space of 256 bytes(this depends on the page size). When your loader binary code is 1024 bytes you would set it to : 1024/256 = 4

After the normal application code there is also the optional application data. This area can also be set with a fuse.

When using a boot loader you need to take care of the fact that your normal application code must start after the boot code. This can be done by using $ROMSTART in your code.

TCAx

Timer TCA has 1 or more wave outputs. As a user you need to set the pin to the output mode. 

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

Add on

The addition of Xmega to BASCOM was a lot of work. This because only the instruction set was the same. We worked long on UPDI processor support and still this is a work in progress. So expects some updates specific for Xtiny/UPDI.

The Xtiny addition is not free of charge. It requires a commercial add on. It is available from the MCS shop.

The Xtiny add on will support all Xtiny processors. And by that we mean processors from the mega range like mega4808, DA/DB/DD range like avr128da28 etc.

See also

[MEGAX](megax.md), [AVRX](avrx.md)