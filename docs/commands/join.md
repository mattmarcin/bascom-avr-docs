# JOIN

Action

The JOIN function returns a string from a string array

Syntax

target = JOIN(source(start) ,elements [,glue] )

Remarks

target | The string that is assigned. You need to make sure that this string is dimensioned large enough to hold the content.  
---|---  
source | The source string array  
start | The starting position within the string array  
elements | The number of elements to process  
glue | This is an optional byte which you can use to glue the elements together. For example a space, or a dot  
  
The [SPLIT](split.md)() function can split up a string into elements. The JOIN() function does the exact opposite : it creates a string out of a string array.

See also

[SPLIT](split.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name : join.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates JOIN function  
'micro : M88  
'suited for demo : no  
'commercial addon needed : no  
'--------------------------------------------------------------------------------  
  
$regfile = "m88def.dat"  
  
$crystal = 8000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
  
Config Com1 = 115200 , Parity = None , Databits = 8 , Stopbits = 1  
  
  
Dim Ar(10) As String * 20  
Dim S1 , S2 As String * 80  
Dim Cnt As Byte  
  
```
S1 = "this.is.a.test"  
Cnt = Split(s1 , Ar(1) , ".")  
  
S2 = Join(ar(1) , 3)  
Print S2  
  
S2 = Join(ar(1) , 3 , ".")  
```vb
Print S2  
  
End  


```