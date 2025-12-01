# $SERIALINPUT

Action

Specifies that serial input must be redirected.

Syntax

$SERIALINPUT = label

Remarks

Label | The name of the assembler routine that must be called when a character is needed by the INPUT routine. The character must be returned in R24.  
---|---  
  
With the redirection of the INPUT command, you can use your own input routines.

This way you can use other devices as input devices.

Note that the INPUT statement is terminated when a RETURN code (13) is received.

By default when you use INPUT or INKEY(), the compiler will expect data from the COM port. When you want to use a keyboard or remote control as the input device you can write a custom routine that puts the data into register R24 once it needs this data.

See also

[$SERIALOUTPUT](serialoutput.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : $serialinput.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates $SERIALINPUT redirection of serial input

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

'define used crystal

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'dimension used variables

Dim S As String * 10

Dim W As Long

'inform the compiler which routine must be called to get serial characters

$serialinput = Myinput

'make a never ending loop

Do

'ask for name

Input "name " , S

Print S

'error is set on time out

Print "Error " ; Err

Loop

End

'custom character handling routine

'instead of saving and restoring only the used registers

'and write full ASM code, we use Pushall and PopAll to save and restore

'all registers so we can use all BASIC statements

'$SERIALINPUT requires that the character is passed back in R24

```
Myinput:

Pushall 'save all registers

W = 0 'reset counter

Myinput1:

Incr W 'increase counter

! Sbis USR, 7 ' Wait for character

! Rjmp myinput2 'no charac waiting so check again

Popall 'we got something

Err = 0 'reset error

! In _temp1, UDR ' Read character from UART

Return 'end of routine

Myinput2:

If W > 1000000 Then 'with 4 MHz ca 10 sec delay

! rjmp Myinput_exit 'waited too long

```vb
Else

Goto Myinput1 'try again

End If

```
Myinput_exit:

Popall 'restore registers

Err = 1 'set error variable

! ldi R24, 13 'fake enter so INPUT will end

Return