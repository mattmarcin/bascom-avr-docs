# DIM

Action

Dimension a variable.

Syntax

DIM var[,varn] AS [XRAM/SRAM/ERAM]type [AT location/variable] [OVERLAY] [SAFE]

Remarks

Var | Any valid variable name such as b1, i or longname. var may also be an array : ar(10) for example. You can also use a list and created a number of variables of the same data type : DIM A1,A2, BVAR AS BYTE. This will create 3 BYTE variables. When using a list, you may not use identifiers such as #%!&. You may also not use the optional OVERLAY.  It is also possible to define the data type by ending the variable name with an identifier : % for Integer & for Long # for Double ! for Single Dim A!, b# would create a variable A! of the SINGLE data type and a variable B# with the DOUBLE data type When a variable is dimensioned with an identifier, the variable must be referenced with that identifier as well. We encourage the use of Hungarian Notation where you use a prefix instead : Dim bVar As Byte ' the b indicates a BYTE Dim iMyInt As Integer 'the i indicates an INTEGER common used prefixes : b - BYTE w - WORD dw - DWORD i - INTEGER l - LONG s - STRING dbl - DOUBLE sng - SINGLE The IDE can show the data type of the variable when you hover the mouse above the variable name and keep the SHIFT key pressed.  
---|---  
Type | Bit/Boolean, Byte, Word, Integer, Long, Dword, Single, Double, String or Type.  
XRAM | Specify XRAM to store variable into external memory  
SRAM | Specify SRAM to store variable into internal memory (default)  
ERAM | Specify ERAM to store the variable into EEPROM  
OVERLAY | Specify that the variable is overlaid in memory.  
location | The address or name of the variable when OVERLAY is used.  
SAFE | An optional specifier to indicate that access to this variable must be done in a safe way. See the full explanation below.  
  
A string variable needs an additional length parameter:

Dim s As XRAM String * 10

In this case, the string can have a maximum length of 10 characters. Internally one additional byte is needed to store the end of string marker. Thus in the example above, 11 bytes will be used to store the string.

BITS

Note that BITS can only be stored in internal memory.

You may also specify IRAM. IRAM is the place in memory where the registers are located : absolute address 0 - 31. BASCOM uses most of these addresses, depending on the instructions/options you use. For a [$TINY](_tiny.md) chip it makes sense to use IRAM since there is NO SRAM in most tiny AVR chips (TINY15 for example). You may also use to IRAM to overlay registers in memory.

See also [Memory usage](memory_usage.md)

Multiple variables on one line

You may Dimension multiple variables using one DIM statement when you separate them by a comma. There are 2 ways to do so :

Dim A As Byte, B As Byte, C As Word

The second method is even simpler :

Dim A, B, C As Byte

Here all variables are bytes. They are only separated by a comma. In the sample above, C is a word, so the equivalent would need :

Dim A, B As Byte, C As Word

Depending on which method you use, the variables might end up at a different memory location. When not using AT, you should not depend on the memory location of a variable.

Variables are usually stored in the same memory order as they are dimensioned. But you should not depend on it. Some optimization techniques requite that some variables are stored in a certain order. Use [VARPTR](varptr.md) to get the address of a variable in memory.

The Data/TIme routines require that sec,min and hour variables are in a specific order. For those you need to be explicit using AT :

Dim b as byte , m as byte at b + 1 , h as byte at m + 1

This will ensure that the bytes are placed in the specified order. 

SCOPE

The scope for DIM is global. So no matter where you use the DIM statements, the variable will end up as a global visible variable that is visible in all modules, procedures and functions.

When you need a LOCAL variable that is local to the procedure or function, you can use [LOCAL](local.md).

Since LOCAL variables are stored on the frame, it takes more code to dynamic generate and clean up these variables. This because all functions and subs are fully re-entrant. (re-entrant means they can call themselves recursively)

AT

The optional AT parameter lets you specify where in memory the variable must be stored. When the memory location already is occupied, the first free memory location will be used. You need to look in the report file to see where the variable is located in memory. In general it is a bad idea to use fixed locations. The SRAM starts at different locations in various processors. Some use &H60, &H100, or &H2000 for Xmega. When you have hard coded that a variable will start at &H60, and you port your code to an XMEGA this location is not usable. 

OVERLAY

The OVERLAY option will not use any variable space. It will create a sort of phantom variable.

