# CALL

Action

Call and execute a subroutine.

Syntax

CALL Test [ (var1, var-n) ]

Remarks

Var1 | Any BASCOM variable or constant.  
---|---  
Var-n | Any BASCOM variable or constant.  
Test | Name of the subroutine. In this case Test.  
  
You can call sub routines with or without passing parameters.

It is important that the SUB routine is DECLARED before you make the CALL to the subroutine. Of course the number of declared parameters must match the number of passed parameters.

It is also important that when you pass constants to a SUB routine, you must DECLARE these parameters with the BYVAL argument. This because a constant has no address, it is assigned at compile time.

With the CALL statement, you can call a procedure or subroutine.

For example: Call Test2

The call statement enables you to implement your own statements.

You don't have to use the CALL statement:

Test2 will also call subroutine test2

When you don't supply the CALL statement, you must leave out the parenthesis.

So Call Routine(x,y,z) must be written as Routine x,y,z

Unlike normal SUB programs called with the GOSUB statement, the CALL statement enables you to pass variables to a SUB routine that may be local to the SUB.

![notice](notice.jpg)By using CONFIG SUBMODE=NEW, you do not need to DECLARE each sub/function.

See also

[DECLARE](declare_sub.md) , [SUB](sub.md) , [EXIT](exit.md) , [FUNCTION](declare_function.md) , [LOCAL](local.md) , [CONFIG SUBMODE](config_submode.md)

Example

```vb
$regfile = "m48def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim A As Byte , B As Byte 'dimension some variables

Declare Sub Test(b1 As Byte , Byval B2 As Byte) 'declare the SUB program

```
A = 65 'assign a value to variable A

Call Test(a , 5)'call test with parameter A and constant

Test A , 5 'alternative call

```vb
Print A 'now print the new value

End

Sub Test(b1 As Byte , Byval B2 As Byte) 'use the same variable names as 'the declared one

Print B1 'print it

Print Bcd(b2)

```
B1 = 10 'reassign the variable

B2 = 15 'reassign the variable

End Sub

![notice](notice.jpg) One important thing to notice is that you can change b2 but that the change will not be reflected to the calling program!

Variable A is changed however.

This is the difference between the BYVAL and BYREF argument in the DECLARE ration of the SUB program.

When you use BYVAL, this means that you will pass the argument by its value. A copy of the variable is made and passed to the SUB program. So the SUB program can use the value and modify it, but the change will not be reflected to the calling parameter. It would be impossible too when you pass a numeric constant for example.

If you do not specify BYVAL, BYREF will be used by default and you will pass the address of the variable. So when you reassign B1 in the above example, you are actually changing parameter A.