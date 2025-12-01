# DECLARE SUB

Action

Declares a subroutine.

Syntax

DECLARE SUB TEST[( [BYREF|BYVAL|BYLABEL|BYREG|BYSTACK] var as type)]

Remarks

test | Name of the procedure.  
---|---  
Var | Name of the parameter(s).  
Type | Type of the parameter(s) :  Byte, Word, Dword, Integer, Long, Single, Double or String.  When passing a string it is recommended to also pass the maximum length of the string : SomeString As String * 30 would indicate that the string will have a maximum length of 30 characters. Please notice that you need to specify the string length in both the DECLARE and the actual implementation. Unless you use CONFIG SUBMODE=NEW in which case you only write the implementation.  
  
ARRAYS

Arrays can be passed by reference only. You need to add empty parenthesis() after the variable to indicate that you pass an array. 

Inside the sub/function you also need to use () when accessing the variable.

Let's have a look at an example.

```vb
Declare Sub TestArray(ar() as byte, b as byte)

Dim a(10) as byte , q as byte

```
TestArray a() , q

As you can see, we add () after the variable to indicate that it is an array we pass.

When we call the sub program, we pass the first address or the base address of the array. That is a(1) in this case.

Inside the sub module, we also refer to the variable using ().

```vb
Sub TestArray(ar() as byte, b as byte)

print ar(1)

print ar(b)

End Sub

```
In older BASCOM versions, it was not required to use (). You only needed to pass the base address. But that is potential unsafe : if you reference a variable as an array while it is actually a single variable, then you can write to the wrong address. When using (), the compiler knows when an array is expected and can inform you about a possible error. 

If you have old code you can use CONFIG ERROR=IGNORE,380=IGNORE to ignore errors as a result of the updated syntax.

Parameter Passing

When BYREF | BYVAL | BYREG | BYLABEL or BYSTACK is not provided, the parameter will be passed by reference (BYREF).

BYREF

Use BYREF to pass a variable by reference with its address. When using the referenced address, you work on the original variable. So a change of the variable inside the sub routine, will change the passed variable outside the routine as well.

BYVAL

Use BYVAL to pass a copy of the variable. Passing a copy of the variable allows to alter the copy in the sub routine while leaving the original variable unaltered. BYVAL will not change the original passed variable but it requires more code since a copy of the parameter must be created.

BYREG

Use BYREG to pass a copy of the variable using a register. The value will be passed to the register(s) you specify. When multiple bytes need to be passed, multiple registers will be used. Registers are named from R0-R31. When you pass a WORD to register R16, you will also use R17 since a word requires 2 bytes.

You can not pass strings. Only numeric variables and constants.

Using BYREG requires some knowledge of the routines you call. The current implementation does not protect already loaded registers. This means that when you pass multiple registers you could destroy some already loaded registers just because a parameter will destroy the register.

Example : declare Sub MySub(byreg R16 as Word, byreg R18 as long, byreg R22 as dword)

mysub 1000, var(J+100), var(j)

In this example, R16 and R17 are loaded, after this the array index of variable var() need to be calculated which uses the ML16 routine which uses R16-R21

Numeric constants and expression do not alter registers but functions might. A future version will track and protect registers.

Why would you want to use BYREG ? Using BYREG is equivalent to using ASM. It is intended to be used with ASM code inside subs. The FT800 include files use BYREG and BYSTACK. 

Example from FT800:

Sub Stencilfunc(byreg r18 As Byte , Byreg r17 As Byte , Byreg R16 As Byte)

Cmd32 _stencilfunc(r18 , R17 , r16)

End Sub 

BYSTACK

Use BYSTACK to pass a copy of the variable by the soft stack (Y-pointer). BYSTACK will not create a copy of the variable but instead will pass the data directly to the soft stack. 

The first parameter is passed first , LSB first. You will find BYSTACK used in the FT800 include files. BYSTACK has the advantage compared to BYREG that no registers are altered. But it has the disadvantage that it requires an optional step to pass the data to the stack. 

The SUB/FUNCTION need to clean up the stack. Typically you would use LD reg, y+ to pop data from the stack. 

The FT800 uses [CMDFTSTACK](cmdftstack.md) to pop data from the stack and send it to the FT800. 

BYLABEL

Use BYLABEL to pass the address of a label. BYLABEL will pass the word address. It will not work for processors with multiple 64 KB pages.

Using BYLABEL on the EEPROM is possible but the EEPROM image must proceed the call with the label name.

See also [READEEPROM](readeeprom.md), [LOADLABEL](loadlabel.md) and [Memory usage ](memory_usage.md)

