# UpdateScreen

Action

Executes the Commands in the FIFO and Display the Graphics. 

Syntax

UpdateScreen

Remarks

UpdateScreen High level command which executes the following commands

[Display_E](display_e.md)

[CmdSwap](cmdswap.md)

[CmdDlStart](cmddlstart.md)

[WaitCmdFifoEmpty](waitcmdfifoempty.md)

Generally you insert this command towards the end of the loop or when you need to

update the LCD.

Example

```vb
' Pseudocode

Do

```
ClearScreen

BitmapLayout PALETTED, Ft_DispWidth , Ft_DispHeight

BitmapSize NEAREST, BORDER, BORDER, Ft_DispWidth, Ft_DispHeight

...

...

UpdateScreen

Loop