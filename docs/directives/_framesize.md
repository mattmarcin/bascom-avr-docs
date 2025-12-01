# $FRAMESIZE

Action

Sets the available space for the frame.

Syntax

$FRAMESIZE = var

Remarks

Var | A numeric decimal value.  
---|---  
  
While you can configure the Frame Size in Options, Compiler, Chip, it is good practice to put the value into your code. This way you do no need the cfg(configuration) file.

The $FRAMESIZE directive overrides the value from the IDE Options.

It is important that the $FRAMESIZE directive occurs in your main project file. It may not be included in an $include file as only the main file is parsed for $FRAMESIZE. $FRAMESIZE only accepts numeric values. 

![notice](notice.jpg)Functions like [PRINT](print.md), [LCD](lcd_1.md), [INPUT](input.md) and the FP num <> [FORMAT](format.md) String conversion routines require a buffer in SRAM. Because of that the compiler always is using 24 bytes of frame space. This 24 Byte start at the beginning of the Frame which act as the conversion buffer within the frame (See also picture).

Because the FRAME is growing bottom up and this 24 Byte start at the beginning of the FRAME this 24 Byte conversion buffer start at the lowest FRAME Address (See picture). Here you also see that a too small $framesize causes an overwriting of Software Stack and/or Hardware Stack which lead to malfunction. If you use Print numVar, then the numeric variable "numvar" is converted into a string representation of the binary number. The framespace buffer is also used for that.

When there is not enough room inside the frame, the ERR variable will be set to 1. 

See also

[$SWSTACK](_swstack.md), [$HWSTACK](_hwstack.md), [Memory usage](memory_usage.md)

![framesize](framesize.png)

Picture: Memory of ATXMEGA128A1

A LOCAL variable is a temporary variable that is stored in frame. 

There can be only LOCAL variables of the type BYTE, INTEGER, WORD, LONG, SINGLE, DOUBLE or STRING.

A LOCAL Integer will use 2 Bytes of Frame ,

A LOCAL Long will use 4 Bytes. 

A LOCAL string * 20 will use 20 + 1 = 21 Byte (this additional 1 Byte is because every String is terminated with a 0-Byte)

When the SUB or FUNCTION is terminated, the memory will be released back to the frame but the FRAME will not be cleared ! Therefore a LOCAL variable is not initialized. So you can not assume the variable is 0. If you like it to be 0, you need to assign it !

BIT variables are not possible as LOCAL because they are always GLOBAL to the system.

Arrays can NOT be used as LOCAL (but arrays can be passed by REFERENCE as parameter to SUB and FUNCTIONS which just need 2 Bytes Software Stack of the Address of Array start)

See following example for frame calculation:

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
End Sub

```
Now we calculate the FRAME:

The Print A1 will be placed in the first frame-Byte of the 24 Byte conversion buffer.

5 LOCAL Byte (A1 â¦ A5) = 5 Byte of FRAME

LOCAL String: 254 Byte + 1 Byte = 255 Byte

Frame needed = 24Byte Frame conversion Buffer + 5 Byte + 255 Byte = 284 Byte 

This can be easy double checked with BASCOM-AVR Simulator (see following picture).

In following picture you see the start of FRAME which start with the 24Byte conversion buffer. The 31 in the first Frame Byte is from Print A1. After the 24 Byte conversion buffer follow the 5 Local Byte variables (A1 â¦. A5) and then the 255 Byte for the LOCAL String.

As with Software Stack you need to calculate the Framesize needed by the SUB or FUNCTION with the most LOCAL Variables and parameter passed by REFERENCE etc..

Take care when calling a SUB within a SUB. In this case you need to add the FRAME needed by both SUB !

When both SUB need 284 Byte you need to use:

24 Byte conversion Buffer + 2* 5 Byte (A1â¦A5) + 2*255 Byte (String) = 544 Byte

(the conversion buffer is needed only once !)

![frame_calc](frame_calc.png)

Picture: Memory window of BASCOM-AVR Simulator (Frame calculation example)

```vb
For further investigation of Stacks and Frame we use a SUB with 5 LOCAL Byte Variables and a PRINT function within the SUB. We start with hwstack, swstack and framesize defined and in second step we set swstack to 0. In addition we will lower the framesize to a not recommended value to force overwriting of other stack bytes.

$regfile = "xm128a1def.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 64  
$swstack = 128  
$framesize = 256  
  
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

  
A1 = 1  
A2 = 2  
A3 = 3  
A4 = 4  
A5 = 5  
```vb
Print A1  
  
End Sub

```
Here we see the 64 Byte Hardware Stack followed by 128 Byte Software Stack and then 256 Byte Frame. As always the Frame is the 24 Byte conversion buffer + rest of frame.

![framesize6](framesize6.png)

Picture : SRAM for Example with $hwstack = 64, $swstack = 128, $framesize = 256

The Simulator Memory Window show give us the details:

![framesize2](framesize2.png)

Picture: Simulator Memory Window for Example with $hwstack = 64, $swstack = 128, $framesize = 256

The second example use $hwstack = 64, $swstack = 0, $framesize = 256

Without defining a software Stack or with $swstack = 0 the Frame follows direct after the Hardware Stack. The Frame is as always 24 Byte conversion buffer + Rest of Frame.

Rest of Frame is in this case: 256 Byte â 24 Byte = 232 Byte

![framesize4](framesize4.png)

Picture: SRAM for example with $hwstack = 64, $swstack = 0, $framesize = 256

In the BASCOM Simulator Window you now see the addresses of the LOCAL variables are now stored in FRAME (which are usually in the Software Stack). This is not a problem as long as the Frame is big enough not to overwrite these addresses of the LOCAL variables.

(Remember: Address of LOCAL variables are stored in Software Stack (when Software Stack is defined) . The LOCAL Variables itself are stored in FRAME)

And here you see also with the 24 Byte conversion buffer the absolute minimum you need to define for software Stack and Framesize together is 24 Byte !

But this is not the recommendation. The recommendation is always define values for all Stack and Frame !

![framesize5](framesize5.png)

Picture: Simulator Memory Window for Example with $hwstack = 64, $swstack = 0, $framesize = 256