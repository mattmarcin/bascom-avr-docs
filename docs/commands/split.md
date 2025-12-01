# SPLIT

Action

Split a string into a number of array elements.

Syntax

count = SPLIT (source, array(idx), search)

Remarks

count | The number of elements that SPLIT() returned. When the array is not big enough to fill the array, this will be the maximum size of the array. So make sure the array is big enough to hold the results.  
---|---  
source | The source string or string constant to search for.  
array(idx) | The index of the first element of the array that will be filled. Notice that arrays are global.  
search | The character to search for. This can be a string or string constant or a byte with the ASCII value.  
  
When you use the serial port to receive data, in some cases you need to process the data in parts.

For example when you need to split an IP number as "123.45.24.12" you could use INSTR() or you can use SPLIT().

You must DIM the array yourself. The content of the array will be overwritten.

It is also important to know that the individual elements of the array need to be big enough to store the string part.

For example when the array has 5 elements and each element may be 10 characters long, a string that is 11 bytes long will not fit. Another element will be used in that case to store the additional info.

The SPLIT function takes care not to overwrite other memory. So when you split "1.2.2.2.2.2.2.3.3.3" into an array of 3 elements, you will loose the data.

If empty data is encountered, an empty element will be created. Thus "1,2,3,,5" will create 5 elements. Element 4 will be empty.

See also

[INSTR](instr.md) , [CHARPOS](charpos.md) , [JOIN](join.md)

Example

```vb
'--------------------------------------------------------------

' mega48.bas

' mega48 sample file

' (c) 1995-2025, MCS Electronics

'--------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 8000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim S As String * 80

Dim Ar(5) As String * 10

Dim Bcount As Byte

'The split function can split a string or string constant into elements

'It returns the number of elements

'You need to take care that there are enough elements and that each element is big enough

'to hold the result

'When a result does not fit into 1 element it will be put into the next element

'The memory is protected against overwriting.

```
S = "this is a test"

Bcount = Split( "this is a test" , Ar(1) , " ")

```vb
'bcount will get the number of filled elements

'ar(1) is the starting address to use

'" " means that we check for a space

'When you use " aa" , the first element will contain a space

```
Bcount = Split( "thiscannotfit! into the element" , Ar(1) , " ")

```vb
Dim J As Byte

For J = 1 To Bcount

Print Ar(j)

Next

'this demonstrates that your memory is safe and will not be overwritten when there are too many string parts

```
Bcount = Split( "do not overflow the array please" , Ar(1) , " ")

```vb
For J = 1 To Bcount

Print Ar(j)

Next

End

```