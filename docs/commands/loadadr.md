# LOADADR

Action

Loads the address of a variable into a register pair.

Syntax

LOADADR var , reg

Remarks

var | A variable which address must be loaded into the register pair X, Y or Z.  
---|---  
reg | The register X, Y or Z.  
  
The LOADADR statement serves as an assembly helper routine.

Example

```vb
Dim S As String * 12

Dim A As Byte

$ASM

```
loadadr S , X ; load address into R26 and R27

ld _temp1, X ; load value of location R26/R27 into R24(_temp1)

$END ASM