# COMPARE

Action

This function performs a byte compare on two variables.

Syntax

result = COMPARE( var1, var2, bytes)

Remarks

result | A word variable that is assigned with the result of the function. When the 2 variables are equal, the value will be 0. When the 2 variables differ, the index is returned of the position that differs.   
---|---  
var1 , var2 | Any kind of variable like a long or string. Constants are not supported.  
Bytes | The number of bytes to test. The maximum value must fit into a word. (65535).  
  
See also

NONE

Example

```vb
'-------------------------------------------------------------------------  
'name : compare.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates byte COMPARE function, written by MWS  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'-------------------------------------------------------------------------  
' purpose: byte-wise compare  
' arg Val1: first value to compare, type = don't care  
' arg Val2: second value to compare, type = don't care  
' arg BtComp: count of bytes to compare, can be a constant or a variable  
' range is 1 to 65535 bytes  
' result: zero if all bytes within range of BtComp are matching  
' 1 up to BtComp if there's a miss,  
' zero is used for signaling a comlete match, so Config Base has no effect  
' 1 is always the first byte of the variable, whatever type of variable it is  
'-------------------------------------------------------------------------  
  
$regfile = "m328pdef.dat"  
$crystal = 16000000  
$hwstack = 40  
$swstack = 32  
$framesize = 32  
  
```
Const Testver = 2 ' edit for different tests 0,1 or 2  
  
```vb
Dim Mmpos As Word ' dimension word var to hold the result, i.e. mismatch position  
Dim btt As Word ' bytes to test  
  

#if Testver = 0  
Dim Val_a(8) As Byte ' byte array vs. byte array  
Dim Val_b(8) As Byte ' arrays are initialyzed 0  
```
Btt = 8  
Val_a(4) = 1 ' test it  

```vb
#elseif Testver = 1  
Dim Val_a As Double ' Double vs. byte array  
Dim Val_b(8) As Byte  
```
Btt = 8  
Val_b(2) = 1 ' test it  

```vb
#elseif Testver = 2 ' compare strings  
Dim Val_a As String * 16  
Dim Val_b As String * 16  
```
Btt = 12  
Val_a = "Hello Bascom"  
Val_b = "Hello Bascon" ' find the mismatch  

#endif  
  
Mmpos = Compare(val_a , Val_b , Btt)  
  
```vb
If Mmpos > 0 Then  
Print "We have a miss at pos: " ; Mmpos  
Else  
Print "Match!"  
End If  
End

```