# ABS

Action

Returns the absolute value of a numeric signed variable.

Syntax

var = ABS(var2)

Remarks

Var | Variable that is assigned with the absolute value of var2.  
---|---  
Var2 | The source variable to retrieve the absolute value from.  
  
var : Integer , Long, Single or Double.

var2 : Integer, Long, Single or Double.

![notice](notice.jpg) The absolute value of a number is always positive.

See also

NONE

ASM

Calls: _abs16 for an Integer and _abs32 for a Long

Input: R16-R17 for an Integer and R16-R19 for a Long

Output:R16-R17 for an Integer and R16-R19 for a Long

Calls _Fltabsmem for a single from the fp_trig library.

Example

Dim a as Integer, c as Integer

a =-1000

c = Abs(a)

```vb
Print c

End

```