# CONFIG EVENT_SYSTEM XTINY

Action

This statement configures the Xtiny event routing.

Syntax

```vb
CONFIG EVENT_SYSTEM = dummy, ASYNCCHx=asyncX,SYNCCHy=syncY,ASzz=asyncUserZZ,Sn=syncUserN

CONFIG EVENT_SYSTEM = dummy, ASYNCCH0=asyncX,SYNCCH00=syncY,AS00=asyncUserZZ,S0=syncUserN

```
Remarks

The Event System (EVSYS) enables direct peripheral-to-peripheral signaling. It allows a change in one peripheral (the Event Generator) to trigger actions in other peripherals (the Event Users) through Event

channels, without using the CPU. It is designed to provide short and predictable response times between peripherals, allowing for autonomous peripheral control and interaction, and also for synchronized timing

of actions in several peripheral modules. It is thus a powerful tool for reducing the complexity, size, and execution time of the software.

A change of the Event Generator's state is referred to as an Event, and usually corresponds to one of the peripheral's interrupt conditions. Events can be directly forwarded to other peripherals using the

dedicated Event routing network. The routing of each channel is configured in software, including event generation and use.

Only one trigger from an Event generator peripheral can be routed on each channel, but multiple channels can use the same generator source. Multiple peripherals can use events from the same channel.

A channel path can be either asynchronous or synchronous to the main clock. The mode must be selected based on the requirements of the application.

The Event System can directly connect analog and digital converters, analog comparators, I/O port pins, the real-time counter, timer/counters, and the configurable custom logic peripheral. Events can also be generated from software and the peripheral clock.

The are 4 asynchronous event channels (ASYNCCHx) and 2 synchronous event channels(SYNCCHy). 

ASYNCCHx | Async channel x where x is in the range from 0 to 3.  Each channel has different generators of events. For channels 0-3 : CCL_LUT0 CCL_LUT1 AC0_OUT TCD0_CMPBCLR TCD0_CMPASET TCD0_CMPBSET TCD0_PROGEV RTC_OVF RTC_CMP Channel 0 also has the following sources: PORTA.0 - PORTA.7 UPDI Channel 1 also had the following sources : PORTB.0 - PORTB.7 Channel 2 also had the following sources : PORTC.0 - PORTB.5 Channel 4 also had the following sources : PIT_DIV8192 - PIT_DIV64  
---|---  
SYNCCHy | Synchroneous channely where y is in the range from 0-1. Each channel has different generators of events. For channel 0-1 : TCB0 TCA0_OVF_LUNF TCA0_HUNF TCA0_CMP0 TCA0_CMP1 TCA0_CMP2 Channel 0 also has the following sources: PORTC.0 - PORTC.5 PORTA.0- PORTA.7 Channel 1 also has the following sources: PORTB.0 - PORTB.7  
ASzz | Asynchronous user channel input selection. There are 11 channels in the range from 0-10. Each channel selects different input which is fixed for each channel. 00 : TCB0 01 : ADC0 02 : CCL_LUT0EV0 03 : CCL_LUT1EV0 04 : CCL_LUT0EV1 05 : CCL_LUT1EV1 06 : TCD0_EV0 07 : TCD0_EV1 08 : EVOUT0 09 : EVOUT1 10 : EVOUT2 The values are fixed : \- OFF \- SYNCCH0 \- SYNCCH1 \- ASYNCCH0 \- ASYNCCH1 \- ASYNCCH2 \- ASYNCCH3  
Sn | Synchronous user channel input selection. There are 2 channels in the range from 0-1. Each channel selects different input which is fixed for each channel. 00 : TCA0 01 : USART0 The values are fixed : \- OFF \- SYNCCH0 \- SYNCCH1  
  
See also

[ ](atxmega.md)