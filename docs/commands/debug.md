# DEBUG

Action

Instruct compiler to start or stop debugging, or print variable to serial port

Syntax

DEBUG ON | OFF | var

Remarks

ON | Enable debugging  
---|---  
OFF | Disable debugging  
var | A variable which values must be printed to the serial port  
  
During development of your program a common issue is that you need to know the value of a variable.

You can use PRINT to print the value but then it will be in the application as well.

You can use conditional compilation such as :

CONST TEST=1

```vb
#IF TEST

print var

#ENDIF

```
But that will result in a lot of typing work. The DEBUG option is a combination of conditional compilation and PRINT. Whenever you activate DEBUG with the ON parameter, all 'DEBUG var' statements will be compiled.

When you turn DEBUG OFF, all 'DEBUG var' statements will not be compiled.

You can not nest the ON and OFF. The last statements wins.

Typical you will have only one DEBUG ON statement. And you set it to OFF when your program is working.

An example showing nesting is NOT supported:

DEBUG ON

DEBUG ON ' it is still ON

DEBUG OFF' it is OFF now

An example showing multiple DEBUG:

DEBUG ON

DEBUG var ' this is printed

DEBUG var2 ' this is also printed

DEBUG OFF

DEBUG var3 'this is NOT printed

DEBUG var4 ' this is not printed

DEBUG ON ' turn DEBUG ON

If A = 2 Then

DEBUG A ' this is printed when A is 2

End If

![notice](notice.jpg)When DEBUG ON is used, the UART is initialized. This means that TX and RX pins are set to UART mode where they can not be altered by the user with simple SET/RESET statements. 

See also

DBG

ASM

NONE

Example

DEBUG ON

Dim A As Byte

DEBUG A

End