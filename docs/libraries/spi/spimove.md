# SPIMOVE

Action

Sends and receives a value or a variable to the SPI-bus.

Syntax

var = SPIMOVE( source [,count] )

Syntax Xmega

var = SPIMOVE( source ,count , channel )

Syntax SPI1

var = SPI1MOVE( source [,count] )

Remarks

Var | The variable that is assigned with the received byte(s) from the SPI-bus.  
---|---  
Source | The variable or constant whose content must be send to the SPI-bus.  
Count | Optional byte value which specifies how many bytes need to be moved. Notice that for Xmega this parameter is not optional but mandatory.  
Channel | For Xmega only : the channel number or channel variable  
  
SPIMOVE always work on the first SPI interface (SPI0)

SPI1MOVE works on the second SPI interface (SPI1)

See also

[SPIIN](spiin.md) , [SPIINIT](spiinit.md) , [CONFIG SPI](config_spi.md) , [SPI1](spi1init_spi1in_spi1out_spi1mo.md)

Example

Config Spi = Soft , Din = Pinb.0 , Dout = Portb.1 , Ss = Portb.2 , Clock = Portb.3

Spiinit

Dim a(10) as Byte , X As Byte

Spiout A(1) , 5 'send 5 bytes

Spiout X , 1 'send 1 byte

A(1) = Spimove(5) ' move 5 to SPI and store result in a(1)

A(1) = Spimove(a(2),4) ' move 4 bytes from a(2) to a(1)

End

Example Xmega

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128A1_SPI_MOVE.bas  
' This sample demonstrates the Xmega128A1 SPI master mode SPIMOVE  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
Config Osc = Enabled , 32mhzosc = Enabled  
Config Sysclock = 32mhz '--> 32MHz  
  
  
Config Com1 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Waitms 2  
```
Open "COM1:" For Binary As #1  
```vb
Print #1 ,  
Print #1 , "------------SPI MASTER-Slave Test----------------"  
  
' Master = ATXMEGA128A1 running at 3.3 Volt  
' Slave = ATMEGA328P running at 3.3 Volt  
  
'We use Port E for SPI  
'Ddre = &B1011_0000  
'Bit7 = SCK = Output ------> SCK ATMEGA328P (PinB.5)  
'Bit6 = MISO = Input ------> MISO ATMEGA328P (PinB.4)  
'Bit5 = MOSI = Output ------> MOSI ATMEGA328P (PinB.3)  
'Bit4 = SS = Output ------> SS ATMEGA328P (PinB.2)  
```
Slave_select Alias Porte.4  
```vb
Set Slave_select  
  
Dim Switch_bit As Bit  
  
```
Switch Alias Pine.0 ' Switch connected to GND  
```vb
Config Xpin = Porte.0 , Outpull = Pullup  
  
  
  
Dim Bspivar As Byte  
Dim Spi_send_byte As Byte  
Dim Spi_receive_byte As Byte  
Dim Ar(4) As Byte  
  
  
'SPI, Master|Slave , MODE, clock division  
Config Spie = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk32 , Data_order = Msb , Ss = Auto  
'SS = Auto set the Slave Select (SS) automatically before a print #X or input #X command (including initialization of the pin)  
'Master SPI clock = 1MHz  
```
Open "SPIE" For Binary As #12  
  
  
```vb
Config Debounce = 50  
  
Do  
  
```
Debounce Switch , 0 , Switch_sub , Sub 'Switch Debouncing  
  
```vb
If Switch_bit = 1 Then 'When Switch pressed  
Reset Switch_bit  
  
```
Incr Spi_send_byte  
```vb
Print "Spi_send_byte = " ; Spi_send_byte  
  
'SEND TO SLAVE  
Print #12 , Spi_send_byte 'SEND ONE BYTE TO SLAVE  
  
Waitms 3  
  
'READ FROM SLAVE  
Input #12 , Spi_receive_byte 'READ ONE BYTE FROM SLAVE  
  
Print #1 , "Spi_receive_byte = " ; Spi_receive_byte  
  
'Lets move some bytes  
```
Ar(1) = Spimove(ar(1) , 4 , #12)  
```vb
End If  
  
  
Loop  
  
  
  
End 'end program  
  
'there is NO CLOSE for SPI  
  
  
```
Switch_sub:  
```vb
Set Switch_bit  
Return

```