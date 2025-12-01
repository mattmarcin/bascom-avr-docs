# INPUTHEX

Action

Allows hexadecimal input from the keyboard during program execution.

Syntax

INPUTHEX [" prompt" ] , var[ , varn ]

Remarks

prompt | An optional string constant printed before the prompt character.  
---|---  
Var,varn | A numeric variable to accept the input value.  
  
The INPUTHEX routine can be used when you have a RS-232 interface on your uP.

The RS-232 interface can be connected to a serial communication port of your computer.

This way you can use a terminal emulator and the keyboard as input device.

You can also use the build in terminal emulator.

The input entered may be in lower or upper case (0-9 and A-F)

```vb
If var is a byte then the input can be maximum 2 characters long.

If var is an integer/word then the input can be maximum 4 characters long.

If var is a long then the input can be maximum 8 characters long.

```
In VB you can specify &H with INPUT so VB will recognize that a hexadecimal string is being used.

BASCOM implements a new statement: INPUTHEX. This is only to save code as otherwise also code would be needed for decimal conversion.

See also

[INPUT](input.md) , [ECHO](echo.md) , [INPUTBIN](inputbin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : input.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: INPUT, INPUTHEX

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

Dim V As Byte , B1 As Byte

Dim C As Integer , D As Byte

Dim S As String * 15

Input "Use this to ask a question " , V

Input B1 'leave out for no question

Input "Enter integer " , C

Print C

```
Inputhex "Enter hex number (4 bytes) " , C

Print C

Inputhex "Enter hex byte (2 bytes) " , D

```vb
Print D

Input "More variables " , C , D

Print C ; " " ; D

Input C Noecho 'supress echo

Input "Enter your name " , S

Print "Hello " ; S

Input S Noecho 'without echo

Print S

End

```