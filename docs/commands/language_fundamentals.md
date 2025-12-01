# Language Fundamentals

Characters from the BASCOM character set are put together to form labels, keywords, variables and operators.

These in turn are combined to form the statements that make up a program.

This chapter describes the character set and the format of BASCOM program lines. In particular, it discusses:

•| The specific characters in the character set and the special meanings of some characters.  
---|---  
  
•| The format of a line in a BASCOM program.  
---|---  
  
•| Line labels.  
---|---  
  
•| Program line length.  
---|---  
  
Character Set

The BASCOM BASIC character set consists of alphabetic characters, numeric characters, and special characters.

The alphabetic characters in BASCOM are the uppercase letters (A-Z) and lowercase letters (a-z) of the alphabet.

The BASCOM numeric characters are the digits 0-9.

The letters A-H can be used as parts of hexadecimal numbers.

The following characters have special meanings in BASCOM statements and expressions:

Character | Name  
---|---  
ENTER | Terminates input of a line  
| Blank ( or space)  
' | Single quotation mark (apostrophe)  
* | Asterisks (multiplication symbol)  
+ | Plus sign  
, | Comma  
- | Minus sign  
. | Period (decimal point)  
/ | Slash (division symbol) will be handled as \  
: | Colon  
" | Double quotation mark  
; | Semicolon  
< | Less than  
= | Equal sign (assignment symbol or relational operator)  
> | Greater than  
\ | Backslash (integer/word division symbol)  
^ | Exponent  
  
The BASCOM program line

BASCOM program lines have the following syntax:

[[line-identifier]] [[statement]] [[:statement]] ... [[comment]]

Using Line Identifiers

BASCOM support one type of line-identifier; alphanumeric line labels:

An alphabetic line label may be any combination of from 1 to 32 letters and digits, starting with a letter and ending with a colon.

BASCOM keywords are not permitted.

The following are valid alphanumeric line labels:

Alpha:

ScreenSUB:

Test3A:

Case is not significant. The following line labels are equivalent:

alpha:

Alpha:

ALPHA:

Line labels may begin in any column, as long as they are the first characters other than blanks on the line.

Blanks are not allowed between an alphabetic label and the colon following it.

A line can have only one label. When there is a label on the line, no other identifiers may be used on the same line. So the label is the sole identifier on a line.

BASCOM Statements

A BASCOM statement is either "executable" or " non-executable".

An executable statement advances the flow of a programs logic by telling the program what to do next.

Non executable statement perform tasks such as allocating storage for variables, declaring and defining variable types.

The following BASCOM statements are examples of non-executable statements:

•| REM or (starts a comment)  
---|---  
  
•| DIM  
---|---  
  
A "comment" is a non-executable statement used to clarify a programs operation and purpose.

