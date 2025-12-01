# CHECKFLOAT

Action

This function validates the value of a floating point variable.

Syntax

targ = CHECKFLOAT(var [,option])

Remarks

targ | A numeric variable that will be assigned with the result of the validation.  The following bits can be set: cBitInfinity = 0 cmBitInfinity = 1 ;(2 ^ cBitInfinity) cBitZero = 1 cmBitZero = 2 ;(2 ^ cBitZero) cBitNAN = 2 cmBitNAN = 4 ;(2 ^ cBitNAN) cBitSign = 7 cmBitSign = 128 ;(2 ^ cBitSign) The byte values are shown in italic. The bit constants are defined in the single and double libraries.  
---|---  
var | A floating point variable such as a single or double to validate.  
option | This is an optional numeric constant that servers as a mask. This allows to test for makes it possible to test for a single error.  
  
A floating point value may contain an illegal value as the result of a calculation. These illegal values are NAN (not a number) and INFINITY.

The two other tests which are performed are a test for zero, and a sign test. 

```vb
If the result bit 0 is '1' then the number is infinity.

If the result bit 1 is '1' then the number is zero.

If the result bit 2 is '1' then the number if NAN.

If the result bit 7 is '1' then the number is negative. 

If you want to test only for NAN and INFINITY you can add the bits and pass this as the optional numeric mask. For NAN and INFINITY this would be 1+4=5

```
The resulting value will be AND-ed and if any of the two bits is set, the result will be non-zero, indicating an error. If both values are 0, the result will be zero.

![notice](notice.jpg)This functions works for both the double and single data types. For the single there is however a note. When you divide a number by a real 0, the result is a zero (0).

In the double data type you actually get an INFinite number. For this reason the sample contains a trick with overlayed variables to test the function.

See also

NONE

Example

```vb
$regfile = "m2561def.dat"  
$crystal = 8000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
$baud = 19200  
  
  
$lib "single.lbx"  
  
Dim S1 As Single , S2 As Single , S3 As Single  
dim d1 as Double , d2 as Double , d3 as Double  
dim bCheck as Byte  
dim bs(4) as Byte at s3 overlay  
dim bd(8) as Byte at d3 overlay  
  
  
```
S1 = 0 : Bcheck = Checkfloat(s1) : Print Bin(bcheck)  
  
S1 = 0 : Bcheck = Checkfloat(s1 , 2) : Print Bin(bcheck)  
  
  
  
d1 = 1: d2 = 0 : d3 = d1 / d2 ' 1/0 should result in infinty  
Bcheck = Checkfloat(d3) : Print Bin(bcheck)  
Bcheck = Checkfloat(d3 , 5) : Print Bcheck ' test for infinity and nan  
  
d1 = -1  
d3 = sqr(d1) ' should produce NAN  
Bcheck = Checkfloat(d3) : Print Bin(bcheck)  
  
' single routines must be checked for returning IEEE-Rulues according values  
s1 = 1: s2 = 0 : s3 = s1 / s2 ' 1/0 should result in infinty  
Bcheck = Checkfloat(s3) : Print Bin(bcheck)  
  
s1 = -1  
s3 = sqr(s1) ' should produce NAN  
Bcheck = Checkfloat(s3) : Print Bin(bcheck)  
  
  
' now check with hard-coded values for singles  
bs(1) = &HFF: bs(2) = &HFF: bs(3) = &HFF: bs(4) = &H7F ' NAN  
Bcheck = Checkfloat(s3) : Print Bin(bcheck)  
  
bs(1) = &H00: bs(2) = &H00: bs(3) = &H80: bs(4) = &H7F ' infinity  
Bcheck = Checkfloat(s3) : Print Bin(bcheck)  
  
End