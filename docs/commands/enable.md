# ENABLE

Action

Enable specified interrupt.

(ATTINY, ATMEGA, ATXMEGA)

Syntax

ENABLE interrupt [, prio]

[, prio] is only for ATXMEGA

Remarks

Interrupt | Description  
---|---  
INT0 | External Interrupt 0  
INT1 | External Interrupt 1  
OVF0,TIMER0, COUNTER0 | TIMER0 overflow interrupt  
OVF1,TIMER1, COUNTER1 | TIMER1 overflow interrupt  
CAPTURE1, ICP1 | INPUT CAPTURE TIMER1 interrupt  
COMPARE1A,OC1A or COMPARE1, OC1 | TIMER1 OUTPUT COMPARE A interrupt In case of only one compare interrupt  
COMPARE1B,OC1B | TIMER1 OUTPUT COMPARE B interrupt  
SPI | SPI interrupt  
URXC | Serial RX complete interrupt  
UDRE | Serial data register empty interrupt  
UTXC | Serial TX complete interrupt  
SERIAL | Disables URXC, UDRE and UTXC  
ACI | Analog comparator interrupt  
ADC | A/D converter interrupt  
  
|   
  
XMEGA ONLY |   
  
prio | The priority you want to assign to the interrupt. Specify Lo, Hi or Med.  In the Xmega you must provide the priority of the interrupts. Lo=Low priority. Hi=High priority and Med=Medium priority. If you do not specify a priority, MED will be used.  
  
By default all interrupts are disabled.

The global interrupts master switch is also disabled by default. 

If you enable an interrupt, it will only fire if the master interrupt switch is enabled.

You enable this master switch with ENABLE INTERRUPTS.

You can disable it with DISABLE INTERRUPTS.

If an interrupt is executed, the global master switch will be disabled automatically by the hardware.

This is to prevent other interrupts to occur. 

When the interrupt routine returns, the processor hardware will automatically enable the master switch so new interrupts may occur.

The following schematic demonstrates the interrupt master switch. It forms an AND with the other interrupts. This means that both the interrupt of a hardware source and the master switch interrupt must be enabled. ENABLE interrupts will enable the I flag in SREG.

![int-global](int-global.png)

It depends on the processor how many and which interrupts it has. If you type ENABLE in the editor, you will get a pop up with a list of interrupts you can chose from.

ATTINY & ATMEGA Interrupt List

In normal AVR chips the priority is determined by the interrupts address. The lower the address, the higher the priority.

In the DAT file you can find a list with interrupts and their address.

For example , taken from the m1280def.dat file :

[INTLIST]

count=56

INTname1=INT0,$002,EIMSK.INT0,EIFR.INTF0

INTname2=INT1,$004,EIMSK.INT1,EIFR.INTF1

INTname3=INT2,$006,EIMSK.INT2,EIFR.INTF2

INTname4=INT3,$008,EIMSK.INT3,EIFR.INTF3

INTname5=INT4,$00a,EIMSK.INT4,EIFR.INTF4

INTname6=INT5,$00c,EIMSK.INT5,EIFR.INTF5

INT0 has the highest priority since it has the lowest address (address 2)

Following an Overview where INT0 is used as an example.

Overview

1\. You configure an Interrupt

  
```vb
On Int0 Int0_isr   
Config Int0 = Low Level

```
2\. You enable the specific Interrupt

  
Enable Int0  


3\. Enable all Interrupts

  
Enable Interrupts  
  
  
4\. You have an Interrupt Service Routine after the "End" with an Return  


```vb
End

' Interrupt Service Routine  
```
Int0_isr:  
```vb
' so someting.....  
Return

```
XMEGA

The XMEGA has a priority system. You can specify if an interrupt has a low, medium or high priority.

But you MUST enable these priorities with [CONFIG PRIORITY](config_priority.md)

Please read the topic [CONFIG PRIORITY](config_priority.md) in order to understand which interrupt to enable.

In the DAT file you can find a list with interrupts and their address.

For example , taken from the "xm128A4Udef.dat file "

INTLIST]

count=95

INTname1=OSCFAIL,$0002,OSC_XOSCFAIL.0,OSC_XOSCFAIL.1 ; XOSC Failure Detection Register

INTname2=PORTC_INT0,$0004,#PORTC_INTCTRL.0,PORTC_INTFLAGS.0

INTname3=PORTC_INT1,$0006,#PORTC_INTCTRL.2,PORTC_INTFLAGS.1

INTname4=PORTR_INT0,$0008,#PORTR_INTCTRL.0,PORTR_INTFLAGS.0

INTname5=PORTR_INT1,$000A,#PORTR_INTCTRL.2,PORTR_INTFLAGS.1

INTname6=DMA_CH0,$000C,#,DMA_CH0_CTRLB.0,DMA_CH0_CTRLB.4

INTname7=DMA_CH1,$000E,#,DMA_CH1_CTRLB.0,DMA_CH1_CTRLB.4

INTname8=DMA_CH2,$0010,#,DMA_CH2_CTRLB.0,DMA_CH2_CTRLB.4

INTname9=DMA_CH3,$0012,#,DMA_CH3_CTRLB.0,DMA_CH3_CTRLB.4

INTname10=RTC_OVF,$0014,#RTC_INTCTRL.0,RTC_INTFLAGS.0

INTname11=RTC_COMP,$0016,#RTC_INTCTRL.2,RTC_INTFLAGS.1

Example with PORTC_INT0  
  
```vb
On Portc_int0 portc_isr  
Enable Portc_int0 , Hi  


```
In [ATXMEGA](atxmega.md) there is an example for Pin Interrupt.

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

See also

[DISABLE](disable.md) , [ON](on_interrupt.md) , [CONFIG PRIORITY](config_priority.md), [ATXMEGA](atxmega.md)

Example

  
```vb
$regfile = "attiny25.dat"  
$crystal = 1000000 ' 1MHz  
$hwstack = 10  
$swstack = 0  
$framesize = 24  
  
  
On Int0 Int0_isr ' INT0 will be the wake-up source for Powerdown Mode  
Config Int0 = Low Level ' External Pull-up (47K) on Portb.2  
Enable Int0  
  
'###############################################################################  
Do  
Wait 3 ' now we have 3 second to measure the Supply Current in Active Mode  
  
Enable Interrupts  
  
' Now call Powerdown function  
Config Powermode = Powerdown  
  
'Here you have time to measure PowerDown current consumption until a Low Level on Portb.1 which is the PowerDown wake-up  
Loop  
'###############################################################################  
End  
  
  
```
Int0_isr:  
```vb
' wake_up  
Return

```