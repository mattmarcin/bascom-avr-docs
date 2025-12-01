# BCD

Action

Converts a variable stored in BCD format into a string.

Syntax

PRINT BCD( var )

LCD BCD( var)

Remarks

Var | Numeric variable to convert.  
---|---  
  
When you want to use an I2C clock device which stores its values in BCD format you can use this function to print the value correctly.

BCD() displays values with a leading zero.

The BCD() function is intended for the PRINT/LCD statements.

Use the MAKEBCD function to convert variables from decimal to BCD.

Use the MAKEDEC function to convert variables from BCD to decimal.

See also

[MAKEDEC](makedec.md) , [MAKEBCD](makebcd.md)

ASM

Calls: _BcdStr

Input: X hold address of variable

Output: R0 with number of bytes, frame with data.

Example

```vb
'--------------------------------------------------------------------------------

'name : bcd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of split and combine BCD Bytes

'suited for demo : yes

'commercial addon needed : no

'use in simulator : possible

'--------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'===============================================================================

' Set up Variables

'===============================================================================

Dim A As Byte 'Setup A Variable

Dim B As Byte 'Setup B Variable

Dim C As Byte 'Setup C Variable

```
A = &H89 

```vb
'===============================================================================

' Main

'===============================================================================

```
Main:

```vb
Print "Combined : " ; Hex(a) 'Print A

'-------------------------------------------------------------------------------

```
B = A And &B1111_0000 'Mask To Get Only High Nibble Of Byte

Shift B , Right , 4 'Shift High Nibble To Low Nibble Position , Store As B

C = A And &B0000_1111 'Mask To Get Only Low Nibble Of Byte , Store As C

```vb
Print "Split : " ; B ; " " ; C 'Print B (High Nibble) , C(low Nibble)

'-------------------------------------------------------------------------------

```
Shift B , Left , 4 'Shift Data From Low Nibble Into High Nibble Position

A = B + C 'Add B (High Nibble) And C(low Nibble) Together

```vb
Print "Re-Combined: " ; Hex(a); " " ; Bcd(a)  'Print A (re -combined Byte)

End 'End Program

```