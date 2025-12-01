# Tools LIB Manager

With this option the following window will appear:

![lib_manager](lib_manager.png)

The Libraries are shown in the left pane. When you select a library, the routines that are in the library will be shown in the right pane.

After selecting a routine in the left pane, you can DELETE it with the DELETE button..

Clicking the ADD button allows you to add an ASM routine to the library. The ADD Paste button will add a routine from the clipboard instead of a file on disk.

The COMPILE button will compile the lib into an LBX file. When an error occurs you will get an error. By watching the content of the generated lbx file you can determine the error.

A compiled LBX file does not contain comments and a huge amount of mnemonics are compiled into object code. This object code is inserted at compile time of the main BASIC program. This results in faster compilation time.

The DEMO version comes with the compiled MCS.LIB file which is named MCS.LBX. The ASM source (MCS.LIB) is included only with the commercial edition.

With the ability to create LBX files you can create add on packages for BASCOM and sell them. For example, the LBX files could be distributed for free, and the ASM source could be sold.

Some library examples :

•| MODBUS crc routine for the modbus slave program.  
---|---  
  
•| Glcd.lib contains the graphical LCD asm code  
---|---  
  
Commercial packages available from MCS:

•| I2CSLAVE library  
---|---  
  
•| BCCARD for communication with www.basiccard.com chipcards  
---|---  
  
See Also

[$LIB](lib.md) for writing your own libraries