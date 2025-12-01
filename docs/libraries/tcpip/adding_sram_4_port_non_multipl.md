# Adding SRAM 4-port Non Multiplexed

The following information was contributed by Juergen Bitzer.

![Adding sram 4port non multiplexed](adding sram 4port non multiplexed.zoom79.png)

The EBI allows to use an SRAM in 4-port non multiplexed mode. This means that you need little parts but you loose 4 ports.

Example

```vb
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = &H32  
$swstack = &H32  
$framesize = &H32  
$xramstart = &H100000  
$xramsize = &H080000  
  
'------------------  
' CPU:  
' ATXMEGA128A1U-AU : 2,23/100 Mouser Muss -->A1U-AU<\-- sein !!!  
' ATXMEGA64A1U-AU  
'------------------  
' SRam:  
' 512 KB AS6C4008-55PCN : SRAM 4MB 2.7V-5.5V, 512KX8, PDIP32  
  
' 512 KB AS6C4008-55SIN : SRAM 4MB 2.7V-5.5V, 512KX8, SOP32  
' 512 KB AS6C4008-55SIN : SRAM 4MB 2.7V-5.5V, 512KX8, SOP32  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
  
' #### Four Port SRAM ####  
' MODE SRAM 4Port direkt  
  
' PortH.0 - Pin 55 /WR  
' PortH.1 - Pin 56 /RD  
  
' PortE.4 - Pin 39 /CS0 / A16 -> CS0: SRAM 512 KB  
' PortE.5 - Pin 40 /CS1 / A17 -> CS1: unbenutzt  
' PortE.6 - Pin 41 /CS2 / A18 -> CS2: unbenutzt  
' PortE.7 - Pin 42 /CS3 / A19 -> CS3: unbenutzt  
  
' PortJ.0 - Pin 65 D0 -> SRam  
' PortJ.1 - Pin 66 D1 -> SRam  
' PortJ.2 - Pin 67 D2 -> SRam  
' PortJ.3 - Pin 68 D3 -> SRam  
' PortJ.4 - Pin 69 D4 -> SRam  
' PortJ.5 - Pin 70 D5 -> SRam  
' PortJ.6 - Pin 71 D6 -> SRam  
' PortJ.7 - Pin 72 D7 -> SRam  
  
' PortK.0 - Pin 75 A0 -> SRam  
' PortK.1 - Pin 76 A1 -> SRam  
' PortK.2 - Pin 77 A2 -> SRam  
' PortK.3 - Pin 78 A3 -> SRam  
' PortK.4 - Pin 79 A4 -> SRam  
' PortK.5 - Pin 80 A5 -> SRam  
' PortK.6 - Pin 81 A6 -> SRam  
' PortK.7 - Pin 82 A7 -> SRam  
  
' PortF.0 - Pin 45 A8 -> SRam  
' PortF.1 - Pin 46 A9 -> SRam  
' PortF.2 - Pin 47 A10 -> SRam  
' PortF.3 - Pin 48 A11 -> SRam  
' PortF.4 - Pin 49 A12 -> SRam  
' PortF.5 - Pin 40 A13 -> SRam  
' PortF.6 - Pin 41 A14 -> SRam  
' PortF.7 - Pin 42 A15 -> SRam  
  
' PortH.2 - Pin 57 A16 -> SRam  
' PortH.3 - Pin 58 A17 -> SRam  
' PortH.4 - Pin 59 A18 -> SRam  
' PortH.5 - Pin 60 A19 - unbenutzt  
' PortH.6 - Pin 61 A20 - unbenutzt  
' PortH.7 - Pin 62 A21 - unbenutzt  
  
'-------------------------------------------------------------------------------  
'----------generate a 32 MHz system clock by use of the PLL (2MHz * 23 = 46MHz)  
  
Config Osc = Disabled , Extosc = Enabled  
  
'Set the Multiplication factor and select the clock Reference for the PLL  
'Osc_pllctrl = &B00_0_10100 '2MHz clock Source and Multiplication factor = 23  
' 00 : 2 MHz internal OSC  
' 01 : Reerved  
' 10 : 32 MHz internal OSC  
' 11 : External Clock Source  
' 1 : 0=PLL-Output devided by 1 |1=PLL-Output devided by 2  
' xxxxx: Multiplikation of PLL 1-31  
```
Osc_pllctrl = &B11_0_01000 : Const Mhz = 32 ' 32 MHz  
  
```vb
'enable PLL  
Set Osc_ctrl.4 'PLL enable  
  
'configure the systemclock  
Config Sysclock = Pll 'use PLL  
  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
```
Open "com1:" For Binary As #1  
  
