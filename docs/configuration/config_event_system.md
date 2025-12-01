# CONFIG EVENT_SYSTEM

Action

This statement configures the Xmega event routing.

Syntax

CONFIG EVENT_SYSTEM = dummy, MUXx=MUX, QDx=QD, QDIx=QDI, QDIRMx=QDIRM,DIGFLTx=DIGFLT

The letter X is used to indicate that a value between 0 and 7 can be used. So there is MUX0, MUX1, MUX2,MUX3 etc.

Remarks

The Event System is a set of features for inter peripheral communication. It enables the possibility

for a change of state in one peripheral to automatically trigger actions in other peripherals.

The change of state in a peripheral that will trigger actions in other peripherals is configurable in

software. It is a simple, but powerful system as it allows for autonomous control of peripherals

without any use of interrupt, CPU or DMA resources.

There are 8 multiplexers and 8 control registers. Register 0, 2 and 4 can be used for quadrature decoding. 

MUX | There are 8 multiplexers, named MUX0-MUX7. The MUX is used to select an event source.There are many sources for events : NONE : disabled, default RTC_OVF : Real Timer overflow RTC_CMP : Real Timer compare match ACA_CH0 : analog comparator ACA, channel 0 ACA_CH1 : analog comparator ACA, channel 1 ACA_WIN : analog comparator ACA, window ACB_CH0 : analog comparator ACB, channel 0 ACB_CH1 : analog comparator ACB, channel 1 ACB_WIN : analog comparator ACB, window ADCA_CH0- ADCA_CH3 : ADCA channel 0-3 ADCB_CH0- ADCB_CH3 : ADCB channel 0-3 PORTA.0 - PORTA.7 : PORT A pin 0-7 PORTB.0 - PORTB.7 : PORT B pin 0-7 PORTC.0 - PORTC.7 : PORT C pin 0-7 PORTD.0 - PORTD.7 : PORT D pin 0-7 PORTE.0 - PORTE.7 : PORT E pin 0-7 PORTF.0 - PORTF.7 : PORT F pin 0-7 PRESCALER1, PRESCALER2, PRESCALER4, PRESCALER8, PRESCALER16, PRESCALER32, PRESCALER64,PRESCALER128,PRESCALER256,PRESCALER512,PRESCALER1024,PRESCALER2048,PRESCALER4096,PRESCALER8192,PRESCALER16384 : The clock divided by 1,2,4,8,16,32,64,128,256 etc. TCC0_OVF : Timer TC0 overflow TCC0_ERR : Timer TC0 error TCC0_CCA : Timer TC0 capture or compare match A TCC0_CCB : Timer TC0 capture or compare match B TCC0_CCC : Timer TC0 capture or compare match C TCC0_CCD : Timer TC0 capture or compare match D TCC1_OVF : Timer TC1 overflow TCC1_ERR : Timer TC1 error TCC1_CCA : Timer TC1 capture or compare match A TCC1_CCB : Timer TC1 capture or compare match B TCC1_CCC : Timer TC1 capture or compare match C TCC1_CCD : Timer TC1 capture or compare match D Dito for TCD0, TCD1, TCE0, TCE1, TCF0 and TCF1  
---|---  
QD | Enables or disables the quadrature decoder. Will only work on QD0,QD2 and QD4.  
QDI | Enables or disables the quadrature decode index. Will only work on QDI0, QDI2 and QDI4.  
QDIRM | Quadrature decode index recognition mode. This is a numeric constant between 0 and 3. Each value represents the 2 possible bit values for the two input signals. Will only work on QDIRM0, QDIRM2 and QDIRM4.  
DIGFLT | Defines the length of digital filtering used. Events will be passed through to the event channel only when the event source has been active and sampled with the same level for a number of peripheral clock for the number of cycles as defined by DIGFLT.  The number of samples is in the range from 1-8. The default is 1 sample.  
|   
  
See also

[ATXMEGA](atxmega.md)

Example 1:  
  
```vb
' Select PortC.0 as INPUT to event channel 0  
' Digflt0 = 8 --> Enable Digital Filtering for Event Channel 0. 

' The Event must be active for 8 samples in order to be passed to the Event system  
' Event Channel 1 INPUT = Timer/Counter C0 Overflow  
' Event Channel 2 INPUT = Analog Input Port A Channel 0  
' Event Channel 3 INPUT = Real Timer overflow  
Config Event_system = Dummy , _  
```
Mux0 = Portc.0 , Digflt0 = 8 , _  
Mux1 = Tcc0_ovf , _  
Mux2 = Adca_ch0 , _  
Mux3 = Rtc_ovf

Example 2:

```vb
'Event Channel 7 is input for the Timer/Counter TcD1 overflow 

Config Event_system = Dummy , Mux7 = Tcd1_ovf 

```
Example 3:

  
```vb
' Using the Counter/Timer to count events like a falling edge on Pine.5  
  
$regfile = "xm256a3bdef.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 'Portf.2 and Portf.3 is COM7  
```
Open "COM7:" For Binary As #1  
  
```vb
'Config Interrupts  
Config Priority = Static , Vector = Application , Lo = Enabled , Med = Enabled 'Enable Lo Level Interrupts  
  
Dim Timer_overflow As Bit  
  
Print #1 , "---Event Counting with Timer C0 over Event Channel 0 from PINE.5----"  
  
Config Porte.5 = Input  
Config Xpin = Porte.5 , Outpull = Pullup , Sense = Falling 'enable Pullup and reaction on falling edge  
Config Event_system = Dummy , Mux0 = Porte.5 , Digflt0 = 8 'Eventchannel 0 = PINE.5, enable digital filtering

Config Tcc0 = Normal , Prescale = E0 , Event_source = E0 , Event_action = Capture' Normal = no waveform generation, Event Source = Event Channel 0  
  
On Tcc0_ovf Timerd0_int  
Enable Tcc0_ovf , Lo 'Enable overflow interrupt in LOW Priority  
```
Tcc0_per = 5 'Interrupt when Count > 5  
```vb
Enable Interrupts  
  
'################MAINLOOP#######################################################  
Do  
  
Wait 1  
Print #1 , "TCC0_CNT = " ; Tcc0_cnt 'Actual Count  
  
If Timer_overflow = 1 Then  
Reset Timer_overflow  
Print #1 , "TCC0_OVERVLOW" 'Print it when Overflow Interrupt is fired  
End If  
  
Loop  
'################MAINLOOP#######################################################  
  
  
End  
  
```
Timerd0_int:  
```vb
Set Timer_overflow  
Return

```