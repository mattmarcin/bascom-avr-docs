# CmdSwap

Action

Swap the current Display List

Syntax

CmdSwap

Remarks

When the co-processor engine executes this command, it requests a display list swap

immediately after current display list is scanned out. Internally, the co-processor engine

implements this command by writing to Reg_DlSwap

Note: The Bascom FT800 Lib calls CmdSwap from within [UpdateScreen](upperline.md) so it's not required in most circumstances.