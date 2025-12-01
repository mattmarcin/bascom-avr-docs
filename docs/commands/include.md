# $INCLUDE

Action

Includes an ASCII file in the program at the current position.

Syntax

$INCLUDE "file"

Remarks

File | Name of the ASCII file, which must contain valid BASCOM statements. This option can be used if you make use of the same routines in many programs. You can write modules and include them into your program. If there are changes to make you only have to change the module file, not all your BASCOM programs. You can only include ASCII files! An include file will only be included once, even if you include it multiple times.  
---|---  
  
Use [$INC](_inc.md) when you want to include binary files.

You can specify an absolute file name (with a drive and full path) like : $INCLUDE "c:\folder\myfile.bas"

Or you can specify a relative file name like : $INCLUDE "myfile.bas"

The main program path will be used to determine the absolute file name. 

If your main file is stored under c:\abc\main.bas , and you include a file named "test.inc" , the compiler expects a file named "c:\abc\test.inc"

You can include a path too. The path is relative to the main file.

When used in sub folders use " \ " (back slash). The path uses the DOS/Windows convention. A forward slash will work too since windows does not seem to be bothered with it. 

Example with sub folder Test: $include "Test\my_functions.bas"

When you include sub procedures and functions before the actual code, your code will run into this code. You can use a GOTO to jump over the included code or you can use CONFIG SUBMODE=NEW so that the compiler will only include the used functions. See Example2

See Also

[$INC](_inc.md) , [CONFIG SUBMODE=NEW](config_submode.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 10  
$swstack = 10  
$framesize = 26

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'--------------------------------------------------------------

Print "INCLUDE.BAS"

'Note that the file 123.bas contains an error

$include "123.bas" 'include file that prints Hello

Print "Back in INCLUDE.BAS"

End

```
Example2

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$hwstack = 10  
$swstack = 10  
$framesize = 26

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'--------------------------------------------------------------

$include "mysubs.bas" 'include file with sub procedures

'this is the included code : Sub Test()

' print "Test"

' End Sub 

'Without a GOTO to jump over the included code the code will run into the sub without a call

' Or use CONFIG SUBMODE=NEW so you do not need to change a thing

Print "Back in INCLUDE.BAS"

End

```