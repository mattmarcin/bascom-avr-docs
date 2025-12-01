# CONFIG CLOCKDIV

Action  
  
Sets the clock divisor.

Syntax

CONFIG CLOCKDIV = constant

Remarks

constant | The clock division factor to use. Possible values are 1 , 2 , 4 , 8 ,16 , 32 ,64 , 128 and 256.  
---|---  
  
The options to set the clock divisor is available in most new chips. Under normal conditions the clock divisor is one. Thus an oscillator value of 8 MHz will result in a system clock of 8 MHz. With a clock divisor of 8, you would get a system clock of 1 MHz.

Low speeds can be used to generate an accurate system frequency and for low power consumption.

Some chips have a 8 or 16 division enabled by default by a fuse bit.

You can then reprogram the fuse bit or you can set the divisor from code.

When you set the clock divisor take care that you adjust the $CRYSTAL directive also.

$CRYSTAL specifies the clock frequency of the system. So with 8 MHz clock and divisor of 8 you would specify $CRYSTAL = 1000000.

Some older chips use a different method for clock division. These chips do not support CONFIG CLOCK but they might support [CLOCKDIVSION](clockdivision.md).

See also

[$CRYSTAL](crystal_1.md) , [CLOCKDIVISION](clockdivision.md)

Example

CONFIG CLOCKDIV = 8 'we divide 8 MHz crystal clock by 8 resulting in 1 MHz speed