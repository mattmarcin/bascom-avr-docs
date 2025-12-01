# CONFIG DP

Action

This option sets the character used for the decimal point for singles and fusing.

Syntax

CONFIG DP= "dp"

Remarks

The decimal point is a dot (.) by default. The STR() and FUSING functions convert a single into a string. The fraction is separated by a dot. In a number of counties the comma is used as a separator. 

Old Syntax:

Valid options are : CONFIG DP = "." and CONFIG DP = ","

New preferred Syntax:

Valid options are : CONFIG DP = DOT and CONFIG DP = COMMA

This options only sets the character for str() and fusing for singles. In your code you still need to code with a dot : var = 1234.333

See also

NONE

Example

```vb
CONFIG DP = ","

Dim s as single

```
S = 1234.56

print s