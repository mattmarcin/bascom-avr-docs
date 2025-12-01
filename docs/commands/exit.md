# EXIT

Action

Exit a FOR..NEXT, DO..LOOP , WHILE ..WEND, SUB..END SUB or FUNCTION..END FUNCTION.

Syntax

```vb
EXIT FOR

EXIT DO

EXIT WHILE

EXIT SUB

EXIT FUNCTION

```
Remarks

With the EXIT statement you can exit a structure at any time. 

Remarks about EXIT SUB/FUNCTION

It is important that you exit a SUB or FUNCTION with EXIT. Do not use a RETURN. A return can be used inside a sub routine to return from a sub routine located inside the sub routine.

```vb
For example:

Sub Test()

gosub label1

Exit Sub

```
label1:

```vb
print "test"

return

End Sub

```
When you use EXIT SUB or EXIT FUNCTION, the compiler will create a jump to a label with the sub/function name, prefixed with two underscores.

For example your Sub routine is named Test(), and you use Exit Sub, a label will be created with the name __TEST:

See Also

[DO](do_loop.md), [WHILE](what_is_new_in_2081.md), [FOR](for_next.md) , [SUB](sub.md), [FUNCTION](sub.md) , [CONTINUE](continue.md), [REDO](redo.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : exit.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: EXIT

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

Dim B1 As Byte , A As Byte

```
B1 = 50 'assign var

```vb
For A = 1 To 100 'for next loop

If A = B1 Then 'decision

Exit For 'exit loop

End If

Next

Print "Exit the FOR..NEXT when A was " ; A

```
A = 1

Do

Incr A

```vb
If A = 10 Then

Exit Do

End If

Loop

Print "Loop terminated"

End

```