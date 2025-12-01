# ECHO

Action

Turns the ECHO on or off while asking for serial INPUT.

Syntax

ECHO value

Remarks

Value | ON to enable ECHO and OFF to disable ECHO.  
---|---  
  
When you use INPUT to retrieve values for variables, all info you type can be echoed back. In this case you will see each character you enter. When ECHO is OFF, you will not see the characters you enter.

In versions 1.11.6.2 and earlier the ECHO options were controlled by an additional parameter on the INPUT statement line like : INPUT "Hello " , var NOECHO

This would suppress the ECHO of the typed data. The new syntax works by setting ECHO ON and OFF. For backwards compatibility, using NOECHO on the INPUT statement line will also work. In effect it will turn echo off and on automatic.

By default, ECHO is always ON.

See also

[INPUT](input.md)

ASM

The called routines from mcs.lib are _ECHO_ON and _ECHO_OFF

The following ASM is generated when you turn ECHO OFF.

Rcall Echo_Off

This will set bit 3 in R6 that holds the ECHO state.

When you turn the echo ON the following code will be generated

Rcall Echo_On

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