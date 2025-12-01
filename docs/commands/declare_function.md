# DECLARE FUNCTION

Action

Declares a user function.

Syntax

DECLARE FUNCTION TEST[( [BYREF/BYVAL] prm as type)] As type

Remarks

test | Name of the function.  
---|---  
prm | Name of the optional parameters.  
Type | Type of the parameter(s) and of the result. Byte,Word, Dword, Integer, Long, Single, Double or String. Bits are not supported. When passing a string it is recommended to also pass the maximum length of the string : SomeString As String * 30 would indicate that the string will have a maximum length of 30 characters. Please notice that you need to specify the string length in both the DECLARE and the actual implementation. Unless you use CONFIG SUBMODE=NEW in which case you only write the implementation.  
  
When BYREF or BYVAL is not specified, the parameter will be passed by reference.

Use BYREF to pass a variable by reference with its address. This means that you work on the string you pass. Any change you make in the sub/function you will make on the original string.

Use BYVAL to pass a copy of the variable. This means that a copy is created and the address of this copy is passed to the sub/function. If you change the string, the original sting remains the same.

Use BYLABEL to pass the address of a label. 

See the [CALL](call.md) and [DECLARE SUB](declare_sub.md) statements for more details. 

See also [Memory usage](memory_usage.md)

![notice](notice.jpg)SUB and FUNCTION are the same with 1 difference : a function returns a result which can be assigned to a variable. 

ARRAYS

Arrays can be passed by reference only. You need to add empty parenthesis() after the variable to indicate that you pass an array. 

Inside the sub/function you also need to use () when accessing the variable.

Let's have a look at an example which calls a SUB. Functions and Subs are similar with the difference that a functions returns a result.

```vb
Declare Sub TestArray(ar() as byte, b as byte)

Dim a(10) as byte , q as byte

```
TestArray a(1) , q

As you can see, we add () after the variable to indicate that it is an array we pass.

When we call the sub program, we pass the first address or the base address of the array. That is a(1) in this case. See also [CONFIG BASE.](config_base.md)

Inside the sub module, we also refer to the variable using ().

```vb
Sub TestArray(ar() as byte, b as byte)

print ar(1)

print ar(b)

End Sub

```
In older BASCOM versions, it was not required to use (). You only needed to pass the base address. But that is potential unsafe : if you reference a variable as an array while it is actually a single variable, then you can write to the wrong address. When using (), the compiler knows when an array is expected and can inform you about a possible error. 

If you have old code you can use CONFIG ERROR=IGNORE,380=IGNORE to ignore errors as a result of the updated syntax.

![notice](notice.jpg) You must declare each function before writing the function or calling the function. And the declaration must match the function.

Bits are global and can not be passed to functions or subs.

When you want to pass a string, you pass it with it's data type : string. So the size is not important. For example :

Declare function Test(s as string, byval z as string) as byte

You may and should specify the optional maximum length. In fact it is highly recommended that you do so.

![notice](notice.jpg)When you set the function result, you need to take care that no other code is executed after this. 

So a good way to set the result would be this :

Function Myfunc(b as byte) as Byte

local bDummy as byte

'some code here

Myfunc=3 ' assign result

```vb
' no other code is executed

End Function 

```
Also good would be:

Function Myfunc(b as byte) as Byte

local bDummy as byte

'some code here

Myfunc=1 ' assign default result

Print "this is a test " ; b

Myfunc=4 ' now again the result is the last code

```vb
' no other code is executed

End Function 

If you execute other code after you assigned the function result, registers will be trashed. This is no problem if you assigned the function result to a variable. But when you use a function without assigning it to a variable, some temporarily registers are used which might be trashed.

```
Thus this special attention is only needed when you use the function like :

If Myfunc()=3 then 'myfunc is not assigned to a variable but the result is needed for the test

When you use :

myvar=Myfunc() 

Then you will not trash the registers. So in such a case there is no problem to run code after the function assignment.

To keep it safe, assign the result just before you exit the function.

![notice](notice.jpg)IMPORTANT

In order to prevent memory overwrites there are some things you need to be aware of. 

All data types have a fixed length. A byte takes 1 byte, a word takes 2 bytes, etc. 

Strings have a variable length. When you dimension the string you specify the maximum amount of memory that will be used by the string.

DIM S as string * 10 means that 10 bytes + 1 trailer byte, will be reserved in RAM for string named S.

When you assign this string with a constant the compiler will check if the assigned string is dimensioned large enough to hold the string constant. You will get an error if it does not fit.

