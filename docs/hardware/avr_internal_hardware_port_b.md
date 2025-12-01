# AVR Internal Hardware Port B

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