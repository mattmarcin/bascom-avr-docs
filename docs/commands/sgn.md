# SGN

Action

Returns the sign of a numeric value.

Syntax

var = SGN( x )

Remarks

Var | A numeric variable that is assigned with the SGN() of variable x.  
---|---  
X | The numeric variable to get the sign of.  
  
```vb
For values < 0, -1 will be returned

For 0, 0 will be returned

For values >0, 1 will be returned

While the SGN function can return a negative value, it can only do so for integers, longs, singles and doubles.

```
When a byte, word or dword is passed, only 0 or 1 can be returned since these values do not contain a sign bit.

When a byte,word or dword is passed, the returned value is a byte.

When an integer is passed, the returned value is an integer.

When a long is passed, the returned value is a long.

When a single is passed, the returned value is a single.

When a double is passed, the returned value is a double.

See Also

[INT](int.md) , [FIX](fix.md) , [ROUND](round.md)

Example

Dim S As Single , X As Single , Y As Single

X = 2.3 : S = Sgn(x)

Print S

X = -2.3 : S = Sgn(x)

```vb
Print S

End

```