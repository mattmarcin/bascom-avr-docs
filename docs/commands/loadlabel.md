# LOADLABEL

Action

Assigns a word variable with the address of a label.

Syntax

Var = LOADLABEL(label )

Remarks

var | The variable that is assigned with the address of the label.  
---|---  
lbl | The name of the label  
  
In some cases you might need to know the address of a point in your program. To perform a Cpeek() for example.

You can place a label at that point and use LoadLabel to assign the address of the label to a variable.

When you assign a DWORD variable, the 24 bit address will be loaded into the variable. 

If you use Loadlabel on an EEPROM label (a label used in the $EEPROM data area) , these labels must precede the Loadlabel function.

This would be ok :

$eeprom ' eeprom image

label1:

data 1,2,3,4,5

label2:

data 6,7,8,9,10

```vb
$data ' back to normal mode

dim w as word

```
w=loadlabel(label2)

This code will work since the loadlabel is used after the EEPROM data labels.