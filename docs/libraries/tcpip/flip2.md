# FLIP

Action

Flips the bits in a byte.

Syntax

var = FLIP( s )

Remarks

Var | The variable that is assigned with the flipped byte S.  
---|---  
S | The source variable to flip.  
  
The FLIP function can be useful in cases where you have reversed the data lines d0-d7.

It will reverse or mirror the bits

See also

NONE

Example

```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack=32  
$swstack = 16  
$framesize=24  
  
Dim B As Byte , V As Byte  
  
For B = 1 To 20  
```
V = Flip(b)  
```vb
Print B ; " " ; Bin(b) ; " " ; Bin(v)  
Next  
  
End

```
OUTPUT

1 00000001 10000000

2 00000010 01000000

3 00000011 11000000

4 00000100 00100000

5 00000101 10100000

6 00000110 01100000

7 00000111 11100000

8 00001000 00010000

9 00001001 10010000

10 00001010 01010000

11 00001011 11010000

12 00001100 00110000

13 00001101 10110000

14 00001110 01110000

15 00001111 11110000

16 00010000 00001000

17 00010001 10001000

18 00010010 01001000

19 00010011 11001000

20 00010100 00101000