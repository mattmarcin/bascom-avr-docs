# Options Programmer

With this option you can modify the programmer settings.

![options_programmer](options_programmer.png)

OPTION | DESCRIPTION  
---|---  
Programmer | Select one from the list.  
Play sound | Name of a WAV file to be played when programming is finished. Press the directory button to select a file.  
Erase Warning | Set this option when you want a confirmation when the chip is erased.  
Auto flash | Some programmers support auto flash. Pressing F4 will program the chip without showing the programmer window.  
Auto verify | Some programmers support verifying. The chip content will be verified after programming.  
Upload code and data | Set this option to program both the FLASH memory and the EEPROM memory  
Program after compile | When compilation is successful, the chip will be programmed  
Set focus to terminal emulator | When the chip is programmed, the terminal emulator will be shown  
|   
| Parallel printer port programmers  
LPT address | Port address of the LPT that is connected to the programmer.  
Port delay | An optional delay in uS. It should be 0. But on some systems a delay might be needed.  
|   
| Serial port programmer  
COM port | The com port the programmer is connected to.  
STK500 EXE | The path of stk500.exe. This is the full file location to the files stk500.exe that comes with the STK500.  
USB | For mkII and other Atmel USB programmers you can enter the serial number here. Or you can look it up from the list.  
Baud | Some serial programmers have an optional baud rate you can chose. The usual values are supported. When you want special custom baud rate you can replace the baud rate by creating a file named : progbaud.lst In this text file you can place all the baud rates. For example : 123 300 600 1200 2400 4800 9600 9610 19200 38400 57600 128000 256000 115200 500000 Then save the file. The file must reside in the bascom-avr application folder. The file is loaded when you run bascom. It will depend on your PC hardware/driver if the baud you use will actually work.   
|   
| Other  
Use HEX | Select when a HEX file must be sent instead of the bin file.  
Program | The program to execute. This is your programmer software.  
Parameter | The optional parameter that the program might need. Use {FILE} to insert the binary filename(file.bin) and {EEPROM} to insert the filename of the generated EEP file. When âUse Hexâ is checked the filename (file.hex) will be inserted for {FILE}. In all cases a binary file will be inserted for {EEPROM} with the extension .EEP Use {CHIP} to insert the official device name of the chip. The device name is required by some programmers.  
  
See Also

[Supported programmers](supported_programmers.md)