# CONFIG DACA|DACB

Action

This statement configures the DACA or DACB in the Xmega.

Syntax

CONFIG DACx=dac, IO0=IO0, IO1=IO1, INTERNAL_OUTPUT =INTOTP, CHANNEL=channel, TRIGGER_CH0=trig0,  TRIGGER_CH1=trig1, REFERENCE=ref, LEFT_ADJUSTED=adjusted, EVENT_CHANNEL=event, INTERVAL=interval, REFRESH=refresh

Remarks

DACX | Chose either DACA or DACB. DACA is connected to PORTA. DACB is connected to PORTB.  
---|---  
dac | ENABLED or DISABLED. Chose ENABLED to enable the DAC.  
IO0 | ENABLED or DISABLED. Chose ENABLED to enable output 0. Each DAC has 2 outputs. When multiple outputs are used, the DAC is using S&H.  
IO1 | ENABLED or DISABLED. Chose ENABLED to enable output 1.   
Intotp | ENABLED or DISABLED. Chose ENABLED to enable the internal output.  
Channel | SINGLE or DUAL. If both outputs are used, you need to enable the second output with IO1.  
Trig0 | ENABLED or DISABLED. Chose ENABLED to enable the trigger of channel 0.  
Trig1 | ENABLED or DISABLED. Chose ENABLED to enable the trigger of channel 1.  
Ref | The DAC needs a stable voltage reference. You can chose one of the following: \- INT1V. This will select the internal 1V reference \- AVCC. This will use AVCC as reference. \- AREFA. This will use AREFA as reference. \- AREFB. This will use AREFB as reference. The output of the DAC can never be higher then the voltage reference. When you chose INT1V, the output is from 0-1V in 4096 steps.  
Adjusted | ENABLED or DISABLED. By default the DAC output is right adjusted (this means the first 8 Bit are in the Low Byte and the following 4 Bit in the High Byte of the 16-bit Register).  You can left alight the result.   
Event | The event channel to use for the event system.   
Interval | The minimum interval between 2 conversions.  This is a value of : 1,2,4,8,16,32,64 or 128. The default in the register is 64. A value of 64 will give an interval of 64 clock cycles. The value is set in clock cycles and the time in Âµ Second depend on the CLKper (Peripheral Clock) setting. The minimum in SINGLE Channel mode is 1ÂµS (1M conversions per seconds). The minimum in DUAL Channel mode (S/H mode) should no be below 1.5ÂµS (666K conversions per second). In DUAL Channel mode the 50% increase of peripheral clock cycles is AUTOMATICALLY added by the XMEGA chip.  
Refresh | The DAC channel refresh timing. This is the interval refresh time in DUAL channel mode. Possible values: OFF 16, 32, 128, 256, 512, 1014, 2048, 4096, 8192, 16384, 32768, 65536.  A value of 16 means an interval of 16 clock cycles. The default loaded is 64. Note: Higher refresh rates causes higher power consumption. Manual conversions or Events between the refresh intervals do NOT affect the refresh intervals. This means the channels will be refreshed at a constant timing even when the data register are for example updated in between.  
  
The DAC data register is available in the DACA0, DACA1 and DACB0 and DACB1 variables.

The DAC module can output conversion rates up to 1 M conversions per second with a resolution of 12 bits. 

A DAC conversion can be triggered by:

•| writing to the DAC data register (DACA0, DACA1 and DACB0 and DACB1)  
---|---  
  
•| an Event over Event System (when configured to trigger from Event system the DAC data register can be updated several times without triggering an conversion. In case of an Event the latest value in the DAC data register will be used for conversion)  
---|---  
  
Trigger mode can be different between DAC Channels. For example DAC Channel 0 can be setup to work with Events while Channel 1 can be configured to start conversion when DAC data register is updated.

