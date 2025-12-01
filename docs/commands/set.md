# SET

Action

Set a bit to the value one.

Syntax

```vb
SET bit

SET var.x

SET var

```
Remarks

Bit | Bit or Boolean variable.  
---|---  
Var | A byte, integer, word or long variable.  
X | Bit of variable to set. Valid values are : 0-7 (byte, registers), 0-15 (Integer/Word) and (0-31) for a Long  
  
When the bit is not specified, bit 0 will be set. 

Also notice that the bit range is 0-255. Using a larger value on a variable will overwrite a different variable !

When you need an array of say 128 bits you can use code like this : dim ar(32) as long

You can index these variables like : SET ar(1).127 , in this case you write only to the memory of the intended variable.

See also

[RESET](reset.md) , [TOGGLE](toggle.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : boolean.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: AND, OR, XOR, NOT, BIT, SET, RESET and MOD

'suited for demo : yes

'commercial add on needed : no

'use in simulator : possible

'--------------------------------------------------------------------------------

'This very same program example can be used in the Help-files for  
' AND, OR, XOR, NOT, BIT, SET, RESET and MOD  
  
  
$baud = 19200  
$crystal = 16000000  
$regfile = "m32def.dat"  
  
$hwstack = 40  
$swstack = 20  
$framesize = 20  
  
Dim A As Byte , B1 As Byte , C As Byte  
Dim Aa As Bit , I As Integer  
  
```
A = 5 : B1 = 3 ' assign values  
C = A And B1 ' and a with b  
Print "A And B1 = " ; C ' print it: result = 1  
  
C = A Or B1  
Print "A Or B1 = " ; C ' print it: result = 7  
  
C = A Xor B1  
Print "A Xor B1 = " ; C ' print it: result = 6  
  
A = 1  
C = Not A  
Print "c = Not A " ; C ' print it: result = 254  
C = C Mod 10  
```vb
Print "C Mod 10 = " ; C ' print it: result = 4  
  
  
If Portb.1 = 1 Then  
Print "Bit set"  
Else  
Print "Bit not set"  
End If 'result = Bit not set  
  
```
Aa = 1 'use this or ..  
```vb
Set Aa 'use the set statement  
If Aa = 1 Then  
Print "Bit set (aa=1)"  
Else  
Print "Bit not set(aa=0)"  
End If 'result = Bit set (aa=1)  
  
```
Aa = 0 'now try 0  
```vb
Reset Aa 'or use reset  
If Aa = 1 Then  
Print "Bit set (aa=1)"  
Else  
Print "Bit not set(aa=0)"  
End If 'result = Bit not set(aa=0)  
  
```
C = 8 'assign variable to &B0000_1000  
```vb
Set C 'use the set statement without specifying the bit  
Print C 'print it: result = 9 ; bit0 has been set  
  
```
B1 = 255 'assign variable  
```vb
Reset B1.0 'reset bit 0 of a byte variable  
Print B1 'print it: result = 254 = &B11111110  
  
```
B1 = 8 'assign variable to &B00001000  
```vb
Set B1.0 'set it  
Print B1 'print it: result = 9 = &B00001001  
End

```