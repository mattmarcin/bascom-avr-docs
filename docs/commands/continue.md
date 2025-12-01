# CONTINUE

Action

The CONTINUE statement will skip code inside a loop till the end of the loop.

Syntax

CONTINUE

Remarks

CONTINUE must be used inside a DO-LOOP, WHILE-WEND or FOR-NEXT loop.

The code jump is always inside the current loop.

Some times you want to skip some code without leaving a loop. You can solve this with a GOTO and a label but use of GOTO creates hard to understand code. For this reason some languages have the CONTINUE statement. 

```vb
DO-LOOP  
DO

```
some code here

some code here

CONTINUE_WILL_JUMP_TO_THIS_POINT

```vb
LOOP

WHILE-WEND

WHILE <CONDIITON>

```
some code here

some code here

CONTINUE_WILL_JUMP_TO_THIS_POINT

```vb
WEND

FOR-NEXT

FOR VAR=START TO END

```
some code here

some code here

CONTINUE_WILL_JUMP_TO_THIS_POINT

NEXT

See also

[EXIT](exit.md) , [REDO](redo.md)

Example

```vb
'-------------------------------------------------------------------------------------------------------------  
' REDO and CONTINUE example  
'  
'-------------------------------------------------------------------------------------------------------------  
$regfile = "m128def.dat"  
$hwstack = 32  
$swstack = 16  
$FrameSize = 24  
  
  
dim b as byte  
```
const test = 0  
  

```vb
#if test = 0  
for b = 1 to 10  
'when REDO is used, the code will continue here  
print b  
if b = 3 then  
```
continue ' when b becomes 3, the code will continue at the NEXT statement  
```vb
end if  
if b = 9 then exit for  
if b = 8 then  
```
redo ' when b becomes 8, the code will continue after the FOR statement, it will not increase the variable B !  
```vb
'so in this example the loop will be forever  
end if  
print b  
'code continues here when CONTINUE is used  
next  
  

#elseif test = 1  
```
b = 0  
do  
incr b  
if b = 2 then  
continue  
elseif b = 3 then  
redo  
```vb
end if  
loop until b > 5  
  

#elseif test = 2  
```
b = 0  
while b < 5  
incr b  
if b = 2 then  
continue  
elseif b = 3 then  
redo  
```vb
end if  
wend  

#endif  
end

```