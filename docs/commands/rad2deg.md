# RAD2DEG

Action

Converts a value from radians to degrees.

Syntax

var = RAD2DEG( Source )

Remarks

Var | A numeric variable that is assigned with the angle of variable source.  
---|---  
Source | The single or double variable to get the angle of.  
  
All trig functions work with radians. Use deg2rad and rad2deg to convert between radians and angles.

See Also

[DEG2RAD](deg2rad.md)

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