' Termninal initialisieren  
Printbin #1 , &H1B ; &H5B ; &H30 ; &H6D ' All attributes off(normal)  
Printbin #1 , &H1B ; &H5B ; &H32 ; &H4A ' Bildschirm löschen  
Printbin #1 , &H1B ; &H5B ; &H48 ; ' Cursor Home  
Printbin #1 , &H1B ; &H5B ; &H3F ; &H32 ; &H35 ; &H68 ; ' Cursor an  
  
```vb
'-------------------------------------------------------------------------------  
' Einstellungen externer Speicher  
' Alle EBI-Ports müssen auf OUTPUT  
' ALLE Ports, die ATKIV-LOW sind müssen auf 1 gesetzt werden !!!  
' ALLE Ports, die ATKIV-HIGH sind müssen auf 0 gesetzt werden !!!  
  
Print #1 , "Config Ports for external Adress / Data-Bus with no ALE... ";  
  
```
Portj_dirset = &B1111_1111 : Portj = &B0000_0000 ' D0:7  
Portj_pin0ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin1ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin2ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin3ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin4ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin5ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin6ctrl = &B0_0_000_000 'Totem (PushPull)  
Portj_pin7ctrl = &B0_0_000_000 'Totem (PushPull)  
  
Portk_dirset = &B1111_1111 : Portk = &B1111_1111 ' A0:7  
Portk_pin0ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin1ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portk_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
```vb
' PortX_pinYctrl = &B0_0_001_000 : X= Port A... Y= Bit Nr. 0-7  
' X :7 : 0= SlewRate normal, 1= SlewRate limited  
' X :6 : 0= IO normal, 1= IO inverted  
' XXX :5:3: 000 = Totem (PushPull)  
' XXX :5:3: 001 = Totem + Buskeeper  
' XXX :5:3: 010 = Totem + Pulldown on Input  
' XXX :5:3: 011 = Totem + PullUp on Input  
' XXX :5:3: 100 = Wired or  
' XXX :5:3: 101 = Wired and  
' XXX :5:3: 110 = Wired Or + PullDown  
' XXX :5:3: 111 = Wired And + PullUp  
' XXX:2:0: 000 = Both edges trigger port Interrupts / Events  
' XXX:2:0: 001 = Rising edge trigger port Interrupts / Events  
' XXX:2:0: 010 = Falling edge trigger port Interrupts / Events  
' XXX:2:0: 011 = Low Level trigger port Interrupts / Events  
' XXX:2:0: 100 = Reserved  
' XXX:2:0: 101 = Reserved  
' XXX:2:0: 110 = Reserved  
' XXX:2:0: 111 = Input Buffer Disabled (Only Port A to F) for use with ADC or AC  
  
  
```
Portf_dirset = &B1111_1111 : Portf = &B1111_1111 ' A8:15  
Portf_pin0ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin1ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Portf_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
Porth_dirset = &B1111_1111 : Porth = &B1111_1111 ' WR, RD , A16, A17, A18, A19, A20, A21  
Porth_pin0ctrl = &B0_0_000_000 'Totem (PushPull)  
Porth_pin1ctrl = &B0_0_000_000 'Totem (PushPull)  
Porth_pin2ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin3ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin4ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin5ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin6ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
Porth_pin7ctrl = &B0_0_001_000 'Totem (PushPull) + Buskeeper  
  
