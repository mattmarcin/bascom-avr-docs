# TYPE

Action

Defines a memory container using normal data types.

Syntax

TYPE SomeName

mem1 As DataType

memn As DataType

END TYPE

Remarks

Type describes a container of data types. It does not use any memory. Memory allocation is done using DIM. 

You start a new Type by using the TYPE statement. It must be followed by the type name.

On new lines you enter the member names followed by their data type. This is just like the DIM statement except that you only provide the data type.

You can also use an earlier defined data type. 

It is also possible to create an array by specifying an index. This index is one dimensional.

You end the definition on a new line using END TYPE.

Some examples : 

Type Rectest  
Naam As String * 9 '0-9, 10 bytes  
B As Byte '1 byte  
C As Integer '2 bytes  
End Type 'total size 13  
  
Type Mem  
Ar(16) As Byte '16 bytes  
X As Rectest '13 bytes  
End Type '29 total size  
  
Type Trec3  
J As Byte ' 1 byte  
End Type 'total 1 byte  
  
Type Trec2  
N As Integer '2 bytes  
W As Word '2 bytes  
R As Trec3 '1 bytes  
End Type 'total 5 bytes  
  
Type Trec1  
B As Byte '1 byte  
Q(10) As Byte '10 bytes  
Z(5) As Trec2 '5x2=25 bytes  
End Type 'total 36 bytes  
  
Type Tstr  
Naam As String * 16 '17 bytes  
B As Byte '1 bytes  
I As Integer '2 bytes  
W As Word '2 bytes  
Dw As Dword '4 bytes  
L As Long '4 bytes  
S As Single '4 bytes  
D As Double '8 bytes  
Ar(5) As String * 12 '5x13=65  
```vb
End Type 'total 107 bytes  
  
Dim Myrec(5) As Trec1 'using DIM you refer to the type name  
Dim Rec1 , Rec2 As Rectest  
Dim Recar(4) As Mem  
Dim Srec As Tstr  


  
```
When you refer to a typed variable you either use the name to refer to the whole record or when you want to access a member, you use a DOT followed by the member name.  
When a type contains nested types you use multiple DOTs and member names till you reach the desired member.  
The same BASCOM rules apply for typed variables as normal variables.  


There are some limitations since the type was not part of the compiler when designed.

Some of the limitations might be changed in the future.  
\- variable types can be only used in RAM and XRAM. It will not work on ERAM  
\- you can not perform bit operation on a type member : rec.b.1 = 1 will not work  
\- boolean/bit types can not be used as members.  
\- just like arrays, types are global and are passed by reference only  


INDIRECT Types

Besides the normal types there is also the indirect type. It works exact the same but when you DIM the variable that uses the type you use an additional specifier named INDIRECT

```vb
Dim Somerec As Trec1 Indirect

While a normal variable that uses a type uses memory determined at compilation the Indirect variable type has an internal address which need to be set by the user.

```
An example :

Dim Idrec As Tstr Indirect 'claims no memory

Const Cx = Sizeof(idrec) 'determine the size of the variable

Dim Al(cx) As Byte 'create an array in memory with the size of the type

Idrec_adr = Varptr(al(1)) 'set the address to the memory of al array

The address is the name of the variable with a suffix of _adr

So what is this good for you wonder?

When the memory would be dynamically allocated and released by a memory manager there would be no fixed memory address. So this variant is intended to be used with a memory manager.

A free memory manager exists. See the help description of Options, Compiler, Output, Extended Constants for more details.

See also

