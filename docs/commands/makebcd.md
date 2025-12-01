# MAKEBCD

Action  
  
Convert a variable into its BCD value.

Syntax

var1 = MAKEBCD(var2)

Remarks

var1 | Variable that will be assigned with the converted value.  
---|---  
Var2 | Variable that holds the decimal value.  
  
When you want to use an I2C clock device, which stores its values as BCD values you can use this function to convert variables from decimal to BCD.

For printing the BCD value of a variable, you can use the BCD() function which converts a BCD number into a BCD string.

See also

[MAKEDEC](makedec.md) , [BCD](bcd.md) , [MAKEINT](makeint.md)

Example

Dim A As Byte

A = 65

Lcd A

Lowerline

Lcd Bcd(a)

A = Makebcd(a)

Lcd " " ; A

End