Porte_dirset = &B1111_1111 : Porte = &B1111_0000 ' CS3, CS2, CS1, CS0  
Porte_pin0ctrl = &B0_0_000_000 'Totem (PushPull) CS3  
Porte_pin1ctrl = &B0_0_000_000 'Totem (PushPull) CS2 SRAM  
Porte_pin2ctrl = &B0_0_000_000 'Totem (PushPull) CS1 SRAM  
Porte_pin3ctrl = &B0_0_000_000 'Totem (PushPull) CS0 TFT  
Porte_pin4ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin5ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin6ctrl = &B0_0_000_000 'Totem (PushPull)  
Porte_pin7ctrl = &B0_0_000_000 'Totem (PushPull)  
  
  
```vb
' EBI-OUT legt die 4 ChipSelect's auf einen anderen Port, damit die Adressleitungen  
' A16 bis A21 auf Port-H frei wird.  
```
Portcfg_ebiout = &B0000_00_11  
```vb
' XXXX : RESERVED  
' -> 00 : EBI Port3 adress output on PORT-F 0..7: SD: 4'h0, A[11:8] - SR or SR-LPC with SD on CS3: A[23:16] - SR NoAle or ALE1: A[15:8]  
' 01 : EBI Port3 adress output on PORT-E 0..7: SD: 4'h0, A[11:8] - SR or SR-LPC with SD on CS3: A[23:16] - SR NoAle or ALE1: A[15:8]  
' 10 : EBI Port3 adress output on PORT-F 4..7: SD: A[11:8] - SR or SR-LPC with SD on CS3: A[19:16] - SR NoAle or ALE1: ---  
' 11 : EBI Port3 adress output on PORT-E 4..7: SD: A[11:8] - SR or SR-LPC with SD on CS3: A[19:16] - SR NoAle or ALE1: ---  
  
' 00 : EBI CS-output on PORT-H 4..7  
' 01 : EBI CS-output on PORT-L 4..7  
' 10 : EBI CS-output on PORT-F 4..7  
' -> 11 : EBI CS-output on PORT-E 4..7  
  
  
```
Ebi_ctrl = &B01_00_11_10 'SRAM ALE12, 3Port  
```vb
' XX : 00: 4 Bit Data Bus  
' XX -> : 01: 8 Bit Data Bus  
' XX : 10: RESERVED  
' XX : 11: RESERVED  
  
' XX -> : 00: LPC-Mode: ALE1  
' XX : 01: LPC-Mode: RESERVED  
' XX : 10: LPC-Mode: ALE12  
' XX : 11: LPC-Mode: RESERVED  
  
' XX : 00: ALE1 - Adressbyte 0 and 1 multiplexed  
' XX : 01: ALE2 - Adressbyte 0 and 2 multiplexed  
' XX : 10: ALE12- Adressbyte 0,1 and 2 multiplexed  
' -> XX : 11: NOALE- No adress multiplexing  
  
' XX: 00: Externer Bus disabled  
' XX: 01: 3 Port Control-Bus # Data-Bus # A0:A7 und A8:A15 über ALE1 gemuxt  
' -> XX: 10: 4 Port  
' XX: 11: 2 Port  
  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'-------------------------------------------------------------------------------  
'ChipSelect0 für 512 KByte SRam  
  
' xxxxxxxx xxxx----  
' Bit: 23 bis 12 11 bis 0 nicht verwendet  
' | |  
```
Ebi_cs0_baseaddr = &B00010000_00000000 ' Start &H100000 = 1M  
```vb
' 00000000_00100000_00000000 = &H002000 = 8K  
' 00000000_00110000_00000000 = &H003000 = 12K  
' 00000000_01000000_00000000 = &H004000 = 16K  
' 00000000_10000000_00000000 = &H008000 = 32K  
' 00000001_00000000_00000000 = &H010000 = 64K  
' 00000010_00000000_00000000 = &H020000 = 128K  
' 00000100_00000000_00000000 = &H040000 = 256K  
' 00001000_00000000_00000000 = &H080000 = 512K  
' -> 00010000_00000000_00000000 = &H100000 = 1M  
' 00100000_00000000_00000000 = &H800000 = 2M  
' 01000000_00000000_00000000 = &H800000 = 4M  
' 10000000_00000000_00000000 = &H800000 = 8M  
  
```
Ebi_cs0_ctrla = &B0_01011_01 ' Size &H080000 = 512 KB  
```vb
' X : RESERVED  
' XXXXX : AdressBlockSize  
' 00000 : 256 Byte  
' 00001 : 512 Byte  
' 00010 : 1 KByte  
' 00011 : 2 KByte  
' 00100 : 4 KByte  
' 00101 : 8 KByte  
' 00110 : 16 KByte  
' 00111 : 32 KByte  
' 01000 : 64 KByte  
' 01001 : 128 KByte  
' 01010 : 256 KByte  
' -> 01011 : 512 KByte  
' 01100 : 1 MByte  
' 01101 : 2 MByte  
' 00110 : 4 MByte  
' 01111 : 8 MByte  
' 10000 : 16 MByte  
' XX : ChipSelectMode  
' 00 : disabled  
' -> 01 : Enabled for SRAM  
' 10 : Enabled for SRAM LPC (LowPinCount)  
' 11 : Enabled for SD-SRAM  
  
```
Ebi_cs0_ctrlb = &B00000_100 ' je nach Geschwindigkeit des SRam's  
```vb
' XXXXX : RESERVED  
' XXX : Waitstates  
' 000 : 0 Waitstates  
' 001 : 1 Waitstates  
' 010 : 2 Waitstates  
' 011 : 3 Waitstates  
' -> 100 : 4 Waitstates  
' 101 : 5 Waitstates  
' 110 : 6 Waitstates  
' 111 : 7 Waitstates  
  
'-------------------------------------------------------------------------------  
  
' Nun kann das externe SRam genauso wie das interne SRam angesprochen werden.  
' Vorteil: erheblich schneller im Zugriff, wie DRam !!!  
' So kann auch Hardware "memory-mapped" eingebunden werden  
' oder ein ISA-Bus realisiert werden.  
  
' Now you can use the external SRAM just like the internal SRAM.  
' This is much faster like DRAM  
' This way you can also map hardware and access registers as you would do for SRAM  
  
$xramstart = &H100000  
$xramsize = &H080000

```