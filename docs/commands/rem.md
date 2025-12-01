# REM

Action

Instruct the compiler that comment will follow.

Syntax

REM or '

Remarks

You can and should comment your program for clarity and your later sanity.

You can use REM or ' followed by your comment.

All statements after REM or ' are treated as comments so you cannot use statements on the same line after a REM statement.

Block comments can be used too:

```vb
'( start block comment

print "This will not be compiled

') end block comment

```
Example

Rem TEST.BAS version 1.00

Print A ' " this is comment : PRINT " Hello "

^ - - - This Will Not Be Executed!