# Memory usage

SRAM

Every variable uses memory. Variables are stored in memory. This memory is also called SRAM (static ram). 

The available memory depends on the chip. When you double click on the chip pinout, you can view the parameters of the used chip.

A special kind of memory are the registers in the AVR. Registers 0-31 have addresses 0-31.

Almost all registers are used by the compiler or might be used in the future.

Which registers are used depends on the program statements you use.

This brings us back to the SRAM.

No SRAM is used by the compiler other than the space needed for the software stack ([$SWSTACK](_swstack.md)) and frame 

([$FRAMESIZE](_framesize.md))

Some statements might use some SRAM. When this is the case it is mentioned in the help topic of that statement.

For example, [CONFIG CLOCK](config_clock.md) in user mode requires variables to hold the time. Variables like _sec , _min , _hour, _day , _month , _year.

Each 8 bits used occupy one byte. When you dimension 1 bit, you will also use 1 byte. 

Each byte variable occupies one byte.

Each integer/word variable occupies two bytes.

Each Long, Dword or Single variable occupies four bytes.

Each double variable occupies 8 bytes.

Each string variable occupies at least 2 bytes.

A string with a length of 10 occupies 11 bytes.

![notice](notice.jpg)Strings need an additional byte (Null termination) to indicate the end of the string. That's why a string of 10 bytes occupies 11 bytes.

![notice](notice.jpg)With dimension of a bit you will occupy one byte.

Use bits or byte variables wherever you can to save memory. (not allowed for negative values)

See also [DIM](dim.md)

The software stack is used to store the addresses of LOCAL variables and for variables that are passed to SUB routines.

Each LOCAL variable and passed variable to a SUB/FUNCTION, requires two bytes to store the address (because it is a 16-Bit address = 2 bytes).

So when you have a SUB routine in your program that passes 10 variables, you need 10 * 2 = 20 bytes. 

When you use 2 LOCAL variables in the SUB program that receives the 10 variables, you need additional 2 * 2 = 4 bytes.

See also [DECLARE SUB](declare_sub.md), [DECLARE FUNCTION](declare_function.md)

The software stack ([$SWSTACK](_swstack.md)) size can be calculated by taking the maximum number of parameters in a SUB routine, adding the number of LOCAL variables and multiplying the result by 2. To be safe, add 4 more bytes for internally used LOCAL variables.

LOCAL variables are stored in a place that is named the Frame ([$FRAMESIZE](_framesize.md))

When you have a LOCAL STRING with a size of 40 bytes, and a LOCAL LONG, you need 41 + 4 bytes = 45 bytes of frame space.

When you use conversion routines such as [STR](str.md), [VAL](val.md), [HEX](hex.md), [INPUT](input.md) etc. that convert from numeric to string and vice versa, you also need a frame. Note that the use of the [INPUT](input.md) statement with a numeric variable, or the use of the [PRINT](print.md) or [LCD](lcd_1.md) statement with a numeric variable, will also force you to reserve 24 bytes of frame space. This because these routines use the internal numeric<>string conversion routines. 

![notice](notice.jpg)In fact, the compiler creates a buffer of 24 bytes that serves as scratchpad for temporary variables, and conversion buffer space. So the frame space should be 24 at minimum ([$FRAMESIZE](_framesize.md) = 24). This 24 Byte start at the beginning of the Frame which act as the conversion buffer within the frame

For an ATXMEGA or ATMEGA you have usually enough SRAM so you can start with higher values of Stack and Frame.

With an ATTINY13 and 64Byte SRAM it is a challenge but also start with all stack defined and lower the Stack Values when your application program grows.

•| Avoid to use SUB or FUNCTIONS (If you want to save SRAM space)  
---|---  
  
•| If you use Functions like PRINT, LCD, INPUT and the FP num <> FORMAT(), String conversion you need to define the 24 Byte conversion buffer (at least 24Byte for Software Stack + FRAME together).  
---|---  
  
![memusage1](memusage1.png)

In this case just 9 Bytes are left for global variables !

See also: [$HWSTACK](_hwstack.md), [$SWSTACK](_swstack.md), [$FRAMESIZE](_framesize.md)

XRAM

Some processors have an external memory interface. For example the ATMEGA128 has such an interface.

The additional memory is named XRAM memory (extended or external memory).

When you add 32 KB RAM, the first address will be 0.

But because the XRAM can only start after the internal SRAM, the lower memory locations of the XRAM will not be available for use. The processor will automatically use the SRAM if an address is accessed that is in range of the SRAM memory.

Thus adding 32KB of XRAM, will result in a total of 32 KB RAM.

With ATXMEGA you can add XRAM with the EBI (External Bus Interface). There is no problem to add for example 

16 MByte of external SDRAM.

See [CONFIG XRAM](configxram.md)

ERAM

Most AVR chips have internal EEPROM on board.

This EEPROM can be used to store and retrieve data.

In BASCOM, this data space is called ERAM.

An important difference is that an ERAM variable can only be written to a maximum of 100.000 times. So only assign an ERAM variable when it is required, and never use it in a loop or the ERAM will become unusable.

Always use the Brown out detection of the processor to prevent EEPROM corruption.

See also [DIM](dim.md)

For ATXMEGA see also [CONFIG EEPROM](config_eeprom.md)

Constant code usage

Constants are stored in a constant table.

Each used constant in your program will end up in the constant table.

```vb
For example:

Print "ABCD"  
Print "ABCD"

```
This example will only store one constant (ABCD).

```vb
Print "ABCD"  
Print "ABC"

```
In this example, two constants will be stored because the strings differ.

Stack

See also: [$HWSTACK](_hwstack.md), [$SWSTACK](_swstack.md), [$FRAMESIZE](_framesize.md)

