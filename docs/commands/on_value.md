# ON VALUE

Action

Branch to one of several specified labels, depending on the value of a variable.

Syntax

ON var GOTO|GOSUB label1 [, label2 ] [,CHECK]

Remarks

Var | The numeric variable to test. This can also be a SFR such as PORTB.  
---|---  
label1, label2 | The labels to jump to depending on the value of var.  
CHECK | An optional check for the number of provided labels. When used, the maximum number of labels is 255.  The check will insert code to jump over the address jump block. This will limit the number of entries.   
  
Note that the index value is zero based. So when var is 0, the first specified label is jumped/branched.

It is important that each possible value has an associated label.

You must specify if you jump to the label or that you call the the label.

Use GOTO to jump to the label. Program flow will continue at that label.

Use GOSUB to call the label. The label must have a matching RETURN. Optional you can call a sub routine but it may not have parameters.

When there are not enough labels, the stack will get corrupted. For example :

ON value GOTO label1, label2

When the variable value has a value of two (2), there is no associated label.

You can use the optional CHECK so the compiler will check the value against the number of provided labels. When there are not enough labels for the value, there will be no GOTO or GOSUB and the next line will be executed.

See Also

[ON INTERRUPT](on_interrupt.md) , [GOTO](goto.md) , [GOSUB](gosub.md)

ASM

The following code will be generated for a non-MEGA micro with ON value GOTO.

Ldi R26,$60 ; load address of variable

Ldi R27,$00 ; load constant in register

Ld R24,X

Clr R25

Ldi R30, Low(ON_1_ * 1) ; load Z with address of the label

Ldi R31, High(ON_1_ * 1)

Add zl,r24 ; add value to Z

Adc zh,r25

Ijmp ; jump to address stored in Z

ON_1_:

Rjmp lbl1 ; jump table

Rjmp lbl2

Rjmp lbl3

The following code will be generated for a non-MEGA micro with ON value GOSUB.

;##### On X Gosub L1 , L2

Ldi R30,Low(ON_1_EXIT * 1)

Ldi R31,High(ON_1_EXIT * 1)

Push R30 ;push return address

Push R31

Ldi R30,Low(ON_1_ * 1) ;load table address

Ldi R31,High(ON_1_ * 1)

Ldi R26,$60

Ld R24,X

Clr R25

Add zl,r24 ; add to address of jump table

Adc zh,r25

Ijmp ; jump !!!

ON_1_:

Rjmp L1

Rjmp L2

ON_1_EXIT:

As you can see a jump is used to call the routine. Therefore the return address is first saved on the stack.

Example 1

```vb
'-----------------------------------------------------------------------------------------

'name : ongosub.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : ON .. GOSUB/GOTO

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

Input "Enter value 0-2 " , A 'ask for input

```
Rem Note That The Starting Value Begins With 0

```vb
On A Gosub L0 , L1 , L2

Print "Returned"

If Portb < 2 Then 'you can also use the portvalue

On Portb Goto G0 , G1

End If

```
End_prog:

End

L0:

```vb
Print "0 entered"

Return

```
L1:

```vb
Print "1 entered"

Return

```
L2:

```vb
Print "2 entered"

Return

```
G0:

```vb
Print "P1 = 0"

Goto End_prog

```
G1:

```vb
Print "P1 = 1"

Goto End_prog

```
Example 2

This sample use call/sub instead of labels

```vb
'-----------------------------------------------------------------------------------------

'name : ongosub.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : ON .. GOSUB/GOTO

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

Declare Sub  L0()

Declare Sub  L1()

Declare Sub  L2()

Dim A As Byte

Input "Enter value 0-2 " , A 'ask for input

```
Rem Note That The Starting Value Begins With 0

```vb
On A Gosub L0 , L1 , L2

Print "Returned"

If Portb < 2 Then 'you can also use the portvalue

On Portb Goto G0 , G1

End If

```
End_prog:

```vb
End

Sub L0()

Print "0 entered"

End Sub

Sub L1()

Print "1 entered"

End Sub

Sub L2()

Print "2 entered"

End Sub

```
G0:

```vb
Print "P1 = 0"

Goto End_prog

```
G1:

```vb
Print "P1 = 1"

Goto End_prog

```