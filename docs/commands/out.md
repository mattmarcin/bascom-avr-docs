# OUT

Action

Sends a byte to a hardware port or internal or external memory address.

Syntax

OUT address, value

Remarks

Address | The address where to send the byte to in the range of 0-FFFF hex. For Xmega which supports huge memory, the address is in range from 0-&HFFFFFF.  
---|---  
Value | The variable or value to output.  
  
The OUT statement can write a value to any AVR memory location.

It is advised to use Words for the address. An integer might have a negative value and will write of course to a word address. So it will be 32767 higher as supposed. This because an integer has it's most significant bit set when it is negative.

![notice](notice.jpg) To write to XRAM locations you must enable the External RAM access in the [Compiler Chip Options](options_compiler_chip.md).

You do not need to use OUT when setting a port variable. Port variables and other registers of the micro can be set like this : PORTB = value , where PORTB is the name of the register.

![notice](notice.jpg)Take special care when using register variables. The address-part of the OUT statement, expects a numeric variable or constant. When you use a hardware register like for example PORTB, what will happen is that the value of PORTB will be used. Just as when you use a variable, it will use the variable value. 

So when the goal is to just write to a hardware register, you need to use the normal assignment : PORTB=3

See also

[INP](inp.md) , [PEEK](peek.md) , [POKE](poke.md) , [SETREG](setreg.md), [GETREG](getreg.md)

Example

Out &H8000 , 1 'send 1 to the databus(d0-d7) at hex address 8000

End