# $SWSTACK

Action

Sets the available space for the software stack.

Syntax

$SWSTACK = var

Remarks

Var | A numeric decimal value.  
---|---  
  
While you can configure the SW Stack in Options, Compiler, Chip, it is good practice to put the value into your code. This way you do no need the cfg(configuration) file.

The $SWSTACK directive overrides the value from the IDE Options.

![notice](notice.jpg) It is important that the $SWSTACK directive occurs in your main project file. It may not be included in an $include file as only the main file is parsed for $SWSTACK. $SWSTACK only accepts numeric values. 

Software Stack stores the parameter addresses passed to a subroutine and LOCAL variable addresses. 

So the Software stack stores the addresses of variables where each passed variable and local variable use 2 bytes per respective addresses. 

When using SUB or FUNCTION there are 3 ways for parameters:

•| Using BYREF pass a variable by reference with its ADDRESS (so it is pointing to an existing variable which is already in SRAM)  
---|---  
  
•| Using BYVAL the value is stored in FRAME (during the SUB is processed) so it is pointing to the address in FRAME.  
---|---  
  
•| Using BYLABEL pass the address of a label  
---|---  
  
When nothing is specified the parameter will be passed BYREF.

See also

[$HWSTACK](_hwstack.md) , [$FRAMESIZE](_framesize.md), [Memory Usage](memory_usage.md)

For example if you have used 10 locals in a SUB and there are 3 parameters passed to it, you need:

(10 * 2 Byte) + (3 * 2 Byte) = 26 Byte Software Stack.

The following SUB need 10 Byte of Software Stack:

5* 2 Byte = 10 Byte

![swstack](swstack.png)

So the software stack size can be calculated by taking the maximum number of parameter passed to a SUB routine, adding the number of LOCAL variables and multiplying the result by 2. To be safe, add 4 more bytes for internally used LOCAL variables.

If you have several SUB or FUNCTIONS search for the SUB or FUNCTION with the most parameters and LOCAL variables and use that calculated maximum numbers for defining the Software Stack ($swstack).

The Software Stack is growing top down (see picture) and start direct after the Hardware Stack. The Software Stack grows against the FRAME.

![swstack_memmap](swstack_memmap.png)

Picture: Example Memory of ATXMEGA128A1

[[****]](<memory_usage.htm>)

Example

```vb
$regfile = "xm128a1def.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 128  
$framesize = 288  
  
  
Config Osc = Enabled , 32mhzosc = Enabled '32MHz  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1 '32MHz  
'Config Interrupts  
Config Priority = Static , Vector = Application , Lo = Enabled 'Enable Lo Level Interrupts  
Config Com1 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Declare Sub My_sub()  
  
```
Call My_sub()  
  
```vb
End 'end program  
  
Sub My_sub()  
```
Local A1 As Byte , A2 As Byte , A3 As Byte , A4 As Byte , A5 As Byte  
Local S As String * 254  
  
For A1 = 1 To 254  
S = S + "1"  
Next A1  
  
A1 = 1  
A2 = 2  
A3 = 3  
A4 = 4  
A5 = 5  
```vb
Print A1  
  
End Sub 'default use 40 for the frame space

```