How to handle the two Data Channels with one conversion Block:

  
```vb
' +-----------+ +------------------+  
' | Channel 0 | -------->| |-----> Out 0  
' +-----------+ | CONVERSION BLOCK |  
' +-----------+ | |  
' | Channel 1 | -------->| |-----> Out 1  
' +-----------+ +------------------+  
' |

' |

' Event System

```
The fact that there are two data channels but one conversion block it needs to be configured by CHANNEL.

•| If Channel is SINGLE: Channel 0 is used in continuous-drive output mode and Channel 0 is then always connected to conversion block.  
---|---  
  
•| If Channel is DUAL: Both channels work in Sample and Hold (S/H) mode. The Sample and Hold keep the DAC output values during a conversion of the other channel. To refresh the output value in DUAL channel mode the refresh timing can be set.   
---|---  
  
What can you drive with the XMEGA DAC outputs ?

\- The ouputs can drive loads of 1KOhm or capacitive loads of 100pF

It is possible to use the XMEGA DMA Controller to output data on DAC Channels. 

See [CONFIG DMACHx](config_dmachx.md), [CONFIG DMA](config_dma.md)

See also Example Nr 2 below.

Calibration of DAC:

To Calibrate to DAC you can use the values from the signature row or you can change manual the Dacb_ch0offsetcal and Dacb_gaincal register.

```vb
For example for using signature row for DACB Ch0 this is:

'DACB  
```
B = Readsig(32) 'DACB Calibration Byte 0 (DACBOFFCAL)  
Dacb_ch0offsetcal = B 'write to the DACB offset register  
Print #1 , "DACB Calibration Byte 0 = " ; B  
B = Readsig(33) 'DACB Calibration Byte 1 (DACBGAINCAL)  
Dacb_gaincal = B  
Print #1 , "DACB Calibration Byte 1 = " ; B

See also Atmel Application Note AVR1301 for further details.

See also

[START](start.md) , [STOP](stop.md),[ CONFIG EVENT_SYSTEM](config_event_system.md)

Example Nr 1:

(For another example see also the example xm128a1.bas from the samples\chips folder)

  
```vb
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
Dim Var As Byte  
  
Config Portf.0 = Output  
```
Led1 Alias Portf.0  
  
Config Portf.1 = Output  
Led2 Alias Portf.1  
  
  
  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single , Reference = Int1v , Interval = 64 , Refresh = 64  
Dacb0 = 4095 '1 V output on portb.2  
  
```vb
'Start Dacb ' to enable it  
'Stop Dacb ' to disable it  
  
Do  
  
```
Incr Var  
Waitms 500  
Dacb0 = 4095 '1 V output on portb.2  
```vb
Set Led1  
Reset Led2  
  
Waitms 500  
Reset Led1  
```
Dacb0 = 0 '0 V output on portb.2  
```vb
Set Led2  
  
Print #1 , "Tick " ; Var  
  
Loop  
  
End 'end program

```
Example Nr 2 (Ouput an Array of data from SRAM to DAC B over DMA):

(This example is generating an sawtooth wave on DAC B Channel 0 = Portb.2 on ATXMEGA256A3B)

  
```vb
' Ouput an Array of data from SRAM to DAC B over DMA  
  
' Timing: Timer/Counter TC0 feed the Event Channel 0  
' Event Channel 0 feed the DAC B Channel 0  
  
' Array Channel_0(1) is a word array filled with values  
  
' DMA Channel 0 start at Channel_0(1) and increment until 8192 Byte (= 2*4096). After the DMA transaction the source address will be reloaded  
' The destination address is the data register of DAC B Channel 0 and is incrementd once (to update the Low Byte and High Byte of the 12-Bit output value)  
  
'Frequency of output signal = 32MHz/32 = 1MHz --> 1MHz/4096 (Sample_Count) = appx. 244Hz  
  
$regfile = "xm256a3bdef.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Priority = Static , Vector = Application , Lo = Enabled  
  
Config Com7 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8 'Portf.2 and Portf.3 is COM7  
```
Open "COM7:" For Binary As #1  
  
