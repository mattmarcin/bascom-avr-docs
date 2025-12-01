# READEEPROM

Action

Reads the content from the DATA EEPROM and stores it into a variable.

Syntax

READEEPROM var , address

Remarks

Var | The name of the variable that must be stored  
---|---  
Address | The address in the EEPROM where the data must be read from.  
  
This statement is provided for backwards compatibility with BASCOM-8051.

You can also use the ERAM variable instead of READEEPROM :

```vb
Dim V as Eram Byte 'store in EEPROM

Dim B As Byte 'normal variable

```
B = 10

V = B 'store variable in EEPROM

B = V 'read from EEPROM

When you use the assignment version, the data types must be equal!

According to a data sheet from ATMEL, the first location in the EEPROM with address 0, can be overwritten during a reset so don't use it.

You may also use ERAM variables as indexes. Like :

Dim ar(10) as Eram Byte

When you omit the address label in consecutive reads, you must use a new READEEPROM statement. It will not work in a loop:

Readeeprom B , Label1

```vb
Print B

Do

```
Readeeprom B

Print B Loop

Until B = 5

This will not work since there is no pointer maintained. The way it will work :

ReadEEprom B , Label1 ' specify label

ReadEEPROM B ' read next address in EEPROM

ReadEEPROM B ' read next address in EEPROM

OR

```vb
Dim Next_Read as Integer

Dim In_byte as Byte

Dim Eerom_position as Integer

```
Eerom_position = 20 ' Set the start read point in eerom

For Next_Read = 1 To 5 Step 1 ' Set up the bytes to be read from eeprom

Readeeprom In_byte , eeprom_position ' Use a variable as the pointer to eeprom location

Call another_sub_routine ' 

Incr Chr_pos_font ' Now set pointer for next eeprom data byte

Next

In the XMEGA, you need to set the mode to mapped : [CONFIG EEPROM](config_eeprom.md) = MAPPED.

See also

[WRITEEEPROM](writeeeprom.md) , [$EEPROM](eeprom.md)

ASM

NONE

Example

```vb
'-----------------------------------------------------------------------------------------

'name : eeprom2.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows how to use labels with READEEPROM

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

'first dimension a variable

Dim B As Byte

Dim Yes As String * 1

'Usage for readeeprom and writeeprom :

'readeeprom var, address

'A new option is to use a label for the address of the data

'Since this data is in an external file and not in the code the eeprom data

'should be specified first. This in contrast with the normal DATA lines which must

'be placed at the end of your program!!

'first tell the compiler that we are using EEPROM to store the DATA

$eeprom

'the generated EEP file is a binary file.

'Use $EEPROMHEX to create an Intel Hex file usable with AVR Studio.

'$eepromhex

'specify a label

```
Label1:

Data 1 , 2 , 3 , 4 , 5

Label2:

Data 10 , 20 , 30 , 40 , 50

```vb
'Switch back to normal data lines in case they are used

$data

'All the code above does not generate real object code

'It only creates a file with the EEP extension

'Use the new label option

```
Readeeprom B , Label1

```vb
Print B 'prints 1

'Succesive reads will read the next value

'But the first time the label must be specified so the start is known

```
Readeeprom B

Print B 'prints 2

Readeeprom B , Label2

Print B 'prints 10

Readeeprom B

```vb
Print B 'prints 20

'And it works for writing too :

'but since the programming can interfere we add a stop here

Input "Ready?" , Yes

```
B = 100

Writeeeprom B , Label1

B = 101

Writeeeprom B

'read it back

Readeeprom B , Label1

```vb
Print B 'prints 100

'Succesive reads will read the next value

'But the first time the label must be specified so the start is known

```
Readeeprom B

```vb
Print B 'prints 101

End

```