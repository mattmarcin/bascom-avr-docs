# 1-Wire Libraries

> Dallas 1-Wire protocol

## 1WIRE



---

## 1WIRECOUNT

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

---

## 1WREAD

Action

This statement reads data from the 1wire bus into a variable.

Syntax

var2 = 1WREAD( [ bytes] )

var2 = 1WREAD( bytes , port , pin)

Remarks

var2 | Reads a byte from the bus and places it into variable var2.  
---|---  
bytes | Optional parameter to specify the number of bytes to read.  
Port | The PIN port name like PINB or PIND.  
Pin | The pin number of the port. In the range from 0-7. Must be a numeric constant or variable.  
  
Multi 1-wire devices on different pins are supported.

To use this you must specify the port pin that is used for the communication.

The 1wreset, 1wwrite and 1wread statements will work together when used with the old syntax. And the pin can be configured from the compiler options or with the [CONFIG 1WIRE statement](config_1wire.md).

The syntax for additional 1-wire devices is :

1WRESET port, pin

1WWRITE var/constant , bytes, port, pin

var = 1WREAD(bytes, port, pin) for reading multiple bytes

See also

[1WWRITE](1wwrite.md) , [1WRESET](1wreset.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wire.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wreset, 1wwrite and 1wread()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' pull-up of 4K7 required to VCC from Portb.2

' DS2401 serial button connected to Portb.2

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'when only bytes are used, use the following lib for smaller code

$lib "mcsbyte.lib"

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

Dim Ar(8) As Byte , A As Byte , I As Byte

Do

Wait 1

```
1wreset 'reset the device

Print Err 'print error 1 if error

1wwrite &H33 'read ROM command

For I = 1 To 8

Ar(i) = 1wread() 'place into array

```vb
Next

'You could also read 8 bytes a time by unremarking the next line

'and by deleting the for next above

'Ar(1) = 1wread(8) 'read 8 bytes

For I = 1 To 8

Print Hex(ar(i)); 'print output

Next

Print 'linefeed

Loop

'NOTE THAT WHEN YOU COMPILE THIS SAMPLE THE CODE WILL RUN TO THIS POINT

'THIS because of the DO LOOP that is never terminated!!!

'New is the possibility to use more than one 1 wire bus

'The following syntax must be used:

For I = 1 To 8

```
Ar(i) = 0 'clear array to see that it works

Next

1wreset Pinb , 2 'use this port and pin for the second device

1wwrite &H33 , 1 , Pinb , 2 'note that now the number of bytes must be specified!

```vb
'1wwrite Ar(1) , 5,pinb,2

'reading is also different

```
Ar(1) = 1wread(8 , Pinb , 2) 'read 8 bytes from portB on pin 2

```vb
For I = 1 To 8

Print Hex(ar(i));

Next

'you could create a loop with a variable for the bit number !

For I = 0 To 3 'for pin 0-3

```
1wreset Pinb , I

1wwrite &H33 , 1 , Pinb , I

Ar(1) = 1wread(8 , Pinb , I)

```vb
For A = 1 To 8

Print Hex(ar(a));

Next

Print

Next

End

```

---

## 1WRESET

Action

This statement brings the 1wire pin to the correct state, and sends a reset to the bus.

Syntax

1WRESET

1WRESET PORT , PIN

Remarks

1WRESET | Reset the 1WIRE bus. The error variable ERR will return 1 if an error occurred  
---|---  
Port | The register name of the input port. Like PINB, PIND.  
Pin | The pin number to use. In the range from 0-7. May be a numeric constant or variable.  
  
The global variable ERR is set when an error occurs.

There is also support for multi 1-wire devices on different pins.

To use this you must specify the port and pin that is used for the communication.

The 1wreset, 1wwrite and 1wread statements will work together when used with the old syntax. And the pin can be configured from the compiler options or with the CONFIG 1WIRE statement.

The syntax for additional 1-wire devices is :

1WRESET port , pin

1WWRITE var/constant ,bytes] , port, pin

var = 1WREAD( bytes) , for the configured 1 wire pin

var = 1WREAD(bytes, port, pin) ,for reading multiple bytes

See also

[1WREAD](1wread.md) , [1WWRITE](1wwrite.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wire.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wreset, 1wwrite and 1wread()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' pull-up of 4K7 required to VCC from Portb.2

' DS2401 serial button connected to Portb.2

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'when only bytes are used, use the following lib for smaller code

$lib "mcsbyte.lib"

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

Dim Ar(8) As Byte , A As Byte , I As Byte

Do

Wait 1

```
1wreset 'reset the device

Print Err 'print error 1 if error

1wwrite &H33 'read ROM command

For I = 1 To 8

Ar(i) = 1wread() 'place into array

```vb
Next

'You could also read 8 bytes a time by unremarking the next line

'and by deleting the for next above

'Ar(1) = 1wread(8) 'read 8 bytes

For I = 1 To 8

Print Hex(ar(i)); 'print output

Next

Print 'linefeed

Loop

'NOTE THAT WHEN YOU COMPILE THIS SAMPLE THE CODE WILL RUN TO THIS POINT

'THIS because of the DO LOOP that is never terminated!!!

'New is the possibility to use more than one 1 wire bus

'The following syntax must be used:

For I = 1 To 8

```
Ar(i) = 0 'clear array to see that it works

Next

1wreset Pinb , 2 'use this port and pin for the second device

1wwrite &H33 , 1 , Pinb , 2 'note that now the number of bytes must be specified!

```vb
'1wwrite Ar(1) , 5,pinb,2

'reading is also different

```
Ar(1) = 1wread(8 , Pinb , 2) 'read 8 bytes from portB on pin 2

```vb
For I = 1 To 8

Print Hex(ar(i));

Next

'you could create a loop with a variable for the bit number !

For I = 0 To 3 'for pin 0-3

```
1wreset Pinb , I

1wwrite &H33 , 1 , Pinb , I

Ar(1) = 1wread(8 , Pinb , I)

```vb
For A = 1 To 8

Print Hex(ar(a));

Next

Print

Next

End

```

---

## 1WSEARCHFIRST

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

---

## 1WSEARCHNEXT

Action

This statement reads the next ID from the 1wire bus into a variable(array).

Syntax

var2 = 1WSEARCHNEXT()

var2 = 1WSEARCHNEXT( port , pin)

Remarks

var2 | A variable or array that should be at least 8 bytes long that will be assigned with the 8 byte ID from the next 1wire device on the bus.  
---|---  
Port | The PIN port name like PINB or PIND.  
Pin | The pin number of the port. In the range from 0-7. May be a numeric constant or variable.  
  
The 1wireSearchFirst() function must be called once to initiate the ID retrieval process. After the 1wireSearchFirst() function is used you should use successive function calls to the 1wireSearchNext function to retrieve other ID's on the bus.

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

_1wire_Search_Next : (calls _1WIRE, _ADJUST_PIN , _ADJUST_BIT_ADDRESS)

Parameters passed : R24 : pin number, R30 : port , X : address of target array

Returns nothing.

See also

[1WWRITE](1wwrite.md) , [1WRESET](1wreset.md) , [1WREAD ](1wread.md), [1WSEARCHFIRST](1wsearchfirst.md), [1WIRECOUNT](1wirecount.md)

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

---

## 1WVERIFY

Action

This verifies if an ID is available on the 1wire bus.

Syntax

1WVERIFY ar(1)

1WVERIFY ar(1) , port, pin

Remarks

Ar(1) | A byte array that holds the ID to verify.  
---|---  
port | The name of the PORT PINx register like PINB or PIND.  
pin | The pin number in the range from 0-7. May be a numeric constant or variable.  
  
Returns ERR set to 0 when the ID is found on the bus otherwise it will be 1.

ASM

The following asm routines are called from mcs.lib.

_1wire_Search_Next : (calls _1WIRE, _ADJUST_PIN , _ADJUST_BIT_ADDRESS)

See also

[1WWRITE](1wwrite.md) , [1WRESET](1wreset.md) , [1WREAD ](1wread.md), [1WSEARCHFIRST](1wsearchfirst.md), [1WIRECOUNT](1wirecount.md)

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

' optional call it with pinnumber line 1wverify reg_no(1),pinb,1

'As for the other 1wire statements/functions, you can provide the port and pin number as anoption

'W = 1wirecount(pinb , 1) 'for example look at pin PINB.1

End

```

---

## 1WWRITE

Action

This statement writes a variable to the 1wire bus.

Syntax

1WWRITE var1

1WWRITE var1, bytes

1WWRITE var1 , bytes , port , pin

Remarks

var1 | Sends the value of var1 to the bus. The number of bytes can be specified too but this is optional.  
---|---  
bytes | The number of bytes to write. Must be specified when port and pin are used.  
port | The name of the PORT PINx register like PINB or PIND.  
pin | The pin number in the range from 0-7. May be a numeric constant or variable.  
  
Multiple 1-wire devices on different pins are supported.

To use this you must specify the port and pin that are used for the communication.

The 1wreset, 1wwrite and 1wread statements will work together when used with the old syntax. And the pin can be configured from the compiler options or with the [CONFIG 1WIRE](config_1wire.md) statement.

The syntax for additional 1-wire devices is :

1WRESET port , pin

1WWRITE var/constant, bytes, port , pin

var = 1WREAD(bytes, port, pin) ,for reading multiple bytes

See also

[1WREAD](1wread.md) , [1WRESET](1wreset.md)

Example

```vb
'--------------------------------------------------------------------------------

'name : 1wire.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates 1wreset, 1wwrite and 1wread()

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

' pull-up of 4K7 required to VCC from Portb.2

' DS2401 serial button connected to Portb.2

'--------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 'default use 10 for the SW stack

$framesize = 40 'default use 40 for the frame space

'when only bytes are used, use the following lib for smaller code

$lib "mcsbyte.lib"

Config 1wire = Portb.0 'use this pin

'On the STK200 jumper B.0 must be inserted

Dim Ar(8) As Byte , A As Byte , I As Byte

Do

Wait 1

```
1wreset 'reset the device

Print Err 'print error 1 if error

1wwrite &H33 'read ROM command

For I = 1 To 8

Ar(i) = 1wread() 'place into array

```vb
Next

'You could also read 8 bytes a time by unremarking the next line

'and by deleting the for next above

'Ar(1) = 1wread(8) 'read 8 bytes

For I = 1 To 8

Print Hex(ar(i)); 'print output

Next

Print 'linefeed

Loop

'NOTE THAT WHEN YOU COMPILE THIS SAMPLE THE CODE WILL RUN TO THIS POINT

'THIS because of the DO LOOP that is never terminated!!!

'New is the possibility to use more than one 1 wire bus

'The following syntax must be used:

For I = 1 To 8

```
Ar(i) = 0 'clear array to see that it works

Next

1wreset Pinb , 2 'use this port and pin for the second device

1wwrite &H33 , 1 , Pinb , 2 'note that now the number of bytes must be specified!

```vb
'1wwrite Ar(1) , 5,pinb,2

'reading is also different

```
Ar(1) = 1wread(8 , Pinb , 2) 'read 8 bytes from portB on pin 2

```vb
For I = 1 To 8

Print Hex(ar(i));

Next

'you could create a loop with a variable for the bit number !

For I = 0 To 3 'for pin 0-3

```
1wreset Pinb , I

1wwrite &H33 , 1 , Pinb , I

Ar(1) = 1wread(8 , Pinb , I)

```vb
For A = 1 To 8

Print Hex(ar(a));

Next

Print

Next

End

```

---

## M128-1wire-PortF

This user contributed library is only for the atmega128 when 1wire is used on PORTF.

Normally the port registers DDR, PORT and PIN are grouped and this is used to work with pointers.

PORTF is however incompatible since it is grouped different. This library uses fixed addresses.

\- When using this library you can not use 1wire devices on other ports. This because this lib overloads the default library.

\- The EXTENDED=1 option from [CONFIG 1WIRE](config_1wire.md) may not be used in combination with this library.

---
