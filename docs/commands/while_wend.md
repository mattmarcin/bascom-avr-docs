# WHILE-WEND

Action

Executes a series of statements in a loop, as long as a given condition is true.

Syntax

WHILE condition

statements

WEND

Remarks

If the condition is true then any intervening statements are executed until the WEND statement is encountered.

BASCOM then returns to the WHILE statement and checks the condition.

```vb
If it is still true, the process is repeated.

If it is not true, execution resumes with the statement following the WEND statement.

```
So in contrast with the DO-LOOP structure, a WHILE-WEND condition is tested first so that if the condition fails, the statements in the WHILE-WEND structure are never executed.

See also

[DO-LOOP](do_loop.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : while_w.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: WHILE, WEND

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
A = 1 'assign var

```vb
While A < 10 'test expression

Print A 'print var

```
Incr A 'increase by one

```vb
Wend 'continue loop

End

```