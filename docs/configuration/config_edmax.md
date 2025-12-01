# CONFIG EDMAx

Action

Configures the enhanced direct memory access (DMA) channel of the XMEGA.

Syntax

CONFIG EDMACHx=enabled|disabled,BURSTLEN=bl, CHANRPT=chrpt, CTR=ctr, SINGLESHOT=ss, TCI=tci, EIL=eil,SAR=sar, SAM=sam,DAR=dar,DAM=dam, TRIGGER,trig, BTC=btc,SADR=sadr, DADR=dadr

Remarks

In order to understand the various options better, we first have a quick look at DMA. Please consult the help topic [CONFIG DMAx](config_dmachx.md) and the atmel documentation for the EDMA.

Normally, when you want to transfer data, the processor need to execute a number of operations.

The BASCOM MEMCOPY for example will use processor instructions like LD (load data) and ST(store data) in a loop.

If you want to clear 32KB of memory you need at least 32 K instructions. This will consume time, and all this time the processor can not handle other tasks.

In a PC, you do not want to use the processor to be busy when you load a file from disk. The EDMA controller will handle this. It can move blocks of memory between devices while the processor performs other tasks.

You can also send for example an array in SRAM to an USART over EDMA so the processor will not be busy handling the transfer from the Array to the USART.

There is also an example to receive bytes over USART to SRAM in the Bascom-AVR/Samples folders.

Before CONFIG EDMACHx can be used you need to use Config EDMA ([CONFIG_DMA](config_edma.md))

DMACHx | There are 4 DMA channels numbered 0-3. By default these DMA channels are disabled. Use ENABLED to enable the channel.   
---|---  
bl | BURSTLEN Each DMA channel has an internal transfer buffer that is either 1 or 2 byte long. The buffer is used to reduce the time the DMA controller occupy the bus. Options : \- 1 : 1 byte burst mode \- 2 : 2 byte burst mode  
chanrpt | Channel Repeat  Setting this bit enables the repeat mode. In repeat mode, this bit is cleared by hardware in the beginning of the last block transfer. Options : Enabled : enabled repeat mode Disabled : disabled repeat mode  
ctr | DMA Channel Transfer Request Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at the beginning of the data transfer Options : Enabled : request transfer  
ss | DMA Channel Single Shot Data transfer Setting this bit enables the single shot mode. The channel will then do a burst transfer of BL bytes on the transfer trigger. This bit can not be changed if the channel is busy.  Options : Enabled : enable SS mode.  
tci | DMA Channel Transaction Complete Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
eil | DMA Channel Error Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
sar | Source Address Reload The channel source address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA source address register is reloaded with initial value at end of  
each block transfer. BURST : DMA source address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA source address register is reloaded with initial value at  
end of each transaction.  
sam | Source Address Mode The address can be altered the following way : FIXED : The address remains the same. INC : The address is incremented by one  If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte.  
dar | Channel Destination Address Reload The channel destiny address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA destiny address register is reloaded with initial value at end of  
each block transfer. BURST : DMA destiny address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA destiny address register is reloaded with initial value at  
end of each transaction.  
dam | Destiny Address Mode The address can be altered the following way : FIXED : The address remains the same. INC : The address is incremented by one  If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte. In case of an byte array it would start with array(1) and the next byte would be array(2) which will be transferred and so on.  
trigger | Trigger Source Select The trigger selected which device triggers the DMA transfer. A zero (0) will disable a trigger. You can manual start a DATA TRANSFER with START DMACHx statement. You can find the hardware trigger values in the datasheet. For example, EVENTSYS channel 0 would be 1. And EVENSTYS channel 1 would be 1. In case of for example an USART you need to add the base value and add an offset. Example: Base value for USARTC0 is &H4B Offset for (RXC) Receive complete is &H00 Offset for (DRE) Data Register Empty is &H01 So when you want to use the DRE the trigger is &H4B + &H01 = &H4C  
btc | Block Transfer Count The BTC represents the 16-bit value TRFCNT. Which also means the max value is 64Kbyte. TRFCNT defines the number of bytes in a block transfer. The value of TRFCNT is decremented after each byte read by the DMA channel. When TRFCNT reaches zero, the register is reloaded with the last value written to it. When repeat is 1, this is the total amount of bytes to send in the DMA transaction.  
sadr | Source Address This is the address of the DMA source. For example, the address of a variable. Or the address of a register. Use [VARPTR](varptr.md)() to find the address of a variable. For example if the source address is an array: sadr = varptr(ar(1)) For example if the source address is an hardware address like from an USART: sadr = Varptr(usarte0_data) or ADC A Channel 0: Sadr = Varptr(adca_ch0_res)  
dadr | Destination Address The destiny address.  This can be also for example an array in SRAM: dadr = varptr(dest(1)) This can be also for example a hardware recourse like USART: Dadr = Varptr(usarte0_data) or for example for DAC B Channel 0: Dadr = Varptr(dacb_ch0datal)  
  
After you have configured the DMA channel, you can start the transfer with the START EDMACHx statement.

This will write the TRFREQ bit in the CTRLA register.

Setting the TRFREQ Bit (DMA Channel Transfer Request) requests a DATA TRANSFER on the EDMA channel.

Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at

the beginning of the data transfer.

See also

[CONFIG DMA](config_dma.md) , [START DMACHx](start.md), [ATXMEGA](atxmega.md) , [CONFIG EDMA](config_edma.md)

Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1-DMA.bas  
' This sample demonstrates DMA with an Xmega32E5  
'-----------------------------------------------------------------  
$regfile = "xm32e5def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Dim Ar(100) As Byte , Dest(100) As Byte , J As Byte , W As Word  
  
For J = 1 To 100  
```
Ar(j) = J ' create an array and assign a value  
```vb
Next  
  
Print "DMA DEMO"  
Config Edma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
  
'you can configure 4 DMA channels  
Config Edmach0 = Enabled , Burstlen = 1 , Chanrpt = Enabled , Tci = Off , Eil = Off , Sar = None , Sam = Inc , Dar = None , Dam = Inc , Trigger = 0 , Btc = 100 , Sadr = Varptr(ar(1)) , Dadr = Varptr(dest(1))  
  
```
Start Edmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
For J = 1 To 50  
Print J ; "-" ; Ar(j) ; "-" ; Dest(j) ' print the values  
Next  
End

```