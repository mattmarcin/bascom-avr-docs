# $EEPROM

Action

Instruct the compiler to store the data in the DATA lines following the $EEPROM directive in an EEP file.

Syntax

$EEPROM

Remarks

The AVR has built-in EEPROM. With the WRITEEEPROM and READEEPROM statements, you can write to and read from the EEPROM.

To store information in the EEPROM, you can add DATA lines to your program that hold the data that must be stored in the EEPROM.

A separate file is generated with the EEP extension. This file can be used to program the EEPROM.

The compiler must know which DATA must go into the code memory and which into the EEPROM memory and therefore two compiler directives were added.

```vb
$EEPROM and $DATA.

$EEPROM tells the compiler that the DATA lines following the compiler directive must be stored in the EEP file.

```
To switch back to the default behavior of the DATA lines, you must use the $DATA directive.

The READ statement that is used to read the DATA info may only be used with normal DATA lines. It does not work with DATA stored in EEPROM.

![notice](notice.jpg) Do not confuse $DATA directive with the DATA statement.

So while normal DATA lines will store the specified data into the code memory of the micro which is called the flash memory, the [$EEPROM](eeprom.md) and $DATA will cause the data to be stored into the EEPROM. The EEP file is a binary file. The [$EEPROMHEX](_eepromhex.md) directive can be used to create Intel HEX records in the EEP file 

See also

[$EEPROM](eeprom.md) , [READEEPROM](readeeprom.md) , [WRITEEEPROM](writeeeprom.md) , [DATA](data_2.md) , [$EEPROMHEX](_eepromhex.md)

ASM

NONE

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates $DATA directive

'-------------------------------------------------------------------------------

$regfile = "2313def.dat"  
$baud = 19200  
$crystal = 4000000 ' 4 MHz crystal  
$hwstack = 16  
$swstack = 16  
$framesize = 16  
  
Dim B As Byte  
```
Readeeprom B , 0 'now B will be 1  
End  
  
Dta:  
$eeprom  
Data 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8  
```vb
$data  
End

```