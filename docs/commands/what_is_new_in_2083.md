# What is new in 2083

For the Xtiny the following changes were made to 2083.008:

\- xtiny 8 pin chips set the wrong tx pin for config com. as a work around, you can define a portb alias that points to portA

\- printing a constant using the str() function : print str(number_constant) would include a leading space for positive numbers. Variables do not have 

this (VB behavior).

\- xtiny config xpin was missing the INVERTIO option in the DAT files.

\- passing a big string for which the size could not be determined, would not release space which would result in a quick crash. 

to determine the size of passed strings, you best declare with the size indicator like : someString as String * cSize

\- config spi0 for xtiny 202,402,212,412(8 pins) did not set the SS pin in the proper state. 

\- config vref was not described in the help

\- adc.bas sample added for xtiny

\- xtiny dat files updated for config adc and signature row offset adjusted. 

\- xtiny adc1 can also be configured now

\- xtiny renamed ACI to AC : config ac0. Also added ac1 and ac2

\- xtiny config dac1 and dac2 added.

\- xtiny config port_mux added.

\- xtiny SPI sample added

\- showing report in project mode inside the editor as a TAB did not set focus to the report.

\- xtiny dac.bas sample added

\- xtiny portmux.bas sample added

\- optional custom defined menu shortcuts added. See help : Options Environment

\- RESET MICRO added which will soft reset the micro. for xtiny/xmega a hardware soft reset is performed. For normal AVR a jump to the start address is 

performed. 

\- getadc can also read and process the internal temp sensor when you define a const named _adc_kelvin. The value is unimportant. see adc.bas example

\- multiple asm .def with different register but same name will give an error now since .defs are global. 

\- num2str for xtiny/xmega offset added to avoid str() causing problems when passed to a function

Public release

\- new option SAFE for variables. [Dim](dim.md) b as bit SAFE , see help.

\- added BOOTONLY option to [$LOADER](loader.md) directive. $loader bootaddress[,BOOTONLY] this will write just the boot loader code to the BIN file. The HEX remains as is.

\- you can select the [Options_Select_Settings_File](options_select_settings_file.md) now. This setting is stored in the registry.

\- project files are stored with absolute files names inside the prj file. An absolute file name is relative to the location. 

\- simulator bug fixed where SI file simulation data was not processed properly.

\- [MemFill](memfill.md) added. 

\- using instr() with {xxx} for the search string does not work : pos=instr(someAString,"{065}")

\- using compare_a/compare_b=clear for timer0 resulted in SET instead of CLEAR. 

\- bascomp command line utility updated to support new file structure

\- multiple instances bug fixed.

\- mcs.lbx was not in sync with mcs.lib (it was not compiled when a last minute change was made)

\- when using channel specifier without # you will get an error

\- stk500v2 based programmers like mkII and stk500v2 could give a program error when your code contains empty blocks And the processor has multiple 64KB segments. applies to normal mega only. 

\- [crc8](crc8.md) overloaded version added for big strings.

\- 2082 broke the default printing function

\- added DES asm instruction.

\- added [DesEncrypt](desencrypt.md) and [DesDecrypt](desdecrypt.md) which are also supported by the simulator

\- [inputbin](inputbin.md) accepts an optional variable for the number of bytes to receive. delimited by a ;

\- [simulator](program_simulate.md) update.

\- simulator double click cycles, will reset cycles

\- simulator allows to load a custom serial data file from file

\- [Xtiny](xtiny.md) support, requires a commercial add on

\- CTS/RTS bug fixed : only part of the buffer was used

\- added PA version of dat files M88PAdef,M644PAdef,M48PAdef,M168PA. These are almost the same as the P versions. They are binary compatible and have the same ID

\- searching in files would not search in the specified folder when the folder name contained a space. Instead the root folder was used.

\- $programmer option did not support conditional compilation. It was global. Now supports #IF/#ENDIF. but only when 'Use new method' is used in environment IDE options.

\- CLEAR serialinx buffer did not clear the RTS pin when cts/rts was used for xmega uarts 4-7. 

\- xmega high baud calculation > 2MB and higher did not support double rate flag resulting in a wrong baud rate

\- for next using a step for bytes could fail when the byte boundary was crossed.

\- xmega num2str code rewritten and xmega routine rewritten that used _XmegaFix_Rol_R1014 and _XMEGAFIX_CLEAR. These routines are not used anymore!

\- using a string function with select case, could result in improper branching, depending on the user function. 

select case mid(someString,start,len) for example. 

\- bascom-AVR and the SETUP are now code signed.

\- CONFIG XPIN for the E-series : slewrate will be set the whole port, not for an individual pin

\- [crc16uni](crc16uni.md) can handle 65535 bytes

\- low/high can be used as a procedure too for BASCOM-8051 compatibility.

\- UPDI programmer can write fuses

Please notice that this version has significant changes in order to support the Xtiny platform.

While everything was extensively tested, it is still possible you encounter a bug.

When you encounter a problem you did not had with 2082 you best contact support.