# CONFIG SINGLE

Action

Instruct the compiler to use an alternative conversion routine for representation of a single.

Syntax

CONFIG SINGLE = SCIENTIFIC , DIGITS = value

Remarks

Single | SCIENTIFIC for scientific notation. Use NORMAL for the normal default notation. Using both modes will increase your code size.  
---|---  
Digits | A numeric constant with a value between 0 and 7. A value of 0 will result in no trailing zero's. A value between 1-7 can be used to specify the number of digits behind the comma.  
  
When a conversion is performed from numeric single variable, to a string, for example when you PRINT a single, or when you use the STR() function to convert a single into a string, a special conversion routine is used that will convert into human readable output. You will get an output of digits and a decimal point.

This is well suited for showing the value on an LCD display. But there is a downside also. The routine is limited in the way that it can not shown very big or very small numbers correct.

The CONFIG SINGLE will instruct the compiler to use a special version of the conversion routine. This version will use scientific notation such as : 12e3.

You can specify how many digits you want to be included after the decimal point.

It is possible to switch between notations by using multiple CONFIG SINGLE statements. As soon at the compiler encounters a CONFIG SINGLE, it will change to output to the selected format. You should not use CONFIG SINGLE inside a sub/function since this is not a dynamic feature that can be changed at run time.

See also

[FUSING](fusing.md), [STR](str.md)

ASM

Uses single.lbx library

Example

```vb
'----------------------------------------------------------------

' (c) 1995-2025, MCS

' single_scientific.bas

' demonstation of scientific , single output

'----------------------------------------------------------------

$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

'you can view the difference by compiling and simulating this sample with the

'line below remarked and active

Config Single = Scientific , Digits = 7

Dim S As Single

```
S = 1

Do

S = S / 10

```vb
Print S

Loop

```