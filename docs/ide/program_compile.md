# Program Compile

With this option, you compile your current program.

Your program will be saved automatically before being compiled.

The following files will be created depending on the [Option Compiler Settings.](options_compiler.md)

File | Description  
---|---  
xxx.BIN | Binary file which can be programmed into the microprocessor.  
xxx.DBG | Debug file that is needed by the simulator.  
xxx.OBJ | Object file for simulating using AVR Studio. Also needed by the internal simulator.  
xxx.HEX | Intel hexadecimal file, which is needed by some programmers.  
xxx.ERR | Error file. Only created when errors are found.  
xxx.RPT | Report file.  
xxx.EEP | EEPROM image file  
  
If a serious error occurs, you will receive an error message in a dialog box and the compilation will end.

All other errors will be displayed at the bottom of the edit window, just above the status bar.

When you click on the line with the error info, you will jump to the line that contains the error. The margin will also display the ![BASC0033_wmf](basc0033_wmf.gif)sign.

At the next compilation, the error window will disappear or reappear if there are still errors.

See also ['Syntax Check'](program_syntax_check.md) for further explanation of the Error window.

Program compile shortcut: ![BASC0034_wmf](basc0034_wmf.gif), F7