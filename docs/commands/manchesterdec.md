# MANCHESTERDEC

Action

This functions decodes a Manchester encoded word into a byte.

Syntax

target = ManChesterDec(source)

Remarks

target | The byte variables that is assigned with the decoded Manchester value.  
---|---  
source | A Word variable containing the Manchester encoded value.  
  
Manchester encoding (also known as phase encoding) is a line code in which the encoding of each data bit is either low then high, or high then low, for equal time. It is a self-clocking signal with no DC component. Because each input bit is represented as 01 or 10, the resulting data is twice the size of the input data.

Manchester encoding is used with RF and IR data transmission.

When there is an error in the decoding, register R25 will be set to 255.

See also

[MANCHESTERENC](manchesterenc.md)

Example

```vb
'-----------------------PROJECT------------------------------------------------  
'name ManchesterCoding.BAS  
'copyright © 2018, MCS  
'purpose DEMO MANCHESTER ENCODING and DECODING  
'micro M1280  
'----------------------------------------------------------------  
$regfile = "m1280def.dat" ' specify the uC used  
$crystal = 32000000 ' Oscillator frequency  
$hwstack = 40 ' hardware stack  
$swstack = 40 ' software stack  
$framesize = 40 ' frame space  
  
Dim B As Byte , J As Byte , W As Word  
For J = 0 To 255  
```
W = Manchesterenc(j) ' encode into manchester code whith results into a WORD  
B = Manchesterdec(w) ' decode it back  
```vb
If R25 <> 0 Then ' when an error occurs, register r25 is 255  
Print "ERROR"  
End If  
Print J ; " " ; Hex(w) ; " " ; B  
Next

```