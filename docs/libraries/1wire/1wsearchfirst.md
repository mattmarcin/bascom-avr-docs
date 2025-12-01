# 1WSEARCHFIRST

Action

This statement reads the first ID from the 1wire bus into a variable(array).

Syntax

var2 = 1WSEARCHFIRST()

var2 = 1WSEARCHFIRST( port , pin)

Remarks

var2 | A variable or array that should be at least 8 bytes long that will be assigned with the 8 byte ID from the first 1wire device on the bus.  
---|---  
port | The PIN port name like PINB or PIND.  
pin | The pin number of the port. In the range from 0-7. Maybe a numeric constant or variable.  
  
The 1wireSearchFirst() function must be called once to initiate the ID retrieval process. After the 1wireSearchFirst() function is used you should use successive function calls to the [1wSearchNext](1wsearchnext.md) function to retrieve other ID's on the bus.

A string can not be assigned to get the values from the bus. This because a null may be returned as a value and the null is also used as a string terminator.

I would advice to use a byte array as shown in the example.

The 1wirecount function will take 4 bytes of SRAM.

___1w_bitstorage , Byte used for bit storage :

lastdeviceflag bit 0

id_bit bit 1

cmp_id_bit bit 2

search_dir bit 3

___1wid_bit_number, Byte

___1wlast_zero, Byte

___1wlast_discrepancy , Byte

ASM

The following asm routines are called from mcs.lib.

_1wire_Search_First : (calls _1WIRE, _ADJUST_PIN , _ADJUST_BIT_ADDRESS)

Parameters passed : R24 : pin number, R30 : port , X : address of target array

Returns nothing.

See also

[1WWRITE](1wwrite.md) , [1WRESET](1wreset.md) , [1WREAD ](1wread.md), [1WSEARCHNEXT](1wsearchnext.md), [1WIRECOUNT](1wirecount.md)

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