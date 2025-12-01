# CONFIG ERROR

Action

Instructs the compiler to ignore one or more errors.

Syntax

CONFIG ERROR=ignore, err=ignore [err1=ignore]

Remarks

In some situations you might want to ignore an error. For example if a new version adds a certain check that was not available in a previous version you will get errors. If you ignore the error, the code will compile without errors. This will not work in any situation. Some errors can not be ignored. You should never use this option for a finished product. 

See also

NONE

Example

Config Error = Ignore , 369 = Ignore

Lbl:

Dim Lbl As Word ' this would generate an error 369 without the ignore !!!