# CONFIG PRIORITY XTINY

Action

Configures the interrupt system and priority for Xmega 

Syntax

CONFIG PRIORITY= prio, VECTOR= vector, COMPACT= compact , HI= hi

Remarks

prio | STATIC or ROUNDROBIN. In the AVR the lowest interrupt address has the highest priority. When you chose STATIC the interrupts behave as in non-Xmega chips. To prevent that a low priority interrupt never get executed you can select ROUNDROBIN  
---|---  
vector | APPLICATION or BOOT. Application is the default. This will place the interrupt vectors at address 0, the starting address.  When you chose BOOT, the interrupt vectors are placed at the beginning of the boot section. This makes it possible to use interrupts in a boot loader application.  
compact | ENABLED or DISABLED. Chose ENABLED to write a compact interrupt table.  
hi | The interrupt that should be given a HIGH priority. Only one interrupt can be given a HIGH priority.  Possible values : NMI,VLM,PORTA_INT,PORTB_INT,PORTC_INT,RTC_OVF,PIT_OVF,TCA0_LUNF,TCA0_HUNF,TCA0_CMP0,TCA0_CMP1,TCA0_CMP2,TCB0_INT,TCD0_OVF,TCD0_TRIG,AC0_COMP0,ADC0_RDY,ADC0_WCOMP,TWI0_SLAVE,TWI0_MASTER,SPI0_INT,USART0_RXC,USART0_DRE,USART0_TXC,NVM_EE  
  
In the XTINY, you can provide one interrupt to be serviced with a HIGH priority.

By default the interrupt address with the lowest address will get the highest interrupt. This is NMI with address 0. 

After that the PORT interrupts will get priority over all the other interrupts.

When you would like that USART0_RXC would get a HIGH (or the highest) interrupt, you can specify the interrupt name so it will be serviced with the highest priority.

Config Priority = Static , Vector = Application , HI = USART0_RXC 

See also

[ENABLE](enable.md) , [DISABLE](disable.md) , [ON](on_interrupt.md)

Example

```vb
Config Priority = Static , Vector = Application , Hi = USART0_RXC

On Usartc0_rxc Rxc_isr

Enable Usartc0_rxc 

Enable Interrupts

```