# File ZIP

This option will put all project files into a ZIP file.

The file will be given the ZIP extension and is saved into the same folder as the main file.

When your file is named main.bas, the file main.zip will be created.

The following files will be included :

\- all files which are included with $INCLUDE

\- all files which are included with $INC

\- all files which are included with $BGF

If a file is included in the code but can not be found you will get a warning.

![file_zip](file_zip.png)

This option does take conditional compilation into account. 

Meaning that :

```vb
#const a=1

#if a=2

$Include "FT800.inc"

$Include "FT800_Functions.inc"

#endif

```
The files ft800.inc and ft800_functions.inc are not included since the condition does not match.