But when you assign a string with a function or other string, or perform a string concatenation (+ string) there is no such check. This means that you can overwrite the memory that is placed behind the string.

Consider the following examples. 

Example 1, this will give an error since the constant will not fit.

```vb
$RegFile = "m88def.dat"  
$Crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
  
dim s as string *10  
```
s="0123456789A"   
End

Example 2, this will be ok since the string is large enough.

```vb
$RegFile = "m88def.dat"  
$Crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
  
dim s as string *10  
```
s="0123456789"  
End

![notice](notice.jpg)

Example 3, this will give no error but will overwrite memory since data is added to the string which is not large enough

```vb
$RegFile = "m88def.dat"  
$Crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
  
dim s as string *10  
```
s="0123456789"  
s=s+"abc"  
End

![notice](notice.jpg)

Example 4, this is the same as sample 3 but will demonstrate that variable B will be overwritten

```vb
$RegFile = "m88def.dat"  
$Crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
  
dim s as string *10 ,b as byte  
```
b=123  
s="0123456789"  
s=s+"abc"  
```vb
print b  
  
End

```
Example 5, this is when you reserve 100 bytes for the frame/temp space, but you pass data which would take more than that. You get an error in that case.

```vb
$regfile = "m128def.dat"  
$crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100 'notice that it is 100  
  
Declare Sub test(ByVal S As String * 160)  
' ^^^^ will not fit  
```
Call test("012")  
  
Sub test(ByVal S As String * 160)  
Local vs As String * 3  
vs = "AAA"  
End Sub

In example 6 we pass a constant but we specified a maximum length, and we will get error 119 : constant too big to fit

```vb
$regfile = "m128def.dat"  
$crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100   
  
Declare Sub test(ByVal S As String * 10)  
  
```
Call test("0123456789a") 'notice that the size is 11 so we get an error  
  
Sub test(ByVal S As String * 10)  
Local vs As String * 3  
vs = "AAA"  
End Sub

In example 7 we use $FRAMECHECK to see if the data will fit. We call the same sub (recursive) and we never exit which mean the memory is never released. So after a few calls we run out of space and ERR becomes 1

```vb
$regfile = "m128def.dat"  
$crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
$FrameCheck  
  
Declare Sub test(ByVal S As String * 10)  
  
```
Call test("0123456789")  
  
Sub test(ByVal S As String * 10)  
Local vs As String * 3  
```vb
print err 'will be 1 when there is not enough frame space  
'you will see that ERR will be 0 but becomes 1 when there is not enough space  
```
vs = "AAA"  
test "abc" 'call ourselves which is not smart but will demo the check  
End Sub

![notice](notice.jpg)

In example 8 we see how unsafe it can be when you do not specify the length of the string

```vb
$regfile = "m128def.dat"  
$crystal = 8000000  
$hwstack = 50  
$swstack = 40  
$framesize = 100  
$FrameCheck  
  
Declare Sub test(ByVal S As String)  
  
```
Call test("0123")  
  
Sub test(ByVal S As String)  
Local vs As String * 3  
```vb
print err 'will be 1 when there is not enough frame space  
'you will see that ERR will be 0 but becomes 1 when there is not enough space  
```
vs = "AAA"  
S = "012345" '<\--- This overwrites local vs  
```vb
print err'there was enough space so we get 0, still there is an overwrite  
End Sub

```
See also

[CALL](call.md), [SUB](sub.md) , [CONFIG SUBMODE](config_submode.md) , [EXIT](exit.md) , [$FRAMECHECK](hwcheck.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : function.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of user function

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

'A user function must be declare before it can be used.

'A function must return a type

Declare Function Myfunction(byval I As Integer , S As String) As Integer

'The byval paramter will pass the parameter by value so the original value

'will not be changed by the function

Dim K As Integer

Dim Z As String * 10

Dim T As Integer

'assign the values

```
K = 5

Z = "123"

T = Myfunction(k , Z)

```vb
Print T

End

Function Myfunction(byval I As Integer , S As String) As Integer

'you can use local variables in subs and functions

```
Local P As Integer

P = I

```vb
'because I is passed by value, altering will not change the original

'variable named k

```
I = 10

P = Val(s) + I

```vb
'finally assign result

'Note that the same data type must be used !

'So when declared as an Integer function, the result can only be

'assigned with an Integer in this case.

```
Myfunction = P

End Function