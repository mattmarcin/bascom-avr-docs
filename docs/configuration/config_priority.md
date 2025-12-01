# CONFIG PRIORITY XMEGA

Action

Configures the interrupt system and priority for Xmega 

Syntax

CONFIG PRIORITY= prio, VECTOR= vector, HI= hi, LO= lo, MED= med 

Remarks

prio | STATIC or ROUNDROBIN. In the AVR the lowest interrupt address has the highest priority. When you chose STATIC the interrupts behave as in non-Xmega chips. To prevent that a low priority interrupt never get executed you can select ROUNDROBIN  
---|---  
vector | APPLICATION or BOOT. Application is the default. This will place the interrupt vectors at address 0, the starting address.  When you chose BOOT, the interrupt vectors are placed at the beginning of the boot section. This makes it possible to use interrupts in a boot application.  
hi | ENABLED or DISABLED. Chose ENABLED to enable the HI priority interrupts.  
lo | ENABLED or DISABLED. Chose ENABLED to enable the LO priority interrupts.  
med | ENABLED or DISABLED. Chose ENABLED to enable the MED priority interrupts.  
  
In the XMEGA, you must enable HI, LO or MED interrupts before you can use them.

When you enable an interrupt you also must specify the priority.

For example : Enable Usartc0_rxc , Lo 

This would enable the USARTC0_RX interrupt and would assign it a low priority. 

In this case, at least the LO priority should be enabled :

Config Priority = Static , Vector = Application , Lo = Enabled 

When you use LO and MED interrupts, you need to enable the both.

![notice](notice.jpg)When you do not specify the priority when enabling an interrupt like : ENABLE Tcc0_ovf , the compiler will use the MED interrupt level. This means that you must enable this as well when using CONFIG PRIORITY. When you do NOT use CONFIG PRIORITY, but only ENABLE INTERRUPTS, the compiler will activate the MED interrupt automatically. 

So when not using CONFIG PRIORITY all will work out just fine, but when using CONFIG PRIORITY, do not forget to enable the MED priority.

See also

[ENABLE](enable.md) , [DISABLE](disable.md) , [ON](on_interrupt.md)

Example

```vb
Config Priority = Static , Vector = Application , Lo = Enabled

On Usartc0_rxc Rxc_isr

Enable Usartc0_rxc , Lo

Enable Interrupts

```