# CONFIG POWER_REDUCTION

Action

This option configures the power reduction registers to reduce power consumption.

Syntax

CONFIG POWER_REDUCTION= dummy, device=ON|OFF

Remarks

The Power Reduction (PR) registers provides a method to stop the clock to individual peripherals.

When this is done the current state of the peripheral is frozen and the associated I/O

registers cannot be read or written. Resources used by the peripheral will remain occupied;

hence the peripheral should in most cases be disabled before stopping the clock. Enabling the

clock to a peripheral again, puts the peripheral in the same state as before it was stopped. This

can be used in Idle mode and Active mode to reduce the overall power consumption significantly.

In all other sleep modes, the peripheral clock is already stopped.

Not all devices have all the peripherals associated with a bit in the power reduction registers.

Setting a power reduction bit for a peripheral that is not available will have no effect.

Device | A hardware resource of the Xmega. The following hardware resources can be deactivated to reduce power: AES EBI LCD RTC EVSYS DMA DACA, DACB ACA,ACB ADCA,ADCB TWIC,TWID,TWIE,TWIF USARTC0,USARTC1, USARTD0,USARTD1,USARTE0,USARTE1,USARTF0,USARTF1 SPIC,SPID,SPIE,SPIF TCC0,TCC1,TCD0,TCD1,TCE0,TCE1,TCF0,TCF1 HIRESC,HIRESD,HIRESE,HIRESF XCL A value of ON will leave the resource enabled and a value of OFF will activate the power reduction.  
---|---  
  
You should use the CONFIG POWER_REDUCTION at start up to disable all unused resources. All the power reduction registers will be set for the provided resources. But the existing configuration will not be preserved. When you need to enable/disable an individual resource at run time, you can manual access the register with a SET or RESET command.

For example, the DMA, EVSYS, RTC, EBI and AES bits are located in the PRGEN register. If you disable DMA and AES the compiler will write a value of 17 (dma +aes) to the PRGEN register.

It will not first read the existing value, and preserve the other bits. That is why this statement should be used once.

When you specify one value, for example DMA, it will write 1 to the PRGEN register and thus overwriting the previous AES bit that was 1, with a 0. 

The additional code to mask and set the bits did not seem useful at implementation time. At user request this behaviour can be changed in a future version.

See also

NONE

Example

```vb
'-----------------------------------------------------------  
' XM128A1-POWER-REDUCTION.BAS  
' (c) 1995-2025 MCS Electronics  
' sample provided by MAK3  
'-----------------------------------------------------------  
  
' CONFIG POWER_REDUCTION and USING EVENT SYSTEM  
  
' This Example show how to use the config power_reduction and give first insights to the XMEGA EVENT SYSTEM  
  
' Regarding the Eventsytem this example easy show after event configuration that one Port Pin is routed to another Port Pin.  
' You can see it works even during the WAIT 4 command and there are no PORT READ OR WRITE commands in the Do .... Loop !  
' It also shows how to manual fire an Event  
  
$regfile = "xm128a1def.dat"  
$crystal = 2000000 ' 2MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Enabled  
Config Sysclock = 2mhz ' 2MHz  
  
' YOU CAN MINIMIZE POWER CONSUMPTION FOR EXAMPLE WITH :  
' 1. Use Low supply voltage  
' 2. Use Sleep Modes  
' 3. Keep Clock Frequencys low (also with Precsalers)  
' 4. Use Powe Reduction Registers to shut down unused peripherals  
  
'With Power_reduction you can shut down specific peripherals that are not used in your application  
'Paramters: aes,dma,ebi,rtc,evsys,daca,dacb,adca,adcb,aca,acb,twic,usartc0,usartc1,spic,hiresc,tcc0,tcc1  
Config Power_reduction = Dummy , Aes = Off , Twic = Off , Twid = Off , Twie = Off , Aca = Off , Adcb = Off , Tcc0 = Off , Tcc1 = Off , Dma = Off  
  
'For the following we need the EVENT System therefore we do not shut down EVENT SYSTEM  
  
Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM1:" For Binary As #1  
```vb
Waitms 2  
  
Print #1 ,  
Print #1 , "-----------S T A R T-----------------"  
  
'Configure PC0 for input, triggered on falling edge  
Config Pinc.0 = Input  
```
Portc_pin0ctrl = &B00_011_010  
```vb
'^ ^  
'^ React on falling edge (010)  
'^  
'enable Pullup  
  
'Select PC0 as input to event channel 0  
'select the event source for Event Channel 0  
```
Evsys_ch0mux = &B0110_0_000 'Event Source for Event Channel 0 = Portc.0  
```vb
'^ ^  
'^ ^  
'^ Pin0  
'portC  
  
```
Evsys_ch0ctrl = &B0_00_0_0_111 '8 SAMPLES for Digital Filter  
```vb
'^  
'Digital Filter config  
Config Pinc.7 = Output  
'Event Channel 0 Ouput Configuration  
```
Portcfg_clkevout = &B0_0_01_0_0_00 'Output on PINC.7 /Clock Out must be disabled  
  
```vb
Print #1 , "Portcfg_clkevout = " ; Bin(portcfg_clkevout)  
Print #1 , "Mainloop -->"  
  
  
Do  
'IMPORTANT: YOU WILL SEE THE PIN CHANGES ALSO DURING WAIT 4 BECAUSE IT USE EVENT SYSTEM  
Wait 4  
  
'This shows how to manual fire an Event  
Set Evsys_strobe.0  
Loop  
  
End 'end program

```