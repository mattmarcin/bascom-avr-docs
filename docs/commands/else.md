# ELSE

Action

Executed if the IF-THEN expression is false.

Syntax

ELSE

Remarks

You don't have to use the ELSE statement in an IF THEN .. END IF structure.

You can use the ELSEIF statement to test for another condition.

IF a = 1 THEN

...

ELSEIF a = 2 THEN

..

ELSEIF b1 > a THEN

...

ELSE

...

END IF

See also

[IF](if_then_else_end_if.md) , [END IF](if_then_else_end_if.md) , [SELECT-CASE](select_case_end_select.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : if_then.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: IF, THEN, ELSE

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

Dim A As Byte , B1 As Byte

Input "Number " , A 'ask for number

If A = 1 Then 'test number

Print "You got it!"

End If

If A = 0 Then 'test again

Print "Wrong" 'thats wrong

Else 'print this if a is not 0

Print "Almost?"

End If

```
Rem You Can Nest If Then Statements Like This

B1 = 0

```vb
If A = 1 Then

If B1 = 0 Then

Print "B1=0"

End If

Else

Print "A is not 0"

End If

Input "Number " , A

If A = 1 Then '

Print "Ok"

```
Elseif A = 2 Then 'use elseif for more tests

Print "2" : A = 3

Elseif A = 3 Then

```vb
Print "3"

End If

If A.1 = 1 Then Print "Bit 1 set" 'test for a bit

End

```