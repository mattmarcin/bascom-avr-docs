# WaitCmdFifoEmpty

Action

Executes Commands in the FIFO buffer.

Syntax

WaitCmdFifoEmpty

Remarks

WaitCmdFifoEmpty polls a loop checking the state of the Reg_Cmd_Read and Reg_Cmd_Write registers

to see whether the FT800 has executed the commands in the FIFO buffer.

If the your code is long you have to be careful it's not more than 4K otherwise you can get

overflows/corruption.

Inserting WaitCmdFifoEmpty in area of your code allows you to execute parts of your code

instantly, but be aware it won't display any Graphics and don't use it for Graphics Display

(use [UpdateScreen)](updatescreen.md)