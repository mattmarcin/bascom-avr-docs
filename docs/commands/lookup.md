# LOOKUP

Action

Returns a value from a data table based on the index.

Syntax

var = LOOKUP( value, label)

Remarks

Var | The returned value  
---|---  
Value | A value with the index of the table  
Label | The label where the data starts. You may also use a variable that holds the address of a label. This way you can pass data to a sub module. When processors are used with multiple 64KB pages, the page RAMPZ will be set as well.  
  
The maximum index value to use is 65535. The first entry will return a value of 0.

All items in the data table must be of the same data type. So you can not mix bytes and singles for example.

The data type of the return value must match the data type of the items in the table.

So this is wrong :

dim x as single

x=lookup(2,Dta)

dta:

data 1,2,3 'data does not match the used single in lookup

See also

[LOOKUPSTR](lookupstr.md) , [DATA](data_2.md) , [LOOKDOWN](lookdown.md) , [LOADWORDADR](loadwordadr.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B1 As Byte , I As Integer

```
B1 = Lookup(2 , Dta)

Print B1 ' Prints 3 (zero based)

I = Lookup(0 , Dta2) ' print 1000

```vb
Print I

End

```
Dta:

Data 1 , 2 , 3 , 4 , 5

Dta2:

Data 1000% , 2000%