# MAKEDEC

Action

Convert a BCD byte or Integer/Word variable to its DECIMAL value.

Syntax

var1 = MAKEDEC(var2)

Remarks

var1 | Variable that will be assigned with the converted value.  
---|---  
var2 | Variable that holds the BCD value.  
  
When you want to use an I2C clock device, which stores its values as BCD values you can use this function to convert variables from BCD to decimal.

See also

[MAKEBCD](makebcd.md) , [MAKEBCD](makebcd.md), [MAKEINT](makeint.md)

Example

Dim A As Byte

A = 65

```vb
Print A

Print Bcd(a)

```
A = Makedec(a)

```vb
Print Spc(3) ; A

End

```