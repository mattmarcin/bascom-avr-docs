# MEMCOPY

Action

Copies a block of memory

Syntax

bts = MEMCOPY(source, target , bytes [, option])

Remarks

bts | The total number of bytes copied. This must be an integer or word variable.  
---|---  
source | The first address of the source variable that will be copied.  
target | The first address of the target variable that will be copied to.  
bytes | The number of bytes to copy from "source" to "target" The range is from 1-65535. ![notice](notice.jpg)There is not check for 0 bytes to copy. When using a variable make sure that it is not zero, since the effect will be that &HFFFF bytes will be copied.  
option | An optional numeric constant with one of the following values : 1 - only the source address will be increased after each copied byte 2 - only the target address will be increased after each copied byte 3 - both the source and target address will be increased after each copied byte  
  
By default, option 3 is used as this will copy a block of memory from one memory location to another location. But it also possible to fill an entire array of memory block with the value of 1 memory location. For example to clear a whole block or preset it with a value.

And with option 2, you can for example get a number of samples from a register like PINB and store it into an array.

MEMCOPY checks the size of the target variable and it will not overwrite data if the number of bytes is greater than the size of the target data. For example : 

Dim tar(4) as byte, sar(8) as byte

MEMCOPY sar(1), tar(1),8 

Even while 8 bytes are specified, the data size for tar() is 4 and thus only 4 bytes will be copied.

When you use MEMCOPY Inside a sub routine/function with passed parameters, there is no way to check the target size. 

In this case, there is no check on the target size and the number of specified bytes will be moved, no matter the target data size.

This is potential unsafe when you specify too many bytes since other memory could be overwritten.

MEMCOPY could be used to clear an array quickly.

See also

[MEMFILL](memfill.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------

'name : MEMCOPY.BAS

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show memory copy function

'suited for demo : yes

'commercial addon needed : no

'use in simulator : possible

'----------------------------------------------------------------------

$regfile = "m88def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 16 ' default use 10 for the SW stack

$framesize = 40

Dim Ars(10) As Byte 'source bytes

Dim Art(10) As Byte 'target bytes

Dim J As Byte 'index

For J = 1 To 10 'fill array

```
Ars(j) = J

Next

J = Memcopy(ars(1) , Art(1) , 4) 'copy 4 bytes

```vb
Print J ; " bytes copied"

For J = 1 To 10

Print Art(j)

Next

```
J = Memcopy(ars(1) , Art(1) , 10 , 2) 'assign them all with element 1

```vb
Print J ; " bytes copied"

For J = 1 To 10

Print Art(j)

Next

Dim W As Word , L As Long

```
W = 65511

J = Memcopy(w , L , 2) 'copy 2 bytes from word to long

End