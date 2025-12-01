# QUOTE

Action

The Quote function will return a string surrounded by quotes.

Syntax

var = QUOTE( Source )

Remarks

Var | A string variable that is assigned with the quoted string of variable source.  
---|---  
Source | The string or string constant to be quoted.  
  
The Quote() function can be used in HTML web server pages. 

QUOTE supports [$BIGSTRINGS](bigstrings.md)

See also

NONE

Example

Dim S as String * 20

S = "test"

S = Quote(s)

```vb
Print S ' would print "test"

End

```