# $FILE

Action

Change name of generated files.

Syntax

$FILE = "myname.bin"

Remarks

In some cases it is desired to change the name of the output file. By default, the generated files have the same base name as the opened project file. So if your program name is "mytest.bas" , all generated files will start with the base "mytest".

The $FILE directive let you change this base name. 

![notice](notice.jpg)Simulating and programming will NOT work since the IDE uses the base name of your project. If you change it with $FILE, the files can not be located. 

See also

NONE

Example

$FILE = "mytest.bin"