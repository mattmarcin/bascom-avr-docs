# STR2DIGITS

Action

This statement will convert a string into an array of binary numbers.

Syntax

STR2DIGITS  s , ar(1)

Remarks

s | A string variable that holds a number. For example "12345"  
---|---  
ar(1) | The first element of a byte array that will be assigned with the binary representation of the digits. After the conversion, the first element will be assigned with the number of processed digits. The next element will become the most right digit of the string, the last element will become the first character of the string. In this example with string "12345" ar(1) = 5 ar(2) = 5 ar(3) = 4 ar(4) = 3 ar(5) = 2 ar(6) = 1 Your array need to be big enough to hold all digits and the digit counter.  
  
You can convert a string into a number with VAL() and a number into a string with STR().

In some cases, it is required to have access to all the individual digits of a variable.

While you can use a loop and MOD to get all digits, the STR2DIGITS will work for bytes, word, and longs.

Non numeric digits will not be converted properly. For example, in a string "-0" , the 0 which is ASCII 48, will be converted into a 0. The - is 45 and will result in 45-48=-3, and in byte form : 253.

The dot (.) will be converted into 254. 

See also

[STR](str.md) , [VAL](val.md)

Example

```vb
'-------------------------------------------------------------------------------  
' ARDUINO-Duemilanove.BAS  
' Also tested with ARDUINO NANO V3.0  
' (c) 1995-2025, MCS Electronics  
' This is a sample file for the Mega328P based ARDUINO board  
' Select Programmer 'ARDUINO' , 57600 baud and the proper COM port  
'-------------------------------------------------------------------------------  
$regfile= "m328pdef.dat" ' used micro  
$crystal=16000000 ' used xtal  
$baud=19200 ' baud rate we want  
config clockdiv=1 ' either use this or change the divider fuse byte  
'-------------------------------------------------------------------------------  
  
dim w as word  
dim s as string * 6, ar(6) as byte  
  
config portb=output ' make portb an output  
do  
toggle portb ' toggle level  
waitms 1000 ' wait 1 sec  
print "Duemilanove" ' test serial com  
  
```
w=w+1 : s=str(w) ' convert w to a string  
str2digits s,ar(1) ' convert string into an array with binary numbers  
loop