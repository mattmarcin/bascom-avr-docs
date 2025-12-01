# $EXTERNAL

Action

Instruct the compiler to include ASM routines from a library.

Syntax

$EXTERNAL Myroutine [, myroutine2]

Remarks

You can place ASM routines in a library file. With the $EXTERNAL directive you tell the compiler which routines must be included in your program.

See also

[$LIB](lib.md)

Example

```vb
$regfile = "m48def.dat"  
$crystal = 4000000  
$baud = 19200  
$hwstack = 16  
$swstack = 16  
$framesize = 16  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
'In order to let this work you must put the mylib.lib file in the LIB dir  
'And compile it to a LBX  
'-------------------------------------------------------------------------  
'define the used library  
$lib"mylib.lbx"  
'you can also use the original ASM :  
'$LIB "mylib.LIB"  
  
'also define the used routines  
$external Test  
'this is needed so the parameters will be placed correct on the stack  
Declare Sub Test(byval X As Byte , Y As Byte)  
'reserve some space  
Dim Z As Byte  
'call our own sub routine  
```
Call Test(1 , Z)  
```vb
'z will be 2 in the used example  
End

```