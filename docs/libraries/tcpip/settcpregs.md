# SETTCPREGS

Action

Writes to an ethernet chip register

Syntax

SETTCPREGS address, var , bytes

Remarks

address | The address of the register. This must be the address of the MSB, or the address with the lowest address. The address should not include the base address.  
---|---  
var | The variable to write.  
bytes | The number of bytes to write.  
  
Most options are implemented with BASCOM statements or functions. When there is a need to write to the ethernet chip register you can use the SETTCPREGS command. It can write multiple bytes. It is important that you specify the lowest address. The SETTCPREGS statement will add the base address of the chip to the address so you should not add it yourself. Use the address from the datasheet.

The addresses are different for the W3100,W5100,W5200 and W5300. 

Some registers you might want to alter are the Retry Count Register(RCR) and Retry Time Register(RTR).

See also

[GETTCPREGS](gettcpregs.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------  
'name : regs_SPI.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : test custom regs reading writing  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-----------------------------------------------------------------------------------------  
$regfile = "m88def.dat" ' specify the used micro  
  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 80 ' default use 32 for the hardware stack  
$swstack = 128 ' default use 10 for the SW stack  
$framesize = 80 ' default use 40 for the frame space  
  
Dim L As Long  
  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = Low , Phase = 0 , Clockrate = 4 , Noss = 0  
'Init the spi pins  
```
Spiinit  
  
```vb
'we do the usual  
Print "Init TCP" ' display a message  
Enable Interrupts ' before we use config tcpip , we need to enable the interrupts  
Config Tcpip = Int1 , Mac = 12.128.12.34.56.78 , Ip = 192.168.1.70 , Submask = 255.255.255.0 , Gateway = 192.168.1.1 , Localport = 1000 , Tx = $55 , Rx = $55 , Chip = W5100 , Spi = 1  
Print "Init done"  
  
'set the IP address to 192.168.0.135  
```
Settcp 12.128.12.24.56.78 , 192.168.1.135 , 255.255.255.0 , 192.168.1.1  
  
'now read the IP address direct from the registers  
L = Gettcpregs(&H0f , 4)  
```vb
Print Ip2str(l)  
  
Dim B4 As Byte At L Overlay ' this byte is the same as the LSB of L  
  
'now make the IP address 192.168.1.136 by writing to the LSB  
```
B4 = 136  
Settcpregs &H0F , L , 4 'write  
  
'and check if it worked  
L = Gettcpregs(&H0f , 4)  
```vb
Print Ip2str(l)  
  
'and with PING you can check again that now it works  
  
  
End

```