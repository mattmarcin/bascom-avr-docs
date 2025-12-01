# HIGHW

Action

Retrieves the most significant word of a long variable.

Syntax

var = HIGHW( s )

Remarks

Var | The variable that is assigned with the MS word of var S.  
---|---  
S | The source variable to get the MSB from.  
  
There is no LowW() function. This because when you assign a Long to a word or integer, only the lower part is assigned. For this reason you do not need a Loww() function. W=L will do the same.

See also

[LOW](low.md) , [HIGH](high.md)

Example

Dim X As Word , L As Long

L = &H12345678

X = Highw(l)

Print Hex(x)