```vb
If you pass a string you may specify the length of the string. This length will be the maximum length the string may grow. This is important when you pass a string BYVAL. 

For example, when you pass a string like "ABC" to a subroutine or function using BYVAL, the compiler will create a copy with a length of 3. This is sufficient to pass it to the sub routine.

```
But if the sub routine adds data to the string, it will not fit since the string is too short. In such a case you can specify the length. s as string * 10, will create a string with a size of 10.

See the [CALL](call.md) statement for more details.

![notice](notice.jpg) You must declare each function before writing the function or calling the function. And the declaration must match the function. Optional you can use [CONFIG SUBMODE](config_submode.md)=NEW so DECLARE is not required.

Bits are global and can not be passed to functions or subs.

![notice](notice.jpg) See [DECLARE FUNCTION](debug.md) paragraph named IMPORTANT

See also

[CALL](call.md), [SUB](sub.md) , [FUNCTION](declare_function.md) , [CONFIG SUBMODE](config_submode.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : declare.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrate using declare

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' Note that the usage of SUBS works different in BASCOM-8051

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

' First the SUB programs must be declared

'Try a SUB without parameters

Declare Sub Test2()

'SUB with variable that can not be changed(A) and

'a variable that can be changed(B1), by the sub program

'When BYVAL is specified, the value is passed to the subprogram

'When BYREF is specified or nothing is specified, the address is passed to

'the subprogram

Declare Sub Test(byval A As Byte , B1 As Byte)

Declare Sub Testarray(byval A As Byte , B1 As Byte)

'All variable types that can be passed

'Notice that BIT variables can not be passed.

'BIT variables are GLOBAL to the application

Declare Sub Testvar(b As Byte , I As Integer , W As Word , L As Long , S As String)

'passing string arrays needs a different syntax because the length of the strings must be passed by the compiler

'the empty () indicated that an array will be passed

Declare Sub Teststr(b As Byte , Dl() As String)

Dim Bb As Byte , I As Integer , W As Word , L As Long , S As String * 10 'dim used variables

Dim Ar(10) As Byte

Dim Sar(10) As String * 8 'strng array

For Bb = 1 To 10

```
Sar(bb) = Str(bb) 'fill the array

Next

Bb = 1

'now call the sub and notice that we always must pass the first address with index 1

Call Teststr(bb , Sar(1))

Call Test2 'call sub

Test2 'or use without CALL

'Note that when calling a sub without the statement CALL, the enclosing parentheses must be left out

Bb = 1

Call Test(1 , Bb) 'call sub with parameters

```vb
Print Bb 'print value that is changed

'now test all the variable types

```
Call Testvar(bb , I , W , L , S )

```vb
Print Bb ; I ; W ; L ; S

'now pass an array

'note that it must be passed by reference

```
Testarray 2 , Ar(1)

```vb
Print "ar(1) = " ; Ar(1)

Print "ar(3) = " ; Ar(3)

$notypecheck ' turn off type checking

```
Testvar Bb , I , I , I , S

```vb
'you can turn off type checking when you want to pass a block of memory

$typecheck 'turn it back on

End

'End your code with the subprograms

'Note that the same variables and names must be used as the declared ones

Sub Test(byval A As Byte , B1 As Byte) 'start sub

Print A ; " " ; B1 'print passed variables

```
B1 = 3 'change value

```vb
'You can change A, but since a copy is passed to the SUB,

'the change will not reflect to the calling variable

End Sub

Sub Test2 'sub without parameters

Print "No parameters"

End Sub

Sub Testvar(b As Byte , I As Integer , W As Word , L As Long , S As String)

```
Local X As Byte

X = 5 'assign local

B = X

I = -1

W = 40000

L = 20000

S = "test"

```vb
End Sub

Sub Testarray(byval A As Byte , B1 As Byte) 'start sub

Print A ; " " ; B1 'print passed variables

```
B1 = 3 'change value of element with index 1

B1(1) = 3 'specify the index which does the same as the line above

B1(3) = 3 'modify other element of array

```vb
'You can change A, but since a copy is passed to the SUB,

'the change will not reflect to the calling variable

End Sub

'notice the empty() to indicate that a string array is passed

Sub Teststr(b As Byte , Dl() As String)

```
Dl(b) = Dl(b) + "add"

End Sub

Example BYLABEL

```vb
$regfile = "m88def.dat"  
$hwstack = 40  
$swstack = 80  
$framesize = 80  
  
Dim B As Byte , W As Word  
  
Declare Sub Somesub(bylabel Mylabel As Word)  
```
Somesub Alabel  
```vb
End  
  
  
Sub Somesub(bylabel Mylabel As Word)  
```
W = Mylabel ' this points to the BYTE address of the data  
!lds _dptrl,{W } ' point to  
!LDS _dptrh,{W+1}  
Read B : Print B  
End Sub  
  
Alabel:  
Data 1 , 2 , 3