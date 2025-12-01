# FOR-NEXT

Action

Execute a block of statements a number of times.

Syntax

FOR var = start TO end [STEP value]

Remarks

var | The variable counter to use  
---|---  
start | The starting value of the variable var  
end | The ending value of the variable var  
value | The value var is increased/decreased with each time NEXT is encountered.  
  
•| For incremental loops, you must use TO.  
---|---  
  
•| For decremental loops, you must use a negative step size.  
---|---  
  
•| You must end a FOR structure with the NEXT statement.  
---|---  
  
•| The use of STEP is optional. By default, a value of 1 is used.  
---|---  
  
When you know in advance how many times a block of code must be executed, the FOR..NEXT loop is convenient to use.

You can exit a FOR .. NEXT loop with the EXIT FOR statement. 

It is important that the if you use variables for START and END, that these are of the same data type. So for example:

```vb
Dim x, as byte, st as byte, ed as byte

FOR x = st TO ED ' this is ok since all variables are of the same data type

Dim x as Byte, st as Word, Ed as Long

FOR x = st TO ED ' this is NOT ok since all variables are of different data type. 

```
The reason is that when the condition is evaluated, it will create a compare on 2 bytes, while you actually want to have a word since the end variable is a word. 

A for next loop with an integer has an upper limit of 32766 and not 32767, the maximum value that fits into an integer.

This is done in order to save code space. Checking an overflow from 32767 to -32768 would cost extra code. 

There are also other alternatives. You can use a Do.. Loop for example :

```vb
Dim Var As Byte

Do

'code

```
Incr Var

Loop Until Var = 10

There are various way to get the result you need.

See also

[EXIT FOR](exit.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : for_next.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: FOR, NEXT

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

Dim A As Byte , B1 As Byte , C As Integer

For A = 1 To 10 Step 2

Print "This is A " ; A

Next A

Print "Now lets count down"

For C = 10 To -5 Step -1

Print "This is C " ; C

Next

Print "You can also nest FOR..NEXT statements."

For A = 1 To 10

Print "This is A " ; A

For B1 = 1 To 10

Print "This is B1 " ; B1

Next ' note that you do not have to specify the parameter

Next A

End

```