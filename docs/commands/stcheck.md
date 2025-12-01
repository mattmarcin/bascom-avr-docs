# STCHECK

Action

Calls a routine to check for various stack overflows. This routine is intended for debug purposes.

Syntax

STCHECK

Remarks

The different stack spaces used by BASCOM-AVR lead to lots of questions about them.

The STCHECK routine can help to determine if the stack size are trashed by your program. The program STACK.BAS is used to explain the different settings.

Note that STCHECK should be removed form your final program. That is once you tested your program and found out is works fine, you can remove the call to STCHECK since it costs time and code space.

The settings used are :

Hwstack = 8

Softstack = 2

Framesize = 14

Below is a part of the memory of the 90S2313 used for the example:

C0 C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE CF

D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE DF

FR FR FR FR FR FR FR FR

FR FR FR FR FR FR YY YY SP SP SP SP SP SP SP SP

Since the last memory in SRAM is DF, the hardware stack is occupied by D8-DF(8 bytes)

When a call is made or a push is used the data is saved at the position the hardware stack pointer is pointing to. After this the stack pointer is decreased.

A call uses 2 bytes so SP will be SP-2. (DF-2) =DD

When 8 bytes are stored the SP will point to D7. Another call or push will thus destroy memory position D7 which is occupied by the soft stack.

The soft stack begins directly after the hardware stack and is also growing down.

The Y pointer(r28+r29) is used to point to this data.

Since the Y pointer is decreased first and then the data is saved, the pointer must point at start up to a position higher. That is D8, the end of the hardware space.

St -y,r24 will point to D8-1=D7 and will store R24 at location D7.

Since 2 bytes were allocated in this example we use D7 and D6 to store the data.

When the pointer is at D6 and another St -y,r24 is used, it will write to position D5 which is the end of the frame space that is used as temporarily memory.

The frame starts at C8 and ends at D5. Writing beyond will overwrite the soft stack.

And when there is no soft stack needed, it will overwrite the hardware stack space.

The map above shows FR(frame), YY(soft stack data) and SP(hardware stack space)

How to determine the right values?

The stack check routine can be used to determine if there is an overflow.

It will check :

-if SP is below it's size. In this case below D8.

-if YY is below itâs size in this case when it is D5

-if the frame is above its size in this case D6

When is YY(soft stack) used? When you use a LOCAL variable inside a SUB or function. Each local variable will use 2 bytes.

When you pass variables to user Subroutines or functions it uses 2 bytes for each parameter.

call mysub(x,y) will use 2 * 2 = 4 bytes.

local z as byte ' will use another 2 bytes

This space is freed when the routine ends.

But when you call another sub inside the sub, you need more space.

sub mysub(x as byte,y as byte)

call testsub(r as byte) ' we must add another 2 bytes

When you use empty(no params) call like :

call mytest() , No space is used.

When do you need frame space?

When ever you use a num<>string conversion routine like:

Print b (where b is a byte variable)

Bytes will use 4 bytes max (123+0)

Integer will use 7 bytes max (-12345+0)c

Longs will use 16 bytes max

And the single will use 24 bytes max

When you add strings and use the original the value must be remembered by the compiler.

Consider this :

s$ = "abcd" + s$

Here you give s$ a new value. But you append the original value so the original value must be remembered until the operation has completed. This copy is stored in the frame too.

So when string s$ was dimmed with a length of 20, you need a frame space of 20+1(null byte)

When you pass a variable by VALUE (BYVAL) then you actually pass a copy of the variable.

When you pass a byte, 1 byte of frame space is used, a long will take 4 bytes.

When you use a LOCAL LONG, you also need 4 bytes of frame space to store the local long.

The frame space is reused and so is the soft stack space and hardware stack space.

So the hard part is to determine the right sizes!

The stack check routine must be called inside the deepest nested sub or function.

Gosub test

test:

```vb
gosub test1

return

```
test1:

' this is the deepest level so check the stack here

stcheck

return

Stcheck will use 1 variable named ERROR. You must dimension it yourself.

Dim Error As Byte

Error will be set to :

1: if hardware stack grows down into the soft stack space

2: if the soft stack space grows down into the frame space

3: if the frame space grows up into the soft stack space.

The last 2 errors are not necessarily bad when you consider that when the soft stack is not used for passing data, it may be used by the frame space to store data. Confusing right.?

![notice](notice.jpg) It is advised to use the simpler DBG/$DBG method. This requires that you can simulate your program.

ASM

Routines called by STCHECK :

_StackCheck : uses R24 and R25 but these are saved and restored.

Because the call uses 2 bytes of hardware stack space and the saving of R24 and R25 also costs 2 bytes, it uses 4 more bytes of hardware stack space than your final program would do that f course does not need to use STCHECK.

Example

```vb
'-----------------------------------------------------------------------------------------

'name : stack.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to check for the stack sizes

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 8 ' default use 32 for the hardware stack

$swstack = 2 ' default use 10 for the SW stack

$framesize = 14 ' default use 40 for the frame space

'settings must be :

'HW Stack : 8

'Soft Stack : 2

'Frame size : 14

'note that the called routine (_STACKCHECK) will use 4 bytes

'ofhardware stack space

'So when your program works, you may subtract the 4 bytes of the needed hardware stack size

'in your final program that does not include the STCHECK

'testmode =0 will work

'testmode =1 will use too much hardware stack

'testmode =2 will use too much soft stack space

'testmode =3 will use too much frame space

```
Const Testmode = 0

```vb
'compile and test the program with testmode from 0-3

'you need to dim the ERROR byte !!

Dim Error As Byte

#if Testmode = 2

Declare Sub Pass(z As Long , Byval K As Long)

#else

Declare Sub Pass()

#endif

Dim I As Long

```
I = 2

```vb
Print I

'call the sub in your code at the deepest level

'normally within a function or sub

#if Testmode = 2

```
Call Pass(i , 1)

#else

Call Pass()

```vb
#endif

End

#if Testmode = 2

Sub Pass(z As Long , Byval K As Long)

#else

Sub Pass()

#endif

#if Testmode = 3

```
Local S As String * 13

#else

Local S As String * 8

```vb
#endif

Print I

Gosub Test

End Sub

```
Test:

#if Testmode = 1

push r0 ; eat some hardware stack space

push r1

push r2

```vb
#endif

' *** here we call the routine ***

```
Stcheck

```vb
' *** when error <>0 then there is a problem ***

#if Testmode = 1

```
pop r2

pop r1

pop r0

```vb
#endif

Return

```