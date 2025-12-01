# Edit Proper Indent

This option will properly indent your code.

Indention is used to make code better readable.

Every structure will be indented. And nested will increase indenting.

This code :

For C = 0 To 100

B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

```
Will be transformed into :

For C = 0 To 100

B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

```
And this is a sample with nesting :

```vb
Do

Input "Data to write ? (0-255)" , D

Print "Reading content of EEPROM (via ERAM Byte)"

For C = 0 To 100

```
B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

Loop

```
When indenting does not work you need to check your code for mistakes. For example for endif instead of End If.

Proper indenting is also required for [proper drawing of indention](edit_show_excluded_code.md).