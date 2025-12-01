# CONST

Action

Declares a symbolic constant.

Syntax

CONST symbol = numconst

CONST symbol = stringconst

CONST symbol = expression

Remarks

Symbol | The name of the symbol.  
---|---  
Numconst | The numeric value to assign to the symbol.  
Stringconst | The string to assign to the symbol  
Expression | An expression that returns a value to assign the constant  
  
Assigned constants consume no program memory because they only serve as a reference to the compiler.

The compiler will replace all occurrences of the symbol with the assigned value.

You can use a constant to give a value a more meaningful name.

For example : 

variable = 1

const optHeaterOn = 1

variable = optHeaterOn

The source code is better to read when you assign a constant. Even better when the values change later, for example when HeaterOn becomes 2, you only need to replace 1 line of code.

See also

[ALIAS](alias.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : const.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo for constants

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

'dimension some variables

Dim Z As String * 10

Dim B As Byte

'assign some constants

'constants dont use program memory

```
Const S = "test"

Const A = 5 'declare a as a constant

Const B1 = &B1001

'or use an expression to assign a constant

Const X =(b1 * 3) + 2

Const Ssingle = Sin(1)

```vb
Print X

Print Ssingle

```
B = A

'the same as b = 5

Z = S

```vb
'the same as Z = "test"

Print A

Print B1

Print S

'you can use constants with conditional compilation

#if A = 5 ' note there is no then

Print "constant a is 5"

#if S = "test"

Print "nested example"

#else ' else is optional

#endif

#else

#endif

End

```