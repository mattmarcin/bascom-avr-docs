# $REGFILE

Action

Instruct the compiler to use the specified register file instead of the selected dat file.

Syntax

$REGFILE = "name"

Remarks

Name | The name of the register file. The register files are stored in the BASCOM-AVR application directory and they all have the DAT extension. The register file holds information about the chip such as the internal registers and interrupt addresses. The register file info is derived from atmel definition files.  
---|---  
  
The $REGFILE statement overrides the setting from the Options, Compiler, Chip menu.

The settings are stored in a <project>.CFG file.

The $REGFILE directive must be the first statement in your program. It may not be put into an included file since only the main source file is checked for the $REGFILE directive.

![notice](notice.jpg) It is good practice to use the $REGFILE directive. It has the advantage that you can see in the source which chip it was written for. The $REGFILE directive is also needed when the [PinOut](viewpinout.md) viewer or the [PDF](viewpdfviewer.md) viewer is used.

The register files contain the hardware register names from the micro. They also contain the bit names. These are constants that you may use in your program. But the names can not be used to dim a variable for example.

Example :

DIM PORTA As Byte

This will not work since PORTA is a register constant.

See also

[$SWSTACK](_swstack.md) , [$HWSTACK](_hwstack.md) , [$FRAMESIZE](_framesize.md), [Memory usage](memory_usage.md)

ASM

NONE

Example

$REGFILE = "8515DEF.DAT"