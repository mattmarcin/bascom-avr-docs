# $LCDPUTDATA

Action

Specifies that LCD data output must be redirected.

Syntax

$LCDPUTDATA = label

Remarks

Label | The name of the assembler routine that must be called when a character is printed with the LCD statement. The character must be placed in R24.  
---|---  
  
With the redirection of the LCD statement, you can use your own routines.

See also

[$LCDPUTCTRL](lcdputctrl.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'dimension used variables

Dim S As String* 10

Dim W As Long

'inform the compiler which routine must be called to get serial 'characters

$lcdputdata= Myoutput

$lcdputctrl= Myoutputctrl

'make a never ending loop

Do

```
Lcd "test"

```vb
Loop

End

'custom character handling routine

'instead of saving and restoring only the used registers

'and write full ASM code, we use Pushall and PopAll to save and 'restore

'all registers so we can use all BASIC statements

'$LCDPUTDATA requires that the character is passed in R24

```
Myoutput:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return

MyoutputCtrl:

Pushall 'save all registers

'your code here

Popall 'restore registers

Return