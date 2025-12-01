# WRITEEEPROM

Action

Write a variables content to the DATA EEPROM.

Syntax

WRITEEEPROM var , address

Remarks

var | The name of the variable that must be stored  
---|---  
address | The address in the EEPROM where the variable must be stored. A new option is that you can provide a label name for the address. See example 2.  
  
This statement is provided for compatibility with BASCOM-8051.

You can better use :

```vb
Dim V as Eram Byte 'store in EEPROM

Dim B As Byte 'normal variable

```
B = 10

V = B 'store variable in EEPROM which is the actual writeeeprom

When you use the assignment version, the data types must be the same!

According to a data sheet from ATMEL, the first location in the EEPROM with address 0, can be overwritten during a reset. It is advised not to use this location.

For security, register R23 is set to a magic value before the data is written to the EEPROM.

All interrupts are disabled while the EEPROM data is written. Interrupts are enabled automatic after the data is written.

It is advised to use the Brownout circuit that is available on most AVR processors. This will prevent that data is written to the EEPROM when the voltage drops under the specified level.

When data is written to the EEPROM, all interrupts are disabled, and after the EEPROM has been written, the interrupts are re-enabled.

In the XMEGA, you need to set the mode to mapped : [CONFIG EEPROM](config_eeprom.md) = MAPPED.

![notice](notice.jpg)When you define a constant named UPDATEEPROM the eprom cells will be only written when the value differs. Instead of just writing the value, the EPROM content is first read and compared to the new value. Only when the new value differs the new value is written to the EEPROM. A memory location can be written to 100.000 times at least. 

The constant UPDATEEPROM can have any value. There is only a check if this constant is defined. So even : CONST UPDATEEPROM=0 will use the special update code.

See also

[READEEPROM](readeeprom.md)

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