A comment is introduced by the REM statement or a single quote character(').

The following lines are equivalent:

```vb
PRINT " Quantity remaining" : REM Print report label.  
PRINT " Quantity remaining" ' Print report label.

```
More than one BASCOM statement can be placed on a line, but colons(:) must separate statements, as illustrated below.

FOR I = 1 TO 5 : PRINT " Gday, mate." : NEXT I

Comment

Comment is intended to clarify your code. Describe what the code is supposed to do. 

You can use single line comment using the REM statement. By default, comment is shown in green. 

Since REM is a lot of type work, you can also use the ' sign 

When you want to comment multiple lines, you can also use block comment. 

Block comment starts with '(

It ends with ')

Please notice that block comment must be the first non white space on the line. 

Rem some comment  
```vb
Print 'also comment  
'( block  
```
comment  
multiple lines  
') print "ok"  


BASCOM LineLength

If you enter your programs using the built-in editor, you are not limited to any line length, although it is advised to shorten your lines to 80 characters for clarity.

Data Types

Every variable in BASCOM has a data type that determines what can be stored in the variable. The next section summarizes the elementary data types.

Elementary Data Types

Type | Bytes used | Range | Description  
---|---|---|---  
Bit | 1/8 Byte | 0-1 | A bit can hold only the value 0 or 1. A group of 8 bits is called a byte  
Byte | 1 Byte | 0 to 255 | Bytes are stored as unsigned 8-bit binary numbers  
Integer | 2 Bytes | -32,768 to +32,767 | Integers are stored as signed sixteen-bit binary numbers  
Word | 2 Bytes | 0 to 65535 | Words are stored as unsigned sixteen-bit binary numbers  
Dword | 4 Bytes | 0 to 4294967295 | Dwords are stored as unsigned 32-bit binary numbers  
Long | 4 Bytes | -2147483648 to 2147483647 | Longs are stored as signed 32-bit binary numbers  
Single | 4 Bytes | 1.5 x 10^â45 to 3.4 x 10^38 | Singles are stored as signed 32 bit binary numbers  
Double | 8 Bytes | 5.0 x 10^â324 to 1.7 x 10^308 | Doubles are stored as signed 64 bit binary numbers  
String | up to 254 Bytes |   
| Strings are stored as bytes and are terminated with a chr(0) byte. A string dimensioned with a length of 10 bytes will occupy 11 bytes  
  
Variables can be stored internal (default) , external or in EEPROM.

Variables

A variable is a name that refers to an object--a particular number.

A numeric variable, can be assigned only a numeric value (either integer, byte, long, single or bit).

The following list shows some examples of variable assignments:

•| A constant value:  
---|---  
  
A = 5

C = 1.1

•| The value of another numeric variable:  
---|---  
  
abc = def

k = g

•| The value obtained by combining other variables, constants, and operators: Temp = a + 5  
---|---  
  
Temp = C + 5

•| The value obtained by calling a function:  
---|---  
  
Temp = Asc(S)

Constants

A constant is a placeholder for a fixed value : you can assign it with a value only once : CONST Something = 100

Constants can be assigned with a numeric or string value. To assign a string use double quotes : CONST SomeString = "BASCOM"

You can also use expressions with constants : CONST SomeThing = 1 + 2 / (3+4)

When you keep the SHIFT key pressed and hover the mouse cursor over a constant, a tooltip/hint will show the value.

When using numeric constants in [DATA](data_2.md) lines, you need to inform the compiler about the data type. This is done by ending the constant value with a suffix. See the help for DATA.

Variable Names

A BASCOM variable name may contain up to 32 characters.

The characters allowed in a variable name are letters and numbers.

The first character in a variable name must be a letter.

A variable name cannot be a reserved word, but embedded reserved words are allowed.

For example, the following statement is illegal because AND is a reserved word.

AND = 8

However, the following statement is legal:

ToAND = 8

Reserved words include all BASCOM commands, statements, function names, internal registers and operator names.

(see [BASCOM Reserved Words](reserved_words.md) , for a complete list of reserved words).

You can specify a hexadecimal or binary number with the prefix &H or &B.

a = &HA , a = &B1010 and a = 10 are all the same.

Before assigning a variable, you must tell the compiler about it with the [DIM](dim.md) statement.

Dim b1 As Bit, I as Integer, k as Byte , s As String * 10

The STRING type needs an additional parameter to specify the length.

You can also use [DEFINT](defxxx.md), [DEFBIT](defxxx.md), [DEFBYTE](defxxx.md) ,[DEFWORD](defxxx.md) ,[DEFLNG](defxxx.md) or [DEFSNG](defxxx.md).

For example,DEFINT c tells the compiler that all variables that are not dimensioned and that are beginning with the character c are of the Integer type.

BITS and Interrupts

Bits are stored in bytes. A write to a bit/boolean variable is non-atomic. Which means that multiple operations are required to update the bit value in the byte. When interrupts are used that update bits in the same byte, you can have the effect that a change becomes lost.

To prevent this you can disable interrupts and enable them after you have updated the bit variable. Or you can use a byte instead which is recommended since it would use less code. 

Expressions and Operators

This chapter discusses how to combine, modify, compare, or get information about expressions by using the operators available in BASCOM.

Anytime you do a calculation you are using expressions and operators.

This chapter describes how expressions are formed and concludes by describing the following kind of operators:

•| Arithmetic operators, used to perform calculations.  
---|---  
  
•| Relational operators, used to compare numeric or string values.  
---|---  
  
•| Logical operators, used to test conditions or manipulate individual bits.  
---|---  
  
•| Functional operators, used to supplement simple operators.  
---|---  
  
Expressions and Operators

An expression can be a numeric constant, a variable, or a single value obtained by combining constants, variables, and other expressions with operators.

Operators perform mathematical or logical operations on values.

The operators provided by BASCOM can be divided into four categories, as follows:

1\. Arithmetic

2\. Relational

3\. Logical

4\. Functional

Arithmetic

Arithmetic operators are +, - , * , \, / and ^.

•| Integer  
---|---  
  
Integer division is denoted by the backslash (\\).

Example: Z = X \ Y

•| Modulo Arithmetic  
---|---  
  
Modulo arithmetic is denoted by the modulus operator MOD.

Modulo arithmetic provides the remainder, rather than the quotient, of an integer division.

Example: X = 10 \ 4 : remainder = 10 MOD 4

•| Overflow and division by zero  
---|---  
  
Division by zero, produces an error.

At the moment no message is produced, so you have to make sure yourself that this won't happen.

Relational Operators

Relational operators are used to compare two values as shown in the table below.

The result can be used to make a decision regarding program flow.

Operator | Relation Tested | Expression   
---|---|---  
= | Equality | X = Y  
<> | Inequality | X <> Y  
< | Less than | X < Y  
> | Greater than | X > Y  
<= | Less than or equal to | X <= Y  
>= | Greater than or equal to | X >= Y  
  
Logical Operators

Logical operators perform tests on relations, bit manipulations, or Boolean operators.

There four operators in BASCOM are : 

Operator | Meaning  
---|---  
NOT | Logical complement  
AND | Conjunction  
OR | Disjunction  
XOR | Exclusive or  
  
It is possible to use logical operators to test bytes for a particular bit pattern.

For example the AND operator can be used to mask all but one of the bits of a status byte, while OR can be used to merge two bytes to create a particular binary value.

Example

A = 63 And 19  
PRINT A  
A = 10 Or 9  
PRINT A

Output

19

11

Floating point SINGLE (4 BYTE)(ASM code used is supplied by Jack Tidwell)

Single numbers conforming to the IEEE binary floating point standard.

An eight bit exponent and 24 bit mantissa are supported.

Using four bytes the format is shown below:

31 30________23 22______________________________0

s exponent mantissa

The exponent is biased by 128. Above 128 are positive exponents and below are negative. The sign bit is 0 for positive numbers and 1 for negative. The mantissa is stored in hidden bit normalized format so that 24 bits of precision can be obtained.

All mathematical operations are supported by the single.

You can also convert a single to an integer or word or vise versa:

Dim I as Integer, S as Single

S = 100.1 'assign the single

I = S 'will convert the single to an integer

Here is a fragment from the Microsoft knowledge base about FP:

Floating-point mathematics is a complex topic that confuses many programmers. The tutorial below should help you recognize programming situations where floating-point errors are likely to occur and how to avoid them. It should also allow you to recognize cases that are caused by inherent floating-point math limitations as opposed to actual compiler bugs.

Decimal and Binary Number Systems

Normally, we count things in base 10. The base is completely arbitrary. The only reason that people have traditionally used base 10 is that they have 10 fingers, which have made handy counting tools.

The number 532.25 in decimal (base 10) means the following:

(5 * 10^2) + (3 * 10^1) + (2 * 10^0) + (2 * 10^-1) + (5 * 10^-2)

500 + 30 + 2 + 2/10 + 5/100

_________

= 532.25

In the binary number system (base 2), each column represents a power of 2 instead of 10. For example, the number 101.01 means the following:

(1 * 2^2) + (0 * 2^1) + (1 * 2^0) + (0 * 2^-1) + (1 * 2^-2)

4 + 0 + 1 + 0 + 1/4

_________

= 5.25 Decimal

How Integers Are Represented in PCs

\-----------------------------------

Because there is no fractional part to an integer, its machine representation is much simpler than it is for floating-point values. Normal integers on personal computers (PCs) are 2 bytes (16 bits) long with the most significant bit indicating the sign. Long integers are 4 bytes long.

Positive values are straightforward binary numbers. For example:

1 Decimal = 1 Binary

2 Decimal = 10 Binary

22 Decimal = 10110 Binary, etc.

However, negative integers are represented using the two's complement scheme. To get the two's complement representation for a negative number, take the binary representation for the number's absolute value and then flip all the bits and add 1. For example:

4 Decimal = 0000 0000 0000 0100

1111 1111 1111 1011 Flip the Bits

-4 = 1111 1111 1111 1100 Add 1

Note that adding any combination of two's complement numbers together

using ordinary binary arithmetic produces the correct result.

Floating-Point Complications

Every decimal integer can be exactly represented by a binary integer; however, this is not true for fractional numbers. In fact, every number that is irrational in base 10 will also be irrational in any system with a base smaller than 10.

For binary, in particular, only fractional numbers that can be represented in the form p/q, where q is an integer power of 2, can be expressed exactly, with a finite number of bits.

Even common decimal fractions, such as decimal 0.0001, cannot be represented exactly in binary. (0.0001 is a repeating binary fraction with a period of 104 bits!)

This explains why a simple example, such as the following

SUM = 0  
FOR I% = 1 TO 10000  
SUM = SUM + 0.0001  
```vb
NEXT I%  
PRINT SUM ' Theoretically = 1.0.

```
will PRINT 1.000054 as output. The small error in representing 0.0001

in binary propagates to the sum.

For the same reason, you should always be very cautious when making comparisons on real numbers. The following example illustrates a common programming error:

item1# = 69.82#

item2# = 69.20# + 0.62#

IF item1# = item2# then print "Equality!"

This will NOT PRINT "Equality!" because 69.82 cannot be represented exactly in binary, which causes the value that results from the assignment to be SLIGHTLY different (in binary) than the value that is generated from the expression. In practice, you should always code such comparisons in such a way as to allow for some tolerance.

General Floating-Point Concepts

It is very important to realize that any binary floating-point system can represent only a finite number of floating-point values in exact form. All other values must be approximated by the closest represent able value. The IEEE standard specifies the method for rounding values to the "closest" represent able value. BASCOM supports the standard and rounds according to the IEEE rules.

Also, keep in mind that the numbers that can be represented in IEEE are spread out over a very wide range. You can imagine them on a number line. There is a high density of represent able numbers near 1.0 and -1.0 but fewer and fewer as you go towards 0 or infinity.

The goal of the IEEE standard, which is designed for engineering calculations, is to maximize accuracy (to get as close as possible to the actual number). Precision refers to the number of digits that you can represent. The IEEE standard attempts to balance the number of bits dedicated to the exponent with the number of bits used for the fractional part of the number, to keep both accuracy and precision within acceptable limits.

IEEE Details

Floating-point numbers are represented in the following form, where

[exponent] is the binary exponent:

X = Fraction * 2^(exponent - bias)

[Fraction] is the normalized fractional part of the number, normalized because the exponent is adjusted so that the leading bit is always a 1. This way, it does not have to be stored, and you get one more bit of precision. This is why there is an implied bit. You can think of this like scientific notation, where you manipulate the exponent to have one digit to the left of the decimal point, except in binary, you can always manipulate the exponent so that the first bit is a 1, since there are only 1s and 0s.

[bias] is the bias value used to avoid having to store negative exponents.

The bias for single-precision numbers is 127 and 1023 (decimal) for double-precision numbers.

The values equal to all 0's and all 1's (binary) are reserved for representing special cases. There are other special cases as well, that indicate various error conditions.

Single-Precision Examples

2 = 1 * 2^1 = 0100 0000 0000 0000 ... 0000 0000 = 4000 0000 hex

Note the sign bit is zero, and the stored exponent is 128, or

100 0000 0 in binary, which is 127 plus 1. The stored mantissa is (1.)

000 0000 ... 0000 0000, which has an implied leading 1 and binary point, so the actual mantissa is 1.

-2 = -1 * 2^1 = 1100 0000 0000 0000 ... 0000 0000 = C000 0000 hex

Same as +2 except that the sign bit is set. This is true for all IEEE format floating-point numbers.

4 = 1 * 2^2 = 0100 0000 1000 0000 ... 0000 0000 = 4080 0000 hex

Same mantissa, exponent increases by one (biased value is 129, or 100 0000 1 in binary.

6 = 1.5 * 2^2 = 0100 0000 1100 0000 ... 0000 0000 = 40C0 0000 hex

Same exponent, mantissa is larger by half -- it's

(1.) 100 0000 ... 0000 0000, which, since this is a binary fraction, is 1-1/2 (the values of the fractional digits are 1/2, 1/4, 1/8, etc.).

1 = 1 * 2^0 = 0011 1111 1000 0000 ... 0000 0000 = 3F80 0000 hex

Same exponent as other powers of 2, mantissa is one less than 2 at 127, or 011 1111 1 in binary.

.75 = 1.5 * 2^-1 = 0011 1111 0100 0000 ... 0000 0000 = 3F40 0000 hex

The biased exponent is 126, 011 1111 0 in binary, and the mantissa is (1.) 100 0000 ... 0000 0000, which is 1-1/2.

2.5 = 1.25 * 2^1 = 0100 0000 0010 0000 ... 0000 0000 = 4020 0000 hex

Exactly the same as 2 except that the bit which represents 1/4 is set in the mantissa.

0.1 = 1.6 * 2^-4 = 0011 1101 1100 1100 ... 1100 1101 = 3DCC CCCD hex

1/10 is a repeating fraction in binary. The mantissa is just shy of 1.6, and the biased exponent says that 1.6 is to be divided by 16 (it is 011 1101 1 in binary, which is 123 n decimal). The true exponent is 123 - 127 = -4, which means that the factor by which to multiply is 2**-4 = 1/16. Note that the stored mantissa is rounded up in the last bit. This is an attempt to represent the un-representable number as accurately as possible. (The reason that 1/10 and 1/100 are not exactly representable in binary is similar to the way that 1/3 is not exactly representable in decimal.)

0 = 1.0 * 2^-128 = all zeros -- a special case.

Other Common Floating-Point Errors

The following are common floating-point errors:

1\. Round-off error

This error results when all of the bits in a binary number cannot be used in a calculation.

Example: Adding 0.0001 to 0.9900 (Single Precision)

Decimal 0.0001 will be represented as:

(1.)10100011011011100010111 * 2^(-14+Bias) (13 Leading 0s in Binary!)

0.9900 will be represented as:

(1.)11111010111000010100011 * 2^(-1+Bias)

Now to actually add these numbers, the decimal (binary) points must be aligned. For this they must be Unnormalized. Here is the resulting addition:

.000000000000011010001101 * 2^0 <\- Only 11 of 23 Bits retained

+.111111010111000010100011 * 2^0

________________________________

.111111010111011100110000 * 2^0

This is called a round-off error because some computers round when shifting for addition. Others simply truncate. Round-off errors are important to consider whenever you are adding or multiplying two very different values.

2\. Subtracting two almost equal values

.1235

-.1234

_____

.0001

This will be normalized. Note that although the original numbers each had four significant digits, the result has only one significant digit.

3\. Overflow and underflow

This occurs when the result is too large or too small to be represented by the data type.

4\. Quantizing error

This occurs with those numbers that cannot be represented in exact form by the floating-point standard.

Rounding

When a Long is assigned to a single, the number is rounded according to the rules of the IEEE committee.

For explanation: 1.500000 is exact the middle between 1.00000 and 2.000000. If x.500000 is always rounded up, than there is trend for higher values than the average of all numbers. So their rule says, half time to round up and half time to round down, if value behind LSB is exact ..500000000.

The rule is, round this .500000000000 to next even number, that means if LSB is 1 (half time) to round up, so the LSB is going to 0 (=even), if LSB is 0 (other half time) to round down, that means no rounding.

This rounding method is best since the absolute error is 0.

You can override the default IEEE rounding method by specifying the $LIB LONG2FLOAT.LBX library which rounds up to the next number. This is the method used up to 1.11.7.4 of the compiler.

Double

The double is essential the same as a single. Except the double consist of 8 bytes instead of 4. The exponent is 11 bits leaving 52 bits for the mantissa.

Arrays

An array is a set of sequentially indexed elements having the same type. Each element of an array has a unique index number that identifies it. Changes made to an element of an array do not affect the other elements.

The index must be a numeric constant, a byte, an integer, word or long.

The maximum number of elements is 65535. For Xmega with huge memory it is 8MB!

The first element of an array is always one by default. This means that elements are 1-based.

You can change this with CONFIG BASE=0. In this case, the first element will be element 0.

Arrays can be used on each place where a 'normal' variable is expected.

You can add an offset to the index too. This could be used to emulate a 2 dimensional array.

row_index = row : shift row_index, left,4

value = parameter_array(column+row_index)

Example:

```vb
'create an array named a, with 10 elements (1 to 10)  
Dim A(10) As Byte  
'create an integer  
Dim C As Integer  
'now fill the array  
For C = 1 To 10  
'assign array element  
```
A(c)= C  
```vb
' print it  
Print A(c)  
Next  
'you can add an offset to the index too  
```
C = 0  
A(c + 1)= 100  
```vb
Print A(c + 1)  
End

```
Strings

A string is used to store text. A string must be dimensioned with the length specified.

DIM S as STRING * 5

Will create a string that can store a text with a maximum length of 5 bytes.

The space used is 6 bytes because a string is terminated with a null byte.

To assign the string:

Ds = "abcd"

To insert special characters into the string :

s= "AB{027}cd"

The {ascii} will insert the ASCII value into the string.

The number of digits must be 3. 

s = "{27}" will assign "{27}" to the string instead of escape character 27!

Because the null byte (ASCII 0) is used to terminate a string, you can not embed a null byte into a string.

Casting

In BASCOM-AVR when you perform operations on variables they all must be of the same data type.

long = long1 * long2 ' for example

The assigned variables data type determines what kind of math is performed.

```vb
For example when you assign a long, long math will be used.

If you try to store the result of a LONG into a byte, only the LSB of the LONG will be stored into the BYTE.

```
Byte = LONG

When LONG = 256 , it will not fit into a BYTE. The result will be 256 AND 255 = 0.

Of course you are free to use different data types. The correct result is only guaranteed when you are using data types of the same kind or that result always can fit into the target data type.

When you use strings, the same rules apply. But there is one exception:

Dim b as Byte  
  
b = 123 ' ok this is normal  
b = "A" ' b = 65

When the target is a byte and the source variable is a string constant denoted by "", the ASCII value will be stored in the byte. This works also for tests :

```vb
IF b = "A" then ' when b = 65  
  
END IF

```
This is different compared to QB/VB where you can not assign a string to a byte variable.

SINGLE CONVERSION

When you want to convert a SINGLE into a byte, word, integer or long the compiler will automatic convert the values when the source string is of the SINGLE data type.

integer = single

You can also convert a byte, word, integer or long into a SINGLE by assigning this variable to a SINGLE.

single = long