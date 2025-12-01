# CONFIG DMACHx

Action

Configures the direct memory access (DMA) channel of the XMEGA.

Syntax

CONFIG DMACHx=enabled|disabled,BURSTLEN=bl, CHANRPT=chrpt, CTR=ctr, SINGLESHOT=ss, TCI=tci, EIL=eil,SAR=sar, SAM=sam,DAR=dar,DAM=dam, TRIGGER,trig, BTC=btc, REPEAT=rpt,SADR=sadr, DADR=dadr

Remarks

In order to understand the various options better, we first have a better look at DMA.

Normally, when you want to transfer data, the processor need to execute a number of operations.

The BASCOM MEMCOPY for example will use processor instructions like LD (load data) and ST(store data) in a loop.

If you want to clear 32KB of memory you need at least 32 K instructions. This will consume time, and all this time the processor can not handle other tasks.

In a PC, you do not want to use the processor to be busy when you load a file from disk. The DMA controller will handle this. It can move blocks of memory between devices.

You can also send for example an array in SRAM to an USART over DMA so the processor will not be busy handling the transfer from the Array to the USART. See also the example below.

There is also an example to receive bytes over USART to SRAM in the Bascom-AVR/Samples folders.

Before CONFIG DMACHx can be used you need to use Config Dma ([CONFIG_DMA](config_dma.md))

DMA Transaction

A complete DMA read and write operation between memories and/or peripherals is called a DMA transaction.

A transaction is done in data blocks and the size of the transaction (number of bytes to transfer) is selectable from software and controlled by the block size and repeat counter

settings. Each block transfer is divided into smaller bursts

Block Transfer and Repeat

The size of the block transfer is set by the Block Transfer Count Register, and can be anything from 1 byte to 64 KBytes.

A repeat counter can be enabled to set a number of repeated block transfers before a transaction is complete. The repeat is from 1 to 255 and unlimited repeat count can be achieved by

setting the repeat count to zero.

Burst Transfer

As the AVR CPU and DMA controller use the same data buses a block transfer is divided into smaller burst transfers. The burst transfer is selectable to 1, 2, 4, or 8 bytes.

This means that, if the DMA acquires a data bus and a transfer request is pending it will occupy the bus until all bytes in the burst transfer is transferred.

A bus arbiter controls when the DMA controller and the AVR CPU can use the bus. The CPU always has priority, so as long as the CPU request access to the bus, any pending burst transfer

must wait. The CPU requests bus access when it executes an instruction that write or read data to SRAM, I/O memory, EEPROM and the External Bus Interface

![dma](dma.jpg)

