# RETURN

Action

Return from a subroutine.

Syntax

RETURN

Remarks

Subroutines must be ended with a related RETURN statement.

Interrupt subroutines must also be terminated with the Return statement.

See also

[GOSUB](gosub.md)

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