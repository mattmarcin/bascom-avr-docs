# CONFIG BASE

Action

This option specifies the lower boundary of all arrays.

Syntax

CONFIG BASE= value

Remarks

By default the first element of an array starts at 1. With CONFIG BASE=0 you can override this default so that all arrays start at 0. 

In some cases it is simpler that elements start at 0.

A constant named _BASE reflects the setting. You can not change the BASE at run time. 

![notice](notice.jpg)When you change this setting in existing code, you need to alter your code. For example when you used this code:

Dim a(10) as byte : a(10) = 10

And you set CONFIG BASE=0, it will mean that element 10 is invalid.

While in QB an additional element is created, this is not a good idea in bascom because it will require more space.

See also

[DIM](dim.md)

Example

```vb
CONFIG BASE=0

Dim ar(10) as byte , j as byte

For j=0 to 9 'array uses element 0-9

```
ar(j)=j

Next

Example

```vb
CONFIG BASE=1

Dim ar(10) as byte , j as byte

For j=1 to 10 ' arrays uses element 1-10

```
ar(j)=j

Next