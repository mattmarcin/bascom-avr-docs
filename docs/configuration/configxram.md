# CONFIG XRAM

Action

Instruct the compiler to set options for external memory access.

Syntax

CONFIG XRAM = mode [ , WaitstateLS=wls] [ , WaitStateHS=whs ]

Syntax Older chips

CONFIG XRAM = mode , Waitstate=wls

Syntax Xmega

CONFIG XRAM = mode, sdbus=sdbus,lpc=lpc,sdcol=sdcol,sdcas=sdcas,sdrow=sdrow,refresh=refresh,initdelay=initdelay,modedelay=modedelay,rowcycledelay=rowcycledelay,rowprechargedelay=rowprechargedelay,wrdelay=wrdelay,ersdelay=esrdelay, rowcoldelay=rowcoldelay,modesel0=sel,adrsize0=adr,baseadr0=base,modesel1=sel,adrsize1=adr,baseadr1=base,modesel2=sel,adrsize2=adr,baseadr2=base,modesel3=sel,adrsize3=adr,baseadr3=base

See also: [Adding XRAM with External Memory Interface](adding_xram.md)

Remarks AVR

Mode | The memory mode. This is either enabled or disabled. By default, external memory access is disabled.  
---|---  
Wls | When external memory access is enabled, some chips allow you to set a wait state. The number of modes depend on the chip. A modern chip such as the Mega8515 has 4 modes : 0 - no wait states 1 - 1 cycle wait state during read/write 2 - 2 cycle wait state during read/write 3 - 2 cycle wait state during read/write and 1 before new address output WLS works on the lower sector. Provided that the chip supports this.  
Whs | When external memory access is enabled, some chips allow you to set a wait state. The number of modes depend on the chip. A modern chip such as the Mega8515 has 4 modes : 0 - no wait states 1 - 1 cycle wait state during read/write 2 - 2 cycle wait state during read/write 3 - 2 cycle wait state during read/write and 1 before new address output WHS works on the high sector. Provided that the chip supports this.  
  
Wait states are needed in case you connect equipment to the bus, that is relatively slow. Especial older electronics/chips.

Some AVR chips also allow you to divide the memory map into sections. By default the total XRAM memory address is selected when you set a wait state.

Older chips like the 90S8515 do not have a lower and upper sector. The setting is for all the memory in that case.

The $XA directive should not be used anymore. It is the same as CONFIG XRAM=Enabled.

![notice](notice.jpg)When using IDLE or another power down mode, it might be needed to use CONFIG XRAM again, after the chip wakes from the power down mode. 

[[See also Adding XRAM]](<adding_xram.htm>)

XMEGA

Mode | The memory mode. There are 4 options: \- DISABLED, this will turn off the EBI and is the default \- 3PORT. For using EBI in 3 PORT mode. \- 4PORT. For using EBI in 4 PORT mode. \- 2PORT. For using EBI in 2 PORT mode. The EBI uses specific ports for each of the modes.  
---|---  
sdbus | When using SDRAM, you need to configure 4 bit or 8 bit data width. For the 3 PORT mode you need to use 4 bit SDRAM. Options are : 4 and 8.  
  
|   
  
sdcol | When using SDRAM, you need to configure the number of columns of the chip. This depends on the chip. You can find this info in the datasheet of the SDRAM chip. For example a chip with column address A0-A9 would use 10 bits. Options : 8 ,9, 10 or 11.  
sdrow | When using SDRAM, you need to configure the number of rows of the chip. This depends on the chip. You can find this info in the datasheet of the SDRAM chip.  Options : 11 or 12.  
sdcas | When using SDRAM you can configure the CAS latency as a number of Peripheral 2x Clock cycles. By default this is two Peripheral 2x Clock cycles.  Options are : -2 : CAS latency is two Peripheral 2x Clock cycles -3 : CAS latency is three Peripheral 2x Clock cycles  
refresh | When using SDRAM this value sets the refresh period as a number of peripheral clock cycles. Use a value between 0-1023. The value depends on the chip.  
initdelay | When using SDRAM this value sets the delay of the initialization sequence that is sent after the voltages have been stabilized and the SDRAM clock is stable. The value is in the range of 0-16384  
modedelay | When using SDRAM this value select the delay between Mode Register command and an Activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-3  
rowcycledelay | When using SDRAM this value select the delay between a refresh an and Activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
rowprechargedelay | When using SDRAM this value select the delay between a pre-charge command and another command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
wrdelay | When using SDRAM this value selects the write recovery time in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-3  
esrdelay | When using SDRAM this value selects the delay between CKE set high and activate command in number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
rowcoldelay | When using SDRAM this value selects the delay between an activate command and a read/write command as a number of Peripheral 2x clock (CLKPER2) cycles. The range is between 0-7  
  
