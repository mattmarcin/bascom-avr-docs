# Adding XRAM to XMEGA using EBI

This information has been provided by Electronic Design Bitzer.

Some XMEGA processors have an EBI. The following circuit shows how to set up the EBI for 8 bit bus mode where the SRAM can be selected with a jumper.

128 KB SM621008VLLP70T : SRAM LLPow 3,3V 128Kx8 70ns TSOP32(I)

512 KB SM624008VLLP70M : SRAM LLPow 3,3V 512Kx8 70ns SOP32

The BASCOM setup code : 

```vb
' All EBI-Ports must be set to OUTPUT

' All Ports, ACTIVE-LOW , must be set to 1 !!!

' All Ports, ACTIVE-HIGH, must be set to 0 !!!

```
Porth_dirset = &B1111_1111 : Porth = &B1111_0011 'WR, RD, ALE1, ALE2, CS0-3 = output : ALE1 & 2 auf 0 !!!

Portj_dirset = &B1111_1111 : Portj = &B1111_1111

Portk_dirset = &B1111_1111 : Portk = &B1111_1111

Config Xram = 3port , Ale = Ale12 , Sdbus = 8 , Modesel0 = Sram , Adrsize0 = 256b , Waitstate0 = 4 , Baseadr0 = &H10000 , _

Modesel1 = Sram , Adrsize1 = 128k , Waitstate1 = 1 , Baseadr1 = &H20000

See also : [CONFIG XRAM](configxram.md)

![xram-ebi](xram-ebi.zoom58.png)