DMACHx | There are 4 DMA channels numbered 0-3. By default these DMA channels are disabled. Use ENABLED to enable the channel.   
---|---  
bl | BURSTLEN Each DMA channel has an internal transfer buffer that is used for 2, 4 and 8 byte burst transfers. When a transfer is triggered, a DMA channel will wait until the transfer buffer contains two bytes before the transfer starts. For 4 or 8 byte transfer, any remaining bytes is transferred as soon as they are ready for a DMA channel. The buffer is used to reduce the time the DMA controller occupy the bus. Options : \- 1 : 1 byte burst mode \- 2 : 2 byte burst mode \- 4 : 4 byte burst mode \- 8 : 8 byte burst mode  
chanrpt | Channel Repeat  Setting this bit enables the repeat mode. In repeat mode, this bit is cleared by hardware in the beginning of the last block transfer. The REPCNT register should be configured before setting the REPEAT bit. When using the CONFIG command, the compiler will handle this. Options : Enabled : enabled repeat mode Disabled : disabled repeat mode  
ctr | DMA Channel Transfer Request Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at the beginning of the data transfer Options : Enabled : request transfer  
ss | DMA Channel Single Shot Data transfer Setting this bit enables the single shot mode. The channel will then do a burst transfer of BL bytes on the transfer trigger. This bit can not be changed if the channel is busy.  Options : Enabled : enable SS mode.  
tci | DMA Channel Transaction Complete Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
eil | DMA Channel Error Interrupt Level The interrupt can be turned OFF, or be given a priority LO, MED or HI  
sar | Source Address Reload The channel source address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA source address register is reloaded with initial value at end of  
each block transfer. BURST : DMA source address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA source address register is reloaded with initial value at  
end of each transaction.  
sam | Source Address Mode The source address can be altered the following way : FIXED : The source address remains the same. INC : The source address is incremented by one.  DEC : The source address is decremented by one. If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the the source address is increased after each byte.  
dar | Channel Destination Address Reload The channel destiny address can be reloaded the following way: NONE : No reload performed. BLOCK : DMA destiny address register is reloaded with initial value at end of  
each block transfer. BURST : DMA destiny address register is reloaded with initial value at end of  
each burst transfer. TRANSACTION : DMA destiny address register is reloaded with initial value at  
end of each transaction.  
dam | Destiny Address Mode The destiny address can be altered the following way : FIXED : The destiny address remains the same. INC : The destiny address is incremented by one.  DEC : The destiny address is decremented by one. If you want to write to a PORT, for example to generate a wave, you would chose FIXED. But if you want to move a block of memory, you want to use INC so the destiny address is increased after each byte. In case of a byte array it would start with array(1) and the next byte would be array(2) which will be transferred and so on.  
trigger | Trigger Source Select The trigger selected which device triggers the DMA transfer. A zero (0) will disable a trigger. You can manual start a DATA TRANSFER with START DMACHx statement. You can find the hardware trigger values in the datasheet. For example, EVENTSYS channel 0 would be 1. And EVENSTYS channel 1 would be 1. In case of for example an USART you need to add the base value and add an offset. Example: Base value for USARTC0 is &H4B Offset for (RXC) Receive complete is &H00 Offset for (DRE) Data Register Empty is &H01 So when you want to use the DRE the trigger is &H4B + &H01 = &H4C  
btc | Block Transfer Count The BTC represents the 16-bit value TRFCNT. Which also means the max value is 64Kbyte. TRFCNT defines the number of bytes in a block transfer. The value of TRFCNT is decremented after each byte read by the DMA channel. When TRFCNT reaches zero, the register is reloaded with the last value written to it. When repeat is 1, this is the total amount of bytes to send in the DMA transaction.  
repeat | Repeat Counter Register REPCNTcounts how many times a block transfer is performed. For each block transfer this register will be decremented. Unlimited repeat is activated by setting this register to 0.  
sadr | Source Address This is the address of the DMA source. For example, the address of a variable. Or the address of a register. Use [VARPTR](varptr.md)() to find the address of a variable. For example if the source address is an array: sadr = varptr(ar(1)) For example if the source address is an hardware address like from an USART: sadr = Varptr(usarte0_data) or ADC A Channel 0: Sadr = Varptr(adca_ch0_res)  
dadr | Destination Address The destiny address.  This can be also for example an array in SRAM: dadr = varptr(dest(1)) This can be also for example a hardware recourse like USART: Dadr = Varptr(usarte0_data) or for example for DAC B Channel 0: Dadr = Varptr(dacb_ch0datal)  
  
After you have configured the DMA channel, you can start the transfer with the START DMACHx statement.

This will write the TRFREQ bit in the CTRLA register.

Setting the TRFREQ Bit (DMA Channel Transfer Request) requests a DATA TRANSFER on the DMA channel.

Setting this bit requests a data transfer on the DMA Channel. This bit is automatically cleared at

the beginning of the data transfer.

To enable the DMA Channel you need to set the Dma_chX_ctrla.7 bit.

For example for DMA Channel 0 this is Set Dma_ch0_ctrla.7

Setting this bit enables the DMA channel. This bit is automatically cleared when the transaction

is completed.

See also

[CONFIG DMA](config_dma.md) , [START DMACHx](start.md), [ATXMEGA](atxmega.md) , [CONFIG EDMA](config_edma.md) , [CONFIG EDMAx](config_edmax.md)

Example (copy SRAM Array to another SRAM Array over DMA):

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1-DMA.bas  
' This sample demonstrates DMA with an Xmega128A1  
'-----------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled 'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Com1 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
dim ar(100) as byte, dest(100) as byte,j as byte ,w as word  
  
for j=1 to 100  
```
ar(j)=j ' create an array and assign a value  
```vb
next  
  
print "DMA DEMO"  
config dma= enabled, doublebuf=disabled,cpm = RR ' enable DMA  
  
