# $PROG

Action

Directive to auto program the lock and fuse bits.

Syntax old AVR

$PROG LB, FB , FBH , FBX

Syntax Xmega

$PROG LB, F0 , F1 , F2 , F3 ,F4 , F5

Remarks

While the lock and fuse bits make the AVR customizable, the settings for your project can give some problems.

The $PROG directive will create a file with the project name and the PRG extension.

Every time you program the chip, it will check the lock and fuse bit settings and will change them if needed.

So in a new chip, the lock and fuse bits will be set automatically. A chip that has been programmed with the desired settings will not be changed.

The programmer has an option to create the PRG file from the current chip settings.

The LB, FH, FBH and FBX values are stored in hexadecimal format in the PRJ file.

You may use any notation as long as it is a numeric constant.

Some chips might not have a setting for FBH or FBX, or you might not want to set all values. In that case, do NOT specify the value. For example:

$PROG &H20 ,,,

This will only write the Lockbit settings.

$PROG ,,&H30,

This will only write the FBH settings.

LB | Lockbit settings  
---|---  
FB | Fusebit settings  
FBH | Fusebit High settings  
FBX | Extended Fusebit settings  
  
Sometimes the data sheet refers to the Fusebit as the Fusebit Low settings.

The $PROG setting is only supported by the AVRISP, STK200/300, Sample Electronics and Universal MCS Programmer Interface. The USB-ISP programmer also supports the $PROG directive.

![notice](notice.jpg) When you select the wrong Fuse bit, you could lock your chip. For example when you choose the wrong oscillator option, it could mean that the micro expects an external crystal oscillator. But when you connect a simple crystal, it will not work.

In these cases where you can not communicate with the micro anymore, the advise is to apply a clock signal to X1 input of the micro.

You can then select the proper fuse bits again.

When you set the Lock bits, you can not read the chip content anymore. Only after erasing the chip, it could be reprogrammed again.

![important](important.jpg) Once the lock bits and fuse bits are set, it is best to remark the $PROG directive. This because it takes more time to read and compare the bits every time.

Xmega

The Xmega has one lock byte and 6 fuse bytes. For an Xmega the Write PRG option will write the correct code. 

Xtiny

The Xtiny has way more fuses and has a special CONFIG FUSES statement code. 

See also

[Programmers](supported_programmers.md) , [CONFIG FUSES](config_fuses.md) , [$PROGRAMMER](programmer.md)