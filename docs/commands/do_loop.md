# DO-LOOP

Action

Repeat a block of statements until condition is true.

Syntax

DO

statements

LOOP [ UNTIL expression]

Remarks

You can exit a DO..LOOP with the EXIT DO statement.

The DO-LOOP is always performed at least once.

The main part of your code can best be executed within a DO.. LOOP.

You could use a GOTO also but it is not as clear as the DO LOOP.

Main:

```vb
' code

GOTO Main

Do

' Code

Loop

```
Of course in the example above, it is simple to see what happens, but when the code consist of a lot of lines of code, it is not so clear anymore what the GOTO Main does.

See also

[EXIT](exit.md) , [WHILE-WEND](while_wend.md) , [FOR-NEXT](for_next.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : do_loop.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: DO, LOOP

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

Dim A As Byte

```
A = 1 'assign a var

```vb
Do 'begin a do..loop

Print A 'print var

```
Incr A 'increase by one

```vb
Loop Until A = 10 'do until a=10

End

'You can write a never-ending loop with the following code

Do

'Your code goes here

Loop

```