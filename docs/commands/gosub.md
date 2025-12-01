# GOSUB

Action

Branch to and execute subroutine.

Syntax

GOSUB label

Remarks

Label | The name of the label where to branch to.  
---|---  
  
With GOSUB, your program jumps to the specified label, and continues execution at that label.

When it encounters a RETURN statement, program execution will continue after the GOSUB statement.

A GOSUB can not pass parameters, all it does is calling a label, execute it and returns.

So why use a GOSUB? Imagine you have a set of code you want to execute from different locations in your code.

While you can repeat the code, you can best write the code once, and call it using GOSUB.

Example :

```vb
if a = 1 Then

Gosub ABC

end if

if b =1 then

gosub ABC

End if

End

```
ABC:

print "this is label ABC"

a=a+1

```vb
RETURN

If A and B are both 1, the ABC label is called twice. 

Do notice the END statement which will make sure that the code does not execute the ABC label without an actual GOSUB. You can test in the simulator, and see what happens in you remark the END statement.

```
![notice](notice.jpg)Instead of using GOSUB, it is better to use a SUB procedure with a CALL. A SUB module can have local variables and you can pass parameters. 

See also

[GOTO](goto.md) , [CALL](call.md) , [RETURN](return.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : gosub.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: GOTO, GOSUB and RETURN

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

Goto Continue

Print "This code will not be executed"

```
Continue: 'end a label with a colon

```vb
Print "We will start execution here"

Gosub Routine

Print "Back from Routine"

End

```
Routine: 'start a subroutine

```vb
Print "This will be executed"

Return 'return from subroutine

```