```vb
Dim x as Long at &H60 'long uses 60,61,62 and 63 hex of SRAM  
  
Dim B1 As Byte At &H60 Overlay 'overlay at the same address at &H60  
Dim B2 As Byte At &H61 Overlay  


```
B1 and B2 are no real variables! They refer to a place in memory. In this case to &H60 and &H61. By assigning the phantom variable B1, you will write to memory location &H60 that is used by variable X.

So to define it better, OVERLAY does create a normal usable variable, but it will be stored at the specified memory location which could be already be occupied by another OVERLAY variable, or by a normal variable.

You can not overlay BIT/Boolean variables. These are global variables stored in bytes which can not be overlayed. You can however use an ALIAS : Mybit ALIAS SomeByte.0

![notice](notice.jpg)Take care with the OVERLAY option. Use it only when you understand it. Refer to a variable if possible, not to an absolute address.

You can also read the content of B1: 

Print B1

This will print the content of memory location &H60.

By using a phantom variable you can manipulate the individual bytes of real variables.

Overlay example 2

```vb
Dim L as Long at &H60  
Dim W as Word at &H62 OVERLAY

```
W will now point to the upper two bytes of the long.

Overlay example 3

Following you find the Bascom-AVR Simulator Memory status when you run the following example in Bascom-AVR Simulator. This example is intended to be used with the simulator. You need to uncomment the $sim when you want to test it on an real AVR.

![notice](notice.jpg)Strings need an additional byte (Null termination). So you need an overlay of 8 bytes when you overlay a string with 7 bytes.

![overlay_example_1](overlay_example_1.jpg)

  
  
```vb
$regfile = "m644pdef.dat"  
$crystal = 4000000  
$hwstack = 60  
$swstack = 60  
$framesize = 60 'frame space can grow rapid when using it on variables with a big size (strings)  
$baud = 9600  
$sim '$sim to use this example in Bascom-AVR simulator  
  
  
Print "-------------------------"  
  
Dim Array(5) As Byte  
Dim My_string As String * 4 At Array Overlay  
Dim K As Byte  
  
```
K = 1  
  
My_string = "Test"  
  
```vb
' ---> 4 ASCII but 5 Bytes because of 0 Termination of String which is another byte  
' This is how it will be stored in SRAM  
' Array(1) Array(2) Array(3) Array(4) Array(5)  
' +--------+--------+--------+--------+--------+  
' | T | e | s | t | 00 |  
' +--------+--------+--------+--------+--------+  
  
Print Chr(array(1))  
Print Chr(array(2))  
  
Print "-------------------------"  
  
Dim Teststring As String * 5  
Dim Ar(6) As Byte At Teststring Overlay  
Dim J As Byte  
```
J = &H03  
  
Ar(5) = 47  
  
Teststring = "Hello"  
  
```vb
' ---> 5 ASCII but 6 Bytes because of 0 Termination of String  
' This is how it will be stored in SRAM  
' Ar(1) Ar(2) Ar(3) Ar(4) Ar(5) Ar(6)  
' +--------+--------+--------+--------+--------+--------+  
' | H | e | l | l | o | 00 |  
' +--------+--------+--------+--------+--------+--------+  
  
For K = 1 To 5  
Print Chr(ar(k)) ;  
Next  
Print  
  
```
K = 1  
  
```vb
Print "-------------------------"  
  
Dim My_word As Word  
Dim Low_byte As Byte At My_word Overlay  
Dim High_byte As Byte At My_word + 1 Overlay  
  
```
Low_byte = &B0000_1111  
High_byte = &B1111_0000  
  
```vb
' This is how it will be stored in SRAM  
' <\-------my_word-------->  
' +-----------+----------+  
' | Low_byte |High_byte |  
' +-----------+----------+  
  
'But when you print it with print bin(Variable) you will see it as  
  
' <\-------my_word-------->  
' 11110000 00001111  
' +-----------+----------+  
' | High_byte |Low_byte |  
' +-----------+----------+  
  
Print "My_word = " ; Bin(my_word)  
  
Print "-------------------------"  
  
Dim My_long_1 As Long  
Dim Byte_1 As Byte At My_long_1 Overlay  
Dim Byte_2 As Byte At My_long_1 + 1 Overlay  
Dim Byte_3 As Byte At My_long_1 + 2 Overlay  
Dim Byte_4 As Byte At My_long_1 + 3 Overlay  
  
```
Byte_1 = 1  
Byte_2 = 2  
Byte_3 = 3  
Byte_4 = 4  
  
