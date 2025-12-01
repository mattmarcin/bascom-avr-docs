# DATA

Action

Specifies constant values to be read by subsequent READ statements.

Syntax

DATA var [, varn]

Remarks

Var | Numeric or string constant.  
---|---  
  
The DATA related statements use the internal registers pair R8 and R9 to store the data pointer.

To store a " sign on the data line, you can use :

DATA $34

The $-sign tells the compiler that the ASCII value will follow.

You can use this also to store special characters that can't be written by the editor such as chr(7)

Another way to include special ASCII characters in your string constant is to use {XXX}. You need to include exactly 3 digits representing the ASCII character. For example 65 is the ASCII number for the character A.

DATA "TEST{065}"

Will be read as TESTA.

While :

DATA "TEST{65}" will be read as :

TEST{65}. This because only 2 digits were included instead of 3.

{xxx} works only for string constants. It will also work in a normal string assignment :

s = "{065}" . This will assign A to the string s.

Because the DATA statements allow you to generate an EEP file to store in EEPROM, the [$DATA](data_1.md) and [$EEPROM](eeprom.md) directives have been added. Read the description of these directives to learn more about the DATA statement.

The DATA statements must not be accessed by the flow of your program because the DATA statements are converted to the byte representation of the DATA.

When your program flow enters the DATA lines, unpredictable results will occur.

So as in QB, the DATA statement is best be placed at the end of your program or in a place that program flow will no enter.

```vb
For example this is fine:

Print "Hello"

Goto jump

```
DATA "test"

Jump:

'because we jump over the data lines there is no problem.

The following example will case some problems:

```vb
Dim S As String * 10

Print "Hello"

```
Restore lbl

Read S

DATA "test"

Print S

When the END statement is used it must be placed BEFORE the DATA lines.

When you have multiple labels with data you need to be aware that each time a label is used, previous data will be aligned to a word. This because the AVR has a word address. This means that :

abc:

DATA 1

klm:

DATA 2

Will consume not 2 bytes but 2 words.

But :

abc:

DATA 1,2

klm:

DATA 3,4

Will also consume 4 bytes. When RESTORE is used, the label address is used which is a word. So take care to put labels only at places which need to be RESTORED/READ.

Difference with QB

Integer and Word constants must end with the %-sign.

Long and Dword constants must end with the &-sign.

Single constants must end with the !-sign.

Double constants must end with the #-sign.

See also

[READ](read.md) , [RESTORE](restore.md) , [$DATA](data_1.md) , [$EEPROM](eeprom.md) , [LOOKUP](lookup.md), [LOOKUPSTR](lookupstr.md) , [LOOKDOWN](lookdown.md) , [$USER](user.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : readdata.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : READ,RESTORE

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

Dim A As Integer , B1 As Byte , Count As Byte

Dim S As String * 15

Dim L As Long

```
Restore Dta1 'point to stored data

For Count = 1 To 3 'for number of data items

Read B1 : Print Count ; " " ; B1

Next

Restore Dta2 'point to stored data

For Count = 1 To 2 'for number of data items

Read A : Print Count ; " " ; A

Next

Restore Dta3

Read S : Print S

Read S : Print S

Restore Dta4

Read L : Print L 'long type

```vb
'demonstration of readlabel

Dim W As Iram Word At 8 Overlay ' location is used by restore pointer

'note that W does not use any RAM it is an overlayed pointer to the data pointer

```
W = Loadlabel(dta1) ' loadlabel expects the labelname

Read B1

```vb
Print B1

End

```
Dta1:

Data &B10 , &HFF , 10

Dta2:

Data 1000% , -1%

Dta3:

Data "Hello" , "World"

```vb
'Note that integer values (>255 or <0) must end with the %-sign

'also note that the data type must match the variable type that is

'used for the READ statement

```
Dta4:

Data 123456789&

```vb
'Note that LONG values must end with the &-sign

'Also note that the data type must match the variable type that is used

'for the READ statement

```