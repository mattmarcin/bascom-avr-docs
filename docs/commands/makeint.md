# MAKEINT

Action

Compact two bytes into a word or integer.

Syntax

varn = MAKEINT(LSB , MSB)

Remarks

Varn | Variable that will be assigned with the converted value.  
---|---  
LSB | Variable or constant with the LS Byte.  
MSB | Variable or constant with the MS Byte.  
  
The equivalent code is:

varn = (256 * MSB) + LSB

See also

[LOW](low.md) , [HIGH](high.md) , [MAKEBCD](makebcd.md) , [MAKEDEC](makedec.md)

Example

Dim A As Integer , I As Integer

A = 2

I = Makeint(a , 1) 'I = (1 * 256) + 2 = 258

End