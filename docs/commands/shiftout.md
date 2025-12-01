# SHIFTOUT

Action

Shifts a bit stream out of a variable into a port pin .

Syntax

SHIFTOUT pin , pclock , var , option [, bits , delay ]

Remarks

Pin | The port pin which serves as a data output.  
---|---  
Pclock | The port pin which generates the clock.  
Var | The variable that is shifted out.  
Option | Option can be : 0 â MSB shifted out first when clock goes low 1 â MSB shifted out first when clock goes high 2 â LSB shifted out first when clock goes low 3 â LSB shifted out first when clock goes high  
Bits | Optional number of bits to shift out.  
Delay | Optional delay in uS. When you specify the delay, the number of bits must also be specified. When the default must be used you can also use NULL for the number of bits.  
  
If you do not specify the number of bits to shift, the number of shifts will depend on the type of the variable.

When you use a byte, 8 shifts will occur and for an integer, 16 shifts will occur. For a Long and Single 32 shifts will occur.

The SHIFTIN routine can be used to interface with all kind of chips.

The PIN is normally connected with the input of a chip that will receive information.

The PCLOCK pin is used to clock the bits out of the chip.

The VARIABLE is a normal BASIC variable. And may be of any type except for BIT. The data that is stored in the variable is sent with PIN.

The OPTIONS is a constant that specifies the direction of the bits. The chip that reads the data may want the LS bit first or the MS bit first. It also controls on which edge of the clock signal the data is sent to PIN.

The number of bits may be specified. You may omit this info. In that case the number of bits of the element data type will be used.

The DELAY normally consists of 2 NOP instructions. When the clock is too fast you can specify a delay time(in uS).

![notice](notice.jpg)The clock pin is brought to a initial level before the shifts take place. For mode 0, it is made 1. This way, the first clock can go from 1 to 0. And back to 1. You could see this as another clock cycle. So check if you use the proper mode. Or put the clock pin in the right state before you use SHIFT.

See also

[SHIFTIN](shiftin.md) , [SHIFT](shift.md)

Example

See [SHIFTIN](shiftin.md) sample