```vb
Print Bin(my_long_1)  
  
' This is how it will be stored in SRAM  
' <\-------my_long_1------------>  
' +-------+------+------+------+  
' | Byte_1|Byte_2|Byte_3|Byte_4|  
' +-------+------+------+------+  
  
'But when you print it with print bin(Variable) you will see it as  
  
' <\-------my_long_1------------>  
' +-------+------+------+------+  
' | Byte_4|Byte_3|Byte_2|Byte_1|  
' +-------+------+------+------+  
  
Print "-------------------------"  
  
Dim My_dword As Dword At $140 ' This places the my_long_2 variable at a fixed SRAM address starting at HEX 140  
Dim Byte__1 As Byte At $140 Overlay ' NOTICE: because this will be stored at the specified memory location  
Dim Byte__2 As Byte At $141 Overlay ' which could be already be occupied by another OVERLAY variable, or by a normal variable the  
Dim Byte__3 As Byte At $142 Overlay ' compiler generate an ERROR "Address already occupied" in this case.  
Dim Byte__4 As Byte At $143 Overlay  
  
  
```
Byte__1 = 1  
Byte__2 = 2  
Byte__3 = 3  
Byte__4 = 4  
  
```vb
'This is how it will be stored in SRAM  
' <\----------my_dword---------->  
' +-------+------+------+------+  
' | Byte_1|Byte_2|Byte_3|Byte_4|  
' +-------+------+------+------+  
  
'But when you print it with print bin(Variable) you will see it as  
' <\----------my_dword---------->  
' +-------+------+------+------+  
' | Byte_4|Byte_3|Byte_2|Byte_1|  
' +-------+------+------+------+  
  
Print "my_dword = " ; Bin(my_dword)  
  
Print "-------------------------"  
  
Dim My_dword_2 As Dword  
Dim My_word_2 As Word At My_dword_2 Overlay  
Dim My_byte3 As Byte At My_dword_2 + 2 Overlay  
Dim My_byte4 As Byte At My_dword_2 + 3 Overlay  
  
```
My_word_2 = &B11111111_00000000  
My_byte3 = &B00000011  
My_byte4 = &B10000000  
  
```vb
'This is how it will be stored in SRAM  
' <\--------------my_dword_2------------>  
' +---------+--------+--------+--------+  
' | my_word_2 |my_byte3|my_byte4|  
' +---------+--------+--------+--------+  
  
'But when you print it with print bin(Variable) you will see it as  
' <\--------------my_dword_2------------>  
' +---------+--------+--------+--------+  
' | my_byte4|my_byte3| my_word_2 |  
' +---------+--------+--------+--------+  
  
Print Bin(my_dword_2)  
  
Print "-------------------------"  
  
' Now we examine the Null terminator in Strings  
  
Dim My_date(11) As Byte ' 8 strings + 3 Null terminator = 11 Byte  
Dim Day As String * 2 At My_date(1) Overlay  
Dim Null_terminator As Byte At My_date(1) + 2 Overlay ' Null terminator  
Dim Month As String * 2 At My_date(1) + 3 Overlay  
Dim Null_terminator_2 As Byte At My_date(1) + 5 Overlay ' Null terminator  
Dim Year As String * 4 At My_date(1) + 6 Overlay  
Dim Null_terminator_3 As Byte At My_date(1) + 10 Overlay ' Null terminator  
  
```
Day = "16"  
Month = "11"  
Year = "2011"  
  
```vb
Print "Day= " ; Day  
Print "Month= " ; Month  
Print "Year= " ; Year  
  
'For example the print function use the Null Terminator to check the end of the string  
'When we set now the Null_terminator to "/" (forward slash) instead of 0 then the print function print until a Null terminator is recognised  
```
Null_terminator = 47 ' 47 = "/" (forward slash  
  
```vb
Print Day ' This will now print "16/11" because the first Null terminator will be found after the "11"  
  
  
  
End ' end program

```
Using variable name instead of address

As variables can be moved though the program during development it is not always convenient to specify an address. You can also use the name of the variable :

```vb
DIM W as WORD

Dim B as BYTE AT W OVERLAY

```
Now B is located at the same address as variable W.

For XRAM variables, you need [additional hardware ](adding_xram.md): an external RAM and address decoder chip.

ERAM

