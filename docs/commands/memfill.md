# MEMFILL

Action

Fills a block of memory with a given value

Syntax

MEMFILL source, bytes, value

Remarks

source | The first address of the source variable that will be filled. This can be a normal numeric variable or an array like ar(1)  
---|---  
bytes | The number of bytes to fill.  The range is from 1-65535. ![notice](notice.jpg)There is not check for 0 bytes to copy. When using a variable make sure that it is not zero, since the effect will be that &HFFFF bytes will be filled.  
value | This is a byte or numeric constant with the ASCII value to use for the memory filling. To clear an array, use 0.  
  
MEMFILL intended use is to clear an array or to fill an array quickly.

To clear an array use a value of 0. 

See also

[MEMCOPY](memcopy.md)

ASM

CALLS _MEM_FILL in mcs.lib

Example

```vb
$regfile = "m1280def.dat"  
$crystal = 8000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
$baud = 19200  
  
Config Base = 0 'array start at 0  
  
Dim Ar(100) As Byte , X As Byte  
  
Print "MEMFILL test"  
  
'fill array/memory with ASCII A  
```
Memfill Ar(1) , 10 , 65 'skip the first entry so it remains 0  
  
```vb
Do  
Print X ; "->" ; Ar(x)  
```
Incr X  
```vb
Loop Until X = 10  
  
End  


```