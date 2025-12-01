# WR8

Action

This statement will write an address and a byte parameter to the FT800.

Syntax

WR8 address , prm

Remarks

The address need to be an address in the FT800 address range. See FT800 manual for more info.

The parameter (prm) is a word numeric value. It depends on the address which parameter value you may send.

When you want to write to the FIFO buffer you can best use CMD8.

See also

[CMD8](cmd8.md) , [CMD16](cmd16.md), [CMD32](cmd32.md) , [WR16](wr16.md), [WR32](wr32.md)

Example

Wr8 Reg_GPIO_Dir , &H83  
Wr8 Reg_GPIO , &H83  
  
Wr16 Reg_Touch_rzThresh , 1200

  
Wr32 Ram_DL + 0, &H02FFFFFF