For ERAM variables, it is important to understand that these are not normal variables. ERAM variables serve as a way to simple read and write the EEPROM memory. You can use READEEPROM and WRITEEEPROM for that purpose too.

To write to an ERAM variable you have to use an SRAM variable as the source : eramVAR= sramVAR

To read from an ERAM variable you have to use an SRAM variable as the targer : sramVAR=eramVAR

Both variables need to be of the same data type. So when writing to an ERAM double, the source variable need to be of the double type too.

ERAM can be assigned with a numeric value too : eramVAR= 123

You can not use an ERAM variable as you would use a normal variable.

Also keep in mind that when you write to ERAM, you write to EEPROM, and that after 100.000 times, the EEPROM will not erase properly. 

Dim b as byte, bx as ERAM byte

B = 1

Bx = b ' write to EEPROM

B = bx ' read from EEPROM

Updateeprom

When you define a constant named Updateeprom in your code, the EEPROM will only be updated when the value differs. In order to do so, the EEPROM is read before the new value is written. This will take some extra time/code. The constant only need to be defined, the value itself is not important. Like : CONST Updateeprom=1

Xmega

The XMEGA need an additional configuration command : [CONFIG EEPROM](config_eeprom.md) = MAPPED, in order to use ERAM. Or use the QUICK option.

Arrays

An array is a sequential collection of elements with the same data type. Till version 2077, arrays could have only 1 index or dimension. But in 2078 this has been changed and while there are no technical limits for unlimited indexes, the limit has been set to 5. This means that you can create a variable array like : Dim ar(5,10,5) As Byte

This will create a BYTE variable named AR, and it has 3 indexes. Each index requires space, in this sample the amount of bytes required would be : 5 * 10 * 5 = 250 * lengthOfByte = 250 bytes.

```vb
For a WORD, which uses 2 bytes, the required space would have been 250 * 2 = 500 bytes.

While using multiple indexes might be a nice feature, it comes with a penalty : the processor need to calculate the address in memory based on the indexes. The more indexes you add, the more calculations/code is required.

```
When you use a single index, the old calculation method is used. When using multiple indexes, a new method is used which calls array calculator code in mcs.lib.

As mentioned, the maximum number of indexes is 5 so : Dim ar(5,5,5,10,10) As Byte would work. 

Multiple indexes is a new feature in 2078. The simulator does not support this option yet, so for the simulator, only 1 array exists. 

Lets see how memory is organized when using multiple indexes. For the sample we use an array of 5x3 bytes.

Dim ar(5,3) as byte. 

This gives us the following possible index values :

1,1 1,2 1,3

2,1 2,2 2,3

3,1 3,2 3,3

4,1 4,2 4,3

5,1 5,2 5,3

Since the memory of the processor is linear, we have 15 cells.

Address | Cell  
---|---  
n | 1,1  
n+1 | 1,2  
n+2 | 1,3  
n+3 | 1,4  
n+4 | 1,5  
n+5 | 2,1  
n+6 | 2,2  
n+7 | 2,3  
n+8 | 2,4  
n+9 | 2,5  
n+10 | 3,1  
n+11 | 3,2  
n+12 | 3,3  
n+13 | 3,4  
n+14 | 3,5  
  
Arrays start with element 1 by default. Thus DIM ar(5) will create 5 elements and the first element is ar(1). 

Some times it is more convenient to start with element 0. For this you can use the CONFIG BASE=0 option.

When [CONFIG BASE](config_base.md) is set to 0, and not the default 1, the first element will be 0 : DIM ar(5), will make ar(0) the first element, and ar(4) the last element.

![notice](notice.jpg)Multi DIM arrays are not supported for bootloaders with an address > 64KB. This means that for an Mega128 bootloader it will not work. The reason is that the compiler places a type/index table in the first segment for faster calculation. 

Size

The maximum size of an array depends on the available memory and the data type. The XMEGA supports up to 8 MB of external memory. BASCOM supports this but the implementation is still considered BETA. It should not be used for production. The only thing you need to do to activate the big memory is to specify the size with $XRAMSIZE.

For example : $XRAMSIZE=8000000 will tell the compiler that you use 8 MB of external memory.

Additional registers must be set to pass the 24 bit address. This will create more code. 

There is only one restriction : you can/may not pass variables located in the external memory to a sub or function.

The compiler will always pass a word address and does not support to pass the additional byte.

SAFE

The optional SAFE attribute can be used to specify that access to a variable must be done in a safe way. So when would it be unsafe?

