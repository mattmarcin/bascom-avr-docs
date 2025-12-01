# BCCALL

Action

Calls a subroutine or procedure in the BasicCard.

Syntax

BCCALL name( nad , cla, ins, p1, p2 [param1 , paramn])

Remarks

name | The name of the procedure to all in the BasicCard. It must be defined first with BCDEF. The name used with BCDEF and BCCALL do not need to be the same as the procedure in the BasicCard but it is advised to use the same names.  
---|---  
NAD | Node address byte. The BasicCard responds to all node address values. Use 0 for default.  
CLA | Class byte. First byte of two byte CLA-INS command. Must match the value in the BasicCard procedure.  
INS | Instruction byte. Second byte of two byte CLA-INS command. Must match the value in the BasicCard procedure.  
P1 | Parameter 1 of CLAâINS header.  
P2 | Parameter 2 of CLA-INS header  
  
![notice](notice.jpg)This statements uses BCCARD.LIB, a library that is available separately from MCS Electronics.

When in your BasicCard basic program you use:

'test of passing parameters

Command &hf6 &h01 ParamTest( b as byte, w as integer,l as long)

b=b+1

w=w+1

l=l+1

end command

You need to use &HF6 for CLA and 1 for INS when you call the program:

Bccall Paramtest(0 , &HF6 , 1 , 0 , 0 , B , W , L)

^ NAD

^CLA

^INS

^P1

^P2

When you use BCCALL, the NAD, CLA, INS, P1 and P2 are sent to the BasicCard. The parameter values are also sent to the BasicCard. The BasicCard will execute the command defined with CLA and INS and will return the result in SW1 and SW2.

The parameter values altered by the BasicCard are also sent by the BasicCard.

You can not sent constant values. Only variables may be sent. This because a constant can not be changed.

See Also

[CONFIG BCCARD](config_bccard.md) , [BCDEF](bcdef.md) , [BCRESET](bcreset.md)

Example

```vb
'------------------------------------------------------------------------------

' BCCARD.BAS

' This AN shows how to use the BasicCard from Zeitcontrol

' www.basiccard.com

'------------------------------------------------------------------------------

'connections:

' C1 = +5V

' C2 = PORTD.4 - RESET

' C3 = PIN 4 - CLOCK

' C5 = GND

' C7 = PORTD.5 - I/O

' /--------------------------------\

' | |

' | C1 C5 |

' | C2 C6 |

' | C3 C7 |

' | C4 C8 |

' | |

' \\--------------------------------/

'

'

'----------- configure the pins we use ------------

Config Bccard = D , Io = 5 , Reset = 4

' ^ PORTD.4

' ^------------ PORTD.5

' ^--------------------- PORT D

'Load the sample calc.bas into the basiccard

' Now define the procedure in BASCOM

' We pass a string and also receive a string

```
Bcdef Calc(string)

```vb
'We need to dim the following variables

'SW1 and SW2 are returned by the BasicCard

'BC_PCB must be set to 0 before you start a session

'Our program uses a string to pass the data so DIM it

Dim S As String * 15

'Baudrate might be changed

$baud = 9600

' Crystal used must be 3579545 since it is connected to the Card too

$crystal = 3579545

'Perform an ATR

```
Bcreset

```vb
'Now we call the procedure in the BasicCard

'bccall funcname(nad,cla,ins,p1,p2,PRM as TYPE,PRM as TYPE)

```
S = "1+1+3" ' we want to calculate the result of this expression

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
' ^--- variable to pass that holds the expression

' ^------- P2

' ^----------- P1

' ^--------------- INS

' ^-------------------- CLA

' ^-------------------------- NAD

'For info about NAD, CLA, INS, P1 and P2 see your BasicCard manual

'if an error occurs ERR is set

' The BCCALL returns also the variables SW1 and SW2

Print "Result of calc : " ; S

Print "SW1 = " ; Hex(sw1)

Print "SW2 = " ; Hex(sw2)

'Print Hex(_bc_pcb) ' for test you can see that it toggles between 0 and 40

Print "Error : " ; Err

'You can call this or another function again in this session

```
S = "2+2"

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
Print "Result of calc : " ; S

Print "SW1 = " ; Hex(sw1)

Print "SW2 = " ; Hex(sw2)

'Print Hex(_bc_pcb) ' for test you can see that it toggles between 0 and 40

Print "Error : " ; Err

'perform another ATR

```
Bcreset

Input "expression " , S

Bccall Calc(0 , &H20 , 1 , 0 , 0 , S)

```vb
Print "Answer : " ; S

'----and now perform an ATR as a function

Dim Buf(25) As Byte , I As Byte

```
Buf(1) = Bcreset()

```vb
For I = 1 To 25

Print I ; " " ; Hex(buf(i))

Next

'typical returns :

'TS = 3B

'T0 = EF

'TB1 = 00

'TC1 = FF

'TD1 = 81 T=1 indication

'TD2 = 31 TA3,TB3 follow T=1 indicator

'TA3 = 50 or 20 IFSC ,50 =Compact Card, 20 = Enhanced Card

'TB3 = 45 BWT blocl waiting time

'T1 -Tk = 42 61 73 69 63 43 61 72 64 20 5A 43 31 32 33 00 00

' B a s i c C a r d Z C 1 2 3

'and another test

'define the procedure in the BasicCard program

```
Bcdef Paramtest(byte , Word , Long )

