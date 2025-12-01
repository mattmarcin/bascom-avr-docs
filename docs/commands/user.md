# $USER

Action

This directive will let the compiler create an .usr file that contains the data following this directive. Switch back to normal DATA statements with $DATA

Syntax

$USER

Remarks

Some new UPDI processors have a large User Signature data area. While smaller User Signature areas can be changed by the UPDI programmer, it is not practical when the size is larger than 64 bytes.

The MCS EDBG programmer has a new TAB : User Signature where you can change data similar as the EEPROM TAB. 

You can create an .USR file using the $USER directive followed by DATA statements. Switch back to normal Flash DATA using $DATA, the default. 

The file the compiler creates is a binary file. The MCS EDBG programmer will load the data automatically when it exists.

See also

[READUSERSIG](readusersig.md) , [$DATA](data_2.md) , [DATA](data_1.md)

Partial Example

  
```vb
'create .usr data file  
$user  
```
Data 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16  
```vb
' ^ address 0  
'switch back to normal DATA lines  
$data  
```
Data 10 , 20