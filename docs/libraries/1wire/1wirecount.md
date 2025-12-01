# 1WIRECOUNT

Action

This statement reads the number of 1wire devices attached to the bus.

Syntax

var2 = 1WIRECOUNT()

var2 = 1WIRECOUNT( port , pin)

Remarks

var2 | A WORD variable that is assigned with the number of devices on the bus.  
---|---  
port | The PIN port name like PINB or PIND.  
pin | The pin number of the port. In the range from 0-7. May be a numeric constant or variable.  
  
The variable must be of the type word or integer.

You can use the 1wirecount() function to know how many times the 1wsearchNext() function should be called to get all the Id's on the bus.

The 1wirecount function will take 4 bytes of SRAM.

___1w_bitstorage , Byte used for bit storage :

lastdeviceflag bit 0

id_bit bit 1

cmp_id_bit bit 2

search_dir bit 3

___1wid_bit_number, Byte

___1wlast_zero, Byte

___1wlast_discrepancy , Byte

When there is no 1WIRE device on the bus, the ERR bit will be set. When devices are found, ERR will be cleared.

ASM

The following asm routines are called from mcs.lib.

_1wire_Count : (calls _1WIRE, _1WIRE_SEARCH_FIRST , _1WIRE_SEARCH_NEXT)

Parameters passed : R24 : pin number, R30 : port , Y+0,Y+1 : 2 bytes of soft stack, X : pointer to the frame space

Returns Y+0 and Y+1 with the value of the count. This is assigned to the target variable.

See also

[1WWRITE](1wwrite.md) , [1WRESET](1wreset.md) , [1WREAD ](1wread.md), [1WSEARCHFIRST](1wsearchfirst.md), [1WSEARCHNEXT](1wsearchnext.md) , [Using the 1wire protocol](using_the_1_wire_protocol.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wireSearch.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wsearch

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

'The following internal bytes are used by the scan routines

'___1w_bitstorage , Byte used for bit storage :

' lastdeviceflag bit 0

' id_bit bit 1

' cmp_id_bit bit 2

' search_dir bit 3

'___1wid_bit_number, Byte

'___1wlast_zero, Byte

'___1wlast_discrepancy , Byte

'___1wire_data , string * 7 (8 bytes)

'[DIM variables used]

'we need some space from at least 8 bytes to store the ID

Dim Reg_no(8) As Byte

'we need a loop counter and a word/integer for counting the ID's on the bus

Dim I As Byte , W As Word

'Now search for the first device on the bus

```
Reg_no(1) = 1wsearchfirst()

```vb
For I = 1 To 8 'print the number

Print Hex(reg_no(i));

Next

Print

Do

'Now search for other devices

```
Reg_no(1) = 1wsearchnext()

```vb
For I = 1 To 8

Print Hex(reg_no(i));

Next

Print

Loop Until Err = 1

'When ERR = 1 is returned it means that no device is found anymore

'You could also count the number of devices

```
W = 1wirecount()

```vb
'It is IMPORTANT that the 1wirecount function returns a word/integer

'So the result variable must be of the type word or integer

'But you may assign it to a byte or long too of course

Print W

'as a bonus the next routine :

' first fill the array with an existing number

```
Reg_no(1) = 1wsearchfirst()

```vb
' unremark next line to chance a byte to test the ERR flag

'Reg_no(1) = 2

'now verify if the number exists

```
1wverify Reg_no(1)

```vb
Print Err

'err =1 when the ID passed n reg_no() does NOT exist

' optinal call it with pinnumber line 1wverify reg_no(1),pinb,1

'As for the other 1wire statements/functions, you can provide the port and pin number as anoption

'W = 1wirecount(pinb , 1) 'for example look at pin PINB.1

End

```