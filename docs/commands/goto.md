# GOTO

Action

Jump to the specified label or address.

Syntax

GOTO label

Remarks

Labels can be up to 32 characters long.

When you use duplicate labels, the compiler will give you a warning.

Valid labels

\- A valid label ends with a colon (:)

\- A valid label starts on the line. 

\- There is no space between the label name and the colon. 

Label: is a valid label. 

Label : is invalid

Since a colon is also used to separate multiple lines of code, the label must be the only code on the line. 

```vb
For example :

print "abc" : print "klm" 'these lines are separated by a colon. 

```
abc: : print "klm" 'this is invalid since the line starts with a label.

Besides using a label you can also specify an address. GOTO &H0000 would jump to the reset vector of the processor.

Because numeric addresses can be specified, it is advised to use non-numerical labels. 

Notice that an address in the AVR is a WORD address. AVR instructions are 16 bit wide which means that for each instruction you need at least 2 bytes.

It is best to use label names.

See also

[GOSUB](gosub.md)

Example

Dim A As Byte

Start: ' a label must end with a colon

A = A + 1 ' increment a

```vb
If A < 10 Then ' is it less than 10?

Goto Start ' do it again

End If ' close IF

Print "Ready" ' that is it

```