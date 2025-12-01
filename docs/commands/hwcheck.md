# $HWCHECK, $SWCHECK, $SOFTCHECK

Action

This directive can be used to determine the required stack space.

Syntax

```vb
$HWCHECK

$FRAMECHECK

$SOFTCHECK

```
Remarks

All variables you DIM in your application require RAM or SRAM space. But an application needs more RAM space.

Each time you call a sub or function, or us gosub, the processor need to know at which address to return after returning from the call. For this purpose, the processor saves this address on the hardware stack. There is noting you can do about this. This hardware stack grows downwards. Some basic statements compile into code that do not need any calls. But some call a machine language function which in turn can call other functions. Which and how many other calls will be made depend on the selected processor and other options. sometimes it also depends on variable parameters.

When parameters are passed to a sub or function, the address is passed of the variables. These are word addresses thus using 2 bytes for each variable. This passing is being done via the so called soft stack. This area is located below the HW stack space. And it also grows down.

All LOCAL variables you use also need 2 bytes of the soft stack.

When you pass a parameter with BYVAL or when you create a LOCAL variable, some temporarily space is need. 

Consider this example : somestring = "abc" + somestring 

When the compiler assigns "abc" to somestring, the somestring variable will become "abc" and it will overwrite the content making it impossible to add it's content after the "abc".

So we first need to store the content of somestring before we can start assigning new data to this string.

This copy also requires space.

This space is created dynamically and is taken from the so called frame space. This space is located below the soft stack.

Now you can use $DBG or some default values for most projects to determine the values.

But when you have a problem and have absolutely no idea how the settings must be made, you can use the $HWCHECK option.

You start with including a special library named "stackcheck.lib" to your code.

Then you run your application and somewhere in your code you print the value of the generated _hw_lowest variable.

This variable is set to &HFFFF and each time a call is made, the stack is compared to this value. If the hardware stack (SPL and SPH registers) are lower then the _hw_lowest value, _hw_lowest is assigned with the new lowest stack value.

This way you determine the lowest possible hardware stack value that occurred during the runtime of your application. 

Of course it is important that your application runs all code.

You can print the value or show it on LCD. To determine the actual needed space you subtract it from the stacktop value.

```vb
For the softstack the same applies. It will store the lowest Y-pointer value to the variable named _sw_lowest.

For the framespace the the variable _fw_highest is used and this variables is increasing.

```
The stackcheck.bas example demonstrates how to retrieve the values when a recursive sub is used.

See also

NONE

Example

```vb
$regfile = "m88def.dat"  
$hwstack = 40  
$swstack = 80  
$framesize = 80  
$lib "stackcheck.lib"  
  
Declare Sub Test(byval Prm As Byte)  
  
Print "stack test"  
  
Dim G As Byte , W As Word  
Dim P As Byte  
  
$hwcheck 'hw stack check on  
$framecheck  
$softcheck  
  
```
Test P  
Print _hw_lowest  
W = _hwstackstart - _hw_lowest  
```vb
Print "HW stack needed : " ; W  
  
Print _fw_highest  
If _fw_highest > 0 Then  
```
W = _frame_high - _fw_highest  
```vb
Print "Frame space needed : " ; W  
End If  
  
  
Print _sw_lowest  
```
W = _hwstack_low - _sw_lowest  
```vb
Print "SW stack needed : " ; W  
  
  
End  
  
  
Sub Test(byval Prm As Byte)  
```
Local L As Byte  
```vb
Print "HWSTACK:" ; _hw_lowest  
Print "Frame:" ; _fw_highest  
Print "SWSTACK:" ; _sw_lowest  
  
```
G = G + 1 ' global var  
```vb
If G >= 5 Then  
Exit Sub  
Else  
```
Test P 'recursive call  
```vb
End If  
End Sub

```