| The options ending with x, are available multiple times.(0-3) So there is an option named selfrefresh0, selfrefresh1, selfrefresh2 and selfrefresh3.  
selfrefreshX | When using SDRAM this options can turn on/off self refresh of the SDRAM. Not all SDRAM have this capability. Valid options are : \- ENABLED \- DISABLED. This is the default.  
sdmodeX | When using SDRAM this option sets the SDRAM mode. This is either NORMAL (default) or LOAD.  
modeselX | This option selects the MODE of the CS line.  There are 4 CS lines and modes. When using SDRAM you can only select modesel3 to configure the SDRAM. The following options are possible: \- DISABLE \- SRAM \- LPC (this is SRAM in low pin count mode) \- SDRAM  
adrsizeX | This options sets the address size for the chip select. This is the size of the block above the base address and determines which address lines are compared to generate the CS. Options are: 256b , 256 bytes, address 8:23 512b, 512 bytes, address 9:23  1K , 1 KB , address 10:23 2K , 2 KB , address 11:23 4K , 4 KB , address 12:23 8K, 8 KB , address 13:23 16K , 16 KB , address 14:23 32K , 32 KB , address 15:23 64K , 64 KB , address 16:23 128K , 128 KB, address 17:23 256K , 256 KB , address 18:23 512K , 512 KB , address 19:23 1M , 1 MB, address 20:23 2M , 2 MB , address 21:23 4M , 4 MB , address 22:23 8M , 8 MB, address 23 16M , 16 MB   
baseadrX | This option sets the chip base address which is the lowest address in the address space enabled by the chip select. The value is a word and sets address bits 12:23. Bits 0:11 are unused and need to be 0. For an 8 MB SDRAM the valid values are 0 and &H800000. Since the lower bits are not used the address is divided by 256 by the compiler. When using 0, the memory overlaps the SRAM which is not a big problem with 8MB of ram!  
  
|   
  
| In SRAM mode there are some other options you must set  
lpc | This sets the ALE mode in LPC SRAM mode.  Options are :  ALE1 : data multiplexed with address byte 0 ALE12 : data multiplexed with address byte 0 and 1  
ale | This sets the ALE mode in normal SRAM mode. Options are : ALE1 : address byte 0 and 1 multiplexed ALE2 : address byte 0 and 2 multiplexed ALE12 : address byte 0, 1 and 2 multiplexed NOALE : No address multiplexing  
waitstateX | The wait state selects the wait states for SRAM and SRAM LPC access as a number of peripheral 2x clock cycles. This is a value in the range from 0-7  
  
![notice](notice.jpg)While the EBI (External Bus Interface) can be configured to use a big 8 MB or 16 MB SDRAM, the compiler was changed in order to support more then 64KB of RAM (you need BASCOM-AVR Verison 2.0.7.4 or higher).

For 3PORT , 4-bit SDRAM mode the ports are set to the right direction and level. For all other modes you need to do this.

An example on how to determine the columns and rows is shown below:

![sdram](sdram.png)

In 4 bit data mode, you use 16 Meg x 4, the row addressing is A0-A11 thus 12 bit and the column addressing is A0-A9 thus 10 bit.

See also

[$XA](xa.md) , [$WAITSTATE](_waitstate.md), [Memory Usage](memory_usage.md), [Adding Xram](adding_xram.md)

ASM

NONE

Example

CONFIG XRAM = Enabled, WaitstateLS=1 , WaitstateHS=2

Xmega SRAM Example

CONFIG XRAM=3PORT , MODESEL3=SRAM, ADRSIZE3=1M , BASEADR3=&h100000 , ALE

= ALE1 , WAITSTATE3 = 0

Xmega Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-XRAM-SDRAM-XPLAIN.bas  
' This sample demonstrates the Xmega128A1 XRAM SDRAM  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
$xramsize = &H800000  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
'for xplain we need 9600 baud  
Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Dim B As Byte , B1 As Byte , B2 As Byte  
Config Porte = Output  
For B = 1 To 5  
Toggle Porte  
Waitms 1000  
Next  
  
Print "Xplain SDRAM test"  
'the XPLAIN has a 64 MBit SDRAM which is 8 MByte, it is connected in 3 port, 4 bit databus mode  
'in the PDF of the SDRAM you can see it is connected as 16 Meg x 4. Refreshcount is 4K and the row address is A0-A11, column addressing is A0-A9  
Config Xram = 3port , Sdbus = 4 , Sdcol = 10 , Sdcas = 3 , Sdrow = 12 , Refresh = 500 , Initdelay = 3200 , Modedelay = 2 , Rowcycledelay = 7 , Rowprechargedelay = 7 , Wrdelay = 1 , Esrdelay = 7 , Rowcoldelay = 7 , Modesel3 = Sdram , Adrsize3 = 8m , Baseadr3 = &H0000  
'the config above will set the port registers correct. it will also wait for Ebi_cs3_ctrlb.7  
'for all other modes you need to do this yourself !  
  
