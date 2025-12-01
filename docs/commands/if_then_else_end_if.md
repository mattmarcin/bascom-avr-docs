# IF-THEN-ELSE-END IF

Action

Allows conditional execution or branching, based on the evaluation of a Boolean expression.

Syntax

IF expression THEN

[ ELSEIF expression THEN ]

[ ELSE ]

END IF

Remarks

Expression | Any expression that evaluates to true or false.  
---|---  
  
The one line version of IF can be used :

IF expression THEN statement [ ELSE statement ]

The use of [ELSE] is optional.

Tests like IF THEN can also be used with bits and bit indexes.

IF var.bit = 1 THEN

^--- bit is a variable or numeric constant in the range from 0-255

You can use OR or AND to test on multiple conditions. The conditions are evaluated from left to right. 

```vb
IF A=1 OR A=2 OR A=3 OR B>10 THEN

IF A=1 AND A>3 THEN

Dim Var As Byte, Idx As Byte

```
Var = 255

Idx = 1

```vb
If Var.idx = 1 Then

Print "Bit 1 is 1"

```
EndIf

See also

[ELSE](else.md)

Example

Dim A As Integer

A = 10

```vb
If A = 10 Then 'test expression

Print "This part is executed." 'this will be printed

Else

Print "This will never be executed." 'this not

End If

If A = 10 Then Print "New in BASCOM"

If A = 10 Then Goto Label1 Else print "A<>10"

```
Label1:

Rem The following example shows enhanced use of IF THEN

```vb
If A.15 = 1 Then 'test for bit

Print "BIT 15 IS SET"

```
EndIf

Rem the following example shows the 1 line use of IF THEN [ELSE]

If A.15 = 0 Then Print "BIT 15 is cleared" Else Print "BIT 15 is set"