```vb
Print #1 ,  
Print #1 , "Start DAC B Channel 0 over DMA Example"  
  
  
Dim Var As Byte  
  
Config Portf.0 = Output  
```
Led1 Alias Portf.0  
  
Config Portf.1 = Output  
Led2 Alias Portf.1  
  
  
Const Sample_count = 4096 'Number of 12-Bit Samples (Measurement Values)  
```vb
Dim Channel_0(sample_count) As Word 'Array  
Dim Dma_ready As Bit  
Dim Dma_channel_0_error As Bit  
  
  
```
Enable_dmach0 Alias Dma_ch0_ctrla.7 'Enable DMA Channel 0  
  
```vb
Dim I As Word  
  
For I = 1 To 4096 'From 0V .....3.3Volt (with Reference = avcc)  
```
Channel_0(i) = I 'Generate a Sawtooth wave  
```vb
Next  
  
  
Config Tcc0 = Normal , Prescale = 1 'Setup Timer/Counter TC0 in nomal mode , Prescale = 1 --> no prescaler  
```
Tcc0_per = 31 '31 --> 32MHz/32 = 1MHz  
  
```vb
Config Event_system = Dummy , Mux0 = Tcc0_ovf 'TCC 0 overflow --> Event Channel 0  
  
  
' The xm256a3bd only have one DAC (DAC B)  
Config Dacb = Enabled , Io0 = Enabled , Channel = Single , Trigger_ch0 = Enabled , Event_channel = 0 , Reference = Avcc , Interval = 4 , Refresh = 16  
' DAC B Channel 0 is triggered by Event Channel 0  
  
  
' DMA Interrupt  
On Dma_ch0 Dma_ch0_int 'Interrupt will be enabled with Tci = XX in Config DMAX  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA, Double Buffer disabled  
  
' DMA Channel 0 is used here  
Config Dmach0 = Enabled , Burstlen = 2 , Chanrpt = Enabled , Tci = Lo , Eil = Lo , Singleshot = Enabled , _  
```
Sar = Transaction , Sam = Inc , Dar = Burst , Dam = Inc , Trigger = &H25 , Btc = 8192 , Repeat = 0 , Sadr = Varptr(channel_0(1)) , Dadr = Varptr(dacb_ch0datal)  
  
```vb
' Trigger = &H25 (DAC B Base Level Trigger) + Channel 0 = &H00 --> &H25  
' Burstlen is 2 byte because the DAC output value is a 12-Bit value you need to transfer 2 byte  
' Source address (the array) is incremented until all bytes transfered (8192 byte)  
' Destination address (DAC B Channel 0) is incremented once to transfer the low byte and high byte of the 12-bit value  
' BTC = 8192 BYTE (needed to transfer the 4096 word)  
' Reapeat = 0 --> repeat forever  
  
  
Enable Interrupts  
  
  
  
'Frequency of output signal = 32MHz/32 = 1MHz --> 1MHz/4096 (Sample_Count) = appx. 244Hz  
  
Do  
  
  
Loop  
  
End 'end program  
  
  
'----------------------[Interrupt Service Routines]-----------------------------  
  
' Dma_ch0_int is for DMA Channel ERROR Interrupt A N D for TRANSACTION COMPLETE Interrupt  
' Which Interrupt fired must be checked in Interrupt Service Routine  
```
Dma_ch0_int:  
  
```vb
If Dma_intflags.0 = 1 Then 'Channel 0 Transaction Interrupt Flag  
Set Dma_intflags.0 'Clear the Channel 0 Transaction Complete flag  
Set Dma_ready  
End If  
  
If Dma_intflags.4 = 1 Then 'Channel 0 ERROR Flag  
Set Dma_intflags.4 'Clear the flag  
Set Dma_channel_0_error 'Channel 0 Error  
End If  
  
Return

```