```vb
'dim some variables

Dim B As Byte , W As Word , L As Long

'assign the variables

```
B = 1 : W = &H1234 : L = &H12345678

Bccall Paramtest(0 , &HF6 , 1 , 0 , 0 , B , W , L)

```vb
Print Hex(sw1) ; Spc(3) ; Hex(sw2)

'and see that the variables are changed by the BasicCard !

Print B ; Spc(3) ; Hex(w) ; " " ; Hex(l)

'try the echotest command

```
Bcdef Echotest(byte)

Bccall Echotest(0 , &HC0 , &H14 , 1 , 0 , B)

```vb
Print B

End 'end program

```
Rem BasicCard Sample Source Code

Rem ------------------------------------------------------------------

Rem Copyright (C) 1997-2001 ZeitControl GmbH

Rem You have a royalty-free right to use, modify, reproduce and

Rem distribute the Sample Application Files (and/or any modified

Rem version) in any way you find useful, provided that you agree

Rem that ZeitControl GmbH has no warranty, obligations or liability

Rem for any Sample Application Files.

Rem ------------------------------------------------------------------

```vb
#Include CALCKEYS.BAS

Declare ApplicationID = "BasicCard Mini-Calculator"

```
Rem This BasicCard program contains recursive procedure calls, so the

Rem compiler will allocate all available RAM to the P-Code stack unless

Rem otherwise advised. This slows execution, because all strings have to

Rem be allocated from EEPROM. So we specify a stack size here:

```vb
#Stack 120

' Calculator Command (CLA = &H20, INS = &H01)

'

' Input: an ASCII expression involving integers, and these operators:

'

' * / % + - & ^ |

'

' (Parentheses are also allowed.)

'

' Output: the value of the expression, in ASCII.

'

' P1 = 0: all numbers are decimal

' P1 <> 0: all numbers are hex

' Constants

```
Const SyntaxError = &H81

Const ParenthesisMismatch = &H82

Const InvalidNumber = &H83

Const BadOperator = &H84

```vb
' Forward references

Declare Function EvaluateExpression (S$, Precedence) As Long

Declare Function EvaluateTerm (S$) As Long

Declare Sub Error (Code@)

'test for passing a string

```
Command &H20 &H01 Calculator (S$)

Private X As Long

S$ = Trim$ (S$)

X = EvaluateExpression (S$, 0)

```vb
If Len (Trim$ (S$)) <> 0 Then Call Error (SyntaxError)

If P1 = 0 Then S$ = Str$ (X) : Else S$ = Hex$ (X)

End Command

'test of passing parameters

```
Command &hf6 &h01 ParamTest( b as byte, w as integer,l as long)

b=b+1

w=w+1

l=l+1

```vb
end command

Function EvaluateExpression (S$, Precedence) As Long

```
EvaluateExpression = EvaluateTerm (S$) 

Do

S$ = LTrim$ (S$)

```vb
If Len (S$) = 0 Then Exit Function

Select Case S$(1)

Case "*"

If Precedence > 5 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression * _

EvaluateExpression (S$, 6)

```vb
Case "/"

If Precedence > 5 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression / _

EvaluateExpression (S$, 6)

```vb
Case "%"

If Precedence > 5 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression Mod _

EvaluateExpression (S$, 6)

```vb
Case "+"

If Precedence > 4 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression + _

EvaluateExpression (S$, 5)

```vb
Case "-"

If Precedence > 4 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression - _

EvaluateExpression (S$, 5)

```vb
Case "&"

If Precedence > 3 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression And _

EvaluateExpression (S$, 4)

```vb
Case "^"

If Precedence > 2 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression Xor _

EvaluateExpression (S$, 3)

```vb
Case "|"

If Precedence > 1 Then Exit Function

```
S$ = Mid$ (S$, 2)

EvaluateExpression = EvaluateExpression Or _

EvaluateExpression (S$, 2)

```vb
Case Else

Exit Function

End Select

Loop

End Function

Function EvaluateTerm (S$) As Long

Do ' Ignore unary plus

```
S$ = LTrim$ (S$)

```vb
If Len (S$) = 0 Then Call Error (SyntaxError)

If S$(1) <> "+" Then Exit Do

```
S$ = Mid$ (S$, 2)

```vb
Loop

If S$(1) = "(" Then ' Expression in parentheses

```
S$ = Mid$ (S$, 2)

EvaluateTerm = EvaluateExpression (S$, 0)

S$ = LTrim$ (S$)

If S$(1) <> ")" Then Call Error (ParenthesisMismatch)

S$ = Mid$ (S$, 2)

Exit Function

ElseIf S$(1) = "-" Then ' Unary minus

S$ = Mid$ (S$, 2)

EvaluateTerm = -EvaluateTerm (S$)

```vb
Exit Function

Else ' Must be a number

If P1 = 0 Then ' If decimal

```
EvaluateTerm = Val& (S$, L@)

Else

EvaluateTerm = ValH (S$, L@)

```vb
End If

If L@ = 0 Then Call Error (InvalidNumber)

```
S$ = Mid$ (S$, L@ + 1)

```vb
End If

End Function

Sub Error (Code@)

```
SW1 = &H64

SW2 = Code@

```vb
Exit

End Sub

```