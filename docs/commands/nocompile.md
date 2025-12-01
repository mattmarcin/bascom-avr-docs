# $NOCOMPILE

Action

Instruct the compiler not to compile the file.

Syntax

$NOCOMPILE

Remarks

This looks like an odd directive. Since you can split your program in multiple files, and you can create configuration files, you might open a file and try to compile it. Only normal project files can be compiled and you will get a number of errors and also unwanted files like error, report, etc.

To prevent that you compile a file that is intended to be included, you can insert the $NOCOMPILE directive.

Then the file will only be compiled when it is called from your main file, or other include file.

A file that is opened as thus the main file, and which includes the $NOCOMP directive, can not be compiled.

The IDE will see it as a successful compilation. This is important for the Batch Compiler.

See also

[Batch Compiler](toolsbatchcompile.md)

Example

$NOCOMPILE