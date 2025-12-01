# SWAP

Action

Exchange two variables of the same type.

Exchange a nibble or 2 bytes

Syntax

SWAP var1, var2

SWAP var3

Remarks

var1 | A variable of type bit, byte, integer, word, long or string.  
---|---  
var2 | A variable of the same type as var1.  
var3 | A byte, integer,word,long or dword  
  
After the swap, var1 will hold the value of var2 and var2 will hold the value of var1.

When using swap with a single variable it need to be a byte, integer/word or long/dword variable.

In version 2084 you can also swap a dword or long.

When using swap on a byte, the nibbles will be swapped. 

Example :

byte=&B1100_0001 : swap byte : byte will become : &B0001_1100

When using swap on a single integer or word, the 2 bytes will be swapped so the LSB becomes the MSB and the MSB becomes the LSB.

When using swap on a single dword or long, the 4 bytes will be swapped the following way :

LSB NSB1 NSB2 MSB will become : MSB NSB2 NSB1 LSB

Example

```vb
'-----------------------------------------------------------------------------------------

'name : swap.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: SWAP

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim A As Byte , B1 As Byte

Dim Bbit1 As Bit , Bbit2 As Bit

Dim S1 As String * 10 , S2 As String * 10

```
S1 = "AAA" : S2 = "BBB"

Swap S1 , S2

A = 5 : B1 = 10 'assign some vars

Print A ; " " ; B1 'print them

Swap A , B1 'swap them

```vb
Print A ; " " ; B1 'print is again

Set Bbit1

```
Swap Bbit1 , Bbit2

```vb
Print Bbit1 ; Bbit2

End

```