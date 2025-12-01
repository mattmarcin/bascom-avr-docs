# POWER

Action

Returns the power of a single or double variable and its argument

Syntax

var = POWER( source, raise )

Remarks

Var | A numeric variable that is assigned with the power of variable source ^ raise.  
---|---  
Source | The single or double variable to get the power of.  
  
The POWER function works for positive floating point variables only.

When you use a ^ b , the sign will be preserved.

While Excel does not allow raising a negative single, QB does allow it.

The Power functions uses less code compared with the code that is generated when you use ^ for floating point values.

It is important that you use single variables for both single and raise. Constants are not accepted.

In version 1.11.9.2 the power function is improved so that it returns the same result as Excel. Previously it returned the same number as QB/VB. For example : -2 ^ 2 would be returned as -4, but -2 ^ 3 would be returned as -8 which is wring since -2 ^ 3 = -2 x -2 x -2=4 x -2 = -8. Minus times a minutes makes a positive number. So it depends on the sign of the base and if the number of raise if even or odd. 

The exception handling was also improved. 

Base | Raise | Result  
---|---|---  
0 | 0 | NAN  
NAN | x | NAN  
x | NAN | NAN  
Infinity | x | NAN  
x | Infinity | NAN  
0 | x<0 | Infinity  
0 | x>0 | 0  
x | 0 | 1  
x<0 | x<>int(x) | NAN  
  
See Also

[EXP](exp.md) ,[LOG](log.md), [LOG10](log10.md) , [SQR](sqr.md)

Example

[Show sample](fp_trig.md)

Example for Double Exceptions

```vb
$regfile = "m128def.dat"  
$crystal = 4000000

  
Dim D1 As Double , D2 As Double , D3 As Double  
Dim dInf as Double, dNAN as Double

```
d1 = -1: dNAN = log(d1)  
d1 = 1: d2 = 0: dInf = D1 / D2

```vb
Print "POWER() - Test"  
Print "=============="

```
D1 = 0: D2 = 0: GoSub ShowPowerTest

D1 = dNAN: D2 = 3: GoSub ShowPowerTest

D1 = 3: D2 = dNAN: GoSub ShowPowerTest

D1 = dInf: D2 = 4: GoSub ShowPowerTest

D1 = 4: D2 = dInf: GoSub ShowPowerTest

D1 = 0: D2 = -2: GoSub ShowPowerTest

D1 = 0: D2 = 3: GoSub ShowPowerTest

D1 = 5: D2 = 0: GoSub ShowPowerTest

D1 = -2: D2 = -3.5: GoSub ShowPowerTest

D1 = -2: D2 = 3.5: GoSub ShowPowerTest

D1 = -2: D2 = -3: GoSub ShowPowerTest

D1 = -2: D2 = -4: GoSub ShowPowerTest

D1 = -2: D2 = -5: GoSub ShowPowerTest

D1 = -2: D2 = 3: GoSub ShowPowerTest

D1 = -2: D2 = 4: GoSub ShowPowerTest

D1 = -2: D2 = 5: GoSub ShowPowerTest

  
end

  
ShowPowerTest:

D3 = POWER(D1, D2)

```vb
Print "POWER( " ; D1 ; " , " ; D2 ; ") = " ; D3

Return  
  
  
```
\--------------------------Simulator Output -------------------  
POWER() - Test

==============

POWER( 0 , 0) = NAN

POWER( NAN , 3) = NAN

POWER( 3 , NAN) = NAN

POWER( Infinity , 4) = NAN

POWER( 4 , Infinity) = NAN

POWER( 0 , -2) = Infinity

POWER( 0 , 3) = 0

POWER( 5 , 0) = 1

POWER( -2 , -3.5) = NAN

POWER( -2 , 3.5) = NAN

POWER( -2 , -3) = -125E-3

POWER( -2 , -4) = 62.5E-3

POWER( -2 , -5) = -31.25E-3

POWER( -2 , 3) = -8

POWER( -2 , 4) = 16

POWER( -2 , 5) = -32