[DIM](dim.md) , [SIZEOF](sizeof.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name :  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose :  
'micro : avr64da64  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
  
$regfile = "AVRX64da64.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 64  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
'Config Base = 0  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1 , Tx_rx_xc_xd_pin = Alt1_pa4_pa5_pa6_pa7  
  
'a TYPE Defines a data type containing one or more elements  
'each element is defined just as you do with DIM  
'a TYPE does not occupy any space, it defines how much space is used when it is DIMensioned  
'below are some examples of types.  
  
  
```
Type Rectest  
Naam As String * 9 '0-9, 10 bytes  
B As Byte '1 byte  
C As Integer '2 bytes  
End Type 'total size 13  
  
Type Mem  
Ar(16) As Byte '16 bytes  
X As Rectest '13 bytes  
End Type '29 total size  
  
Type Trec3  
J As Byte ' 1 byte  
End Type 'total 1 byte  
  
Type Trec2  
N As Integer '2 bytes  
W As Word '2 bytes  
R As Trec3 '1 bytes  
End Type 'total 5 bytes  
  
Type Trec1  
B As Byte '1 byte  
Q(10) As Byte '10 bytes  
Z(5) As Trec2 '5x2=25 bytes  
End Type 'total 36 bytes  
  
Type Tstr  
Naam As String * 16 '17 bytes  
B As Byte '1 bytes  
I As Integer '2 bytes  
W As Word '2 bytes  
Dw As Dword '4 bytes  
L As Long '4 bytes  
S As Single '4 bytes  
D As Double '8 bytes  
Ar(5) As String * 12 '5x1365  
```vb
End Type '107 bytes  
  
'declare som subs for testing  
Declare Sub Sbt(rec As Rectest)  
Declare Sub Sbtest(byval B1 As Byte , B2 As Byte , Rec As Rectest)  
  
'dim some vars for test  
Dim Ss As String * 10  
Dim Ar(2) As Byte  
Dim B As Byte  
Dim Myrec(5) As Trec1 'using DIM you refer to the type name  
Dim Bdum As Byte , Idx As Byte , Qdx As Byte , Zdx As Byte  
Dim B1 As Byte  
Dim Rec1 , Rec2 As Rectest  
Dim Recar(4) As Mem  
Dim B2 As Byte  
Dim Srec As Tstr  
  
'when you refer to a typed variable you either use the name to refer to the whole record  
'or when you want to access a member, you use a DOT followed by the member name  
'when a type contains nested types you use multiple DOTs and membernames till you reach the member of interest.  
'The same BASCOM rules apply for typed variables as normal variables.  
  
'There are some limitations. Some of them might be changed in the near future  
'- variable types can be only used in RAM and XRAM. It will not work on ERAM  
'- you can not do bit operation in a type member : rec.b.1 = 1 will not work  
'- boolean/bit types can not be used as members.  
'- types are global and are passed by reference only  
  
```
B = 2 'assign a normal byte  
  
Rec1.b = 2 'assign to the byte member  
  
Srec.naam = "abc" 'assign a string  
Srec.ar(1) = "one" 'ar is an index so it must be addressed as index  
Srec.ar(b) = "two"  
Srec.b = B 'byte  
Srec.i = -1234 'integer  
Srec.w = 50000 'word  
Srec.dw = 12345678 'double word  
Srec.s = 12.34 'single  
Srec.d = 500.1234 'double  
Bdum = 1 'some other byte  
Swap Srec.ar(1) , Srec.ar(b) 'swap to record members  
  
```vb
Print Srec.naam 'print content of member  
Print Srec.b 'print byte value  
  
```
Sbt Rec1 'call a subroutine  
Sbtest Srec.b , Srec.b , Rec1 'call another sub  
  
Rec1.naam = "abc" 'assign string member  
Myrec(3).z(2).w = &HEEBB 'nested records assignment  
Myrec(3).z(b).w = Myrec(3).z(2).w + 100 'math operation on a record  
  
Myrec(1).z(2).r.j = 1  
Myrec(2).z(b).r.j = B  
Myrec(bdum).z(2).r.j = 3  
Myrec(bdum).z(2).r.j = Myrec(2).z(2).r.j  
Myrec(1) = Myrec(2) 'copy entire record  
Myrec(bdum) = Myrec(2)  
```vb
Print Myrec(4).z(2).r.j  
  
For Idx = 1 To 5  
```
Myrec(idx).b = Idx  
For Qdx = 1 To 10  
Myrec(idx).q(qdx) = Qdx  
```vb
Next  
Next  
  
```
Rec1 = Rec2 'copy whole record  
  
```vb
End  
  
'when you create a sub/function that pass a typed variable you need to define the type name  
Sub Sbtest(byval B1 As Byte , B2 As Byte , Rec As Rectest)  
```
B1 = B1 + 1 'we add one which does not matter since we pass a local copy  
Print B1 'print the value  
B2 = B2 + 1 'this is passed by reference , add 1  
Print B2 'print it, the calling value is changed as well  
Rec.b = &HB 'print the record member value  
Rec.c = &HC  
```vb
End Sub  
  
'another simple test  
Sub Sbt(rec As Rectest)  
```
Rec.b = &HB  
Rec.c = &HC  
End Sub