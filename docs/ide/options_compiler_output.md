# Options Compiler Output

![options_compiler_output](options_compiler_output.png)

Options Compiler Output

Item | Description  
---|---  
Binary file | Select to generate a binary file. (xxx.bin)  
Debug file | Select to generate a debug file (xxx.dbg)  
Hex file | Select to generate an Intel HEX file (xxx.hex)  
Report file | Select to generate a report file (xxx.rpt)  
Error file | Select to generate an error file (xxx.err)  
AVR Studio object file | Select to generate an AVR Studio object file (xxx.obj) Using the OBJ file you can debug with AVR Studio. This also allows to use tools like ICE. In Studio 6.0 (fixed in 6.1) you need to make these changes in Studio : Locate the file atmelstudio.pkgundef under the installation folder for Atmel. Studio. Remove (or remark) the below lines from the file and save the file.  [$RootKey$\Languages\Language Services\Basic] [$RootKey$\AutomationProperties\TextEditor\Basic]  
Size warning | Select to generate a warning when the code size exceeds the Flash ROM size.  
Swap words | This option will swap the bytes of the object code words. Useful for some programmers. Should be disabled for most programmers. Don't use it with the internal supported programmers.  
Optimize code | This options does additional optimization of the generated code. Since it takes more compile time it is an option.  
Show internal variables | Internal variables are used. Most of them refer to a register. Like _TEMP1 = R24. This option shows these variables in the report.