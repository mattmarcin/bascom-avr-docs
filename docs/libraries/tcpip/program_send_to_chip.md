# Program Send to Chip

Program send to chip shortcut ![BASC0058_wmf](basc0058_wmf.gif), F4

When you access the programmer from the main menu, you will notice the submenu. From the sub menu you can choose 'Program' or 'Manual Program'.

Program will erase and program the processor without any user intervention. 

Manual Program will only show the programmer window. You can manually choose the options to program the chip when the programmer supports it.

Auto Program also needs the option 'Auto Flash' to be set in the [Programmer options](options_programmer.md).

The following section applies to the Programmer window (program chip directly NOT selected) otherwise this is not shown to the user.

âBufferâ below refers to the buffer memory that holds data to be programmed to, or read from the chip.

Menu item | Description  
---|---  
File Exit | Return to editor  
File, Test | With this option you can set the logic level to the LPT pins. This is only intended for the Sample Electronics programmer.  
Buffer Clear | Clears buffer  
Buffer Load from file | Loads a file into the buffer  
Buffer Save to file | Saves the buffer content to a file  
Chip Identify | Identifies the chip  
Write buffer into chip | Programs the buffer into the chip ROM or EEPROM  
Read chip code into buffer | Reads the code or data from the chips code memory or data memory  
Chip blank check | Checks if the chip is blank or erased  
Chip erase | Erase the content of both the program memory and the data memory  
Chip verify | Verifies if the buffer is the same as the chip program or data memory  
Chip Set lock bits | Writes the selected lock bits LB1 and/or LB2. Only an erase will reset the lock bits  
Chip auto program | Erases the chip and programs the chip. After the programming is completed, verification is performed.  
  
The following window will be shown for most programmers:

![programmer](programmer.png)

Note that a chip must be ERASED before it can be programmed.

By default the Flash ROM TAB is shown and the binary data is displayed.

When you have an EEPROM in your project, the EEPROM TAB will show this data too.

The most important TAB is in many cases the Lock & Fuse Bits TAB.

When you select it , the lock and fuse bits will be read.

![programmer_LBFB](programmer_lbfb.png)

These Lock and Fuse bits are different in almost every chip !

You can select new settings and write them to the chip. But be careful ! When you select a wrong oscillator option , you can not program the chip anymore without applying an external clock signal.

This is also the solution to communicate with the chip again : connect a clock pulse to the oscillator input. You could use an output from a working micro, or a clock generator or simple 555 chip circuit.

When you found the right settings, you can use [$PROG](_prog.md) to write the proper settings to new, un-programmed chips. To get this setting you press the 'Write PRG' button.

After a new chip is programmed with $PROG, you should remark the line for safety and quicker programming.

The 'Write PRG' will write the settings, read from the Microprocessor, it will NOT insert the unsaved settings you have made manual. Thus, you must first use the 'Write XXX' buttons to write the changed fuse bits settings to the chip, then you can use the 'Write PRG'.

Notice that the Write xxx buttons are disabled by default. Only after you have changed a lock or fuse bit value, the corresponding button will be enabled. You must click this button in order to apply the new Lock or Fuse bit settings.

Many new chips have an internal oscillator. The default value is in most cases 8 MHz. But since in most cases the 'Divide by 8' option is also enabled, the oscillator value will be 1 MHz. We suggest to change the 'Divide by 8' fuse bit so you will have a speed of 8 MHz.

In your program you can use [$crystal](crystal_1.md) = 8000000 then.

![notice](notice.jpg)$crystal will only inform the compiler which oscillator speed you have selected. This is needed for a number of statements. $crystal will NOT set the speed of the oscillator itself.

![important](important.jpg) Do not change the fuse bit that will change the RESET to a port pin. Some chips have this option so you can use the reset pin as a normal port pin. While this is a great option it also means you can not program the chip anymore using the ISP.