# $DEFAULT

Action

Set the default for data types dimensioning to the specified type.

Syntax

$DEFAULT var

Remarks

Var | SRAM, XRAM, ERAM  
---|---  
  
Each variable that is dimensioned will be stored into SRAM, the internal memory of the chip. You can override it by specifying the data type.

Dim B As XRAM Byte , will store the data into external memory.

When you want all your variables to be stored in XRAM for example, you can use the statement : $DEFAULT XRAM

Each Dim statement will place the variable in XRAM in that case.

To switch back to the default behavior, use $END $DEFAULT

See also

NONE

ASM

NONE

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

$default Xram

Dim A As Byte , B As Byte , C As Byte

'a,b and c will be stored into XRAM

$default Sram

Dim D As Byte

'D will be stored in internal memory, SRAM

```