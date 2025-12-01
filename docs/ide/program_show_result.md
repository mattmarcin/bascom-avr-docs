# Program Show Result

Use this option to view information concerning the result of the compilation.

See the [Options Compiler Output](options_compiler_output.md) for specifying which files will be created.

The files that can be viewed are "report" and "error".

File show result shortcut : ![BASC0036_wmf](basc0036_wmf.gif),CTRL+W

Information provided in the report:

Info | Description  
---|---  
Report | Name of the program  
Date and time | The compilation date and time.  
Compiler | The version of the compiler.  
Processor | The selected target processor.  
SRAM | Size of microprocessor SRAM (internal RAM).  
EEPROM | Size of microprocessor EEPROM (internal EEPROM).  
ROMSIZE | Size of the microprocessor FLASH ROM.  
ROMIMAGE | Size of the compiled program.  
BAUD | Selected baud rate.  
XTAL | Selected XTAL or frequency.  
BAUD error | The error percentage of the baud rate.  
XRAM | Size of external RAM if available.  
Stack start | The location in memory, where the hardware stack points to. The HW-stack pointer grows downward.  
S-Stacksize | The size of the software stack.  
S-Stackstart | The location in memory where the software stack pointer points to. The software stack pointer grows downward.  
Framesize | The size of the frame. The frame is used for storing local variables.  
Framestart | The location in memory where the frame starts.  
LCD address | The address that must be placed on the bus to enable the LCD display E-line.  
LCD RS | The address that must be placed on the bus to enable the LCD RS-line  
LCD mode | The mode the LCD display is used with. 4 bit mode or 8 bit mode.  
LCD DB7-DB4 | The port pins used for controlling the LCD in pin mode.  
LCD E | The port pin used to control the LCD enable line.  
LCD RS | The port pin used to control the LCD RS line.  
Variable | The variable name and address in memory  
Constant | Constants name and value Some internal constants are : _CHIP : number that identifies the selected chip _RAMSIZE : size of SRAM _ERAMSIZE : size of EEPROM _XTAL : value of crystal _BUILD : number that identifies the version of the compiler _COMPILER : number that identifies the platform of the compiler  
Warnings | This is a list with variables that are dimensioned but not used. Some of them  
EEPROM binary image map | This is a list of all ERAM variables with their value. It is only shown when [DATA](data_2.md) lines are used to create the EEP file. (EEPROM binary image).  
  
When the option : Load Report in IDE, is set, the report will be shown as a text file in the IDE.