Dim X(65000) As Xram Byte , B as byte  
  
Print "SRAM"  
```
X(10000) = 100 ' this will use normal SRAM  
B = X(10000)  
```vb
Print "result : " ; B  
  
End

```
Another ATXMEGA Example:

  
```vb
'Example to copy a SRAM Array to a XRAM Array over Direct Memory Access (DMA)  
  
  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
' for xplain you need 9600 baud  
' Config Com1 = 9600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Config Com5 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM5:" For Binary As #1  
  
```vb
'SRAM Variables  
Dim Ar(100) As Byte , J As Word , W As Word  
Dim B As Byte  
  
  
' Demoboards like XPLAIN has a 64 MBit SDRAM (MT48LC16M4A2TG) which is 8 MByte, it is connected in 3 port, 4 bit databus mode  
' http://www.micron.com/products/ProductDetails.html?product=products/dram/sdram/MT48LC16M4A2TG-75  
' in the PDF of the SDRAM you can see it is connected as 16 Meg x 4. Refreshcount is 4K and the row address is A0-A11, column addressing is A0-A9  
' SDRAM = SYNCHRONOUS DRAM  
Config Xram = 3port , Sdbus = 4 , Sdcol = 10 , Sdcas = 3 , Sdrow = 12 , Refresh = 500 , Initdelay = 3200 , Modedelay = 2 , Rowcycledelay = 7 , Rowprechargedelay = 7 , Wrdelay = 1 , Esrdelay = 7 , Rowcoldelay = 7 , Modesel3 = Sdram , Adrsize3 = 8m , Baseadr3 = &H0000  
' the config above will set the port registers correct. it will also wait for Ebi_cs3_ctrlb.7  
' for all other modes you need to do this yourself !  
  
$xramsize = 8000000 ' 8 MByte  
  
'XRAM Variables  
Dim Dummy(100000) As Xram Byte 'Xram Variable with 100000 Bytes to ensure we are working above 64KByte  
Dim Dest(100) As Xram Byte 'Next Xram Var with 100 Byte  
  
  
For J = 1 To 100  
```
Ar(j) = J ' create an array and assign a value  
```vb
Next  
  
Print #1 , "Start DMA DEMO --> copy SRAM Array to XRAM Array"  
Config Dma = Enabled , Doublebuf = Disabled , Cpm = Rr ' enable DMA  
  
  
'you can configure 4 DMA channels  
Config Dmach0 = Enabled , Burstlen = 8 , Chanrpt = Enabled , Tci = Off , Eil = Off , Sar = None , Sam = Inc , Dar = None , Dam = Inc , Trigger = 0 , Btc = 100 , Repeat = 1 , Sadr = Varptr(ar(1)) , Dadr = Varptr(dest(1))  
  
```
Start Dmach0 ' this will do a manual/software DMA transfer, when trigger<>0 you can use a hardware event as a trigger source  
  
```vb
'-------------------------------------------------------------------------------  
For J = 1 To 50  
```
B = Dest(j) 'This step is needed to work with XRAM above 64KByte  
```vb
Print #1 , J ; "-" ; Ar(j) ; "-" ; B ' print the values  
Next  
  
'-------------------------------------------------------------------------------  
  
  
  
End  
  
'end program  
  
  
  
  
'(  
```
Terminal Output of example:  
  
Start DMA DEMO --> copy SRAM Array to XRAM Array  
1-1-1  
2-2-2  
3-3-3  
4-4-4  
5-5-5  
6-6-6  
7-7-7  
8-8-8  
9-9-9  
10-10-10  
11-11-11  
12-12-12  
13-13-13  
14-14-14  
15-15-15  
16-16-16  
17-17-17  
18-18-18  
19-19-19  
20-20-20  
21-21-21  
22-22-22  
23-23-23  
24-24-24  
25-25-25  
26-26-26  
27-27-27  
28-28-28  
29-29-29  
30-30-30  
31-31-31  
32-32-32  
33-33-33  
34-34-34  
35-35-35  
36-36-36  
37-37-37  
38-38-38  
39-39-39  
40-40-40  
41-41-41  
42-42-42  
43-43-43  
44-44-44  
45-45-45  
46-46-46  
47-47-47  
48-48-48  
49-49-49  
50-50-50  
')