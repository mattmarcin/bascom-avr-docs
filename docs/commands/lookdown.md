# LOOKDOWN

Action

Returns the index of a series of data.

Syntax

var = LOOKDOWN( value, label, entries)

Remarks

Var | The returned index value  
---|---  
Value | The value to search for  
Label | The label where the data starts  
entries | The number of entries that must be searched  
  
When you want to look in BYTE series the VALUE variable must be dimensioned as a BYTE. When you want to look in INTEGER or WORD series the VALUE variable must be dimensioned as an INTEGER.

The LookDown function is the counterpart of the LookUp function.

Lookdown will search the data for a value and will return the index when the value is found. It will return â1 when the data is not found.

Lookdown() supports byte, integer, dword and long data types.

See also

[LOOKUPSTR](lookupstr.md) , [LOOKUP](lookup.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : lookdown.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : LOOKDOWN

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

Dim Idx As Integer , Search As Byte , Entries As Byte

'we want to search for the value 3

```
Search = 3

'there are 5 entries in the table

Entries = 5

'lookup and return the index

Idx = Lookdown(search , Label , Entries)

Print Idx

Search = 1

Idx = Lookdown(search , Label , Entries)

Print Idx

Search = 100

Idx = Lookdown(search , Label , Entries)

```vb
Print Idx ' return -1 if not found

'looking for integer or word data requires that the search variable is

'of the type integer !

Dim Isearch As Integer

```
Isearch = 400

Idx = Lookdown(isearch , Label2 , Entries)

```vb
Print Idx ' return 3

End

```
Label:

Data 1 , 2 , 3 , 4 , 5

Label2:

Data 1000% , 200% , 400% , 300%