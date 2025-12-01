# STR

Action

Returns a string representation of a number.

Syntax

var = STR( x [,digits])

Remarks

var | A string variable.  
---|---  
X | A numeric variable.  
digits | An options parameter, only allowed for singles and doubles. It specifies how many digits after the comma/point are used. When using with a single, you need to use : [CONFIG SINGLE=SCIENTIFIC](configsingle.md)  
  
![notice](notice.jpg)The string must be big enough to store the result. So if you have a string like this : Dim S as string * 4, and you use it on a single with the value 0.00000001 then there is not enough space in the string to hold the result. Strings that are assigned with Str() should be dimmed 16 characters long.

You do not need to convert a variable into a string before you print it.

When you use PRINT var, then you will get the same result as when you convert the numeric variable into a string, and print that string.

The PRINT routine will convert the numeric variable into a string before it gets printed to the serial port.

As the integer conversion routines can convert byte, integer, word and longs into a string it also means some code overhead when you do not use longs. You can include the alternative library named [mcsbyte](mcsbyte.md).lbx then. This library can only print bytes. There is also a library for printing integers and words only. This library is named [mcsbyteint](mcsbyteint.md).

When you use these libs to print a long you will get an error message.

See also

[VAL](val.md) , [HEX](hex.md) , [HEXVAL](hexval.md) , [MCSBYTE](mcsbyte.md) , [BIN](bin.md) , [STR2DIGITS](str2digits.md) , [FUSING](fusing.md)

Difference with VB

In VB STR() returns a string with a leading space. BASCOM does not return a leading space.

Example

Dim A As Byte , S As String * 10

A = 123

S = Str(a)

```vb
Print S ' 123

'when you use print a, you will get the same result.

'but a string can also be manipulated with the string routines.

End

```