'you can configure 4 DMA channels  
config dmach0=enabled ,burstlen=8,chanrpt=enabled, tci=off,eil=off, sar=none,sam=inc,dar=none,dam=inc ,trigger=0,btc=100 ,repeat =1,sadr=varptr(ar(1)),dadr=varptr(dest(1))  
  
```
start dmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
for j=1 to 50  
print j;"-";ar(j);"-";dest(j) ' print the values  
next  
end

```
Example (send an array to USART over DMA):

  
```vb
'Terminal Output of following example:  
'(  
  
```
\----- Array to USART over DMA -----  
  
Hello Bascom  
Hello XMEGA  
  
```vb
')  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
Config Priority = Static , Vector = Application , Lo = Enabled  
  
' DMA Interrupt  
On Dma_ch0 Dma_ch0_int  
'Interrupt will be enabled with Tci = XX in Config DMAX  
  
Config Com5 = 38400 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM5:" For Binary As #5  
  
```vb
Dim My_array(15) As Byte  
Dim My_string As String * 14 At My_array(1) Overlay  
Dim Dma_ready As Bit  
Dim Dma_channel_0_error As Bit  
  
```
Enable_dmach0 Alias Dma_ch0_ctrla.7 'Enable DMA Channel 0  
  
```vb
Print #5 ,  
Print #5 , "----- Array to USART over DMA -----"  
Print #5 ,  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
'configure DMA channel  
Config Dmach0 = Disabled , Burstlen = 1 , Chanrpt = Disabled , Tci = Lo , Eil = Off , Singleshot = Enabled , Sar = Transaction , _  
```
Sam = Inc , Dar = None , Dam = Fixed , Trigger = &H8C , Btc = 14 , Repeat = 0 , Sadr = Varptr(my_array(1)) , Dadr = Varptr(usarte0_data)  
```vb
' BURSTLEN = 1  
' Tci = Lo , Eil = Off --> enable TRANSACTION COMPLETE Interrupt  
' Singleshot = Enabled --> Setting this bit enables the single shot mode. 

' The channel will then do a burst transfer of BL bytes on the transfer trigger.  
' SAR (Source Address Reload) = After each transaction  
' SAM = inc --> source address is increased after each byte  
' DAR = NONE --> No reload performed  
' DAM (Destiny Address Mode) --> Fixed --> The address remains the same  
' Trigger = &H8C --> Base Value of USARTE0 = &H8B + Offset for DRE (Data Register Empty)= 1 --> &H8C  
' BTC = 14 --> Block Transfer Count is 14 Byte  
' We start with Dmach0 = Disabled --> will be enabled when we need it  
  
' Start dmach0 --> will set the TRFREQ Bit (DMA Channel Transfer Request). 

' Setting this bit requests a DATA TRANSFER on the DMA channel.  
  
' We use here Enable_dmach0 Alias Dma_ch0_ctrla.7 This bit is automatically cleared when the DMA TRANSACTION is completed  
  
Enable Interrupts  
```
My_string = "Hello Bascom" + Chr(13) + Chr(10) ' Hello Bascom + Carriage Return + Line Feed  
  
Set Enable_dmach0 ' Enable the DMA Channel 0 (This bit is automatically cleard when transaction is completed)  
  
Bitwait Dma_ready , Set ' Wait until first DMA transaction is ready (DMA TRANSACTION COMPLETE Interrupt)  
Reset Dma_ready  
  
My_string = "Hello XMEGA" + Chr(13) + Chr(10)  
  
```vb
Set Enable_dmach0 ' Enable the DMA Channel 0 (This bit is automatically cleard when transaction is completed)  
  
End  
  
'----------[Interrupt Service Routines]-----------------------------------------  
  
' Dma_ch0_int is for DMA Channel ERROR Interrupt A N D for TRANSACTION COMPLETE Interrupt  
' Which Interrupt fired must be checked in Interrupt Service Routine  
  
```
Dma_ch0_int: ' DMA Transaction complete  
  
```vb
If Dma_intflags.0 = 1 Then ' Channel 0 Transaction Interrupt Flag  
Set Dma_intflags.0 ' Clear the Channel 0 Transaction Complete flag  
Set Dma_ready  
End If  
  
'(  
If Dma_intflags.4 = 1 Then ' Channel 0 ERROR Flag  
Set Dma_intflags.4 ' Clear the flag  
Set Dma_channel_0_error ' Channel 0 Error  
End If  
')  
  
Return

```