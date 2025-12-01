# DEG2RAD

Action

Converts an angle in to radians.

Syntax

var = DEG2RAD( angle )

Remarks

Var | A numeric variable that is assigned with the radians of variable Source.  
---|---  
angle | The single or double variable to get the degrees of.  
  
All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

Radian is the ratio between the length of an arc and its radius. The radian is the standard unit of angular measure.

You can find a good explanation at [wikipedia](<http://en.wikipedia.org/wiki/Radian>).

See Also

[RAD2DEG](rad2deg.md)

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates DEG2RAD function

'-------------------------------------------------------------------------------

Dim S As Single

```
S = 90

S = Deg2Rad(s)

Print S

S = Rad2deg(s)

```vb
Print S

End

```