The Stack is a part of SRAM (Static RAM). In SRAM the compiler stores user dimensioned variables, as well as internal variables, but SRAM holds also Hardware Stack, Software Stack and Frame. The Variables always start at the lowest SRAM Address. After Reset all SRAM Bytes are 0 (and strings are "") so the SRAM memory is cleared after reset. With the $noramclear option you can turn this behavior off which means the SRAM is not cleared after reset.

The available SRAM depends on the Chip.

With ATTINY13 for example you have 64Byte of SRAM and you will find this information beside the user manual in the *.DAT file. You can also double click the chip in Chip Pinout to view the chip parameters.

The following you find in the attiny13.dat file:  SRAM = 64 ; SRAM size

Global Variables start with the lowest SRAM Address and the Hardware Stack start with the highest SRAM Address.

![memusage2](memusage2.png)

Example for using with Bascom-AVR Simulator:

```vb
$regfile = "attiny13.dat"  
$crystal = 4000000  
$hwstack = 30  
$swstack = 0  
$framesize = 24  
  
Dim B As Byte  
```
B = 5  
  
  
Pcmsk = &B00000001 'PIN Change Int  
```vb
ON PCINT0 pin_change_isr  
Set Gimsk.5  
Enable Interrupts  
  
Do  
```
!NOP  
```vb
Loop  
  
End 'end program  
  
```
pin_change_isr:  
B = 7  
Return

With an ATTINY13 the SRAM is just 64Byte and it is easy to see which SRAM Bytes will be overwritten with Bascom AVR Simulator Memory Window.

Click on M to display the memory window.

![memusage3](memusage3.png)

![memusage4](memusage4.png)

Picture: SRAM of ATTINY13 when executing the above ATTINY13 example in Bascom Simulator

You can see the Hardware Stack (32 Byte) , Frame (24 Byte) and the Variable B.

For this example you do not really need a Frame so it could be also $framesize = 0 for this example.

With ATXMEGA128A1 there is 8K Byte of SRAM available and you can find in the DAT file  (SRAM = 8192 ; SRAM size )

![notice](notice.jpg)The Values of Stack should be ALWAYS defined at the beginning of any BASCOM-AVR Program in the main project file. The best place is right after the [$REGFILE](regfile.md) statement.

Example:

```vb
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 32 ' default use 32 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  


```
The following example show what can happen when you define NO Stacks or Frame or when you define not enough Stack or Frame. 

In this example we use: $hwstack = 64, $swstack = 0, $framesize = 8

As we know now Software Stack and FRAME together must be as absolute minimum 24 Byte (for the conversion buffer) so we force the overwriting of Hardware Stack which causes malfunction.

(Reminder: Donât start with the lowest values for Stack and Frame)

![](embim1.png)

Picture : SRAM for example with$hwstack = 64, $swstack = 0, $framesize = 8 

You can now imagine what could happen:

•| Because of overwritten return address in Hardware Stack the micro is jumping to somewhere else and malfunction if forced.  
---|---  
  
•| Functions like PRINT overwrite addresses of LOCAL Variables and here also will the micro jump to somewhere else and malfunction is forced.  
---|---  
  
![memusage6](memusage6.png)

Picture: Simulator Memory Windows for example with $hwstack = 64, $swstack = 0, $framesize = 8 

Now an example for passing an Array to a SUB:

![memusage11](memusage11.png)

With this example we see the complete SRAM.

The SRAM start with the dimed variables. In this case it start with the variable I followed by the Array Ar of 16 Byte and in the end the variable B. 

Because it is easier with the memory window of Bascom Simulator I choose multiple of 16 for Stack and Framesize.

We have here 2 Addresses stored in Software Stack. One address for the Array and one address for the variable B.

So passing an Array to a SUB just need 2 Bytes for the address in Stack which is the same size as for one Byte variable (here variable B).

![memusage7](memusage7.png)

Picture: Simulator Memory Window for example passing an Array to a SUB

With this example you also see that especially with ATTINY and smaller ATMEGA it is not that complicated to see if other SRAM bytes will be overwritten by something and causes malfunction.

You have with the Simulator window the âbig pictureâ of SRAM and STACK together.

As already written it is easier to use multiple of 16 for Hardware Stack, Software Stack and FRAME as a starting point because one line in Simulator Memory window is 16 Bytes.

How to see which Variables are stored on which SRAM Byte ?

You can find out the stored variable with the Bascom-AVR Simulator Memory Window by clicking on that byte.

Click on SRAM Bytes show the OCCUPIED BY in the footer of that window.

Only the first Byte of an Array will show the Name of the Array !

![memusage8](memusage8.png)

Picture: How to see which Variables are stored on which SRAM Byte

You can also find this information in the Compiler output report:

In this case under VARIABLES

![memusage9](memusage9.png)

Picture: How to see which Variables are stored on which SRAM Address

The following small example is good for examining the Bascom-AVR internal variables like _sec, _min or _hour in Bascom-AVR Simulator Memory Window.

```vb
Config Clock = User for example create the internal variables for seconds (_sec), minutes (_min) ,hour (_hour) etcâ¦. You can see this variables by clicking on the SRAM Byte and watch the footer of that Bascom-AVR Simulator Memory Window footer.

$regfile = "m88def.dat"  
$hwstack = 48  
$swstack = 80  
$framesize = 80  
  
Config Clock = User  
  
End 'end program

```
![memusage10](memusage10.png)

Picture: Internal Variables in the Bascom-AVR Simulator Memory Window

See also: [$HWSTACK](_hwstack.md), [$SWSTACK](_swstack.md), [$FRAMESIZE](_framesize.md)