Imagine that you DIM a BYTE and access this byte in your main code but also inside an interrupt service routine (ISR).

A typical piece of code would be for the main code :

1 - LDS r24, address of BYTE load into register R24 the value of the byte 

2 - Inc R24 increase the value of the register R24

3 - STS address, R24 write the updated value of the register back to the byte

The ISR will save the register R24. So that will not cause a problem. 

Imagine that the ISR must read the value of the byte, depending on the step in main, it will load a different value.

When interrupted at step 1, the ISR will load the same value

When interrupted at step 2, the ISR will load the increased value

When interrupted at step 3, the ISR will also load the new increased value

The case above will probably not cause much problems to your code.

Now what if the ISR will alter the value? It could write for example a zero to the byte. 

The ISR will have similar code like the main code :

1 - LDS r24, address of BYTE load into register R24 the value of the byte 

2 - CLR R24 clear the value of the register R24

3 - STS address, R24 write the updated value of the register back to the byte

Now depending on the step in the main code, the following will happen :

When interrupted at step 1, the register is loaded , the ISR clears the variable to 0, but since R24 was saved and restored it holds the previous value. It then will continue to be increased and saved. The other steps will have a similar outcome. 

This is normal since you interrupted a process. 

It is like printing to the serial port "Hello world" and an ISR will print a *. This star will appear in the other data.

Beside writing at the same time to the same variable, there is another problem with variables that have a longer data length than 1 byte.

Lets say you work on a WORD that is 2 bytes and has a value of &H1234

The code :

1- LDS R24, address of LSB

2- LDS R25, address of MSB

3- add some value to R24 like 1

4- add some value to R25 like 1

5- STS address of LSB, R24

6- STS address of MSB, R25

The normal outcome would be &H1335 since both registers were increased by 1.

When this code is interrupted between step 5 and 6, and the WORD variable is read, it will not have the right value. This because one of the registers is not written yet. When you read a BYTE, it will always have the value that you have written to it. (either in the main or ISR).

But in this sample you would read &H1235 because the MSB register R25 is not written to memory yet.

BITS

Bits are stored in bytes. This can cause the same problems when you manipulate bits that have the same byte address.

So what do we do to prevent problems? The normal solution is to disable interrupts in your code and re-enable them when you write to variables that are also access inside the ISR : 

DISABLE INTERRUPTS

SomeWord = 0

ENABLE INTERRUPTS

Now the ISR can not interrupt the updating of the variable. So it can not read the wrong value.

The SAFE option will disable interrupts and enables them, whenever you write or read a safe variable. 

Please notice that this will not be done inside an ISR since when an ISR is executed, the global interrupts are disabled by default at the hardware level.

And also notice that when interrupts were not enabled yet, they will be as soon you access a variable with the SAFE flag !

From version 2086 off, at the cost of some extra code, the I flag is saved and restored.

Using the SAFE flag on a BIT will make ALL the bits of the byte of that group SAFE as well. 

```vb
For example :

Dim b1 as BIT SAFE , b2 as BIT

```
Now b1 and b2 will be placed inside the same byte. And since b1 is marked with SAFE, b2 will be safe too since it shares the same memory location.

You can not use the SAFE attribute on an OVERLAY variable. 

TYPES

A type is a container for a number of normal data types. See also [TYPE](type.md).

Almost all rules apply to types. Dim rec as klm 'where klm is a defined TYPE

See Also

[CONST](const.md) , [LOCAL](local.md), [Memory usage](memory_usage.md) , [CONFIG BASE](config_base.md) , [TYPE](type.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : dim.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo: DIM

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

Dim B1 As Bit 'bit can be 0 or 1

Dim A As Byte 'byte range from 0-255

Dim C As Integer 'integer range from -32767 - +32768

Dim L As Long

Dim W As Word

Dim S As String * 11 'length can be up to 11 characters

'new feature : you can specify the address of the variable

Dim K As Integer At &H120

'the next dimensioned variable will be placed after variable s

Dim Kk As Integer

'Assign bits

```
B1 = 1 'or

```vb
Set B1 'use set

'Assign bytes

```
A = 12

A = A + 1

'Assign integer

C = -12

C = C + 100

Print C

W = 50000

```vb
Print W

'Assign long

```
L = 12345678

```vb
Print L

'Assign string

```
S = "Hello world"

```vb
Print S

End

```