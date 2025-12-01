# CmdDlStart

Action

Start a New Display List.

When the co-processor engine executes this command, it waits until the display list is ready for writing, then sets Reg_Cmd_DL to zero.

Syntax

CmdDlStart

Remarks

In most of FTDI's FT800 C/C++ examples you will notice this command is used at the beginning of each loop or graphic routine.

Note: The Bascom FT800 Lib calls CmdDlStart from within [UpdateScreen](upperline.md) so it's not required in most circumstances.