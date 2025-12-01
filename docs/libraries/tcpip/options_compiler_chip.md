# Options Compiler Chip

![BASC0062](basc0062.gif)

The following options are available:

Options Compiler Chip

Item | Description  
---|---  
Chip | Selects the target chip. Each chip has a corresponding x.DAT file with specifications of the chip. Note that some DAT files are not available yet.  
XRAM | Selects the size of the external RAM. KB means Kilo Bytes. For 32 KB you need a 62256 STATIC RAM chip.  
HW Stack | The amount of bytes available for the hardware stack. When you use GOSUB or CALL, you are using 2 bytes of HW stack space. When you nest 2 GOSUBâs you are using 4 bytes (2*2). Most statements need HW stack too. An interrupt needs 32 bytes.  
Soft Stack | Specifies the size of the software stack. Each local variable uses 2 bytes. Each variable that is passed to a sub program uses 2 bytes too. So when you have used 10 locals in a SUB and the SUB passes 3 parameters, you need 13 * 2 = 26 bytes.  
Frame size | Specifies the size of the frame. Each local variable is stored in a space that is named the frame space. When you have 2 local integers and a string with a length of 10, you need a frame size of (2*2) + 11 = 15 bytes. The internal conversion routines used when you use INPUT num, or STR(), or VAL(), etc, also use the frame. They need a maximum of 16 bytes. So for this example 15+16 = 31 would be a good value.  
XRAM wait state | Select to insert a wait state for the external RAM.  
External Access enable | Select this option to allow external access of the micro. The 8515 for example can use port A and C to control a RAM chip. This is almost always selected if XRAM is used  
Default | Press or click this button to use the current Compiler Chip settings as default for all new projects.