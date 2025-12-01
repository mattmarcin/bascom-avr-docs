# SIZEOF

Action

This function returns the size of a variable.

Syntax

size = Sizeof(var)

Remarks

The SizeOf function returns the size in memory of a variable. It does not matter where the variable is stored : sram, xram or eeprom.

The functions accepts normal variables and indexed variables. When using an index, note that the total size is returned of the array. No matter which index you specify.

Since variables do not store run time information this function only works at compile time. So you can not use this function in a dynamic way

Variables use the following amount of memory.

Variable | Size in Bytes  
---|---  
Bit | 1  
Byte | 1  
Integer | 2  
Word | 2  
Dword | 4  
Long | 4  
Single | 4  
Double | 8  
String  | length + 1  
String * 1 | 2  
String * 10 | 11  
  
A bit is 1/8 of a byte. So there will fit 8 bits into a byte. The function will return the minimum length.

A string always uses an additional byte since strings are null terminated. Which means a null marks the end of a string. 

See also

[VARPTR](varptr.md)

Example

```vb
'--------------------------------------------------------------------------------------  
' sizeof.bas  
' (c)1995-2025, MCS Electronics  
' demo of sizeof() function  
'  
'--------------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$hwstack = 32  
$swstack = 32  
$FrameSize=24  
  
'set the base for arrays to 0  
Config Base = 0  
  
Dim S As String * 10  
Dim B As Byte  
Dim I As Integer  
Dim L As Long  
Dim Sng As Single  
Dim D As Double  
  
Dim Bar(3) As Byte  
Dim Sar(4) As String * 5  
  
```
Const X3 = Sizeof(sar(0))  
  
```vb
Print X3  
Print Sizeof(s)  
Print Sizeof(b)  
Print Sizeof(i)  
Print Sizeof(l)  
Print Sizeof(sng)  
Print Sizeof(d)  
Print Sizeof(bar(_base))  
Print Sizeof(sar(_base))  
```
B = Sizeof(sar(_base))  
  
End