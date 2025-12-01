# Options Communication

With this option, you can modify the communication settings for the terminal emulator.

![options_communication](options_communication.png)

Item | Description  
---|---  
Comport | The communication port of your PC that you use for the terminal emulator.  
Baud rate | The baud rate to use.  
Parity | Parity, default None.  
Data bits | Number of data bits, default 8.  
Stop bits | Number of stop bits, default 1.  
Handshake | The handshake used, default is none.  
Emulation | Emulation used, default TTY and VT100.  
Font | Font type and color used by the emulator.  
Back color | Background color of the terminal emulator.  
Keep TE open | This option will keep the terminal emulator COM port open when you close the window or move the focus away. Some serial programmers which close the COM port when they need to program, will not work in this mode when they use the same COM port.  
Use Existing COM ports | When you select this option, you will get a list with the available COM ports only at places you can select a COM port. When you insert an USB virtual COM port, it will be added to list automatically. Removing virtual COM ports will also update the available COM port list. When you do not select this option you get a list with COM1-COM255.  
  
Note that the baud rate of the terminal emulator and the baud rate setting of the [compiler options](options_compiler_communication.md), must be the same in order to work correctly.

The reason why you can specify them both to be different is that you can use the terminal emulator for other purposes too.